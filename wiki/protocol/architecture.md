---
title: Architecture and Implementation Boundary
slug: architecture
wiki_type: protocol
status: active
sources:
  - path: whitepaper/03-architecture.md
    kind: repo
    last_seen: 2026-09-20
crosslinks: [vision, protocol/proof-of-publication, implementation/tech-stack, release/testnet-roadmap]
open_questions:
  - "Which rollup design, if any, should be selected for a future L2?"
  - "What protocol and accountability rules should govern a future data DAG?"
answers_filed: []
last_ingest: 2026-09-20
last_lint: 2026-09-20
review_due: 2026-12-20
tags: [protocol, architecture, l1, planned]
---

# Architecture and Implementation Boundary

## Current

Wrfcoin currently has one Proof-of-Publication L1. Its implemented
environmental-data flow is commit, reveal, oracle attestation, quorum decision,
and deterministic reward state. The Actix `launch_api` route registration is
the source of truth for the node HTTP surface.

The repository can be ahead of the private deployment. “Implemented” therefore
does not mean “publicly reachable”; use [[release/testnet-roadmap]] and the root
`STATUS.md` for that boundary.

## Planned

L2 rollups, a DAG data sidechain, full stake slashing (only partial slashing
exists today), carbon/RWA markets, and
cross-layer accountability are planned. They are not active testnet layers or
guarantees. The old three-layer diagram describes target architecture only.

## Implementation map

Relevant Rust workspace packages include `native-chain`, `shared-protocol`,
`consensus-engines`, `p2p`, privacy tooling, and `tools/cli`. A crate's presence
does not prove it is selected or healthy in a deployed node.

## Evidence

- `whitepaper/03-architecture.md` records the current/planned split.
- `core4/native-chain/src/bin/launch_api/routes/mod.rs` registers served routes.
- `core4#3262` tracks the checked first-tranche OpenAPI description.
- `core4#3240` tracks the unresolved location-reference reward defect.
