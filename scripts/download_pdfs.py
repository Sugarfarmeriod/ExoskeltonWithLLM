from __future__ import annotations

import argparse
from pathlib import Path

from pipeline_utils import (
    MANUAL_FIELDS,
    PAPERS,
    RAW,
    clean_text,
    ensure_dirs,
    is_probably_pdf,
    load_json,
    looks_like_blocked,
    publisher_url,
    save_json,
    session,
    suggested_pdf_name,
    write_csv,
    normalize_doi,
)


def candidate_urls(paper: dict) -> list[tuple[str, str]]:
    out = []
    for key, status in [("pdf_url", "open_access_pdf"), ("oa_url", "open_access_pdf")]:
        url = clean_text(paper.get(key))
        if url:
            out.append((url, status))
    doi_url = publisher_url(paper)
    if doi_url and doi_url not in [u for u, _ in out]:
        out.append((doi_url, "institution_access_pdf"))
    return out


def download_one(paper: dict, timeout: int = 15) -> tuple[dict, dict | None]:
    s = session()
    reasons = []
    for url, status in candidate_urls(paper):
        try:
            resp = s.get(url, timeout=timeout, allow_redirects=True)
        except Exception as exc:
            reasons.append(f"{url}: {type(exc).__name__}")
            continue
        blocked = looks_like_blocked(resp)
        if blocked:
            reasons.append(f"{url}: {blocked}")
            continue
        if resp.status_code >= 400:
            reasons.append(f"{url}: HTTP {resp.status_code}")
            continue
        if is_probably_pdf(resp):
            dest = PAPERS / suggested_pdf_name(paper)
            dest.write_bytes(resp.content)
            paper["pdf_path"] = str(dest)
            paper["pdf_url_used"] = url
            paper["pdf_status"] = status
            return paper, None
        reasons.append(f"{url}: not_pdf_or_landing_page")
    paper["pdf_status"] = "abstract_only" if paper.get("abstract") else "metadata_only"
    return paper, {
        "title": paper.get("title", ""),
        "doi": paper.get("doi", ""),
        "publisher_url": publisher_url(paper),
        "reason_failed": " | ".join(reasons)[:1000] or "no_pdf_url_found",
        "suggested_filename": suggested_pdf_name(paper),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()
    ensure_dirs()
    papers = load_json(RAW / "search_results.json", [])
    previous = load_json(RAW / "papers_with_pdf_status.json", [])
    previous_by_key = {}
    for old in previous:
        key = normalize_doi(old.get("doi")) or clean_text(old.get("title")).lower()
        if key:
            previous_by_key[key] = old
    for paper in papers:
        key = normalize_doi(paper.get("doi")) or clean_text(paper.get("title")).lower()
        old = previous_by_key.get(key)
        if old and old.get("pdf_path") and Path(old["pdf_path"]).exists():
            for field in ["pdf_path", "pdf_url_used", "pdf_status", "text_path", "note_path"]:
                if old.get(field):
                    paper[field] = old[field]
    if not papers:
        raise SystemExit("Run scripts/search_papers.py first")
    updated = []
    manual = []
    for idx, paper in enumerate(papers[: args.limit], 1):
        if paper.get("pdf_path") and Path(paper["pdf_path"]).exists():
            updated.append(paper)
            save_json(RAW / "papers_with_pdf_status.json", updated + papers[idx : args.limit])
            write_csv(Path("outputs") / "manual_download.csv", manual, MANUAL_FIELDS)
            continue
        paper, miss = download_one(paper)
        updated.append(paper)
        if miss:
            manual.append(miss)
        save_json(RAW / "papers_with_pdf_status.json", updated + papers[idx : args.limit])
        write_csv(Path("outputs") / "manual_download.csv", manual, MANUAL_FIELDS)
    save_json(RAW / "papers_with_pdf_status.json", updated)
    write_csv(Path("outputs") / "manual_download.csv", manual, MANUAL_FIELDS)
    downloaded = sum(1 for p in updated if p.get("pdf_path"))
    print(f"papers={len(updated)} downloaded={downloaded} manual_needed={len(manual)}")


if __name__ == "__main__":
    main()
