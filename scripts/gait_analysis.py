"""Deterministic gait analysis for normalized exoskeleton trial data."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from trial_io import TrialData, load_trial


@dataclass(frozen=True)
class AnalysisConfig:
    foot_contact_threshold: float = 0.5
    phase_event_threshold: float = 0.5
    min_valid_cycles: int = 1
    min_cycle_duration: float = 0.4
    max_cycle_duration: float = 2.5
    safe_torque_epsilon: float = 1e-9


def analyze_trial(trial: TrialData, config: AnalysisConfig | None = None) -> dict[str, Any]:
    """Analyze one validated trial and return traceable gait metrics."""

    cfg = config or AnalysisConfig()
    signals = trial.signals
    time = signals["time"]

    foot_events = detect_foot_contact_events(
        time,
        signals["feet_load"],
        threshold=cfg.foot_contact_threshold,
    )
    phase_events = detect_phase0_events(
        time,
        signals["phase0_event"],
        threshold=cfg.phase_event_threshold,
    )
    cycles = segment_cycles_from_events(
        phase_events,
        min_duration=cfg.min_cycle_duration,
        max_duration=cfg.max_cycle_duration,
    )

    unavailable: dict[str, str] = {}
    metrics = {
        "tracking_rmse": rmse(signals["q_meas"], signals["q_ref"]),
        "peak_flexion_error": max(signals["q_meas"]) - max(signals["q_ref"]),
        "phase_delay_seconds": estimate_peak_phase_delay(
            time,
            signals["q_meas"],
            signals["q_ref"],
            cycles,
        ),
        "torque_peak_abs": max(abs(value) for value in signals["tau_e"]),
        "torque_rms": rms(signals["tau_e"]),
        "torque_limit_ratio": torque_limit_ratio(
            signals["tau_e"],
            signals["safe_torque"],
            epsilon=cfg.safe_torque_epsilon,
        ),
    }

    if metrics["phase_delay_seconds"] is None:
        unavailable["phase_delay_seconds"] = (
            "No valid phase0_event cycle was available for peak timing comparison."
        )

    quality = {
        "is_usable_for_parameter_suggestion": len(cycles) >= cfg.min_valid_cycles,
        "valid_cycle_count": len(cycles),
        "min_valid_cycles": cfg.min_valid_cycles,
        "warnings": [],
    }
    if len(cycles) < cfg.min_valid_cycles:
        quality["warnings"].append(
            "Valid gait cycle count is below the configured minimum."
        )

    return {
        "trial": {
            "trial_id": trial.metadata["trial_id"],
            "application": trial.metadata["application"],
            "affected_side": trial.metadata["affected_side"],
            "source_csv": str(trial.source_csv),
            "sample_count": trial.sample_count,
            "duration_seconds": trial.duration,
        },
        "config": {
            "foot_contact_threshold": cfg.foot_contact_threshold,
            "phase_event_threshold": cfg.phase_event_threshold,
            "min_valid_cycles": cfg.min_valid_cycles,
            "min_cycle_duration": cfg.min_cycle_duration,
            "max_cycle_duration": cfg.max_cycle_duration,
        },
        "events": {
            "foot_contact": foot_events,
            "phase0": phase_events,
        },
        "cycles": cycles,
        "reference": {
            "type": "in_trial_reference",
            "q_ref_field": "q_ref",
            "dq_ref_field": "dq_ref",
            "notes": "First implementation uses the reference trajectory exported with the trial.",
        },
        "metrics": metrics,
        "quality": quality,
        "unavailable_fields": unavailable,
    }


def write_gait_metrics(
    trial_dir: str | Path,
    output_path: str | Path,
    config: AnalysisConfig | None = None,
) -> dict[str, Any]:
    """Load a trial, analyze it, and write JSON metrics."""

    trial = load_trial(trial_dir)
    result = analyze_trial(trial, config=config)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def detect_foot_contact_events(
    time: list[float],
    feet_load: list[float],
    threshold: float,
) -> list[dict[str, Any]]:
    """Detect threshold crossing foot-contact events."""

    events: list[dict[str, Any]] = []
    if not time:
        return events
    previous_contact = feet_load[0] >= threshold
    events.append(
        {
            "time": time[0],
            "type": "contact_on" if previous_contact else "contact_off",
            "source": "foot-load-derived",
            "threshold": threshold,
        }
    )
    for index in range(1, len(time)):
        is_contact = feet_load[index] >= threshold
        if is_contact != previous_contact:
            events.append(
                {
                    "time": time[index],
                    "type": "contact_on" if is_contact else "contact_off",
                    "source": "foot-load-derived",
                    "threshold": threshold,
                }
            )
        previous_contact = is_contact
    return events


def detect_phase0_events(
    time: list[float],
    phase0_event: list[float],
    threshold: float,
) -> list[dict[str, Any]]:
    """Detect rising edges in the phase0 event signal."""

    events: list[dict[str, Any]] = []
    previous_active = False
    for index, value in enumerate(phase0_event):
        active = value >= threshold
        if active and not previous_active:
            events.append(
                {
                    "time": time[index],
                    "sample_index": index,
                    "source": "phase0-event-derived",
                    "threshold": threshold,
                }
            )
        previous_active = active
    return events


def segment_cycles_from_events(
    phase_events: list[dict[str, Any]],
    min_duration: float,
    max_duration: float,
) -> list[dict[str, Any]]:
    """Create gait cycle boundaries from adjacent phase0 events."""

    cycles: list[dict[str, Any]] = []
    for index in range(len(phase_events) - 1):
        start_event = phase_events[index]
        end_event = phase_events[index + 1]
        duration = end_event["time"] - start_event["time"]
        is_valid = min_duration <= duration <= max_duration
        cycles.append(
            {
                "cycle_index": index,
                "start_time": start_event["time"],
                "end_time": end_event["time"],
                "start_sample_index": start_event["sample_index"],
                "end_sample_index": end_event["sample_index"],
                "duration_seconds": duration,
                "is_valid": is_valid,
                "quality_notes": []
                if is_valid
                else [f"Cycle duration {duration:.3f}s outside configured bounds."],
            }
        )
    return [cycle for cycle in cycles if cycle["is_valid"]]


def estimate_peak_phase_delay(
    time: list[float],
    q_meas: list[float],
    q_ref: list[float],
    cycles: list[dict[str, Any]],
) -> float | None:
    """Estimate measured-reference peak timing delay over valid cycles."""

    delays: list[float] = []
    for cycle in cycles:
        start = cycle["start_sample_index"]
        end = cycle["end_sample_index"] + 1
        if end <= start:
            continue
        meas_segment = q_meas[start:end]
        ref_segment = q_ref[start:end]
        if not meas_segment or not ref_segment:
            continue
        meas_peak = start + max(range(len(meas_segment)), key=meas_segment.__getitem__)
        ref_peak = start + max(range(len(ref_segment)), key=ref_segment.__getitem__)
        delays.append(time[meas_peak] - time[ref_peak])
    if not delays:
        return None
    return sum(delays) / len(delays)


def rmse(values: list[float], reference: list[float]) -> float:
    errors = [(value - ref) ** 2 for value, ref in zip(values, reference)]
    if not errors:
        return math.nan
    return math.sqrt(sum(errors) / len(errors))


def rms(values: list[float]) -> float:
    if not values:
        return math.nan
    return math.sqrt(sum(value * value for value in values) / len(values))


def torque_limit_ratio(
    tau_e: list[float],
    safe_torque: list[float],
    epsilon: float,
) -> float:
    ratios = [
        abs(tau) / max(abs(limit), epsilon)
        for tau, limit in zip(tau_e, safe_torque)
    ]
    if not ratios:
        return math.nan
    return max(ratios)
