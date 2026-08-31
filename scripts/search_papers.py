from __future__ import annotations

import argparse
from typing import Any

from pipeline_utils import (
    OUTPUTS,
    RAW,
    clean_text,
    ensure_dirs,
    normalize_doi,
    polite_sleep,
    read_queries,
    save_json,
    score_paper,
    session,
)


def openalex_search(query: str, per_page: int = 25) -> list[dict[str, Any]]:
    s = session()
    url = "https://api.openalex.org/works"
    params = {
        "search": query,
        "per-page": per_page,
        "filter": "from_publication_date:2014-01-01",
        "sort": "relevance_score:desc",
    }
    resp = s.get(url, params=params, timeout=30)
    resp.raise_for_status()
    works = resp.json().get("results", [])
    rows = []
    for work in works:
        authors = [
            a.get("author", {}).get("display_name", "")
            for a in work.get("authorships", [])[:8]
            if a.get("author", {}).get("display_name")
        ]
        best_oa = work.get("best_oa_location") or {}
        primary = work.get("primary_location") or {}
        source = (primary.get("source") or {}) if primary else {}
        abstract = ""
        inv = work.get("abstract_inverted_index")
        if inv:
            words = sorted(
                ((pos, word) for word, poses in inv.items() for pos in poses),
                key=lambda x: x[0],
            )
            abstract = " ".join(word for _, word in words)
        rows.append(
            {
                "source": "OpenAlex",
                "title": clean_text(work.get("title")),
                "authors": "; ".join(authors),
                "year": work.get("publication_year") or "",
                "venue": clean_text(source.get("display_name") or work.get("host_venue", {}).get("display_name")),
                "doi": normalize_doi(work.get("doi")),
                "abstract": clean_text(abstract),
                "url": work.get("doi") or work.get("id") or "",
                "pdf_url": clean_text(best_oa.get("pdf_url")),
                "oa_url": clean_text(best_oa.get("landing_page_url")),
                "is_oa": bool(work.get("open_access", {}).get("is_oa")),
                "query": query,
                "cited_by_count": work.get("cited_by_count") or 0,
            }
        )
    return rows


def crossref_search(query: str, rows: int = 15) -> list[dict[str, Any]]:
    s = session()
    resp = s.get(
        "https://api.crossref.org/works",
        params={"query": query, "rows": rows, "filter": "from-pub-date:2014"},
        timeout=30,
    )
    resp.raise_for_status()
    items = resp.json().get("message", {}).get("items", [])
    out = []
    for item in items:
        date_parts = item.get("published-print", item.get("published-online", item.get("created", {}))).get("date-parts", [[]])
        year = date_parts[0][0] if date_parts and date_parts[0] else ""
        links = item.get("link", [])
        pdf_url = ""
        for link in links:
            if "pdf" in link.get("content-type", "").lower() or str(link.get("URL", "")).lower().endswith(".pdf"):
                pdf_url = link.get("URL", "")
                break
        out.append(
            {
                "source": "Crossref",
                "title": clean_text(item.get("title")),
                "authors": "; ".join(
                    clean_text(f"{a.get('given','')} {a.get('family','')}")
                    for a in item.get("author", [])[:8]
                ),
                "year": year,
                "venue": clean_text(item.get("container-title")),
                "doi": normalize_doi(item.get("DOI")),
                "abstract": clean_text(item.get("abstract")),
                "url": clean_text(item.get("URL")),
                "pdf_url": clean_text(pdf_url),
                "is_oa": False,
                "query": query,
                "cited_by_count": item.get("is-referenced-by-count") or 0,
            }
        )
    return out


def dedupe_rank(papers: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    seen: dict[str, dict[str, Any]] = {}
    for paper in papers:
        title = clean_text(paper.get("title"))
        if not title:
            continue
        key = normalize_doi(paper.get("doi")) or title.lower()
        existing = seen.get(key)
        if existing:
            for field in ["abstract", "pdf_url", "oa_url", "authors", "venue", "doi", "url"]:
                if not existing.get(field) and paper.get(field):
                    existing[field] = paper[field]
            existing["source"] = f"{existing.get('source')};{paper.get('source')}"
            existing["query"] = f"{existing.get('query')}; {paper.get('query')}"
            existing["is_oa"] = bool(existing.get("is_oa") or paper.get("is_oa"))
            existing["cited_by_count"] = max(int(existing.get("cited_by_count") or 0), int(paper.get("cited_by_count") or 0))
        else:
            seen[key] = paper
    ranked = []
    for paper in seen.values():
        score, why = score_paper(paper)
        paper["relevance_score"] = score
        paper["why_relevant"] = why
        ranked.append(paper)
    ranked.sort(key=lambda p: (int(p.get("relevance_score") or 0), int(p.get("cited_by_count") or 0)), reverse=True)
    return ranked[:limit]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--per-query", type=int, default=25)
    args = parser.parse_args()
    ensure_dirs()
    queries = read_queries()
    if not queries:
        raise SystemExit("queries.md is empty or missing")

    all_papers = []
    errors = []
    for query in queries:
        try:
            rows = openalex_search(query, per_page=args.per_query)
            all_papers.extend(rows)
        except Exception as exc:
            errors.append({"source": "OpenAlex", "query": query, "error": repr(exc)})
        polite_sleep()
        try:
            rows = crossref_search(query, rows=max(8, args.per_query // 2))
            all_papers.extend(rows)
        except Exception as exc:
            errors.append({"source": "Crossref", "query": query, "error": repr(exc)})
        polite_sleep()

    ranked = dedupe_rank(all_papers, args.limit)
    save_json(RAW / "search_results.json", ranked)
    save_json(RAW / "search_errors.json", errors)
    (OUTPUTS / "expanded_keywords.md").write_text(
        "\n".join(
            [
                "# Expanded keywords",
                "",
                "原始关键词来自 queries.md。本次脚本额外用于评分/识别的同义词：",
                "",
                "- human in the loop / human-in-the-loop",
                "- covariance matrix adaptation / CMA-ES",
                "- wearable robot",
                "- gait phase / gait state / ground contact / intent",
                "- adaptive impedance / admittance",
                "- metabolic cost / EMG / gait symmetry / interaction torque",
                "- therapist input / clinical instruction / high-level input",
                "- natural language / LLM / semantic human-robot interaction",
                "- shared control / intent-based control",
            ]
        ),
        encoding="utf-8",
    )
    print(f"searched={len(all_papers)} deduped_ranked={len(ranked)} errors={len(errors)}")


if __name__ == "__main__":
    main()
