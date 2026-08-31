# Exoskeleton robot control for synchronous walking assistance in repetitive manual handling works based on dual unscented Kalman filter

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Exoskeleton robot control for synchronous walking assistance in repetitive manual handling works based on dual unscented Kalman filter
- 作者：Sado Fatai; Hwa Jen Yap; Raja Ariffin Raja Ghazilla; Norhafizan Ahmad
- 年份：2018
- 期刊/会议：PLoS ONE
- DOI：10.1371/journal.pone.0200193
- URL：https://doi.org/10.1371/journal.pone.0200193
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, stability；指标：metabolic cost, EMG reduction/activity, stability

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

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

Prolong walking is a notable risk factor for work-related lower-limb disorders (WRLLD) in industries
such as agriculture, construction, service profession, healthcare and retail works. It is one of the
common causes of lower limb fatigue or muscular exhaustion leading to poor balance and fall.
Exoskeleton technology is seen as a modern strategy to assist worker's in these professions to
minimize or eliminate the risk of WRLLDs. Exoskeleton has potentials to benefit workers in prolong
walking (amongst others) by augmenting their strength, increasing their endurance, and minimizing
high muscular activation, resulting in overall work efficiency and productivity. Controlling
exoskeleton to achieve this purpose for able-bodied personnel without impeding their natural
movement is, however, challenging. In this study, we propose a control strategy that integrates a
Dual Unscented Kalman Filter (DUKF) for trajectory generation/prediction of the spatio-temporal
features of human walking (i.e. joint position, and velocity, and acceleration) and an impedance cum
supervisory controller to enable the exoskeleton to follow this trajectory to synchronize with the
human walking. Experiment is conducted with four subjects carrying a load and walking at their
normal speed- a typical scenario in industries. EMG signals taken at two muscles: Right Vastus
Intermedius (on the thigh) and Right Gastrocnemius (on the calf) indicated reduction in muscular
activation during the experiment. The results also show the ability of the control system to predict
spatio-temporal features of the pilots' walking and to enable the exoskeleton to move in concert
with the pilot.
