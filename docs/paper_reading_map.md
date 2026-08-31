# 论文阅读地图：先知道这堆论文在讲什么

本文档是给当前项目用的“读论文导航”。它不替代逐篇精读笔记，而是先回答三个问题：

1. 这些论文分成哪几类？
2. 每类到底在讲什么？
3. 你应该按什么顺序读，才不会被论文堆淹没？

## 当前论文线的核心判断

本项目不适合把论文主线写成“LLM 直接控制下肢外骨骼”。更稳的主线是：

> 面向膝关节外骨骼 DMP-阻抗控制的安全约束、试次级、个体化参数调整框架。

LLM/Agent 文献的作用是支撑一个高层接口：

> 治疗师或研究者用自然语言表达训练目标，LLM 将其翻译成受限参数意图，再由规则、优化器、安全约束和人工确认把关。

因此，论文大致分成两条线：

- **外骨骼控制主线**：HIL 优化、DMP、阻抗控制、个体化辅助、安全约束。
- **LLM/Agent 接口线**：自然语言到技能/参数/约束的映射，高层规划，安全过滤。

## A 类：外骨骼个体化与 Human-in-the-loop 优化

这是主线。你写论文时最该依赖这类文献。

它们通常在做这件事：

```text
把外骨骼助力曲线参数化
-> 选一个人体相关指标作为目标函数
-> 用 Bayesian optimization / CMA-ES / HIL optimization 找个人最优参数
-> 在真人穿戴实验中证明比固定参数好
```

常见优化对象：

- 助力峰值大小，对应你的 `Amplitude`
- 助力时机，对应你的 `phase_offset`
- 助力持续时间或曲线宽度，对应你的 `tau`
- 阻抗/刚度/阻尼，对应你的 `MO_Kp`、`MO_Kd`

常见评价指标：

- metabolic cost
- EMG reduction
- gait symmetry
- walking speed
- interaction torque
- comfort / preference
- convergence trials

你应该把这类论文读成一句话：

> 别人证明了外骨骼参数需要个体化，并且可以通过低频优化从人体反馈中调出来。

代表论文：

- Human-in-the-loop optimization of exoskeleton assistance during walking
- Human-in-the-loop optimization of hip assistance with a soft exosuit
- Human-in-the-loop optimization of knee exoskeleton assistance for minimizing metabolic and muscular effort
- Comparing optimized exoskeleton assistance of the hip, knee, and ankle
- Human-in-the-loop optimization of exoskeleton assistance via online simulation of metabolic cost
- Learning to Assist Different Wearers in Multitasks
- A Two-Layer Human-in-the-Loop Optimization Framework for Customizing Lower-Limb Exoskeleton Assistance

和本项目的关系：

```text
这些论文支撑“低频调参”这件事是正经外骨骼研究方向。
你的系统区别在于：已有 AO-DMP-阻抗-Speedgoat 链路，所以优化空间可以直接落到 Amplitude / tau / phase_offset / MO_Kp / MO_Kd。
```

## B 类：DMP、阻抗控制与自适应外骨骼控制

这是控制底座。它们告诉你：你的参数为什么是这些，而不是凭空选的。

它们通常在做这件事：

```text
用 DMP / CPG / reference trajectory 生成步态轨迹
-> 用 PD / impedance / admittance 跟踪或协助
-> 根据人机交互、意图、误差或阶段调整参数
```

重点看三个问题：

1. 它如何表达轨迹？
2. 它如何调刚度、阻尼或助力强度？
3. 它有没有把安全限制放进控制链路？

代表论文：

- A Lower Limb Exoskeleton Adaptive Control Method Based on Model-free Reinforcement Learning and Improved DMPs
- DMP-Based Motion Generation for a Walking Exoskeleton Robot Using Reinforcement Learning
- Interaction learning control with movement primitives for lower limb exoskeleton
- Review of control strategies for lower-limb exoskeletons to assist gait
- Active-Impedance Control of a Lower-Limb Assistive Exoskeleton
- Adaptive Impedance Control of a Human-Robotic System Based on Motion Intention Estimation

