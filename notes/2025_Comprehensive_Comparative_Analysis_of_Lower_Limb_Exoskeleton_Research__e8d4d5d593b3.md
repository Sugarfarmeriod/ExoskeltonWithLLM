# Comprehensive Comparative Analysis of Lower Limb Exoskeleton Research: Control, Design, and Application

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Comprehensive Comparative Analysis of Lower Limb Exoskeleton Research: Control, Design, and Application
- 作者：Sk Hasan; Nafizul Alam
- 年份：2025
- 期刊/会议：未提供
- DOI：10.20944/preprints202505.2023.v1
- URL：https://doi.org/10.20944/preprints202505.2023.v1
- PDF 状态：abstract_only

## 2. 一句话结论

可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

状态估计器

## 4. 控制底座

impedance control, PD/torque control, high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩, EMG, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, stability；指标：metabolic cost, EMG reduction/activity, stability

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

abstract only

## 13. 语义/治疗师输入扩展记录

- 输入类型：GUI/button/shared-control interface
- 输出类型：trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：simulation only
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：future extension

## Abstract / Metadata Evidence

This review provides a comprehensive analysis of recent advancements in lower limb exoskeleton
systems, focusing on applications, control strategies, hardware architecture, sensing modalities,
human-robot interaction, evaluation methods, and technical innovations. The study spans systems
developed for gait rehabilitation, mobility assistance, terrain adaptation, pediatric use, and
industrial support. Applications range from sit-to-stand transitions and post-stroke therapy to
balance support and real-world navigation. Control approaches vary from traditional impedance and
fuzzy logic models to advanced data-driven frameworks including reinforcement learning, recurrent
neural networks, and digital twin-based optimization. These controllers support personalized and
adaptive interaction, enabling real-time intent recognition, torque modulation, and gait phase
synchronization across different users and tasks. Hardware platforms include powered multi-degree-
of-freedom exoskeletons, passive assistive devices, compliant joint systems, and pediatric-specific
configurations. Innovations in actuator design, modular architecture, and lightweight materials
support increased usability and energy efficiency. Sensor systems integrate EMG, EEG, IMU, vision,
and force feedback, supporting multimodal perception for motion prediction, terrain classification,
and user monitoring. Human-robot interaction strategies emphasize safe, intuitive, and cooperative
engagement. Controllers are increasingly user-specific, leveraging biosignals and gait metrics to
tailor assistance. Evaluation methodologies include simulation, phantom testing, and human-subject
trials across clinical and real-world environments, with performance measured through joint tracking
accuracy, stability indices, and functional mobility scores. Overall, the review highlights the
field’s evolution toward intelligent, adaptable, and user-centered systems, offering promising
solutions for rehabilitation, mobility enhancement, and assistive autonomy in diverse populations.
Following a detailed review of current developments, strategic recommendations are made to enhance
and evolve existing exoskeleton technologies.
