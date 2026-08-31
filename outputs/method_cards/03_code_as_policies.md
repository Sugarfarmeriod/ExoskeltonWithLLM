# 方法卡 03：Code as Policies

## 你只需要记住

- LLM 不直接产生底层控制量，而是生成调用已有感知和控制 API 的程序。
- 预定义 API 把语言模型限制到机器人真实具备的能力。
- 分层函数组合可以把复杂任务拆成多个可复用子功能。

## 在本项目中怎么用

不允许 LLM 任意生成并执行 Python 代码，只允许结构化调用白名单工具：

```text
validate_trial
analyze_trial
compare_trials
optimize_parameters
check_constraints
build_next_trial_plan
```

每个工具必须有固定输入 schema、输出 schema 和权限说明。

## 证据

- PDF 第 3 页：语言模型程序调用感知模块和控制 primitive API。
- PDF 第 4～5 页：分层函数生成与实验说明。

## 老师问时怎么说

“我借鉴的是 LLM 调用已有 API 的分层结构，不是让大模型直接写外骨骼控制代码。底层工具仍然是可测试的确定性程序。”

## 不要说

- 不要把论文的任意代码生成原样用于安全关键系统。
- 不要声称机械臂实验已经证明外骨骼效果。

