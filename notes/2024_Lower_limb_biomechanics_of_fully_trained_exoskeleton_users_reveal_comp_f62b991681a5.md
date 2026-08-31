# Lower limb biomechanics of fully trained exoskeleton users reveal complex mechanisms behind the reductions in energy cost with human-in-the-loop optimization

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Lower limb biomechanics of fully trained exoskeleton users reveal complex mechanisms behind the reductions in energy cost with human-in-the-loop optimization
- 作者：Katherine L. Poggensee; Steven H. Collins
- 年份：2024
- 期刊/会议：Frontiers in Robotics and AI
- DOI：10.3389/frobt.2024.1283080
- URL：https://doi.org/10.3389/frobt.2024.1283080
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost；指标：metabolic cost

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Exoskeletons that assist in ankle plantarflexion can improve energy economy in locomotion.
Characterizing the joint-level mechanisms behind these reductions in energy cost can lead to a
better understanding of how people interact with these devices, as well as to improved device design
and training protocols. We examined the biomechanical responses to exoskeleton assistance in
exoskeleton users trained with a lengthened protocol. Kinematics at unassisted joints were generally
unchanged by assistance, which has been observed in other ankle exoskeleton studies. Peak
plantarflexion angle increased with plantarflexion assistance, which led to increased total and
biological mechanical power despite decreases in biological joint torque and whole-body net
metabolic energy cost. Ankle plantarflexor activity also decreased with assistance. Muscles that act
about unassisted joints also increased activity for large levels of assistance, and this response
should be investigated over long-term use to prevent overuse injuries.
