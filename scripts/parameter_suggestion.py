"""Conservative parameter suggestion rules for gait metrics."""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class SuggestionThresholds:
    min_valid_cycles: int = 1
    phase_delay_seconds: float = 0.05
    peak_flexion_error: float = 0.05
    tracking_rmse: float = 0.08
    torque_limit_veto_ratio: float = 0.85
    torque_limit_reduce_ratio: float = 0.95


def suggest_parameters(
    gait_metrics: dict[str, Any],
    thresholds: SuggestionThresholds | None = None,
) -> dict[str, Any]:
    """Create bounded, conservative parameter suggestions from metrics JSON."""

    cfg = thresholds or SuggestionThresholds()
    metrics = gait_metrics.get("metrics", {})
    quality = gait_metrics.get("quality", {})
    trial = gait_metrics.get("trial", {})

    valid_cycle_count = int(quality.get("valid_cycle_count", 0))
    torque_ratio = _number_or_none(metrics.get("torque_limit_ratio"))
    phase_delay = _number_or_none(metrics.get("phase_delay_seconds"))
    peak_error = _number_or_none(metrics.get("peak_flexion_error"))
    tracking_rmse = _number_or_none(metrics.get("tracking_rmse"))

    global_vetoes: list[str] = []
    if valid_cycle_count < cfg.min_valid_cycles:
        global_vetoes.append("valid_cycle_count_below_minimum")
    torque_veto = torque_ratio is not None and torque_ratio >= cfg.torque_limit_veto_ratio
    torque_reduce = torque_ratio is not None and torque_ratio >= cfg.torque_limit_reduce_ratio

    suggestions = {
        "phase_offset": _suggest_phase_offset(phase_delay, cfg, global_vetoes),
        "Amplitude": _suggest_amplitude(
            peak_error,
            torque_veto,
            torque_reduce,
            cfg,
            global_vetoes,
        ),
        "assist_gain": _suggest_assist_gain(
            tracking_rmse,
            torque_veto,
            torque_reduce,
            cfg,
            global_vetoes,
        ),
        "MO_Kp": _suggest_kp(
            tracking_rmse,
            torque_veto,
            cfg,
            global_vetoes,
        ),
        "MO_Kd": _suggest_kd(
            tracking_rmse,
            torque_veto,
            cfg,
            global_vetoes,
        ),
    }

    return {
        "trial": {
            "trial_id": trial.get("trial_id", ""),
            "application": trial.get("application", ""),
            "affected_side": trial.get("affected_side", ""),
        },
        "source_metrics": {
            "valid_cycle_count": valid_cycle_count,
            "phase_delay_seconds": phase_delay,
            "peak_flexion_error": peak_error,
            "tracking_rmse": tracking_rmse,
            "torque_limit_ratio": torque_ratio,
        },
        "thresholds": asdict(cfg),
        "global_vetoes": global_vetoes,
        "suggestions": suggestions,
        "human_confirmation_required": True,
        "control_boundary": (
            "Suggestions are offline advisory actions only; they must not be "
            "written to Speedgoat or Simulink automatically."
        ),
    }


def write_parameter_suggestion(
    metrics_path: str | Path,
    output_path: str | Path,
    thresholds: SuggestionThresholds | None = None,
) -> dict[str, Any]:
    metrics = json.loads(Path(metrics_path).read_text(encoding="utf-8"))
    suggestion = suggest_parameters(metrics, thresholds=thresholds)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(suggestion, ensure_ascii=False, indent=2), encoding="utf-8")
    return suggestion


def _suggest_phase_offset(
    phase_delay: float | None,
    cfg: SuggestionThresholds,
    global_vetoes: list[str],
) -> dict[str, Any]:
    if global_vetoes:
        return _decision("RULE_PHASE_QUALITY_HOLD", "hold", global_vetoes)
    if phase_delay is None:
        return _decision("RULE_PHASE_UNAVAILABLE_HOLD", "hold", ["phase_delay_unavailable"])
    if phase_delay > cfg.phase_delay_seconds:
        return _decision(
            "RULE_PHASE_LATE_ADVANCE",
            "advance",
            [],
            "Measured peak is late relative to reference.",
        )
    if phase_delay < -cfg.phase_delay_seconds:
        return _decision(
            "RULE_PHASE_EARLY_DELAY",
            "delay",
            [],
            "Measured peak is early relative to reference.",
        )
    return _decision("RULE_PHASE_WITHIN_BAND_HOLD", "hold", [])


