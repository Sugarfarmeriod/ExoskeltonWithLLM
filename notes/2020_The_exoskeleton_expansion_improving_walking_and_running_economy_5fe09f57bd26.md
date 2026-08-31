# The exoskeleton expansion: improving walking and running economy

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：The exoskeleton expansion: improving walking and running economy
- 作者：Gregory S. Sawicki; Owen N. Beck; Inseung Kang; Aaron J. Young
- 年份：2020
- 期刊/会议：Journal of NeuroEngineering and Rehabilitation
- DOI：10.1186/s12984-020-00663-9
- URL：https://doi.org/10.1186/s12984-020-00663-9
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer

## 5. 输入数据

足底压力/力传感, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost；指标：metabolic cost

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Since the early 2000s, researchers have been trying to develop lower-limb exoskeletons that augment
human mobility by reducing the metabolic cost of walking and running versus without a device. In
2013, researchers finally broke this 'metabolic cost barrier'. We analyzed the literature through
December 2019, and identified 23 studies that demonstrate exoskeleton designs that improved human
walking and running economy beyond capable without a device. Here, we reviewed these studies and
highlighted key innovations and techniques that enabled these devices to surpass the metabolic cost
barrier and steadily improve user walking and running economy from 2013 to nearly 2020. These
studies include, physiologically-informed targeting of lower-limb joints; use of off-board actuators
to rapidly prototype exoskeleton controllers; mechatronic designs of both active and passive
systems; and a renewed focus on human-exoskeleton interface design. Lastly, we highlight emerging
trends that we anticipate will further augment wearable-device performance and pose the next grand
challenges facing exoskeleton technology for augmenting human mobility.
