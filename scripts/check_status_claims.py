#!/usr/bin/env python3
"""Guard public documentation against known stale capability claims."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    "STATUS.md": ("IMPLEMENTED", "PARTIAL", "PLANNED", "NOT OFFERED"),
    "whitepaper/06-tech-stack.md": ("SLIP-0010", "secp256k1 addresses are receive-only", "libp2p"),
    "whitepaper/07-roadmap.md": ("public join path is **PARTIAL**", "SHA3-256"),
    "whitepaper/04-consensus.md": ("## PARTIAL: slashing",),
}
PROHIBITED = {
    "STATUS.md": ("Bech32", "Design intent only. The representation work"),
    "whitepaper/04-consensus.md": ("validator or contributor stake is currently at\nrisk",),
    "whitepaper/05-tokenomics.md": ("Bad behavior is slashed.",),
    "whitepaper/06-tech-stack.md": ("Bech32",),
    "whitepaper/07-roadmap.md": ("minimal TCP; libp2p planned", "**Testnet target:**", "Bech32"),
    "wiki/index.md": ("qmd query", "qmd search", "qmd get"),
}


def main() -> int:
    errors: list[str] = []
    for name, needles in REQUIRED.items():
        text = (ROOT / name).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"{name}: missing required truth marker: {needle}")
    for name, needles in PROHIBITED.items():
        text = (ROOT / name).read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                errors.append(f"{name}: stale unqualified claim survives: {needle}")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("documentation status claims OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
