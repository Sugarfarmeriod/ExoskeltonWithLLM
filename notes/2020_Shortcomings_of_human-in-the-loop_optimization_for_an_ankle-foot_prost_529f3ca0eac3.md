# Shortcomings of human-in-the-loop optimization for an ankle-foot prosthesis: a case series

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Shortcomings of human-in-the-loop optimization for an ankle-foot prosthesis: a case series
- 作者：Cara Gonzalez Welker; Alexandra S. Voloshina; Vincent L. Chiu; Steven H. Collins
- 年份：2020
- 期刊/会议：bioRxiv (Cold Spring Harbor Laboratory)
- DOI：10.1101/2020.10.17.343970
- URL：https://doi.org/10.1101/2020.10.17.343970
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式

## 3. AI 插入位置

参数优化器

## 4. 控制底座

PD/torque control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩

## 6. 输出参数

MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, gait symmetry, comfort score；指标：metabolic cost, gait symmetry, comfort score

## 8. 实验对象和实验任务

000 individuals

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖复杂 EMG 阵列、代谢仪或动作捕捉，需降级为参考目标函数，不作为最小系统前提。

## 12. 证据来源

PDF

## Abstract / Metadata Evidence

ABSTRACT Human-in-the-loop optimization allows for individualized device control based on measured
human performance. This technique has been used to produce large reductions in energy expenditure
during walking with exoskeletons but has not yet been applied to prosthetic devices. In this series
of case studies, we applied human-in-the-loop optimization to the control of an active ankle-foot
prosthesis used by participants with unilateral transtibial amputation. We optimized the parameters
of five control architectures that captured aspects of successful exoskeletons and commercial
prostheses, but none resulted in significantly lower metabolic rate than generic control. In one
control architecture, we increased the exposure time per condition by a factor of five, but the
optimized controller still resulted in higher metabolic rate. Finally, we optimized for self-
reported comfort instead of metabolic rate, but the resulting controller was not preferred. There
are several reasons why human-in-the-loop optimization may have failed for people with amputation.
Control architecture is an unlikely cause given the variety of controllers tested. The lack of
effect likely relates to adaptation protocol or differences in the learning mechanisms or objectives
of people with amputation. Future work should investigate these causes to determine whether human-
in-the-loop optimization for prostheses could be successful.
