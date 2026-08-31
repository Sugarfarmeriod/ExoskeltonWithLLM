# A Novel Balance Control Strategy Based on Enhanced Stability Pyramid Index and Dynamic Movement Primitives for a Lower Limb Human-Exoskeleton System

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：A Novel Balance Control Strategy Based on Enhanced Stability Pyramid Index and Dynamic Movement Primitives for a Lower Limb Human-Exoskeleton System
- 作者：Fashu Xu; Jing Qiu; Wenbo Yuan; Hong Cheng
- 年份：2021
- 期刊/会议：Frontiers in Neurorobotics
- DOI：10.3389/fnbot.2021.751642
- URL：https://doi.org/10.3389/fnbot.2021.751642
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

stability, safety constraint；指标：stability, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

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

- 输入类型：GUI/button/shared-control interface
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

The lower limb exoskeleton is playing an increasing role in enabling individuals with spinal cord
injury (SCI) to stand upright, walk, turn, and so on. Hence, it is essential to maintain the balance
of the human-exoskeleton system during movements. However, the balance of the human-exoskeleton
system is challenging to maintain. There are no effective balance control strategies because most of
them can only be used in a specific movement like walking or standing. Hence, the primary aim of the
current study is to propose a balance control strategy to improve the balance of the human-
exoskeleton system in dynamic movements. This study proposes a new safety index named Enhanced
Stability Pyramid Index (ESPI), and a new balance control strategy is based on the ESPI and the
Dynamic Movement Primitives (DMPs). To incorporate dynamic information of the system, the ESPI
employs eXtrapolated Center of Mass (XCoM) instead of the center of mass (CoM). Meanwhile, Time-to-
Contact (TTC), the urgency of safety, is used as an automatic weight assignment factor of ESPI
instead of the traditional manual one. Then, the balance control strategy utilizing DMPs to generate
the gait trajectory according to the scalar and vector values of the ESPI is proposed. Finally, the
walking simulation in Gazebo and the experiments of the human-exoskeleton system verify the
effectiveness of the index and balance control strategy.
