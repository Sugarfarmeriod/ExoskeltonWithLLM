# Foot contact forces can be used to personalize a wearable robot during human walking

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Foot contact forces can be used to personalize a wearable robot during human walking
- 作者：Michael S. Jacobson; Prakyath Kantharaju; Hyeongkeun Jeong; Jae-Kwan Ryu; Jung-Jae Park; Hyun-Joon Chung; Myunghee Kim
- 年份：2022
- 期刊/会议：Scientific Reports
- DOI：10.1038/s41598-022-14776-9
- URL：https://doi.org/10.1038/s41598-022-14776-9
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, gait symmetry, comfort score；指标：metabolic cost, EMG reduction/activity, gait symmetry, comfort score

## 8. 实验对象和实验任务

8 individuals

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Individuals with below-knee amputation (BKA) experience increased physical effort when walking, and
the use of a robotic ankle-foot prosthesis (AFP) can reduce such effort. The walking effort could be
further reduced if the robot is personalized to the wearer using human-in-the-loop (HIL)
optimization of wearable robot parameters. The conventional physiological measurement, however,
requires a long estimation time, hampering real-time optimization due to the limited experimental
time budget. This study hypothesized that a function of foot contact force, the symmetric foot
force-time integral (FFTI), could be used as a cost function for HIL optimization to rapidly
estimate the physical effort of walking. We found that the new cost function presents a reasonable
correlation with measured metabolic cost. When we employed the new cost function in HIL ankle-foot
prosthesis stiffness parameter optimization, 8 individuals with simulated amputation reduced their
metabolic cost of walking, greater than 15% (p < 0.02), compared to the weight-based and control-off
conditions. The symmetry cost using the FFTI percentage was lower for the optimal condition,
compared to all other conditions (p < 0.05). This study suggests that foot force-time integral
symmetry using foot pressure sensors can be used as a cost function when optimizing a wearable robot
parameter.
