# Optimization of Torque-Control Model for Quasi-Direct-Drive Knee Exoskeleton Robots Based on Regression Forecasting

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Optimization of Torque-Control Model for Quasi-Direct-Drive Knee Exoskeleton Robots Based on Regression Forecasting
- 作者：Yuxuan Xia; Wei Wei; Xichuan Lin; Jiaqian Li
- 年份：2024
- 期刊/会议：Sensors
- DOI：10.3390/s24051505
- URL：https://doi.org/10.3390/s24051505
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, PD/torque control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity, safety constraint；指标：EMG reduction/activity, safety constraint

## 8. 实验对象和实验任务

23 subjects

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

abstract only

## 13. 语义/治疗师输入扩展记录

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

The choice of torque curve in lower-limb enhanced exoskeleton robots is a key problem in the control
of lower-limb exoskeleton robots. As a human-machine coupled system, mapping from sensor data to
joint torque is complex and non-linear, making it difficult to accurately model using mathematical
tools. In this research study, the knee torque data of an exoskeleton robot climbing up stairs were
obtained using an optical motion-capture system and three-dimensional force-measuring tables, and
the inertial measurement unit (IMU) data of the lower limbs of the exoskeleton robot were
simultaneously collected. Nonlinear approximations can be learned using machine learning methods. In
this research study, a multivariate network model combining CNN and LSTM was used for nonlinear
regression forecasting, and a knee joint torque-control model was obtained. Due to delays in
mechanical transmission, communication, and the bottom controller, the actual torque curve will lag
behind the theoretical curve. In order to compensate for these delays, different time shifts of the
torque curve were carried out in the model-training stage to produce different control models. The
above model was applied to a lightweight knee exoskeleton robot. The performance of the exoskeleton
robot was evaluated using surface electromyography (sEMG) experiments, and the effects of different
time-shifting parameters on the performance were compared. During testing, the sEMG activity of the
rectus femoris (RF) decreased by 20.87%, while the sEMG activity of the vastus medialis (VM)
increased by 17.45%. The experimental results verify the effectiveness of this control model in
assisting knee joints in climbing up stairs.
