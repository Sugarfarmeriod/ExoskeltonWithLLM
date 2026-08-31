from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd


BASE_COLUMNS = [
    "q_meas",
    "dq_meas",
    "q_ref",
    "dq_ref",
    "tau_e",
    "FeetLoad_left",
    "FeetLoad_right",
    "Phi",
    "Phase0Event",
]


FEATURE_COLUMNS = [
    "q_meas",
    "dq_meas",
    "q_ref",
    "dq_ref",
    "e_q",
    "e_dq",
    "tau_e",
    "FeetLoad_left",
    "FeetLoad_right",
    "FeetLoad_sum",
    "FeetLoad_diff",
    "Phi",
    "sin_Phi",
    "cos_Phi",
    "Phase0Event",
    "tau_e_rms",
    "tau_e_peak",
    "tau_e_slope",
    "e_q_rms",
    "e_q_peak",
    "e_q_slope",
    "e_dq_rms",
    "e_dq_peak",
    "e_dq_slope",
]


@dataclass(frozen=True)
class FeatureConfig:
    raw_hz: float = 1000.0
    target_hz: float = 100.0
    rolling_ms: float = 120.0
    contact_threshold: float = 0.1
    transition_ms: float = 120.0
    safe_torque: float = 20.0
    tracking_error_q: float = 0.15
    tracking_error_dq: float = 1.0


