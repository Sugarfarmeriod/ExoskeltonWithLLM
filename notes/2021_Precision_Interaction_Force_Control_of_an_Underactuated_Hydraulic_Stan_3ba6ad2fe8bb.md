# Precision Interaction Force Control of an Underactuated Hydraulic Stance Leg Exoskeleton Considering the Constraint from the Wearer

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Precision Interaction Force Control of an Underactuated Hydraulic Stance Leg Exoskeleton Considering the Constraint from the Wearer
- 作者：Shan Chen; Tenghui Han; Fangfang Dong; Lei Lu; Haijun Liu; Xiaoqing Tian; Jiang Han
- 年份：2021
- 期刊/会议：Machines
- DOI：10.3390/machines9050096
- URL：https://doi.org/10.3390/machines9050096
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, PD/torque control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩

## 6. 输出参数

MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

interaction torque/force, safety constraint；指标：interaction torque/force, safety constraint

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：GUI/button/shared-control interface
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：simulation only
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Hydraulic lower limb exoskeletons are wearable robotic systems, which can help people carry heavy
loads. Recently, underactuated exoskeletons with some passive joints have been developed in large
numbers for the purpose of decreasing the weight and energy consumption of the system. There are
many control algorithms for a multi-joint fully actuated exoskeleton, which cannot be applied for
underactuated systems due to the reduction in the number of control inputs. Besides, since the
hydraulic actuator is not a desired force output source, there exist high order nonlinearities in
hydraulic exoskeletons, which makes the controller design more challenging than motor driven
exoskeleton systems. This paper proposed a precision interaction force controller for a 3DOF
underactuated hydraulic stance leg exoskeleton. First, the control effect of the wearer is
considered and the posture of the exoskeleton back is assumed as a desired trajectory under the
control of the wearer. Under this assumption, the system dynamics are changed from a 3DOF
underactuated system in joint space to a 2DOF fully actuated system in Cartesian space. Then, a
three-level interaction force controller is designed in which the high-level controller conducts
human motion intent inference, the middle level controller tracks human motion and the low-level
controller achieves output force tracking of hydraulic cylinders. The MIMO adaptive robust control
algorithm is applied in the controller design to effectively address the high order nonlinearities
of the hydraulic system, multi-joint couplings and various model uncertainties. A gain tuning method
is also provided to facilitate the controller gains selection for engineers. Comparative simulations
are conducted, which demonstrate that the principal human-machine interaction force components can
be minimized and good robust performance to load change and modeling errors can be achieved.
