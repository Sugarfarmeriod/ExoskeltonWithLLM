from __future__ import annotations

import argparse
from pathlib import Path

import torch

from features import FEATURE_COLUMNS
from model_tcn_multitask import TCNMultiTaskModel


class OnnxWrapper(torch.nn.Module):
    def __init__(self, model: TCNMultiTaskModel) -> None:
        super().__init__()
        self.model = model

    def forward(self, x):
        out = self.model(x)
        return out["gait_state"], out["anomaly_type"], out["risk_level"], out["gate_gain"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Export MS-TGSS model to ONNX")
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--out", default="ms_tgss.onnx")
    parser.add_argument("--opset", type=int, default=17)
    args = parser.parse_args()

    ckpt = torch.load(args.checkpoint, map_location="cpu")
    model = TCNMultiTaskModel(in_channels=len(FEATURE_COLUMNS), hidden_channels=ckpt["hidden"])
    model.load_state_dict(ckpt["model"])
    model.eval()

    window_size = max(int(round(ckpt["window_ms"] / 1000.0 * ckpt["target_hz"])), 2)
    dummy = torch.randn(1, len(FEATURE_COLUMNS), window_size)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    torch.onnx.export(
        OnnxWrapper(model),
        dummy,
        out_path,
        input_names=["input_window"],
        output_names=["gait_state_logits", "anomaly_type_logits", "risk_level_logits", "gate_gain"],
        dynamic_axes={"input_window": {0: "batch"}, "gate_gain": {0: "batch"}},
        opset_version=args.opset,
    )
    print(f"Exported ONNX model to {out_path}")


if __name__ == "__main__":
    main()
