#!/usr/bin/env python3
"""Render the WRFCoin wiki to a single browsable HTML page.

Walks ``wiki/**/*.md``, parses YAML frontmatter, renders markdown to HTML,
resolves ``[[wikilinks]]`` to in-page anchors, and ships a self-contained
sidebar + content layout at ``site/wiki.html`` so the sibling library bridge's
``wiki.html#<anchor>`` links resolve.

Anchors are folder-slash-flattened to match the library's link scheme:
``protocol/architecture`` → ``protocol-architecture``.

The renderer is intentionally minimal: no PyYAML, no markdown library. It
handles enough of CommonMark + Obsidian-style ``[[wikilinks]]`` to be useful
for this wiki without adding dependencies.

Usage:
    python3 scripts/generate_wiki.py
    python3 scripts/generate_wiki.py --wiki /path/to/wiki --output /path/to/wiki.html
"""

from __future__ import annotations

import argparse
import html as _html
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
WIKI_ROOT  = SCRIPT_DIR.parent
REPO_ROOT = WIKI_ROOT.parent
DEFAULT_OUTPUT = REPO_ROOT / "site" / "wiki.html"

# Skip these — they are operating guides / logs, rendered separately at the end.
SECONDARY_FILES = {"AGENTS.md", "log.md"}

# Directory order in the sidebar.
GROUP_ORDER = [
    "framing", "protocol", "economics", "implementation",
    "governance", "release", "synthesis", "sources",
]
GROUP_NUMERAL = {
    "framing": "i", "protocol": "ii", "economics": "iii", "implementation": "iv",
    "governance": "v", "release": "vi", "synthesis": "vii", "sources": "viii",
}


# ── frontmatter (minimal YAML; no PyYAML dep) ─────────────────────────────────

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    fm_raw = m.group(1)
    body = text[m.end():]
    data: dict = {}
    current_key: str | None = None
    current_list: list | None = None
    for line in fm_raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        # list item (two-space indent + dash)
        if line.startswith("  - "):
            val = line[4:].strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            if current_list is None and current_key is not None:
                current_list = []
                data[current_key] = current_list
            if current_list is not None:
                current_list.append(val)
            continue
        # nested dict key under a list item (4-space indent) — flatten into preceding string
        if line.startswith("    ") and current_list and current_list and isinstance(current_list[-1], str):
            current_list[-1] = current_list[-1] + " · " + line.strip()
            continue
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if not val:
                current_key = key
                current_list = None
                data[key] = []
                continue
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                items = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
                data[key] = items
            elif val.startswith('"') and val.endswith('"'):
                data[key] = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                data[key] = val[1:-1]
            else:
                data[key] = val
            current_key = None
            current_list = None
    return data, body


# ── markdown → HTML (minimal) ─────────────────────────────────────────────────

_WIKILINK_RE    = re.compile(r"\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]")
_LINK_RE        = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_BOLD_RE        = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC_RE      = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")


def path_to_anchor(rel_path: str) -> str:
    """Match the library generator's anchor scheme: folder/slug → folder-slug."""
    p = rel_path[:-3] if rel_path.endswith(".md") else rel_path
    return p.replace("/", "-")


