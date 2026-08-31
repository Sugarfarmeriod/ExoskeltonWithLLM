# Human-Robot Variable Impedance Skill Transfer Learning Based on Dynamic Movement Primitives and Vision System

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Human-Robot Variable Impedance Skill Transfer Learning Based on Dynamic Movement Primitives and Vision System
- 作者：Honghui Zhang; Fang Peng; Miaozhe Cai
- 年份：2025
- 期刊/会议：未提供
- DOI：10.20944/preprints202507.0153.v1
- URL：https://doi.org/10.20944/preprints202507.0153.v1
- PDF 状态：abstract_only

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

足底压力/力传感, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity, stability, safety constraint；指标：EMG reduction/activity, stability, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

abstract only

## 13. 语义/治疗师输入扩展记录

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

To enhance robotic adaptability in dynamic environments, this study proposes a multimodal framework
for skill transfer. The framework integrates vision-based kinesthetic teaching with surface
electromyography (sEMG) signals to estimate human impedance. We establish a Cartesian-space model of
upper-limb stiffness, linearly mapping sEMG signals to endpoint stiffness. For flexible task
execution, dynamic movement primitives (DMPs) generalize learned skills across varying scenarios. An
adaptive admittance controller, incorporating sEMG-modulated stiffness, is developed and validated
on a UR5 robot. Experiments involving elastic band stretching demonstrate that the system
successfully transfers human impedance characteristics to the robot, enhancing stability,
environmental adaptability, and safety during physical interaction.
