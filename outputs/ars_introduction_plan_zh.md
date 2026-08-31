# ARS Introduction 规划：AI 融入膝关节外骨骼 DMP-阻抗控制框架

> 版本说明：本文件是较早的 ARS 规划稿。当前请以根目录 `PAPER_START_HERE.md` 和 `outputs/ars_introduction_plan_hybrid_zh.md` 为准。事实口径：`TestStructure.slx` 是当前正式实验模型，当前 AO 仅依赖足底压力，与既有中文论文中的关节运动 AFO 不是前后版本关系。导师当前规划招募 8 名健康受试者，年龄范围等纳入标准仍待确认；本论文及系统实现不包含 EMG 或 IMU。

## 当前阶段

- 使用 skill：`academic-research-suite`
- 路由：`academic-paper` workflow
- 模式：plan / outline hybrid
- 当前产物：Introduction 结构蓝图 + 论证蓝图
- 下一关口：用户确认 Introduction 论证路线后，进入中文初稿起草

## 1. Paper Configuration Record

| 字段 | 当前设定 |
|---|---|
| 论文类型 | 工程方法论文 / 控制系统框架论文，接近 IMRaD |
| 学科 | 康复机器人、外骨骼控制、人机交互控制、AI for robotics |
| 主语言流程 | 先中文逻辑稿，再转英文论文表达 |
| 目标读者 | 外骨骼控制、康复机器人、可穿戴机器人、AI 个性化控制方向审稿人 |
| 核心研究问题 | AI 应该如何接入已有膝关节外骨骼 DMP-阻抗控制框架，才能提高个体化辅助能力，同时不破坏实时安全闭环？ |
| 中心主张 | AI 应作为低频、有界的 DMP/阻抗参数优化器或状态评价器，而不是直接替代实时力矩控制器。 |
| 控制底座 | 足底压力 -> AO（`FeetLoad`、`Phase0Event`、`Phi`、`Omega`）-> DMP 轨迹生成 -> TorqueController/PD 或阻抗控制 -> Torque_Guard -> 力矩输出 |
| 关键参数 | `Amplitude`, `tau`, `phase_offset`, `MO_Kp`, `MO_Kd`, `MO_OverwriteKpGain`, `SafeTorque` |
| 关键信号 | `Phi`, `Phase0Event`, `FeetLoad`, `q_meas`, `dq_meas`, `q_ref`, `dq_ref`, `tau_e` |
| 文献主路线 | Route A：AI as a low-frequency DMP/impedance parameter optimizer |
| 次要路线 | Route B：步态相位/负载/意图估计；Route D：语义/治疗师输入接口作为未来扩展 |

## 2. Introduction 顶层结构

推荐 Introduction 目标长度：

- 中文逻辑稿：约 1600-2200 字
- 英文正式稿：约 900-1200 words
- 段落数：7 段

### 结构概览

Introduction 的任务不是展示“AI 很强”，而是建立一个工程判断：

> 对安全关键的膝关节外骨骼而言，实时力矩控制环应保持可解释、可验证和可限幅；AI 的合理位置是在该实时环外，以低频方式优化 DMP/阻抗参数。

因此，引言应按如下路径推进：

```text
康复/助行需求
-> 人机同步、舒适性、安全性和个体差异
-> DMP-阻抗/PD 是已有实时控制底座
-> 该底座的瓶颈是参数选择
-> AI/HIL/BO/CMA-ES 可用于个体化参数优化
-> 但现有文献缺少到本系统变量的明确映射
-> 本文提出低频、安全约束的 AI 参数优化层
```

## 3. Detailed Outline

### P1：康复与助行背景

**目的**：建立外骨骼研究的应用动机。

**核心内容**：

- 膝关节外骨骼可用于步态康复、行走辅助、肌力补偿和运动功能重建。
- 可穿戴外骨骼不同于固定康复设备，需要在真实人机耦合中提供辅助。
- 辅助效果不只取决于驱动能力，还取决于助力是否与步态相位、关节状态和负载变化同步。

**建议引用类型**：

- lower-limb / knee exoskeleton review
- stroke gait rehabilitation / wearable robot review
- knee exoskeleton assistance papers

**过渡句功能**：

从“外骨骼有用”过渡到“外骨骼控制难”。

### P2：人机交互控制难点

**目的**：把问题从应用价值推进到控制问题。

**核心内容**：

- 不同使用者存在步态周期、膝关节活动范围、负载状态、肌力和交互力矩差异。
- 固定参数可能导致助力不足、助力过度、相位不同步或舒适性下降。
- 因此，关键不是输出更大力矩，而是在安全约束内调节助力时机、助力强度和阻抗特性。

**建议引用类型**：

- personalized exoskeleton assistance
- HIL optimization for exoskeleton assistance
- interaction torque / comfort / metabolic or EMG objective papers（后两类仅作外部方法参考，本研究不采集 EMG）

**过渡句功能**：

从“控制难点”过渡到“已有控制底座能解决一部分问题”。

### P3：DMP-阻抗控制作为实时底座

**目的**：说明本文不是抛弃传统控制，而是在已有控制链上加 AI。

