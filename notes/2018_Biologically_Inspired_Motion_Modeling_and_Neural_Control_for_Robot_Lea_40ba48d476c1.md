# Biologically Inspired Motion Modeling and Neural Control for Robot Learning From Demonstrations

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Biologically Inspired Motion Modeling and Neural Control for Robot Learning From Demonstrations
- 作者：Chenguang Yang; Chuize Chen; Ning Wang; Zhaojie Ju; Jian Fu; Min Wang
- 年份：2018
- 期刊/会议：IEEE Transactions on Cognitive and Developmental Systems
- DOI：10.1109/tcds.2018.2866477
- URL：https://doi.org/10.1109/tcds.2018.2866477
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

stability, safety constraint；指标：stability, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

In this paper, we propose a biologically inspired framework for robot learning based on
demonstrations. The dynamic movement primitive (DMP), which is motivated by neurobiology and human
behavior, is employed to model a robotic motion that is generalizable. However, the DMP method can
only be used to handle a single demonstration. To enable the robot to learn from multiple
demonstrations, the DMP is combined with the Gaussian mixture model (GMM) to integrate the features
of multiple demonstrations, where the conventional GMM is further replaced by the fuzzy GMM (FGMM)
to improve the fitting performance. Also, a novel regression algorithm for FGMM is derived to
retrieve the nonlinear term of the DMP. Additionally, a neural network-based controller is developed
for the robot to track the generated motions. In this network, the cerebellar model articulation
controller is employed to compensate for the unknown robot dynamics. The experiments have been
performed on a Baxter robot to demonstrate the effectiveness of the proposed methods.
