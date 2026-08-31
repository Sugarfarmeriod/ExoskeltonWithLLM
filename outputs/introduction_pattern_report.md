# 引言写法模式分析报告

本报告仅基于本地 PDF 文本缓存生成。脚本用启发式规则抽取类似 Introduction 的段落，并总结这些论文常用的引言写作动作；它是写作规划辅助材料，不等同于已经逐条核验引用的文献综述。

- 文本缓存目录文件总数（含历史/重复缓存）：132
- 当前矩阵记录数：108
- 矩阵关联且可读取的文本缓存数：92
- 成功抽取的引言-like 段落数：63
- 来源表：`outputs/introduction_pattern_sources.csv`

## 高频写作动作

- 从康复/移动能力需求切入：38 篇引言
- 解释为什么需要外骨骼辅助：47 篇引言
- 介绍已有控制底座：21 篇引言
- 把问题转化为个体化/参数调节问题：39 篇引言
- 引入 AI/优化作为自适应机制：20 篇引言
- 用传感/状态估计支撑同步控制：29 篇引言
- 强调实时、安全、可部署约束：36 篇引言
- 最后明确本文贡献：24 篇引言

## 常见论证路径

- 一般背景 -> 提出方法：24 篇。例子：Exoskeleton robot control for synchronous walking assistance in repetitive manual handling; RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control; AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipula
- 辅助收益 -> 个体差异/调参缺口：19 篇。例子：Therapist-exoskeleton-patient interaction for gait therapy; Improving CMA-ES Convergence Speed, Efficiency, and Reliability in Noisy Robot Optimizatio; Powered knee exoskeleton improves sit-to-stand transitions in stroke patients using electr
- 康复需求 -> 控制底座 -> 实时/安全部署：9 篇。例子：Dynamic Movement Primitives Modulation-Based Compliance Control for a New Sitting/Lying Lo; Review on Control Strategies for Lower Limb Rehabilitation Exoskeletons; A Pediatric Knee Exoskeleton With Real-Time Adaptive Control for Overground Walking in Amb
- 个体化需求 -> 控制参数 -> 优化器：5 篇。例子：Electromyography Signal Acquisition, Filtering, and Data Analysis for Exoskeleton Developm; Novel Design on Knee Exoskeleton with Compliant Actuator for Post-Stroke Rehabilitation; Optimizing lower limb rehabilitation: the intersection of machine learning and rehabilitat
- 已有控制能力 -> 尚未解决的控制缺口：5 篇。例子：Learning Cooperative Primitives with physical Human-Robot Interaction for a HUman-powered ; Learning Physical Human–Robot Interaction With Coupled Cooperative Primitives for a Lower ; A Lower Limb Exoskeleton Adaptive Control Method Based on Model-free Reinforcement Learnin
- 传感/状态估计 -> 控制同步：1 篇。例子：Exoskeleton Active Walking Assistance Control Framework Based on Frequency Adaptive Dynami

## 可迁移到本项目的引言模板

1. 临床/辅助需求：膝关节外骨骼可用于步态康复与行走辅助，但实际收益依赖人与外骨骼之间是否同步、舒适且安全。
2. 现有工程基础：DMP 轨迹生成结合阻抗/PD 力矩控制具有可解释、低维、实时可部署等优势，适合 Simulink/Speedgoat 控制链路。
3. 核心限制：辅助效果对 `Amplitude`、`tau`、`phase_offset`、`MO_Kp`、`MO_Kd` 等参数敏感；人工调参难以覆盖不同个体和不同步态状态。
4. 文献过渡：HIL optimization、Bayesian optimization、CMA-ES、步态相位估计和自适应阻抗控制说明，学习方法可以用于个性化辅助；但很多工作没有把 AI 插入点明确映射到一个带安全边界的 DMP-阻抗实现中。
5. 研究缺口：对于准直驱膝关节外骨骼，缺少的不是端到端实时力矩策略，而是在实时控制环外运行的低频参数自适应层；该层必须服从 `Torque_Guard`、`SafeTorque` 和饱和限幅。
6. 本文目标：将 AI 表述为 DMP/阻抗参数的有界优化器，利用 `Phi`、`Phase0Event`、`FeetLoad`、`q_meas`、`dq_meas`、`tau_e` 等本地信号构造目标函数或评价指标。
7. 本文贡献：说明系统框架、优化参数集合、目标/安全约束，以及实验或验证流程。

## 可模仿的句式类型

### 个体化 / 调参缺口

- Framework for Personalizing Wearable Devices Using Real-Time Physiological Measures: Using BO, the HIL optimization identified the optimal parameters twice as fast as the method proposed by Felt.
- Shortcomings of human-in-the-loop optimization of an ankle-foot prosthesis emulator: a case series: Introduction Over 600 000 individuals in the US live with a major lower limb amputation, with this number expected to double by 2050 due © 2021 The Authors.
- Optimizing lower limb rehabilitation: the intersection of machine learning and rehabilitative robotics: Following this, machine learning also plays a pivotal role in optimizing personalized TYPE Mini Review PUBLISHED 26 January 2024 | DOI 10.3389/fresc.2024.1246773 Frontiers in Rehabilitation Sciences 01 frontiersin.org rehabilitation protocols and predict patient outcomes ( 7).
- Human-in-the-loop optimization of wearable device parameters using an EMG-based objective function: The current focus is on achieving individualized assistance, acknowledging that physiological and neurological differences among individuals affect their response to the same device and assistance (Zhang et al.,2017).
- Electromyography Signal Acquisition, Filtering, and Data Analysis for Exoskeleton Development: Moreover, variations in skin impedance, movement artifacts [7], and individual anatomical differences can significantly affect the quality and reliability of EMG signals.
- Dynamic Movement Primitives Modulation-Based Compliance Control for a New Sitting/Lying Lower Limb Rehabilitation Robot: Since the model parameters are difficult to obtain accurately by system identification, the active disturbance rejection controller (ADRC) has gradually gained attention in rehabilitation robots [20].

