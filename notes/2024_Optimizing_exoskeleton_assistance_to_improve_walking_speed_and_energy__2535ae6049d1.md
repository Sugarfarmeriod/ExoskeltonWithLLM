# Optimizing exoskeleton assistance to improve walking speed and energy economy for older adults

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Optimizing exoskeleton assistance to improve walking speed and energy economy for older adults
- 作者：Ava Lakmazaheri; Seungmoon Song; Brian B. Vuong; Blake Biskner; Deborah M. Kado; Steven H. Collins
- 年份：2024
- 期刊/会议：Journal of NeuroEngineering and Rehabilitation
- DOI：10.1186/s12984-023-01287-5
- URL：https://doi.org/10.1186/s12984-023-01287-5
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, comfort score, safety constraint；指标：metabolic cost, comfort score, safety constraint

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
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

BACKGROUND: Walking speed and energy economy tend to decline with age. Lower-limb exoskeletons have
demonstrated potential to improve either measure, but primarily in studies conducted on healthy
younger adults. Promising techniques like optimization of exoskeleton assistance have yet to be
tested with older populations, while speed and energy consumption have yet to be simultaneously
optimized for any population. METHODS: We investigated the effectiveness of human-in-the-loop
optimization of ankle exoskeletons with older adults. Ten healthy adults > 65 years of age (5
females; mean age: 72 ± 3 yrs) participated in approximately 240 min of training and optimization
with tethered ankle exoskeletons on a self-paced treadmill. Multi-objective human-in-the-loop
optimization was used to identify assistive ankle plantarflexion torque patterns that simultaneously
improved self-selected walking speed and metabolic rate. The effects of optimized exoskeleton
assistance were evaluated in separate trials. RESULTS: Optimized exoskeleton assistance improved
walking performance for older adults. Both objectives were simultaneously improved; self-selected
walking speed increased by 8% (0.10 m/s; p = 0.001) and metabolic rate decreased by 19% (p = 0.007),
resulting in a 25% decrease in energetic cost of transport (p = 8e-4) compared to walking with
exoskeletons applying zero torque. Compared to younger participants in studies optimizing a single
objective, our participants required lower exoskeleton torques, experienced smaller improvements in
energy use, and required more time for motor adaptation. CONCLUSIONS: Our results confirm that
exoskeleton assistance can improve walking performance for older adults and show that multiple
objectives can be simultaneously addressed through human-in-the-loop optimization.
