# Exoskeleton Active Walking Assistance Control Framework Based on Frequency Adaptive Dynamics Movement Primitives

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Exoskeleton Active Walking Assistance Control Framework Based on Frequency Adaptive Dynamics Movement Primitives
- 作者：Shiyin Qiu; Wei Guo; Fusheng Zha; Jing Deng; Xin Wang
- 年份：2021
- 期刊/会议：Frontiers in Neurorobotics
- DOI：10.3389/fnbot.2021.672582
- URL：https://doi.org/10.3389/fnbot.2021.672582
- PDF 状态：open_access_pdf

## 2. 一句话结论

可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

状态估计器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, interaction torque/force；指标：metabolic cost, EMG reduction/activity, interaction torque/force

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：GUI/button/shared-control interface
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

This paper introduces a novel exoskeleton active walking assistance control framework based on
frequency adaptive dynamics movement primitives (FADMPs). The FADMPs proposed in this paper is an
online learning and prediction algorithm which is able to online estimate the fundamental frequency
of human joint trajectory, learn the shape of joint trajectory and predict the future joint
trajectory during walking. The proposed active walking assistance control framework based on FADMPs
is a model-based controller which relies on the human joint torque estimation. The assistance torque
provided by exoskeleton is estimated by human lower limb inverse dynamics model which is sensitive
to the noise in the joint motion trajectory. To estimate a smooth joint torque profile, the joint
motion trajectory must be filtered first by a lowpass filter. However, lowpass filter will introduce
an inevitable phase delay in the filtered trajectory. Both simulations and experiments in this paper
show that the phase delay has a significant effect on the performance of exoskeleton active
assistance. The active assistant control framework based on FADMPs aims at improving the performance
of active assistance control by compensating the phase delay. Both simulations and experiments on
active walking assistance control show that the performance of active assistance control can be
further improved when the phase delay in the filtered trajectory is compensated by FADMPs.
