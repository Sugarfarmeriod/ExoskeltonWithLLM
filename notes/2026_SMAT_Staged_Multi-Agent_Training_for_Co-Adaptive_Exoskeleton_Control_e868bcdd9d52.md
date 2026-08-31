# SMAT: Staged Multi-Agent Training for Co-Adaptive Exoskeleton Control

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：SMAT: Staged Multi-Agent Training for Co-Adaptive Exoskeleton Control
- 作者：Yifei Yuan Ghaith Androwis Xianlian Zhou
- 年份：2026
- 期刊/会议：arXiv
- DOI：10.48550/arXiv.2603.07618
- URL：https://arxiv.org/abs/2603.07618
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

待确认

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

stability, safety constraint；指标：stability, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Effective exoskeleton assistance requires co-adaptation: as the device alters joint dynamics, the
user reorganizes neuromuscular coordination, creating a non-stationary learning problem. Most
learning-based approaches do not explicitly account for the sequential nature of human motor
adaptation, leading to training instability and poorly timed assistance. We propose Staged Multi-
Agent Training (SMAT), a four-stage curriculum designed to mirror how users naturally acclimate to a
wearable device. In SMAT, a musculoskeletal human actor and a bilateral hip exoskeleton actor are
trained progressively: the human first learns unassisted gait, then adapts to the added device mass;
the exoskeleton subsequently learns a positive assistance pattern against a stabilized human policy,
and finally both agents co-adapt with full torque capacity and bidirectional feedback. We implement
SMAT in the MyoAssist simulation environment using a 26-muscle lower-limb model and an attached hip
exoskeleton. Our musculoskeletal simulations demonstrate that the learned exoskeleton control policy
produces an average 10.1% reduction in hip muscle activation relative to the no-assist condition. We
validated the learned controller in an offline setting using open-source gait data, then deployed it
to a physical hip exoskeleton for treadmill experiments with five subjects. The resulting policy
delivers consistent assistance and predominantly positive mechanical power without the need for any
explicitly imposed timing shift (mean positive power: 13.6 W at 6 Nm RMS torque to 23.8 W at 9.3 Nm
RMS torque, with minimal negative power) consistently across all subjects without subject-specific
retraining.
