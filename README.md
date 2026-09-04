# ExoPilot Agent

面向膝关节外骨骼研发试验的受约束 AI Agent：把一次 Speedgoat 试次转化为可复核的步态指标、保守的参数建议和工程诊断报告。

> 项目性质：小型外骨骼企业场景下的研发型作品集 / MVP。
> 项目角色：AI Agent / Applied AI Intern，负责从需求澄清、资料调研、数据契约、工具实现到安全边界与验收设计。
> 当前状态：确定性分析与建议流水线已可运行；完整 LLM 工具编排、真实试次标定和人体实验仍在推进。

## 项目故事

一家小型外骨骼研发团队已经拥有 MATLAB/Simulink + Speedgoat 实时控制链路，但试验后的分析和调参仍高度依赖工程师：导出日志、检查步态周期、比较参考轨迹、判断力矩裕量、修改下一试次参数，再手工整理报告。

这个流程有三个问题：

- 慢：每次试验都要重复清洗数据和计算指标。
- 不一致：不同工程师对“应该调什么、调多少”的判断口径不同。
- 难追溯：建议、依据、否决原因和最终操作容易散落在聊天与临时文件里。

我的实习任务不是让 LLM 接管控制器，而是在 6–8 周内做出一个可演示、可验证的研发副驾驶：让 Agent 调用确定性工具完成分析，只在白名单动作空间内提出下一试次建议，并把最终决定留给人类工程师。

## 产品定位

ExoPilot 服务于外骨骼公司的研发与试验团队，而不是直接面向患者。

| 角色 | 现有痛点 | ExoPilot 提供的价值 |
| --- | --- | --- |
| 控制工程师 | 重复检查相位、跟踪误差和力矩裕量 | 统一指标与保守调参建议 |
| 试验工程师 | 日志格式不统一、试次难复现 | 固定数据契约与试次归档 |
| 算法研究员 | 论文证据与工程实现脱节 | 可追溯的方法卡、证据矩阵和规格 |
| 项目负责人 | 无法快速判断建议是否安全、是否有依据 | 带规则 ID、阈值和否决原因的报告 |

这不是一个“聊天机器人套壳”。Agent 的价值在于编排已经验证的工具、解释结构化结果和维护审计链，而不是凭语言能力猜测控制参数。

## 为什么这是一个通用 Agent 工程项目

ExoPilot 的业务对象是外骨骼，但工程骨架与客服、运维、投研或 Coding Agent 相同：理解目标、获取上下文、选择工具、校验结果、执行受限动作，并留下评测与追踪记录。

| 企业 Agent 能力 | 常见业务 Agent | ExoPilot |
| --- | --- | --- |
| Context | 订单、知识库、代码仓库 | trial metadata、历史试次、参数快照 |
| Tool Calling | CRM、搜索、工单 API | 步态分析、跟踪指标、力矩裕量、参数规则 |
| Planning | 查询 → 判断 → 执行动作 | 校验 → 分析 → 安全裁决 → 生成建议 |
| Structured Output | 工单、SQL、代码补丁 | `parameter_suggestion.json` |
| Guardrail | 权限、金额、沙箱 | 数据质量、力矩阈值、参数白名单 |
| Human-in-the-loop | 高风险操作审批 | 工程师确认下一试次参数 |
| Eval & Trace | 任务成功率、调用轨迹 | trial → metric → rule → suggestion → approval |

项目的可迁移价值不依赖外骨骼行业：核心工作是把领域专家的知识转化为 Agent 可安全调用的软件契约。外骨骼只是一个高约束的 vertical。

## 目标 Agent Loop

```text
工程师目标 / 穿戴者反馈
           │
           ▼
   Agent 识别任务与试次
           │
           ├─ load_trial / check_data_quality
           ├─ analyze_gait / compute_tracking_metrics
           ├─ compute_torque_margin
           └─ evaluate_parameter_policy
                         │
                         ▼
             确定性安全规则与参数白名单
                         │
                         ▼
       指标 JSON → 参数建议 JSON → 诊断报告
                         │
                         ▼
                   工程师审批
                         │
                         ▼
        下一试次由现有 Simulink/Speedgoat 链路执行
```

LLM 位于实时力矩环之外，按试次或步态窗口低频工作。它不能直接输出力矩，不能绕过 `Torque_Guard` 和 Saturation，也不能自动向 Speedgoat 写入参数。

