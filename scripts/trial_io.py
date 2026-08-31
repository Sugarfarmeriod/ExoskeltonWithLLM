"""Load and validate normalized exoskeleton trial data.

The loader consumes a trial directory containing metadata.json and a wide CSV
file. It intentionally avoids heavy dependencies so it can run in the project
root with the standard Python runtime.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REQUIRED_METADATA_FIELDS = (
    "trial_id",
    "application",
    "target_name",
    "affected_side",
    "subject_id",
    "signals_are_time_aligned",
)

REQUIRED_SIGNAL_FIELDS = (
    "time",
    "q_meas",
    "dq_meas",
    "q_ref",
    "dq_ref",
    "feet_load",
    "phi",
    "phase0_event",
    "tau_e",
    "safe_torque",
    "assist_enabled",
)

WIDE_SIGNAL_FILENAMES = (
    "signals_wide.csv",
    "signals_wide_if_aligned.csv",
)


class TrialDataError(ValueError):
    """Raised when a trial directory cannot be loaded or validated."""


@dataclass(frozen=True)
class TrialData:
    """In-memory representation of a validated trial."""

    trial_dir: Path
    metadata: dict[str, Any]
    signals: dict[str, list[float]]
    source_csv: Path

    @property
    def sample_count(self) -> int:
        return len(self.signals["time"])

    @property
    def duration(self) -> float:
        time = self.signals["time"]
        if len(time) < 2:
            return 0.0
        return time[-1] - time[0]


def load_trial(trial_dir: str | Path) -> TrialData:
    """Load and validate one trial directory."""

    trial_path = Path(trial_dir)
    if not trial_path.exists():
        raise TrialDataError(f"Trial directory does not exist: {trial_path}")
    if not trial_path.is_dir():
        raise TrialDataError(f"Trial path is not a directory: {trial_path}")

    metadata_path = trial_path / "metadata.json"
    if not metadata_path.exists():
        raise TrialDataError(f"Missing metadata file: {metadata_path}")

    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise TrialDataError(f"Invalid metadata JSON: {metadata_path}: {exc}") from exc

    missing_metadata = [
        field for field in REQUIRED_METADATA_FIELDS if field not in metadata
    ]
    if missing_metadata:
        raise TrialDataError(
            "Missing required metadata fields: " + ", ".join(missing_metadata)
        )

    source_csv = _find_wide_csv(trial_path)
    rows = _read_csv_rows(source_csv)
    if not rows:
        raise TrialDataError(f"Signal CSV has no data rows: {source_csv}")

    signal_map = metadata.get("signal_map", {})
    if signal_map is None:
        signal_map = {}
    if not isinstance(signal_map, dict):
        raise TrialDataError("metadata.signal_map must be an object if provided.")

    headers = set(rows[0].keys())
    missing_signals: list[str] = []
    resolved_columns: dict[str, str] = {}
    for field in REQUIRED_SIGNAL_FIELDS:
        column_name = str(signal_map.get(field, field))
        if column_name not in headers:
            missing_signals.append(f"{field} -> {column_name}")
        else:
            resolved_columns[field] = column_name

    if missing_signals:
        raise TrialDataError(
            "Missing required signal columns: " + ", ".join(missing_signals)
        )

    signals: dict[str, list[float]] = {}
    for field, column_name in resolved_columns.items():
        signals[field] = _parse_numeric_column(rows, column_name, field)

    _validate_time(signals["time"])
    expected_len = len(signals["time"])
    length_errors = [
        field
        for field, values in signals.items()
        if len(values) != expected_len
    ]
    if length_errors:
        raise TrialDataError(
            "Signal length mismatch for fields: " + ", ".join(length_errors)
        )

    return TrialData(
        trial_dir=trial_path,
        metadata=metadata,
        signals=signals,
        source_csv=source_csv,
    )


def summarize_trial(trial: TrialData) -> dict[str, Any]:
    """Create a compact summary suitable for logs or smoke tests."""

    return {
        "trial_id": trial.metadata["trial_id"],
        "application": trial.metadata["application"],
        "affected_side": trial.metadata["affected_side"],
        "source_csv": str(trial.source_csv),
        "sample_count": trial.sample_count,
        "duration_seconds": trial.duration,
        "signals": list(REQUIRED_SIGNAL_FIELDS),
    }


def _find_wide_csv(trial_path: Path) -> Path:
    for filename in WIDE_SIGNAL_FILENAMES:
        candidate = trial_path / filename
        if candidate.exists():
            return candidate
    expected = ", ".join(WIDE_SIGNAL_FILENAMES)
    raise TrialDataError(f"Missing wide signal CSV. Expected one of: {expected}")


def _read_csv_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise TrialDataError(f"Signal CSV has no header: {csv_path}")
        return list(reader)


def _parse_numeric_column(
    rows: list[dict[str, str]],
    column_name: str,
    field_name: str,
) -> list[float]:
    values: list[float] = []
    for row_index, row in enumerate(rows, start=2):
        raw_value = row.get(column_name, "")
        if raw_value is None or str(raw_value).strip() == "":
            raise TrialDataError(
                f"Empty value in field {field_name} column {column_name} "
                f"at CSV row {row_index}."
            )
        try:
            values.append(float(raw_value))
        except ValueError as exc:
            raise TrialDataError(
                f"Non-numeric value in field {field_name} column {column_name} "
                f"at CSV row {row_index}: {raw_value!r}"
            ) from exc
    return values


def _validate_time(time: list[float]) -> None:
    if not time:
        raise TrialDataError("time field is empty.")
    for index in range(1, len(time)):
        if time[index] <= time[index - 1]:
            raise TrialDataError(
                "time must be strictly increasing; "
                f"row {index + 2} has {time[index]} after {time[index - 1]}."
            )
