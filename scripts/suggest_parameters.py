"""Generate conservative parameter suggestions from gait metrics JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from parameter_suggestion import SuggestionThresholds, write_parameter_suggestion


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate bounded parameter suggestions from gait metrics."
    )
    parser.add_argument("metrics_json", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output JSON path. Defaults beside metrics_json as parameter_suggestion.json.",
    )
    parser.add_argument("--torque-veto-ratio", type=float, default=0.85)
    parser.add_argument("--min-valid-cycles", type=int, default=1)
    args = parser.parse_args()

    output_path = args.output
    if output_path is None:
        output_path = args.metrics_json.with_name("parameter_suggestion.json")

    result = write_parameter_suggestion(
        args.metrics_json,
        output_path,
        thresholds=SuggestionThresholds(
            min_valid_cycles=args.min_valid_cycles,
            torque_limit_veto_ratio=args.torque_veto_ratio,
        ),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"Wrote parameter suggestion: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
