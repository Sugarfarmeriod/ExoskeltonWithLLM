# The Effects of Incline Level on Optimized Lower-Limb Exoskeleton Assistance

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：The Effects of Incline Level on Optimized Lower-Limb Exoskeleton Assistance
- 作者：Patrick W. Franks; Gwendolyn M. Bryan; Ricardo Reyes; Meghan P. O’Donovan; Karen N. Gregorczyk; Steven H. Collins
- 年份：2021
- 期刊/会议：未提供
- DOI：10.1101/2021.09.13.460170
- URL：https://doi.org/10.1101/2021.09.13.460170
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer, high-level interface

## 5. 输入数据

足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, comfort score；指标：metabolic cost, comfort score

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

abstract only

## 13. 语义/治疗师输入扩展记录

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

Abstract For exoskeletons to be successful in real-world settings, they will need to be effective
across a variety of terrains, including on inclines. While some single-joint exoskeletons have
assisted incline walking, recent successes in level-ground assistance suggest that greater
improvements may be possible by optimizing assistance of the whole leg. To understand how
exoskeleton assistance should change with incline, we used human-in-the-loop optimization to find
whole-leg exoskeleton assistance torques that minimized metabolic cost on a range of grades. We
optimized assistance for three expert, able-bodied participants on 5 degree, 10 degree and 15 degree
inclines using a hip-knee-ankle exoskeleton emulator. For all assisted conditions, the cost of
transport was reduced by at least 50% relative to walking in the device with no assistance, a large
improvement to walking that is comparable to the benefits of whole-leg assistance on level-ground.
This corresponds to large absolute reductions in metabolic cost, with the most strenuous conditions
reduced by 4.9 W/kg, more than twice the entire energy cost of level walking. Optimized extension
torque magnitudes and exoskeleton power increased with incline, with hip extension, knee extension
and ankle plantarflexion often growing as large as allowed by comfort-based limits. Applied powers
on steep inclines were double the powers applied during level-ground walking, indicating that larger
exoskeleton power may be optimal in scenarios where biological powers and costs are higher. Future
exoskeleton devices can be expected to deliver large improvements in walking performance across a
range of inclines, if they have sufficient torque and power capabilities.
