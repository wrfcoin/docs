# Implementation status

Source assessment: **2026-10-19**, against current `main` of the owning repositories. This is a source review, not a deployment audit or launch GO. Test files cited below were inspected as evidence of coverage; their suites were not rerun for this documentation update.

A route or test on `main` does not establish what a visitor can reach today. Start with the [quickstart](testnet/quickstart.md), [software availability](testnet/downloads.md) and [node-status guide](testnet/node-status.md). No live-node probes were performed.

## Status vocabulary

- **IMPLEMENTED** — a concrete source route, state transition or client implementation exists; deployment is not implied.
- **PARTIAL** — useful code exists, but an end-to-end, publication or deployed requirement is missing or unverified.
- **PLANNED** — architectural intent or pending work; not offered by the current testnet.
- **NOT OFFERED** — deliberately unavailable for this cut.

## Capability matrix (2026-10-19)

Evidence paths are repository-relative paths on `main`, prefixed with the owning repository name. They refer to source, not private issue threads or snapshot-incompatible revisions. Every final-column item is **not verified for this publication**.

| Capability | Status | Evidence on main and source boundary | Not verified for this publication |
|---|---|---|---|
| Single Proof-of-Publication L1 | **IMPLEMENTED** | `core4/shared-protocol/src/consensus/proof_of_publishing.rs`; `core4/native-chain/src/bin/launch_api/routes/mod.rs`. Proof-of-Publication implementation and chain/transaction routes exist. | Active node image, consensus configuration and liveness; not verified for this publication. |
| Environmental commit → reveal | **IMPLEMENTED** | `core4/native-chain/src/bin/launch_api/routes/mod.rs`; `core4/native-chain/src/bin/launch_api/routes/transactions.rs`. Contribution commit/reveal handlers are registered. | Submission, finalization and collector integration; not verified for this publication. |
| Oracle attestation quorum | **IMPLEMENTED** | `core4/native-chain/src/bin/launch_api/routes/oracle.rs`; `oracle-reference/README.md`. Attestation/status handlers exist; the reference service is distinct from the retired Python attestation loop. | Current oracle membership, online counts and quorum availability; not verified for this publication. |
| Contribution reward accounting | **PARTIAL** | `core4/shared-protocol/src/blockchain/state.rs`; `core4/shared-protocol/src/weather/reference.rs`; `core4/shared-protocol/src/weather/station_reference.rs`. Accounting and reference-quality code exist. Reference sources, pairing windows and missing-data behavior limit what comparisons establish; the old defect report is not current validation. | Geographic fairness, deployed reference policy and credited rewards; not verified for this publication. |
| Client-signed wallet transfers | **IMPLEMENTED** | `backend/server/routes/wallet-transfer-contract.js`; `backend/__tests__/routes/wallet-signed-send.test.ts`; `mobile/lib/services/crypto/signed_transfer.dart`. Client ed25519 authorization and transfer contract exist; test source covers signed sends. | Browser/mobile-to-node submission and final settlement; not verified for this publication. |
| Wallet key scheme | **IMPLEMENTED** | `frontend/src/services/walletCrypto/firstPartyKeys.ts`; `mobile/test/services/crypto/wallet_key_scheme_vector_test.dart`; `backend/server/routes/wallet-transfer-contract.js`. BIP-39 seed → SLIP-0010 ed25519 master key; address uses the first 20 bytes of SHA3-256(public key). Signing is client-side. | Installed-client key handling and device security; not verified for this publication. |
| libp2p networking | **IMPLEMENTED** | `core4/p2p/Cargo.toml`; `infra/testnet/JOIN_TESTNET.md`. libp2p dependency and operator join instructions exist. | Public peering, NAT reachability, recovery and deployed topology; not verified for this publication. |
| Public read-only explorer/map/search stage | **PARTIAL** | `frontend/src/config/features.ts`; `frontend/src/components/explorer/PublicReadOnlyExplorer.tsx`. Read surfaces exist behind explicit public-read configuration. | Published build flags, privacy/rate-limit gates and endpoint reachability; not verified for this publication. |
| Forecast scoring and forecast products | **PARTIAL** | `core4/forecast-score/Cargo.toml`; `forecast-score/README.md`; `meteo-types/README.md`. Chain scoring and standalone reference libraries exist. Standalone scoring/types do not establish consensus compatibility or payouts. | End-to-end forecast acceptance, truth coverage and credited rewards; not verified for this publication. |
| Standalone DeFi quote service | **PARTIAL** | `defi-protocols/README.md`; `defi-protocols/docs/adr/0002-settlement-and-custody.md`. Opt-in simulator is read/quote-only with simulated:true; no custody, settlement or chain writes. | A running quote service; balance-moving functionality is unavailable; not verified for this publication. |
| L2 Optimistic/ZK rollups | **PLANNED** | `smart-contracts/README.md`. Reference protocol sources are not a deployed EVM or active testnet rollup. | Rollup deployment and live integration; not verified for this publication. |
| DAG environmental-data sidechain | **PLANNED** | `core4/native-chain/src/bin/launch_api/routes/transactions.rs`; `storage-providers/README.md`. Current contribution route is L1 commit/reveal; storage clients are not evidence of a live DAG sidechain. | Sidechain deployment and storage-network integration; not verified for this publication. |
| Stake slashing for bad observations/validations | **PARTIAL** | `core4/shared-protocol/src/blockchain/state.rs`; `core4/shared-protocol/tests/station_owner_slash_identity_activation_3214.rs`; `core4/shared-protocol/src/security/slashing.rs`. Slashing code exists. Station-owner identity handling is activation-gated and ships unscheduled; pre-activation reveal-time deduction still uses a station identity. Owner to confirm any activation decision. | Active policy, activation schedule and actual balance deductions; not verified for this publication. |
| WRC-20, carbon-credit, ESG, and RWA marketplaces | **PLANNED** | `smart-contracts/README.md`; `frontend/src/config/features.ts`. Reference contracts and gated UI do not establish served marketplaces. | Deployment, settlement and marketplace operation; not verified for this publication. |
| Cross-chain value movement | **NOT OFFERED** | `frontend/src/pages/NewWalletPage.jsx`; `smart-contracts/README.md`. Wallet labels bridging unavailable for testnet launch; reference contracts are not deployed bridge evidence. | Cross-chain integration; no balance-moving bridge is offered; not verified for this publication. |
| Mainnet or production service | **NOT OFFERED** | `core4/docs/TESTNET_DISCLAIMER.md`. Test-network scope only; no migration to mainnet is promised. | Production readiness; no mainnet service is claimed; not verified for this publication. |
| Operator status page (/dashboard) | **IMPLEMENTED** | `core4/native-chain/src/bin/launch_api/routes/status_page.rs`; `core4/native-chain/src/bin/launch_api/routes/mod.rs`. Dashboard handler and route are on main and ship in the Windows node preview 3 installer (v0.3.0). | Deployed page, operator access and current readings; not verified for this publication. |
| Production freshness (/node/resources) | **IMPLEMENTED** | `core4/native-chain/src/bin/launch_api/routes/network.rs`. Resource response derives producing/stalled from tip age; missing tip reports stalled. This is telemetry, not a consensus guarantee. | Current production state and deployed response; not verified for this publication. |
| Same-origin admin guard | **IMPLEMENTED** | `core4/native-chain/src/bin/launch_api/routes/origin.rs`. Guard handles same-origin browser access alongside Host checks. | Deployed guard behavior and access configuration; not verified for this publication. |
| Uptime from process boot | **IMPLEMENTED** | `core4/native-chain/src/bin/launch_api/main.rs`; `core4/native-chain/src/bin/launch_api/routes/chain.rs`; `core4/native-chain/src/bin/launch_api/routes/network.rs`. Startup initializes uptime clocks before requests. | Deployed process uptime; not verified for this publication. |
| Offline forecast receipt signer | **IMPLEMENTED** | `core4/tools/cli/WrfcoinCLI/src/forecast_receipt.rs`. Offline producer binds chain identity and self-verifies; production custody uses PKCS#11, file keys are debug rehearsal-only. Creating a receipt does not submit it or establish oracle membership. | Authorized signer custody, scoring policy, consensus acceptance and deployment; not verified for this publication. |
| Forecaster kit | **PLANNED** | `docs/testnet/forecasting.md`. Post-GO kit is not merged; published guide describes a preview and validate-only preparation, not an installed product. | Kit publication, integration and payout readiness; not verified for this publication. |
| Downloads page and signed manifest | **PARTIAL** | `frontend/src/pages/PublicDownloadsPage.jsx`; `frontend/src/services/downloadsManifest.ts`; `infra/testnet/edge/downloads.caddy`; `mobile/docs/RELEASING.md`. Page/parser and manifest, checksum and detached-signature serving paths exist. The live manifest publishes the unsigned Windows node preview 3 installer; signed downloads remain pending in the guide. Metadata display does not prove signature verification. | Signed manifest/artifacts, signer identity, public URLs and installation; not verified for this publication. |
| Web Send | **IMPLEMENTED** | `frontend/src/config/features.ts`; `frontend/src/components/wallet/v2/SendModal.jsx`; `frontend/src/pages/NewWalletPage.jsx`. Password-confirmed Send UI is wired to wallet submission, gated by public/operator configuration and wallet identity. | Published flags, unlocked-wallet behavior and settled on-chain sends; not verified for this publication. |

