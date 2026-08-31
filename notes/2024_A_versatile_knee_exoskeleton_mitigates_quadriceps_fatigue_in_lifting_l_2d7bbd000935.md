# A versatile knee exoskeleton mitigates quadriceps fatigue in lifting, lowering, and carrying tasks

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：A versatile knee exoskeleton mitigates quadriceps fatigue in lifting, lowering, and carrying tasks
- 作者：Nikhil Divekar; Gray C. Thomas; Avani R. Yerva; Hannah B. Frame; Robert D. Gregg
- 年份：2024
- 期刊/会议：Science Robotics
- DOI：10.1126/scirobotics.adr8282
- URL：https://doi.org/10.1126/scirobotics.adr8282
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, stability, safety constraint；指标：metabolic cost, EMG reduction/activity, stability, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

The quadriceps are particularly susceptible to fatigue during repetitive lifting, lowering, and
carrying (LLC), affecting worker performance, posture, and ultimately lower-back injury risk.
Although robotic exoskeletons have been developed and optimized for specific use cases like lifting-
lowering, their controllers lack the versatility or customizability to target critical muscles
across many fatiguing tasks. Here, we present a task-adaptive knee exoskeleton controller that
automatically modulates virtual springs, dampers, and gravity and inertia compensation to assist
squatting, level walking, and ramp and stairs ascent/descent. Unlike end-to-end neural networks, the
controller is composed of predictable, bounded components with interpretable parameters that are
amenable to data-driven optimization for biomimetic assistance and subsequent application-specific
tuning, for example, maximizing quadriceps assistance over multiterrain LLC. When deployed on a
backdrivable knee exoskeleton, the assistance torques holistically reduced quadriceps effort across
multiterrain LLC tasks (significantly except for level walking) in 10 human users without user-
specific calibration. The exoskeleton also significantly improved fatigue-induced deficits in time-
based performance and posture during repetitive lifting-lowering. Last, the system facilitated
seamless task transitions and garnered a high effectiveness rating postfatigue over a multiterrain
circuit. These findings indicate that this versatile control framework can target critical muscles
across multiple tasks, specifically mitigating quadriceps fatigue and its deleterious effects.
