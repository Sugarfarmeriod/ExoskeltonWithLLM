# A Two-Layer Human-in-the-Loop Optimization Framework for Customizing Lower-Limb Exoskeleton Assistance

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：A Two-Layer Human-in-the-Loop Optimization Framework for Customizing Lower-Limb Exoskeleton Assistance
- 作者：Siqi Zheng; Ge Lv
- 年份：2023
- 期刊/会议：未提供
- DOI：10.36227/techrxiv.22327378.v1
- URL：https://doi.org/10.36227/techrxiv.22327378.v1
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer, high-level interface

## 5. 输入数据

IMU, 膝速度, 膝力矩/交互力矩, EMG, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, stability, safety constraint；指标：metabolic cost, EMG reduction/activity, stability, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

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
- 是否真实机器人闭环：simulation only
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：future extension

## Abstract / Metadata Evidence

Task-invariant control paradigms can enable lowerlimb exoskeletons to provide assistance for their
users across various locomotor tasks without prescribing to specific joint kinematics. As an
energetic control method, energy shaping can alter a human's body energetics in the closed-loop to
provide gait benefits. To obtain the energy shaping law for underactuated systems, a set of
nonlinear partial differential equations, called the matching condition, needs to be solved to
determine the achievable closed-loop dynamics. However, solving matching conditions for high-
dimensional nonlinear systems is generally difficult. In addition, how to define parameters for the
closed-loop dynamics that render the optimal exoskeleton assistance remains unclear. In this paper,
we proposed a twolayer, human-in-the-loop optimization framework for lower-limb exoskeletons to
customize their assistance to human users. The inner-layer optimization finds solutions to the
matching condition, meanwhile following the energy trajectories of a virtual reference model defined
based on the self-selected gaits of humans and a scaled version of their anatomical parameters. The
outer-layer incorporates human-in-the-loop Bayesian Optimization to update reference energy's
parameters for reducing metabolic costs. Simulation results on two biped models demonstrate that the
proposed framework can solve matching conditions numerically at the selected timestamps and the
associated energy shaping strategies can reduce human metabolic cost. Moreover, exoskeletons torques
calculated using an able-bodied subject's kinematic data well match human biological torques.
