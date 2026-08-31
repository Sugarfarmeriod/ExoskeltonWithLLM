"""Generate traceable Markdown reports from metrics and suggestion JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ReportInputError(ValueError):
    """Raised when report inputs are not structured analysis outputs."""


REQUIRED_METRICS_KEYS = ("trial", "metrics", "quality", "events", "cycles")
REQUIRED_SUGGESTION_KEYS = (
    "trial",
    "source_metrics",
    "thresholds",
    "suggestions",
    "human_confirmation_required",
)


def generate_report(
    metrics_json: str | Path,
    suggestion_json: str | Path,
    output_path: str | Path,
) -> str:
    metrics = _load_json(metrics_json, REQUIRED_METRICS_KEYS, "gait metrics")
    suggestion = _load_json(
        suggestion_json,
        REQUIRED_SUGGESTION_KEYS,
        "parameter suggestion",
    )
    report = render_report(metrics, suggestion)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
    return report


def render_report(metrics: dict[str, Any], suggestion: dict[str, Any]) -> str:
    trial = metrics["trial"]
    quality = metrics["quality"]
    metric_values = metrics["metrics"]
    suggestions = suggestion["suggestions"]
    source_metrics = suggestion["source_metrics"]

    unsupported = validate_traceability(metrics, suggestion)
    lines = [
        f"# 试次诊断报告: {trial.get('trial_id', '')}",
        "",
        "## 试次身份",
        "",
        f"- 应用: `{trial.get('application', '')}`",
        f"- 患侧: `{trial.get('affected_side', '')}`",
        f"- 样本数: `{trial.get('sample_count', '')}`",
        f"- 时长: `{_fmt(trial.get('duration_seconds'))}` 秒",
        "",
        "## 数据质量",
        "",
        f"- 有效周期数: `{quality.get('valid_cycle_count')}`",
        f"- 参数建议可用: `{quality.get('is_usable_for_parameter_suggestion')}`",
        f"- 质量警告: `{'; '.join(quality.get('warnings', [])) or '无'}`",
        "",
        "## 关键指标",
        "",
        f"- 相位延迟: `{_fmt(metric_values.get('phase_delay_seconds'))}` 秒",
        f"- 峰值屈曲误差: `{_fmt(metric_values.get('peak_flexion_error'))}`",
        f"- Tracking RMSE: `{_fmt(metric_values.get('tracking_rmse'))}`",
        f"- 力矩峰值绝对值: `{_fmt(metric_values.get('torque_peak_abs'))}`",
        f"- 力矩 RMS: `{_fmt(metric_values.get('torque_rms'))}`",
        f"- 力矩限幅比例: `{_fmt(metric_values.get('torque_limit_ratio'))}`",
        "",
        "## 建议摘要",
        "",
    ]

    for parameter_name in ("phase_offset", "Amplitude", "assist_gain", "MO_Kp", "MO_Kd"):
        decision = suggestions.get(parameter_name, {})
        vetoes = decision.get("veto_reasons", [])
        lines.append(
            "- "
            f"`{parameter_name}`: `{decision.get('action', 'unknown')}` "
            f"via `{decision.get('rule_id', 'unknown')}`; "
            f"否决原因: `{'; '.join(vetoes) or '无'}`"
        )

    lines.extend(
        [
            "",
            "## 安全检查",
            "",
            f"- 力矩限幅比例来源: `{source_metrics.get('torque_limit_ratio')}`",
            f"- 全局否决: `{'; '.join(suggestion.get('global_vetoes', [])) or '无'}`",
            f"- 人工确认 required: `{suggestion.get('human_confirmation_required')}`",
            "",
            "## 可追溯性检查",
            "",
            f"- Unsupported claims: `{'; '.join(unsupported) or '无'}`",
            "",
            "## 人工确认状态",
            "",
            "- 状态: `pending_human_review`",
            "- 说明: 本报告只解释离线分析和规则建议，不会自动写入 Speedgoat 或 Simulink 参数。",
            "",
        ]
    )
    return "\n".join(lines)


def validate_traceability(
    metrics: dict[str, Any],
    suggestion: dict[str, Any],
) -> list[str]:
    """Return unsupported claim markers for missing source fields."""

    missing: list[str] = []
    for field in (
        "phase_delay_seconds",
        "peak_flexion_error",
        "tracking_rmse",
        "torque_peak_abs",
        "torque_rms",
        "torque_limit_ratio",
    ):
        if field not in metrics.get("metrics", {}):
            missing.append(f"metrics.{field}")
    for field in ("phase_offset", "Amplitude", "assist_gain", "MO_Kp", "MO_Kd"):
        decision = suggestion.get("suggestions", {}).get(field)
        if not isinstance(decision, dict) or "rule_id" not in decision or "action" not in decision:
            missing.append(f"suggestions.{field}")
    return missing


def _load_json(path: str | Path, required_keys: tuple[str, ...], label: str) -> dict[str, Any]:
    json_path = Path(path)
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ReportInputError(f"Invalid {label} JSON: {json_path}: {exc}") from exc
    missing = [key for key in required_keys if key not in data]
    if missing:
        raise ReportInputError(
            f"Input is not structured {label}; missing keys: {', '.join(missing)}"
        )
    return data


def _fmt(value: Any) -> str:
    if value is None:
        return "不可用"
    if isinstance(value, (int, float)):
        return f"{value:.6g}"
    return str(value)
