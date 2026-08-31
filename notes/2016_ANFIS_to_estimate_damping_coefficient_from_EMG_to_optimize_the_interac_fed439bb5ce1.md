# ANFIS to estimate damping coefficient from EMG to optimize the interaction force

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：ANFIS to estimate damping coefficient from EMG to optimize the interaction force
- 作者：Tanvir Anwar; Adel Al-Jumaily
- 年份：2016
- 期刊/会议：未提供
- DOI：10.1109/microcom.2016.7522589
- URL：https://doi.org/10.1109/microcom.2016.7522589
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

控制器/阻抗自适应

## 4. 控制底座

impedance control, high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity, interaction torque/force, comfort score, stability；指标：EMG reduction/activity, interaction torque/force, comfort score, stability

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 是否真实机器人闭环：not confirmed
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：future extension

## Abstract / Metadata Evidence

Although Lower Limb Robotic Rehabilitation device exhibit a great prospect in the rehabilitation of
impaired limb, yet it has not been widely applied to clinical rehabilitation. This is mostly due to
the insufficient bidirectional information interaction between exoskeleton and patient. In the
shared control at the interaction point, it is very important that the deficiency of impaired lower
limb in sharing the knee joint dynamics (Capturing of the intended action of the patient) is
extracted beforehand to estimate as to how much assistance the robotic exoskeleton would provide.
The intended action data that can be extracted from EMG signal may include the intended posture,
intended torque, intended knee joint angle, intended knee joint torque and impedance parameter. In
this paper, an application of Adaptive Network Based Fuzzy Inference System (ANFIS) has been
proposed for proprioceptive feedback on the status of the interaction force at the patient robotic
exoskeleton interaction point. ANFIS has been used to model the relationship between input and
output. Interaction forces, rate of change in surface electromyography (EMG) signal are two inputs
to ANFIS model and impedance parameters damping coefficients (also stiffness) is output. Impedance
control law has damping as one of the tuning parameter. The resultant total torque is calculated
from this law. The proposed model is able to estimate damping and demonstrate decent accuracy in
modulating the knee joint dynamics to minimize the interaction force at the Patient Exoskeleton
interaction point.
