# Optimized hip-knee-ankle exoskeleton assistance reduces the metabolic cost of walking with worn loads

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Optimized hip-knee-ankle exoskeleton assistance reduces the metabolic cost of walking with worn loads
- 作者：Gwendolyn M. Bryan; Patrick W. Franks; Seungmoon Song; Ricardo Reyes; Meghan P. O’Donovan; Karen N. Gregorczyk; Steven H. Collins
- 年份：2021
- 期刊/会议：Journal of NeuroEngineering and Rehabilitation
- DOI：10.1186/s12984-021-00955-8
- URL：https://doi.org/10.1186/s12984-021-00955-8
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, comfort score, stability；指标：metabolic cost, EMG reduction/activity, comfort score, stability

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：control/impedance parameters, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

BACKGROUND: Load carriage is common in a wide range of professions, but prolonged load carriage is
associated with increased fatigue and overuse injuries. Exoskeletons could improve the quality of
life of these professionals by reducing metabolic cost to combat fatigue and reducing muscle
activity to prevent injuries. Current exoskeletons have reduced the metabolic cost of loaded walking
by up to 22% relative to walking in the device with no assistance when assisting one or two joints.
Greater metabolic reductions may be possible with optimized assistance of the entire leg. METHODS:
We used human-in the-loop optimization to optimize hip-knee-ankle exoskeleton assistance with no
additional load, a light load (15% of body weight), and a heavy load (30% of body weight) for three
participants. All loads were applied through a weight vest with an attached waist belt. We measured
metabolic cost, exoskeleton assistance, kinematics, and muscle activity. We performed Friedman's
tests to analyze trends across worn loads and paired t-tests to determine whether changes from the
unassisted conditions to the assisted conditions were significant. RESULTS: Exoskeleton assistance
reduced the metabolic cost of walking relative to walking in the device without assistance for all
tested conditions. Exoskeleton assistance reduced the metabolic cost of walking by 48% with no load
(p = 0.05), 41% with the light load (p = 0.01), and 43% with the heavy load (p = 0.04). The smaller
metabolic reduction with the light load may be due to insufficient participant training or lack of
optimizer convergence. The total applied positive power was similar for all tested conditions, and
the positive knee power decreased slightly as load increased. Optimized torque timing parameters
were consistent across participants and load conditions while optimized magnitude parameters varied.
CONCLUSIONS: Whole-leg exoskeleton assistance can reduce the metabolic cost of walking while
carrying a range of loads. The consistent optimized timing parameters across participants and
conditions suggest that metabolic cost reductions are sensitive to torque timing. The variable
torque magnitude parameters could imply that torque magnitude should be customized to the
individual, or that there is a range of useful torque magnitudes. Future work should test whether
applying the load to the exoskeleton rather than the person's torso results in larger benefits.
