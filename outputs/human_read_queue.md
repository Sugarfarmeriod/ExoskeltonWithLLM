# 最小阅读队列

目标不是读完论文，而是能向老师解释 5 个关键方法。每篇只需 5～10 分钟。

## 1. Power Knee：膝关节力矩不对称度

- 看：[方法卡](method_cards/01_power_knee.md)
- PDF： [本地全文](../papers/2025_The_clinical_effects_of_the_Ossur_Power_Knee_10.1186_s12984-025-01729-2.pdf)
- 只看 PDF 第 5～7 页，重点是第 6 页公式 (2)。
- 看完应能回答：`DoA_tau = 0` 表示什么？为什么不能直接用单侧 `tau_e` 代替人体膝关节力矩？
- 状态：`ai_extracted`

## 2. DMP + 贝叶斯优化：外骨骼数值工具

- 看：[方法卡](method_cards/02_dmp_bayesian_optimization.md)
- PDF： [本地全文](../papers/2024_Learning_to_Assist_Different_Wearers_in_Multitasks_Efficient_and_Indiv_10.1109_tro.2024.3468768.pdf)
- 只看 PDF 第 7、14、18 页，重点是公式 (31) 和 Algorithm 2。
- 看完应能回答：优化器输入什么、评价什么、多久更新一次？
- 状态：`ai_extracted`

## 3. Code as Policies：LLM 怎样调用工具

- 看：[方法卡](method_cards/03_code_as_policies.md)
- PDF： [本地全文](../papers/2023_Code_as_Policies_Language_Model_Programs_for_Embodied_Control.pdf)
- 只看 PDF 第 3～5 页。
- 看完应能回答：为什么 LLM 需要通过预定义 API 接触机器人？
- 状态：`ai_extracted`

## 4. Inner Monologue：反馈怎样进入 Agent

- 看：[方法卡](method_cards/04_inner_monologue.md)
- PDF： [本地全文](../papers/2023_Inner_Monologue_Embodied_Reasoning_through_Planning_with_Language_Models.pdf)
- 只看 PDF 第 2、4、7 页。
- 看完应能回答：什么反馈触发重试，什么反馈触发重新规划？
- 状态：`ai_extracted`

## 5. Safety Chip：谁拥有安全裁决权

- 看：[方法卡](method_cards/05_safety_chip.md)
- PDF： [本地全文](../papers/2024_Plug_in_the_Safety_Chip_Enforcing_Constraints_for_LLM_driven_Robot_Agents.pdf)
- 只看 PDF 第 1、3～4 页。
- 看完应能回答：为什么不能只在提示词里告诉 LLM “注意安全”？
- 状态：`ai_extracted`

