from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import quote, urljoin

from pipeline_utils import (
    MANUAL_FIELDS,
    PAPERS,
    RAW,
    clean_text,
    ensure_dirs,
    is_probably_pdf,
    load_json,
    looks_like_blocked,
    normalize_doi,
    publisher_url,
    save_json,
    session,
    suggested_pdf_name,
    write_csv,
)


UNPAYWALL_EMAIL = "research@example.com"


def add_candidate(candidates: list[tuple[str, str]], url: str, status: str) -> None:
    url = clean_text(url)
    if not url:
        return
    if url.startswith("//"):
        url = "https:" + url
    if url.startswith("http") and url not in [u for u, _ in candidates]:
        candidates.append((url, status))


def doi_based_candidates(paper: dict) -> list[tuple[str, str]]:
    doi = normalize_doi(paper.get("doi"))
    candidates: list[tuple[str, str]] = []
    if not doi:
        return candidates

    add_candidate(candidates, paper.get("pdf_url", ""), "open_access_pdf")
    add_candidate(candidates, paper.get("oa_url", ""), "open_access_pdf")

    lower = doi.lower()
    if lower.startswith("10.48550/arxiv."):
        arxiv_id = lower.split("arxiv.", 1)[1]
        add_candidate(candidates, f"https://arxiv.org/pdf/{arxiv_id}", "open_access_pdf")
    if lower.startswith("10.1101/"):
        suffix = lower.split("10.1101/", 1)[1]
        add_candidate(candidates, f"https://www.biorxiv.org/content/10.1101/{suffix}.full.pdf", "open_access_pdf")
        add_candidate(candidates, f"https://www.medrxiv.org/content/10.1101/{suffix}.full.pdf", "open_access_pdf")
    if lower.startswith("10.3390/"):
        mdpi_code = lower.split("10.3390/", 1)[1]
        # MDPI DOI codes can usually be resolved through the DOI page, but these fallbacks cover common article paths.
        add_candidate(candidates, f"https://www.mdpi.com/search?q={quote(mdpi_code)}", "open_access_pdf")
    if lower.startswith("10.20944/preprints"):
        add_candidate(candidates, f"https://www.preprints.org/manuscript/{lower.rsplit('.', 1)[0].split('preprints', 1)[-1].strip('.')}/download", "open_access_pdf")
    add_candidate(candidates, f"https://doi.org/{doi}", "institution_access_pdf")
    return candidates


def openalex_candidates(paper: dict) -> list[tuple[str, str]]:
    doi = normalize_doi(paper.get("doi"))
    if not doi:
        return []
    s = session()
    url = "https://api.openalex.org/works/https://doi.org/" + quote(doi, safe="")
    resp = s.get(url, timeout=20)
    if resp.status_code >= 400:
        return []
    data = resp.json()
    candidates: list[tuple[str, str]] = []
    for loc in [data.get("best_oa_location") or {}, data.get("primary_location") or {}] + (data.get("locations") or []):
        add_candidate(candidates, loc.get("pdf_url", ""), "open_access_pdf")
        add_candidate(candidates, loc.get("landing_page_url", ""), "open_access_pdf" if loc.get("is_oa") else "institution_access_pdf")
    return candidates


def unpaywall_candidates(paper: dict) -> list[tuple[str, str]]:
    doi = normalize_doi(paper.get("doi"))
    if not doi:
        return []
    s = session()
    resp = s.get(
        f"https://api.unpaywall.org/v2/{quote(doi, safe='')}",
        params={"email": UNPAYWALL_EMAIL},
        timeout=20,
    )
    if resp.status_code >= 400:
        return []
    data = resp.json()
    candidates: list[tuple[str, str]] = []
    for loc in [data.get("best_oa_location") or {}] + (data.get("oa_locations") or []):
        add_candidate(candidates, loc.get("url_for_pdf", ""), "open_access_pdf")
        add_candidate(candidates, loc.get("url", ""), "open_access_pdf")
    return candidates


def semantic_scholar_candidates(paper: dict) -> list[tuple[str, str]]:
    doi = normalize_doi(paper.get("doi"))
    if not doi:
        return []
    s = session()
    resp = s.get(
        f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi, safe='')}",
        params={"fields": "openAccessPdf,url,title"},
        timeout=20,
    )
    if resp.status_code >= 400:
        return []
    data = resp.json()
    candidates: list[tuple[str, str]] = []
    pdf = data.get("openAccessPdf") or {}
    add_candidate(candidates, pdf.get("url", ""), "open_access_pdf")
    add_candidate(candidates, data.get("url", ""), "open_access_pdf")
    return candidates


