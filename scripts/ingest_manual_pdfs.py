from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader

from pipeline_utils import INBOX, RAW, clean_text, copy_manual_pdf, ensure_dirs, load_json, normalize_doi, save_json


def pdf_probe_text(path: Path, max_pages: int = 2) -> str:
    try:
        reader = PdfReader(str(path))
        chunks = []
        for page in reader.pages[:max_pages]:
            chunks.append(page.extract_text() or "")
        return clean_text(" ".join(chunks)).lower()
    except Exception:
        return ""


def score_match(src: Path, probe: str, paper: dict) -> int:
    name = src.stem.lower()
    title = clean_text(paper.get("title")).lower()
    doi = normalize_doi(paper.get("doi"))
    score = 0
    if doi:
        doi_file = doi.replace("/", "_").replace(".", "_")
        if doi in name or doi_file in name or doi in probe:
            score += 80
    if title:
        title_tokens = [t for t in title.replace("-", " ").split() if len(t) > 3]
        if title in name or title in probe:
            score += 100
        score += sum(5 for tok in title_tokens[:12] if tok in name)
        score += sum(3 for tok in title_tokens[:16] if tok in probe)
    return score


def main() -> None:
    ensure_dirs()
    papers = load_json(RAW / "papers_with_pdf_status.json", load_json(RAW / "search_results.json", []))
    inbox_pdfs = sorted(INBOX.glob("*.pdf"))
    ingested = 0
    alternates = 0
    unmatched = 0
    for src in inbox_pdfs:
        match = None
        probe = pdf_probe_text(src)
        best_score = 0
        for paper in papers:
            score = score_match(src, probe, paper)
            if score > best_score:
                best_score = score
                match = paper
        if best_score < 15:
            match = None
        if not match:
            unmatched += 1
            continue

        dest = copy_manual_pdf(src, match)
        if match.get("pdf_path"):
            alternate_paths = match.setdefault("alternate_pdf_paths", [])
            if str(dest) not in alternate_paths:
                alternate_paths.append(str(dest))
            alternates += 1
        else:
            match["pdf_path"] = str(dest)
            match["pdf_status"] = "manual_pdf"
            ingested += 1
    save_json(RAW / "papers_with_pdf_status.json", papers)
    print(
        f"inbox_pdfs={len(inbox_pdfs)} matched_ingested={ingested} "
        f"alternate_versions={alternates} unmatched={unmatched}"
    )


if __name__ == "__main__":
    main()
