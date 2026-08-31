from __future__ import annotations

import csv
from pathlib import Path

from pipeline_utils import (
    MANUAL_FIELDS,
    PAPERS,
    RAW,
    clean_text,
    ensure_dirs,
    is_probably_pdf,
    load_json,
    normalize_doi,
    save_json,
    score_paper,
    session,
    write_csv,
)


REFERENCES = [
    {
        "category": "llm_rehab_interface",
        "title": "Virtual Technician: A multi-modal interface facilitating therapists' adoption of rehab robots",
        "year": "2026",
        "doi": "10.18416/AUTOMED.2026.2512",
        "url": "https://www.journals.infinite-science.de/index.php/automed/article/download/2512/1443/9651",
        "why_for_project": "Therapist natural language is mapped to rehabilitation robot parameter adjustments.",
    },
    {
        "category": "llm_exoskeleton_interface",
        "title": "LLM-Enabled Incremental Learning Framework for Hand Exoskeleton Control",
        "year": "2025",
        "doi": "10.1109/TASE.2024.3382679",
        "url": "https://ieeexplore.ieee.org/document/10489910/",
        "manual_only": True,
        "why_for_project": "Hand exoskeleton control interface using LLM-enabled incremental command learning.",
    },
    {
        "category": "llm_exoskeleton_interface",
        "title": "A Semantic-Aware Framework for Safe and Intent-Integrative Assistance in Upper-Limb Exoskeletons",
        "year": "2025",
        "doi": "10.48550/arXiv.2508.10378",
        "url": "https://arxiv.org/pdf/2508.10378",
        "why_for_project": "LLM extracts task semantics and maps them to safe assistive exoskeleton configurations.",
    },
    {
        "category": "llm_robot_planning",
        "title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
        "year": "2023",
        "doi": "10.48550/arXiv.2204.01691",
        "url": "https://proceedings.mlr.press/v205/ichter23a/ichter23a.pdf",
        "why_for_project": "Shows how LLM high-level plans should be constrained by executable robot affordances.",
    },
    {
        "category": "llm_robot_planning",
        "title": "Code as Policies: Language Model Programs for Embodied Control",
        "year": "2023",
        "doi": "10.1109/ICRA48891.2023.10160591",
        "url": "https://arxiv.org/pdf/2209.07753",
        "why_for_project": "Uses LLM-generated code to call existing robot APIs and parameterized control primitives.",
    },
    {
        "category": "llm_robot_planning",
        "title": "ProgPrompt: Generating Situated Robot Task Plans using Large Language Models",
        "year": "2023",
        "doi": "10.1109/ICRA48891.2023.10161317",
        "url": "https://arxiv.org/pdf/2209.11302",
        "why_for_project": "Constrains LLM plans through available actions and executable program-like prompts.",
    },
    {
        "category": "llm_robot_planning",
        "title": "Inner Monologue: Embodied Reasoning through Planning with Language Models",
        "year": "2023",
        "doi": "10.48550/arXiv.2207.05608",
        "url": "https://arxiv.org/pdf/2207.05608",
        "why_for_project": "Uses environment and human feedback for closed-loop language-level robot planning.",
    },
    {
        "category": "vla_background",
        "title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
        "year": "2023",
        "doi": "10.48550/arXiv.2307.15818",
        "url": "https://arxiv.org/pdf/2307.15818",
        "why_for_project": "Background on direct VLA action models; useful contrast for why knee exoskeletons need safer high-level use.",
    },
    {
        "category": "vla_background",
        "title": "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models",
        "year": "2023",
        "doi": "10.48550/arXiv.2307.05973",
        "url": "https://arxiv.org/pdf/2307.05973",
        "why_for_project": "LLM/VLM extracts constraints and affordances, then model-based planning handles execution.",
    },
    {
        "category": "vla_failure_detection",
        "title": "AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation",
        "year": "2024",
        "doi": "10.48550/arXiv.2410.00371",
        "url": "https://arxiv.org/pdf/2410.00371",
        "why_for_project": "VLM detects and reasons over manipulation failures; useful as a contrast for supervisory safety/comfort evaluation rather than direct exoskeleton torque control.",
    },
    {
        "category": "vla_feedback",
        "title": "Enhancing Robotic Manipulation with AI Feedback from Multimodal Large Language Models",
        "year": "2024",
        "doi": "10.48550/arXiv.2402.14245",
        "url": "https://arxiv.org/pdf/2402.14245",
        "why_for_project": "Uses multimodal LLM feedback to improve robot manipulation; relevant as an analogy for high-level evaluation feedback, not a primary exoskeleton controller.",
    },
    {
        "category": "llm_human_feedback_control",
        "title": "Learning to Learn Faster from Human Feedback with Language Model Predictive Control",
        "year": "2024",
        "doi": "10.48550/arXiv.2402.11450",
        "url": "https://arxiv.org/pdf/2402.11450",
        "why_for_project": "Connects language-model predictive control and human feedback; relevant to therapist/user feedback loops for bounded parameter adaptation.",
    },
    {
        "category": "llm_robot_safety",
        "title": "LLM-Guided Safety Agent for Edge Robotics with an ISO-Compliant Perception-Compute-Control Architecture",
        "year": "2026",
        "doi": "10.48550/arXiv.2604.20193",
        "url": "https://arxiv.org/pdf/2604.20193",
        "why_for_project": "Safety-agent architecture is relevant to separating high-level AI reasoning from real-time perception-compute-control loops.",
    },
    {
        "category": "speech_exoskeleton_interface",
        "title": "Speech-Based Human-Exoskeleton Interaction for Lower Limb Motion Planning",
        "year": "2023",
        "doi": "10.48550/arXiv.2310.03137",
        "url": "https://arxiv.org/pdf/2310.03137",
        "why_for_project": "Directly relevant to high-level speech input for lower-limb exoskeleton motion planning; likely Route D/future-extension evidence unless mapped to bounded DMP/impedance parameters.",
    },
    {
        "category": "generative_exoskeleton_rehab",
        "title": "Upper-Limb Rehabilitation with a Dual-Mode Individualized Exoskeleton Robot: A Generative-Model-Based Solution",
        "year": "2024",
        "doi": "10.48550/arXiv.2409.03193",
        "url": "https://arxiv.org/pdf/2409.03193",
        "why_for_project": "Generative-model individualized exoskeleton rehabilitation; useful for personalization framing, but upper-limb transfer must be limited.",
    },
    {
        "category": "gesture_exoskeleton_interface",
        "title": "A novel gesture interaction control method for rehabilitation lower extremity exoskeleton",
        "year": "2025",
        "doi": "10.48550/arXiv.2504.01888",
        "url": "https://arxiv.org/pdf/2504.01888",
        "why_for_project": "Lower-extremity exoskeleton interaction method; relevant to intent/interface literature and possible mode/trajectory selection.",
    },
    {
        "category": "llm_robot_safety",
        "title": "Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents",
        "year": "2024",
        "doi": "10.1109/ICRA57147.2024.10611447",
        "url": "https://h2r.cs.brown.edu/wp-content/uploads/yang24.pdf",
        "why_for_project": "Adds a verifiable safety-constraint module around LLM-driven robot agents.",
    },
    {
        "category": "llm_robot_safety",
        "title": "Updating Robot Safety Representations Online From Natural Language Feedback",
        "year": "2026",
        "doi": "",
        "url": "https://ieeexplore.ieee.org/iel8/11127273/11127223/11127680.pdf",
        "manual_only": True,
        "why_for_project": "Uses language feedback to update robot safety representations; relevant to translating natural-language safety goals.",
    },
]


