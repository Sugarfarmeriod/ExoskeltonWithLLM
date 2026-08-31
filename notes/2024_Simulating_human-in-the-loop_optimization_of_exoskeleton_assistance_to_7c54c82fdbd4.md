# Simulating human-in-the-loop optimization of exoskeleton assistance to compare optimization algorithm performance

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Simulating human-in-the-loop optimization of exoskeleton assistance to compare optimization algorithm performance
- 作者：Zoe Kutulakos; Patrick Slade
- 年份：2024
- 期刊/会议：未提供
- DOI：10.1101/2024.04.05.587982
- URL：https://doi.org/10.1101/2024.04.05.587982
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer, high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩, EMG, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, comfort score；指标：metabolic cost, EMG reduction/activity, comfort score

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

abstract only

## 13. 语义/治疗师输入扩展记录

- 输入类型：therapist instruction / clinical goal
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

Abstract Assistive robotic devices like exoskeletons offer the promise of improving mobility for
millions of people. However, developing devices that improve an objective mobility metric is
challenging. Human-in-the-loop optimization is a systematic approach for personalizing robotic
assistance to maximize a mobility metric that has improved device performance for different metrics
and applications. Successfully performing human-in-the-loop optimization requires the experimenter
to make many decisions, like selecting the appropriate optimization algorithm, hyperparameters, and
convergence criteria. Typically, selecting these experimental settings involves pilot
experimentation. We propose an approach that uses a probabilistic surrogate model, mapping
assistance parameters to corresponding experimental evaluations of the objective mobility metric, to
simulate human-in-the-loop optimization and inform these decisions. In this paper, we form a
surrogate model of the metabolic landscape of walking with exoskeleton assistance using an existing
experimental dataset. We simulate human-in-the-loop optimization by using a synthetic metabolic
landscape model to evaluate the metabolic cost of walking with different assistance parameters,
instead of performing an experimental measurement. We perform three simulated scenarios optimizing
assistance for an expert subject, a novice subject adapting to the device, and an expert subject
with up to 20 assistance parameters. The code and analyses from this work are open-source to promote
use by other researchers. Simulation enables direct comparison of optimization settings to inform
experimental human-in-the-loop optimization and potentially reduce the resources and time required
to develop effective assistive devices.
