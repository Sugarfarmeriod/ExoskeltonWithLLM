from __future__ import annotations

import torch
from torch import nn
from torch.nn import functional as F


class TemporalBlock(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int, dilation: int, dropout: float) -> None:
        super().__init__()
        padding = (kernel_size - 1) * dilation // 2
        self.conv1 = nn.Conv1d(in_channels, out_channels, kernel_size, padding=padding, dilation=dilation)
        self.bn1 = nn.BatchNorm1d(out_channels)
        self.conv2 = nn.Conv1d(out_channels, out_channels, kernel_size, padding=padding, dilation=dilation)
        self.bn2 = nn.BatchNorm1d(out_channels)
        self.dropout = nn.Dropout(dropout)
        self.proj = nn.Conv1d(in_channels, out_channels, 1) if in_channels != out_channels else nn.Identity()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        residual = self.proj(x)
        y = self.dropout(F.relu(self.bn1(self.conv1(x))))
        y = self.dropout(F.relu(self.bn2(self.conv2(y))))
        return F.relu(y + residual)


class AttentionPooling(nn.Module):
    def __init__(self, channels: int) -> None:
        super().__init__()
        self.score = nn.Sequential(
            nn.Conv1d(channels, channels // 2, kernel_size=1),
            nn.Tanh(),
            nn.Conv1d(channels // 2, 1, kernel_size=1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        weights = torch.softmax(self.score(x), dim=-1)
        return torch.sum(x * weights, dim=-1)


class TCNMultiTaskModel(nn.Module):
    def __init__(
        self,
        in_channels: int,
        hidden_channels: int = 64,
        num_blocks: int = 4,
        kernel_size: int = 5,
        dropout: float = 0.15,
    ) -> None:
        super().__init__()
        blocks = []
        channels = in_channels
        for idx in range(num_blocks):
            blocks.append(
                TemporalBlock(
                    channels,
                    hidden_channels,
                    kernel_size=kernel_size,
                    dilation=2**idx,
                    dropout=dropout,
                )
            )
            channels = hidden_channels
        self.backbone = nn.Sequential(*blocks)
        self.pool = AttentionPooling(hidden_channels)
        self.shared = nn.Sequential(
            nn.Linear(hidden_channels, hidden_channels),
            nn.ReLU(),
            nn.Dropout(dropout),
        )
        self.gait_state_head = nn.Linear(hidden_channels, 3)
        self.anomaly_type_head = nn.Linear(hidden_channels, 6)
        self.risk_level_head = nn.Linear(hidden_channels, 3)
        self.gate_gain_head = nn.Sequential(nn.Linear(hidden_channels, 1), nn.Sigmoid())

    def forward(self, x: torch.Tensor) -> dict[str, torch.Tensor]:
        z = self.backbone(x)
        pooled = self.pool(z)
        h = self.shared(pooled)
        return {
            "gait_state": self.gait_state_head(h),
            "anomaly_type": self.anomaly_type_head(h),
            "risk_level": self.risk_level_head(h),
            "gate_gain": self.gate_gain_head(h).squeeze(-1),
        }


def multitask_loss(outputs: dict[str, torch.Tensor], batch: dict[str, torch.Tensor]) -> torch.Tensor:
    loss_gait = F.cross_entropy(outputs["gait_state"], batch["gait_state"])
    loss_anomaly = F.cross_entropy(outputs["anomaly_type"], batch["anomaly_type"])
    loss_risk = F.cross_entropy(outputs["risk_level"], batch["risk_level"])
    loss_gate = F.smooth_l1_loss(outputs["gate_gain"], batch["gate_gain"])
    return loss_gait + loss_anomaly + loss_risk + 0.5 * loss_gate