**核心内容**：

- DMP 可以用低维参数表示膝关节参考轨迹，适合调节 `Amplitude`、`tau` 和 `phase_offset`。
- 阻抗/PD 控制可以把参考轨迹转化为可解释的人机交互力矩，适合调节 `MO_Kp` 和 `MO_Kd`。
- `Torque_Guard`、`SafeTorque` 和 saturation limits 为实时输出提供安全边界。
- MATLAB/Simulink + Speedgoat 的实时链路适合保留确定性控制器。

**建议引用类型**：

- DMP + exoskeleton
- adaptive impedance control
- quasi-direct-drive knee exoskeleton torque control

**过渡句功能**：

从“控制底座可用”过渡到“但是参数仍然是瓶颈”。

### P4：参数选择是瓶颈

**目的**：明确本文创新入口。

**核心内容**：

- DMP-阻抗框架是否有效，取决于轨迹参数和控制增益是否适合当前使用者和当前步态阶段。
- 人工调参慢、依赖经验，且很难同时权衡轨迹跟踪、交互力矩、舒适度、步态对称性和安全限幅。
- 这些问题天然适合被表述为低维、约束优化问题，而不是端到端力矩学习问题。

**建议引用类型**：

- Bayesian optimization / CMA-ES / HIL optimization
- cost function selection
- personalized assistance using physiological measures

**过渡句功能**：

从“参数瓶颈”过渡到“AI/优化文献已经给出方法基础”。

### P5：AI 个体化优化文献基础

**目的**：把 AI 引进来，但不让 AI 变成泛泛口号。

**核心内容**：

- 既有 HIL optimization、Bayesian optimization、CMA-ES 研究已用于优化外骨骼辅助强度、时机、代谢成本、EMG 或舒适度；其中 EMG/代谢仅说明外部方法谱系，不是本研究的采集指标。
- 步态相位、足底压力、关节角速度和交互力矩等信号可作为状态估计或评价输入。
- 这些研究说明 AI 可以服务个体化辅助，但其工程接入点必须受控制系统结构限制。

**建议引用类型**：

- HIL optimization top papers
- foot pressure / gait phase estimation papers
- adaptive impedance or DMP + RL papers

**过渡句功能**：

从“AI 有用”过渡到“AI 插在哪里仍不清楚”。

### P6：研究缺口与本文定位

**目的**：给出明确 gap，避免写成普通综述。

**核心内容**：

- 现有研究常强调代谢降低、EMG 降低或步态改善等结果，但不总是说明这些优化变量如何落到一个具体实时控制链路中；本研究只采用现有足底压力、膝运动学和膝力矩信号可支持的目标。
- 对本项目来说，AI 不能绕过 `Torque_Guard`，也不能直接输出未经验证的实时膝关节力矩。
- 缺口在于：缺少一个把 AI 输出映射到 DMP 参数、阻抗参数和安全约束的层级化框架。

**建议引用类型**：

- HIL optimization studies as support
- LLM/semantic robotics papers only as contrast or future interface
- safety-constrained robot/LLM papers as discussion support

**过渡句功能**：

从“缺口”过渡到“本文具体做什么”。

### P7：本文贡献

**目的**：清楚、具体、工程化地收束 Introduction。

建议贡献写成三条：

1. 提出一种 AI 融入 DMP-阻抗膝关节外骨骼控制框架的层级结构，将 AI 定位为低频参数优化器，而不是实时力矩控制器。
2. 定义 AI 层的输入、输出和约束：输入包括 `Phi`、`Phase0Event`、`FeetLoad`、`q_meas`、`dq_meas`、`tau_e`；输出包括 `Amplitude`、`tau`、`phase_offset`、`MO_Kp`、`MO_Kd`；约束包括 `SafeTorque`、saturation limits 和参数变化率限制。
3. 给出该结构在 MATLAB/Simulink + Speedgoat 控制链路中的实现与验证方案，用于评估个体化辅助、交互安全和控制可部署性。

## 4. Argument Blueprint

### Central Thesis

本文主张：在准直驱膝关节外骨骼中，AI 的主要价值不是替代实时力矩控制器，而是在 DMP-阻抗控制底座之外，以低频、安全约束的方式优化轨迹和阻抗参数，从而兼顾个体化辅助、实时可部署性和人机交互安全。

### Sub-Argument 1：外骨骼辅助需要个体化参数适配

- **Claim**：不同使用者和不同步态状态需要不同助力参数。
- **Evidence**：HIL optimization、personalized wearable device、knee/hip/ankle assistance optimization 文献普遍优化时机、幅值或控制参数。
- **Reasoning**：如果同一组参数无法适配所有人，那么控制问题就应被表达为参数适配问题。
- **Counter-argument**：也可以用一个鲁棒控制器覆盖大部分情况。
- **Rebuttal**：鲁棒控制可保证基本稳定，但不等于个体最优辅助；本研究将以足底压力、膝运动学和膝力矩可支持的同步、交互、安全或对称性代理指标评价调参，不使用 EMG/IMU。
- **强度评估**：Strong。

