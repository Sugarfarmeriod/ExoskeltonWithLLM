from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import textwrap
import time
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
RAW = OUTPUTS / "raw_metadata"
NOTES = ROOT / "notes"
PAPERS = ROOT / "papers"
INBOX = PAPERS / "inbox"
TEXTS = OUTPUTS / "pdf_text"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0 Safari/537.36 ExoskeletonWithLLM/0.1"
)

FIELDS = [
    "title",
    "year",
    "venue",
    "doi",
    "pdf_status",
    "ai_role",
    "control_base",
    "optimized_parameters",
    "objective",
    "sensors",
    "subjects",
    "metrics",
    "semantic_input_type",
    "semantic_output_type",
    "robot_closed_loop",
    "parameter_mapping",
    "implementation_difficulty",
    "quick_paper_fit",
    "relevance_score",
    "why_relevant",
]

MANUAL_FIELDS = ["title", "doi", "publisher_url", "reason_failed", "suggested_filename"]

PRIORITY_KEYWORDS = {
    "human-in-the-loop": 18,
    "human in the loop": 18,
    "bayesian optimization": 18,
    "cma-es": 16,
    "covariance matrix adaptation": 16,
    "impedance": 12,
    "dynamic movement primitive": 12,
    "dmp": 12,
    "exoskeleton": 10,
    "wearable robot": 9,
    "knee": 8,
    "gait phase": 8,
    "gait state": 8,
    "ground contact": 8,
    "intent": 7,
    "adaptive": 7,
    "co-adaptive": 8,
    "multi-agent": 6,
    "reinforcement learning": 7,
    "musculoskeletal": 5,
    "hip exoskeleton": 5,
    "stroke": 6,
    "gait symmetry": 6,
    "metabolic": 5,
    "therapist input": 4,
    "clinical instruction": 4,
    "high-level input": 4,
    "natural language": 4,
    "semantic": 4,
    "shared control": 5,
    "intent-based control": 5,
}

LOW_PRIORITY = {
    "pure vision": -8,
    "mechanical design": -8,
    "finite element": -8,
    "medical chatbot": -18,
    "patient chatbot": -18,
    "medical question answering": -18,
    "rehabilitation advice": -14,
    "chatgpt": -10,
    "large language model": -6,
}

SEMANTIC_TERMS = [
    "therapist input",
    "clinical instruction",
    "high-level input",
    "natural language",
    "large language model",
    "llm",
    "semantic",
    "shared control",
    "intent-based control",
]

CONTROL_MAPPING_TERMS = [
    "trajectory",
    "torque",
    "impedance",
    "stiffness",
    "damping",
    "phase",
    "gait",
    "mode switching",
    "assistance",
    "safety",
    "constraint",
    "parameter",
]


def ensure_dirs() -> None:
    for path in [OUTPUTS, RAW, NOTES, PAPERS, INBOX, TEXTS]:
        path.mkdir(parents=True, exist_ok=True)


