# Soft Wearable Robots: Development Status and Technical Challenges

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Soft Wearable Robots: Development Status and Technical Challenges
- 作者：Yongjun Shi; Wei Dong; Weiqi Lin; Yongzhuo Gao
- 年份：2022
- 期刊/会议：Sensors
- DOI：10.3390/s22197584
- URL：https://doi.org/10.3390/s22197584
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, comfort score；指标：metabolic cost, EMG reduction/activity, comfort score

## 8. 实验对象和实验任务

12 individuals

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

In recent years, more and more research has begun to focus on the flexible and lightweight design of
wearable robots. During this process, many novel concepts and achievements have been continuously
made and shown to the public, while new problems have emerged at the same time, which need to be
solved. In this paper, we give an overview of the development status of soft wearable robots for
human movement assistance. On the basis of a clear definition, we perform a system classification
according to the target assisted joint and attempt to describe the overall prototype design level in
related fields. Additionally, it is necessary to sort out the latest research progress of key
technologies such as structure, actuation, control and evaluation, thereby analyzing the design
ideas and basic characteristics of them. Finally, we discuss the possible application fields, and
propose the main challenges of this valuable research direction.
