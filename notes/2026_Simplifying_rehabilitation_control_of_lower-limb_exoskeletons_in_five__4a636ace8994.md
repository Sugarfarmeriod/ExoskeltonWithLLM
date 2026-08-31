# Simplifying rehabilitation control of lower-limb exoskeletons in five ambulation modes via dataset-driven state-machine calibration

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Simplifying rehabilitation control of lower-limb exoskeletons in five ambulation modes via dataset-driven state-machine calibration
- 作者：Clément Lhoste; Alberto Cantón; Emek Barış Küçüktabak; Matthew R. Short; Rebecca Schwanemann; Shoshana Clark; Daniel Ludvig; Kevin Lynch
- 年份：2026
- 期刊/会议：Journal of NeuroEngineering and Rehabilitation
- DOI：10.1186/s12984-026-01917-8
- URL：https://doi.org/10.1186/s12984-026-01917-8
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer, high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

interaction torque/force；指标：interaction torque/force

## 8. 实验对象和实验任务

19 healthy

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

Lower-limb exoskeletons are a useful tool in rehabilitation settings as they can provide customized
assistance to individuals during functional exercises. These approaches typically rely on state-
machine-based control with impedance controllers tailored to different locomotion phases, ensuring
appropriate assistance across various activities and environments. However, these methods
necessitate lengthy calibration procedures, as many impedance parameters need to be fine-tuned to
provide appropriate assistance for various activities (e.g., overground walking, ramps, and stairs).
This study presents three contributions: (1) a state-machine-based control strategy for partial
assistance lower-limb exoskeletons, (2) a computational method to extract reference trajectories
from a benchmark dataset (Camargo et al. in J Biomech 119:110320, 2021), enabling the identification
of state-machine controller parameters and simplifying calibration procedures and (3) a dataset of
19 healthy individuals walking in five walking conditions (overground walking, upstairs, downstairs,
up ramps, and down ramps) using either the state-machine approach or a transparent controller. The
state-machine controller produced in average more negative interaction power ($$-2.6\times 10^{-2}$$
W/kg) compared to transparent control ($$0.8\times 10^{-2}$$ W/kg), indicating greater user
assistance. Preferred walking speed was notably faster with the state-machine controller,
particularly on level ground, ramps and stairs ascent (25–32% increase). Kinematic analysis revealed
closer alignment to able-bodied gait patterns with the state-machine controller, suggesting improved
gait quality. At the same time, the dataset of the collected locomotion activities (dataset link)
will constitute a new benchmark dataset for locomotion. In this work, we presented and evaluated a
novel state-machine-based control strategy for partial-assistance lower-limb exoskeletons. In this
approach, reference trajectories are extracted from a benchmark dataset, simplifying calibration
procedures. Additionally, we provide a dataset of 19 healthy individuals using two exoskeleton
controllers. The proposed controller will be applied to patient populations, while the dataset will
serve as a valuable resource for advancing robust and effective control mechanisms through machine
learning techniques.
