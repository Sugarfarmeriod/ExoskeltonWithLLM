# 方法卡 05：独立安全裁决

## 你只需要记住

- Safety Chip 将安全约束放在 LLM Agent 外部。
- 独立监视器验证并屏蔽不安全动作，再把违反原因返回给 LLM。
- 只在提示词中写“注意安全”不能提供可验证保证。

## 在本项目中怎么用

定义拥有否决权的确定性工具：

```text
check_constraints(candidate_parameters, trial_quality, torque_metrics)
```

至少检查参数上下界、单次变化幅度、试次质量、力矩安全余量和人工确认状态。输出只能是：

```text
accepted
rejected + reason_codes
```

LLM 不能覆盖拒绝结果，`Torque_Guard` 仍保留执行阶段的最终保护。

## 证据

- PDF 第 1 页：安全模块的研究动机。
- PDF 第 3 页：constraint monitor 验证并剪除 Agent 动作。
- PDF 第 4 页：将违反原因反馈给 LLM 重新规划。

## 老师问时怎么说

“LLM 只有提案权，没有安全裁决权；参数检查由独立程序完成，被拒绝后 Agent 只能根据原因重新给方案。”

## 不要说

- 不要声称 LLM 自己能够保证外骨骼安全。
- 不必直接照搬论文的 LTL，实现可先采用经过验证的数值边界和状态规则。
