# Dynamic Movement Primitives Modulation-Based Compliance Control for a New Sitting/Lying Lower Limb Rehabilitation Robot

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Dynamic Movement Primitives Modulation-Based Compliance Control for a New Sitting/Lying Lower Limb Rehabilitation Robot
- 作者：Jie Zhou; Yao Sun; Rong Song; Zhe Wei
- 年份：2024
- 期刊/会议：IEEE Access
- DOI：10.1109/access.2024.3376391
- URL：https://doi.org/10.1109/access.2024.3376391
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP, PD/torque control

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

safety constraint；指标：safety constraint

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：therapist instruction / clinical goal
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Compliant physical human-robot interaction (pHRI), as well as the accuracy and robustness of
trajectory tracking, are crucial for rehabilitation robots. In this paper, a new sitting/lying lower
limb rehabilitation robot, SUT-SLLRR, has been designed for patients with lower extremity motor
dysfunction. A dynamic movement primitives modulation-based compliance control strategy (DMPM-CCS)
has been proposed for the SUT-SLLRR. The high-level trajectory planner consists of the trajectory
generator based on dynamic movement primitives (DMPs), acceleration layer modulation generator, and
velocity layer modulation generator, which can reshape the reference trajectory to generate desired
trajectory within a constrained joint space through pHRI. Besides, the linear active disturbance
rejection controller (LADRC) is adopted as the low-level position controller to ensure that each
joint can accurately and robustness track the desired trajectory under internal and external
disturbances. Simulation and experimental results indicate that the proposed strategy can provide
the compliant pHRI within the constrained joint space and ensure the accuracy and robustness of
trajectory tracking.
