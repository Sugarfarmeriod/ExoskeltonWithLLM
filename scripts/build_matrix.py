from __future__ import annotations

from pathlib import Path

from pipeline_utils import (
    FIELDS,
    RAW,
    classify_paper,
    ensure_dirs,
    is_semantic_direction,
    is_pure_llm_or_chatbot,
    load_json,
    pdf_status_for,
    save_json,
    text_blob,
    write_csv,
)


def main() -> None:
    ensure_dirs()
    papers = load_json(RAW / "papers_with_pdf_status.json", [])
    rows = []
    low = []
    for paper in papers:
        paper.update(classify_paper(paper))
        paper["pdf_status"] = pdf_status_for(paper)
        rows.append({field: paper.get(field, "") for field in FIELDS})
        blob = text_blob(paper)
        score = int(paper.get("relevance_score") or 0)
        semantic_route = is_semantic_direction(blob)
        semantic_weak = paper.get("ai_role") == "高层语义/治疗师输入接口" and paper.get("parameter_mapping") == "no direct mapping confirmed"
        if score < 25 or is_pure_llm_or_chatbot(blob) or semantic_route:
            low.append(paper)

    write_csv(Path("outputs") / "paper_matrix.csv", rows, FIELDS)
    lines = ["# Rejected or Low Priority", ""]
    for paper in low:
        lines.append(
            f"- **{paper.get('title','未命名')}** ({paper.get('year','')}) | "
            f"score={paper.get('relevance_score','')} | role={paper.get('ai_role','')} | "
            f"{paper.get('why_relevant','')}"
        )
    Path("outputs/rejected_or_low_priority.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    save_json(RAW / "papers_with_pdf_status.json", papers)
    print(f"matrix_rows={len(rows)} low_priority={len(low)}")


if __name__ == "__main__":
    main()
