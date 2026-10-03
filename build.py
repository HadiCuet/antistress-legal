#!/usr/bin/env python3
"""Builds index.html and support.html from the Markdown sources (headings, paragraphs, lists, bold, links)."""
import html, re

STYLE = """
  :root { --fg:#1c1c1e; --muted:#6b7280; --bg:#ffffff; --border:#e4e4e7; --accent:#1f8a8a; }
  @media (prefers-color-scheme: dark) { :root { --fg:#f4f4f5; --muted:#a1a1aa; --bg:#0b0b0c; --border:#27272a; --accent:#5cc8c8; } }
  * { box-sizing: border-box; }
  html, body { margin:0; padding:0; background:var(--bg); color:var(--fg);
    font:16px/1.65 -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, system-ui, sans-serif; -webkit-font-smoothing:antialiased; }
  main { max-width:760px; margin:0 auto; padding:48px 24px 80px; }
  h1 { font-size:2.1rem; line-height:1.2; letter-spacing:-0.02em; margin:0 0 16px; }
  h2 { font-size:1.25rem; margin:36px 0 10px; letter-spacing:-0.01em; }
  h3 { font-size:1rem; margin:22px 0 8px; color:var(--muted); font-weight:600; text-transform:uppercase; letter-spacing:0.04em; }
  a { color:var(--accent); }
  ul { padding-left:1.2em; }
  li { margin:6px 0; }
"""

def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text

def render(source, out):
    lines = open(source, encoding="utf-8").read().splitlines()
    body, in_list, title = [], False, ""
    for line in lines:
        if line.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{inline(line[2:])}</li>")
            continue
        if in_list:
            body.append("</ul>")
            in_list = False
        if line.startswith("# "):
            title = line[2:]
            body.append(f"<h1>{inline(title)}</h1>")
        elif line.startswith("## "):
            body.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("### "):
            body.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.strip():
            body.append(f"<p>{inline(line)}</p>")
    if in_list:
        body.append("</ul>")
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{STYLE}</style>
</head>
<body>
<main>
{chr(10).join(body)}
</main>
</body>
</html>
"""
    open(out, "w", encoding="utf-8").write(page)

render("privacy-policy.md", "index.html")
render("support.md", "support.html")
