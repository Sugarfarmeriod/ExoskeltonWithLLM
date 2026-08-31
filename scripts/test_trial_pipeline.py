"""Focused smoke tests for the trial analysis pipeline.

This is intentionally a plain Python script instead of a pytest suite so it
can run in the current minimal project environment.
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

from diagnostic_report import ReportInputError, generate_report
from gait_analysis import write_gait_metrics
from parameter_suggestion import write_parameter_suggestion
from trial_io import TrialDataError, load_trial


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = PROJECT_ROOT / "data" / "fixtures" / "synthetic_trial_001"


def main() -> int:
    test_fixture_loads()
    test_missing_required_signal_fails()
    test_full_pipeline_outputs()
    test_report_rejects_raw_csv()
    print("trial pipeline tests passed")
    return 0


def test_fixture_loads() -> None:
    trial = load_trial(FIXTURE_DIR)
    assert trial.sample_count == 11
    assert trial.duration == 1.0


def test_missing_required_signal_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        trial_dir = Path(tmp)
        shutil.copy(FIXTURE_DIR / "metadata.json", trial_dir / "metadata.json")
        (trial_dir / "signals_wide.csv").write_text(
            "time,q_meas\n0,0\n1,1\n",
            encoding="utf-8",
        )
        try:
            load_trial(trial_dir)
        except TrialDataError as exc:
            message = str(exc)
            assert "Missing required signal columns" in message
            assert "dq_meas" in message
        else:
            raise AssertionError("Expected missing signal validation failure.")


def test_full_pipeline_outputs() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        output_dir = Path(tmp)
        metrics_path = output_dir / "gait_metrics.json"
        suggestion_path = output_dir / "parameter_suggestion.json"
        report_path = output_dir / "diagnostic_report.md"

        metrics = write_gait_metrics(FIXTURE_DIR, metrics_path)
        suggestion = write_parameter_suggestion(metrics_path, suggestion_path)
        report = generate_report(metrics_path, suggestion_path, report_path)

        assert metrics["quality"]["valid_cycle_count"] == 1
        assert suggestion["human_confirmation_required"] is True
        assert "Unsupported claims" in report
        assert metrics_path.exists()
        assert suggestion_path.exists()
        assert report_path.exists()


def test_report_rejects_raw_csv() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        suggestion_path = Path(tmp) / "parameter_suggestion.json"
        suggestion_path.write_text(
            json.dumps(
                {
                    "trial": {},
                    "source_metrics": {},
                    "thresholds": {},
                    "suggestions": {},
                    "human_confirmation_required": True,
                }
            ),
            encoding="utf-8",
        )
        try:
            generate_report(FIXTURE_DIR / "signals_wide.csv", suggestion_path, Path(tmp) / "x.md")
        except ReportInputError:
            return
        raise AssertionError("Expected report generator to reject raw CSV input.")


if __name__ == "__main__":
    raise SystemExit(main())
