# 7. Roadmap

Four capability phases. The private testnet has crossed parts of Phase 1 and
Phase 2, but the public join path is **PARTIAL** and the deployed images can lag
current `main`. This roadmap is not a statement that a public launch occurred;
see [Implementation status](../STATUS.md).

---

## Phase 1 — Foundation *(PARTIAL deployment readiness)*

The goal of Phase 1 is to have a working blockchain — not yet doing the interesting weather-oracle work, but functioning as a chain you can transact on.

- L1 primitives: blocks, transactions, Merkle trees
- P2P networking layer (libp2p is implemented; deployed peer health is a
  separate operational claim)
- Wallet and key management (ed25519 via SLIP-0010, BIP-39, `0x`-hex SHA3-256
  addresses)
- CLI tools: `keygen`, `send`, `mine`, `status`
- Proof of Publication consensus with commit/reveal and oracle attestations
- CI/CD with fuzzing, security scanning, and dependency auditing

**Status:** the private testnet exists and advances, but repository capability,
deployed capability, and public reachability are reported separately. Public
joining is not yet offered.

**Phase 1 ends when:** a multi-node testnet can be stood up and basic transactions can flow through it reliably.

---

## Phase 2 — Weather Oracle Launch

Phase 2 turns Wrfcoin into something that actually does its job: producing verified environmental data with cryptoeconomic backing.

- Validator system for meteorologists and data scientists
- Crowdsourced observation submission interface
- Forecast submission + community voting mechanism
- WRF reward distribution for accurate forecasts and validated data
- Public API / oracle for on-chain forecast access
- Open-source publication of the implementation (subject to security review)

**Phase 2 ends when:** Wrfcoin is the source of weather forecasts that are *measurably* competitive with traditional sources for at least one hyperlocal use case.

**Status:** PARTIAL. Observation, attestation, forecast, and reward machinery
exists, but forecast quality, reward fairness, public reachability, and several
operator gates remain incomplete.

---

## Phase 3 — Meta-OS Integration

Phase 3 widens the network's role from "weather oracle" to "coordination layer for environmental analysis across the broader DePIN ecosystem."

- Cross-chain task routing — delegate compute-intensive work to specialized networks (Render Network for GPU compute, Akash for general compute, Filecoin for storage, Arweave for archival)
- Wrapped token management for external assets (wRNDR, wFIL, wLINK, wAKT, wTAO, etc.)
- Unified task evaluation and reward engine — accuracy-weighted compensation for results across networks
- Smart-contract automation for task origination and routing

**Phase 3 ends when:** a non-trivial workload (e.g., a high-resolution regional forecast) is routinely composed of work delegated across at least three external networks, settled in WRF.

---

## Phase 4 — Ecosystem Expansion

Phase 4 is when the network starts hosting third-party climate-finance and environmental applications at scale.

- Agricultural domain: crop forecasting, irrigation optimization, soil-health markets
- Event forecasting: outdoor events, disaster preparedness, parametric insurance
- Real-world-asset integration: climate-risk assessment for real estate, infrastructure, supply chains
- Advanced analytics and research marketplace — WRC-20 tokens for paid access to specific datasets
- DAO-governed treasury allocations for ecosystem grants

**Phase 4 has no defined end.** It's the steady-state of the network operating as the climate-information infrastructure layer.

---

## What this roadmap is *not*

It is not a token-launch schedule. There is no scheduled exchange listing, no public sale, no investor pitch in this document. The token exists to align contributor incentives, not to be a fundraising mechanism.

It is not a guaranteed timeline. Phase 1 has been in progress for about a year of intermittent work; Phase 2 will take as long as it takes to be production-ready. Anyone who needs a date-certain commitment to feature delivery should not build critical infrastructure on Wrfcoin yet.

It is not a feature wish list. Each phase is constrained to the work that's necessary for the *next* phase to make sense. The protocol grows by addition, not by accumulation.

---

## How to follow along

- **This repo** — protocol vision and architecture (you're reading it)
- **[@wrfcoin](https://github.com/wrfcoin) org** — implementation repos, opening up around the testnet launch

Substantive feedback on this whitepaper is welcome via GitHub issues. The protocol benefits from being read by people who'll push back on it.
