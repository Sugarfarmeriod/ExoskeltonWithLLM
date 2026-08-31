"""Build a compact Markdown summary of signal candidate groups."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = PROJECT_ROOT / "tools" / "generated"
INPUT_JSON = GENERATED_DIR / "teststructure_signal_candidates.json"
OUTPUT_MD = GENERATED_DIR / "teststructure_signal_candidate_summary.md"


def main() -> int:
    payload = json.loads(INPUT_JSON.read_text(encoding="utf-8"))
    groups = sorted(
        payload["groups"],
        key=lambda item: item["recommended_count"],
        reverse=True,
    )
    candidates = payload["candidates"]

    lines = [
        "# TestStructure 信号候选摘要",
        "",
        f"- 模型: `{payload['model']}`",
        f"- 候选连线/信号: `{payload['total_candidates']}`",
        f"- 推荐高亮候选: `{sum(1 for c in candidates if c['recommended'])}`",
        f"- 生成方式: `{payload['method']}`",
        "",
        "## 高相关模块 Top 30",
        "",
        "| 模块路径 | 候选数 | 推荐数 |",
        "| --- | ---: | ---: |",
    ]
    for group in groups[:30]:
        if group["recommended_count"] == 0:
            continue
        lines.append(
            f"| `{group['group_path']}` | {group['candidate_count']} | {group['recommended_count']} |"
        )

    lines.extend(
        [
            "",
            "## 优先查看的模块",
            "",
            "- `TestStructure/InterForceControlTask`：控制主链路入口，能看到 AO、DMP、TorqueController、Torque_Guard 之间的外部连线。",
            "- `TestStructure/InterForceControlTask/AO*`：相位、足底负载、Phase0Event 相关候选。",
            "- `TestStructure/InterForceControlTask/DMP`：DMP 轨迹和参数相关候选。",
            "- `TestStructure/InterForceControlTask/TorqueController*`：Kp/Kd、助力增益和力矩控制相关候选。",
            "- `TestStructure/InterForceControlTask/Torque_Guard`：安全限幅和最终力矩保护相关候选。",
            "- `TestStructure/InterForceControlTask/Bus Selector`：电机位置、速度、传感器、力矩等总线拆分候选。",
            "",
            "## 页面使用建议",
            "",
            "1. 打开 `tools/generated/teststructure_signal_selector.html`。",
            "2. 先点“只看推荐”，再按模块路径批量勾选。",
            "3. 优先筛选关键词：`Phi`、`Phase0Event`、`FeetLoad`、`DMP`、`Torque`、`Kp`、`Kd`。",
            "4. 勾选后点“生成选择 JSON”，把右侧 JSON 发回来，我再据此给你生成 `signal_map` 和 File Log 接线清单。",
        ]
    )

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote summary: {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
