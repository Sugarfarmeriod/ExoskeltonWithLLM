# Validation of Dynamic Bayesian Optimization for a Non-Stationary Human-in-the-Loop Optimization Problem

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Validation of Dynamic Bayesian Optimization for a Non-Stationary Human-in-the-Loop Optimization Problem
- 作者：GilHwan Kim; Fabrizio Sergi
- 年份：2025
- 期刊/会议：未提供
- DOI：10.1101/2025.09.08.674907
- URL：https://doi.org/10.1101/2025.09.08.674907
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer

## 5. 输入数据

IMU, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, stability, safety constraint；指标：metabolic cost, EMG reduction/activity, stability, safety constraint

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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

Abstract Human-in-the-Loop Optimization (HILO) has demonstrated efficacy in achieving a plethora of
assistive or augmentative effects. However, conventional optimizers such as Bayesian optimization
(BO) do not account for the non-stationary aspects of the human-robot system, and may thus be
limited in the domains of robot-assisted training or rehabilitation. In this study, we implemented
HILO using dynamic Bayesian optimization (DBO) to define the optimal value of a single control
parameter to target a desired effect in propulsion mechanics, specifically in the maximum hip
extension (HE) angle during stance. Sixteen healthy participants received unilateral hip torque
pulses via a hip exoskeleton for about 15 minutes while walking on a treadmill. Exoskeleton torques
were determined via HILO using DBO or BO. Unknown to the optimizers, treadmill speed was gradually
increased to amplify the non-stationary behavior of the system. Experimental results revealed that
DBO outperformed BO in the later stages of training, leading to improved cost and to final values of
torques closer to the true value. The primary difference between optimizers arose from their ability
to model the history-dependent relationship between applied torque and output. BO associated later
deviations between expected and measured output to process noise, while DBO developed a more
accurate predictive model of the input-output relationship that gave proper weighing to past
datapoints for making predictions.
