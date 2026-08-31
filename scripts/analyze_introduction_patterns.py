from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_CACHE = ROOT / "outputs" / "text_cache"
PAPER_MATRIX = ROOT / "outputs" / "paper_matrix.csv"
RAW_METADATA = ROOT / "outputs" / "raw_metadata" / "papers_with_pdf_status.json"
OUT_REPORT = ROOT / "outputs" / "introduction_pattern_report.md"
OUT_CSV = ROOT / "outputs" / "introduction_pattern_sources.csv"


SIGNALS = {
    "rehab_context": [
        "rehabilitation",
        "stroke",
        "mobility",
        "walking ability",
        "gait training",
        "motor function",
    ],
    "assistive_need": [
        "assist",
        "assistance",
        "restore",
        "augment",
        "reduce effort",
        "metabolic",
        "muscle activity",
        "fatigue",
    ],
    "control_backbone": [
        "impedance",
        "admittance",
        "torque control",
        "pd control",
        "dynamic movement primitive",
        "dmp",
        "trajectory",
    ],
    "personalization_gap": [
        "personalized",
        "individual",
        "user-specific",
        "subject-specific",
        "tuning",
        "manual tuning",
        "parameter",
        "adaptation",
    ],
    "ai_optimizer": [
        "human-in-the-loop",
        "human in the loop",
        "bayesian optimization",
        "cma-es",
        "covariance matrix adaptation",
        "reinforcement learning",
        "machine learning",
    ],
    "sensing_state": [
        "gait phase",
        "gait event",
        "intent",
        "ground contact",
        "foot pressure",
        "imu",
        "emg",
    ],
    "safety_deployment": [
        "real-time",
        "safety",
        "safe",
        "constraint",
        "bounded",
        "wearable",
        "portable",
        "closed-loop",
    ],
    "contribution_marker": [
        "this paper",
        "this study",
        "we propose",
        "we present",
        "we develop",
        "we evaluate",
        "our contribution",
    ],
}


@dataclass
class IntroRecord:
    source_id: str
    title: str
    year: str
    doi: str
    path: str
    words: int
    signals: dict[str, int]
    intro: str


def load_matrix() -> dict[str, dict[str, str]]:
    if not PAPER_MATRIX.exists():
        return {}
    rows: dict[str, dict[str, str]] = {}
    with PAPER_MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            title = (row.get("title") or "").strip()
            if title:
                rows[normalize_title(title)] = row
    return rows


def matrix_row_count() -> int:
    if not PAPER_MATRIX.exists():
        return 0
    with PAPER_MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def load_metadata_by_id() -> dict[str, dict[str, str]]:
    if not RAW_METADATA.exists():
        return {}
    papers = json.loads(RAW_METADATA.read_text(encoding="utf-8"))
    result: dict[str, dict[str, str]] = {}
    for paper in papers:
        doi = (paper.get("doi") or "").strip().lower()
        key = doi or f"{paper.get('title','')} {paper.get('year','')}".lower()
        import hashlib

        pid = hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]
        result[pid] = paper
        text_path = paper.get("text_cache_path")
        if text_path:
            result[Path(text_path).stem] = paper
    return result


