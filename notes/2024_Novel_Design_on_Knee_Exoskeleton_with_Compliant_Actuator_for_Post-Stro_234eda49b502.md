# Novel Design on Knee Exoskeleton with Compliant Actuator for Post-Stroke Rehabilitation

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Novel Design on Knee Exoskeleton with Compliant Actuator for Post-Stroke Rehabilitation
- 作者：Lin Wu; Chao Wang; Jiawei Liu; Benjian Zou; Samit Chakrabarty; Tianzhe Bao; Sheng Quan Xie
- 年份：2024
- 期刊/会议：Sensors
- DOI：10.3390/s25010153
- URL：https://doi.org/10.3390/s25010153
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, PD/torque control, low-frequency optimizer

## 5. 输入数据

足底压力/力传感, 膝角度, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

EMG reduction/activity, comfort score, stability；指标：EMG reduction/activity, comfort score, stability

## 8. 实验对象和实验任务

stroke participants/patients（数量待查 PDF）

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖复杂 EMG 阵列、代谢仪或动作捕捉，需降级为参考目标函数，不作为最小系统前提。

## 12. 证据来源

PDF

## Abstract / Metadata Evidence

Knee joint disorders pose a significant and growing challenge to global healthcare systems. Recent
advancements in robotics, sensing technologies, and artificial intelligence have driven the
development of robot-assisted therapies, reducing the physical burden on therapists and improving
rehabilitation outcomes. This study presents a novel knee exoskeleton designed for safe and adaptive
rehabilitation, specifically targeting bed-bound stroke patients to enable early intervention. The
exoskeleton comprises a leg splint, thigh splint, and an actuator, incorporating a series elastic
actuator (SEA) to enhance torque density and provide intrinsic compliance. A variable impedance
control method was also implemented to achieve accurate position tracking of the exoskeleton, and
performance tests were conducted with and without human participants. A preliminary clinical study
involving two stroke patients demonstrated the exoskeleton's potential in reducing muscle
spasticity, particularly at faster movement velocities. The key contributions of this study include
the design of a compact SEA with improved torque density, the development of a knee exoskeleton
equipped with a cascaded position controller, and a clinical test validating its effectiveness in
alleviating spasticity in stroke patients. This study represents a significant step forward in the
application of SEA for robot-assisted rehabilitation, offering a promising approach to the treatment
of knee joint disorders.
