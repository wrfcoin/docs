#!/usr/bin/env python3
"""Fetch dynamic state for WRFCoin repos via the GitHub CLI.

Combines a static metadata block (name, description, stack, role, category,
key-metric label) with live GitHub data (open PRs, last push, recent commits)
and writes ``cache/repo-state.json`` for ``generate_library.py``.

Static block is the source of truth for repo categorization. Live block is
best-effort; on rate limits or network failures the script keeps the prior
cache contents and adds an ``unreachable`` flag.

Usage:
    python3 scripts/fetch_repo_state.py
    python3 scripts/fetch_repo_state.py --org wrfcoin --output cache/repo-state.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ORG = "wrfcoin"

# Static metadata. Source of truth for repo categorization, description, and
# the headline "key metric" each card displays. Names of the keys match the
# generator's expectations.
REPOS: list[dict[str, Any]] = [
    {
        "name": "core4",
        "category": "active",
        "stack": "Rust workspace",
        "role": "L1 home · consensus · privacy",
        "key_metric": "8 crates",
    },
    {
        "name": "backend",
        "category": "active",
        "stack": "Node.js / TypeScript",
        "role": "25 microservices",
        "key_metric": "25 services",
    },
    {
        "name": "frontend",
        "category": "active",
        "stack": "React 18 / TypeScript",
        "role": "Platform UI · 450+ components",
        "key_metric": "450+ components",
    },
    {
        "name": "smart-contracts",
        "category": "active",
        "stack": "Solidity 0.8 / Hardhat",
        "role": "DeFi, governance, NFTs, bridges",
        "key_metric": "348 contracts",
    },
    {
        "name": "infra",
        "category": "active",
        "stack": "Docker · k8s · Terraform",
        "role": "Deployment · monitoring · 184 scripts",
        "key_metric": "184 scripts",
    },
    {
        "name": "security-testing",
        "category": "active",
        "stack": "Rust",
        "role": "Attack simulation · stress testing",
        "key_metric": "stress + attacks",
    },
    {
        "name": "mobile",
        "category": "active",
        "stack": "Flutter / Dart",
        "role": "Wallet · barometer · GPS",
        "key_metric": "wallet + sensors",
    },
    {
        "name": "defi-protocols",
        "category": "greenfield",
        "stack": "—",
        "role": "Account abstraction · liquid staking · lending (issue #370)",
        "key_metric": "empty",
    },
    {
        "name": "storage-providers",
        "category": "greenfield",
        "stack": "—",
        "role": "IPFS · Filecoin · Arweave (issue #371)",
        "key_metric": "empty",
    },
    {
        "name": "blockchain-core",
        "category": "archived",
        "stack": "Rust (single crate)",
        "role": "Original monolithic blockchain · FROZEN",
        "key_metric": "ref only",
    },
]


def gh_json(args: list[str]) -> Any:
    """Run a gh subcommand and return parsed JSON. Returns None on error."""
    try:
        result = subprocess.run(
            ["gh"] + args,
            capture_output=True,
            text=True,
            timeout=30,
            check=True,
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, json.JSONDecodeError) as e:
        sys.stderr.write(f"gh error ({' '.join(args)}): {e}\n")
        return None


def fetch_repo_live(name: str) -> dict[str, Any]:
    """Simpler version: one gh repo view + one gh pr list + one gh search commits."""
    out: dict[str, Any] = {"unreachable": False}

    meta = gh_json([
        "repo", "view", f"{ORG}/{name}",
        "--json", "pushedAt,description,isArchived",
    ])
    if meta is None:
        return {"unreachable": True}
    out["last_push"] = meta.get("pushedAt")
    out["github_description"] = meta.get("description") or ""
    out["is_archived_on_github"] = bool(meta.get("isArchived"))

    prs = gh_json([
        "pr", "list", "--repo", f"{ORG}/{name}",
        "--state", "open",
        "--json", "number,isDraft,reviewDecision",
        "--limit", "100",
    ])
    if prs is None:
        prs = []
    out["open_prs"] = len(prs)
    out["draft_prs"] = sum(1 for p in prs if p.get("isDraft"))
    out["prs_awaiting_merge"] = sum(
        1 for p in prs
        if not p.get("isDraft") and p.get("reviewDecision") == "APPROVED"
    )

    # Recent commits via search-commits API: count commits in last 7 days.
    # Use gh api with q= filter.
    week_ago = (datetime.now(timezone.utc).timestamp() - 7 * 86400)
    week_ago_iso = datetime.fromtimestamp(week_ago, tz=timezone.utc).strftime("%Y-%m-%d")
    search = gh_json([
        "api",
        f"search/commits?q=repo:{ORG}/{name}+committer-date:>={week_ago_iso}",
        "-H", "Accept: application/vnd.github.cloak-preview+json",
    ])
    if isinstance(search, dict):
        out["recent_commits_7d"] = search.get("total_count", 0)
    else:
        out["recent_commits_7d"] = None
    return out


def main(argv: list[str] | None = None) -> int:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--org", default=ORG)
    parser.add_argument("--output", type=Path, default=repo_root / "cache" / "repo-state.json")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    repos: list[dict[str, Any]] = []
    unreachable_count = 0
    for static in REPOS:
        if not args.quiet:
            print(f"  fetching {static['name']}...", file=sys.stderr)
        live = fetch_repo_live(static["name"])
        merged = {**static, **live, "repo_url": f"https://github.com/{args.org}/{static['name']}"}
        repos.append(merged)
        if live.get("unreachable"):
            unreachable_count += 1

    out = {
        "schema": "wrfcoin-repo-state-v1",
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "org": args.org,
        "repo_count": len(repos),
        "unreachable_count": unreachable_count,
        "repos": repos,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if not args.quiet:
        active = sum(1 for r in repos if r["category"] == "active")
        greenfield = sum(1 for r in repos if r["category"] == "greenfield")
        archived = sum(1 for r in repos if r["category"] == "archived")
        total_prs = sum(r.get("open_prs", 0) for r in repos)
        print(f"Wrote {args.output}")
        print(f"  repos: {len(repos)} ({active} active, {greenfield} greenfield, {archived} archived)")
        print(f"  open PRs across org: {total_prs}")
        if unreachable_count:
            print(f"  unreachable: {unreachable_count}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
