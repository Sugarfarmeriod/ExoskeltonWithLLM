"""Build a static HTML selector for TestStructure signal candidates."""

from __future__ import annotations

import html
import json
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATED_DIR = PROJECT_ROOT / "tools" / "generated"
INPUT_JSON = GENERATED_DIR / "teststructure_signal_candidates.json"
OUTPUT_HTML = GENERATED_DIR / "teststructure_signal_selector.html"


def main() -> int:
    payload = json.loads(INPUT_JSON.read_text(encoding="utf-8"))
    candidates = payload["candidates"]
    grouped: dict[str, list[dict]] = defaultdict(list)
    for candidate in candidates:
        grouped[candidate["group_path"]].append(candidate)

    html_text = render(payload, grouped)
    OUTPUT_HTML.write_text(html_text, encoding="utf-8")
    print(f"Wrote selector: {OUTPUT_HTML}")
    return 0


def render(payload: dict, grouped: dict[str, list[dict]]) -> str:
    total = payload["total_candidates"]
    recommended = sum(1 for item in payload["candidates"] if item["recommended"])
    groups_html = "\n".join(
        render_group(group_name, items)
        for group_name, items in sorted(grouped.items(), key=lambda kv: kv[0].lower())
    )
    data_json = json.dumps(payload["candidates"], ensure_ascii=False)
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>TestStructure 信号选择器</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f7f9;
      --panel: #ffffff;
      --ink: #1e242c;
      --muted: #647181;
      --line: #d8dde5;
      --accent: #1464d2;
      --accent-soft: #e9f1ff;
      --warn: #8a4b00;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font: 14px/1.45 "Segoe UI", "Microsoft YaHei", Arial, sans-serif;
    }}
    header {{
      position: sticky;
      top: 0;
      z-index: 10;
      background: rgba(255,255,255,.96);
      border-bottom: 1px solid var(--line);
      padding: 14px 22px;
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: 20px;
      font-weight: 650;
    }}
    .summary {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      color: var(--muted);
    }}
    .pill {{
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 2px 9px;
      background: #fff;
    }}
    .toolbar {{
      display: grid;
      grid-template-columns: minmax(220px, 1fr) auto auto auto auto;
      gap: 8px;
      margin-top: 12px;
      align-items: center;
    }}
    input[type="search"] {{
      width: 100%;
      padding: 9px 10px;
      border: 1px solid var(--line);
      border-radius: 6px;
      font: inherit;
    }}
    button {{
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      border-radius: 6px;
      padding: 8px 10px;
      cursor: pointer;
      font: inherit;
      white-space: nowrap;
    }}
    button.primary {{
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }}
    main {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) 360px;
      gap: 16px;
      padding: 16px 22px 28px;
    }}
    .group {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      margin-bottom: 12px;
      overflow: hidden;
    }}
    .group-head {{
      display: grid;
      grid-template-columns: auto 1fr auto auto;
      gap: 10px;
      align-items: center;
      padding: 10px 12px;
      background: #fbfcfe;
      border-bottom: 1px solid var(--line);
    }}
    .group-title {{
      font-weight: 650;
      overflow-wrap: anywhere;
    }}
    .group-count {{
      color: var(--muted);
      font-size: 12px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
    }}
    th, td {{
      border-bottom: 1px solid #edf0f4;
      padding: 8px 10px;
      vertical-align: top;
      text-align: left;
    }}
    th {{
      color: var(--muted);
      font-size: 12px;
      font-weight: 600;
      background: #fff;
    }}
    tr.recommended td {{
      background: var(--accent-soft);
    }}
    .path {{
      font-family: Consolas, "Cascadia Mono", monospace;
      font-size: 12px;
      overflow-wrap: anywhere;
    }}
    .signal-name {{
      font-weight: 600;
    }}
    .muted {{
      color: var(--muted);
    }}
    .keywords {{
      color: var(--warn);
      font-size: 12px;
    }}
    aside {{
      position: sticky;
      top: 116px;
      align-self: start;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
    }}
    textarea {{
      width: 100%;
      min-height: 360px;
      resize: vertical;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 9px;
      font: 12px/1.4 Consolas, "Cascadia Mono", monospace;
    }}
    .side-title {{
      font-weight: 650;
      margin-bottom: 8px;
    }}
    .hint {{
      color: var(--muted);
      font-size: 12px;
      margin: 8px 0;
    }}
    .hidden {{ display: none; }}
    @media (max-width: 980px) {{
      .toolbar {{ grid-template-columns: 1fr 1fr; }}
      main {{ grid-template-columns: 1fr; }}
      aside {{ position: static; }}
    }}
  </style>
</head>
<body>
<header>
  <h1>TestStructure 信号选择器</h1>
  <div class="summary">
    <span class="pill">模型: {escape(payload["model"])}</span>
    <span class="pill">候选信号: {total}</span>
    <span class="pill">关键词推荐: {recommended}</span>
    <span class="pill">生成时间: {escape(payload.get("generated_at", ""))}</span>
  </div>
  <div class="toolbar">
    <input id="search" type="search" placeholder="搜索信号名、模块路径、关键词，例如 Phi / Torque / DMP">
    <button onclick="showRecommendedOnly()">只看推荐</button>
    <button onclick="selectRecommended()">选择推荐</button>
    <button onclick="selectVisible(true)">选择当前筛选</button>
    <button onclick="selectVisible(false)">取消当前筛选</button>
    <button class="primary" onclick="updateOutput()">生成选择 JSON</button>
  </div>
