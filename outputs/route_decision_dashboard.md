# MS-TGSS 技术路线可视化看板

<details>
<summary>看板说明与结论</summary>

系统名称：**面向 DMP-阻抗膝关节外骨骼的多源时序步态状态与安全监督器**

简称：**MS-TGSS / MT-GSS**

结论：当前工程主线合并为“多源时序步态状态识别 + 异常风险感知安全门控 + 低频有界参数修正”。语义/治疗师自然语言输入单独放在远期高层接口，不进入当前实现。

资料依据：`research_routes.md`、`light_screening_report.md`、`top_10_for_deep_reading.md`、`InterForceControlTask_parameter_report.md`、`light_rank_top30.csv`。本看板只使用压缩资料和参数报告，不继续大规模精读 PDF。

</details>

## 1. 总体路线决策

```mermaid
flowchart TD
    A["现有基础<br/>AO / Phi / Phase0Event<br/>DMP 参考轨迹<br/>PD/阻抗力矩<br/>Torque_Guard + 限幅"] --> B["当前工程主线<br/>多源时序状态识别<br/>异常风险感知安全门控"]
    B --> C["插入位置<br/>TorqueController 之后<br/>Torque_Guard 之前"]
    C --> D["输出<br/>步态状态 gait_state<br/>异常类型 anomaly_type<br/>风险等级 risk_level<br/>门控增益 gate_gain"]
    D --> E["规则约束安全层<br/>SafeTorque / 跟踪误差<br/>FeetLoad / Phase0Event 周期"]
    E --> F["tau_gate = gate_gain_final * tau_e"]
    F --> G["Torque_Guard<br/>限幅 Saturation<br/>力矩输出"]
    B --> H["低频参数修正层<br/>Amplitude / phase_offset<br/>MO_Kp / MO_Kd<br/>MO_OverwriteKpGain / SafeTorque"]
    H --> I["有界、低频、人工可审计<br/>不绕过 Torque_Guard"]
    A --> J["远期高层接口<br/>治疗师自然语言目标"]
    J --> K["语义解析到参数建议<br/>人工确认后更新"]
```

## 2. 现有控制链路

```mermaid
flowchart LR
    AO["AO / 步态相位估计<br/>Phi, Phase0Event, FeetLoad"] --> DMP["DMP 参考轨迹生成<br/>Amplitude, tau, phase_offset<br/>q_ref, dq_ref"]
    DMP --> TC["TorqueController<br/>PD / 阻抗控制<br/>MO_Kp, MO_Kd, MO_OverwriteKpGain<br/>tau_e"]
    TC --> TG["Torque_Guard<br/>SafeTorque, FeetLoad, 关节限位"]
    TG --> SAT["限幅 Saturation<br/>[-20, 20]"]
    SAT --> OUT["力矩输出"]
```

## 3. 新增 AI 模块插入位置

```mermaid
flowchart LR
    AO["AO<br/>Phi / Phase0Event / FeetLoad"] --> DMP["DMP<br/>q_ref / dq_ref"]
    DMP --> TC["TorqueController<br/>tau_e"]
    TC --> AI["多源时序安全监督器<br/>TCN + 注意力池化 + 多任务输出头"]
    AI --> GATE["规则约束安全层<br/>最终增益 = min(预测增益, 规则增益)"]
    GATE --> TAU["tau_gate = gate_gain_final * tau_e"]
    TAU --> TG["Torque_Guard"]
    TG --> SAT["限幅 Saturation"]
    SAT --> OUT["力矩输出"]
```

## 4. 多源输入信号

