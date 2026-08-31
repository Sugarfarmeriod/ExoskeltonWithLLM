# Framework for Personalizing Wearable Devices Using Real-Time Physiological Measures

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Framework for Personalizing Wearable Devices Using Real-Time Physiological Measures
- 作者：Prakyath Kantharaju; Sai Siddarth Vakacherla; Michael S. Jacobson; Hyeongkeun Jeong; Meet Nikunj Mevada; Xingyuan Zhou; Matthew J. Major; Myunghee Kim
- 年份：2023
- 期刊/会议：IEEE Access
- DOI：10.1109/access.2023.3299873
- URL：https://doi.org/10.1109/access.2023.3299873
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, comfort score, safety constraint；指标：metabolic cost, comfort score, safety constraint

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

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Personalizing wearable robots by incorporating user physiological feedback can improve energy
efficiency and comfort. However, many current personalization methods are specific to a particular
device and often require reprogramming, making them less accessible. In this study, we present an
open-source, device-independent personalization framework that allows for human-in-the-loop
optimization. This modular framework includes cost functions and optimization algorithms that use a
physiological response to optimize wearable robot parameters. We tested this framework in three case
studies involving diverse subjects and wearable robots. The first case study focused on
personalizing an ankle-foot prosthesis using indirect calorimetry feedback. This resulted in a 5.3%
and 18.1% reduction in metabolic cost for walking for two individuals with transtibial amputation,
compared to the weight-based assistance. The second case study personalized a robotic ankle
exoskeleton for three different walking speeds using indirect calorimetry feedback for two subjects.
The metabolic cost was reduced by 1%, 2%, and 5.8% for one subject and by 20.8%, 1.9%, and 19% for
the other subject, compared to a generic assistance condition for increasing speeds. The third case
study personalized gait parameters, specifically step frequency, using an electrocardiogram
(ECG)-based cost function along with an optimization algorithm variant, resulting in a 43% reduction
in optimization time for one able-bodied subject. These case studies suggest that our
personalization framework can effectively personalize wearable robot parameters and potentially
enhance assistance benefits.