def heading_slug(s: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", s.lower()).strip("-")


def render_inline(s: str, page_index: dict[str, str]) -> str:
    # Pull out inline-code spans first so their contents are escaped but unmolested by other rules.
    spans: list[str] = []
    def _stash(m: re.Match) -> str:
        spans.append(_html.escape(m.group(1)))
        return f"\x00CODE{len(spans)-1}\x00"
    s = _INLINE_CODE_RE.sub(_stash, s)
    s = _html.escape(s, quote=False)

    def _wikilink(m: re.Match) -> str:
        target = m.group(1).strip()
        label  = (m.group(2) or target).strip()
        # try multiple lookup forms
        key = target.replace(".md", "")
        anchor = page_index.get(key) or page_index.get(key.split("/")[-1])
        if anchor:
            return f'<a class="wikilink" href="#{anchor}">{_html.escape(label)}</a>'
        return f'<a class="wikilink broken" href="#" title="No page found for {_html.escape(target)}">{_html.escape(label)}</a>'

    s = _WIKILINK_RE.sub(_wikilink, s)
    s = _LINK_RE.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = _BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", s)
    s = _ITALIC_RE.sub(lambda m: f"<em>{m.group(1)}</em>", s)

    # Restore code spans.
    for i, span in enumerate(spans):
        s = s.replace(f"\x00CODE{i}\x00", f"<code>{span}</code>")
    return s


def render_markdown(body: str, page_index: dict[str, str]) -> str:
    lines = body.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    code_lang = ""
    code_buf: list[str] = []
    list_stack: list[str] = []

    def close_lists() -> None:
        while list_stack:
            out.append(f"</{list_stack.pop()}>")

    while i < len(lines):
        line = lines[i]
        # fenced code
        if line.startswith("```"):
            if in_code:
                lang_class = f' class="lang-{code_lang}"' if code_lang else ""
                out.append(f"<pre><code{lang_class}>" + _html.escape("\n".join(code_buf)) + "</code></pre>")
                code_buf = []
                code_lang = ""
                in_code = False
            else:
                close_lists()
                code_lang = line[3:].strip()
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_lists()
            level = len(m.group(1))
            raw = m.group(2).strip()
            text = render_inline(raw, page_index)
            anchor = heading_slug(raw)
            out.append(f'<h{level} id="{anchor}">{text}</h{level}>')
            i += 1
            continue
        # blockquote
        if line.startswith("> "):
            close_lists()
            out.append(f"<blockquote>{render_inline(line[2:], page_index)}</blockquote>")
            i += 1
            continue
        # horizontal rule
        if re.match(r"^---+\s*$", line):
            close_lists()
            out.append("<hr>")
            i += 1
            continue
        # unordered list
        m = re.match(r"^(\s*)-\s+(.*)$", line)
        if m:
            if not list_stack or list_stack[-1] != "ul":
                close_lists()
                out.append("<ul>")
                list_stack.append("ul")
            out.append(f"<li>{render_inline(m.group(2), page_index)}</li>")
            i += 1
            continue
        # ordered list
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            if not list_stack or list_stack[-1] != "ol":
                close_lists()
                out.append("<ol>")
                list_stack.append("ol")
            out.append(f"<li>{render_inline(m.group(1), page_index)}</li>")
            i += 1
            continue
        # blank
        if not line.strip():
            close_lists()
            i += 1
            continue
        # table — minimal: detect | sep | line then expect a delimiter row
        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?[\s\-|:]+\|?\s*$", lines[i + 1]):
            close_lists()
            header_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append("<table><thead><tr>" + "".join(
                f"<th>{render_inline(c, page_index)}</th>" for c in header_cells
            ) + "</tr></thead><tbody>")
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                row_cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>" + "".join(
                    f"<td>{render_inline(c, page_index)}</td>" for c in row_cells
                ) + "</tr>")
                i += 1
            out.append("</tbody></table>")
            continue
        # paragraph
        close_lists()
        para_lines = [line]
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if (not nxt.strip()
                    or nxt.startswith("#")
                    or nxt.startswith("```")
                    or nxt.startswith("> ")
                    or re.match(r"^---+\s*$", nxt)
                    or re.match(r"^\s*-\s+", nxt)
                    or re.match(r"^\s*\d+\.\s+", nxt)):
                break
            para_lines.append(nxt)
            j += 1
        para = " ".join(l.strip() for l in para_lines)
        out.append(f"<p>{render_inline(para, page_index)}</p>")
        i = j
    close_lists()
    return "\n".join(out)


# ── wiki walk ─────────────────────────────────────────────────────────────────

def collect_pages(wiki_root: Path) -> list[dict]:
    pages: list[dict] = []
    if not wiki_root.exists():
        return pages
    for md in sorted(wiki_root.rglob("*.md")):
        rel = md.relative_to(wiki_root).as_posix()
        if rel.startswith("."):
            continue
        text = md.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        rel_no_ext = rel[:-3] if rel.endswith(".md") else rel
        anchor = path_to_anchor(rel)

        # derive wiki_type
        if "/" in rel:
            default_type = rel.split("/")[0]
        else:
            default_type = "framing"
        page_type = fm.get("wiki_type") or default_type

        status = fm.get("status") or "stub"
        title  = fm.get("title") or rel_no_ext.split("/")[-1].replace("-", " ").title()

        sources = fm.get("sources") or []
        oqs     = fm.get("open_questions") or []
        source_count = len(sources) if isinstance(sources, list) else int(sources or 0)
        oq_count     = len(oqs) if isinstance(oqs, list) else int(oqs or 0)

        pages.append({
            "rel": rel,
            "rel_no_ext": rel_no_ext,
            "anchor": anchor,
            "title": title,
            "wiki_type": page_type,
            "status": status,
            "last_updated": fm.get("last_ingest") or fm.get("last_updated") or "",
            "review_due": fm.get("review_due") or "",
            "tags": fm.get("tags") or [],
            "crosslinks": fm.get("crosslinks") or [],
            "source_count": source_count,
            "open_questions": oq_count,
            "body": body,
            "fm": fm,
            "is_secondary": md.name in SECONDARY_FILES,
        })
    return pages


