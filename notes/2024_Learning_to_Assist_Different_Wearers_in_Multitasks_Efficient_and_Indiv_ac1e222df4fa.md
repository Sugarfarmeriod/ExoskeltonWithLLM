# Learning to Assist Different Wearers in Multitasks: Efficient and Individualized Human-in-the-Loop Adaptation Framework for Lower-Limb Exoskeleton

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Learning to Assist Different Wearers in Multitasks: Efficient and Individualized Human-in-the-Loop Adaptation Framework for Lower-Limb Exoskeleton
- 作者：Yu Chen; Shu Miao; Gong Chen; Jing Ye; Chenglong Fu; Bin Liang; Shiji Song; Xiang Li
- 年份：2024
- 期刊/会议：IEEE Transactions on Robotics
- DOI：10.1109/tro.2024.3468768
- URL：https://doi.org/10.1109/tro.2024.3468768
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, DMP, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, gait symmetry, interaction torque/force, comfort score, stability, safety constraint；指标：metabolic cost, EMG reduction/activity, gait symmetry, interaction torque/force, comfort score, stability, safety constraint

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

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

One of the typical purposes of using lower-limb exoskeleton robots is to provide assistance to the
wearer by supporting their weight and augmenting their physical capabilities according to a given
task and human motion intentions. The generalizability of robots across different wearers in
multiple tasks is important to ensure that the robot can provide correct and effective assistance in
actual implementation. However, most lower-limb exoskeleton robots exhibit only limited
generalizability. Therefore, this article proposes a human-in-the-loop learning and adaptation
framework for exoskeleton robots to improve their performance in various tasks and for different
wearers. To suit different wearers, an individualized walking trajectory is generated online using
dynamic movement primitives and Bayes optimization. To accommodate various tasks, a task translator
is constructed using a neural network to generalize a trajectory to more complex scenarios. These
generalization techniques are integrated into a unified variable impedance model, which regulates
the exoskeleton to provide assistance while ensuring safety. In addition, an anomaly detection
network is developed to quantitatively evaluate the wearer's comfort, which is considered in the
trajectory learning procedure and contributes to the relaxation of conflicts in impedance control.
The proposed framework is easy to implement, because it requires proprioceptive sensors only to
perform and deploy data-efficient learning schemes. This makes the exoskeleton practical for
deployment in complex scenarios, accommodating different walking patterns, habits, tasks, and
conflicts. Experiments and comparative studies on a lower-limb exoskeleton robot are performed to
demonstrate the effectiveness of the proposed framework.
