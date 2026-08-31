# Optimization and evaluation of lower limb exoskeleton based on human-exo coupling dynamics

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Optimization and evaluation of lower limb exoskeleton based on human-exo coupling dynamics
- 作者：未提供
- 年份：2025
- 期刊/会议：未提供
- DOI：10.52843/cassyni.ctzs0d
- URL：https://doi.org/10.52843/cassyni.ctzs0d
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, DMP, PD/torque control, low-frequency optimizer, high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝力矩/交互力矩, EMG, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, interaction torque/force, comfort score, stability, safety constraint；指标：metabolic cost, EMG reduction/activity, interaction torque/force, comfort score, stability, safety constraint

## 8. 实验对象和实验任务

15 healthy

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

The rapid advancement of lower limb exoskeleton technology has created new opportunities to enhance
human locomotion and reduce operational fatigue. In our study, the in-depth investigation of human-
exoskeleton coupling dynamics has been conducted and exoskeleton performance by evaluating assistive
efficiency has been optimized. First, we propose a linear human-exoskeleton coupling model that
integrates electromyography (EMG) features and human physiological parameters to predict coupling
parameters using a CNN-LSTM neural network. On this basis, we refine the coupling model to a
nonlinear framework, analyzing the effects of coupling position, looseness, and other influencing
factors on the coupling parameters. Additionally, we propose a regression model for predictive
analysis. To further explore human-exoskeleton interaction, we extract a dynamic physical model of
coupling forces using a sparse regression algorithm. Additionally, we propose a mechanics-based
ground reaction force calculation method and establish a human-exoskeleton coupling dynamic model
for walking gait. The inertia parameters of both the exoskeleton and human body are experimentally
identified to enhance model accuracy. Finally, to maximize the assistive effect of the lower limb
exoskeleton, we introduce an optimization framework based on human energy efficiency principles. A
set of comprehensive evaluation metrics, incorporating both joint and muscle dynamics, is
established as a reference for exoskeleton performance evaluation.
