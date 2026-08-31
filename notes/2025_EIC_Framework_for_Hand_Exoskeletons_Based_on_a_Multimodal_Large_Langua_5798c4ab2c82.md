# EIC Framework for Hand Exoskeletons Based on a Multimodal Large Language Model

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：EIC Framework for Hand Exoskeletons Based on a Multimodal Large Language Model
- 作者：Houcheng Li; Zhenchan Su; Honglei Guo; Yifan Wang; Zeyu Liu; Long Cheng
- 年份：2025
- 期刊/会议：2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- DOI：10.1109/IROS60139.2025.11246670
- URL：https://doi.org/10.1109/iros60139.2025.11246670
- PDF 状态：manual_pdf

## 2. 一句话结论

可增强 AO/Phi/Phase0Event 或足底负重/意图估计；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

状态估计器

## 4. 控制底座

high-level interface

## 5. 输入数据

足底压力/力传感, 膝角度, 膝力矩/交互力矩, EMG, 治疗师/语义输入

## 6. 输出参数

待确认

## 7. 目标函数或评价指标

EMG reduction/activity, comfort score；指标：EMG reduction/activity, comfort score

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可增强 AO/Phi/Phase0Event 或足底负重/意图估计；语义/治疗师输入可作为高层参数或模式选择接口，但优先级低于优化器和状态估计器；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque
- 实现难度：medium
- 是否适合 1-2 个月快速成稿：secondary angle only

## Abstract / Metadata Evidence

Current hand exoskeleton interaction methods primarily focus on recognizing a limited range of hand
motion intentions and rely on pre-programmed control for predefined commands. This paper proposes an
embodied interaction control framework based on a multimodal large language model. Speech and image
information are fused to infer hand motion intentions and generate motion plans for the exoskeleton,
which are executed by an underlying control strategy. Experiments validate the effectiveness and
generalizability of the framework.
