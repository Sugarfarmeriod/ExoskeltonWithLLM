# Ultra-Robust Real-Time Estimation of Gait Phase

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Ultra-Robust Real-Time Estimation of Gait Phase
- 作者：Mohammad Shushtari; Hannah Dinovitzer; Jiacheng Weng; Arash Arami
- 年份：2022
- 期刊/会议：IEEE Transactions on Neural Systems and Rehabilitation Engineering
- DOI：10.1109/tnsre.2022.3207919
- URL：https://doi.org/10.1109/tnsre.2022.3207919
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

gait symmetry, RMSE；指标：gait symmetry, RMSE

## 8. 实验对象和实验任务

14 participants

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

- 输入类型：GUI/button/shared-control interface
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

An ultra-robust accurate gait phase estimator is developed by training a time-delay neural network
(D67) on data collected from the hip and knee joint angles of 14 participants during treadmill and
overground walking. Collected data include normal gait at speeds ranging from 0.1m/s to 1.9m/s and
conditions such as long stride, short stride, asymmetric walking, stop-start, and abrupt speed
changes. Spatial analysis of our method indicates an average RMSE of 1.74±0.23% and 2.35±0.52% in
gait phase estimation of test participants in the treadmill and overground walking, respectively.
The temporal analysis reveals that D67 detects heel-strike events with an average MAE of 1.70±0.54%
and 2.74±0.92% of step duration on test participants in the treadmill and overground walking,
respectively. Both spatial and temporal performances are uniform across participants and gait
conditions. Further analyses indicate the robustness of the D67 to smooth and abrupt speed changes,
limping, variation of stride length, and sudden start or stop of walking. The performance of the D67
is also compared to the state-of-the-art techniques confirming the superior and comparable
performance of the D67 to techniques without and with a ground contact sensor, respectively. The
estimator is finally tested on a participant walking with an active exoskeleton, demonstrating the
robustness of D67 in interaction with an exoskeleton without being trained on any data from the test
subject with or without an exoskeleton.
