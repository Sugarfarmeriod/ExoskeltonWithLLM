# The characteristics of human-robot coadaptation during human-in-the-loop optimization of exoskeleton control

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：The characteristics of human-robot coadaptation during human-in-the-loop optimization of exoskeleton control
- 作者：Wei Wang; Yige Liu; Pengqing Ren; Juanjuan Zhang; Jingtai Liu
- 年份：2018
- 期刊/会议：2018 IEEE International Conference on Robotics and Biomimetics (ROBIO)
- DOI：10.1109/robio.2018.8665057
- URL：https://doi.org/10.1109/robio.2018.8665057
- PDF 状态：metadata_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

待确认

## 6. 输出参数

待确认

## 7. 目标函数或评价指标

待确认；指标：待从 PDF/全文确认

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖复杂 EMG 阵列、代谢仪或动作捕捉，需降级为参考目标函数，不作为最小系统前提。

## 12. 证据来源

metadata only

## Abstract / Metadata Evidence

未提供。
