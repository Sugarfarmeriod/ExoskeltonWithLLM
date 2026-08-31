from __future__ import annotations

import re
from pathlib import Path

from pipeline_utils import RAW, clean_text, ensure_dirs, load_json, paper_id, save_json

TEXT_CACHE = Path("outputs/text_cache")
CARD_DIR = Path("outputs/evidence_cards")

TRACKED_KEYWORDS = [
    "human-in-the-loop",
    "Bayesian optimization",
    "CMA-ES",
    "gait phase",
    "anomaly detection",
    "safety",
    "DMP",
    "impedance",
    "exoskeleton",
    "knee",
    "stroke",
]

SYSTEM_TERMS = [
    "q",
    "dq",
    "q_ref",
    "dq_ref",
    "tau_e",
    "FeetLoad",
    "Phi",
    "Phase0Event",
    "Amplitude",
    "tau",
    "phase_offset",
    "Kp",
    "Kd",
    "SafeTorque",
]

RELEVANCE_TERMS = [
    "human-in-the-loop",
    "human in the loop",
    "bayesian",
    "optimization",
    "cma-es",
    "dmp",
    "dynamic movement primitive",
    "impedance",
    "stiffness",
    "damping",
    "gait phase",
    "phase",
    "exoskeleton",
    "knee",
    "stroke",
    "safety",
    "torque",
    "assistance",
    "adaptive",
    "intent",
    "foot",
    "load",
]

SECTION_PATTERNS = {
    "introduction": re.compile(r"\b(1\s*)?(introduction|background)\b", re.I),
    "method": re.compile(r"\b(methods?|methodology|materials and methods|control method|proposed method|approach)\b", re.I),
    "experiment": re.compile(r"\b(experiments?|evaluation|results?|validation|user study|clinical evaluation)\b", re.I),
    "conclusion": re.compile(r"\b(conclusions?|discussion|future work)\b", re.I),
}


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"-\n(?=[a-z])", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_paragraphs(text: str) -> list[str]:
    raw = re.split(r"\n\s*\n|--- page \d+ ---", text)
    paragraphs: list[str] = []
    for para in raw:
        para = clean_text(para)
        if len(para) < 80:
            continue
        if len(para) > 1200:
            sentences = re.split(r"(?<=[.!?])\s+", para)
            chunk = ""
            for sentence in sentences:
                if len(chunk) + len(sentence) > 1000 and chunk:
                    paragraphs.append(chunk.strip())
                    chunk = sentence
                else:
                    chunk = f"{chunk} {sentence}".strip()
            if chunk:
                paragraphs.append(chunk.strip())
        else:
            paragraphs.append(para)
    return paragraphs


