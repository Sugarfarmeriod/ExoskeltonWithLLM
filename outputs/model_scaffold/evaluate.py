from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error
from torch.utils.data import DataLoader

from dataset import GaitWindowDataset, prepare_frame
from features import FEATURE_COLUMNS, FeatureConfig, compute_rule_gate
from model_tcn_multitask import TCNMultiTaskModel


@torch.no_grad()
def collect_predictions(model, loader, device):
    model.eval()
    y_true = {"gait_state": [], "anomaly_type": [], "risk_level": [], "gate_gain": []}
    y_pred = {"gait_state": [], "anomaly_type": [], "risk_level": [], "gate_gain": []}
    for batch in loader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(batch["x"])
        for key in ["gait_state", "anomaly_type", "risk_level"]:
            y_true[key].extend(batch[key].cpu().numpy().tolist())
            y_pred[key].extend(outputs[key].argmax(dim=1).cpu().numpy().tolist())
        y_true["gate_gain"].extend(batch["gate_gain"].cpu().numpy().tolist())
        y_pred["gate_gain"].extend(outputs["gate_gain"].cpu().numpy().tolist())
    return y_true, y_pred


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate MS-TGSS model")
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--data", required=True, help="CSV path for evaluation")
    parser.add_argument("--out-dir", default="runs/ms_tgss_eval")
    parser.add_argument("--batch-size", type=int, default=128)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    ckpt = torch.load(args.checkpoint, map_location=device)
    config = FeatureConfig(**ckpt["config"])
    frame = prepare_frame(args.data, config, inject_anomalies=False)
    window_size = max(int(round(ckpt["window_ms"] / 1000.0 * ckpt["target_hz"])), 2)
    dataset = GaitWindowDataset([frame], window_size, stride=1, fit_standardizer=False)
    dataset.standardizer.load_state_dict(ckpt["standardizer"])

    model = TCNMultiTaskModel(in_channels=len(FEATURE_COLUMNS), hidden_channels=ckpt["hidden"]).to(device)
    model.load_state_dict(ckpt["model"])
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False)

    y_true, y_pred = collect_predictions(model, loader, device)
    report_lines = []
    for key in ["gait_state", "anomaly_type", "risk_level"]:
        report_lines.append(f"# {key}\n")
        report_lines.append(classification_report(y_true[key], y_pred[key], zero_division=0))
        report_lines.append(f"confusion_matrix:\n{confusion_matrix(y_true[key], y_pred[key])}\n")
    report_lines.append(f"# gate_gain\nMAE: {mean_absolute_error(y_true['gate_gain'], y_pred['gate_gain']):.4f}\n")
    (out_dir / "metrics.txt").write_text("\n".join(report_lines), encoding="utf-8")

    starts = [start for _, start in dataset.index]
    last_rows = frame.iloc[[start + window_size - 1 for start in starts]].reset_index(drop=True)
    gate_gain_rule = compute_rule_gate(last_rows)
    gate_gain_pred = np.asarray(y_pred["gate_gain"], dtype=np.float32)
    risk_pred = np.asarray(y_pred["risk_level"], dtype=np.int64)
    gate_gain_final = np.minimum(gate_gain_pred, gate_gain_rule)
    gate_gain_final[risk_pred == 2] = 0.0
    caution = risk_pred == 1
    gate_gain_final[caution] = np.clip(gate_gain_final[caution], 0.3, 0.7)
    tau_gate = gate_gain_final * last_rows["tau_e"].to_numpy(np.float32)

    playback = pd.DataFrame(
        {
            "sample_index": [start + window_size - 1 for start in starts],
            "gait_state_pred": y_pred["gait_state"],
            "anomaly_type_pred": y_pred["anomaly_type"],
            "risk_level_pred": y_pred["risk_level"],
            "gate_gain_pred": gate_gain_pred,
            "gate_gain_rule": gate_gain_rule,
            "gate_gain_final": gate_gain_final,
            "tau_e": last_rows["tau_e"].to_numpy(np.float32),
            "tau_gate": tau_gate,
        }
    )
    playback.to_csv(out_dir / "simulink_playback_predictions.csv", index=False)
    print(f"Wrote metrics and playback CSV to {out_dir}")


if __name__ == "__main__":
    main()
