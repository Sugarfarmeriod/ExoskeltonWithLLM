# Human-in-the-loop optimization of hip assistance with a soft exosuit during walking

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Human-in-the-loop optimization of hip assistance with a soft exosuit during walking
- 作者：Ye Ding; Myunghee Kim; Scott Kuindersma; Conor J. Walsh
- 年份：2018
- 期刊/会议：Science Robotics
- DOI：10.1126/scirobotics.aar5438
- URL：https://doi.org/10.1126/scirobotics.aar5438
- PDF 状态：abstract_only

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset

## 3. AI 插入位置

参数优化器

## 4. 控制底座

low-frequency optimizer

## 5. 输入数据

待确认

## 6. 输出参数

助力时机/phase_offset

## 7. 目标函数或评价指标

metabolic cost；指标：metabolic cost

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖复杂 EMG 阵列、代谢仪或动作捕捉，需降级为参考目标函数，不作为最小系统前提。

## 12. 证据来源

abstract only

## Abstract / Metadata Evidence

Wearable robotic devices have been shown to substantially reduce the energy expenditure of human
walking. However, response variance between participants for fixed control strategies can be high,
leading to the hypothesis that individualized controllers could further improve walking economy.
Recent studies on human-in-the-loop (HIL) control optimization have elucidated several practical
challenges, such as long experimental protocols and low signal-to-noise ratios. Here, we used
Bayesian optimization-an algorithm well suited to optimizing noisy performance signals with very
limited data-to identify the peak and offset timing of hip extension assistance that minimizes the
energy expenditure of walking with a textile-based wearable device. Optimal peak and offset timing
were found over an average of 21.4 ± 1.0 min and reduced metabolic cost by 17.4 ± 3.2% compared with
walking without the device (mean ± SEM), which represents an improvement of more than 60% on
metabolic reduction compared with state-of-the-art devices that only assist hip extension. In
addition, our results provide evidence for participant-specific metabolic distributions with respect
to peak and offset timing and metabolic landscapes, lending support to the hypothesis that
individualized control strategies can offer substantial benefits over fixed control strategies.
These results also suggest that this method could have practical impact on improving the performance
of wearable robotic devices.