def _suggest_amplitude(
    peak_error: float | None,
    torque_veto: bool,
    torque_reduce: bool,
    cfg: SuggestionThresholds,
    global_vetoes: list[str],
) -> dict[str, Any]:
    if global_vetoes:
        return _decision("RULE_AMP_QUALITY_HOLD", "hold", global_vetoes)
    if torque_reduce:
        return _decision(
            "RULE_AMP_TORQUE_REDUCE",
            "mild_decrease",
            ["torque_limit_ratio_above_reduce_threshold"],
        )
    if peak_error is None:
        return _decision("RULE_AMP_UNAVAILABLE_HOLD", "hold", ["peak_error_unavailable"])
    if peak_error < -cfg.peak_flexion_error:
        if torque_veto:
            return _decision(
                "RULE_AMP_INCREASE_TORQUE_VETO",
                "hold",
                ["torque_limit_ratio_above_veto_threshold"],
            )
        return _decision(
            "RULE_AMP_LOW_PEAK_INCREASE",
            "mild_increase",
            [],
            "Measured peak flexion is below reference.",
        )
    if peak_error > cfg.peak_flexion_error:
        return _decision(
            "RULE_AMP_HIGH_PEAK_DECREASE",
            "mild_decrease",
            [],
            "Measured peak flexion is above reference.",
        )
    return _decision("RULE_AMP_WITHIN_BAND_HOLD", "hold", [])


def _suggest_assist_gain(
    tracking_rmse: float | None,
    torque_veto: bool,
    torque_reduce: bool,
    cfg: SuggestionThresholds,
    global_vetoes: list[str],
) -> dict[str, Any]:
    if global_vetoes:
        return _decision("RULE_ASSIST_QUALITY_HOLD", "hold", global_vetoes)
    if torque_reduce:
        return _decision(
            "RULE_ASSIST_TORQUE_REDUCE",
            "mild_decrease",
            ["torque_limit_ratio_above_reduce_threshold"],
        )
    if tracking_rmse is None:
        return _decision("RULE_ASSIST_UNAVAILABLE_HOLD", "hold", ["tracking_rmse_unavailable"])
    if tracking_rmse > cfg.tracking_rmse:
        if torque_veto:
            return _decision(
                "RULE_ASSIST_INCREASE_TORQUE_VETO",
                "hold",
                ["torque_limit_ratio_above_veto_threshold"],
            )
        return _decision(
            "RULE_ASSIST_HIGH_RMSE_INCREASE",
            "mild_increase",
            [],
            "Tracking RMSE is above threshold and torque margin is available.",
        )
    return _decision("RULE_ASSIST_WITHIN_BAND_HOLD", "hold", [])


def _suggest_kp(
    tracking_rmse: float | None,
    torque_veto: bool,
    cfg: SuggestionThresholds,
    global_vetoes: list[str],
) -> dict[str, Any]:
    if global_vetoes:
        return _decision("RULE_KP_QUALITY_HOLD", "hold", global_vetoes)
    if tracking_rmse is None:
        return _decision("RULE_KP_UNAVAILABLE_HOLD", "hold", ["tracking_rmse_unavailable"])
    if tracking_rmse > cfg.tracking_rmse:
        if torque_veto:
            return _decision(
                "RULE_KP_INCREASE_TORQUE_VETO",
                "hold",
                ["torque_limit_ratio_above_veto_threshold"],
            )
        return _decision("RULE_KP_HIGH_RMSE_INCREASE", "mild_increase", [])
    return _decision("RULE_KP_WITHIN_BAND_HOLD", "hold", [])


def _suggest_kd(
    tracking_rmse: float | None,
    torque_veto: bool,
    cfg: SuggestionThresholds,
    global_vetoes: list[str],
) -> dict[str, Any]:
    if global_vetoes:
        return _decision("RULE_KD_QUALITY_HOLD", "hold", global_vetoes)
    if tracking_rmse is None:
        return _decision("RULE_KD_UNAVAILABLE_HOLD", "hold", ["tracking_rmse_unavailable"])
    if tracking_rmse > cfg.tracking_rmse:
        if torque_veto:
            return _decision(
                "RULE_KD_INCREASE_TORQUE_VETO",
                "hold",
                ["torque_limit_ratio_above_veto_threshold"],
            )
        return _decision("RULE_KD_HIGH_RMSE_INCREASE", "mild_increase", [])
    return _decision("RULE_KD_WITHIN_BAND_HOLD", "hold", [])


def _decision(
    rule_id: str,
    action: str,
    veto_reasons: list[str],
    rationale: str = "",
) -> dict[str, Any]:
    return {
        "rule_id": rule_id,
        "action": action,
        "veto_reasons": veto_reasons,
        "rationale": rationale,
    }


def _number_or_none(value: Any) -> float | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:
        return None
    return number