和本项目的关系：

```text
这些论文支撑 DMP/阻抗控制是合理底座。
你的创新不一定是重新发明 DMP 或阻抗控制，而是把它们变成可解释、可约束、可低频优化的参数空间。
```

## C 类：LLM 做机器人高层规划或工具调用

这类论文不是外骨骼主线，但可以帮你解释“LLM 在机器人里应该放在哪一层”。

它们通常在做这件事：

```text
自然语言任务
-> LLM 分解任务、生成程序或选择技能
-> 机器人已有技能/规划器/控制器执行
```

重要结论：

> LLM 通常不应该直接替代低层控制器，而是放在高层语义、规划、技能选择或程序生成层。

代表论文：

- SayCan / Do As I Can, Not As I Say
- Code as Policies
- ProgPrompt
- Inner Monologue

逐篇一句话：

- **SayCan**：LLM 说“应该做什么”，可行性/value function 决定“当前能不能做”。
- **Code as Policies**：LLM 把自然语言转成调用机器人 API 的代码，而不是直接输出电机命令。
- **ProgPrompt**：用程序式 prompt 限定 LLM 只能调用已有动作。
- **Inner Monologue**：LLM 结合环境反馈和人类反馈持续修正高层计划。

和本项目的关系：

```text
治疗师说“摆动期多帮一点”
-> LLM 只能映射到候选意图，例如 increase Amplitude 或 adjust phase_offset
-> 不能直接输出实时 torque
```

## D 类：LLM + 康复机器人 / 外骨骼接口

这是 LLM 线里最贴近本项目的一类。数量不多，但很重要。

它们通常在做这件事：

```text
治疗师/用户自然语言
-> LLM 解析任务、意图或上下文
-> 输出结构化参数、动作或配置
-> 由规则、安全层或人工确认把关
```

代表论文：

- Virtual Technician: A multi-modal interface facilitating therapists' adoption of rehab robots
- LLM-Enabled Incremental Learning Framework for Hand Exoskeleton Control
- A Semantic-Aware Framework for Safe and Intent-Integrative Assistance in Upper-Limb Exoskeletons

逐篇一句话：

- **Virtual Technician**：把治疗师的自然语言意图翻译成康复机器人参数建议，强调治疗师仍保留决策权。
- **Hand Exoskeleton LLM Incremental Learning**：手部外骨骼用自然语言解析器处理已有命令，用 LLM 扩展未预设手势/物体任务。
- **Semantic-Aware Upper-Limb Exoskeleton**：LLM 提取任务语义并配置辅助参数，再结合异常检测、轨迹细化和阻抗控制保证安全。

和本项目的关系：

```text
这三篇是你讲“LLM/Agent 接入外骨骼不是为了直接控力矩，而是为了语义到参数接口”的关键参考。
它们可以支撑你的未来系统设计：
therapist instruction -> structured parameter intent -> safety/rule check -> human confirmation。
```

## E 类：VLA / 端到端机器人动作模型

这类论文很有名，但对你的主线只能当背景，不适合作为直接方案。

代表论文：

- RT-2
- VoxPoser

逐篇一句话：

- **RT-2**：把视觉、语言和机器人动作放进同一个模型里，尝试从网页知识迁移到机器人动作。
- **VoxPoser**：LLM/VLM 从语言里提取 affordance 和约束，生成 3D value maps，再由模型规划器执行。

和本项目的关系：

```text
这些论文说明“语言到动作”是机器人前沿趋势。
但膝关节外骨骼是高安全 human-in-the-loop 系统，所以本文应主动说明：我们不采用 LLM/VLA 直接输出实时动作，而采用高层受限参数接口。
```

## F 类：LLM 机器人安全约束

这类论文用于回答审稿人最可能问的问题：

> LLM 乱说怎么办？

它们通常在做这件事：

```text
LLM 生成候选动作/计划/约束
-> 形式化规则、CBF、LTL、安全表示或人工确认过滤
-> 不安全动作被拒绝或重规划
```

