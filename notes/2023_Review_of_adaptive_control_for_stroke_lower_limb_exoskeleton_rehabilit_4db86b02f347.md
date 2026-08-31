# Review of adaptive control for stroke lower limb exoskeleton rehabilitation robot based on motion intention recognition

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Review of adaptive control for stroke lower limb exoskeleton rehabilitation robot based on motion intention recognition
- 作者：Dongnan Su; Zhigang Hu; Jipeng Wu; Peng Shang; Zhaohui Luo
- 年份：2023
- 期刊/会议：Frontiers in Neurorobotics
- DOI：10.3389/fnbot.2023.1186175
- URL：https://doi.org/10.3389/fnbot.2023.1186175
- PDF 状态：open_access_pdf

## 2. 一句话结论

可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

状态估计器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

IMU, 足底压力/力传感

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

待确认；指标：待从 PDF/全文确认

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可增强 AO/Phi/Phase0Event 或足底负重/意图估计；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 是否真实机器人闭环：not confirmed
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Stroke is a significant cause of disability worldwide, and stroke survivors often experience severe
motor impairments. Lower limb rehabilitation exoskeleton robots provide support and balance for
stroke survivors and assist them in performing rehabilitation training tasks, which can effectively
improve their quality of life during the later stages of stroke recovery. Lower limb rehabilitation
exoskeleton robots have become a hot topic in rehabilitation therapy research. This review
introduces traditional rehabilitation assessment methods, explores the possibility of lower limb
exoskeleton robots combining sensors and electrophysiological signals to assess stroke survivors'
rehabilitation objectively, summarizes standard human-robot coupling models of lower limb
rehabilitation exoskeleton robots in recent years, and critically introduces adaptive control models
based on motion intent recognition for lower limb exoskeleton robots. This provides new design ideas
for the future combination of lower limb rehabilitation exoskeleton robots with rehabilitation
assessment, motion assistance, rehabilitation treatment, and adaptive control, making the
rehabilitation assessment process more objective and addressing the shortage of rehabilitation
therapists to some extent. Finally, the article discusses the current limitations of adaptive
control of lower limb rehabilitation exoskeleton robots for stroke survivors and proposes new
research directions.