```mermaid
flowchart TD
    S1["q_meas, dq_meas"] --> F["特征构造器"]
    S2["q_ref, dq_ref"] --> F
    S3["tau_e"] --> F
    S4["FeetLoad_left, FeetLoad_right"] --> F
    S5["Phi, sin(Phi), cos(Phi)"] --> F
    S6["Phase0Event"] --> F
    F --> E1["e_q = q_ref - q_meas"]
    F --> E2["e_dq = dq_ref - dq_meas"]
    F --> E3["移动均方根 / 峰值 / 斜率"]
    E1 --> W["300-500 ms 滑动窗口<br/>1 kHz 降采样到 100 或 200 Hz"]
    E2 --> W
    E3 --> W
    W --> M["TCN 时序主干网络"]
```

## 5. TCN + 注意力池化 + 多任务输出模型结构

```mermaid
flowchart LR
    X["窗口张量<br/>通道 x 时间"] --> C1["TCN 模块 1<br/>空洞一维卷积"]
    C1 --> C2["TCN 模块 2<br/>残差连接 + 随机失活"]
    C2 --> C3["TCN 模块 3<br/>更大空洞率"]
    C3 --> ATT["注意力池化<br/>加权时序摘要"]
    ATT --> H1["步态状态输出头<br/>支撑期 / 摆动期 / 过渡期"]
    ATT --> H2["异常类型输出头<br/>正常 / 相位错配 / 跟踪误差<br/>力矩风险 / 足底负载不一致 / 传感器故障"]
    ATT --> H3["风险等级输出头<br/>正常 / 注意 / 危险"]
    ATT --> H4["门控增益输出头<br/>连续 0..1 或 {1.0, 0.5, 0.0}"]
```

## 6. 标签生成流程

```mermaid
flowchart TD
    RAW["行走记录数据<br/>q, dq, ref, tau_e, FeetLoad, Phi, Phase0Event"] --> CONTACT["FeetLoad 弱标签<br/>支撑期 / 摆动期"]
    RAW --> EVENT["Phase0Event 事件标签<br/>周期边界与过渡期"]
    RAW --> ERR["跟踪误差规则<br/>e_q, e_dq, tau_e 峰值"]
    RAW --> INJ["合成异常注入<br/>信号丢失、误触发、相位偏移、力矩尖峰"]
    CONTACT --> GS["步态状态标签"]
    EVENT --> GS
    ERR --> AT["异常类型标签"]
    INJ --> AT
    AT --> RISK["风险等级标签<br/>正常 / 注意 / 危险"]
    ERR --> RISK
    RISK --> GATE["门控增益目标<br/>正常 1.0，注意 0.3-0.7，危险 0.0"]
```

## 7. 实验验证流程

```mermaid
flowchart LR
    D1["离线记录数据"] --> D2["降采样 + 窗口切片 + 标签"]
    D2 --> D3["异常注入"]
    D3 --> T["模型训练<br/>TCN 多任务学习"]
    T --> E["离线评估<br/>F1 / 检测延迟 / 误报警"]
    E --> S["Simulink 回放<br/>tau_e 对比 tau_gate"]
    S --> W["低风险穿戴验证<br/>正常行走、启停、变速"]
```

## 8. 安全门控逻辑

```mermaid
flowchart TD
    P["模型输出<br/>risk_level, gate_gain_pred"] --> R1["预测门控"]
    SAFE["规则输入<br/>SafeTorque, abs(tau_e), e_q/e_dq<br/>FeetLoad 一致性, Phase0Event 周期"] --> R2["规则门控增益 gate_gain_rule"]
    R1 --> MIN["最终门控增益 = min(预测增益, 规则增益)"]
    R2 --> MIN
    MIN --> DANGER{"风险等级 = 危险？"}
    DANGER -->|是| ZERO["gate_gain_final = 0"]
    DANGER -->|否| CAUTION{"风险等级 = 注意？"}
    CAUTION -->|是| MID["限制在 0.3-0.7"]
    CAUTION -->|否| ONE["正常状态允许不超过 1.0"]
    ZERO --> TAU["tau_gate = gate_gain_final * tau_e"]
    MID --> TAU
    ONE --> TAU
    TAU --> TG["Torque_Guard + Saturation"]
```

