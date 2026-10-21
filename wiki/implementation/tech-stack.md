---
title: Reference Implementation Tech Stack
slug: tech-stack
wiki_type: implementation
status: active
sources:
  - path: whitepaper/06-tech-stack.md
    kind: repo
    last_seen: 2026-09-20
crosslinks: [protocol/architecture, protocol/proof-of-publication, release/testnet-roadmap]
open_questions:
  - "What evidence gates any future post-quantum migration?"
  - "Which checks are required and non-vacuous for each release?"
answers_filed: []
last_ingest: 2026-09-20
last_lint: 2026-09-20
review_due: 2026-12-20
tags: [implementation, rust, cryptography, libp2p]
---

# Reference Implementation Tech Stack

## Current

The reference implementation is a Rust Cargo workspace whose active packages
include `native-chain`, `shared-protocol`, `consensus-engines`, `p2p`, privacy
components, and `tools/cli`. The node uses libp2p; the old minimal-TCP migration
description is obsolete.

New wallets use ed25519. The settled derivation is BIP-39 mnemonic to seed with
an empty passphrase, followed by the SLIP-0010 ed25519 master key with no child
path. Addresses are `0x` plus the first 20 bytes of SHA3-256(public key).
Legacy secp256k1 addresses are receive-only. Clients, not the backend, sign.

## Boundaries

Post-quantum cryptography, active L2s, and mainnet operations remain planned.
The application-layer DeFi direction is read/quote-only and simulated; it is
not an L1 consensus primitive and cannot move balances.

The presence of a test or workflow is not itself evidence: skipped, zero-step,
or infrastructure-blocked checks do not prove a claim.

## Evidence

- `whitepaper/06-tech-stack.md` records these choices and boundaries.
- The cross-client key fixture is tracked by `core4#3234`.
- The checked node API description is tracked by `core4#3262`.
