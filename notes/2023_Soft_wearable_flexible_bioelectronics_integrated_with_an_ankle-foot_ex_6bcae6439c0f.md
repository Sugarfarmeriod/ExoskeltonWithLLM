# Soft wearable flexible bioelectronics integrated with an ankle-foot exoskeleton for estimation of metabolic costs and physical effort

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Soft wearable flexible bioelectronics integrated with an ankle-foot exoskeleton for estimation of metabolic costs and physical effort
- 作者：Jihoon Kim; Prakyath Kantharaju; Hoon Yi; Michael S. Jacobson; Hyungkeun Jeong; Hojoong Kim; Jinwoo Lee; Jared Matthews
- 年份：2023
- 期刊/会议：npj Flexible Electronics
- DOI：10.1038/s41528-023-00239-2
- URL：https://doi.org/10.1038/s41528-023-00239-2
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度

## 6. 输出参数

助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, comfort score, stability；指标：metabolic cost, comfort score, stability

## 8. 实验对象和实验任务

未从摘要确认

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
- 输出类型：control/impedance parameters
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Abstract Activities and physical effort have been commonly estimated using a metabolic rate through
indirect calorimetry to capture breath information. The physical effort represents the work hardness
used to optimize wearable robotic systems. Thus, personalization and rapid optimization of the
effort are critical. Although respirometry is the gold standard for estimating metabolic costs, this
method requires a heavy, bulky, and rigid system, limiting the system’s field deployability. Here,
this paper reports a soft, flexible bioelectronic system that integrates a wearable ankle-foot
exoskeleton, used to estimate metabolic costs and physical effort, demonstrating the potential for
real-time wearable robot adjustments based on biofeedback. Data from a set of activities, including
walking, running, and squatting with the biopatch and exoskeleton, determines the relationship
between metabolic costs and heart rate variability root mean square of successive differences (HRV-
RMSSD) ( R = −0.758). Collectively, the exoskeleton-integrated wearable system shows potential to
develop a field-deployable exoskeleton platform that can measure wireless real-time physiological
signals.