def pmc_candidates(paper: dict) -> list[tuple[str, str]]:
    doi = normalize_doi(paper.get("doi"))
    if not doi:
        return []
    s = session()
    resp = s.get(
        "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/",
        params={"ids": doi, "format": "json"},
        timeout=20,
    )
    if resp.status_code >= 400:
        return []
    records = resp.json().get("records") or []
    candidates: list[tuple[str, str]] = []
    for rec in records:
        pmcid = clean_text(rec.get("pmcid"))
        if not pmcid:
            continue
        if pmcid.isdigit():
            pmcid = "PMC" + pmcid
        article_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
        add_candidate(candidates, article_url, "open_access_pdf")
        try:
            page = s.get(article_url, timeout=20)
            if page.status_code < 400:
                for link in pdf_links_from_html(article_url, page.text):
                    add_candidate(candidates, link, "open_access_pdf")
        except Exception:
            pass
    return candidates


def pdf_links_from_html(base_url: str, html: str) -> list[str]:
    links: list[str] = []
    for match in re.finditer(r"""href=["']([^"']+)["']""", html, re.I):
        href = match.group(1)
        low = href.lower()
        if any(token in low for token in [".pdf", "/pdf", "download", "full.pdf"]):
            links.append(urljoin(base_url, href))
    for match in re.finditer(r"""content=["']([^"']+\.pdf[^"']*)["']""", html, re.I):
        links.append(urljoin(base_url, match.group(1)))
    return links[:12]


def try_download_url(paper: dict, url: str, status: str, timeout: int) -> tuple[bool, str]:
    s = session()
    headers = {"Referer": publisher_url(paper) or "https://doi.org/"}
    try:
        resp = s.get(url, timeout=timeout, allow_redirects=True, headers=headers)
    except Exception as exc:
        return False, f"{url}: {type(exc).__name__}"
    blocked = looks_like_blocked(resp)
    if blocked:
        return False, f"{url}: {blocked}"
    if resp.status_code >= 400:
        return False, f"{url}: HTTP {resp.status_code}"
    if is_probably_pdf(resp):
        dest = PAPERS / suggested_pdf_name(paper)
        idx = 1
        while dest.exists():
            dest = PAPERS / f"{dest.stem}_{idx}.pdf"
            idx += 1
        dest.write_bytes(resp.content)
        paper["pdf_path"] = str(dest)
        paper["pdf_url_used"] = resp.url
        paper["pdf_status"] = status
        return True, f"{url}: downloaded"

    ctype = resp.headers.get("content-type", "").lower()
    if "html" in ctype:
        for pdf_url in pdf_links_from_html(resp.url, resp.text):
            ok, reason = try_download_url(paper, pdf_url, status, timeout)
            if ok:
                return True, reason
    return False, f"{url}: not_pdf_or_landing_page"


def collect_candidates(paper: dict) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    for provider in [doi_based_candidates, pmc_candidates, openalex_candidates, unpaywall_candidates, semantic_scholar_candidates]:
        try:
            for url, status in provider(paper):
                add_candidate(candidates, url, status)
        except Exception:
            continue
    return candidates


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()
    ensure_dirs()
    papers = load_json(RAW / "papers_with_pdf_status.json", load_json(RAW / "search_results.json", []))
    manual = []
    retried = 0
    recovered = 0
    for paper in papers:
        if paper.get("pdf_path") and Path(paper["pdf_path"]).exists():
            continue
        retried += 1
        reasons = []
        for url, status in collect_candidates(paper):
            ok, reason = try_download_url(paper, url, status, args.timeout)
            reasons.append(reason)
            if ok:
                recovered += 1
                break
        if not paper.get("pdf_path"):
            paper["pdf_status"] = "abstract_only" if paper.get("abstract") else "metadata_only"
            manual.append(
                {
                    "title": paper.get("title", ""),
                    "doi": paper.get("doi", ""),
                    "publisher_url": publisher_url(paper),
                    "reason_failed": " | ".join(reasons)[:1500] or "no_legal_direct_pdf_found",
                    "suggested_filename": suggested_pdf_name(paper),
                }
            )
        save_json(RAW / "papers_with_pdf_status.json", papers)
        write_csv(Path("outputs") / "manual_download.csv", manual, MANUAL_FIELDS)
    save_json(RAW / "papers_with_pdf_status.json", papers)
    write_csv(Path("outputs") / "manual_download.csv", manual, MANUAL_FIELDS)
    print(f"retried={retried} recovered={recovered} manual_remaining={len(manual)}")


if __name__ == "__main__":
    main()
