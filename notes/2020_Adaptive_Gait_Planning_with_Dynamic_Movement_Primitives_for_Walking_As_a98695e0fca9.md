# Adaptive Gait Planning with Dynamic Movement Primitives for Walking Assistance Lower Exoskeleton in Uphill Slopes

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Adaptive Gait Planning with Dynamic Movement Primitives for Walking Assistance Lower Exoskeleton in Uphill Slopes
- 作者：Rui Huang; Qian Wu; Jing Qiu; Hong Cheng; Qiming Chen; Zhinan Peng
- 年份：2020
- 期刊/会议：Sensors and Materials
- DOI：10.18494/sam.2020.2550
- URL：https://doi.org/10.18494/sam.2020.2550
- PDF 状态：open_access_pdf

## 2. 一句话结论

可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

状态估计器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

IMU, 足底压力/力传感

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

comfort score, stability；指标：comfort score, stability

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

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

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

The lower exoskeleton system has attracted considerable interest in walking assistance of paraplegic
patients. A critical issue in the walking assistance lower exoskeleton is how to generate gait
motions for paraplegic patients. Predefined gait trajectory planning methods are widely used owing
to their simplicity and effectiveness. However, a predefined gait trajectory planning method has
three main drawbacks: (1) it requires a different gait model for different patients, (2) it cannot
adapt to different terrains, such as slopes and stairs, (3) it does not consider the stability of
the human exoskeleton system. In this study, we modeled the walking assistance lower exoskeleton
with paraplegic patients as a human exoskeleton hybrid agent (HEHA). On the basis of the HEHA model,
an adaptive gait planning method with dynamic movement primitives is proposed; in this method, the
center of mass of HEHA is considered to ensure the stability of the human exoskeleton system. To
adapt different pilots in slope scenarios, the reinforcement learning method is employed to update
the parameters of the proposed gait model. The experimental results in both the simulation
environment and the real-time exoskeleton system show that the proposed gait planning method makes
the human exoskeleton system more stable in uphill slope scenarios.
