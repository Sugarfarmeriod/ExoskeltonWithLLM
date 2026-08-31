from __future__ import annotations

from pathlib import Path
from typing import Sequence

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset

from features import (
    FEATURE_COLUMNS,
    FeatureConfig,
    add_features,
    downsample_frame,
    generate_weak_labels,
    inject_synthetic_anomalies,
)


LABEL_COLUMNS = ["gait_state", "anomaly_type", "risk_level", "gate_gain"]


class Standardizer:
    def __init__(self) -> None:
        self.mean_: np.ndarray | None = None
        self.std_: np.ndarray | None = None

    def fit(self, values: np.ndarray) -> "Standardizer":
        self.mean_ = values.mean(axis=0)
        self.std_ = values.std(axis=0)
        self.std_[self.std_ < 1e-6] = 1.0
        return self

    def transform(self, values: np.ndarray) -> np.ndarray:
        if self.mean_ is None or self.std_ is None:
            raise RuntimeError("Standardizer must be fitted before transform")
        return (values - self.mean_) / self.std_

    def state_dict(self) -> dict[str, list[float]]:
        if self.mean_ is None or self.std_ is None:
            raise RuntimeError("Standardizer is not fitted")
        return {"mean": self.mean_.tolist(), "std": self.std_.tolist()}

    def load_state_dict(self, state: dict[str, Sequence[float]]) -> None:
        self.mean_ = np.asarray(state["mean"], dtype=np.float32)
        self.std_ = np.asarray(state["std"], dtype=np.float32)


def read_table(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() == ".mat":
        try:
            from scipy.io import loadmat
        except ImportError as exc:
            raise ImportError("Install scipy to read MAT files") from exc
        data = loadmat(path)
        table_keys = [k for k, v in data.items() if not k.startswith("__") and getattr(v, "ndim", 0) == 2]
        if not table_keys:
            raise ValueError(f"No 2D arrays found in {path}")
        arr = data[table_keys[0]]
        raise ValueError(
            "MAT loading found a matrix but no column names. Export a CSV table from MATLAB, "
            "or adapt read_table() to your MAT structure."
        )
    raise ValueError(f"Unsupported file type: {path.suffix}")


def prepare_frame(path: str | Path, config: FeatureConfig, inject_anomalies: bool = False) -> pd.DataFrame:
    frame = read_table(path)
    frame = downsample_frame(frame, config.raw_hz, config.target_hz)
    frame = add_features(frame, config)
    frame = generate_weak_labels(frame, config)
    if inject_anomalies:
        frame = inject_synthetic_anomalies(frame, config.target_hz)
        frame = add_features(frame, config)
    return frame


class GaitWindowDataset(Dataset):
    def __init__(
        self,
        frames: Sequence[pd.DataFrame],
        window_size: int,
        stride: int,
        standardizer: Standardizer | None = None,
        fit_standardizer: bool = False,
    ) -> None:
        self.window_size = window_size
        self.stride = stride
        self.frames = list(frames)
        self.index: list[tuple[int, int]] = []
        for frame_idx, frame in enumerate(self.frames):
            max_start = len(frame) - window_size
            for start in range(0, max_start + 1, stride):
                self.index.append((frame_idx, start))

        if not self.index:
            raise ValueError("No windows generated. Check window_size, stride, and data length.")

        self.standardizer = standardizer or Standardizer()
        if fit_standardizer:
            all_values = np.vstack([frame[FEATURE_COLUMNS].to_numpy(np.float32) for frame in self.frames])
            self.standardizer.fit(all_values)

    def __len__(self) -> int:
        return len(self.index)

    def __getitem__(self, idx: int) -> dict[str, torch.Tensor]:
        frame_idx, start = self.index[idx]
        frame = self.frames[frame_idx]
        stop = start + self.window_size
        window = frame.iloc[start:stop]
        x = window[FEATURE_COLUMNS].to_numpy(np.float32)
        x = self.standardizer.transform(x)
        x = np.transpose(x, (1, 0))

        label_row = window.iloc[-1]
        return {
            "x": torch.from_numpy(x),
            "gait_state": torch.tensor(int(label_row["gait_state"]), dtype=torch.long),
            "anomaly_type": torch.tensor(int(label_row["anomaly_type"]), dtype=torch.long),
            "risk_level": torch.tensor(int(label_row["risk_level"]), dtype=torch.long),
            "gate_gain": torch.tensor(float(label_row["gate_gain"]), dtype=torch.float32),
        }


def load_datasets(
    train_paths: Sequence[str | Path],
    val_paths: Sequence[str | Path],
    config: FeatureConfig,
    window_ms: float,
    stride_ms: float,
    inject_anomalies: bool,
) -> tuple[GaitWindowDataset, GaitWindowDataset]:
    window_size = max(int(round(window_ms / 1000.0 * config.target_hz)), 2)
    stride = max(int(round(stride_ms / 1000.0 * config.target_hz)), 1)

    train_frames = [prepare_frame(path, config, inject_anomalies=inject_anomalies) for path in train_paths]
    val_frames = [prepare_frame(path, config, inject_anomalies=False) for path in val_paths]

    standardizer = Standardizer()
    train_set = GaitWindowDataset(train_frames, window_size, stride, standardizer, fit_standardizer=True)
    val_set = GaitWindowDataset(val_frames, window_size, stride, train_set.standardizer, fit_standardizer=False)
    return train_set, val_set
