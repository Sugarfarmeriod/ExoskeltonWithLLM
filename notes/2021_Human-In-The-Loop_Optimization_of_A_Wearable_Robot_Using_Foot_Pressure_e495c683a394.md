# Human-In-The-Loop Optimization of A Wearable Robot Using Foot Pressure Sensors

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：Human-In-The-Loop Optimization of A Wearable Robot Using Foot Pressure Sensors
- 作者：Micheal Jacobson; Prakyath Kantharaju; Hyeongkeun Jeong; Xingyuan Zhou; Jae-Kwan Ryu; Jung-Jae Park; Hyun-Joon Chung; Myunghee Kim
- 年份：2021
- 期刊/会议：Research Square
- DOI：10.21203/rs.3.rs-1186504/v1
- URL：https://doi.org/10.21203/rs.3.rs-1186504/v1
- PDF 状态：open_access_pdf

## 2. 一句话结论

最贴近低频优化 DMP/阻抗参数的接入方式；可映射到 AO/Phi/Phase0Event 与 phase_offset；可映射到 DMP Amplitude 和 SafeTorque 约束；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

参数优化器

## 4. 控制底座

PD/torque control, low-frequency optimizer

## 5. 输入数据

IMU, 足底压力/力传感, 膝速度, 膝力矩/交互力矩, EMG

## 6. 输出参数

助力时机/phase_offset, 助力强度/Amplitude/torque profile, MO_Kp/MO_Kd/阻抗参数, tau/持续时间

## 7. 目标函数或评价指标

metabolic cost, EMG reduction/activity, gait symmetry, comfort score；指标：metabolic cost, EMG reduction/activity, gait symmetry, comfort score

## 8. 实验对象和实验任务

8 individuals

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
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：Amplitude / assistive torque / SafeTorque, phase_offset / Phi / Phase0Event, tau, MO_Kp / MO_Kd / MO_OverwriteKpGain
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

Abstract Background: Individuals with below-knee amputation (BKA) experience increased physical
effort when walking, and the use of a robotic ankle-foot prosthesis (AFP) can reduce such effort.
Our prior study on a robotic AFP showed that walking effort could be reduced if the robot is
personalized to the wearer. The personalization is accomplished using human-in-the-loop (HIL)
optimization, in which the cost function is based on a real-time physiological signal indicating
physical effort. The conventional physiological measurement, however, requires a long estimation
time, hampering real-time optimization due to the limited experimental time budget. In addition, the
physiological sensor, based on respiration uses a mask with rigid elements that may be difficult for
the wearer to use. Prior studies suggest that a symmetry measure using a less intrusive sensor,
namely foot pressure, could serve as a metric of gait performance. This study hypothesized that a
function of foot pressure, the symmetric foot force-time integral, could be used as a cost function
to rapidly estimate the physical effort of walking; therefore, it can be used to personalize
assistance provided by a robotic ankle in a HIL optimization scheme. Methods: We developed a new
cost function derived from a well-known clinical measure, the symmetry index, by hypothesizing that
foot force-time integral (FFTI) symmetry would be highly correlated with metabolic cost. We
conducted experiments on human participants (N = 8) with simulated amputation to test the new cost
function. The study consisted of a discrete trial day, an HIL optimization training day, and an HIL
optimization data collection day. We used the discrete trial day to evaluate the correlation between
metabolic cost and a cost function using symmetric FFTI percentage. During walking, we varied the
prosthetic ankle stiffness while measuring foot pressure and metabolic rate. On the second and third
days, HIL optimization was used to find the optimal stiffness parameter with the new cost function
using symmetric FFTI percentage. Once the optimal stiffness parameter was found, we validated the
performance with comparison to a weight-based stiffness and control-off conditions. We measured
symmetric FFTI percentage during the stance phase, prosthesis push-off work, metabolic cost, and
user comfort in each condition. We expected the optimized prosthetic ankle stiffness based on the
newly developed cost function could reduce the energy expenditure during walking for the individuals
with simulated amputation. Results: We found that the cost function using symmetric foot force-time
integral percentage presents a reasonable correlation with measured metabolic cost (Pearson’s R &gt;
0.62). When we employed the new cost function in HIL ankle-foot prosthesis parameter optimization, 8
individuals with simulated amputation reduced their cost of walking by 15.9% (p = 0.01) and 16.1% (p
= 0.02) compared to the weight-based and control-off conditions, respectively. The symmetric FFTI
percentage for the optimal condition tended to be closer to the ideal symmetry value (50%) compared
to weight-based (p = 0.23) and control-off conditions (p = 0.04). Conclusion: This study suggests
that foot force-time integral symmetry using foot pressure sensors can be used as a cost function
when optimizing a wearable robot parameter.
