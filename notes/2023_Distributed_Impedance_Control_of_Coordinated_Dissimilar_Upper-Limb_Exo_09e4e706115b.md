# Distributed Impedance Control of Coordinated Dissimilar Upper-Limb Exoskeleton Arms

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Distributed Impedance Control of Coordinated Dissimilar Upper-Limb Exoskeleton Arms
- 作者：S. Mohammad Tahamipour-Z.; Jouni Mattila
- 年份：2023
- 期刊/会议：未提供
- DOI：10.36227/techrxiv.21679430.v3
- URL：https://doi.org/10.36227/techrxiv.21679430.v3
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity, interaction torque/force, comfort score, stability；指标：EMG reduction/activity, interaction torque/force, comfort score, stability

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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

Upper-limb exoskeleton (ULE) arms have the potential to assist humans in accomplishing tasks by
distributing a heavy load. ULE arms are designed to be comfortable and lightweight wearable robotic
devices, a design that has resulted in the complexity of their structures, actuators, and power
transmissions. Additionally, different ULE vendor structures and biomechanical variations between
humans have resulted in dissimilar coordinated ULE arm systems. These complex multiple ULE arm
systems can be handled through adaptive virtual decomposition control (VDC) if unknown dynamic
models are not considered. Accordingly, this paper proposes a new distributed framework for the
adaptive impedance-based VDC method to address the abovementioned challenges and thereby enhance the
performance and robustness of the ULE arm systems. To that end, the proposed control method has a
prediction capability and an ancillary control law for coordinated dissimilar ULE arms holding a
common object. The system stability is analyzed using the input-to-state stability approach. The
performance of the proposed controller is evaluated both in simulation with six coordinated ULE arms
and in an experiment with two commercial coordinated ULE arms each with seven degrees of freedom.
Four scenarios are performed with different internal arm forces with and without an obstacle. The
simulation and experiment results are compared with a state-of-the-art adaptive VDC method and show
the superiority of the proposed control method.