def read_queries() -> list[str]:
    qfile = ROOT / "queries.md"
    if not qfile.exists():
        return []
    return [
        line.strip()
        for line in qfile.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        value = " ".join(str(v) for v in value if v)
    value = re.sub(r"<[^>]+>", " ", str(value))
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def normalize_doi(doi: str | None) -> str:
    doi = clean_text(doi).lower()
    doi = doi.replace("https://doi.org/", "").replace("http://dx.doi.org/", "")
    return doi.strip().strip(".")


def slugify(value: str, max_len: int = 90) -> str:
    value = re.sub(r"[^\w\s.-]", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "_", value.strip())
    value = value.strip("._")
    return (value or "untitled")[:max_len]


def paper_id(paper: dict[str, Any]) -> str:
    doi = normalize_doi(paper.get("doi"))
    key = doi or f"{paper.get('title','')} {paper.get('year','')}".lower()
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


def suggested_pdf_name(paper: dict[str, Any]) -> str:
    year = str(paper.get("year") or "unknown")
    title = slugify(clean_text(paper.get("title")), 70)
    doi = slugify(normalize_doi(paper.get("doi")).replace("/", "_"), 40)
    stem = "_".join(part for part in [year, title, doi] if part)
    return f"{stem}.pdf"


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Accept": "application/pdf,application/json,text/html,*/*",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        }
    )
    return s


def text_blob(paper: dict[str, Any], full_text: str = "") -> str:
    return " ".join(
        clean_text(paper.get(k)) for k in ["title", "abstract", "venue", "keywords", "query"]
    ).lower() + " " + full_text[:16000].lower()


def is_semantic_direction(blob: str) -> bool:
    return any(term in blob for term in SEMANTIC_TERMS)


def has_control_mapping(blob: str) -> bool:
    return any(term in blob for term in CONTROL_MAPPING_TERMS)


def is_pure_llm_or_chatbot(blob: str) -> bool:
    chatbot = any(term in blob for term in ["chatbot", "question answering", "medical advice", "patient education"])
    llm = any(term in blob for term in ["llm", "large language model", "chatgpt", "natural language"])
    robot_control = any(term in blob for term in ["robot", "exoskeleton", "control", "trajectory", "torque", "rehabilitation robot"])
    return (chatbot or llm) and not robot_control


def score_paper(paper: dict[str, Any]) -> tuple[int, str]:
    blob = text_blob(paper)
    score = 0
    hits = []
    for kw, pts in PRIORITY_KEYWORDS.items():
        if kw in blob:
            score += pts
            hits.append(kw)
    for kw, pts in LOW_PRIORITY.items():
        if kw in blob:
            score += pts
            hits.append(f"low:{kw}")
    if "exoskeleton" in blob and ("bayesian optimization" in blob or "human-in-the-loop" in blob):
        score += 12
        hits.append("core:optimizer")
    if "dmp" in blob and ("impedance" in blob or "reinforcement learning" in blob):
        score += 8
        hits.append("core:dmp")
    if "knee" in blob and "impedance" in blob:
        score += 5
        hits.append("core:knee_impedance")
    if is_semantic_direction(blob):
        if has_control_mapping(blob):
            score += 7
            hits.append("semantic_control_mapping")
        else:
            score -= 6
            hits.append("semantic_weak_mapping")
    if is_pure_llm_or_chatbot(blob):
        score -= 25
        hits.append("reject:pure_llm_chatbot")
    if re.search(r"\b(?:emg|electromyograph\w*)\b", blob):
        score -= 8
        hits.append("scope:emg_method_reference_only")
    if re.search(r"\bimu\b|inertial measurement unit", blob):
        score -= 8
        hits.append("scope:imu_method_reference_only")
    return max(score, 0), "; ".join(hits[:14])


def classify_semantic(blob: str) -> dict[str, str]:
    if "natural language" in blob or "llm" in blob or "large language model" in blob:
        semantic_input_type = "natural language / LLM"
    elif "therapist" in blob or "clinical instruction" in blob:
        semantic_input_type = "therapist instruction / clinical goal"
    elif "shared control" in blob or "button" in blob or "interface" in blob or "gui" in blob:
        semantic_input_type = "GUI/button/shared-control interface"
    else:
        semantic_input_type = "not semantic / not reported"

    outputs = []
    if "parameter" in blob or "stiffness" in blob or "damping" in blob:
        outputs.append("control/impedance parameters")
    if "trajectory" in blob or "gait" in blob:
        outputs.append("trajectory or gait features")
    if "mode" in blob or "task" in blob or "intent" in blob:
        outputs.append("mode switching / intent")
    if "text" in blob and not outputs:
        outputs.append("text feedback only")

    if "experiment" in blob and any(term in blob for term in ["robot", "exoskeleton", "device"]):
        robot_closed_loop = "yes/likely"
    elif any(term in blob for term in ["simulation", "simulated"]):
        robot_closed_loop = "simulation only"
    else:
        robot_closed_loop = "not confirmed"

    mappings = []
    if "amplitude" in blob or "magnitude" in blob or "torque" in blob or "assistance" in blob:
        mappings.append("Amplitude / assistive torque / SafeTorque")
    if "phase" in blob or "timing" in blob or "onset" in blob:
        mappings.append("phase_offset / Phi / Phase0Event")
    if "duration" in blob or "speed" in blob or "frequency" in blob:
        mappings.append("tau")
    if "stiffness" in blob or "damping" in blob or "impedance" in blob:
        mappings.append("MO_Kp / MO_Kd / MO_OverwriteKpGain")
    if "safety" in blob or "constraint" in blob:
        mappings.append("SafeTorque / safety constraints")

    if not is_semantic_direction(blob):
        difficulty = "not applicable"
        quick_fit = "not semantic route"
    elif mappings and robot_closed_loop == "yes/likely":
        difficulty = "medium"
        quick_fit = "secondary angle only"
    elif mappings:
        difficulty = "medium"
        quick_fit = "future extension"
    else:
        difficulty = "high"
        quick_fit = "not suitable for 1-2 month main paper"

    return {
        "semantic_input_type": semantic_input_type,
        "semantic_output_type": ", ".join(outputs) or "not reported",
        "robot_closed_loop": robot_closed_loop,
        "parameter_mapping": ", ".join(mappings) or "no direct mapping confirmed",
        "implementation_difficulty": difficulty,
        "quick_paper_fit": quick_fit,
    }


def classify_paper(paper: dict[str, Any], full_text: str = "") -> dict[str, str]:
    blob = text_blob(paper, full_text)

    def has(*terms: str) -> bool:
        return any(term in blob for term in terms)

    if has("bayesian optimization", "human-in-the-loop", "human in the loop", "cma-es", "covariance matrix adaptation"):
        ai_role = "参数优化器"
    elif has("gait phase", "gait state", "ground contact", "load estimation", "intent recognition", "intent estimation"):
        ai_role = "状态估计器"
    elif has("dynamic movement primitive", "dmp", "trajectory generation", "reinforcement learning"):
        ai_role = "轨迹生成器/学习器"
    elif has("impedance control", "adaptive impedance", "admittance"):
        ai_role = "控制器/阻抗自适应"
    elif is_semantic_direction(blob):
        ai_role = "高层语义/治疗师输入接口"
    else:
        ai_role = "待人工确认"

    control_base = []
    if has("impedance"):
        control_base.append("impedance control")
    if has("dmp", "dynamic movement primitive"):
        control_base.append("DMP")
    if has("pd control", "torque control"):
        control_base.append("PD/torque control")
    if has("bayesian optimization", "cma-es", "human-in-the-loop"):
        control_base.append("low-frequency optimizer")
    if is_semantic_direction(blob):
        control_base.append("high-level interface")

    params = []
    if has("timing", "phase", "onset"):
        params.append("助力时机/phase_offset")
    if has("magnitude", "amplitude", "peak torque", "torque profile", "assistance"):
        params.append("助力强度/Amplitude/torque profile")
    if has("stiffness", "damping", "impedance"):
        params.append("MO_Kp/MO_Kd/阻抗参数")
    if has("tau", "duration", "speed", "frequency"):
        params.append("tau/持续时间")

    objective = []
    if has("metabolic"):
        objective.append("metabolic cost")
    if has("emg"):
        objective.append("EMG reduction/activity")
    if has("symmetry", "asymmetry"):
        objective.append("gait symmetry")
    if has("interaction torque", "interaction force"):
        objective.append("interaction torque/force")
    if has("rmse"):
        objective.append("RMSE")
    if has("comfort"):
        objective.append("comfort score")
    if has("stability"):
        objective.append("stability")
    if has("safety", "constraint"):
        objective.append("safety constraint")

    sensors = []
    if has("inertial", "imu"):
        sensors.append("IMU")
    if has("force sensor", "load", "ground reaction", "pressure", "foot"):
        sensors.append("足底压力/力传感")
    if has("encoder", "joint angle", "knee angle"):
        sensors.append("膝角度")
    if has("velocity", "angular velocity"):
        sensors.append("膝速度")
    if has("torque"):
        sensors.append("膝力矩/交互力矩")
    if has("emg"):
        sensors.append("EMG")
    if is_semantic_direction(blob):
        sensors.append("治疗师/语义输入")

    subjects = "未从摘要确认"
    m = re.search(r"(\d+)\s+(healthy|subjects|participants|patients|individuals|stroke)", blob)
    if m:
        subjects = m.group(0)
    elif has("stroke"):
        subjects = "stroke participants/patients（数量待查 PDF）"
    elif has("healthy"):
        subjects = "healthy participants（数量待查 PDF）"

    semantic = classify_semantic(blob)
    why = []
    if ai_role == "参数优化器":
        why.append("最贴近低频优化 DMP/阻抗参数的接入方式")
    if ai_role == "状态估计器":
        why.append("可增强 AO/Phi/Phase0Event 或足底负重/意图估计")
    if "impedance control" in control_base:
        why.append("可映射到 MO_Kp/MO_Kd")
    if any("phase" in p for p in params):
        why.append("可映射到 AO/Phi/Phase0Event 与 phase_offset")
    if any("Amplitude" in p or "torque" in p for p in params):
        why.append("可映射到 DMP Amplitude 和 SafeTorque 约束")
    if is_semantic_direction(blob):
        if semantic["parameter_mapping"] != "no direct mapping confirmed":
            why.append("语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器")
        else:
            why.append("语义方向缺少到控制参数的直接映射，只适合相关工作/未来展望")
    if is_pure_llm_or_chatbot(blob):
        why.append("纯 LLM/聊天问答，不进入核心控制文献")
    if "EMG" in sensors or "IMU" in sensors:
        why.append("涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板")
    if not why:
        why.append("与外骨骼 AI 控制相关，但需要全文确认可接入性")

    result = {
        "ai_role": ai_role,
        "control_base": ", ".join(control_base) or "待确认",
        "optimized_parameters": ", ".join(params) or "待确认",
        "objective": ", ".join(objective) or "待确认",
        "sensors": ", ".join(sensors) or "待确认",
        "subjects": subjects,
        "metrics": ", ".join(objective) or "待从 PDF/全文确认",
        "why_relevant": "；".join(why),
    }
    result.update(semantic)
    return result


def pdf_status_for(paper: dict[str, Any]) -> str:
    pdf_path = clean_text(paper.get("pdf_path"))
    status = clean_text(paper.get("pdf_status"))
    if pdf_path and Path(pdf_path).is_file():
        if status in {"open_access_pdf", "institution_access_pdf", "manual_pdf"}:
            return status
        return "manual_pdf"
    return "abstract_only" if clean_text(paper.get("abstract")) else "metadata_only"


def note_filename(paper: dict[str, Any]) -> Path:
    year = str(paper.get("year") or "unknown")
    title = slugify(clean_text(paper.get("title")), 70)
    return NOTES / f"{year}_{title}_{paper_id(paper)}.md"


def is_probably_pdf(resp: requests.Response) -> bool:
    ctype = resp.headers.get("content-type", "").lower()
    return "pdf" in ctype or resp.content[:5] == b"%PDF-"


def looks_like_blocked(resp: requests.Response) -> str:
    text = resp.text[:3000].lower() if "text" in resp.headers.get("content-type", "").lower() else ""
    if resp.status_code in {401, 403}:
        return f"HTTP {resp.status_code}"
    for token in ["login", "captcha", "cloudflare", "shibboleth", "institution", "sso", "access denied"]:
        if token in text:
            return f"blocked_or_auth_page:{token}"
    return ""


def publisher_url(paper: dict[str, Any]) -> str:
    doi = normalize_doi(paper.get("doi"))
    if doi:
        return f"https://doi.org/{doi}"
    return clean_text(paper.get("url"))


def copy_manual_pdf(src: Path, paper: dict[str, Any] | None = None) -> Path:
    name = suggested_pdf_name(paper) if paper else slugify(src.stem, 100) + ".pdf"
    dest = PAPERS / name
    idx = 1
    while dest.exists():
        dest = PAPERS / f"{dest.stem}_{idx}.pdf"
        idx += 1
    shutil.move(str(src), str(dest))
    return dest


def wrap_md(text: str, width: int = 100) -> str:
    text = clean_text(text)
    if not text:
        return "未提供。"
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False))


def polite_sleep(seconds: float = 0.2) -> None:
    time.sleep(seconds)