<details>
<summary>Previous assessment — 2026-09-20 (endpoint note 2026-09-24)</summary>

**Historical runtime evidence, not current status:** deployment/image comparisons, attester counts, endpoint reachability and default-feature observations below have not been reverified. Private issue references describe only the previous assessment and are not evidence for the refreshed matrix. Public snapshots do not carry those threads.

## Historical capability matrix (2026-09-20; runtime claims stale)

| Capability | Status | Evidence and boundary |
|---|---|---|
| Single Proof-of-Publication L1 | **IMPLEMENTED** | `core4/native-chain/src/bin/launch_api` serves chain and transaction routes; the active native-chain path instantiates Proof of Publication. Other consensus-engine crates are not active engines. |
| Environmental commit → reveal | **IMPLEMENTED** | `POST /transactions/contribution/commit` and `/reveal` are registered in `core4/native-chain/src/bin/launch_api/routes/mod.rs`; request handling lives in `routes/transactions.rs`. |
| Oracle attestation quorum | **IMPLEMENTED** | `POST /transactions/oracle/attestation` and `GET /transactions/oracle/status` are served by `routes/oracle.rs`. The testnet registers three attesters with a quorum of two, but only two of them run online; the third is kept offline. Losing either online attester therefore stops contributions from finalizing, even while blocks continue. |
| Contribution reward accounting | **PARTIAL** | Reward state and status routes run, but core4#3240 (private) tracks a location-reference defect that can make reward comparisons unfair. Do not describe rewards as geographically production-ready. |
| Client-signed wallet transfers | **PARTIAL** | Current code requires ed25519 client signatures and exposes submit/nonce reads; the status-date deployment predates these changes. See core4#3251–#3253 and backend#1189 (private). |
| Wallet key scheme | **IMPLEMENTED** | New wallets use ed25519: BIP-39 seed with empty passphrase → SLIP-0010 ed25519 master key (no child path); address is the first 20 bytes of SHA3-256(public key), hex-prefixed with `0x`. Legacy secp256k1 addresses are receive-only. The client signs; the backend does not hold wallet keys. Decision: core4#3234 (private). |
| libp2p networking | **IMPLEMENTED** | The `core4/p2p` crate uses libp2p and the node has feature-gated peer/DHT routes. This does not by itself prove every supervision or recovery path; core4#3229 (private) remains owner-held. |
| Public read-only explorer/map/search stage | **PARTIAL** | Frontend and edge support exist, but the feature is off by default and requires privacy/rate-limit/deployment gates. Decision: frontend#349 (private). |
| Forecast scoring and forecast products | **PARTIAL** | Canonical forecast-score/meteo code exists in core4, but a competitive end-to-end public forecasting product is not established. Decision: core4#3242 (private). |
| Standalone DeFi quote service | **PARTIAL** | The accepted scope is read/quote-only and every response must say `simulated:true`; no route may move a balance until a later decision. Decision: defi-protocols#72 (private). |
| L2 Optimistic/ZK rollups | **PLANNED** | Target architecture only; no active rollup is part of the testnet. |
| DAG environmental-data sidechain | **PLANNED** | Target architecture only; today's observation path uses backend/collector ingestion and L1 commit/reveal/attestation. |
| Stake slashing for bad observations/validations | **PARTIAL** | On core4 `main` (not verified against the deployed images): a contributor whose reveals reach attester quorum and are scored low quality three times in a row is slashed 15 base units (0.00000015 WRF) under the default policy, enforced from block height 0. A separate reveal-time slash for out-of-range data exists but has no effect, because it uses the station ID instead of an account as the slash identity — core4#3214 (private). Validators can be slashed for equivocation (signing two different blocks at the same height). Owner ruling 2026-09-21: station owners are to be slashed for bad data; that design is owner-held in core4#3218 (private) and is not active. |
| WRC-20, carbon-credit, ESG, and RWA marketplaces | **PLANNED** | Examples and design direction, not currently served products. |
| Cross-chain value movement | **NOT OFFERED** | Compatibility/status surfaces may exist, but this cut does not offer a route that moves balances across chains. |
| Mainnet or production service | **NOT OFFERED** | No mainnet exists and the private testnet is not a production service or financial commitment. |


</details>

## Testnet access

Public launch is scheduled for **2026-10-22**. Testnet WRF has no monetary value, and the network may be reset.

The launch publication plan includes code repositories as well as these docs. Core4, backend, frontend, mobile, infra, smart-contracts and docs are published as filtered snapshots; the other selected public repositories retain their histories. Repository publication, signed artifacts and deployment are separate milestones. Signed downloads are **not yet published**; see the downloads guide above.

Use current endpoint responses and the node-status guide to assess reachability. This source matrix does not certify public availability, reward settlement or launch GO.
