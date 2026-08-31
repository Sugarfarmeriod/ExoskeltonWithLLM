# TestStructure 信号候选摘要

- 模型: `TestStructure`
- 候选连线/信号: `2856`
- 推荐高亮候选: `814`
- 生成方式: `static_slx_xml_parse`

## 高相关模块 Top 30

| 模块路径 | 候选数 | 推荐数 |
| --- | ---: | ---: |
| `TestStructure/InterForceControlTask/DMP` | 75 | 75 |
| `TestStructure/InterForceControlTask/AO2/PhaseCorrection` | 70 | 70 |
| `TestStructure/InterForceControlTask/TorqueController/Subsystem2` | 60 | 60 |
| `TestStructure/InterForceControlTask/DMP/cuur_params1` | 42 | 42 |
| `TestStructure/InterForceControlTask/AO1/Subsystem` | 173 | 34 |
| `TestStructure/InterForceControlTask/AO2/Subsystem` | 173 | 34 |
| `TestStructure/InterForceControlTask/AO3/Subsystem` | 173 | 34 |
| `TestStructure/InterForceControlTask/DMP/Subsystem` | 32 | 32 |
| `TestStructure/InterForceControlTask/AO/PhaseCorrection` | 30 | 30 |
| `TestStructure/InterForceControlTask/AO1/PhaseCorrection` | 29 | 29 |
| `TestStructure/InterForceControlTask/TorqueController` | 29 | 29 |
| `TestStructure/InterForceControlTask` | 55 | 26 |
| `TestStructure/InterForceControlTask/AO3/PhaseCorrection` | 25 | 25 |
| `TestStructure/InterForceControlTask/DMP/MATLAB Function8` | 24 | 24 |
| `TestStructure/InterForceControlTask/TorqueController2/ZeroCrossFinder_Right` | 20 | 20 |
| `TestStructure/InterForceControlTask/DMP/MATLAB Function6` | 19 | 19 |
| `TestStructure/InterForceControlTask/Torque_Guard/LimitProtect` | 19 | 19 |
| `TestStructure/InterForceControlTask/TorqueController/TorqueManager` | 19 | 19 |
| `TestStructure/InterForceControlTask/Torque_Guard` | 17 | 17 |
| `TestStructure/InterForceControlTask/TorqueController2` | 15 | 15 |
| `TestStructure/InterForceControlTask/AO/Select` | 53 | 10 |
| `TestStructure/InterForceControlTask/AO1/Select` | 52 | 10 |
| `TestStructure/InterForceControlTask/AO2/Select` | 46 | 9 |
| `TestStructure/InterForceControlTask/AO3/Select` | 46 | 9 |
| `TestStructure/InterForceControlTask/DMP/compute_chunk2` | 9 | 9 |
| `TestStructure/InterForceControlTask/AO` | 23 | 8 |
| `TestStructure/InterForceControlTask/AO2` | 15 | 7 |
| `TestStructure/InterForceControlTask/DMP/MATLAB Function3` | 7 | 7 |
| `TestStructure/InterForceControlTask/TorqueController2/MATLAB Function` | 7 | 7 |
| `TestStructure/InterForceControlTask/AO1` | 14 | 6 |

## 优先查看的模块

- `TestStructure/InterForceControlTask`：控制主链路入口，能看到 AO、DMP、TorqueController、Torque_Guard 之间的外部连线。
- `TestStructure/InterForceControlTask/AO*`：相位、足底负载、Phase0Event 相关候选。
- `TestStructure/InterForceControlTask/DMP`：DMP 轨迹和参数相关候选。
- `TestStructure/InterForceControlTask/TorqueController*`：Kp/Kd、助力增益和力矩控制相关候选。
- `TestStructure/InterForceControlTask/Torque_Guard`：安全限幅和最终力矩保护相关候选。
- `TestStructure/InterForceControlTask/Bus Selector`：电机位置、速度、传感器、力矩等总线拆分候选。

## 页面使用建议

1. 打开 `tools/generated/teststructure_signal_selector.html`。
2. 先点“只看推荐”，再按模块路径批量勾选。
3. 优先筛选关键词：`Phi`、`Phase0Event`、`FeetLoad`、`DMP`、`Torque`、`Kp`、`Kd`。
4. 勾选后点“生成选择 JSON”，把右侧 JSON 发回来，我再据此给你生成 `signal_map` 和 File Log 接线清单。