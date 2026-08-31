# Step length adaptation for walking assistance

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Step length adaptation for walking assistance
- 作者：Qiming Chen; Hong Cheng; Chunfeng Yue; Rui Huang; Hongliang Guo
- 年份：2017
- 期刊/会议：未提供
- DOI：10.1109/icma.2017.8015892
- URL：https://doi.org/10.1109/icma.2017.8015892
- PDF 状态：abstract_only

## 2. 一句话结论

与外骨骼 AI 控制相关，但需要全文确认可接入性

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

DMP

## 5. 输入数据

IMU

## 6. 输出参数

待确认

## 7. 目标函数或评价指标

待确认；指标：待从 PDF/全文确认

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：与外骨骼 AI 控制相关，但需要全文确认可接入性

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖复杂 EMG 阵列、代谢仪或动作捕捉，需降级为参考目标函数，不作为最小系统前提。

## 12. 证据来源

abstract only

## Abstract / Metadata Evidence

Lower exoskeleton has gained considerable interests in rehabilitation and health care applications,
since it has the potential to help the paraplegia patients to walk again. On the control of these
lower exoskeletons, the predefined gait control methods are commonly used, which requires the pilot
to adjust his/her movements to follow the predefined motion trajectories. In the meanwhile, the
desired trajectories are predefined from healthy persons or extrapolated from clinical gait analysis
(CGA) datasets. However, in individual walking assistance situations, the exoskeleton should have
the ability to adapt with variant motions of the pilot, since the pilot will change his motion in
different walking situations. This paper presents a novel step length adaptation method to adapt the
pilot's motion for walking assistance exoskeletons. In this paper, the exoskeleton robot is model as
a special Hybrid Human-Exoskeleton Agent (HHEA), which considers both the exoskeleton and the pilot.
The Dynamic Movement Primitives (DMP) is utilized to model the exoskeleton gait trajectories
dynamically, in which the relationship between the gait length and Center of Mass (CoM) of HHEA is
considered. In the training process, a Reinforcement Learning (RL) method is employed to update the
parameters of dynamic gait model online. We demonstrate the efficiency of the proposed step length
adaptation method in simulation environment as well as a lower limb exoskeleton system named as
AssItive DEvice for paRaplegics (AIDER). Experimental results shows that the proposed step length
adaptation method is able to adapt variant motions of the pilot during walking.