MANIFEST_FIELDS = [
    "category",
    "title",
    "year",
    "doi",
    "url",
    "pdf_status",
    "pdf_path",
    "reason_failed",
    "why_for_project",
]


def safe_filename(ref: dict) -> str:
    title = clean_text(ref["title"])
    keep = []
    for ch in title:
        if ch.isalnum():
            keep.append(ch)
        elif ch in " -_":
            keep.append("_")
    stem = "_".join("".join(keep).split("_"))
    return f"{ref['year']}_{stem[:110]}.pdf"


def download_pdf(ref: dict) -> tuple[str, str, str]:
    dest = PAPERS / safe_filename(ref)
    if dest.exists() and dest.stat().st_size > 0:
        status = "manual_pdf" if ref.get("manual_only") else "open_access_pdf"
        return status, str(dest), "already_exists"

    if ref.get("manual_only"):
        return "manual_download", "", "manual_only_or_institution_access_required"

    s = session()
    try:
        resp = s.get(ref["url"], timeout=(8, 20), allow_redirects=True)
    except Exception as exc:
        return "manual_download", "", f"{type(exc).__name__}: {exc}"

    if resp.status_code >= 400:
        return "manual_download", "", f"HTTP {resp.status_code}"
    if not is_probably_pdf(resp):
        text = resp.text[:160].replace("\n", " ") if hasattr(resp, "text") else ""
        return "manual_download", "", f"not_pdf_or_landing_page: {text}"

    dest.write_bytes(resp.content)
    return "open_access_pdf", str(dest), "downloaded"