</header>
<main>
  <section id="groups">
    {groups_html}
  </section>
  <aside>
    <div class="side-title">已选信号</div>
    <div id="selectedCount" class="hint">尚未生成</div>
    <textarea id="output" spellcheck="false"></textarea>
    <div class="hint">可以把这里的 JSON 发给我，或另存为后续 signal_map / File Log 接线清单。</div>
    <button class="primary" onclick="downloadSelection()">下载 selected_signals.json</button>
  </aside>
</main>
<script>
const candidates = {data_json};

function escapeLower(value) {{
  return String(value || '').toLowerCase();
}}

function rowText(row) {{
  return row.dataset.search || '';
}}

document.getElementById('search').addEventListener('input', () => {{
  const q = escapeLower(document.getElementById('search').value);
  document.querySelectorAll('tr.signal-row').forEach(row => {{
    row.classList.toggle('hidden', q && !rowText(row).includes(q));
  }});
  document.querySelectorAll('.group').forEach(group => {{
    const visible = group.querySelectorAll('tr.signal-row:not(.hidden)').length;
    group.classList.toggle('hidden', visible === 0);
  }});
}});

function groupToggle(groupId, checked) {{
  document.querySelectorAll(`[data-group="${{groupId}}"] input[type="checkbox"]`).forEach(cb => {{
    if (!cb.closest('tr').classList.contains('hidden')) cb.checked = checked;
  }});
  updateOutput();
}}

function selectRecommended() {{
  document.querySelectorAll('input.signal-check').forEach(cb => {{
    const item = candidates.find(x => x.id === cb.value);
    cb.checked = Boolean(item && item.recommended);
  }});
  updateOutput();
}}

function showRecommendedOnly() {{
  document.getElementById('search').value = '';
  document.querySelectorAll('tr.signal-row').forEach(row => {{
    row.classList.toggle('hidden', !row.classList.contains('recommended'));
  }});
  document.querySelectorAll('.group').forEach(group => {{
    const visible = group.querySelectorAll('tr.signal-row:not(.hidden)').length;
    group.classList.toggle('hidden', visible === 0);
  }});
}}

function selectVisible(checked) {{
  document.querySelectorAll('tr.signal-row:not(.hidden) input.signal-check').forEach(cb => cb.checked = checked);
  updateOutput();
}}

function selectedItems() {{
  const ids = new Set(Array.from(document.querySelectorAll('input.signal-check:checked')).map(cb => cb.value));
  return candidates.filter(item => ids.has(item.id));
}}

function updateOutput() {{
  const selected = selectedItems();
  document.getElementById('selectedCount').textContent = `已选 ${{selected.length}} 个信号`;
  document.getElementById('output').value = JSON.stringify({{
    model: '{escape_js(payload["model"])}',
    selected_count: selected.length,
    selected_signals: selected
  }}, null, 2);
}}

function downloadSelection() {{
  updateOutput();
  const blob = new Blob([document.getElementById('output').value], {{type: 'application/json;charset=utf-8'}});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'selected_signals.json';
  a.click();
  URL.revokeObjectURL(url);
}}

updateOutput();
</script>
</body>
</html>"""


def render_group(group_name: str, items: list[dict]) -> str:
    group_id = safe_id(group_name)
    rows = "\n".join(render_row(item, group_id) for item in items)
    recommended = sum(1 for item in items if item["recommended"])
    return f"""
<article class="group">
  <div class="group-head">
    <input type="checkbox" onchange="groupToggle('{group_id}', this.checked)" title="批量选择本组当前可见信号">
    <div>
      <div class="group-title">{escape(group_name)}</div>
      <div class="group-count">{len(items)} 个候选，{recommended} 个关键词推荐</div>
    </div>
    <button onclick="groupToggle('{group_id}', true)">本组全选</button>
    <button onclick="groupToggle('{group_id}', false)">本组清空</button>
  </div>
  <table>
    <thead>
      <tr>
        <th>选</th>
        <th>信号/源模块</th>
        <th>来源路径</th>
        <th>去向</th>
      </tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
  </table>
</article>"""


def render_row(item: dict, group_id: str) -> str:
    keywords = ", ".join(item.get("keyword_hits", []))
    signal = item.get("signal_name") or "(未命名信号)"
    search = " ".join(
        [
            signal,
            item.get("source_block", ""),
            item.get("source_block_type", ""),
            keywords,
            " ".join(item.get("destination_blocks", [])),
        ]
    ).lower()
    row_class = "signal-row recommended" if item["recommended"] else "signal-row"
    checked = ""
    return f"""
<tr class="{row_class}" data-group="{group_id}" data-search="{escape(search)}">
  <td><input class="signal-check" type="checkbox" value="{escape(item["id"])}" {checked} onchange="updateOutput()"></td>
  <td>
    <div class="signal-name">{escape(signal)}</div>
    <div class="muted">{escape(item.get("source_name", ""))} · {escape(item.get("source_block_type", ""))} · port {escape(str(item.get("source_port", "")))}</div>
    <div class="keywords">{escape(keywords)}</div>
  </td>
  <td class="path">{escape(item.get("source_block", ""))}</td>
  <td>
    <div>{escape(str(item.get("destination_count", 0)))} 个目标</div>
    <div class="path muted">{escape(" | ".join(item.get("destination_blocks", [])[:3]))}</div>
  </td>
</tr>"""


def escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def escape_js(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace("'", "\\'")


def safe_id(value: str) -> str:
    return "g_" + "".join(ch if ch.isalnum() else "_" for ch in value)[:80]


if __name__ == "__main__":
    raise SystemExit(main())
