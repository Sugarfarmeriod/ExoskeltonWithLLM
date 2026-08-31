# Adaptive Control of Exoskeleton Robots for Periodic Assistive Behaviours Based on EMG Feedback Minimisation

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Adaptive Control of Exoskeleton Robots for Periodic Assistive Behaviours Based on EMG Feedback Minimisation
- 作者：Luka Peternel; Tomoyuki Noda; Tadej Petrič; Aleš Ude; Jun Morimoto; Jan Babič
- 年份：2016
- 期刊/会议：PLoS ONE
- DOI：10.1371/journal.pone.0148942
- URL：https://doi.org/10.1371/journal.pone.0148942
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

足底压力/力传感, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity；指标：EMG reduction/activity

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

- 输入类型：GUI/button/shared-control interface
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

In this paper we propose an exoskeleton control method for adaptive learning of assistive joint
torque profiles in periodic tasks. We use human muscle activity as feedback to adapt the assistive
joint torque behaviour in a way that the muscle activity is minimised. The user can then relax while
the exoskeleton takes over the task execution. If the task is altered and the existing assistive
behaviour becomes inadequate, the exoskeleton gradually adapts to the new task execution so that the
increased muscle activity caused by the new desired task can be reduced. The advantage of the
proposed method is that it does not require biomechanical or dynamical models. Our proposed learning
system uses Dynamical Movement Primitives (DMPs) as a trajectory generator and parameters of DMPs
are modulated using Locally Weighted Regression. Then, the learning system is combined with adaptive
oscillators that determine the phase and frequency of motion according to measured Electromyography
(EMG) signals. We tested the method with real robot experiments where subjects wearing an elbow
exoskeleton had to move an object of an unknown mass according to a predefined reference motion. We
further evaluated the proposed approach on a whole-arm exoskeleton to show that it is able to
adaptively derive assistive torques even for multiple-joint motion.
