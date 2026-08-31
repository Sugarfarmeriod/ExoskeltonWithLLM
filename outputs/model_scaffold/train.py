from __future__ import annotations

import argparse
import json
from pathlib import Path

import torch
from torch.utils.data import DataLoader

from dataset import load_datasets
from features import FEATURE_COLUMNS, FeatureConfig
from model_tcn_multitask import TCNMultiTaskModel, multitask_loss


def parse_paths(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def train_one_epoch(model, loader, optimizer, device):
    model.train()
    total = 0.0
    for batch in loader:
        batch = {k: v.to(device) for k, v in batch.items()}
        optimizer.zero_grad(set_to_none=True)
        outputs = model(batch["x"])
        loss = multitask_loss(outputs, batch)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
        optimizer.step()
        total += loss.item() * batch["x"].size(0)
    return total / len(loader.dataset)


@torch.no_grad()
def validate(model, loader, device):
    model.eval()
    total = 0.0
    correct = {"gait_state": 0, "anomaly_type": 0, "risk_level": 0}
    count = 0
    for batch in loader:
        batch = {k: v.to(device) for k, v in batch.items()}
        outputs = model(batch["x"])
        total += multitask_loss(outputs, batch).item() * batch["x"].size(0)
        for key in correct:
            pred = outputs[key].argmax(dim=1)
            correct[key] += (pred == batch[key]).sum().item()
        count += batch["x"].size(0)
    metrics = {f"{key}_acc": value / max(count, 1) for key, value in correct.items()}
    metrics["loss"] = total / len(loader.dataset)
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="Train MS-TGSS TCN multitask model")
    parser.add_argument("--train", required=True, help="Comma-separated training CSV paths")
    parser.add_argument("--val", required=True, help="Comma-separated validation CSV paths")
    parser.add_argument("--out-dir", default="runs/ms_tgss")
    parser.add_argument("--raw-hz", type=float, default=1000.0)
    parser.add_argument("--target-hz", type=float, default=100.0)
    parser.add_argument("--window-ms", type=float, default=400.0)
    parser.add_argument("--stride-ms", type=float, default=50.0)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--hidden", type=int, default=64)
    parser.add_argument("--inject-anomalies", action="store_true")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    config = FeatureConfig(raw_hz=args.raw_hz, target_hz=args.target_hz)
    train_set, val_set = load_datasets(
        parse_paths(args.train),
        parse_paths(args.val),
        config,
        window_ms=args.window_ms,
        stride_ms=args.stride_ms,
        inject_anomalies=args.inject_anomalies,
    )
    train_loader = DataLoader(train_set, batch_size=args.batch_size, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_set, batch_size=args.batch_size, shuffle=False, num_workers=0)

    model = TCNMultiTaskModel(in_channels=len(FEATURE_COLUMNS), hidden_channels=args.hidden).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)

    best_loss = float("inf")
    for epoch in range(1, args.epochs + 1):
        train_loss = train_one_epoch(model, train_loader, optimizer, device)
        val_metrics = validate(model, val_loader, device)
        print(
            f"epoch={epoch:03d} train_loss={train_loss:.4f} "
            f"val_loss={val_metrics['loss']:.4f} "
            f"gait_acc={val_metrics['gait_state_acc']:.3f} "
            f"anomaly_acc={val_metrics['anomaly_type_acc']:.3f} "
            f"risk_acc={val_metrics['risk_level_acc']:.3f}"
        )
        if val_metrics["loss"] < best_loss:
            best_loss = val_metrics["loss"]
            torch.save(
                {
                    "model": model.state_dict(),
                    "feature_columns": FEATURE_COLUMNS,
                    "standardizer": train_set.standardizer.state_dict(),
                    "config": vars(config),
                    "window_ms": args.window_ms,
                    "target_hz": args.target_hz,
                    "hidden": args.hidden,
                },
                out_dir / "best_model.pt",
            )

    with open(out_dir / "training_config.json", "w", encoding="utf-8") as f:
        json.dump(vars(args), f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