### Sub-Argument 2：DMP-阻抗控制适合作为 AI 的工程落点

- **Claim**：DMP 和阻抗/PD 控制提供了低维、可解释、实时可部署的参数接口。
- **Evidence**：DMP 文献支持轨迹参数化；阻抗控制文献支持通过刚度/阻尼塑造交互；本项目已有 Simulink/Speedgoat 控制链。
- **Reasoning**：AI 若输出有限维参数，而不是直接输出力矩，则更容易验证、限幅和部署。
- **Counter-argument**：端到端 RL 或神经控制器可能理论上更灵活。
- **Rebuttal**：灵活性并不等于安全可部署；对于膝关节外骨骼，实时力矩输出是安全关键环节，应保留确定性控制和 `Torque_Guard`。
- **强度评估**：Strong。

### Sub-Argument 3：AI 应放在低频优化层而非实时力矩环

- **Claim**：低频优化层能利用 AI 的搜索/学习能力，同时保留实时控制器的安全性。
- **Evidence**：BO/CMA-ES/HIL optimization 多在 trial 间、步态窗口或低频更新中优化参数；安全层可限制参数范围与力矩输出。
- **Reasoning**：低频更新降低实时不确定性，参数边界降低安全风险。
- **Counter-argument**：低频优化可能响应慢，无法处理快速变化的步态扰动。
- **Rebuttal**：快速扰动由实时 PD/阻抗控制和 Torque_Guard 处理；AI 负责慢变量，如个体差异、疲劳、任务模式和舒适性偏好。
- **强度评估**：Compelling。

### Sub-Argument 4：语义/治疗师输入适合作为未来高层接口

- **Claim**：LLM/语义机器人文献可启发治疗师输入接口，但不能作为当前主控制路线。
- **Evidence**：语言机器人论文通常把自然语言映射到动作、约束或规划目标；少数 exoskeleton 交互论文涉及 speech/gesture/generative interface。
- **Reasoning**：这些方法可以转化为“高层目标 -> 受限参数建议”，但不能直接进入实时力矩输出。
- **Counter-argument**：语义接口更有新意，可能更容易写出 AI 特色。
- **Rebuttal**：新意不能替代闭环验证；若没有映射到 `Amplitude`、`phase_offset`、`MO_Kp`、`MO_Kd` 或 `SafeTorque`，就会偏离本项目控制主线。
- **强度评估**：Adequate，适合 Related Work / Discussion，不适合 Introduction 主贡献。

## 5. Evidence Map

| Introduction 位置 | 需要的证据类型 | 本地材料入口 |
|---|---|---|
| P1 康复/助行背景 | lower-limb exoskeleton review, knee exoskeleton assistance | `outputs/light_screening_report.md` 中 review 和 knee exoskeleton 条目 |
| P2 个体差异 | personalized assistance, HIL optimization | top 30 中 HIL/BO/CMA-ES 文献 |
| P3 控制底座 | DMP, impedance, quasi-direct-drive knee control | DMP survey, DMP+exoskeleton, stiffness/torque control 文献 |
| P4 参数瓶颈 | cost function, parameter tuning, BO/CMA-ES | HIL optimization 和 cost function selection 文献 |
| P5 AI 文献基础 | HIL optimization, gait phase/state estimation | BO/CMA-ES、foot pressure、gait phase estimation 文献 |
| P6 gap | system mapping to DMP/impedance/safety chain | 本项目 `AGENTS.md` 控制链路 + paper matrix 映射 |
| P7 贡献 | 本文系统变量和实现方案 | `Phi`, `Phase0Event`, `Amplitude`, `MO_Kp`, `MO_Kd`, `SafeTorque` 等项目变量 |

## 6. Introduction 风险检查

### 高风险写法

- 把 AI 写成端到端实时力矩控制器。
- 只写“AI improves exoskeleton control”，不说明 AI 优化什么。
- 把 LLM/语义交互写成主贡献，但没有闭环控制映射。
- 直接声称降低代谢、降低 EMG、获得 IMU 运动学结果或改善对称性，而没有对应传感器和实验数据。
- 引用未精读论文中的受试者数量、指标数值或实验结果。

### 稳妥写法

- 用“parameter adaptation / parameter optimization / safety-constrained update”描述 AI。
- 用“may / can / is suitable for / is formulated as”谨慎表达未实验证实的部分。
- 所有文献只支持其实际证明的内容，不能从 hip/ankle 论文直接推到 knee exoskeleton 最优效果。
- LLM/语义论文放在“future interface / high-level instruction mapping”中，不放在主贡献。

## 7. 下一步写作门槛

进入中文 Introduction 初稿前，需要确认三点：

1. 论文主线是否固定为 Route A：低频 DMP/阻抗参数优化。
2. 贡献是否写成“框架 + 参数映射 + 验证方案”，而不是承诺尚未完成的临床疗效。
3. Introduction 是否暂时不把 LLM/语义接口作为主线，只作为 Related Work 和 Discussion 的未来扩展。

如果以上三点确认，下一步可以直接起草中文 Introduction 第一版。
