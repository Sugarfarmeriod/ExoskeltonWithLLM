from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader

from pipeline_utils import (
    PAPERS,
    RAW,
    clean_text,
    ensure_dirs,
    load_json,
    normalize_doi,
    paper_id,
    save_json,
)


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "outputs" / "pdf_link_audit.md"
BACKUP = RAW / "papers_with_pdf_status.before_pdf_reconcile.json"
PDF_STATUSES = {"open_access_pdf", "institution_access_pdf", "manual_pdf"}
STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "based",
    "for",
    "from",
    "in",
    "of",
    "on",
    "the",
    "to",
    "using",
    "with",
}


@dataclass(frozen=True)
class Candidate:
    paper_index: int
    pdf_path: Path
    score: int
    reason: str


def probe(path: Path, max_pages: int = 2) -> str:
    try:
        reader = PdfReader(str(path))
        return clean_text(" ".join((page.extract_text() or "") for page in reader.pages[:max_pages])).lower()
    except Exception:
        return ""


def compact(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def title_tokens(value: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-z0-9]+", value.lower())
        if len(token) > 2 and token not in STOPWORDS
    ]


def doi_variants(value: str) -> set[str]:
    doi = normalize_doi(value)
    if not doi:
        return set()
    return {
        doi,
        doi.replace("/", "_"),
        doi.replace("/", "_").replace(".", "_"),
        compact(doi),
    }


def score_candidate(path: Path, text: str, paper: dict) -> tuple[int, str]:
    name = path.stem.lower()
    name_compact = compact(name)
    text_compact = compact(text)
    title = clean_text(paper.get("title")).lower()
    tokens = title_tokens(title)

    for variant in doi_variants(paper.get("doi")):
        if variant and (variant in name or compact(variant) in name_compact or compact(variant) in text_compact):
            return 1200, "exact DOI"

    title_compact = compact(title)
    if title_compact and len(title_compact) >= 24:
        if title_compact in text_compact:
            return 1000, "exact title in PDF text"
        if title_compact in name_compact:
            return 950, "exact title in filename"

    if len(tokens) < 4:
        return 0, "insufficient title tokens"

    name_tokens = set(title_tokens(name))
    text_tokens = set(title_tokens(text[:12000]))
    title_set = set(tokens)
    name_overlap = len(title_set & name_tokens) / len(title_set)
    text_overlap = len(title_set & text_tokens) / len(title_set)
    prefix = tokens[: min(10, len(tokens))]
    prefix_overlap = sum(token in name_tokens for token in prefix) / len(prefix)

    if name_overlap >= 0.80 and len(title_set & name_tokens) >= 5:
        return 800 + round(name_overlap * 100), f"filename title coverage {name_overlap:.0%}"
    if text_overlap >= 0.85 and len(title_set & text_tokens) >= 6:
        return 700 + round(text_overlap * 100), f"PDF-text title coverage {text_overlap:.0%}"
    if prefix_overlap >= 0.90 and name_overlap >= 0.65 and len(prefix) >= 6:
        return 650 + round(name_overlap * 100), f"filename title-prefix coverage {prefix_overlap:.0%}"
    return 0, "no reliable identity match"


def choose_matches(papers: list[dict], pdfs: list[Path], probes: dict[Path, str]) -> dict[int, Candidate]:
    candidates: list[Candidate] = []
    for index, paper in enumerate(papers):
        for path in pdfs:
            score, reason = score_candidate(path, probes[path], paper)
            if score >= 700:
                candidates.append(Candidate(index, path.resolve(), score, reason))

    matches: dict[int, Candidate] = {}
    used_paths: set[Path] = set()
    for candidate in sorted(candidates, key=lambda item: (-item.score, item.paper_index, str(item.pdf_path))):
        if candidate.paper_index in matches or candidate.pdf_path in used_paths:
            continue
        matches[candidate.paper_index] = candidate
        used_paths.add(candidate.pdf_path)
    return matches


def resolved(path: str | Path | None) -> Path | None:
    if not path:
        return None
    return Path(path).resolve()


def status_for_match(paper: dict, matched_path: Path) -> str:
    old_path = resolved(paper.get("pdf_path"))
    old_status = clean_text(paper.get("pdf_status"))
    if old_path == matched_path and old_status in PDF_STATUSES:
        return old_status
    if old_path == matched_path and paper.get("pdf_url_used"):
        return "open_access_pdf"
    return "manual_pdf"


