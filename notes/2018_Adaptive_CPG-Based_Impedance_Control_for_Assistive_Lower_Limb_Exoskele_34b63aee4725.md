# Adaptive CPG-Based Impedance Control for Assistive Lower Limb Exoskeleton

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Adaptive CPG-Based Impedance Control for Assistive Lower Limb Exoskeleton
- 作者：Ruiming Luo; Shouqian Sun; Xiangyu Zhao; Yuxuan Zhang; Yongchuan Tang
- 年份：2018
- 期刊/会议：2018 IEEE International Conference on Robotics and Biomimetics (ROBIO)
- DOI：10.1109/robio.2018.8664912
- URL：https://doi.org/10.1109/robio.2018.8664912
- PDF 状态：manual_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd

## 3. AI 插入位置

参数优化器

## 4. 控制底座

impedance control, low-frequency optimizer

## 5. 输入数据

足底压力/力传感

## 6. 输出参数

MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

待确认；指标：待从 PDF/全文确认

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 MO_Kp/MO_Kd

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

PDF

## 13. 语义/治疗师输入扩展记录

- 输入类型：not semantic / not reported
- 输出类型：not reported
- 是否真实机器人闭环：not confirmed
- 与本项目参数映射：MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

未提供。
