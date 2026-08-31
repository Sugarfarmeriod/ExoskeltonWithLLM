# Hip Exoskeleton for Cycling Assistance

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Hip Exoskeleton for Cycling Assistance
- 作者：Martin Grimmer; Guoping Zhao
- 年份：2024
- 期刊/会议：Bioengineering
- DOI：10.3390/bioengineering11070683
- URL：https://doi.org/10.3390/bioengineering11070683
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset

## 7. 目标函数或评价指标

metabolic cost, comfort score；指标：metabolic cost, comfort score

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖复杂 EMG 阵列、代谢仪或动作捕捉，需降级为参考目标函数，不作为最小系统前提。

## 12. 证据来源

abstract only

## Abstract / Metadata Evidence

Cycling stands as one of the most widely embraced leisure activities and serves purposes such as
exercise, rehabilitation, and commuting. This study aimed to assess the feasibility of assisting
three unimpaired participants (age: 34.0 ± 7.9 years, height: 1.86 ± 0.02 m, weight: 75.7 ± 12.7 kg)
using the GuroX hip exoskeleton, originally designed for walking assistance, during cycling against
a resistance of 1 W/kg. The performance evaluation employed a sweep protocol that manipulated the
timing of the exoskeleton's peak extension and flexion torque in addition to human-in-the-loop
optimization to enhance these timings based on metabolic cost. Our findings indicate that with a
peak assistance torque of approximately 10.3 Nm for extension and flexion, the GuroX substantially
reduced the net metabolic cost of cycling by 31.4 ± 8.1% and 26.4 ± 14.1% compared to transparent
and without exoskeleton conditions, respectively. This demonstrates the significant potential of a
hip exoskeleton developed for walking assistance to profoundly benefit cycling. Additionally,
customizing the assistance strategy proves beneficial in maximizing assistance. While we attribute
the average motor power to be a major contributor to the reduced cycling effort, participant
feedback suggests that user comfort and synchronization between the user and exoskeleton may have
played integral roles. Further research should validate our initial findings by employing a larger
participant pool in real-world conditions. Incorporating a more diverse set of parameters for the
human-in-the-loop optimization could enhance individualized assistance strategies.
