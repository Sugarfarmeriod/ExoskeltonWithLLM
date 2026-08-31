from __future__ import annotations

from pathlib import Path

from pipeline_utils import MANUAL_FIELDS, RAW, ensure_dirs, load_json, publisher_url, suggested_pdf_name, write_csv


def main() -> None:
    ensure_dirs()
    papers = load_json(RAW / "papers_with_pdf_status.json", [])
    manual = []
    for paper in papers:
        if paper.get("pdf_path") and Path(paper["pdf_path"]).exists():
            continue
        manual.append(
            {
                "title": paper.get("title", ""),
                "doi": paper.get("doi", ""),
                "publisher_url": publisher_url(paper),
                "reason_failed": "manual_download_needed",
                "suggested_filename": suggested_pdf_name(paper),
            }
        )
    write_csv(Path("outputs") / "manual_download.csv", manual, MANUAL_FIELDS)
    print(f"manual_remaining={len(manual)}")


if __name__ == "__main__":
    main()
