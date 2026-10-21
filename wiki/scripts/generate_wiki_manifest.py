#!/usr/bin/env python3
"""Generate wiki-manifest.json for the WRFCoin wiki.

Walks the wiki root, parses YAML frontmatter from every markdown file that has
it, and emits ``data/wiki-manifest.json`` matching the schema
``wrfcoin-wiki-manifest-v1``. The manifest is consumed by
``scripts/generate_library.py`` which embeds wiki coverage into
``site/library.html``.

Files without frontmatter (e.g. leftover README placeholders) are skipped.

Usage:
    python3 scripts/generate_wiki_manifest.py
    python3 scripts/generate_wiki_manifest.py --wiki-root /path/to/wiki --output /path/to/manifest.json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("pyyaml required: pip install pyyaml\n")
    sys.exit(2)


SCHEMA_VERSION = "wrfcoin-wiki-manifest-v1"
FRONTMATTER_DELIM = "---"


def parse_frontmatter(text: str) -> dict | None:
    """Return parsed YAML frontmatter, or None if the file has none."""
    if not text.startswith(FRONTMATTER_DELIM):
        return None
    lines = text.split("\n")
    if not lines or lines[0].strip() != FRONTMATTER_DELIM:
        return None
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == FRONTMATTER_DELIM:
            end_idx = i
            break
    if end_idx is None:
        return None
    fm_text = "\n".join(lines[1:end_idx])
    try:
        return yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        sys.stderr.write(f"YAML parse error: {e}\n")
        return None


def derive_count(fm: dict, field: str) -> int:
    """Array length wins; fall back to scalar field; default 0."""
    val = fm.get(field)
    if isinstance(val, list):
        return len(val)
    if isinstance(val, int):
        return val
    return 0


def derive_last_updated(fm: dict) -> str:
    """Prefer last_ingest, then last_lint, then last_updated."""
    for key in ("last_ingest", "last_lint", "last_updated"):
        val = fm.get(key)
        if val:
            return str(val)
    return ""


def build_entry(md_path: Path, wiki_root: Path) -> dict | None:
    text = md_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return None
    rel_path = md_path.relative_to(wiki_root).as_posix()
    slug = fm.get("slug") or md_path.stem
    return {
        "slug": slug,
        "title": fm.get("title", md_path.stem),
        "wiki_type": fm.get("wiki_type", "unknown"),
        "wiki_status": fm.get("status", "stub"),
        "wiki_path": rel_path,
        "source_count": derive_count(fm, "sources"),
        "open_questions": derive_count(fm, "open_questions"),
        "last_updated": derive_last_updated(fm),
    }


def build_manifest(wiki_root: Path) -> dict:
    entries: list[dict] = []
    for md_path in sorted(wiki_root.rglob("*.md")):
        # Skip the AGENTS guide itself; it's a guide, not a wiki page.
        if md_path.name == "AGENTS.md" and md_path.parent == wiki_root:
            continue
        entry = build_entry(md_path, wiki_root)
        if entry is not None:
            entries.append(entry)
    try:
        wiki_root_hint = wiki_root.relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        wiki_root_hint = str(wiki_root)
    return {
        "schema": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "wiki_root": wiki_root_hint,
        "entries": entries,
    }


def main(argv: list[str] | None = None) -> int:
    repo_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--wiki-root", type=Path, default=repo_root)
    parser.add_argument("--output", type=Path, default=repo_root / "data" / "wiki-manifest.json")
    args = parser.parse_args(argv)

    wiki_root = args.wiki_root.resolve()
    if not wiki_root.is_dir():
        sys.stderr.write(f"wiki root does not exist: {wiki_root}\n")
        return 2

    manifest = build_manifest(wiki_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2, sort_keys=False) + "\n", encoding="utf-8")

    total = len(manifest["entries"])
    active = sum(1 for e in manifest["entries"] if e["wiki_status"] == "active")
    sources = sum(e["source_count"] for e in manifest["entries"])
    open_qs = sum(e["open_questions"] for e in manifest["entries"])
    print(f"Wrote {args.output}")
    print(f"  entries: {total} ({active} active)")
    print(f"  sources cited: {sources}")
    print(f"  open questions: {open_qs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
