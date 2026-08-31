# MS-TGSS 技术架构说明

系统名称：**Multi-source Temporal Gait State and Safety Supervisor for DMP-Impedance Knee Exoskeleton**

简称：**MS-TGSS / MT-GSS**

## 1. 设计边界

MS-TGSS 不替代现有 AO、DMP、TorqueController、Torque_Guard 和 Saturation。它插入在 `TorqueController` 和 `Torque_Guard` 之间，对 `tau_e` 做安全门控：

```text
AO / gait phase estimation
-> DMP reference generation
-> TorqueController / PD or impedance control
-> MS-TGSS safety supervisor
-> Torque_Guard
-> Saturation
-> torque output
```

核心原则：

- 神经网络不直接输出实时力矩。
- 最终力矩仍经过 `Torque_Guard` 和 `Saturation`。
- 模型只输出状态、风险和门控建议。
- 规则层对模型输出做最终约束。
- DMP/阻抗参数修正只在低频、有限边界、可审计条件下发生。

## 2. 输入与输出

### 输入信号

建议从 1 kHz 原始日志降采样到 100 Hz 或 200 Hz。模型窗口长度为 300-500 ms。MVP 可先用 400 ms、100 Hz，即每窗口 40 个采样点。

基础输入通道：

- `q_meas`
- `dq_meas`
- `q_ref`
- `dq_ref`
- `e_q = q_ref - q_meas`
- `e_dq = dq_ref - dq_meas`
- `tau_e`
- `FeetLoad_left`
- `FeetLoad_right`
- `Phi`
- `sin(Phi)`
- `cos(Phi)`
- `Phase0Event`

补充特征：

- `tau_e` moving RMS / peak / slope
- `e_q` moving RMS / peak / slope
- `e_dq` moving RMS / peak / slope
- FeetLoad 左右差、总和、变化率
- Phase0Event 周期估计与周期异常标志

### 模型输出

多任务输出头：

- `gait_state_head`: `stance / swing / transition`
- `anomaly_type_head`: `normal / phase_mismatch / tracking_error / torque_risk / footload_inconsistency / sensor_fault`
- `risk_level_head`: `normal / caution / danger`
- `gate_gain_head`: 连续 `0..1`，部署时可离散成 `1.0 / 0.5 / 0.0`

部署输出：

```text
gate_gain_final = min(gate_gain_pred, gate_gain_rule)
tau_gate = gate_gain_final * tau_e
```

## 3. 模型结构

主干网络采用 **TCN + Attention Pooling**：

1. 输入张量形状为 `[batch, channels, time]`。
2. TCN 使用多层 dilated Conv1D，覆盖 300-500 ms 时序上下文。
3. Residual block 保留局部动态，dropout 控制过拟合。
4. Attention pooling 对时间维做加权汇聚，避免只取最后一帧。
5. 四个输出头分别学习步态状态、异常类型、风险级别和门控增益。

这个复杂度高于规则分类器，但仍能在 1-2 个月内完成数据集、训练、离线评估和 Simulink 回放验证。

## 4. 标签生成

标签不依赖昂贵外部设备，优先使用现有 Speedgoat/Simulink 可记录信号生成弱标签。

### gait_state 标签

- `FeetLoad` 高于接触阈值：stance。
- `FeetLoad` 低于接触阈值：swing。
- `Phase0Event` 前后小窗口：transition。
- 左右足底压力不一致时，用被控腿 `MO_<WhichFoot>` 对应侧优先。

### anomaly_type 标签

- `normal`: 正常行走窗口，无显著异常。
- `phase_mismatch`: `Phi` 与 `Phase0Event` 周期不一致，或注入 Phi phase shift。
- `tracking_error`: `abs(e_q)` 或 `abs(e_dq)` 超过训练集正常分布阈值。
- `torque_risk`: `abs(tau_e)` 接近 `SafeTorque` 或出现 spike。
- `footload_inconsistency`: FeetLoad dropout、左右负载逻辑冲突、接触状态与相位冲突。
- `sensor_fault`: 信号 NaN、常值、突变、长时间 dropout。

### risk_level 标签