当前仓库已经实现从日志校验到诊断报告的确定性工具链；Agent 的自然语言入口、工具选择和多步编排仍属于下一阶段。

## 我在项目中负责什么

作为 AI Agent 开放岗的实习项目，我把一个模糊的“LLM + 外骨骼”方向拆成了六类可验收交付：

1. **需求与边界**：明确 Agent 只做低频分析、建议和报告，不进入实时控制闭环。
2. **研究调研**：搭建合法来源的论文检索、筛选、证据卡和方法资产流水线。
3. **数据工程**：定义统一试次 Schema，连接 Speedgoat File Log、MAT/CSV 与 Python 分析。
4. **Agent 工具**：实现校验、步态指标计算、受约束建议和诊断报告生成。
5. **安全与治理**：为每条建议保留阈值、规则 ID、否决原因和人工确认标志。
6. **工程验收**：使用 OpenSpec 固化需求，通过合成试次和聚焦测试验证主流程。

## 真实团队中的协作边界

小型企业的 MVP 团队只需要 3–5 个实际参与角色，Agent 专职开发由一人负责：

| 角色 | 提供什么 | 不由 Agent 工程师替代的决策 |
| --- | --- | --- |
| 研发 / 控制负责人 | 业务目标、禁止动作、安全优先级 | 是否允许进入真实硬件试验 |
| 控制工程师 | 指标定义、参数范围、DMP/阻抗规则 | 参数物理意义与允许调整幅度 |
| 试验工程师 | Speedgoat 日志、信号质量、试次流程 | 数据是否可信、现场是否可执行 |
| Applied AI / Agent Engineer | Schema、Tool、Workflow、Eval、Trace | 不擅自修改控制规则 |
| QA / 伦理 / 法规（后期共享） | 人体试验与产品化要求 | 合规批准与发布决策 |

我的角色是把专家给出的指标、规则和权限边界实现成可靠工具与 Agent 工作流；控制参数、硬件试验和合规结论由对应负责人确认。

## 当前能力

| 模块 | 状态 | 交付物 |
| --- | --- | --- |
| Speedgoat 日志归档 | 已实现 | `tools/import_slrt_filelog_trial.m` |
| 试次数据契约与校验 | 已实现 | `docs/trial_data_schema.md`、`scripts/trial_io.py` |
| 步态周期与指标分析 | 已实现 | `scripts/gait_analysis.py` |
| 受约束参数建议 | 已实现 | `scripts/parameter_suggestion.py` |
| 可追溯诊断报告 | 已实现 | `scripts/diagnostic_report.py` |
| 合成试次端到端演示 | 已实现 | `data/fixtures/synthetic_trial_001/` |
| 文献检索与方法资产 | 已实现 | `scripts/`、`notes/`、`outputs/method_cards/` |
| LLM 工具注册与对话编排 | 设计中 | 复用现有 JSON 工具输出，不让模型读取原始长序列 |
| 真实模型信号映射与阈值标定 | 待工程确认 | 见 `docs/open_decisions.md` |
| 健康受试者验证 | 计划中 | 预计 8 人，协议、伦理与统计方案仍需正式确认 |

## 如何验收 Agent

Agent 不能只以“回答是否像人”来验收。本项目按完整执行轨迹定义评测：

| Eval | 通过条件 | 当前状态 |
| --- | --- | --- |
| Data / Recovery | 缺字段、非数值或时间异常时停止分析并指出原因 | 已有聚焦测试 |
| End-to-end | 合成试次稳定生成 metrics、suggestion、report 三类产物 | 已有回归测试 |
| Safety | 力矩裕量不足或数据不可靠时 HOLD，不得增加助力 | 规则已实现，场景集待扩充 |
| Traceability | 每条建议能回溯到源指标、阈值、规则 ID 和否决原因 | 已实现 |
| Tool Selection | Agent 为任务选择正确工具，不调用无关工具 | 待 LLM 编排层 |
| Tool Arguments | 只使用存在的 trial 和允许的参数，不幻觉参数值 | 待 LLM 编排层 |
| Report Grounding | 报告不得包含结构化输入之外的控制结论 | 已有输入约束，待扩充评测集 |

