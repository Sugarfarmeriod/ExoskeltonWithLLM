# A Lower Limb Exoskeleton Adaptive Control Method Based on Model-free Reinforcement Learning and Improved Dynamic Movement Primitives

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：A Lower Limb Exoskeleton Adaptive Control Method Based on Model-free Reinforcement Learning and Improved Dynamic Movement Primitives
- 作者：Liping Huang; Jianbin Zheng; Yifan Gao; Qiuzhi Song; Yali Liu
- 年份：2025
- 期刊/会议：Journal of Intelligent & Robotic Systems
- DOI：10.1007/s10846-025-02230-7
- URL：https://doi.org/10.1007/s10846-025-02230-7
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, DMP, PD/torque control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, interaction torque/force, comfort score, stability, safety constraint；指标：metabolic cost, interaction torque/force, comfort score, stability, safety constraint

## 8. 实验对象和实验任务

15 healthy

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Recent advancements in lower limb exoskeleton control have predominantly focused on enhancing
walking capabilities across diverse terrains, such as level ground, stairs, and ramps. However,
achieving seamless transitions between these terrains remains a significant challenge due to the
unpredictability of the environment, which hampers adaptive control. In this paper, we propose a
Hierarchical Interactive Learning (HIL) control method based on gait phase and locomotion pattern
recognition. The method comprises two layers: high-level learning and low-level control. The high-
level learning is based on gait phase and locomotion pattern recognition, utilizing the Dynamic
Movement Primitives (DMP) to piecewise learn the desired joint torque curves. The low-level control
utilizes the learned DMP to output torque based on the gait phase and locomotion pattern, while
reinforcement learning is employed to dynamically adjust the control parameters of DMP in real-time
with the goal of minimizing human-exoskeleton interaction forces. The experiments collected gait
data of lower limb movement from active exoskeletons. The results show that our method significantly
reduces human-exoskeleton interaction forces across diverse terrains. In order to verify the
feasibility and effectiveness of the proposed method, 15 healthy subjects were tested with the lower
limb exoskeleton of these 3 generations. The experimental results show that the proposed HIL control
method gives a valuable tool for smooth transitions among different terrains, reduces the reliance
on accurate dynamic models and the average oxygen consumption decreased by about 12%, underscoring
its potential to improve exoskeleton-assisted mobility.
