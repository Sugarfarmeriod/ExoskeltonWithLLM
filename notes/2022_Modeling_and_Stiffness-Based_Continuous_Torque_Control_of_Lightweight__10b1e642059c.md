# Modeling and Stiffness-Based Continuous Torque Control of Lightweight Quasi-Direct-Drive Knee Exoskeletons for Versatile Walking Assistance

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Modeling and Stiffness-Based Continuous Torque Control of Lightweight Quasi-Direct-Drive Knee Exoskeletons for Versatile Walking Assistance
- 作者：Tzu-Hao Huang; Sainan Zhang; Shuangyue Yu; Mhairi K. MacLean; Junxi Zhu; Antonio Di Lallo; Chunhai Jiao; Thomas C. Bulea
- 年份：2022
- 期刊/会议：IEEE Transactions on Robotics
- DOI：10.1109/tro.2022.3170287
- URL：https://doi.org/10.1109/tro.2022.3170287
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, PD/torque control, low-frequency optimizer

## 5. 输入数据

足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

safety constraint；指标：safety constraint

## 8. 实验对象和实验任务

23 subjects

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束

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

State-of-the-art exoskeletons are typically limited by low control bandwidth and small range
stiffness of actuators which are based on high gear ratios and elastic components (e.g., series
elastic actuators). Furthermore, most exoskeletons are based on discrete gait phase detection and/or
discrete stiffness control resulting in discontinuous torque profiles. To fill these two gaps, we
developed a portable lightweight knee exoskeleton using quasi-direct drive (QDD) actuation that
provides 14 Nm torque (36.8% biological joint moment for overground walking). This paper presents 1)
stiffness modeling of torque-controlled QDD exoskeletons and 2) stiffness-based continuous torque
controller that estimates knee joint moment in real-time. Experimental tests found the exoskeleton
had high bandwidth of stiffness control (16 Hz under 100 Nm/rad) and high torque tracking accuracy
with 0.34 Nm Root Mean Square (RMS) error (6.22%) across 0-350 Nm/rad large range stiffness. The
continuous controller was able to estimate knee moments accurately and smoothly for three walking
speeds and their transitions. Experimental results with 8 able-bodied subjects demonstrated that our
exoskeleton was able to reduce the muscle activities of all 8 measured knee and ankle muscles by
8.60%-15.22% relative to unpowered condition, and two knee flexors and one ankle plantar flexor by
1.92%-10.24% relative to baseline (no exoskeleton) condition.
