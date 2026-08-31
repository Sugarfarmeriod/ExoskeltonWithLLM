# Compensating elastic faults in a torque-assisted knee exoskeleton: functional evaluation and user perception study

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Compensating elastic faults in a torque-assisted knee exoskeleton: functional evaluation and user perception study
- 作者：Rodrigo J. Velasco-Guillen; Adna Bliek; Josep M. Font-Llagunes; Bram Vanderborght; Philipp Beckerle
- 年份：2024
- 期刊/会议：Journal of NeuroEngineering and Rehabilitation
- DOI：10.1186/s12984-024-01531-6
- URL：https://doi.org/10.1186/s12984-024-01531-6
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, PD/torque control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

comfort score, safety constraint；指标：comfort score, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Wearable robots are often powered by elastic actuators, which can mimic the intrinsic compliance
observed in human joints, contributing to safe and seamless interaction. However, due to their
increased complexity, when compared to direct drives, elastic actuators are susceptible to faults,
which pose significant challenges, potentially compromising user experience and safety during
interaction. In this article, we developed a fault-tolerant control strategy for torque assistance
in a knee exoskeleton and investigated user experience during a walking task while emulating faults.
We implemented and evaluated the torque control scheme, based on impedance control, for a
mechanically adjustable compliance actuator with nonlinear torque-deflection characteristics.
Conducted functional evaluation experiments showed that the control strategy is capable of providing
support during gait based on a torque profile. A user study was conducted to evaluate the impact of
fault severity and compensation on the perception of support, stiffness, comfort, and trust while
walking with the exoskeleton. Results from the user study revealed significant differences in
participants' responses when comparing support and stiffness levels without fault compensation. In
contrast, no significant differences were found when faults were compensated, indicating that fault
tolerance can be achieved in practice. Meanwhile, comfort and trust measurements do not seem to
depend directly on torque support levels, pointing to other influencing factors that could be
considered in future research.
