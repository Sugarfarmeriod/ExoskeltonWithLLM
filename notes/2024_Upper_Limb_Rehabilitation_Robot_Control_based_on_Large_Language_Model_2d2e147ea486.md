# Upper Limb Rehabilitation Robot Control based on Large Language Model

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Upper Limb Rehabilitation Robot Control based on Large Language Model
- 作者：Yanayir Rifai; Ahmad Ataka; Agus Bejo; Yusuf Kurnia Badriawan
- 年份：2024
- 期刊/会议：2024 International Conference on Computer, Control, Informatics and its Applications (IC3INA)
- DOI：10.1109/IC3INA64086.2024.10732179
- URL：https://doi.org/10.1109/ic3ina64086.2024.10732179
- PDF 状态：manual_pdf

## 2. 一句话结论

语义方向缺少到控制参数的直接映射，只适合相关工作/未来展望；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

高层语义/治疗师输入接口

## 4. 控制底座

high-level interface

## 5. 输入数据

IMU, 足底压力/力传感, 膝角度, 治疗师/语义输入

## 6. 输出参数

待确认

## 7. 目标函数或评价指标

comfort score；指标：comfort score

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：语义方向缺少到控制参数的直接映射，只适合相关工作/未来展望；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 与本项目参数映射：no direct mapping confirmed
- 实现难度：high
- 是否适合 1-2 个月快速成稿：not suitable for 1-2 month main paper

## Abstract / Metadata Evidence

This study explores a large language model as a control interface for an upper-limb rehabilitation
robot. High-level task execution based on an LLM is combined with low-level forward kinematics so
users can issue intuitive commands for reaching, circular, and swinging rehabilitation movements.
The reported experiments compare LLM-based and keypad-based controls using task success and
usability measures.
