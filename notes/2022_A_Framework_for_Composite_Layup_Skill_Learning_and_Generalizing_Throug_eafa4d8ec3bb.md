# A Framework for Composite Layup Skill Learning and Generalizing Through Teleoperation

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：A Framework for Composite Layup Skill Learning and Generalizing Through Teleoperation
- 作者：Weiyong Si; Ning Wang; Qinchuan Li; Chenguang Yang
- 年份：2022
- 期刊/会议：Frontiers in Neurorobotics
- DOI：10.3389/fnbot.2022.840240
- URL：https://doi.org/10.3389/fnbot.2022.840240
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, DMP, low-frequency optimizer, high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 治疗师/语义输入

## 6. 输出参数

MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

stability, safety constraint；指标：stability, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：natural language / LLM
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

In this article, an impedance control-based framework for human-robot composite layup skill transfer
was developed, and the human-in-the-loop mechanism was investigated to achieve human-robot skill
transfer. Although there are some works on human-robot skill transfer, it is still difficult to
transfer the manipulation skill to robots through teleoperation efficiently and intuitively. In this
article, we developed an impedance-based control architecture of telemanipulation in task space for
the human-robot skill transfer through teleoperation. This framework not only achieves human-robot
skill transfer but also provides a solution to human-robot collaboration through teleoperation. The
variable impedance control system enables the compliant interaction between the robot and the
environment, smooth transition between different stages. Dynamic movement primitives based learning
from demonstration (LfD) is employed to model the human manipulation skills, and the learned skill
can be generalized to different tasks and environments, such as the different shapes of components
and different orientations of components. The performance of the proposed approach is evaluated on a
7 DoF Franka Panda through the robot-assisted composite layup on different shapes and orientations
of the components.
