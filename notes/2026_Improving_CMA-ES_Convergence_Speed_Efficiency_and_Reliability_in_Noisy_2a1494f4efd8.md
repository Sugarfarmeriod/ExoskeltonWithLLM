# Improving CMA-ES Convergence Speed, Efficiency, and Reliability in Noisy Robot Optimization Problems

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Improving CMA-ES Convergence Speed, Efficiency, and Reliability in Noisy Robot Optimization Problems
- 作者：Russell Martin; Steven H. Collins
- 年份：2026
- 期刊/会议：ArXiv.org
- DOI：未提供
- URL：https://openalex.org/W7124358511
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

IMU, 膝力矩/交互力矩

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, tau/持续时间

## 7. 目标函数或评价指标

待确认；指标：待从 PDF/全文确认

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：control/impedance parameters, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Experimental robot optimization often requires evaluating each candidate policy for seconds to
minutes. The chosen evaluation time influences optimization because of a speed-accuracy tradeoff:
shorter evaluations enable faster iteration, but are also more subject to noise. Here, we introduce
a supplement to the CMA-ES optimization algorithm, named Adaptive Sampling CMA-ES (AS-CMA), which
assigns sampling time to candidates based on predicted sorting difficulty, aiming to achieve
consistent precision. We compared AS-CMA to CMA-ES and Bayesian optimization using a range of static
sampling times in four simulated cost landscapes. AS-CMA converged on 98% of all runs without
adjustment to its tunable parameter, and converged 24-65% faster and with 29-76% lower total cost
than each landscape's best CMA-ES static sampling time. As compared to Bayesian optimization, AS-CMA
converged more efficiently and reliably in complex landscapes, while in simpler landscapes, AS-CMA
was less efficient but equally reliable. We deployed AS-CMA in an exoskeleton optimization
experiment and found the optimizer's behavior was consistent with expectations. These results
indicate that AS-CMA can improve optimization efficiency in the presence of noise while minimally
affecting optimization setup complexity and tuning requirements.
