# 试次数据输入 Schema

本文档定义从 Speedgoat File Log 或离线样例导出的第一版规范试次输入格式。后续步态分析、参数建议和报告生成都应从这个格式读取数据，不直接读取原始 SLRT 日志。

## 目录结构

每个试次一个目录：

```text
data/raw/<trial_id>/
  metadata.json
  signals_wide.csv
```

当前 MATLAB 归档函数 `tools/import_slrt_filelog_trial.m` 会生成：

```text
data/raw/<trial_id>/
  metadata.json
  filelog_dataset.mat
  signals_long.csv
  signals_wide_if_aligned.csv
```

如果所有信号时间戳一致，Python 加载器会优先读取 `signals_wide.csv`，其次读取 `signals_wide_if_aligned.csv`。如果只有 long CSV，后续可再补重采样/对齐逻辑。

## 必需元数据字段

`metadata.json` 至少应包含：

| 字段 | 含义 |
| --- | --- |
| `trial_id` | 试次 ID，应与目录名一致 |
| `application` | SLRT 应用/模型名 |
| `target_name` | Speedgoat target 名称 |
| `affected_side` | 患侧兼容字段；健康受试者建议写 `none` 或 `not_applicable`，不要虚构患侧 |
| `subject_id` | 受试者匿名编号；正式人体试次应使用非空的假名化 ID，不记录姓名等直接标识符 |
| `signals_are_time_aligned` | wide CSV 中各信号是否共享同一时间轴 |

推荐额外包含：

| 字段 | 含义 |
| --- | --- |
| `import_time` | 日志导入时间 |
| `source_start_date` | 目标机日志开始时间 |
| `parameter_snapshot_path` | 本次试次参数快照 JSON 路径 |
| `signal_map` | 将规范字段名映射到 CSV 实际列名 |
| `participant_group` | 受试者分组；当前正式实验计划使用 `healthy` |
| `tested_side` | 本次控制/测试侧，例如 `left`、`right` 或 `bilateral`，不要借用 `affected_side` 表示 |
| `session_id` | 同一受试者的实验场次匿名编号 |
| `condition_id` | 实验条件编号，用于记录基线、人工调参或优化条件 |
| `sensor_set` | 本次使用的传感器集合；当前研究应明确不含 EMG/IMU |

## 必需信号字段

后续分析使用以下规范字段名：

| 规范字段 | 含义 |
| --- | --- |
| `time` | 秒，单调递增 |
| `q_meas` | 实测膝角度 |
| `dq_meas` | 实测膝角速度 |
| `q_ref` | 参考膝角度 |
| `dq_ref` | 参考膝角速度 |
| `feet_load` | 足底负载或接触强度 |
| `phi` | 步态相位 |
| `phase0_event` | 周期边界或相位 0 事件 |
| `tau_e` | 期望/输出辅助力矩或等价力矩信号 |
| `safe_torque` | 安全力矩上限 |
| `assist_enabled` | 助力使能状态，0/1 |

本论文和系统实现不使用 EMG 或 IMU，因此规范输入不要求也不应假设存在 EMG/IMU 字段。模型端口名 `sEMGMuxIn` 是历史命名，当前实际承载足底压力/电压通道；归档和论文写作均应按足底压力解释。

CSV 可以直接使用规范字段名；如果来自真实模型的列名不同，在 `metadata.json` 中添加：

```json
{
  "signal_map": {
    "q_meas": "KneeAngleMeasured",
    "tau_e": "replay_left_torque_filelog"
  }
}
```

## 可选参数快照字段

参数快照可以放在 `metadata.json` 的 `parameters` 对象中，或放在 `parameter_snapshot_path` 指向的 JSON 文件中。

推荐字段：

| 字段 | 含义 |
| --- | --- |
| `Amplitude` | DMP 幅值 |
| `tau` | DMP 时间尺度 |
| `phase_offset` | 相位偏置 |
| `MO_Kp` | 阻抗/PD 比例增益 |
| `MO_Kd` | 阻抗/PD 微分增益 |
| `MO_OverwriteKpGain` | 覆盖增益或等价助力增益 |

## 校验规则

加载器必须检查：

1. `metadata.json` 存在。
2. `signals_wide.csv` 或 `signals_wide_if_aligned.csv` 存在。
3. 所有必需元数据字段存在。
4. 所有必需信号字段可通过列名或 `signal_map` 找到。
5. `time` 非空、数值化、单调递增。
6. 必需信号长度与 `time` 一致，且没有空值或非数值。

缺失字段时，加载器应输出清晰的缺失字段列表，并停止本试次分析。

## 当前最小样例

合成样例位于：

```text
data/fixtures/synthetic_trial_001/
```

可用以下命令校验：

```powershell
python scripts/check_trial_data.py data/fixtures/synthetic_trial_001
```
