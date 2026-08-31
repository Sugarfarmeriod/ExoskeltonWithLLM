# Reducing Squat Physical Effort Using Personalized Assistance From an Ankle Exoskeleton

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Reducing Squat Physical Effort Using Personalized Assistance From an Ankle Exoskeleton
- 作者：Prakyath Kantharaju; Hyeongkeun Jeong; Sruthi Ramadurai; Michael S. Jacobson; Heejin Jeong; Myunghee Kim
- 年份：2022
- 期刊/会议：IEEE Transactions on Neural Systems and Rehabilitation Engineering
- DOI：10.1109/tnsre.2022.3186692
- URL：https://doi.org/10.1109/tnsre.2022.3186692
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer, high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, gait symmetry, safety constraint；指标：metabolic cost, gait symmetry, safety constraint

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：natural language / LLM
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, SafeTorque / safety constraints
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

Exoskeletons can assist humans during squatting and the assistance has the potential to reduce the
physical demands. Although several squat assistance methods are available, the effect of
personalized assistance on physical effort has not been examined. We hypothesize that personalized
assistance will reduce the physical effort of squatting. We developed a human-in-the-loop Bayesian
optimization scheme to minimize the metabolic cost of squatting using a unilateral ankle
exoskeleton. The optimization identified subject-specific assistance parameters for ascending and
descending during squatting and took 15.8 min on average to converge. The subject-specific optimized
condition reduced metabolic cost by 19.9% and rectus femoris muscle activity by 28.7% compared to
the condition without the exoskeleton with a higher probability of improvement compared to a generic
condition. In an additional study with two participants, the personalized condition presented higher
metabolic cost reduction than the generic condition. These reductions illustrate the importance of
personalized ankle assistance using an exoskeleton for squatting, a physically intensive activity,
and suggest that such a method can be applied to minimize the physical effort of squatting. Future
work can investigate the effect of personalized squat assistance on fatigue and the potential risk
of injury.
