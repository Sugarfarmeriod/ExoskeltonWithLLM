from __future__ import annotations

from pathlib import Path

from pipeline_utils import (
    RAW,
    classify_paper,
    clean_text,
    ensure_dirs,
    load_json,
    note_filename,
    pdf_status_for,
    save_json,
    wrap_md,
)


def build_note(paper: dict) -> str:
    text = ""
    declared_text_path = paper.get("text_cache_path") or paper.get("text_path")
    if declared_text_path and Path(declared_text_path).is_file():
        text = Path(declared_text_path).read_text(encoding="utf-8", errors="ignore")
    cls = classify_paper(paper, text)
    paper.update(cls)
    status = pdf_status_for(paper)
    evidence = "PDF" if status.endswith("_pdf") else ("abstract only" if paper.get("abstract") else "metadata only")
    abstract = clean_text(paper.get("abstract"))
    return f"""# {clean_text(paper.get('title'))}

## 1. 题目、作者、年份、期刊/会议、DOI

- 题目：{clean_text(paper.get('title'))}
- 作者：{clean_text(paper.get('authors')) or '未提供'}
- 年份：{paper.get('year') or '未提供'}
- 期刊/会议：{clean_text(paper.get('venue')) or '未提供'}
- DOI：{clean_text(paper.get('doi')) or '未提供'}
- URL：{clean_text(paper.get('url')) or '未提供'}
- PDF 状态：{status}

## 2. 一句话结论

{cls['why_relevant']}

## 3. AI 插入位置

{cls['ai_role']}

## 4. 控制底座

{cls['control_base']}

## 5. 输入数据

{cls['sensors']}

## 6. 输出参数

{cls['optimized_parameters']}

## 7. 目标函数或评价指标

{cls['objective']}；指标：{cls['metrics']}

## 8. 实验对象和实验任务

{cls['subjects']}

## 9. 与本项目的相似点

- 可按 AO/Phi/Phase0Event、DMP 参数、MO_Kp/MO_Kd、Torque_Guard/SafeTorque 和足底压力/膝角度/膝速度/膝力矩逐项映射。
- 当前自动判断：{cls['why_relevant']}

## 10. 本项目可借鉴点

- 优先把 AI 放在低频参数优化或状态估计层，而不是直接替代实时力矩闭环。
- 若论文涉及时机、强度、阻抗或相位，可转写成 `phase_offset`、`Amplitude`、`tau`、`MO_Kp`、`MO_Kd`、`SafeTorque` 的实验变量。

## 11. 不适合照搬的地方

- 摘要/元数据无法确认的受试者数量、硬件依赖和评价指标，必须等 PDF 全文或人工阅读后再写入。
- 若依赖 EMG、IMU、代谢仪或动作捕捉，需降级为方法/目标函数参考，不作为本论文系统实现前提。

## 12. 证据来源

{evidence}

## 13. 语义/治疗师输入扩展记录

- 输入类型：{cls['semantic_input_type']}
- 输出类型：{cls['semantic_output_type']}
- 是否真实机器人闭环：{cls['robot_closed_loop']}
- 与本项目参数映射：{cls['parameter_mapping']}
- 实现难度：{cls['implementation_difficulty']}
- 是否适合 1-2 个月快速成稿：{cls['quick_paper_fit']}

## Abstract / Metadata Evidence

{wrap_md(abstract)}
"""


def main() -> None:
    ensure_dirs()
    papers = load_json(RAW / "papers_with_pdf_status.json", load_json(RAW / "search_results.json", []))
    count = 0
    for paper in papers:
        note = build_note(paper)
        path = note_filename(paper)
        path.write_text(note, encoding="utf-8")
        paper["note_path"] = str(path)
        count += 1
    save_json(RAW / "papers_with_pdf_status.json", papers)
    print(f"notes={count}")


if __name__ == "__main__":
    main()
