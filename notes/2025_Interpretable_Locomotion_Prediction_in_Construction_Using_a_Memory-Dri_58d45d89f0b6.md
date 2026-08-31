# Interpretable Locomotion Prediction in Construction Using a Memory-Driven LLM Agent With Chain-of-Thought Reasoning

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Interpretable Locomotion Prediction in Construction Using a Memory-Driven LLM Agent With Chain-of-Thought Reasoning
- 作者：Ehsan Ahmadi; Chao Wang
- 年份：2025
- 期刊/会议：arXiv
- DOI：10.48550/arXiv.2504.15263
- URL：https://arxiv.org/abs/2504.15263
- PDF 状态：manual_pdf

## 2. 一句话结论

可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

状态估计器

## 4. 控制底座

high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 膝力矩/交互力矩, EMG, 治疗师/语义输入

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity, comfort score, safety constraint；指标：EMG reduction/activity, comfort score, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：simulation only
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, SafeTorque / safety constraints
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：future extension

## Abstract / Metadata Evidence

Construction tasks are unpredictable and safety-critical. This paper presents a locomotion
prediction agent for exoskeleton assistance that combines spoken commands and visual data from smart
glasses with short-term memory, long-term memory, and a refinement module. The agent predicts
locomotion modes and improves weighted F1 from 0.73 without memory to 0.90 with both memory
components; calibration also improves using Brier score and expected calibration error.