企业侧的成功指标将围绕单次试验分析工时、建议与专家判断一致率、可追溯率和安全违规次数建立基线；接入 LLM 后再增加任务成功率、延迟与调用成本。完成真实试次基线后补充量化收益。

## 安全设计

外骨骼不是普通 SaaS。这个项目把安全约束放在 Agent 能力之前：

- **确定性优先**：原始时序由 Python/MATLAB 工具处理，LLM 只接收结构化摘要。
- **动作白名单**：建议仅允许 `hold`、轻微增减、轻微提前或延后。
- **力矩否决**：接近 `SafeTorque` 时禁止增加助力，并在更高风险下建议降助。
- **数据质量否决**：有效周期不足或信号不可靠时返回 `hold`，不强行给结论。
- **人工确认**：所有建议都带 `human_confirmation_required: true`。
- **控制隔离**：Agent 无权直接修改 Simulink/Speedgoat 参数或生成实时力矩。
- **可追溯性**：输出记录源指标、阈值、规则 ID、建议动作与否决原因。

## 快速演示

环境要求：Python 3.10+。

```powershell
python -m pip install -r requirements.txt
python scripts/run_trial_pipeline.py data/fixtures/synthetic_trial_001
```

运行后会在 `analysis_outputs/synthetic_trial_001/` 生成：

```text
gait_metrics.json           # 周期、相位、幅值、跟踪误差与力矩指标
parameter_suggestion.json   # 受约束动作、规则 ID 与安全否决原因
diagnostic_report.md        # 供工程师审核的试次诊断报告
```

运行最小回归检查：

```powershell
python scripts/test_trial_pipeline.py
```

## 技术选择

- **控制与采集**：MATLAB/Simulink、Speedgoat、File Log
- **分析与工具层**：Python、NumPy、Pandas、SciPy
- **Agent 数据接口**：JSON / Markdown 文件契约
- **需求与验收**：OpenSpec
- **研究资产**：开放元数据 API、结构化证据卡、论文矩阵

刻意没有引入复杂 Web 后台、向量数据库、多 Agent 框架或在线强化学习。对这个 MVP 来说，单 Agent + 确定性工具 + 文件化审计已经足够，也更容易验证。

## 仓库导航

```text
├─ TestStructure.slx           # 正式 Simulink 模型
├─ tools/                      # Speedgoat/Simulink 导出与检查工具
├─ scripts/                    # 数据、分析、建议、报告与调研脚本
├─ data/fixtures/              # 可提交、可复现的合成样例
├─ analysis_outputs/           # 示例指标、建议和报告
├─ docs/                       # 数据契约、开放决策与研究说明
├─ openspec/                   # 已验收的功能规格与变更记录
├─ notes/                      # 单篇论文的结构化证据笔记
├─ outputs/method_cards/       # 可复用的方法资产卡
├─ experiment/                 # 实验线约束
└─ paper/                      # 论文写作线与阶段稿件
```

参考论文原文、全文抽取缓存和潜在敏感的原始试次收件箱不会提交到仓库。

## 从原型到小型企业产品

下一阶段不需要先“做大平台”，而是补齐三条最短闭环：

1. 完成 `TestStructure.slx` 的真实信号映射和单位校验。
2. 用真实但匿名化的低风险试次标定阈值，并验证建议与专家判断的一致性。
3. 接入一个只允许调用白名单工具的 LLM 编排层，对同一批 JSON 输出评估格式正确率、规则遵守率和 unsupported claim rate。

当这些指标稳定后，再考虑权限系统、试次数据库和审核界面。真实硬件运行、人体实验和任何参数下发都必须由工程负责人确认，并遵守伦理、安全与数据管理要求。

## 项目结果

这个项目最终交付的不是“会聊天的外骨骼”，而是一条从控制试次到工程决策的可审计路径：

```text
原始日志 → 可信指标 → 受约束建议 → 人类审核 → 下一试次
```

它展示了 AI Agent 在小型企业里的一个更现实角色：不替代专业人员和安全控制器，而是把分散、重复、难追溯的研发流程变成可复现、可检查、可逐步自动化的工具链。

## 说明

本仓库用于工程研究与作品集展示，不构成医疗建议，也不宣称患者康复或临床疗效。当前研究不使用 EMG 或 IMU；历史端口名 `sEMGMuxIn` 实际承载足底压力/电压信号。