- `normal`: 信号一致，误差和力矩处于正常范围。
- `caution`: 单一异常、轻微 tracking error、短时 footload inconsistency、周期轻微异常。
- `danger`: `tau_e` 接近或超过安全阈值、严重 tracking mismatch、多源信号互相冲突、传感器故障持续。

### gate_gain 标签

- `normal`: `1.0`
- `caution`: `0.3-0.7`，可按异常强度线性降低。
- `danger`: `0.0`

## 5. 规则约束安全层

神经网络输出不能直接决定最终门控。规则层至少包含：

- `abs(tau_e) >= SafeTorque`: `gate_gain_rule = 0`
- `abs(tau_e) >= 0.8 * SafeTorque`: `gate_gain_rule <= 0.5`
- tracking error 超阈值：`gate_gain_rule <= 0.5`
- FeetLoad 与 `Phi`/`Phase0Event` 冲突：`gate_gain_rule <= 0.5`
- Phase0Event 周期过短、过长、丢失：`gate_gain_rule <= 0.5` 或 `0`
- 传感器 NaN、常值、明显 dropout：`gate_gain_rule = 0`

最终逻辑：

```text
gate_gain_final = min(gate_gain_pred, gate_gain_rule)

if risk_level == danger:
    gate_gain_final = 0
elif risk_level == caution:
    gate_gain_final = clamp(gate_gain_final, 0.3, 0.7)
else:
    gate_gain_final = min(gate_gain_final, 1.0)

tau_gate = gate_gain_final * tau_e
```

## 6. Simulink 接入方式

### 离线回放阶段

1. 从 Simulink/Speedgoat 导出 CSV 或 MAT 表格。
2. Python 生成窗口、标签和模型预测。
3. 导出每个时刻的 `gait_state`, `anomaly_type`, `risk_level`, `gate_gain_pred`, `gate_gain_rule`, `gate_gain_final`, `tau_gate`。
4. 在 Simulink 中回放 `tau_e` 与 `tau_gate`，比较门控响应。

### 半实物验证阶段

1. 将 PyTorch 模型导出 ONNX。
2. 在上位机或 Simulink 外部函数中做推理验证。
3. 先只记录 AI 输出，不闭环改变力矩。
4. 通过离线/在线一致性检查后，再启用 `tau_gate` 支路。
5. `tau_gate` 仍进入原 `Torque_Guard` 和 `Saturation`。

### 推荐新增监控量

- `MS_GaitState`
- `MS_AnomalyType`
- `MS_RiskLevel`
- `MS_GateGainPred`
- `MS_GateGainRule`
- `MS_GateGainFinal`
- `MS_TauGate`
- `MS_WindowValid`
- `MS_ModelLatencyMs`

## 7. DMP/阻抗参数低频修正层

触发条件：

- `risk_level = caution` 持续若干步态周期。
- danger 不触发参数优化，只触发停助或降助。
- 正常状态不频繁调整参数。

可建议修正：

- `Amplitude` 小幅降低。
- `MO_OverwriteKpGain` 小幅降低。
- `MO_Kp / MO_Kd` 小幅调整。
- `phase_offset` 小范围修正。
- `SafeTorque` 临时降低。

约束：

- 有界：每次变化量和总变化量必须设上限。
- 低频：按步态周期或试次更新，不按 1 kHz 实时更新。
- 可审计：记录触发原因、建议值、原值、新值。
- 非强化学习：不做在线黑箱探索。
- 不直接控制力矩：只改变下一窗口或下一试次参数。
- 不能绕过 `Torque_Guard` 和 `Saturation`。

## 8. 实验设计

### 实验 A：离线状态识别实验

数据：正常行走数据。

任务：识别 `stance / swing / transition`。

指标：

- Accuracy
- Macro-F1
- confusion matrix

### 实验 B：异常注入检测实验

注入类型：

- FeetLoad dropout
- Phase0Event lost / false trigger
- Phi phase shift
- `q_ref / q_meas` tracking mismatch
- `tau_e` spike

指标：

- Precision
- Recall
- F1
- false alarm rate
- detection delay

### 实验 C：Simulink 回放安全门控实验

对比：

- 原始 `tau_e`
- 门控后 `tau_gate`

指标：

- peak torque reduction
- gate response delay
- normal-state torque preservation

### 实验 D：低风险健康受试者穿戴验证