def write_report(
    papers: list[dict],
    pdfs: list[Path],
    matches: dict[int, Candidate],
    changed: int,
    apply_changes: bool,
) -> None:
    used = {candidate.pdf_path for candidate in matches.values()}
    unmatched_papers = [paper for index, paper in enumerate(papers) if index not in matches]
    unmatched_pdfs = [path for path in pdfs if path.resolve() not in used]
    status_counts: dict[str, int] = {}
    for paper in papers:
        status = clean_text(paper.get("pdf_status")) or "<blank>"
        status_counts[status] = status_counts.get(status, 0) + 1

    lines = [
        "# PDF 链接审计报告",
        "",
        f"- 模式：{'已应用' if apply_changes else '预演'}",
        f"- 元数据记录：{len(papers)}",
        f"- 本地 PDF：{len(pdfs)}",
        f"- 可靠的一对一关联：{len(matches)}",
        f"- 未匹配元数据：{len(unmatched_papers)}",
        f"- 未关联 PDF：{len(unmatched_pdfs)}",
        f"- 发生变化的元数据记录：{changed}",
        "",
        "## 状态汇总",
        "",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"- `{status}`：{count}")

    lines.extend(["", "## 未匹配元数据", ""])
    if unmatched_papers:
        for paper in unmatched_papers:
            lines.append(
                f"- {paper.get('title','未命名')} | DOI: {paper.get('doi') or '无'} | "
                f"status: {paper.get('pdf_status') or '无'}"
            )
    else:
        lines.append("- 无")

    lines.extend(["", "## 未关联 PDF", ""])
    if unmatched_pdfs:
        for path in unmatched_pdfs:
            lines.append(f"- `{path.name}`")
    else:
        lines.append("- 无")

    lines.extend(["", "## 可靠关联", ""])
    for index, candidate in sorted(matches.items()):
        paper = papers[index]
        lines.append(
            f"- {paper.get('title','未命名')} -> `{candidate.pdf_path.name}` "
            f"({candidate.reason}, score={candidate.score})"
        )
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit and reconcile local PDFs with metadata using strict identity matching.")
    parser.add_argument("--apply", action="store_true", help="Apply the audited one-to-one links to raw metadata.")
    args = parser.parse_args()

    ensure_dirs()
    papers = load_json(RAW / "papers_with_pdf_status.json", load_json(RAW / "search_results.json", []))
    pdfs = sorted(PAPERS.glob("*.pdf"))
    probes = {path.resolve(): probe(path) for path in pdfs}
    matches = choose_matches(papers, pdfs, probes)

    changed = 0
    for index, paper in enumerate(papers):
        before = (
            clean_text(paper.get("pdf_path")),
            clean_text(paper.get("pdf_status")),
            clean_text(paper.get("text_cache_path")),
        )
        candidate = matches.get(index)
        if candidate:
            paper["pdf_path"] = str(candidate.pdf_path)
            paper["pdf_status"] = status_for_match(paper, candidate.pdf_path)
            cache_path = ROOT / "outputs" / "text_cache" / f"{paper_id(paper)}.txt"
            paper["text_cache_path"] = str(cache_path.relative_to(ROOT)) if cache_path.is_file() else ""
        else:
            paper["pdf_path"] = ""
            paper["text_cache_path"] = ""
            paper["pdf_status"] = "abstract_only" if clean_text(paper.get("abstract")) else "metadata_only"
        after = (
            clean_text(paper.get("pdf_path")),
            clean_text(paper.get("pdf_status")),
            clean_text(paper.get("text_cache_path")),
        )
        changed += before != after

    if args.apply:
        source = RAW / "papers_with_pdf_status.json"
        if source.exists() and not BACKUP.exists():
            shutil.copy2(source, BACKUP)
        save_json(source, papers)

    write_report(papers, pdfs, matches, changed, args.apply)
    print(
        f"metadata={len(papers)} pdfs={len(pdfs)} matched={len(matches)} "
        f"unmatched_metadata={len(papers) - len(matches)} changed={changed} applied={args.apply}"
    )
    print(f"report={REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
