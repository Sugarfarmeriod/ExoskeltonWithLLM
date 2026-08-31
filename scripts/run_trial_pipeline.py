"""Run validation, gait analysis, suggestions, and report generation."""

from __future__ import annotations

import argparse
from pathlib import Path

from diagnostic_report import generate_report
from gait_analysis import write_gait_metrics
from parameter_suggestion import write_parameter_suggestion
from trial_io import load_trial, summarize_trial


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the trial analysis pipeline.")
    parser.add_argument("trial_dir", type=Path)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Defaults to analysis_outputs/<trial_dir_name>.",
    )
    args = parser.parse_args()

    output_dir = args.output_dir or Path("analysis_outputs") / args.trial_dir.name
    output_dir.mkdir(parents=True, exist_ok=True)

    trial = load_trial(args.trial_dir)
    print("Validated trial:", summarize_trial(trial))

    metrics_path = output_dir / "gait_metrics.json"
    suggestion_path = output_dir / "parameter_suggestion.json"
    report_path = output_dir / "diagnostic_report.md"

    write_gait_metrics(args.trial_dir, metrics_path)
    write_parameter_suggestion(metrics_path, suggestion_path)
    generate_report(metrics_path, suggestion_path, report_path)

    print(f"Wrote metrics: {metrics_path}")
    print(f"Wrote suggestion: {suggestion_path}")
    print(f"Wrote report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
