# Hand gestures classification of sEMG signals based on BiLSTM-metaheuristic optimization and hybrid U-Net-MobileNetV2 encoder architecture

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Hand gestures classification of sEMG signals based on BiLSTM-metaheuristic optimization and hybrid U-Net-MobileNetV2 encoder architecture
- 作者：Khosro Rezaee; Safoura Farsi Khavari; Mojtaba Ansari; Fatemeh Zare; Mohammad Hossein Alizadeh Roknabadi
- 年份：2024
- 期刊/会议：Scientific Reports
- DOI：10.1038/s41598-024-82676-1
- URL：https://doi.org/10.1038/s41598-024-82676-1
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer

## 5. 输入数据

IMU, 膝角度, EMG

## 6. 输出参数

助力时机/phase_offset, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity, safety constraint；指标：EMG reduction/activity, safety constraint

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：control/impedance parameters, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Surface electromyography (sEMG) data has been extensively utilized in deep learning algorithms for
hand movement classification. This paper aims to introduce a novel method for hand gesture
classification using sEMG data, addressing accuracy challenges seen in previous studies. We propose
a U-Net architecture incorporating a MobileNetV2 encoder, enhanced by a novel Bidirectional Long
Short-Term Memory (BiLSTM) and metaheuristic optimization for spatial feature extraction in hand
gesture and motion recognition. Bayesian optimization is employed as the metaheuristic approach to
optimize the BiLSTM model's architecture. To address the non-stationarity of sEMG signals, we employ
a windowing strategy for signal augmentation within deep learning architectures. The MobileNetV2
encoder and U-Net architecture extract relevant features from sEMG spectrogram images. Edge
computing integration is leveraged to further enhance innovation by enabling real-time processing
and decision-making closer to the data source. Six standard databases were utilized, achieving an
average accuracy of 90.23% with our proposed model, showcasing a 3-4% average accuracy improvement
and a 10% variance reduction. Notably, Mendeley Data, BioPatRec DB3, and BioPatRec DB1 surpassed
advanced models in their respective domains with classification accuracies of 88.71%, 90.2%, and
88.6%, respectively. Experimental results underscore the significant enhancement in generalizability
and gesture recognition robustness. This approach offers a fresh perspective on prosthetic
management and human-machine interaction, emphasizing its efficacy in improving accuracy and
reducing variance for enhanced prosthetic control and interaction with machines through edge
computing integration.
