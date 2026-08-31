# Human-in-the-loop optimization of wearable device parameters using an EMG-based objective function

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Human-in-the-loop optimization of wearable device parameters using an EMG-based objective function
- 作者：María Alejandra Díaz; Sander De Bock; Philipp Beckerle; Jan Babič; Tom Verstraten; Kevin De Pauw
- 年份：2024
- 期刊/会议：Wearable Technologies
- DOI：10.1017/wtc.2024.9
- URL：https://doi.org/10.1017/wtc.2024.9
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, comfort score；指标：metabolic cost, EMG reduction/activity, comfort score

## 8. 实验对象和实验任务

19 participants

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, tau
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Advancements in wearable robots aim to improve user motion, motor control, and overall experience by
minimizing energetic cost (EC). However, EC is challenging to measure and it is typically indirectly
estimated through respiratory gas analysis. This study introduces a novel EMG-based objective
function that captures individuals' natural energetic expenditure during walking. The objective
function combines information from electromyography (EMG) variables such as intensity and muscle
synergies. First, we demonstrate the similarity of the proposed objective function, calculated
offline, to the EC during walking. Second, we minimize and validate the EMG-based objective function
using an online Bayesian optimization algorithm. The walking step frequency is chosen as the
parameter to optimize in both offline and online approaches in order to simplify experiments and
facilitate comparisons with related research. Compared to existing studies that use EC as the
objective function, results demonstrated that the optimization of the presented objective function
reduced the number of iterations and, when compared with gradient descent optimization strategies,
also reduced convergence time. Moreover, the algorithm effectively converges toward an optimal step
frequency near the user's preferred frequency, positively influencing EC reduction. The good
correlation between the estimated objective function and measured EC highlights its consistency and
reliability. Thus, the proposed objective function could potentially optimize lower limb exoskeleton
assistance and improve user performance and human-robot interaction without the need for challenging
respiratory gas measurements.