# ── HTML emit ─────────────────────────────────────────────────────────────────

STATUS_LABEL = {
    "active": "active",
    "stub": "stub",
    "review-needed": "review",
    "stale": "stale",
    "missing": "missing",
}


def build_html(pages: list[dict], generated_at: str) -> str:
    # Anchor lookup table for [[wikilinks]] resolution.
    page_index: dict[str, str] = {}
    for p in pages:
        page_index[p["rel_no_ext"]] = p["anchor"]
        # also accept leaf-only references
        leaf = p["rel_no_ext"].split("/")[-1]
        page_index.setdefault(leaf, p["anchor"])

    # Group pages by wiki_type for sidebar nav.
    groups: dict[str, list[dict]] = {}
    for p in pages:
        if p["is_secondary"]:
            continue
        groups.setdefault(p["wiki_type"], []).append(p)
    secondary = [p for p in pages if p["is_secondary"]]

    # Sidebar
    nav_parts: list[str] = ['<nav class="wiki-nav" aria-label="Wiki contents">']
    for group_name in GROUP_ORDER:
        if group_name not in groups:
            continue
        numeral = GROUP_NUMERAL.get(group_name, "")
        entries = sorted(groups[group_name], key=lambda x: x["title"].lower())
        nav_parts.append(
            f'<div class="nav-group" data-type="{_html.escape(group_name)}">'
            f'<div class="nav-label"><span class="nav-numeral">{numeral}</span>{_html.escape(group_name)}</div>'
        )
        for p in entries:
            status = p["status"]
            nav_parts.append(
                f'<a class="nav-item" href="#{p["anchor"]}" '
                f'data-status="{_html.escape(status)}" '
                f'data-search="{_html.escape((p["title"] + " " + " ".join(p["tags"])).lower())}">'
                f'<span class="nav-title">{_html.escape(p["title"])}</span>'
                f'<span class="nav-meta">'
                f'<span class="status-dot status-{_html.escape(status)}" title="{_html.escape(status)}"></span>'
                f'<span class="nav-q">{p["open_questions"]}Q</span>'
                f'</span></a>'
            )
        nav_parts.append("</div>")
    # also any uncategorized groups appended after the canonical order
    for group_name, entries in groups.items():
        if group_name in GROUP_ORDER:
            continue
        nav_parts.append(
            f'<div class="nav-group" data-type="{_html.escape(group_name)}">'
            f'<div class="nav-label">{_html.escape(group_name)}</div>'
        )
        for p in sorted(entries, key=lambda x: x["title"].lower()):
            nav_parts.append(
                f'<a class="nav-item" href="#{p["anchor"]}">'
                f'<span class="nav-title">{_html.escape(p["title"])}</span>'
                f'</a>'
            )
        nav_parts.append("</div>")
    if secondary:
        nav_parts.append('<div class="nav-group nav-group-secondary"><div class="nav-label">supporting</div>')
        for p in secondary:
            nav_parts.append(
                f'<a class="nav-item" href="#{p["anchor"]}"><span class="nav-title">{_html.escape(p["title"])}</span></a>'
            )
        nav_parts.append("</div>")
    nav_parts.append("</nav>")
    nav_html = "\n".join(nav_parts)

    # Content
    article_parts: list[str] = []
    for p in pages:
        rendered = render_markdown(p["body"], page_index)
        status   = p["status"]
        tags_html = "".join(
            f'<span class="tag">{_html.escape(t)}</span>' for t in (p["tags"] or [])
        )
        meta_pills = (
            f'<span class="meta-pill"><span class="status-dot status-{_html.escape(status)}"></span>{_html.escape(STATUS_LABEL.get(status, status))}</span>'
            f'<span class="meta-pill mono">{p["source_count"]} sources</span>'
            f'<span class="meta-pill mono">{p["open_questions"]} open Q</span>'
        )
        if p["last_updated"]:
            meta_pills += f'<span class="meta-pill mono">updated {_html.escape(p["last_updated"])}</span>'
        if p["review_due"]:
            meta_pills += f'<span class="meta-pill mono review">review {_html.escape(p["review_due"])}</span>'

        article_parts.append(
            f'<article class="page" id="{p["anchor"]}" '
            f'data-type="{_html.escape(p["wiki_type"])}" data-status="{_html.escape(status)}">'
            f'<header class="page-head">'
            f'<div class="page-kicker">{_html.escape(p["wiki_type"])} · <code>{_html.escape(p["rel"])}</code></div>'
            f'<h1 class="page-title">{_html.escape(p["title"])}</h1>'
            f'<div class="page-meta">{meta_pills}</div>'
            + (f'<div class="page-tags">{tags_html}</div>' if tags_html else '')
            + '</header>'
            f'<div class="page-body">{rendered}</div>'
            f'</article>'
        )
    content_html = "\n".join(article_parts)

    total           = len(pages)
    active          = sum(1 for p in pages if p["status"] == "active")
    sources_total   = sum(p["source_count"] for p in pages)
    questions_total = sum(p["open_questions"] for p in pages)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>The WRFCoin Wiki</title>
  <link rel="stylesheet" href="assets/library.css">
  <link rel="stylesheet" href="assets/wiki.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Syne:wght@400;500;600;700;800&family=DM+Sans:opsz,wght@9..40,300..700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