代表论文：

- Plug in the Safety Chip
- Updating Robot Safety Representations Online From Natural Language Feedback
- Language-informed safe navigation / language-guided safety constraints 相关工作

和本项目的关系：

```text
LLM 只能生成参数候选，最终必须经过：
- 参数范围
- 单步变化幅度
- SafeTorque 裕度
- Torque_Guard
- 人工确认
```

## 推荐阅读顺序

不要按下载顺序读。建议这样读：

### 第一轮：只读摘要和图，建立地图

1. Virtual Technician
2. A Semantic-Aware Framework for Safe and Intent-Integrative Assistance in Upper-Limb Exoskeletons
3. SayCan
4. Code as Policies
5. Plug in the Safety Chip
6. Human-in-the-loop optimization of knee exoskeleton assistance
7. A Two-Layer Human-in-the-Loop Optimization Framework
8. A Lower Limb Exoskeleton Adaptive Control Method Based on Improved DMPs

目标：知道你的论文该站在哪。

### 第二轮：精读 5 篇

建议先精读：

1. **Virtual Technician**
   - 看它如何把治疗师自然语言变成机器人参数。
2. **A Semantic-Aware Framework for Safe and Intent-Integrative Assistance in Upper-Limb Exoskeletons**
   - 看它如何把 LLM、意图、安全和阻抗控制放在一个系统里。
3. **Human-in-the-loop optimization of knee exoskeleton assistance**
   - 看膝外骨骼个体化优化怎么设参数和指标。
4. **A Lower Limb Exoskeleton Adaptive Control Method Based on Improved DMPs**
   - 看 DMP 和学习/自适应如何结合。
5. **Plug in the Safety Chip**
   - 看如何给 LLM-driven robot agent 加安全外壳。

目标：为你的 introduction 和 method 找骨架。

### 第三轮：补背景

再读：

- SayCan
- Code as Policies
- ProgPrompt
- Inner Monologue
- RT-2
- VoxPoser
- DMP / impedance control survey

目标：写 related work，不让 LLM 部分显得孤立。

## 你可以这样理解整篇论文的逻辑

```text
外骨骼需要个体化辅助
-> HIL 优化可以调参数，但目标函数和参数解释仍依赖工程/治疗师经验
-> DMP-阻抗控制给了一个低维、可解释、可约束的参数空间
-> LLM 可以理解治疗师自然语言，但不能直接控制安全关键设备
-> 所以本文把 LLM 限制在“语义到参数意图”的高层
-> 参数建议再经过试次指标、安全规则和人工确认
-> 最终服务于下一试次的 DMP/阻抗参数调整
```

## 最容易踩的坑

1. **把 LLM 说成实时控制器**
   - 不建议。审稿人会问实时性、安全性、稳定性。

2. **把文献检索系统说成控制系统一部分**
   - 不建议。文献线服务论文写作，不参与外骨骼运行。

3. **把 Agent 讲得太泛**
   - 应收窄为：LLM-based therapist/project-aware tool-using parameter review agent。

4. **没有真实或半真实实验**
   - 外骨骼论文的含金量很依赖实验。至少要有 Speedgoat/Simulink 试次日志、参数建议和安全否决案例。

5. **没有 baseline**
   - 至少需要和人工调参、固定参数、规则调参或无 LLM 接口比较。

## 当前最合适的论文题目方向

中文：

> 面向 DMP-阻抗膝关节外骨骼的安全约束试次级参数审查与自然语言意图接口

英文：

> A Safety-Constrained Trial-Level Parameter Review Interface for DMP-Impedance Knee Exoskeleton Assistance

如果想突出 LLM：

> LLM-Assisted Therapist-in-the-Loop Parameter Adaptation for DMP-Impedance Knee Exoskeleton Assistance

但建议不要把标题写成：

> LLM Agent for Knee Exoskeleton Control

这个题目太容易让人误解成 LLM 直接控腿。
