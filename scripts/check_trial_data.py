"""Validate a normalized exoskeleton trial directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from trial_io import TrialDataError, load_trial, summarize_trial


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a normalized trial directory."
    )
    parser.add_argument(
        "trial_dir",
        type=Path,
        help="Directory containing metadata.json and signals_wide.csv.",
    )
    parser.add_argument(
        "--summary-json",
        type=Path,
        default=None,
        help="Optional path for writing a compact validation summary JSON.",
    )
    args = parser.parse_args()

    try:
        trial = load_trial(args.trial_dir)
    except TrialDataError as exc:
        print(f"Trial validation failed: {exc}", file=sys.stderr)
        return 1

    summary = summarize_trial(trial)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.summary_json is not None:
        args.summary_json.parent.mkdir(parents=True, exist_ok=True)
        args.summary_json.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
