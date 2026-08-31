# Dynamic movement primitives in robotics: A tutorial survey

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Dynamic movement primitives in robotics: A tutorial survey
- 作者：Matteo Saveriano; Fares J. Abu‐Dakka; Aljaž Kramberger; Luka Peternel
- 年份：2023
- 期刊/会议：The International Journal of Robotics Research
- DOI：10.1177/02783649231201196
- URL：https://doi.org/10.1177/02783649231201196
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP, high-level interface

## 5. 输入数据

膝速度, 膝力矩/交互力矩, 治疗师/语义输入

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

待确认；指标：待从 PDF/全文确认

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

Biological systems, including human beings, have the innate ability to perform complex tasks in a
versatile and agile manner. Researchers in sensorimotor control have aimed to comprehend and
formally define this innate characteristic. The idea, supported by several experimental findings,
that biological systems are able to combine and adapt basic units of motion into complex tasks
finally leads to the formulation of the motor primitives’ theory. In this respect, Dynamic Movement
Primitives (DMPs) represent an elegant mathematical formulation of the motor primitives as stable
dynamical systems and are well suited to generate motor commands for artificial systems like robots.
In the last decades, DMPs have inspired researchers in different robotic fields including imitation
and reinforcement learning, optimal control, physical interaction, and human–robot co-working,
resulting in a considerable amount of published papers. The goal of this tutorial survey is two-
fold. On one side, we present the existing DMP formulations in rigorous mathematical terms and
discuss the advantages and limitations of each approach as well as practical implementation details.
In the tutorial vein, we also search for existing implementations of presented approaches and
release several others. On the other side, we provide a systematic and comprehensive review of
existing literature and categorize state-of-the-art work on DMP. The paper concludes with a
discussion on the limitations of DMPs and an outline of possible research directions.
