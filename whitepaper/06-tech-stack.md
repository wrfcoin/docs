# 6. Tech stack

> **Status as of 2026-09.** Rust, ed25519 wallet signing, the native-chain node,
> and libp2p networking are implemented. Post-quantum cryptography, active L2s,
> and production/mainnet operations remain planned. See
> [Implementation status](../STATUS.md).

## Rust workspace

The reference implementation is a Rust Cargo workspace. The active layout
includes `native-chain`, `shared-protocol`, `consensus-engines`, `p2p`, privacy
components, and `tools/cli`; the older `core/network/wallet/cli` diagram was a
conceptual summary, not the current directory tree.

Rust supplies memory safety without garbage collection, predictable systems
performance, and strong types for consensus state. The project also uses
JavaScript/TypeScript services and clients, Flutter/Dart mobile code, and
container/compose deployment tooling. Their presence does not make every
service public or deployed.

## Cryptography and wallets

New wallets use ed25519. The settled derivation is BIP-39 mnemonic to seed with
an empty passphrase, then the SLIP-0010 ed25519 master key with no child path.
Addresses are `0x` plus the first 20 bytes of SHA3-256(public key). Legacy
secp256k1 addresses are receive-only. Clients sign transactions; the backend
does not custody wallet keys.

This is pinned by a byte-identical cross-client fixture. Post-quantum schemes
remain under evaluation and are **PLANNED**, not part of today's wallet claim.

## P2P networking

The node uses **libp2p** through the `core4/p2p` crate for peer transport and
discovery-related functionality. The previous statement that networking was a
minimal TCP transport awaiting migration was stale.

This does not mean every operational recovery path is complete. Supervision of
P2P consumers remains separately reviewed, and a source-level libp2p dependency
is not proof that a particular deployed node currently has healthy peers.

## API and deployment

The real node HTTP surface is the Actix `launch_api`. A checked first-tranche
OpenAPI document is under review in `core4#3262`; legacy generated SDKs do not
describe that node surface. The private testnet deployment can trail current
`main`, so repository implementation and deployed reachability are reported
separately.

## DeFi boundary

No DeFi primitive is part of the L1 consensus protocol. The accepted testnet
direction is an application-layer standalone service that is **read/quote-only**,
marks every response `simulated:true`, and cannot move balances. Any balance-
moving design requires the separate ADR 0002 decision (`defi-protocols#74`).
This reconciles application-level testnet experimentation with the protocol-
level non-goal.

## Quality and supply chain

The repositories contain targeted tests, static checkers, dependency/security
workflows, and build gates. This documentation does not claim that every tool
runs on every push: a check that executes zero steps, is skipped, or is blocked
by runner/billing state is not evidence of correctness. Each readiness claim
must name the command or route that actually ran.

## Not currently offered

- No mainnet or production SLA.
- No active Optimistic or ZK rollup.
- No active DAG data sidechain.
- No protocol-level balance-moving DeFi.
- No guarantee that a route on `main` is present in the older deployed images.
