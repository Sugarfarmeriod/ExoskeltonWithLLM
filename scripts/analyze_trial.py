"""Run deterministic gait analysis for one normalized trial."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from gait_analysis import AnalysisConfig, write_gait_metrics
from trial_io import TrialDataError


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze a normalized gait trial.")
    parser.add_argument("trial_dir", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output JSON path. Defaults to analysis_outputs/<trial_id>/gait_metrics.json.",
    )
    parser.add_argument("--min-valid-cycles", type=int, default=1)
    args = parser.parse_args()

    output_path = args.output
    if output_path is None:
        output_path = Path("analysis_outputs") / args.trial_dir.name / "gait_metrics.json"

    try:
        result = write_gait_metrics(
            args.trial_dir,
            output_path,
            config=AnalysisConfig(min_valid_cycles=args.min_valid_cycles),
        )
    except TrialDataError as exc:
        print(f"Trial analysis failed: {exc}")
        return 1

    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"Wrote gait metrics: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
