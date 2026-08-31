# Powered knee exoskeleton improves sit-to-stand transitions in stroke patients using electromyographic control

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Powered knee exoskeleton improves sit-to-stand transitions in stroke patients using electromyographic control
- 作者：Andrew J. Gunnell; Sergei V. Sarkisian; Heather Hayes; K. Bo Foreman; Lukas Gabert; Tommaso Lenzi
- 年份：2025
- 期刊/会议：Communications Engineering
- DOI：10.1038/s44172-025-00440-3
- URL：https://doi.org/10.1038/s44172-025-00440-3
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity, gait symmetry, stability；指标：EMG reduction/activity, gait symmetry, stability

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

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
- 输出类型：mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Millions of stroke survivors are affected by hemiparesis, resulting in difficulty or inability to
move one side of their body. Hemiparesis severely impacts the ability of individuals to perform
essential everyday activities, reducing independence and quality of life. Here we show that a
powered knee exoskeleton that assists the affected knee joint using proportional electromyographic
control significantly improves the ability to stand up from a seated position in eight stroke
survivors. With the exoskeleton, stroke survivors stood up significantly faster (8.8% reduction in
stand-up time), more symmetrically (13.7% increase in weight-bearing symmetry), and with less effort
on their affected side (32% reduction in peak quadriceps muscle activation, 25% reduction in peak
biological torque generation). The exoskeleton effectively supplemented the lack of strength in
their affected knee, increasing the total knee torque by 59%, which more closely matched their non-
affected knee. These results suggest that powered knee exoskeletons are a promising solution for
enhancing stand-up ability, improving symmetry, reducing effort, and ultimately enhancing stroke
survivors’ mobility and quality of life. Andrew J. Gunnell and colleagues show that a powered knee
exoskeleton helped stroke survivors stand up faster, more evenly, and with less effort. The results
suggest this technology could improve mobility and independence for people with stroke-related
weakness.
