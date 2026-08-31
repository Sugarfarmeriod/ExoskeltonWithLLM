## Why

本项目需要一条可复现的路径，把膝关节外骨骼直线行走试验数据转化为可审计的低频参数建议。当前方向应避免让 LLM 进入实时控制闭环，而是把确定性步态分析工具、受约束参数建议规则和报告生成流程正式化，用于后续 Simulink/Speedgoat 离线回放验证和论文撰写。

## What Changes

- 新增试次分析能力：读取导出的行走数据，并生成结构化步态、跟踪和力矩指标。
- 新增 Speedgoat 数据采集能力：在 Simulink Real-Time 模型中标记关键记录信号，通过目标机 File Log 或等价正规机制把试次数据下载到主机。
- 新增受约束参数建议能力：根据指标为 DMP、助力和阻抗参数生成保守建议。
- 新增面向 LLM 的诊断报告能力：只消费结构化工具输出，生成可追溯报告，不直接控制外骨骼。
- 所有参数更新都必须保留人工确认环节；系统不得直接写入力矩命令，也不得绕过现有安全限制。
- 保留已有文献检索与整理流程；本次 change 聚焦路线图中提出的实验与工具实现主线。

## Capabilities

### New Capabilities

- `trial-gait-analysis`：读取试次数据、检测步态事件、切分步态周期、构建参考模板、对齐患侧与参考侧，并计算结构化指标。
- `speedgoat-data-capture`：配置、启动、停止和下载 Speedgoat/Simulink Real-Time 试次记录数据，并生成可被试次分析读取的本地文件。
- `constrained-parameter-suggestion`：基于数据质量和力矩安全约束，为 `phase_offset`、`Amplitude`、助力增益、`MO_Kp` 和 `MO_Kd` 生成有边界的建议。
- `llm-diagnostic-reporting`：根据指标和规则输出生成可读报告，同时防止无证据结论和直接控制行为。

### Modified Capabilities

- 无。

## Impact

- 影响目录：`scripts/`、`outputs/`、`analysis_outputs/` 以及未来的试次数据目录。
- 影响产物：结构化 JSON 摘要、参数建议 JSON、诊断 Markdown 报告和验证输出。
- 外部系统：MATLAB/Simulink 与 Speedgoat 仍然只是下游人工确认后的执行目标；本次 change 不修改实时控制代码。
- 依赖：继续优先使用 Python 实现确定性工具；后续可在 Simulink 回放或 `.slx` 集成检查中使用 MATLAB。
