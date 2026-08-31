# 论文方法资产入口

这套材料用于替代“逐篇从头精读”。Codex 负责阅读全文并提取方法，用户只审核关键证据页。

## 使用顺序

1. 先看 [最小阅读队列](human_read_queue.md)。
2. 每次只打开一张 [方法卡](method_cards/)。
3. 需要确认时，只查看卡片标出的 PDF 页。
4. 写论文时，从 [方法资产矩阵](method_asset_matrix.csv) 检索公式、实验协议和 Agent 工具。

## 阅读状态

- `ai_extracted`：已从本地 PDF 提取并记录页码，用户尚未核对。
- `user_checked_pages`：用户看过卡片指定的证据页。
- `human_read`：用户确实完整读过全文。

当前首批 5 篇均为 `ai_extracted`，不能表述为用户已经精读。

## 首批覆盖

| 论文 | 主要用途 |
| --- | --- |
| Power Knee clinical effects | 膝关节力矩不对称度、重复测量统计 |
| Learning to Assist Different Wearers | DMP、贝叶斯优化、异常评价 |
| Code as Policies | LLM 调用白名单 API |
| Inner Monologue | 试次反馈、失败重试与重新规划 |
| Safety Chip | 独立安全裁决与拒绝后重规划 |

