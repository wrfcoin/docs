---
title: Testnet Roadmap and Reachability
slug: testnet-roadmap
wiki_type: release
status: active
sources:
  - path: whitepaper/07-roadmap.md
    kind: repo
    last_seen: 2026-09-20
crosslinks: [protocol/architecture, protocol/proof-of-publication, implementation/tech-stack]
open_questions:
  - "When will the reviewed public join path meet every release gate?"
  - "What measurable hyperlocal forecast target closes the weather-oracle phase?"
answers_filed: []
last_ingest: 2026-09-20
last_lint: 2026-09-20
review_due: 2026-10-20
tags: [release, roadmap, testnet, readiness]
---

# Testnet Roadmap and Reachability

## Current state

A private testnet exists and advances. Core L1, libp2p, wallet, commit/reveal,
attestation, and reward-state behavior is implemented, but public reachability
is **PARTIAL**. Repository `main`, pinned deployment revisions, and what a
tester can reach are distinct facts.

The public join path is not offered until endpoint documentation, faucet
honesty, snapshot trust, operator guidance, history scanning, and human
visibility gates are complete. Documentation does not perform deployment,
restart, or repository-visibility actions.

## Capability phases

| Phase | Honest status | Boundary |
|---|---|---|
| Foundation | PARTIAL readiness | Private chain exists; public joining is not offered. |
| Weather oracle | PARTIAL | Observation and attestation work; quality, fairness, reachability, and operator gates remain. |
| Meta-OS integration | PLANNED | No cross-chain production workflow is offered. |
| Ecosystem expansion | PLANNED | No WRC-20, RWA, or climate-finance product is offered. |

There is no date-certain public launch promise. Completion is evidence-gated,
not inferred from a historical target date.

## Evidence

- `STATUS.md` is the dated repository-level matrix.
- `whitepaper/07-roadmap.md` separates current and planned capabilities.
- `wrfcoin/infra` owns deployment, launch-gate, and operator evidence.
