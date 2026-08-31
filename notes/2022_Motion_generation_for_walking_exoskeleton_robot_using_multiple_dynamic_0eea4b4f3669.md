# Motion generation for walking exoskeleton robot using multiple dynamic movement primitives sequences combined with reinforcement learning

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Motion generation for walking exoskeleton robot using multiple dynamic movement primitives sequences combined with reinforcement learning
- 作者：Peng Zhang; Junxia Zhang
- 年份：2022
- 期刊/会议：Robotica
- DOI：10.1017/s0263574721001934
- URL：https://doi.org/10.1017/s0263574721001934
- PDF 状态：abstract_only

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

stability, safety constraint；指标：stability, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

abstract only

## 13. 语义/治疗师输入扩展记录

- 输入类型：GUI/button/shared-control interface
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Abstract In order to assist patients with lower limb disabilities in normal walking, a new
trajectory learning scheme of limb exoskeleton robot based on dynamic movement primitives (DMP)
combined with reinforcement learning (RL) was proposed. The developed exoskeleton robot has six
degrees of freedom (DOFs). The hip and knee of each artificial leg can provide two electric-powered
DOFs for flexion/extension. And two passive-installed DOFs of the ankle were used to achieve the
motion of inversion/eversion and plantarflexion/dorsiflexion. The five-point segmented gait planning
strategy is proposed to generate gait trajectories. The gait Zero Moment Point stability margin is
used as a parameter to construct a stability criteria to ensure the stability of human-exoskeleton
system. Based on the segmented gait trajectory planning formation strategy, the multiple-DMP
sequences were proposed to model the generation trajectories. Meanwhile, in order to eliminate the
effect of uncertainties in joint space, the RL was adopted to learn the trajectories. The experiment
demonstrated that the proposed scheme can effectively remove interferences and uncertainties.
