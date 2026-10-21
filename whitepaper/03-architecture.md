# 3. Architecture

> **Status as of 2026-09 — mixed.** The single L1, commit/reveal observation
> flow, oracle attestations, and reward state are implemented. L2 rollups and a
> DAG data sidechain are **PLANNED**, not running testnet layers. See
> [Implementation status](../STATUS.md) for evidence and deployment boundaries.

## Current implementation

Today's implemented environmental-data path is:

1. A device or upstream weather source reaches the backend/collector.
2. A contributor submits a commitment to the L1.
3. The contributor reveals the observation matching that commitment.
4. Oracle attesters evaluate the reveal and submit attestations.
5. The configured quorum determines whether the contribution is accepted.
6. Reward state is recorded by the L1 state transition.

The running private testnet uses one Proof-of-Publication L1. It does not route
observations through an active DAG sidechain or settle activity from a rollup.
The deployment can also trail current code, so an implemented route is not a
claim that a public tester can reach it; consult [STATUS.md](../STATUS.md).

## Current L1 boundary

The L1 holds blocks, accounts, transactions, contribution commitments and
reveals, oracle attestations, and reward-related state. The `launch_api` route
registration in `core4/native-chain/src/bin/launch_api/routes/mod.rs` is the
machine-checkable HTTP surface.

The current architecture does not prove every product claim in the target
design. Forecast product quality is partial, reward fairness has a known
location-reference defect, data-quality slashing is partial (a
repeated-low-quality slash exists on `main`; slashing station owners for bad
data is still being designed), and carbon/RWA marketplaces are not offered.

---

## Target architecture — PLANNED

The longer-term design separates three workload classes:

```
┌──────────────────────────────────────────────────────────┐
│  L1 — Settlement & Governance               IMPLEMENTED │
│  • Proof of Publication consensus                        │
│  • Commit/reveal + oracle attestation                    │
│  • Canonical account, transaction, and reward state      │
└──────────────────────────────────────────────────────────┘
                            ↑↓
┌──────────────────────────────────────────────────────────┐
│  L2 — DeFi & Throughput                         PLANNED  │
│  • Optimistic / ZK rollups                               │
│  • Liquidity, micro-transactions, marketplaces           │
└──────────────────────────────────────────────────────────┘
                            ↑↓
┌──────────────────────────────────────────────────────────┐
│  Data Sidechains — Environmental Data           PLANNED │
│  • DAG-based high-frequency ingestion                    │
│  • Batch commitments anchored into L1                    │
└──────────────────────────────────────────────────────────┘
```

### Planned L2

Optimistic or ZK rollups remain design options for application-layer
throughput and composability. No rollup is part of the active testnet, and no
current route should be described as inheriting L1 security through a rollup.

### Planned data sidechain

A DAG-based sidechain remains a design direction for concurrent sensor ingest
and later L1 anchoring. The protocol, ordering rules, validation membership,
batch cadence, and cross-layer accountability are not finalized. Today’s
commit/reveal/attestation path runs against the L1 rather than this sidechain.

### Planned stake slashing and marketplaces

Stake-weighted validation, full slashing for bad contributions or validations
(beyond the partial slashing described in [Consensus](./04-consensus.md)),
carbon-credit markets, ESG instruments, and RWA products are target behavior.
They are not current testnet guarantees. Any future activation requires
separate protocol decisions, state transitions, tests, and deployment evidence.

## Implementation map

The active Rust workspace is broader than the old conceptual
`core/network/wallet/cli` diagram. Its relevant packages include
`native-chain`, `shared-protocol`, `consensus-engines`, `p2p`, privacy tooling,
and `tools/cli`. The active node path is `native-chain`; the presence of a
crate or module is not evidence that its feature is selected at runtime.
