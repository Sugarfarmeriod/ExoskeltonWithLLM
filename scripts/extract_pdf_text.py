from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader

from pipeline_utils import INBOX, PAPERS, RAW, ensure_dirs, load_json, paper_id, save_json

TEXT_CACHE = Path("outputs/text_cache")


def normalize_path(path: str | Path) -> Path:
    return Path(path).resolve()


def extract_text(path: Path) -> str:
    reader = PdfReader(str(path))
    chunks: list[str] = []
    for idx, page in enumerate(reader.pages, 1):
        try:
            page_text = page.extract_text() or ""
        except Exception:
            page_text = ""
        chunks.append(f"\n\n--- page {idx} ---\n\n{page_text}")
    return "\n".join(chunks).strip()


def collect_pdf_paths(papers: list[dict]) -> dict[str, Path]:
    pdfs: dict[str, Path] = {}
    for paper in papers:
        pdf_path = paper.get("pdf_path")
        if pdf_path and Path(pdf_path).exists():
            pdfs[paper_id(paper)] = normalize_path(pdf_path)

    known = {normalize_path(path) for path in pdfs.values()}
    for folder in [PAPERS, INBOX]:
        if not folder.exists():
            continue
        for path in folder.glob("*.pdf"):
            resolved = normalize_path(path)
            if resolved in known:
                continue
            fallback_id = path.stem[:120]
            pdfs[fallback_id] = resolved
    return pdfs


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract local PDF text into outputs/text_cache.")
    parser.add_argument("--force", action="store_true", help="Re-extract even when cache files already exist.")
    args = parser.parse_args()

    ensure_dirs()
    TEXT_CACHE.mkdir(parents=True, exist_ok=True)

    papers = load_json(RAW / "papers_with_pdf_status.json", [])
    pdfs = collect_pdf_paths(papers)
    extracted = 0
    skipped = 0
    failed = 0

    for pid, path in sorted(pdfs.items()):
        out = TEXT_CACHE / f"{pid}.txt"
        if out.exists() and not args.force:
            skipped += 1
            for paper in papers:
                if paper_id(paper) == pid:
                    paper["text_cache_path"] = str(out)
            continue
        try:
            text = extract_text(path)
        except Exception as exc:
            failed += 1
            for paper in papers:
                if paper_id(paper) == pid:
                    paper["text_extract_error"] = repr(exc)
            continue
        out.write_text(text, encoding="utf-8")
        extracted += 1
        for paper in papers:
            if paper_id(paper) == pid:
                paper["text_cache_path"] = str(out)

    save_json(RAW / "papers_with_pdf_status.json", papers)
    print(f"pdfs={len(pdfs)} extracted={extracted} skipped={skipped} failed={failed}")


if __name__ == "__main__":
    main()
