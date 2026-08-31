"""Generate a Markdown diagnostic report from structured JSON outputs."""

from __future__ import annotations

import argparse
from pathlib import Path

from diagnostic_report import ReportInputError, generate_report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a traceable Markdown report from metrics and suggestions."
    )
    parser.add_argument("metrics_json", type=Path)
    parser.add_argument("suggestion_json", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output Markdown path. Defaults beside metrics_json as diagnostic_report.md.",
    )
    args = parser.parse_args()

    output_path = args.output
    if output_path is None:
        output_path = args.metrics_json.with_name("diagnostic_report.md")

    try:
        generate_report(args.metrics_json, args.suggestion_json, output_path)
    except ReportInputError as exc:
        print(f"Report generation failed: {exc}")
        return 1

    print(f"Wrote diagnostic report: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
