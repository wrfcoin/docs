---
title: Proof of Publication (PoPub)
slug: proof-of-publication
wiki_type: protocol
status: active
sources:
  - path: whitepaper/04-consensus.md
    kind: repo
    last_seen: 2026-09-20
crosslinks: [vision, protocol/architecture, economics/wrf-token, implementation/tech-stack]
open_questions:
  - "How should Sybil and collusion resistance be calibrated?"
  - "What policy and state transition should implement slashing?"
  - "How should geographic reward fairness be measured?"
answers_filed: []
last_ingest: 2026-09-20
last_lint: 2026-09-20
review_due: 2026-12-20
tags: [protocol, consensus, popub, rewards]
---

# Proof of Publication (PoPub)

## Implemented core

PoPub is the active native-chain consensus path. Contributors commit and reveal
observations; oracle attesters submit signed votes; a configured quorum decides
acceptance; and the L1 records contribution and reward state. The current
private testnet registers three attesters with a quorum of two, but only two
run online; losing either online attester stops contributions from finalizing
even while blocks continue.

## Partial economics

Reward and attestation machinery exists, but the broader four-role market is
not complete. Forecasting and verifier economics are partial, and `core4#3240`
tracks a known location-reference defect affecting reward fairness.

## Planned

Slashing is partial. On core4 `main`, three consecutive low-quality reveals
that reached quorum cost a contributor 15 base units (0.00000015 WRF), and validators can be slashed
for equivocation. A reveal-time out-of-range slash exists but has no effect
(core4#3214, private). Slashing station owners for bad data was ruled in by the
owner on 2026-09-21 and is still being designed (core4#3218, private).

Variable-specific confidence thresholds, anti-collusion policy, forecaster
reputation curves, and cross-layer accountability remain planned.

## Evidence

- `whitepaper/04-consensus.md` records the implementation boundary.
- `core4/native-chain/src/bin/launch_api/routes/oracle.rs` serves oracle routes.
- `core4#3240` records the unresolved reward-fairness defect.