### 控制底座

- Dynamic Movement Primitives Modulation-Based Compliance Control for a New Sitting/Lying Lower Limb Rehabilitation Robot: For patients with weak residual muscle stre ngth, passive control strategies are usually needed to assist the affected limb in repeating training along a predefined trajectory.
- Learning Physical Human–Robot Interaction With Coupled Cooperative Primitives for a Lower Exoskeleton: In Section II-A2, we introduce CCP, which adds an impedance model on top of basic DMP to describe the pHRI between the pilot and the exoskeleton.
- Learning Cooperative Primitives with physical Human-Robot Interaction for a HUman-powered Lower EXoskeleton: Dynamic Movement Primitives (DMP) serves as a powerful tool for representing discrete and periodic trajectories, and has been widely used in imitation learning related applications [5][6], especially in interaction tasks (both interact with human and the environment) [7][8][13].
- Exoskeleton Active Walking Assistance Control Framework Based on Frequency Adaptive Dynamics Movement Primitives: For rehabilitation exoskeleto n, the main control target is to drive the patient’s paralyzed limb to follow a predeﬁned trajectory for rehabilitation purpose.
- Compensating elastic faults in a torque-assisted knee exoskeleton: functional evaluation and user perception study: Journal of NeuroEngineering and Rehabilitation (2024) 21:230 its energy efficiency capabilities, and its intrinsically low output impedance [2 –5].
- Novel Design on Knee Exoskeleton with Compliant Actuator for Post-Stroke Rehabilitation: Despite the aforementioned efforts, existing torque control methodologies for SEAs only consider the motor-side dynamics and loadside position but overlook the intricate and unknown dynamics on the load side [21,22].

### AI / 优化器过渡

- Framework for Personalizing Wearable Devices Using Real-Time Physiological Measures: Kantharaju et al.: Framework for Personalizing Wearable Devices successful personalization methods is a data-driven approach known as Human-in-the-loop (HIL) optimization [1], [4], [15], [16], [17], [18], [19].
- Shortcomings of human-in-the-loop optimization of an ankle-foot prosthesis emulator: a case series: Human-in-the-loop optimization (HILO) has been successfully used to determine control parameters for exoskeletons that result in high reductions in metabolic cost [28 –32].
- Optimizing lower limb rehabilitation: the intersection of machine learning and rehabilitative robotics: Recently, machine learning has shown potential in reducing costs in lower limb rehabilitation, offering solutions that can be managed with less dependency on highly skilled therapists.
- Reducing the muscle activity of walking using a portable hip exoskeleton based on human-in-the-loop optimization: Introduction: Human-in-the-loop optimization has made great progress to improve the performance of wearable robotic devices and become an effective customized assistance strategy.
- Electromyography Signal Acquisition, Filtering, and Data Analysis for Exoskeleton Development: EMGs have become instrumental in developing intuitive and human-in-the-loop interfaces for exoskeleton systems [5], offering a direct correlation between the neural command signals and the resulting movements.
- AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation: The concept of improvement through failures is widely applied in training foundation models and is exemplified by techniques such as Reinforcement Learning with Human Feedback (RLHF)[5, 11], where human oversight and feedback steers models toward desired outcomes.

### 安全 / 部署约束

- Dynamic Movement Primitives Modulation-Based Compliance Control for a New Sitting/Lying Lower Limb Rehabilitation Robot: Wearable LLRRs need the patients to be able to walk independently , which can assist them in completing daily living activities, such as sit -to-stand transfer [7], flat ground walking [8], and going up and down stairs [9].
- A Lower Limb Exoskeleton Adaptive Control Method Based on Model-free Reinforcement Learning and Improved Dynamic Movement Primitives: 1 Introduction In addition to ensuring safety, precision, and robustness, exoskeleton robots need to meet the key requirement of reducing human-exoskeleton interaction force in different terrains to enhance human movement comfort and reduce oxygen consumption [1].
- Electromyography Signal Acquisition, Filtering, and Data Analysis for Exoskeleton Development: Introduction Wearable robotics, both powered (active) and non-powered (passive) exoskeletons, have advanced rapidly over the past two decades with their applications ranging from physical rehabilitation and mobility assistance to industrial support and military augmentation [1].
- Novel Design on Knee Exoskeleton with Compliant Actuator for Post-Stroke Rehabilitation: As a typical human-in-the-loop process, ensuring the safety and comfort of patients during their interaction with knee exoskeletons is critical for both their immediate wellbeing and the long-term success of robot-assisted training.
- A Pediatric Knee Exoskeleton With Real-Time Adaptive Control for Overground Walking in Ambulatory Individuals With Cerebral Palsy: This goal may be combined in some more affected individuals with the secondary objective to make walking easier and/or safer.
- A novel gesture interaction control method for rehabilitation lower extremity exoskeleton: 1 Introduction Exoskeleton robots are wearable devices designed to be worn by humans, enabling coordinated movement with the wearer’s limbs to perform tasks.

## 注意事项

- 抽取片段可能包含 OCR 或 PDF 解析噪声。
- 不建议直接照抄这些句子；重点学习其论证顺序和段落功能。
- 最终写进论文的引用性判断，必须回到 PDF 或元数据逐条核验。
