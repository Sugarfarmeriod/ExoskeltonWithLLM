# Review on Control Strategies for Lower Limb Rehabilitation Exoskeletons

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Review on Control Strategies for Lower Limb Rehabilitation Exoskeletons
- 作者：Wenzhou Li; Guang‐Zhong Cao; Aibin Zhu
- 年份：2021
- 期刊/会议：IEEE Access
- DOI：10.1109/access.2021.3110595
- URL：https://doi.org/10.1109/access.2021.3110595
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer, high-level interface

## 5. 输入数据

膝角度, 膝速度, 膝力矩/交互力矩, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

interaction torque/force, comfort score, stability, safety constraint；指标：interaction torque/force, comfort score, stability, safety constraint

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：therapist instruction / clinical goal
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：not confirmed
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：future extension

## Abstract / Metadata Evidence

Research on lower limb exoskeleton (LLE) for rehabilitation have developed rapidly to meet the need
of the population with neurologic injuries. LLEs for rehabilitation include therapeutic LLEs that
aim to restore walking ability for patients, and assistive LLEs that offer support on activities in
daily life. A substantial part of them can serve both purposes. However, these devices are yet to
reach the final goal of performing human-machine joint movement agilely and smartly. Control
strategy plays an important role in achieving their designed goal. At present, control strategies
face three major challenges: how to detect human intention, how to do motion control with given
intentions, and how to optimize control parameters to suit different individuals. As a contribution,
this paper offers an overview on the state-of-the-art control strategies for rehabilitation LLEs by
classifying them into eight categories, each of which is presented with a technical summary and
tabulated information of representative papers. Moreover, current approaches addressing the three
challenges are discussed in a macroscopic perspective. Finally, it has been explored which
requirements the future control strategies should meet for maximizing the performance of
rehabilitation LLEs.
