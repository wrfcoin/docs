# 4. Consensus

> **IMPLEMENTED core, PARTIAL incentive completeness.** Proof of Publication
> (PoPub) is the only active consensus engine in the current native-chain node.
> Commit/reveal and oracle-attestation quorum run today. Stake slashing is
> **PARTIAL**: a repeated-low-quality slash and validator equivocation slashing
> exist on `main`, while slashing station owners for bad data is still being
> designed. Complete forecaster economics and cross-layer accountability remain
> **PLANNED**. See [Implementation status](../STATUS.md).

## Active Proof of Publication flow

PoPub rewards publication of verifiable environmental observations instead of
proof-of-work computation or capital lockup alone. The implemented flow is:

1. A contributor commits a hash for a station observation.
2. The contributor reveals the payload within the allowed window.
3. Oracle attesters evaluate the revealed contribution and submit signed votes.
4. The configured quorum determines whether the contribution can finalize.
5. The L1 records contribution and reward state through deterministic state
   transitions.

The current private testnet registers three attesters with a quorum of two, but
only two of them run online; the third is kept offline. That is an operational
fact, not a promise of continuous quorum: losing either online attester stops
contributions from finalizing, and reveals defer or expire, even while blocks
continue. `core4/native-chain/src/bin/launch_api`
serves commit, reveal, attestation, and status routes used by this flow.

## What is rewarded today

Contribution and attestation machinery exists, and reward state is observable.
It is not yet honest to claim a complete four-role market for contributors,
validators, forecasters, and verifiers. Forecasting is partial, verifier
economics are not a finished product, and a known reference-station defect can
make geographic reward comparisons unfair (tracked by `core4#3240`).

## Why not PoW or pure PoS?

PoW rewards computational effort; pure PoS rewards capital lockup. PoPub's
design goal is to make verified information production the rewarded work. The
current node still uses stake/account state where implemented, but no other
engine in the `consensus-engines` workspace is selected merely because its
code exists.

## PARTIAL: slashing

What core4 `main` does today (not verified against the deployed images):

- **Repeated low-quality data.** After a reveal reaches attester quorum, it is
  scored for quality. A contributor scored low quality three times in a row is
  slashed 15 base units (0.00000015 WRF) under the default policy, which is enforced from block
  height 0. A reveal without quorum never adds to the streak.
- **Out-of-range data at reveal time.** This slash exists but has no effect: it
  uses the station ID instead of an account as the slash identity (tracked as
  core4#3214, private).
- **Validator equivocation.** Validators can be slashed for signing two
  different blocks at the same height.

Owner ruling 2026-09-21: station owners are to be slashed for bad data. That
design is owner-held (core4#3218, private) and is not active.

## PLANNED: broader slashing and role economics

The following remain design intent, not active guarantees:

- slashing station owners for bad data (see the ruling above);
- slashing contributors for deliberately false observations, beyond the
  repeated-low-quality rule;
- slashing validators for approving bad data or rejecting good data;
- variable-specific ground-truth and confidence thresholds;
- anti-collusion protection in sensor-sparse regions;
- forecaster reputation and reward curves;
- verifier/audit-of-audits compensation;
- accountability that propagates across a future sidechain/L1 boundary.

Until those state transitions and policies are explicitly activated and tested,
the project must not describe complete bad-data accountability. It must also not
say that contributor stake is safe from slashing: repeated low-quality data can
already cost a contributor stake on `main`.

## Open design questions

PoPub still needs calibrated ground truth, Sybil/collusion resistance,
geographic fairness, and a precise slashing destination. Testnet evidence should
be used to settle these questions; the whitepaper does not silently promote
them to implemented behavior.
