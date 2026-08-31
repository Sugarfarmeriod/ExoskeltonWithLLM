from __future__ import annotations

from pathlib import Path

from pipeline_utils import (
    MANUAL_FIELDS,
    PAPERS,
    RAW,
    ensure_dirs,
    is_probably_pdf,
    load_json,
    normalize_doi,
    publisher_url,
    save_json,
    session,
    suggested_pdf_name,
    write_csv,
)


KNOWN_URLS = {
    "10.36227/techrxiv.22327378.v1": [
        "https://d197for5662m48.cloudfront.net/documents/publicationstatus/169066/preprint_pdf/32e7b898251a8e63a1f499c489b69631.pdf",
    ],
    "10.36227/techrxiv.22327378": [
        "https://d197for5662m48.cloudfront.net/documents/publicationstatus/169066/preprint_pdf/32e7b898251a8e63a1f499c489b69631.pdf",
    ],
    "10.1101/2021.02.19.431882": [
        "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9FBC1580F11614B388BE621D716800AD/S2631717621000141a.pdf/div-class-title-comparing-optimized-exoskeleton-assistance-of-the-hip-knee-and-ankle-in-single-and-multi-joint-configurations-div.pdf",
    ],
    "10.1126/scirobotics.aar5438": [
        "https://scholar.harvard.edu/files/ding_kim_2018_scirob_hil_bo_hip_extension_assistance.pdf",
    ],
    "10.1109/tro.2021.3133137": [
        "https://www.pure.ed.ac.uk/ws/portalfiles/portal/258696285/Human_In_The_Loop_GORDON_DOA17112021_AFV.pdf",
    ],
    "10.1109/ro-man47096.2020.9223477": [
        "https://arxiv.org/pdf/2107.00359",
        "https://elib.dlr.de/139975/1/RLMMT_RoMAN_Paper%281%29.pdf",
    ],
    "10.1101/2020.10.17.343970": [
        "https://par.nsf.gov/servlets/purl/10298407",
    ],
}


def download(paper: dict, url: str) -> tuple[bool, str]:
    s = session()
    try:
        resp = s.get(url, timeout=45, allow_redirects=True, headers={"Referer": publisher_url(paper)})
    except Exception as exc:
        return False, f"{url}: {type(exc).__name__}"
    if resp.status_code >= 400:
        return False, f"{url}: HTTP {resp.status_code}"
    if not is_probably_pdf(resp):
        return False, f"{url}: not_pdf"
    dest = PAPERS / suggested_pdf_name(paper)
    idx = 1
    while dest.exists():
        dest = PAPERS / f"{dest.stem}_{idx}.pdf"
        idx += 1
    dest.write_bytes(resp.content)
    paper["pdf_path"] = str(dest)
    paper["pdf_url_used"] = resp.url
    paper["pdf_status"] = "open_access_pdf"
    return True, f"{url}: downloaded"


def main() -> None:
    ensure_dirs()
    papers = load_json(RAW / "papers_with_pdf_status.json", load_json(RAW / "search_results.json", []))
    recovered = 0
    attempts = []
    for paper in papers:
        if paper.get("pdf_path") and Path(paper["pdf_path"]).exists():
            continue
        doi = normalize_doi(paper.get("doi"))
        for url in KNOWN_URLS.get(doi, []):
            ok, reason = download(paper, url)
            attempts.append({"title": paper.get("title", ""), "doi": doi, "reason": reason})
            if ok:
                recovered += 1
                break
    save_json(RAW / "papers_with_pdf_status.json", papers)
    save_json(RAW / "known_pdf_download_attempts.json", attempts)

    manual = []
    for paper in papers:
        if paper.get("pdf_path") and Path(paper["pdf_path"]).exists():
            continue
        paper["pdf_status"] = "abstract_only" if paper.get("abstract") else "metadata_only"
        manual.append(
            {
                "title": paper.get("title", ""),
                "doi": paper.get("doi", ""),
                "publisher_url": publisher_url(paper),
                "reason_failed": "no_legal_direct_pdf_after_retry",
                "suggested_filename": suggested_pdf_name(paper),
            }
        )
    write_csv(Path("outputs") / "manual_download.csv", manual, MANUAL_FIELDS)
    print(f"known_url_recovered={recovered} manual_remaining={len(manual)}")


if __name__ == "__main__":
    main()
