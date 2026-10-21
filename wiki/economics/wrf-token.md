---
title: WRF Economics and WRC-20 Boundary
slug: wrf-token
wiki_type: economics
status: active
sources:
  - path: whitepaper/05-tokenomics.md
    kind: repo
    last_seen: 2026-09-20
crosslinks: [protocol/architecture, protocol/proof-of-publication, release/testnet-roadmap]
open_questions:
  - "What reviewed policy should govern issuance, stake, and slashing?"
  - "What specification and activation gate should define WRC-20?"
answers_filed: []
last_ingest: 2026-09-20
last_lint: 2026-09-20
review_due: 2026-12-20
tags: [economics, token, wrf, planned]
---

# WRF Economics and WRC-20 Boundary

## Current

The L1 records contribution and reward state for the implemented
commit/reveal/attestation flow. That does not establish a complete token market,
public economic service, or geographically fair reward system. `core4#3240`
tracks a known location-reference defect.

## Planned

Validator stake, full slashing (only partial slashing exists today; see
[[protocol/proof-of-publication]]), holder governance, WRC-20, issuance fees,
sidechain/L2 fee flows, carbon credits, ESG instruments, RWA products, and
marketplaces are planned. No current testnet claim should describe those target
economics as active.

The investor-equity/contributor-token separation is project design intent, not
legal advice or a claim of regulatory status.

## Evidence

- `whitepaper/05-tokenomics.md` now labels target economics explicitly.
- `whitepaper/04-consensus.md` identifies implemented consensus and planned
  incentive behavior.
- `STATUS.md` records the dated capability boundary.
