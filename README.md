# ExoskeletonWithLLM Literature Pipeline

本项目用于检索、筛选、下载、阅读和整理“AI 如何融入膝关节外骨骼 DMP-阻抗控制框架”的科研论文。重点判断 AI 应该接入现有 MATLAB/Simulink + Speedgoat 链路的哪一层，而不是泛泛总结 AI 外骨骼。

当前论文实验范围：导师规划招募 8 名健康受试者，开展工程可行性、控制性能和个体化参数优化验证；系统及论文不使用 EMG 或 IMU，不宣称患者康复或临床疗效。

> 回到论文写作主线时，请先阅读 [`PAPER_START_HERE.md`](PAPER_START_HERE.md)。该文件汇总当前事实边界、论文定位、ARS 阶段、材料阅读顺序和下一写作门槛。

## 目录

- `queries.md`：检索关键词，每行一个 query。
- `scripts/`：最小可运行 Python 流程。
- `outputs/raw_metadata/`：开放元数据 API 返回和中间状态。
- `outputs/manual_download.csv`：需要用户手动下载的论文清单。
- `papers/`：已归档 PDF。
- `papers/inbox/`：用户手动下载 PDF 的临时放置目录。
- `outputs/pdf_text/`：PDF 抽取文本。
- `notes/`：单篇结构化 Markdown 笔记。
- `outputs/paper_matrix.csv`：论文矩阵。
- `outputs/top_10_must_read.md`：最优先阅读论文。
- `outputs/research_routes.md`：AI 融入路线建议。
- `outputs/rejected_or_low_priority.md`：低优先级论文。

## 安装依赖

```powershell
python -m pip install -r requirements.txt
```

## 重新检索并更新全部结果

```powershell
python scripts/search_papers.py --limit 50
python scripts/download_pdfs.py --limit 50
python scripts/retry_manual_downloads.py
python scripts/download_known_pdfs.py
python scripts/ingest_manual_pdfs.py
python scripts/extract_pdf_text.py
python scripts/build_notes.py
python scripts/build_matrix.py
python scripts/rank_routes.py
```

## 新增关键词

直接编辑 `queries.md`，每行一个检索式。脚本会优先使用这些关键词，并在 `outputs/expanded_keywords.md` 记录脚本额外用于评分和识别的同义词。

## 手动下载 PDF

如果 `outputs/manual_download.csv` 中记录了需要登录、验证码、机构认证或下载失败的论文，请通过学校图书馆或出版社页面合法下载 PDF，并放入：

```text
papers/inbox/
```

然后运行：

```powershell
python scripts/ingest_manual_pdfs.py
python scripts/extract_pdf_text.py
python scripts/build_notes.py
python scripts/build_matrix.py
python scripts/rank_routes.py
```

脚本会尽量根据 DOI、标题和年份重命名并移动到 `papers/`。

## 补救下载

`scripts/retry_manual_downloads.py` 会对 `outputs/manual_download.csv` 中未下载的论文补查 OpenAlex、Unpaywall、Semantic Scholar 元数据、PMC 和 DOI 落地页，只接受正规来源直接返回的 PDF。

`scripts/download_known_pdfs.py` 保存少量经人工检索确认的正规开放/机构仓储直链，例如 Cambridge Core、arXiv、DLR eLib、Edinburgh PURE、NSF PAR 等。可以继续向脚本里的 `KNOWN_URLS` 字典补充 DOI 到 PDF URL 的映射。

## PDF 获取边界

流程只尝试开放 PDF 和当前网络可直接合法访问的 PDF。遇到 403、登录页、验证码、Cloudflare 或机构认证跳转时，脚本不会继续硬爬，会写入 `outputs/manual_download.csv` 等待手动下载。禁止使用 Sci-Hub 或其他非法来源，禁止保存账号、cookie、token 或登录凭证。

## Speedgoat 试次分析流程

当前第一版实验数据流程是：

```text
SLRT Explorer 运行试次
-> tools/import_slrt_filelog_trial.m 归档 File Log
-> Python 校验试次 schema
-> Python 生成 gait_metrics.json
-> Python 生成 parameter_suggestion.json
-> Python 生成 diagnostic_report.md
```

规范输入格式见：

```text
docs/trial_data_schema.md
```

待确认阈值、参考源和参数映射见：

```text
docs/open_decisions.md
```

校验合成试次：

```powershell
python scripts/check_trial_data.py data/fixtures/synthetic_trial_001
```

运行完整合成流程：

```powershell
python scripts/run_trial_pipeline.py data/fixtures/synthetic_trial_001
```

单步运行：

```powershell
python scripts/analyze_trial.py data/fixtures/synthetic_trial_001 --output analysis_outputs/synthetic_trial_001/gait_metrics.json
python scripts/suggest_parameters.py analysis_outputs/synthetic_trial_001/gait_metrics.json --output analysis_outputs/synthetic_trial_001/parameter_suggestion.json
python scripts/generate_report.py analysis_outputs/synthetic_trial_001/gait_metrics.json analysis_outputs/synthetic_trial_001/parameter_suggestion.json --output analysis_outputs/synthetic_trial_001/diagnostic_report.md
```

运行聚焦测试：

```powershell
python scripts/test_trial_pipeline.py
```
