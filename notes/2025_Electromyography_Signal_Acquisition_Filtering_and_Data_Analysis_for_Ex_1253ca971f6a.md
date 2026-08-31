# Electromyography Signal Acquisition, Filtering, and Data Analysis for Exoskeleton Development

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Electromyography Signal Acquisition, Filtering, and Data Analysis for Exoskeleton Development
- 作者：Jung-Hoon Sul; Lasitha Piyathilaka; Diluka Moratuwage; Sanura Dunu Arachchige; Amal Jayawardena; Gayan Kahandawa; D.M.G. Preethichandra
- 年份：2025
- 期刊/会议：Sensors
- DOI：10.3390/s25134004
- URL：https://doi.org/10.3390/s25134004
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, DMP, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

EMG reduction/activity, comfort score；指标：EMG reduction/activity, comfort score

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Electromyography (EMG) has emerged as a vital tool in the development of wearable robotic
exoskeletons, enabling intuitive and responsive control by capturing neuromuscular signals. This
review presents a comprehensive analysis of the EMG signal processing pipeline tailored to
exoskeleton applications, spanning signal acquisition, noise mitigation, data preprocessing, feature
extraction, and control strategies. Various EMG acquisition methods, including surface,
intramuscular, and high-density surface EMG, are evaluated for their applicability in real-time
control. The review addresses prevalent signal quality challenges, such as motion artifacts, power-
line interference, and crosstalk. It also highlights both traditional filtering techniques and
advanced methods, such as wavelet transforms, empirical mode decomposition, and adaptive filtering.
Feature extraction techniques are explored to support pattern recognition and motion classification.
Machine learning approaches are examined for their roles in pattern recognition-based and hybrid
control architectures. This article emphasizes muscle synergy analysis and adaptive control
algorithms to enhance personalization and fatigue compensation, followed by the benefits of
multimodal sensing and edge computing in addressing the limitations of EMG-only systems. By focusing
on EMG-driven strategies through signal processing, machine learning, and sensor fusion innovations,
this review bridges gaps in human-machine interaction, offering insights into improving the
precision, adaptability, and robustness of next generation exoskeletons.
