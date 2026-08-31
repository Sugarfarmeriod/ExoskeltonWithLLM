# Reducing the energy cost of walking with low assistance levels through optimized hip flexion assistance from a soft exosuit

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Reducing the energy cost of walking with low assistance levels through optimized hip flexion assistance from a soft exosuit
- 作者：Jinsoo Kim; Brendan Quinlivan; Lou-Ana Deprey; Dheepak Arumukhom Revi; Asa Eckert‐Erdheim; Patrick Murphy; Dorothy Orzel; Conor J. Walsh
- 年份：2022
- 期刊/会议：Scientific Reports
- DOI：10.1038/s41598-022-14784-9
- URL：https://doi.org/10.1038/s41598-022-14784-9
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

助力时机/phase_offset, 助力强度/Amplitude/torque profile

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity；指标：metabolic cost, EMG reduction/activity

## 8. 实验对象和实验任务

8 participants

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
- 输出类型：control/impedance parameters, trajectory or gait features
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

As we age, humans see natural decreases in muscle force and power which leads to a slower, less
efficient gait. Improving mobility for both healthy individuals and those with muscle
impairments/weakness has been a goal for exoskeleton designers for decades. In this work, we
discover that significant reductions in the energy cost required for walking can be achieved with
almost 50% less mechanical power compared to the state of the art. This was achieved by leveraging
human-in-the-loop optimization to understand the importance of individualized assistance for hip
flexion, a relatively unexplored joint motion. Specifically, we show that a tethered hip flexion
exosuit can reduce the metabolic rate of walking by up to 15.2 ± 2.6%, compared to locomotion with
assistance turned off (equivalent to 14.8% reduction compared to not wearing the exosuit). This
large metabolic reduction was achieved with surprisingly low assistance magnitudes (average of 89 N,
~ 24% of normal hip flexion torque). Furthermore, the ratio of metabolic reduction to the positive
exosuit power delivered was 1.8 times higher than ratios previously found for hip extension and
ankle plantarflexion. These findings motivated the design of a lightweight (2.31 kg) and portable
hip flexion assisting exosuit, that demonstrated a 7.2 ± 2.9% metabolic reduction compared to
walking without the exosuit. The high ratio of metabolic reduction to exosuit power measured in this
study supports previous simulation findings and provides compelling evidence that hip flexion may be
an efficient joint motion to target when considering how to create practical and lightweight
wearable robots to support improved mobility.
