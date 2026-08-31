from __future__ import annotations

import csv
import re
from pathlib import Path

from pipeline_utils import RAW, clean_text, ensure_dirs, load_json, paper_id

CARD_DIR = Path("outputs/evidence_cards")
TOP30_CSV = Path("outputs/light_rank_top30.csv")
SCREENING_REPORT = Path("outputs/light_screening_report.md")
TOP10_DEEP = Path("outputs/top_10_for_deep_reading.md")
MANUAL_DEEP = Path("outputs/manual_deep_read_list.md")

POSITIVE_WEIGHTS = {
    "human-in-the-loop": 22,
    "human in the loop": 22,
    "bayesian optimization": 22,
    "cma-es": 20,
    "covariance matrix adaptation": 20,
    "dmp": 16,
    "dynamic movement primitive": 16,
    "impedance": 15,
    "stiffness": 10,
    "damping": 10,
    "knee": 10,
    "exoskeleton": 10,
    "wearable robot": 9,
    "gait phase": 9,
    "phase": 5,
    "intent": 8,
    "ground contact": 8,
    "foot pressure": 8,
    "adaptive": 7,
    "co-adaptive": 10,
    "multi-agent": 9,
    "staged": 4,
    "reinforcement learning": 10,
    "musculoskeletal": 7,
    "hip exoskeleton": 6,
    "physical hip exoskeleton": 8,
    "stroke": 6,
    "safety": 6,
    "torque": 5,
    "metabolic": 4,
}

SYSTEM_WEIGHTS = {
    "amplitude": 8,
    "phase_offset": 8,
    "tau": 5,
    "kp": 7,
    "kd": 7,
    "safetorque": 7,
    "phi": 5,
    "phase0event": 5,
    "feetload": 5,
    "q_ref": 4,
    "dq_ref": 4,
    "tau_e": 4,
}

NEGATIVE_WEIGHTS = {
    "chatbot": -25,
    "question answering": -22,
    "medical advice": -20,
    "finite element": -12,
    "mechanical design": -10,
    "vision": -6,
}


def read_card(paper: dict) -> tuple[Path, str]:
    pid = paper_id(paper)
    path = Path(paper.get("evidence_card_path") or CARD_DIR / f"{pid}.md")
    if not path.exists():
        return path, ""
    return path, path.read_text(encoding="utf-8", errors="ignore")


def term_hits(text: str, terms: list[str]) -> list[str]:
    lower = text.lower()
    hits = []
    for term in terms:
        if re.search(rf"(?<![a-z0-9_]){re.escape(term.lower())}(?![a-z0-9_])", lower):
            hits.append(term)
    return hits


def infer_ai_role(blob: str) -> str:
    lower = blob.lower()
    if any(t in lower for t in ["human-in-the-loop", "human in the loop", "bayesian optimization", "cma-es", "optimization"]):
        return "parameter optimizer"
    if any(t in lower for t in ["gait phase", "intent", "ground contact", "state estimation", "foot pressure"]):
        return "state estimator"
    if any(t in lower for t in ["dynamic movement primitive", "dmp", "trajectory generation"]):
        return "trajectory generator / DMP learner"
    if any(t in lower for t in ["natural language", "therapist", "semantic", "llm"]):
        return "semantic / therapist interface"
    return "unclear"


