# Hierarchical Interactive Learning for a HUman-Powered Augmentation Lower EXoskeleton

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Hierarchical Interactive Learning for a HUman-Powered Augmentation Lower EXoskeleton
- 作者：Rui Huang; Hong Cheng; Hongliang Guo; Qiming Chen; Xichuan Lin
- 年份：2016
- 期刊/会议：未提供
- DOI：10.1109/icra.2016.7487142
- URL：https://doi.org/10.1109/icra.2016.7487142
- PDF 状态：abstract_only

## 2. 一句话结论

与外骨骼 AI 控制相关，但需要全文确认可接入性

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

DMP

## 5. 输入数据

待确认

## 6. 输出参数

待确认

## 7. 目标函数或评价指标

interaction torque/force；指标：interaction torque/force

## 8. 实验对象和实验任务

未从摘要确认

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

Learning by demonstration methods have gained considerable interest in human-coupled robot control.
It aims at modeling the goal motion trajectories through human demonstration. However, in lower
exoskeleton control, the physical human-robot interaction is changing from pilot to pilot or even
for one pilot in different walking patterns. This characteristic requires that the exoskeletons
should have the ability to learn and adapt the motion trajectories as well as controllers online.
This paper presents a novel Hierarchical Interactive Learning (HIL) strategy which reduces the
complexity of the exoskeleton sensory system and is able to handle varying interaction dynamics. The
proposed HIL strategy is composed of two learning hierarchies, namely, high-level motion learning
and low-level controller learning. The Dynamic Movement Primitives (DMPs) combined with Locally
Weighted Regression (LWR) are employed to model and learn the motion trajectories, while
reinforcement learning (RL) is used to learn the model-based controller. We demonstrate the
efficiency of proposed HIL strategy on a single degree-of-freedom (DOF) platform as well as a HUman-
powered Augmentation Lower EXoskeleton (HUALEX) system. Experimental results indicate that the
proposed HIL strategy is able to handle the varying interaction dynamics with less interaction force
between the pilot and the exoskeleton when compared to traditional model-based control algorithms.
