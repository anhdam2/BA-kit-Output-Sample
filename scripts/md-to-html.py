#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
from pathlib import Path
import re

import markdown


HTML_TEMPLATE = """<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f7f5;
      --surface: #ffffff;
      --text: #1f2937;
      --muted: #6b7280;
      --border: #e5e7eb;
      --accent: #0f766e;
      --code-bg: #f3f4f6;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.6;
    }}
    main {{
      max-width: 980px;
      margin: 32px auto;
      padding: 40px 48px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      box-shadow: 0 12px 40px rgba(15, 23, 42, 0.06);
    }}
    header {{
      margin-bottom: 32px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--border);
    }}
    header p {{
      margin: 4px 0 0;
      color: var(--muted);
      font-size: 14px;
    }}
    h1, h2, h3, h4 {{ line-height: 1.25; }}
    h1 {{ margin-top: 0; }}
    a {{ color: var(--accent); }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }}
    th, td {{
      border: 1px solid var(--border);
      padding: 10px 12px;
      text-align: left;
      vertical-align: top;
    }}
    th {{ background: #f9fafb; }}
    code {{
      background: var(--code-bg);
      padding: 2px 6px;
      border-radius: 6px;
      font-size: 0.92em;
    }}
    pre {{
      background: #111827;
      color: #f9fafb;
      padding: 16px;
      border-radius: 12px;
      overflow-x: auto;
    }}
    blockquote {{
      margin: 20px 0;
      padding: 12px 16px;
      border-left: 4px solid var(--accent);
      background: #f0fdfa;
    }}
    img {{
      display: block;
      max-width: min(100%, 720px);
      width: auto;
      height: auto;
      margin: 24px auto;
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
      background: #fff;
    }}
    .mermaid {{
      margin: 24px 0;
      padding: 16px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: #fff;
      overflow-x: auto;
    }}
    ul, ol {{ padding-left: 24px; }}
  </style>
  <script type="module">
    import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
    mermaid.initialize({{
      startOnLoad: true,
      theme: "neutral",
      securityLevel: "loose",
      flowchart: {{ useMaxWidth: true, htmlLabels: true }}
    }});
  </script>
</head>
<body>
  <main>
    <header>
      <h1>{title}</h1>
      <p>Tài liệu BA xuất từ Markdown</p>
    </header>
    {body}
  </main>
</body>
</html>
"""


MERMAID_BLOCK_RE = re.compile(
    r"<pre><code class=\"language-mermaid\">(.*?)</code></pre>", re.DOTALL
)


def transform_special_blocks(body: str) -> str:
    def replace_mermaid(match: re.Match[str]) -> str:
        diagram = html.unescape(match.group(1)).strip()
        return f'<div class="mermaid">\n{diagram}\n</div>'

    return MERMAID_BLOCK_RE.sub(replace_mermaid, body)


def render_html(markdown_path: Path) -> Path:
    source = markdown_path.read_text(encoding="utf-8")
    body = markdown.markdown(
        source,
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
    )
    body = transform_special_blocks(body)
    title = markdown_path.stem
    html = HTML_TEMPLATE.format(title=title, body=body)
    target = markdown_path.with_suffix(".html")
    target.write_text(html, encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown_file")
    args = parser.parse_args()

    markdown_path = Path(args.markdown_file).resolve()
    if not markdown_path.exists():
      raise SystemExit(f"Missing input file: {markdown_path}")

    target = render_html(markdown_path)
    print(target)


if __name__ == "__main__":
    main()
