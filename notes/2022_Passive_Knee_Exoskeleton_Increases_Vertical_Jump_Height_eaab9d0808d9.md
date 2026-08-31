# Passive Knee Exoskeleton Increases Vertical Jump Height

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Passive Knee Exoskeleton Increases Vertical Jump Height
- 作者：Coral Ben-David; B. Ostraich; Raziel Riemer
- 年份：2022
- 期刊/会议：IEEE Transactions on Neural Systems and Rehabilitation Engineering
- DOI：10.1109/tnsre.2022.3187056
- URL：https://doi.org/10.1109/tnsre.2022.3187056
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost；指标：metabolic cost

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

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
- 输出类型：control/impedance parameters, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Most exoskeletons are designed to reduce the metabolic costs of performing aerobic tasks such as
walking, running, and hopping. This study presents an exoskeleton that boosts vertical jumping-a
fast, short movement during which the muscles are exerted at peak capacity. It was hypothesized that
a passive exoskeleton would increase vertical jump height without requiring external energy input.
The device comprises springs that work in parallel with the muscles of the quadriceps femoris. The
springs store mechanical energy during knee flexion (the negative work phase) and release that
energy during the subsequent knee extension (the positive work phase), augmenting the muscles. Ten
healthy participants were evaluated in two experimental sessions. In the first session, the
participants jumped without receiving instructions on how to use the exoskeleton, and the results
showed no difference in jump height when jumping with the exoskeleton or jumping without it. In the
second session, the participants were instructed to achieve deeper initial squat heights at the
start of the jump. This resulted in a 6.4% increase in average jump height compared to jumping
without the exoskeleton (each participant performed five jumps for each the two conditions). This is
the first time that a passive exoskeleton has been shown to improve the height of a vertical jump
from a dead stop.
