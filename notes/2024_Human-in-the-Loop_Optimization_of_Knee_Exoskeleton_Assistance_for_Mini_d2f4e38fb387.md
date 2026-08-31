# Human-in-the-Loop Optimization of Knee Exoskeleton Assistance for Minimizing User’s Metabolic and Muscular Effort

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Human-in-the-Loop Optimization of Knee Exoskeleton Assistance for Minimizing User’s Metabolic and Muscular Effort
- 作者：Sara Monteiro; Joana Figueiredo; Pedro Fonseca; João Paulo Vilas‐Boas; Cristina P. Santos
- 年份：2024
- 期刊/会议：Sensors
- DOI：10.3390/s24113305
- URL：https://doi.org/10.3390/s24113305
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

PD/torque control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, interaction torque/force, comfort score, stability；指标：metabolic cost, EMG reduction/activity, interaction torque/force, comfort score, stability

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

abstract only

## 13. 语义/治疗师输入扩展记录

- 输入类型：not semantic / not reported
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Lower limb exoskeletons have the potential to mitigate work-related musculoskeletal disorders;
however, they often lack user-oriented control strategies. Human-in-the-loop (HITL) controls adapt
an exoskeleton’s assistance in real time, to optimize the user–exoskeleton interaction. This study
presents a HITL control for a knee exoskeleton using a CMA-ES algorithm to minimize the users’
physical effort, a parameter innovatively evaluated using the interaction torque with the
exoskeleton (a muscular effort indicator) and metabolic cost. This work innovates by estimating the
user’s metabolic cost within the HITL control through a machine-learning model. The regression model
estimated the metabolic cost, in real time, with a root mean squared error of 0.66 W/kg and mean
absolute percentage error of 26% (n = 5), making faster (10 s) and less noisy estimations than a
respirometer (K5, Cosmed). The HITL reduced the user’s metabolic cost by 7.3% and 5.9% compared to
the zero-torque and no-device conditions, respectively, and reduced the interaction torque by 32.3%
compared to a zero-torque control (n = 1). The developed HITL control surpassed a non-exoskeleton
and zero-torque condition regarding the user’s physical effort, even for a task such as slow
walking. Furthermore, the user-specific control had a lower metabolic cost than the non-user-
specific assistance. This proof-of-concept demonstrated the potential of HITL controls in assisted
walking.
