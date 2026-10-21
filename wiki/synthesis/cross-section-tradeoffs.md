---
title: Cross-Section Design Tradeoffs
slug: cross-section-tradeoffs
wiki_type: synthesis
status: active
sources:
  - path: ../protocol/architecture.md
    kind: wiki
    last_seen: 2026-09-20
  - path: ../protocol/proof-of-publication.md
    kind: wiki
    last_seen: 2026-09-20
  - path: ../economics/wrf-token.md
    kind: wiki
    last_seen: 2026-09-20
crosslinks: [protocol/architecture, protocol/proof-of-publication, economics/wrf-token, release/testnet-roadmap]
open_questions:
  - "How should future sidechain autonomy be bounded by L1 accountability?"
  - "What evidence should activate currently planned token economics?"
answers_filed: []
last_ingest: 2026-09-20
last_lint: 2026-09-20
review_due: 2026-12-20
tags: [synthesis, tradeoffs, planned]
---

# Cross-Section Design Tradeoffs

This page records design questions, not current capabilities.

## Current pressure points

- **Availability versus quorum:** the private testnet registers three attesters
  with a quorum of two, but only two run online, so losing either online
  attester stops real reveals from finalizing while the chain still advances.
- **Reward activity versus fairness:** reward state exists, but a known
  location-reference defect prevents a geographically production-ready claim.
- **Repository versus deployment:** code on `main` can be newer than pinned
  private images; source presence is not public reachability.
- **Public documentation versus release:** documentation may be prepared before
  deployment, secret scanning, and human visibility decisions are complete.

## Planned-design tensions

- L2 throughput versus the added proving/challenge trust model.
- DAG-sidechain autonomy versus L1 accountability and rollback limits.
- Rich WRC-20 environmental semantics versus implementer simplicity.
- Slashing strength versus calibrated evidence and false-positive risk.
- Broader DeFi utility versus the accepted read/quote-only simulated boundary.

None of these planned designs should be inferred from the implemented L1.
