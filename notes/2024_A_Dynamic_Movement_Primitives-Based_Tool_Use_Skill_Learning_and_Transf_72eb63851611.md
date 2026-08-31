# A Dynamic Movement Primitives-Based Tool Use Skill Learning and Transfer Framework for Robot Manipulation

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：A Dynamic Movement Primitives-Based Tool Use Skill Learning and Transfer Framework for Robot Manipulation
- 作者：Zhenyu Lu; Ning Wang; Chenguang Yang
- 年份：2024
- 期刊/会议：IEEE Transactions on Automation Science and Engineering
- DOI：10.1109/tase.2024.3370139
- URL：https://doi.org/10.1109/tase.2024.3370139
- PDF 状态：open_access_pdf

## 2. 一句话结论

可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

## 3. AI 插入位置

轨迹生成器/学习器

## 4. 控制底座

impedance control, DMP

## 5. 输入数据

膝速度, EMG

## 6. 输出参数

助力时机/phase_offset, MO_Kp/MO_Kd/阻抗参数

## 7. 目标函数或评价指标

EMG reduction/activity, safety constraint；指标：EMG reduction/activity, safety constraint

## 8. 实验对象和实验任务

未从摘要确认

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：可映射到 MO_Kp/MO_Kd；可映射到 AO/Phi/Phase0Event 与 phase_offset；涉及本研究不使用的 EMG/IMU，仅作方法参考，不作为直接实现模板

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
- 输出类型：control/impedance parameters, trajectory or gait features, mode switching / intent
- 是否真实机器人闭环：yes/likely
- 与本项目参数映射：phase_offset / Phi / Phase0Event, MO_Kp / MO_Kd / MO_OverwriteKpGain, SafeTorque / safety constraints
- 实现难度：not applicable
- 是否适合 1-2 个月快速成稿：not semantic route

## Abstract / Metadata Evidence

This paper presents a framework for learning and transferring robot tool-use skills based on Dynamic
Movement Primitives (DMPs) for robot fine manipulation. DMPs and their enhanced methods are employed
to acquire a specific tool-use skill applicable to tools with similar sizes, shapes, and uses.
However, the acquired skills may not be transferable to other scenarios and tools with variations.
The new framework introduces two new types of skills based on DMPs: Object Operating (O2) skill and
Tool Flipping (TF) skill. The O2 skill enables robots to handle tools for manipulating objects to
achieve desired effects. The learning process for the O2 skill considers limitations imposed by
tools and the environment during human demonstrations. Distinguishing between whether constraints
can be modelled or not, we propose both a model-based and a constraint-based method to separate a
constraint-irrelevant (CI) skill and the constrained conditions. The CI skill is generalized using a
novel method called constrained -DMP lite, enabling adaptation to new tasks with special tools. The
TF skill addresses situations where tools must generate an action to alter contacting positions on
both objects and tools while avoiding conflicts during movement. Finally, the TF and O2 skills are
generalized to be applied in creating a continuous action chain. We conduct several experiments to
compare and analyze the advantages and disadvantages of the proposed methods with other approaches
in terms of generalizability and calculation complexity. Note to Practitioners —Strengthening robot
tool-use ability has been a hot research topic in recent years because these tools can extend the
reachability and enhance the flexibility of robots. The previous research on DMPs has been utilized
for learning tool-use skills. However, the learned skills few considered the tools’ special use
regulations, therefore the skill of using a tool is hard to transfer to another tool-use case. This
paper explores tool-use skill learning and transfer between different tools by developing a
framework based on the DMPs for this problem. The framework consists of two kinds of skills: O2
skill and TF skill with different purposes as well as a series of newly developed algorithms, such
as constrained -DMP lite, a model-based and a constraint-based CI skill learning methods. These
methods can separate the constraints from human demonstrations of using tools to achieve a CI skill
and generalize the CI skill according to the constraints generated from a new tool-use manipulation
task. We verify the effectiveness of the proposed framework through some typical tool-use
experiments, including pushing objects, cutting and obstacle avoidance in actuality. The development
of this framework can be used in industrial and house working scenarios.