def validate_columns(frame: pd.DataFrame, required: Iterable[str] = BASE_COLUMNS) -> None:
    missing = [name for name in required if name not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def downsample_frame(frame: pd.DataFrame, raw_hz: float, target_hz: float) -> pd.DataFrame:
    if target_hz <= 0 or raw_hz <= 0:
        raise ValueError("raw_hz and target_hz must be positive")
    stride = max(int(round(raw_hz / target_hz)), 1)
    return frame.iloc[::stride].reset_index(drop=True)


def add_features(frame: pd.DataFrame, config: FeatureConfig) -> pd.DataFrame:
    validate_columns(frame)
    out = frame.copy()
    out["e_q"] = out["q_ref"] - out["q_meas"]
    out["e_dq"] = out["dq_ref"] - out["dq_meas"]
    out["FeetLoad_sum"] = out["FeetLoad_left"] + out["FeetLoad_right"]
    out["FeetLoad_diff"] = out["FeetLoad_left"] - out["FeetLoad_right"]
    out["sin_Phi"] = np.sin(out["Phi"])
    out["cos_Phi"] = np.cos(out["Phi"])

    rolling = max(int(round(config.rolling_ms / 1000.0 * config.target_hz)), 3)
    for col in ["tau_e", "e_q", "e_dq"]:
        series = out[col].astype(float)
        out[f"{col}_rms"] = np.sqrt(series.pow(2).rolling(rolling, min_periods=1).mean())
        out[f"{col}_peak"] = series.abs().rolling(rolling, min_periods=1).max()
        out[f"{col}_slope"] = series.diff().fillna(0.0) * config.target_hz

    out[FEATURE_COLUMNS] = out[FEATURE_COLUMNS].replace([np.inf, -np.inf], np.nan).fillna(0.0)
    return out


def generate_weak_labels(frame: pd.DataFrame, config: FeatureConfig) -> pd.DataFrame:
    out = frame.copy()
    contact = out["FeetLoad_sum"] > config.contact_threshold
    out["gait_state"] = np.where(contact, 0, 1)  # 0 stance, 1 swing, 2 transition

    event_idx = np.flatnonzero(out["Phase0Event"].to_numpy() > 0.5)
    transition_radius = max(int(round(config.transition_ms / 1000.0 * config.target_hz / 2.0)), 1)
    for idx in event_idx:
        lo = max(idx - transition_radius, 0)
        hi = min(idx + transition_radius + 1, len(out))
        out.loc[lo:hi, "gait_state"] = 2

    abs_tau = out["tau_e"].abs()
    abs_eq = out["e_q"].abs()
    abs_edq = out["e_dq"].abs()
    footload_bad = (out["FeetLoad_left"] < 0) | (out["FeetLoad_right"] < 0)
    tracking_bad = (abs_eq > config.tracking_error_q) | (abs_edq > config.tracking_error_dq)
    torque_bad = abs_tau > 0.8 * config.safe_torque

    out["anomaly_type"] = 0
    out.loc[tracking_bad, "anomaly_type"] = 2
    out.loc[torque_bad, "anomaly_type"] = 3
    out.loc[footload_bad, "anomaly_type"] = 4
    out.loc[out[BASE_COLUMNS].isna().any(axis=1), "anomaly_type"] = 5

    out["risk_level"] = 0
    out.loc[tracking_bad | torque_bad | footload_bad, "risk_level"] = 1
    out.loc[(abs_tau >= config.safe_torque) | (abs_eq > 2 * config.tracking_error_q), "risk_level"] = 2

    out["gate_gain"] = 1.0
    out.loc[out["risk_level"] == 1, "gate_gain"] = 0.5
    out.loc[out["risk_level"] == 2, "gate_gain"] = 0.0
    return out


def inject_synthetic_anomalies(frame: pd.DataFrame, target_hz: float) -> pd.DataFrame:
    out = frame.copy()
    n = len(out)
    if n < int(2 * target_hz):
        return out

    segments = [
        ("footload_dropout", int(0.20 * n), int(0.25 * n)),
        ("phase_shift", int(0.40 * n), int(0.48 * n)),
        ("tracking_mismatch", int(0.60 * n), int(0.68 * n)),
        ("torque_spike", int(0.80 * n), int(0.82 * n)),
    ]

    for kind, lo, hi in segments:
        hi = max(hi, lo + 1)
        if kind == "footload_dropout":
            out.loc[lo:hi, ["FeetLoad_left", "FeetLoad_right"]] = 0.0
            out.loc[lo:hi, "anomaly_type"] = 4
            out.loc[lo:hi, "risk_level"] = 1
        elif kind == "phase_shift":
            out.loc[lo:hi, "Phi"] = out.loc[lo:hi, "Phi"] + np.pi / 4.0
            out.loc[lo:hi, "anomaly_type"] = 1
            out.loc[lo:hi, "risk_level"] = 1
        elif kind == "tracking_mismatch":
            out.loc[lo:hi, "q_ref"] = out.loc[lo:hi, "q_ref"] + 0.25
            out.loc[lo:hi, "anomaly_type"] = 2
            out.loc[lo:hi, "risk_level"] = 1
        elif kind == "torque_spike":
            out.loc[lo:hi, "tau_e"] = out.loc[lo:hi, "tau_e"] * 2.5 + 15.0
            out.loc[lo:hi, "anomaly_type"] = 3
            out.loc[lo:hi, "risk_level"] = 2

    out["gate_gain"] = 1.0
    out.loc[out["risk_level"] == 1, "gate_gain"] = 0.5
    out.loc[out["risk_level"] == 2, "gate_gain"] = 0.0
    return out


def compute_rule_gate(batch_last_values: pd.DataFrame, safe_torque: float = 20.0) -> np.ndarray:
    gate = np.ones(len(batch_last_values), dtype=np.float32)
    abs_tau = batch_last_values["tau_e"].abs().to_numpy()
    abs_eq = batch_last_values["e_q"].abs().to_numpy()
    abs_edq = batch_last_values["e_dq"].abs().to_numpy()

    gate[abs_tau >= 0.8 * safe_torque] = np.minimum(gate[abs_tau >= 0.8 * safe_torque], 0.5)
    gate[abs_tau >= safe_torque] = 0.0
    gate[abs_eq > 0.15] = np.minimum(gate[abs_eq > 0.15], 0.5)
    gate[abs_edq > 1.0] = np.minimum(gate[abs_edq > 1.0], 0.5)
    return gate
