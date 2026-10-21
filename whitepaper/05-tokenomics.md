# 5. Tokenomics

> **Status as of 2026-09 — target economics, except where stated.** WRF reward
> state exists on the L1. Stake slashing is **PARTIAL** (see
> [Consensus](./04-consensus.md)); holder governance, WRC-20, and
> climate-finance settlement are **PLANNED**. They are not active testnet
> guarantees. See [Implementation status](../STATUS.md).

## WRF — the network's native token

WRF is the utility token of the Wrfcoin network. It is **not** a security and is not sold to investors as such (see *On investors and contributors* below).

### What WRF does

**Reward currency for verifiable work.** Every action the network values — submitting validated environmental data, running accurate forecasts, validating others' work — is paid in WRF. This is the bulk of WRF flow.

**PLANNED — stake for validators.** The target design requires validator stake
and slashes bad behavior. The current environmental-data path enforces only part
of that policy: a repeated-low-quality slash on `main`. (See [Consensus](./04-consensus.md).)

**PLANNED — governance.** The target design gives WRF holders votes on protocol
changes; this is not an active testnet capability.

**PLANNED — ecosystem settlement.** WRC-20, carbon credits, ESG instruments,
and RWA-token settlement remain design goals, not offered products.

### What WRF does NOT do

It is not designed as a speculation vehicle. The network's success metric is *quality and quantity of environmental data published*, not WRF price. Token mechanics are deliberately boring: a clear utility loop (data → reward), a clear stake-and-slash model for validators, no exotic deflationary tricks beyond a small burn on ecosystem-token issuance (see WRC-20 below).

DeFi integrations (lending, derivatives, complex yield strategies on top of WRF) are *deferred* until the underlying utility is established. Premature DeFi-ification of a utility token tends to convert it into a casino chip — the data-quality incentives degrade as the speculative incentives crowd them out. Wrfcoin's design choice is to wait.

## On investors and contributors

A specific design distinction made early in the project:

- **Investors** receive **equity** in the entity that develops Wrfcoin (a conventional company structure). They share in the upside of the *organization*, not the token.
- **Contributors** receive **WRF tokens** for verified work (data, validation, forecasting). They share in the value of the *network*.

This matters for two reasons.

First, regulatory clarity. Issuing tokens to investors as a security raises a long list of compliance concerns in most jurisdictions. Restricting token issuance to *earned* compensation for verifiable work keeps WRF's center of gravity in the utility category and reduces (though does not eliminate) regulatory ambiguity.

Second, incentive alignment. An investor who holds tokens has an incentive for the *price* to go up, regardless of network health. A contributor who earned tokens for verified work has an incentive for the *network* to be useful — because that's what makes future earnings worthwhile. Separating the two roles separates the two incentives.

## PLANNED: WRC-20 ecosystem token standard

ERC-20 (and the equivalents on other chains) is a great general-purpose token standard. It's also generic — it knows nothing about environmental data, verification, or impact tracking.

WRC-20 is Wrfcoin's domain-specific extension: a token standard for **environmental and climate tokens** that runs on Wrfcoin's infrastructure. It inherits ERC-20's transferability and basic accounting, but adds first-class support for the things environmental tokens actually need:

- **Linkage to verified data.** A WRC-20 token can be programmatically tied to environmental data published on Wrfcoin's data sidechains (e.g., a carbon credit token tied to satellite-verified forest area).
- **Issuance gates by validation status.** A token can be configured to require specific validation thresholds before minting (e.g., only mint a regenerative-agriculture token after multiple validators confirm the soil-carbon increase).
- **Impact tracking metadata.** Tokens carry structured metadata about their environmental claim, with on-chain links to the supporting data and validation records.

The WRC-20 design intent: anyone building a climate-finance, ESG, or environmental-monitoring application can issue their own token on Wrfcoin without re-implementing the validation and verification primitives that already exist in the protocol.

### What WRC-20 enables (a non-exhaustive list)

- **Carbon credits** with on-chain provenance from satellite + ground-truth data
- **ESG compliance instruments** for enterprises with auditable supply-chain emissions data
- **Regenerative agriculture tokens** tracking verified soil-carbon and biodiversity outcomes
- **Real-world-asset (RWA) climate-risk tokens** for insurance and reinsurance
- **Scientific data marketplace tokens** for paid access to specific research datasets
- **Disaster-response funding tokens** that release funds based on verified ground conditions

These are *examples*, not commitments. The ecosystem of WRC-20 tokens is whatever third parties choose to build.

## Target token economics — PLANNED

A simplified target model for how WRF could flow through the network:

```
Issuance:
  Validated data publication  ──>  contributors, validators, forecasters

Sinks:
  Validator stake                     (locked but recoverable)
  WRC-20 issuance fee  ──>  burned    (small, deflationary on ecosystem growth)
  L2 / sidechain tx fees  ──>  validators (replaces issuance over time)
  Slashing  ──>  burned or treasury

Speculation:
  Allowed but not subsidized.
  No founder vesting cliffs designed for trading;
  no protocol-level liquidity mining beyond the data-publication reward loop.
```

The intent is for WRF supply growth to *track network utility growth* — more verified data published means more WRF earned, but the earning is gated by the work. The network can't issue WRF without validating that something useful happened.

## What's still being calibrated

Specific numbers — issuance rate, validator stake minimum, slashing percentages, WRC-20 issuance fee — will be set at testnet launch and tuned based on testnet behavior. They are deliberately not in this document because committing to specific numbers before testnet would be premature and misleading.

Both the mechanism and its parameters remain subject to implementation and
review. This chapter does not activate them.