def metadata_key(row: dict) -> str:
    doi = normalize_doi(row.get("doi"))
    if doi:
        return f"doi:{doi}"
    title = clean_text(row.get("title")).lower()
    return f"title:{title}"


def sync_manifest_to_raw_metadata(manifest: list[dict]) -> tuple[int, int]:
    papers = load_json(RAW / "papers_with_pdf_status.json", [])
    index = {metadata_key(paper): paper for paper in papers}
    added = 0
    updated = 0

    for ref in manifest:
        row = {
            "title": ref["title"],
            "year": ref["year"],
            "venue": "arXiv" if "arxiv" in ref.get("doi", "").lower() else "",
            "doi": ref.get("doi", ""),
            "url": ref.get("url", ""),
            "pdf_url": ref.get("url", ""),
            "pdf_status": ref.get("pdf_status", ""),
            "pdf_path": ref.get("pdf_path", ""),
            "query": ref.get("category", ""),
            "keywords": [
                "large language model",
                "robotics",
                "semantic interface",
                "safety",
                "exoskeleton" if "exoskeleton" in ref["title"].lower() else "",
                "lower limb" if "lower limb" in ref["title"].lower() or "lower extremity" in ref["title"].lower() else "",
            ],
            "why_for_project": ref.get("why_for_project", ""),
        }
        row["keywords"] = [item for item in row["keywords"] if item]
        score, hits = score_paper(row)
        row["relevance_score"] = score
        row["score_hits"] = hits
        key = metadata_key(row)
        if key in index:
            index[key].update({k: v for k, v in row.items() if v not in {"", [], None}})
            updated += 1
        else:
            papers.append(row)
            index[key] = row
            added += 1

    save_json(RAW / "papers_with_pdf_status.json", papers)
    return added, updated


def main() -> None:
    ensure_dirs()
    manifest = []
    manual = []

    for ref in REFERENCES:
        print(f"downloading: {ref['title']}", flush=True)
        status, path, reason = download_pdf(ref)
        row = {**ref, "pdf_status": status, "pdf_path": path, "reason_failed": "" if path else reason}
        manifest.append(row)
        if not path:
            manual.append(
                {
                    "title": ref["title"],
                    "doi": ref["doi"],
                    "publisher_url": ref["url"],
                    "reason_failed": reason,
                    "suggested_filename": safe_filename(ref),
                }
            )

    out_path = Path("outputs") / "llm_agent_reference_manifest.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in MANIFEST_FIELDS} for row in manifest)

    write_csv(Path("outputs") / "llm_agent_manual_download.csv", manual, MANUAL_FIELDS)
    added, updated = sync_manifest_to_raw_metadata(manifest)
    print(
        f"references={len(manifest)} downloaded={sum(1 for r in manifest if r['pdf_path'])} "
        f"manual={len(manual)} metadata_added={added} metadata_updated={updated}"
    )


if __name__ == "__main__":
    main()
