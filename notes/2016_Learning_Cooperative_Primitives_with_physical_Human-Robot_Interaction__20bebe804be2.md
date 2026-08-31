# Learning Cooperative Primitives with physical Human-Robot Interaction for a HUman-powered Lower EXoskeleton

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Learning Cooperative Primitives with physical Human-Robot Interaction for a HUman-powered Lower EXoskeleton
- 作者：Rui Huang; Hong Cheng; Hongliang Guo; Xichuan Lin; Qiming Chen; Fuchun Sun
- 年份：2016
- 期刊/会议：未提供
- DOI：10.1109/iros.2016.7759787
- URL：https://doi.org/10.1109/iros.2016.7759787
- PDF 状态：manual_pdf

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

interaction torque/force；指标：interaction torque/force

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

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Human-powered lower exoskeletons have gained considerable interests from both academia and industry
over the past few decades, and thus have seen increasing applications in areas of human locomotion
assistance and strength augmentation. One of the most important aspects in those applications is to
achieve robust control of lower exoskeletons, which, in the first place, requires the proactive
modeling of human movement trajectories through physical Human-Robot Interaction (pHRI). As a
powerful representation tool for motion trajectories, Dynamic Movement Primitive (DMP) has been used
extensively to model human movement trajectories. However, canonical DMPs only offers a general
offline representation of human movement trajectory and neglects the real-time interaction term,
therefore it cannot be directly applied to lower exoskeletons which need to model human motion
trajectories online since different pilots have different trajectories and even one pilot might
change his/her intended trajectory during walking. This paper presents a novel Coupled Cooperative
Primitives (CCPs) scheme, which models the motion trajectories online. Besides maintaining canonical
motion primitives, we also model the interaction term between the pilot and exoskeletons through
impedance models and apply a reinforcement learning method based on Policy Improvement and Path
Integrals (PI 2 ) to learn the parameters online. Experimental results on both a single Degree-Of-
Freedom (DOF) platform and a HUman-powered Augmentation Lower EXoskeleton (HUALEX) system
demonstrate the advantages of our proposed CCP scheme.