def section_windows(paragraphs: list[str]) -> dict[str, list[str]]:
    heading_positions: list[tuple[int, str]] = []
    for idx, para in enumerate(paragraphs):
        probe = para[:140]
        for section, pattern in SECTION_PATTERNS.items():
            if pattern.search(probe):
                heading_positions.append((idx, section))
                break

    windows: dict[str, list[str]] = {name: [] for name in SECTION_PATTERNS}
    if not paragraphs:
        return windows

    if not heading_positions:
        n = len(paragraphs)
        windows["introduction"] = paragraphs[: max(3, n // 6)]
        windows["method"] = paragraphs[n // 6 : n // 2]
        windows["experiment"] = paragraphs[n // 2 : (5 * n) // 6]
        windows["conclusion"] = paragraphs[(5 * n) // 6 :]
        return windows

    heading_positions.sort()
    for pos, (start, section) in enumerate(heading_positions):
        end = heading_positions[pos + 1][0] if pos + 1 < len(heading_positions) else min(len(paragraphs), start + 45)
        windows.setdefault(section, []).extend(paragraphs[start:end])
    return windows


def score_paragraph(para: str) -> int:
    lower = para.lower()
    score = 0
    for term in RELEVANCE_TERMS:
        score += lower.count(term) * 3
    for term in [t.lower() for t in SYSTEM_TERMS]:
        score += lower.count(term) * 2
    if 120 <= len(para) <= 900:
        score += 2
    return score


def select_relevant(paragraphs: list[str], limit: int) -> list[str]:
    scored = [(score_paragraph(para), idx, para) for idx, para in enumerate(paragraphs)]
    scored = [item for item in scored if item[0] > 0]
    scored.sort(key=lambda item: (item[0], -item[1]), reverse=True)
    picked = sorted(scored[:limit], key=lambda item: item[1])
    return [para for _, _, para in picked]


def find_terms(text: str, terms: list[str]) -> list[str]:
    found = []
    lower = text.lower()
    for term in terms:
        pattern = re.escape(term.lower())
        if re.search(rf"(?<![a-z0-9_]){pattern}(?![a-z0-9_])", lower):
            found.append(term)
    return found


def card_for_paper(paper: dict, text: str) -> str:
    normalized = normalize_text(text)
    paragraphs = split_paragraphs(normalized)
    windows = section_windows(paragraphs)
    abstract = clean_text(paper.get("abstract")) or "not available in metadata"
    keywords = paper.get("keywords") or []
    if isinstance(keywords, str):
        keyword_text = keywords
    else:
        keyword_text = ", ".join(str(item) for item in keywords if item)
    combined = " ".join([paper.get("title") or "", abstract, keyword_text, normalized[:30000]])

    sections = [
        ("introduction_relevant_5", select_relevant(windows.get("introduction", []), 5)),
        ("method_relevant_8", select_relevant(windows.get("method", []), 8)),
        ("experiment_evaluation_relevant_8", select_relevant(windows.get("experiment", []), 8)),
        ("conclusion_relevant_5", select_relevant(windows.get("conclusion", []), 5)),
    ]

    lines = [
        "---",
        f"paper_id: {paper_id(paper)}",
        f"title: {clean_text(paper.get('title'))}",
        f"year: {paper.get('year') or ''}",
        f"doi: {paper.get('doi') or ''}",
        f"pdf_status: {paper.get('pdf_status') or ''}",
        "---",
        "",
        "# Evidence Card",
        "",
        f"## Title\n{clean_text(paper.get('title')) or 'untitled'}",
        "",
        f"## Year\n{paper.get('year') or ''}",
        "",
        f"## DOI\n{paper.get('doi') or ''}",
        "",
        f"## Abstract\n{abstract}",
        "",
        f"## Keywords\n{keyword_text or 'not available in metadata'}",
        "",
        "## Tracked Keywords Found",
        ", ".join(find_terms(combined, TRACKED_KEYWORDS)) or "none",
        "",
        "## System Signals / Parameters Found",
        ", ".join(find_terms(combined, SYSTEM_TERMS)) or "none",
    ]

    for heading, selected in sections:
        lines.extend(["", f"## {heading}"])
        if not selected:
            lines.append("No high-relevance paragraph found by local keyword screening.")
        else:
            for idx, para in enumerate(selected, 1):
                lines.append(f"{idx}. {para[:1000]}")
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    ensure_dirs()
    TEXT_CACHE.mkdir(parents=True, exist_ok=True)
    CARD_DIR.mkdir(parents=True, exist_ok=True)

    papers = load_json(RAW / "papers_with_pdf_status.json", [])
    built = 0
    missing_text = 0
    for paper in papers:
        pid = paper_id(paper)
        declared_text_path = paper.get("text_cache_path")
        text_path = Path(declared_text_path) if declared_text_path else None
        if text_path is None or not text_path.is_file():
            missing_text += 1
            text = ""
        else:
            text = text_path.read_text(encoding="utf-8", errors="ignore")
        card_path = CARD_DIR / f"{pid}.md"
        card_path.write_text(card_for_paper(paper, text), encoding="utf-8")
        paper["evidence_card_path"] = str(card_path)
        built += 1

    save_json(RAW / "papers_with_pdf_status.json", papers)
    print(f"evidence_cards={built} missing_text={missing_text}")


if __name__ == "__main__":
    main()