def score_paper(paper: dict, card: str) -> tuple[int, list[str], list[str], str, str]:
    metadata = " ".join(
        clean_text(paper.get(key))
        for key in ["title", "abstract", "venue", "keywords", "why_relevant", "ai_role", "optimized_parameters"]
    )
    blob = f"{metadata}\n{card}"
    lower = blob.lower()
    score = 0
    for term, weight in POSITIVE_WEIGHTS.items():
        if term in lower:
            score += weight
    for term, weight in SYSTEM_WEIGHTS.items():
        if re.search(rf"(?<![a-z0-9_]){re.escape(term)}(?![a-z0-9_])", lower):
            score += weight
    for term, weight in NEGATIVE_WEIGHTS.items():
        if term in lower:
            score += weight

    unavailable_sensor_hits = []
    if re.search(r"\b(?:emg|electromyograph\w*)\b", lower):
        score -= 8
        unavailable_sensor_hits.append("EMG")
    if re.search(r"\bimu\b|inertial measurement unit", lower):
        score -= 8
        unavailable_sensor_hits.append("IMU")

    if paper.get("pdf_status") in {"open_access_pdf", "manual_pdf", "institution_access_pdf"}:
        score += 4
    if paper.get("year"):
        try:
            if int(paper["year"]) >= 2021:
                score += 3
        except Exception:
            pass

    hits = term_hits(blob, list(POSITIVE_WEIGHTS))
    system_hits = term_hits(blob, list(SYSTEM_WEIGHTS))
    ai_role = infer_ai_role(blob)
    why = []
    if any(hit in hits for hit in ["human-in-the-loop", "human in the loop", "bayesian optimization", "cma-es"]):
        why.append("matches low-frequency HIL/Bayesian/CMA-ES optimization priority")
    if any(hit in hits for hit in ["dmp", "dynamic movement primitive", "impedance"]):
        why.append("mentions DMP/impedance control substrate")
    if any(hit in hits for hit in ["gait phase", "intent", "ground contact", "foot pressure"]):
        why.append("supports phase/load/intent estimation route")
    if system_hits:
        why.append("has possible mapping to current Simulink/Speedgoat parameters")
    if unavailable_sensor_hits:
        why.append(
            "uses unavailable sensor(s) "
            + "/".join(unavailable_sensor_hits)
            + "; method reference only"
        )
    if not why:
        why.append("ranked mainly by title/abstract metadata")
    return score, hits, system_hits, ai_role, "; ".join(why)


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = [
        "rank",
        "title",
        "year",
        "venue",
        "doi",
        "pdf_status",
        "light_score",
        "ai_role_light",
        "matched_keywords",
        "matched_system_terms",
        "why_light_rank",
        "evidence_card",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def report_lines(rows: list[dict], total: int) -> list[str]:
    role_counts: dict[str, int] = {}
    for row in rows:
        role_counts[row["ai_role_light"]] = role_counts.get(row["ai_role_light"], 0) + 1
    lines = [
        "# Light Screening Report",
        "",
        "This report is generated from metadata and compressed evidence cards only. It does not use full-PDF deep reading.",
        "",
        "Scope: the planned study uses 8 healthy participants and no EMG/IMU. Papers that rely on EMG/IMU are retained only as method references and receive a light-ranking penalty.",
        "",
        f"- Papers considered: {total}",
        f"- Evidence-card-ranked papers shown: {len(rows)}",
        "- Best current route: Route A, AI as a low-frequency DMP/impedance parameter optimizer.",
        "- Route D semantic/therapist input remains a future-extension route unless it maps into bounded trajectory, impedance, assistance, phase, mode, or safety parameters.",
        "",
        "## Role Distribution In Top 30",
    ]
    for role, count in sorted(role_counts.items(), key=lambda item: item[1], reverse=True):
        lines.append(f"- {role}: {count}")
    lines.extend(["", "## Top 30"])
    for row in rows:
        lines.append(
            f"{row['rank']}. **{row['title']}** ({row['year']}) - score {row['light_score']} - {row['ai_role_light']}\n"
            f"   - DOI: {row['doi'] or 'not available'}\n"
            f"   - Why: {row['why_light_rank']}\n"
            f"   - Evidence card: `{row['evidence_card']}`"
        )
    return lines


def top10_lines(rows: list[dict]) -> list[str]:
    lines = [
        "# Top 10 For Deep Reading",
        "",
        "Read these first if the next step is a focused deep read. Selection is based only on title, abstract, keywords, and evidence cards.",
        "",
        "Scope: the planned study uses 8 healthy participants and no EMG/IMU; unavailable-sensor papers are method references only.",
        "",
    ]
    for row in rows[:10]:
        lines.append(
            f"{row['rank']}. **{row['title']}** ({row['year']})\n"
            f"   - DOI: {row['doi'] or 'not available'}\n"
            f"   - Light score: {row['light_score']}\n"
            f"   - AI role: {row['ai_role_light']}\n"
            f"   - System terms: {row['matched_system_terms'] or 'none'}\n"
            f"   - Reason: {row['why_light_rank']}"
        )
    return lines


def manual_lines(rows: list[dict], watchlist: list[dict] | None = None) -> list[str]:
    lines = [
        "# Manual Deep Read List",
        "",
        "These papers look relevant but should not be deeply read until explicitly requested. Use this as a queue for later top-5 deep reading.",
        "",
        "Scope: the planned study uses 8 healthy participants and no EMG/IMU. Papers dependent on these sensors have lower direct-transfer priority.",
        "",
    ]
    for row in rows[10:30]:
        lines.append(
            f"- **{row['title']}** ({row['year']}) - score {row['light_score']} - {row['ai_role_light']} - DOI: {row['doi'] or 'not available'}"
        )
    if watchlist:
        lines.extend(["", "## User-Added Watchlist", ""])
        for row in watchlist:
            lines.append(
                f"- **{row['title']}** ({row['year']}) - score {row['light_score']} - {row['ai_role_light']} - "
                f"DOI: {row['doi'] or 'not available'} - Evidence card: `{row['evidence_card']}`"
            )
    return lines


def main() -> None:
    ensure_dirs()
    papers = load_json(RAW / "papers_with_pdf_status.json", [])
    scored: list[dict] = []
    seen_titles: set[str] = set()
    for paper in papers:
        card_path, card = read_card(paper)
        score, hits, system_hits, role, why = score_paper(paper, card)
        title_key = re.sub(r"\W+", " ", clean_text(paper.get("title")).lower()).strip()
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)
        scored.append(
            {
                "title": clean_text(paper.get("title")),
                "year": paper.get("year") or "",
                "venue": paper.get("venue") or "",
                "doi": paper.get("doi") or "",
                "pdf_status": paper.get("pdf_status") or "",
                "light_score": score,
                "ai_role_light": role,
                "matched_keywords": "; ".join(hits),
                "matched_system_terms": "; ".join(system_hits),
                "why_light_rank": why,
                "evidence_card": str(card_path),
            }
        )

    scored.sort(key=lambda row: int(row["light_score"]), reverse=True)
    top30 = scored[:30]
    for idx, row in enumerate(top30, 1):
        row["rank"] = idx
    top30_titles = {row["title"] for row in top30}
    user_watchlist = [
        row
        for row in scored
        if row["title"] not in top30_titles
        and ("SMAT" in row["title"] or "Staged Multi-Agent Training" in row["title"])
    ]

    write_csv(TOP30_CSV, top30)
    SCREENING_REPORT.write_text("\n".join(report_lines(top30, len(papers))) + "\n", encoding="utf-8")
    TOP10_DEEP.write_text("\n".join(top10_lines(top30)) + "\n", encoding="utf-8")
    MANUAL_DEEP.write_text("\n".join(manual_lines(top30, user_watchlist)) + "\n", encoding="utf-8")
    print(f"ranked={len(scored)} top30={len(top30)}")


if __name__ == "__main__":
    main()
