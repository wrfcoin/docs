#!/usr/bin/env python3
"""Reject a forked operator guide; this repo keeps only a short pointer stub."""

from __future__ import annotations

import argparse
from pathlib import Path

MAX_LINES = 40
REQUIRED_POINTER = "wrfcoin/infra"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default="testnet/operator-guide.md")
    args = parser.parse_args()
    path = Path(args.path)
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) > MAX_LINES:
        print(f"ERROR: {path} has {len(lines)} lines; pointer stub maximum is {MAX_LINES}")
        return 1
    if REQUIRED_POINTER not in "\n".join(lines):
        print(f"ERROR: {path} does not point to the canonical wrfcoin/infra guide")
        return 1
    print(f"operator guide pointer OK: {len(lines)} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
