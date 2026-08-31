# Human-in-the-loop optimization of active plantarflexion exoskeleton assistance for one individual with chronic stroke

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Human-in-the-loop optimization of active plantarflexion exoskeleton assistance for one individual with chronic stroke
- 作者：未提供
- 年份：2019
- 期刊/会议：Gait &amp; Posture
- DOI：10.1016/j.gaitpost.2019.07.155
- URL：https://doi.org/10.1016/j.gaitpost.2019.07.155
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer, high-level interface

## 5. 输入数据

足底压力/力传感, 膝角度, 膝力矩/交互力矩, 治疗师/语义输入

## 6. 输出参数

助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, gait symmetry, safety constraint；指标：metabolic cost, gait symmetry, safety constraint

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：therapist instruction / clinical goal
- 输出类型：trajectory or gait features
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau, SafeTorque / safety constraints
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

未提供。
