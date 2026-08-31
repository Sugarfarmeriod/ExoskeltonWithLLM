# Selection of Muscle-Activity-Based Cost Function in Human-in-the-Loop Optimization of Multi-Gait Ankle Exoskeleton Assistance

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Selection of Muscle-Activity-Based Cost Function in Human-in-the-Loop Optimization of Multi-Gait Ankle Exoskeleton Assistance
- 作者：Hong Han; Wei Wang; Fengchao Zhang; Xin Li; Jianyu Chen; Jianda Han; Juanjuan Zhang
- 年份：2021
- 期刊/会议：IEEE Transactions on Neural Systems and Rehabilitation Engineering
- DOI：10.1109/tnsre.2021.3082198
- URL：https://doi.org/10.1109/tnsre.2021.3082198
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

PD/torque control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, comfort score；指标：metabolic cost, EMG reduction/activity, comfort score

## 8. 实验对象和实验任务

11 subjects

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Using "human-in-the-loop" (HIL) optimization can obtain suitable exoskeleton assistance patterns to
improve walking economy. However, there are differences in these patterns under different gait
conditions, and currently most HIL optimizations use metabolic cost, which requires long periods to
be estimated for each control law, as the physiological objective to minimize. We aimed to construct
a muscle-activity-based cost function and to find the appropriate initial assistance patterns in HIL
optimization of multi-gait ankle exoskeleton assistance. One healthy subject walked assisted by an
ankle exoskeleton under nine gait conditions and each condition was the combination of different
walking speeds, ground slopes and load weights. Ten assistance patterns were provided for the
subject under each gait condition. Then we constructed a cost function based on surface
electromyography signals of four lower leg muscles and select the muscle weight combination by using
particle swarm optimization algorithm to compose the cost function with maximum differences between
different assistance patterns. The mean weights of medial gastrocnemius, lateral gastrocnemius,
soleus and tibialis anterior activity under all gait conditions are 0.153, 0.104, 0.953 and 0.145,
respectively. Then we verified the effectiveness of this cost function by optimization and
validation experiments conducted on four subjects. Our results are expected to guide the selection
of muscle-activity-based cost functions and improve the time efficiency of HIL optimization.
