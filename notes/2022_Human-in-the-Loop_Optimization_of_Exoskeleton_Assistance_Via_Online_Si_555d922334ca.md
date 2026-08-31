# Human-in-the-Loop Optimization of Exoskeleton Assistance Via Online Simulation of Metabolic Cost

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Human-in-the-Loop Optimization of Exoskeleton Assistance Via Online Simulation of Metabolic Cost
- 作者：Daniel Gordon; Christopher McGreavy; Andreas Christou; Sethu Vijayakumar
- 年份：2022
- 期刊/会议：IEEE Transactions on Robotics
- DOI：10.1109/tro.2021.3133137
- URL：https://doi.org/10.1109/tro.2021.3133137
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, comfort score；指标：metabolic cost, EMG reduction/activity, comfort score

## 8. 实验对象和实验任务

未从摘要确认

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Many assistive robotic devices have been developed to augment or assist human locomotion. Despite
advancements in design and control algorithms, this task remains challenging. Human walking
strategies are unique and complex, and assistance strategies based on the dynamics of unassisted
locomotion typically offer only modest reductions to the metabolic cost of walking. Recently, human-
in-the-loop (HIL) methodologies have been used to identify subject-specific assistive strategies,
which offer significant improvements to energy savings. However, current implementations suffer from
long measurement times, necessitating the use of low-dimensional control parameterizations, and
possibly requiring multiday collection protocols to avoid subject fatigue. We present a HIL
methodology, which optimizes the assistive torques provided by a powered hip exoskeleton. Using
musculoskeletal modeling, we are able to evaluate simulated metabolic rate online. We applied our
methodology to identify assistive torque profiles for seven subjects walking on a treadmill, and
found greater reductions to metabolic cost when compared to generic or off-the-shelf controllers. In
a secondary investigation, we directly compare simulated and measured metabolic rate for three
subjects experiencing a range of assistance levels. The time investment required to identify
assistance strategies via our protocol is significantly lower when compared to existing protocols
relying on calorimetry. In the future, frameworks such as these could be used to enable shorter HIL
protocols or exploit more complex control parameterizations for greater energy savings.