任务：

- 正常行走
- 启停
- 变速

不做人为危险扰动。

指标：

- `gate_gain` 正常保持率
- 误触发率
- RMSE/PCC 是否明显劣化
- 交互力矩是否平滑

## 9. MVP

必须完成：

- CSV/MAT 导出表格读取。
- 100 Hz 或 200 Hz 降采样。
- 300-500 ms 滑动窗口。
- 基础特征：`q_meas`, `dq_meas`, `q_ref`, `dq_ref`, `e_q`, `e_dq`, `tau_e`, `FeetLoad`, `Phi`, `sin(Phi)`, `cos(Phi)`, `Phase0Event`。
- FeetLoad / Phase0Event / error 规则生成弱标签。
- 异常注入脚本逻辑。
- TCN + Attention 多任务模型。
- 多任务 loss。
- 离线评估。
- ONNX 导出。
- Simulink 回放文件导出。

可以先简化：

- gate_gain 先离散为 `1.0 / 0.5 / 0.0`。
- 参数修正层先只生成建议 CSV，不接入在线链路。
- 初期只做单腿信号。
- 初期只做 100 Hz。
- 初期只做 CSV，不强依赖 MAT。

## 10. MVP+

增强内容：

- 连续 `gate_gain` 回归。
- 更完整的异常注入强度扫描。
- 个体间训练/测试拆分。
- ONNX 与 Simulink 推理延迟测试。
- 加入 `MS_ModelLatencyMs` 监控。
- 参数修正层加入多周期统计和人工确认界面。
- 加入健康受试者低风险穿戴验证。

## 11. 可以砍掉的模块

- 治疗师自然语言输入。
- 复杂 Web UI。
- EMG 依赖。
- 代谢仪依赖。
- 全身动作捕捉依赖。
- 强化学习或在线黑箱优化。
- 复杂数据库。
- 自动下载/全文阅读更多论文。

## 12. 绝对不要做

- 不要让 AI 直接输出实时力矩。
- 不要替代 `TorqueController`。
- 不要绕过 `Torque_Guard` 或 `Saturation`。
- 不要在线大幅修改 `Amplitude`, `MO_Kp`, `MO_Kd`, `SafeTorque`。
- 不要把 DMP 参数修正写成强化学习。
- 不要重写 Speedgoat 主控制链路。
- 不要把 LLM/语义接口包装成本阶段主贡献。
- 不要在人为危险扰动下做早期穿戴实验。

## 13. 1-2 个月执行排期

### 第 1 周：数据接口与标签规则

- 整理 Simulink/Speedgoat 导出字段。
- 固定输入通道命名。
- 实现降采样、滑窗、标准化。
- 实现 FeetLoad / Phase0Event / tracking error 弱标签。

### 第 2 周：异常注入与基线训练

- 实现 FeetLoad dropout、Phase0Event 异常、Phi shift、tracking mismatch、tau_e spike。
- 训练 TCN 多任务模型。
- 输出离线 metrics 和 confusion matrix。

### 第 3 周：安全门控层

- 实现 `gate_gain_rule`。
- 实现 `gate_gain_final`。
- 导出 `tau_gate` 回放表。
- 做 `tau_e` 与 `tau_gate` 的离线对比。

### 第 4 周：Simulink 回放

- 将预测结果导入 Simulink 回放。
- 检查门控响应延迟、正常状态保持率、峰值力矩降低。
- 修正阈值和标签规则。

### 第 5-6 周：MVP+ 与低风险验证准备

- 导出 ONNX。
- 验证 ONNX 推理输出与 PyTorch 一致。
- 加入推理延迟统计。
- 生成低频参数修正建议 CSV。

### 第 7-8 周：低风险穿戴验证与材料整理

- 做正常行走、启停、变速。
- AI 输出先监控，再启用门控支路。
- 整理论文主图、实验图、消融结果。

## 14. 最小论文贡献表达

MS-TGSS 的贡献不在于替代控制器，而在于把多源时序感知、异常风险判断和规则约束门控接到已有 DMP-阻抗膝关节外骨骼链路中。它让 AI 承担“状态识别与安全监督”的角色，同时保留原有 `Torque_Guard` 和硬限幅作为最终安全边界。
