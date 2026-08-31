# Dynamic Movement Primitives Based Robot Skills Learning

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Dynamic Movement Primitives Based Robot Skills Learning
- 作者：Linghuan Kong; Wei He; Wenshi Chen; Hui Zhang; Yaonan Wang
- 年份：2023
- 期刊/会议：Machine Intelligence Research
- DOI：10.1007/s11633-022-1346-z
- URL：https://doi.org/10.1007/s11633-022-1346-z
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

足底压力/力传感, 膝速度

## 6. 输出参数

助力时机/phase_offset, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

stability；指标：stability

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset

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
- 输出类型：trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Abstract In this article, a robot skills learning framework is developed, which considers both
motion modeling and execution. In order to enable the robot to learn skills from demonstrations, a
learning method called dynamic movement primitives (DMPs) is introduced to model motion. A staged
teaching strategy is integrated into DMPs frameworks to enhance the generality such that the
complicated tasks can be also performed for multi-joint manipulators. The DMP connection method is
used to make an accurate and smooth transition in position and velocity space to connect complex
motion sequences. In addition, motions are categorized into different goals and durations. It is
worth mentioning that an adaptive neural networks (NNs) control method is proposed to achieve highly
accurate trajectory tracking and to ensure the performance of action execution, which is beneficial
to the improvement of reliability of the skills learning system. The experiment test on the Baxter
robot verifies the effectiveness of the proposed method.
