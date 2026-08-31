# EMG-based Human-In-The Loop Bayesian Optimization to Assist Free Leg Swinging

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：EMG-based Human-In-The Loop Bayesian Optimization to Assist Free Leg Swinging
- 作者：Salvador Echeveste; Pranav A. Bhounsule
- 年份：2025
- 期刊/会议：Preprints.org
- DOI：10.20944/preprints202501.1346.v1
- URL：https://doi.org/10.20944/preprints202501.1346.v1
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, interaction torque/force, comfort score, stability；指标：metabolic cost, EMG reduction/activity, interaction torque/force, comfort score, stability

## 8. 实验对象和实验任务

未从摘要确认

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

abstract only

## 13. 语义/治疗师输入扩展记录

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Background/Objectives: Manual tuning of exoskeleton control parameters is tedious and often
ineffective for adapting to individual users. Human-in-the-loop (HIL) optimization offers an
automated approach, but existing methods typically rely on metabolic cost, which requires prolonged
data collection times of at least 60 seconds. Surface electromyography (EMG) signals, as an
alternative, enable faster optimization with reduced data acquisition times. This study develops a
rapid EMG-based HIL Bayesian optimization framework to tune hip exoskeleton controllers for
assisting free leg swinging. Methods: Eight participants are asked to perform leg swinging at two
frequencies with assistance from a hip exoskeleton. EMG signals from four sensors, representing
muscle activity during forward and backward swings, are dynamically processed into cost functions.
Bayesian optimization with Gaussian processes tunes four controller parameters using an Expected
Improvement acquisition function. Optimization outcomes are validated against no device, zero
torque, and general control baselines. Results: Optimization converged within 142 ± 24 seconds,
yielding muscle activity reductions of 16.1 compared to no device, 21.7% versus zero torque, and
15.1% versus general control (p &amp;amp;lt; 0.001 for all). EMG-based tuning is faster than
metabolic-cost-based methods and perceived as less effortful, with Borg scale reductions of up to
39.5%. Conclusions: EMG-based HIL optimization significantly enhances controller tuning speed and
effectiveness, demonstrating its potential for scalable and user-specific exoskeleton applications.