def normalize_title(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def title_from_text(text: str, fallback: str) -> str:
    lines = [clean_line(x) for x in text.splitlines()[:80]]
    candidates = [
        line
        for line in lines
        if 8 <= len(line) <= 180
        and not line.lower().startswith(("--- page", "abstract", "keywords", "received", "accepted", "published"))
        and len(line.split()) >= 4
    ]
    if candidates:
        return candidates[0]
    return fallback


def clean_line(value: str) -> str:
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def normalize_body(text: str) -> str:
    text = re.sub(r"\n\s*--- page \d+ ---\s*\n", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"-\s*\n\s*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_intro(text: str) -> str:
    flat = normalize_body(text)
    lower = flat.lower()

    starts = []
    for pattern in [
        r"\b1\.?\s+introduction\b",
        r"\bi\.?\s+introduction\b",
        r"\bintroduction\b",
        r"\b1\s+绪论\b",
        r"\b引言\b",
    ]:
        m = re.search(pattern, lower)
        if m:
            starts.append(m.start())
    if not starts:
        return ""
    start = min(starts)

    end_candidates = []
    for pattern in [
        r"\b2\.?\s+[a-z][a-z\s-]{3,60}\b",
        r"\bii\.?\s+[a-z][a-z\s-]{3,60}\b",
        r"\bmethods?\b",
        r"\bmaterials and methods\b",
        r"\brelated work\b",
        r"\bbackground\b",
        r"\bsystem overview\b",
        r"\bmethodology\b",
        r"\b2\s+",
        r"\b二、",
    ]:
        m = re.search(pattern, lower[start + 300 :])
        if m:
            end_candidates.append(start + 300 + m.start())
    end = min(end_candidates) if end_candidates else start + 8000
    intro = flat[start:end]
    words = intro.split()
    if len(words) < 120:
        intro = flat[start : start + 8000]
    return intro[:9000]


def count_signals(intro: str) -> dict[str, int]:
    low = intro.lower()
    return {
        name: sum(1 for term in terms if term in low)
        for name, terms in SIGNALS.items()
    }


def sentence_samples(intros: list[IntroRecord], category: str, limit: int = 6) -> list[str]:
    samples = []
    terms = SIGNALS[category]
    for rec in sorted(intros, key=lambda r: r.signals.get(category, 0), reverse=True):
        sentences = re.split(r"(?<=[.!?。！？])\s+", rec.intro)
        for sent in sentences:
            low = sent.lower()
            if any(term in low for term in terms) and 18 <= len(sent.split()) <= 55:
                samples.append(f"- {rec.title}: {sent.strip()}")
                break
        if len(samples) >= limit:
            break
    return samples


def classify_arc(rec: IntroRecord) -> str:
    s = rec.signals
    if s["ai_optimizer"] and s["personalization_gap"] and s["control_backbone"]:
        return "personalization -> control parameters -> optimizer"
    if s["rehab_context"] and s["control_backbone"] and s["safety_deployment"]:
        return "rehabilitation need -> control backbone -> deployability"
    if s["sensing_state"] and s["control_backbone"]:
        return "sensing/state estimation -> control synchronization"
    if s["assistive_need"] and s["personalization_gap"]:
        return "assistance benefit -> individual tuning gap"
    if s["control_backbone"]:
        return "controller capability -> remaining control gap"
    return "general background -> proposed method"


def main() -> None:
    matrix = load_matrix()
    matrix_records = matrix_row_count()
    metadata_by_id = load_metadata_by_id()
    records: list[IntroRecord] = []
    matrix_cache_paths: list[Path] = []
    seen_paths: set[Path] = set()
    for meta in metadata_by_id.values():
        text_path = meta.get("text_cache_path")
        if not text_path:
            continue
        path = (ROOT / text_path).resolve()
        if path in seen_paths or not path.is_file():
            continue
        seen_paths.add(path)
        matrix_cache_paths.append(path)

    for path in sorted(matrix_cache_paths):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        intro = extract_intro(text)
        if not intro:
            continue
        meta = metadata_by_id.get(path.stem, {})
        fallback_title = re.sub(r"_[0-9a-f]{12}$", "", path.stem).replace("_", " ")
        title = title_from_text(text, fallback_title)
        norm = normalize_title(title)
        row = meta or matrix.get(norm, {})
        signals = count_signals(intro)
        records.append(
            IntroRecord(
                source_id=path.stem,
                title=row.get("title") or title,
                year=row.get("year") or "",
                doi=row.get("doi") or "",
                path=str(path.relative_to(ROOT)),
                words=len(intro.split()),
                signals=signals,
                intro=intro,
            )
        )

    category_counts = Counter()
    arc_counts = Counter()
    examples_by_arc: dict[str, list[IntroRecord]] = defaultdict(list)
    for rec in records:
        for category, count in rec.signals.items():
            if count:
                category_counts[category] += 1
        arc = classify_arc(rec)
        arc_counts[arc] += 1
        examples_by_arc[arc].append(rec)

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        fields = ["source_id", "title", "year", "doi", "path", "words", "arc", *SIGNALS.keys()]
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for rec in records:
            writer.writerow(
                {
                    "source_id": rec.source_id,
                    "title": rec.title,
                    "year": rec.year,
                    "doi": rec.doi,
                    "path": rec.path,
                    "words": rec.words,
                    "arc": classify_arc(rec),
                    **rec.signals,
                }
            )

    lines = [
        "# 引言写法模式分析报告",
        "",
        "本报告仅基于本地 PDF 文本缓存生成。脚本用启发式规则抽取类似 Introduction 的段落，并总结这些论文常用的引言写作动作；它是写作规划辅助材料，不等同于已经逐条核验引用的文献综述。",
        "",
        f"- 文本缓存目录文件总数（含历史/重复缓存）：{len(list(TEXT_CACHE.glob('*.txt')))}",
        f"- 当前矩阵记录数：{matrix_records}",
        f"- 矩阵关联且可读取的文本缓存数：{len(matrix_cache_paths)}",
        f"- 成功抽取的引言-like 段落数：{len(records)}",
        f"- 来源表：`outputs/introduction_pattern_sources.csv`",
        "",
        "## 高频写作动作",
        "",
    ]
    move_names = {
        "rehab_context": "从康复/移动能力需求切入",
        "assistive_need": "解释为什么需要外骨骼辅助",
        "control_backbone": "介绍已有控制底座",
        "personalization_gap": "把问题转化为个体化/参数调节问题",
        "ai_optimizer": "引入 AI/优化作为自适应机制",
        "sensing_state": "用传感/状态估计支撑同步控制",
        "safety_deployment": "强调实时、安全、可部署约束",
        "contribution_marker": "最后明确本文贡献",
    }
    for category, label in move_names.items():
        lines.append(f"- {label}：{category_counts[category]} 篇引言")

    lines.extend(["", "## 常见论证路径", ""])
    arc_zh = {
        "personalization -> control parameters -> optimizer": "个体化需求 -> 控制参数 -> 优化器",
        "rehabilitation need -> control backbone -> deployability": "康复需求 -> 控制底座 -> 实时/安全部署",
        "sensing/state estimation -> control synchronization": "传感/状态估计 -> 控制同步",
        "assistance benefit -> individual tuning gap": "辅助收益 -> 个体差异/调参缺口",
        "controller capability -> remaining control gap": "已有控制能力 -> 尚未解决的控制缺口",
        "general background -> proposed method": "一般背景 -> 提出方法",
    }
    for arc, count in arc_counts.most_common():
        examples = examples_by_arc[arc][:3]
        names = "; ".join(e.title[:90] for e in examples)
        lines.append(f"- {arc_zh.get(arc, arc)}：{count} 篇。例子：{names}")

    lines.extend(
        [
            "",
            "## 可迁移到本项目的引言模板",
            "",
            "1. 临床/辅助需求：膝关节外骨骼可用于步态康复与行走辅助，但实际收益依赖人与外骨骼之间是否同步、舒适且安全。",
            "2. 现有工程基础：DMP 轨迹生成结合阻抗/PD 力矩控制具有可解释、低维、实时可部署等优势，适合 Simulink/Speedgoat 控制链路。",
            "3. 核心限制：辅助效果对 `Amplitude`、`tau`、`phase_offset`、`MO_Kp`、`MO_Kd` 等参数敏感；人工调参难以覆盖不同个体和不同步态状态。",
            "4. 文献过渡：HIL optimization、Bayesian optimization、CMA-ES、步态相位估计和自适应阻抗控制说明，学习方法可以用于个性化辅助；但很多工作没有把 AI 插入点明确映射到一个带安全边界的 DMP-阻抗实现中。",
            "5. 研究缺口：对于准直驱膝关节外骨骼，缺少的不是端到端实时力矩策略，而是在实时控制环外运行的低频参数自适应层；该层必须服从 `Torque_Guard`、`SafeTorque` 和饱和限幅。",
            "6. 本文目标：将 AI 表述为 DMP/阻抗参数的有界优化器，利用 `Phi`、`Phase0Event`、`FeetLoad`、`q_meas`、`dq_meas`、`tau_e` 等本地信号构造目标函数或评价指标。",
            "7. 本文贡献：说明系统框架、优化参数集合、目标/安全约束，以及实验或验证流程。",
            "",
            "## 可模仿的句式类型",
            "",
            "### 个体化 / 调参缺口",
            "",
        ]
    )
    lines.extend(sentence_samples(records, "personalization_gap"))
    lines.extend(["", "### 控制底座", ""])
    lines.extend(sentence_samples(records, "control_backbone"))
    lines.extend(["", "### AI / 优化器过渡", ""])
    lines.extend(sentence_samples(records, "ai_optimizer"))
    lines.extend(["", "### 安全 / 部署约束", ""])
    lines.extend(sentence_samples(records, "safety_deployment"))
    lines.extend(
        [
            "",
            "## 注意事项",
            "",
            "- 抽取片段可能包含 OCR 或 PDF 解析噪声。",
            "- 不建议直接照抄这些句子；重点学习其论证顺序和段落功能。",
            "- 最终写进论文的引用性判断，必须回到 PDF 或元数据逐条核验。",
        ]
    )
    OUT_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"matrix={matrix_records} matrix_texts={len(matrix_cache_paths)} introductions={len(records)}")
    print(f"wrote={OUT_REPORT.relative_to(ROOT)}")
    print(f"wrote={OUT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
