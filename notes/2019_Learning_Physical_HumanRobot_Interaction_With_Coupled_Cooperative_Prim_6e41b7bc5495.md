# Learning Physical Human–Robot Interaction With Coupled Cooperative Primitives for a Lower Exoskeleton

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Learning Physical Human–Robot Interaction With Coupled Cooperative Primitives for a Lower Exoskeleton
- 作者：Rui Huang; Hong Cheng; Jing Qiu; Jianwei Zhang
- 年份：2019
- 期刊/会议：IEEE Transactions on Automation Science and Engineering
- DOI：10.1109/tase.2018.2886376
- URL：https://doi.org/10.1109/tase.2018.2886376
- PDF 状态：manual_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度

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

Human-powered lower exoskeletons have received considerable interests from both academia and
industry over the past decades, and encountered increasing applications in human locomotion
assistance and strength augmentation. One of the most important aspects in those applications is to
achieve robust control of lower exoskeletons, which, in the first place, requires the proactive
modeling of human movement trajectories through physical human-robot interaction (pHRI). As a
powerful representative tool for motion trajectories, dynamic movement primitives (DMP) have been
used to model human movement trajectories. However, canonical DMP only offers a general
representation of human movement trajectory and may neglects the interactive term, therefore it
cannot be directly applied to lower exoskeletons which need to track human joint trajectories
online, because different pilots have different trajectories and even same pilot might change
his/her motion during walking. This paper presents a novel coupled cooperative primitive (CCP)
strategy, which aims at modeling the motion trajectories online. Besides maintaining canonical
motion primitives, we model the interaction term between the pilot and exoskeletons through
impedance models, and propose a reinforcement learning method based on policy improvement and path
integrals (PI 2 ) to learn the parameters online. Experimental results on both a single degree-of-
freedom platform and a HUman-powered Augmentation Lower EXoskeleton (HUALEX) system demonstrate the
advantages of our proposed CCP scheme.