</head>
<body class="wiki-body">
  <header class="wiki-masthead">
    <div class="wiki-dateline">
      <span class="dateline-mark">⁂</span>
      WRFCoin Wiki · <a href="library.html">↩ back to the Library</a>
    </div>
    <h1 class="wiki-title">
      <span class="title-the">The</span>
      <span class="title-main">WRFCoin Wiki</span>
    </h1>
    <p class="wiki-subtitle">curated synthesis · {total} pages · {active} active · {sources_total} sources cited · {questions_total} open questions</p>
    <p class="wiki-meta">generated {generated_at}</p>
  </header>

  <div class="wiki-layout">
    <aside class="wiki-sidebar">
      <div class="wiki-search-wrap">
        <input type="search" id="wiki-search" placeholder="filter pages…" autocomplete="off" />
      </div>
      {nav_html}
    </aside>

    <main class="wiki-main">
      {content_html}

      <footer class="colophon">
        <p class="colophon-lede">A Colophon</p>
        <p>Generated by <code>wiki/scripts/generate_wiki.py</code>.</p>
        <p>Wiki source at <code>wiki/</code>.</p>
        <p class="colophon-mark">{generated_at} · ⁂</p>
      </footer>
    </main>
  </div>

  <script>
  // tiny search — filters sidebar nav items by data-search
  (function(){{
    const input = document.getElementById('wiki-search');
    if (!input) return;
    const items = Array.from(document.querySelectorAll('.nav-item'));
    input.addEventListener('input', () => {{
      const q = input.value.trim().toLowerCase();
      items.forEach(it => {{
        const hay = (it.dataset.search || '') + ' ' + (it.textContent || '').toLowerCase();
        it.classList.toggle('hidden', q && !hay.includes(q));
      }});
      // hide groups that have no visible items
      document.querySelectorAll('.nav-group').forEach(g => {{
        const any = Array.from(g.querySelectorAll('.nav-item')).some(i => !i.classList.contains('hidden'));
        g.classList.toggle('hidden', !any);
      }});
    }});
  }})();
  </script>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--wiki", type=Path, default=WIKI_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)

    pages = collect_pages(args.wiki)
    if not pages:
        sys.stderr.write(f"no pages found in {args.wiki}\n")
        return 2

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    html_out = build_html(pages, generated_at)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html_out, encoding="utf-8")

    print(f"Wrote {args.output}")
    print(f"  pages: {len(pages)}")
    by_type: dict[str, int] = {}
    for p in pages:
        by_type[p["wiki_type"]] = by_type.get(p["wiki_type"], 0) + 1
    for t, n in sorted(by_type.items()):
        print(f"    {t}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