<details>
<summary>9. 可行性对比矩阵</summary>

```mermaid
quadrantChart
    title 工程可行性与当前价值
    x-axis "低当前价值" --> "高当前价值"
    y-axis "低落地性" --> "高落地性"
    quadrant-1 "优先落地"
    quadrant-2 "谨慎增强"
    quadrant-3 "不进入当前实现"
    quadrant-4 "后续观察"
    "多源状态识别与安全门控": [0.86, 0.88]
    "DMP/阻抗参数低频修正": [0.70, 0.58]
    "治疗师语义输入": [0.46, 0.35]
    "AI直接实时力矩控制": [0.20, 0.18]
    "重写Speedgoat主链路": [0.18, 0.12]
```

| 方向 | 当前实现位置 | 1-2 个月落地性 | 主要输出 | 本阶段处理方式 |
|---|---|---:|---|---|
| 多源状态识别与安全门控 | TorqueController 与 Torque_Guard 之间 | 高 | `gait_state`, `anomaly_type`, `risk_level`, `gate_gain` | 主线实现 |
| DMP/阻抗参数低频修正 | 步态周期级或试次级参数入口 | 中 | `Amplitude`, `phase_offset`, `MO_Kp`, `MO_Kd`, `SafeTorque` 的小幅建议 | 作为同一系统的扩展层 |
| 治疗师语义输入 | Speedgoat 外层人机交互入口 | 低到中 | 受限参数建议 | 单独放远期接口 |
| AI 直接实时力矩控制 | 替代 TorqueController | 低 | torque command | 不做 |
| 重写 Speedgoat 主链路 | AO/DMP/控制器整体替换 | 低 | 新控制架构 | 不做 |

</details>

<details>
<summary>10. 最终推荐技术路线</summary>

```mermaid
flowchart TD
    A["最小可行版本<br/>CSV/MAT 导出数据<br/>100/200 Hz 窗口数据集"] --> B["TCN + 注意力池化多任务模型"]
    B --> C["离线状态识别与异常检测"]
    C --> D["规则约束安全层<br/>gate_gain_final"]
    D --> E["Simulink 回放<br/>tau_e 对比 tau_gate"]
    E --> F["低风险穿戴验证<br/>正常行走 / 启停 / 变速"]
    F --> G["论文主图<br/>MS-TGSS 插入现有 DMP-阻抗控制链路"]
    D --> H["扩展层<br/>注意状态持续多周期时<br/>小幅参数修正建议"]
    H --> I["人工确认 + 边界检查<br/>下一窗口或下一试次生效"]
    G --> J["远期接口<br/>治疗师自然语言目标到参数建议"]
```

</details>

<details>
<summary>四类实验</summary>

**实验 A：离线状态识别实验**

正常行走数据，识别支撑期、摆动期、过渡期。指标：准确率、宏平均 F1、混淆矩阵。

**实验 B：异常注入检测实验**

注入 FeetLoad 信号丢失、Phase0Event 丢失或误触发、Phi 相位偏移、`q_ref / q_meas` 跟踪错配、`tau_e` 力矩尖峰。指标：精确率、召回率、F1、误报警率、检测延迟。

**实验 C：Simulink 回放安全门控实验**

对比原始 `tau_e` 和 `tau_gate`。指标：峰值力矩降低量、门控响应延迟、正常状态力矩保留率。

**实验 D：低风险健康受试者穿戴验证**

正常行走、启停、变速，不做人为危险扰动。指标：`gate_gain` 正常保持率、误触发率、RMSE/PCC 是否明显劣化、交互力矩是否平滑。

</details>

<details>
<summary>最先看哪一张</summary>

先看“新增 AI 模块插入位置”和“安全门控逻辑”。这两张最直接说明本方案不替代原控制器、不直接输出实时力矩，而是在 `TorqueController` 和 `Torque_Guard` 之间增加可回放、可约束、可验证的安全监督层。

</details>
