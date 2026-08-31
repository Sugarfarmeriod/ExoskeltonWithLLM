# Human-in-the-loop Optimisation in Robot-assisted Gait Training

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Human-in-the-loop Optimisation in Robot-assisted Gait Training
- 作者：Andreas Christou; Andreas Sochopoulos; Elliot Lister; Sethu Vijayakumar
- 年份：2025
- 期刊/会议：ArXiv.org
- DOI：10.48550/arxiv.2510.05780
- URL：https://doi.org/10.48550/arxiv.2510.05780
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer, high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩, 治疗师/语义输入

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, comfort score；指标：metabolic cost, comfort score

## 8. 实验对象和实验任务

healthy participants（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

Wearable robots offer a promising solution for quantitatively monitoring gait and providing
systematic, adaptive assistance to promote patient independence and improve gait. However, due to
significant interpersonal and intrapersonal variability in walking patterns, it is important to
design robot controllers that can adapt to the unique characteristics of each individual. This paper
investigates the potential of human-in-the-loop optimisation (HILO) to deliver personalised
assistance in gait training. The Covariance Matrix Adaptation Evolution Strategy (CMA-ES) was
employed to continuously optimise an assist-as-needed controller of a lower-limb exoskeleton. Six
healthy individuals participated over a two-day experiment. Our results suggest that while the CMA-
ES appears to converge to a unique set of stiffnesses for each individual, no measurable impact on
the subjects' performance was observed during the validation trials. These findings highlight the
impact of human-robot co-adaptation and human behaviour variability, whose effect may be greater
than potential benefits of personalising rule-based assistive controllers. Our work contributes to
understanding the limitations of current personalisation approaches in exoskeleton-assisted gait
rehabilitation and identifies key challenges for effective implementation of human-in-the-loop
optimisation in this domain.
