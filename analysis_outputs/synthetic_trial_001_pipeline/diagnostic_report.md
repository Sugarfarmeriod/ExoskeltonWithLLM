# 试次诊断报告: synthetic_trial_001

## 试次身份

- 应用: `synthetic_fixture`
- 患侧: `right`
- 样本数: `11`
- 时长: `1` 秒

## 数据质量

- 有效周期数: `1`
- 参数建议可用: `True`
- 质量警告: `无`

## 关键指标

- 相位延迟: `0` 秒
- 峰值屈曲误差: `-0.02`
- Tracking RMSE: `0.0312861`
- 力矩峰值绝对值: `1.45`
- 力矩 RMS: `0.980737`
- 力矩限幅比例: `0.18125`

## 建议摘要

- `phase_offset`: `hold` via `RULE_PHASE_WITHIN_BAND_HOLD`; 否决原因: `无`
- `Amplitude`: `hold` via `RULE_AMP_WITHIN_BAND_HOLD`; 否决原因: `无`
- `assist_gain`: `hold` via `RULE_ASSIST_WITHIN_BAND_HOLD`; 否决原因: `无`
- `MO_Kp`: `hold` via `RULE_KP_WITHIN_BAND_HOLD`; 否决原因: `无`
- `MO_Kd`: `hold` via `RULE_KD_WITHIN_BAND_HOLD`; 否决原因: `无`

## 安全检查

- 力矩限幅比例来源: `0.18125`
- 全局否决: `无`
- 人工确认 required: `True`

## 可追溯性检查

- Unsupported claims: `无`

## 人工确认状态

- 状态: `pending_human_review`
- 说明: 本报告只解释离线分析和规则建议，不会自动写入 Speedgoat 或 Simulink 参数。
