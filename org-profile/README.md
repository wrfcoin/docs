<!-- Organization profile for github.com/wrfcoin. Lives in the docs repo as org-profile/README.md; the maintainer copies it to the wrfcoin/.github repository as profile/README.md. -->

# WRFCoin

**A currency earned by contributing weather data and forecasts.**

WRFCoin is a public blockchain for weather data. Personal weather stations and phones contribute observations, forecasts are published against them, and the chain rewards the contributions it can verify. The token, WRF, exists to pay for verifiable environmental work, not to be traded: the project's measure of success is the quality and quantity of weather data published, not a price.

The long-term aim is a decentralized, hyperlocal layer of environmental data and forecasting that adds to, rather than replaces, the official weather services.

## Testnet status

The **public testnet** opened on **2026-10-22**. It is a test network: it may be reset without notice, testnet WRF has no monetary value, and no migration to a mainnet is promised or implied. The network is regularly tested against attacks as part of testing, so attach nothing you cannot afford to lose. The dated [implementation status](https://github.com/wrfcoin/docs/blob/main/STATUS.md) says what is implemented, partial and planned.

What you can do today:

- **Watch the chain** at <https://wrfcoin.com>: live block height, a weather map, a block explorer, search, the contributor leaderboard, read-only governance and a forecast page.
- **Hold a wallet** on the website or in the Android app, claim testnet WRF from the faucet, and send and receive it.
- **Contribute weather data** from an Ambient Weather station or from a phone with a barometer, and earn testnet WRF for observations the chain can verify.
- **Run a sync node** that follows the chain and serves a local API.

Start with the [quickstart](https://github.com/wrfcoin/docs/blob/main/testnet/quickstart.md).

## Repositories

| Repository | What it is |
| --- | --- |
| [core4](https://github.com/wrfcoin/core4) | The Rust blockchain: node runtime and API, Proof-of-Publication consensus, commit/reveal of observations, oracle attestation, rewards, P2P and the CLI. |
| [backend](https://github.com/wrfcoin/backend) | Node.js/TypeScript API services behind the website and the app: wallet auth, faucet, station registration, weather ingestion, earnings and leaderboard. |
| [frontend](https://github.com/wrfcoin/frontend) | The React website at wrfcoin.com: public pages, web wallet, station onboarding, explorer and map. |
| [mobile](https://github.com/wrfcoin/mobile) | The Flutter Android app: wallet, phone-as-a-station data collection, earnings and leaderboard. |
| [infra](https://github.com/wrfcoin/infra) | Docker Compose stacks, the public edge configuration, monitoring, deployment scripts and the testnet node join tooling. |
| [docs](https://github.com/wrfcoin/docs) | Whitepaper, implementation status, the quickstart and testnet notes. |
| [testnet-support](https://github.com/wrfcoin/testnet-support) | Where testnet participants ask for help and report bugs, with issue templates for wallet, faucet, station and node questions. |
| [smart-contracts](https://github.com/wrfcoin/smart-contracts) | Solidity contracts (token, staking, governance, carbon credits, data validation) that mirror planned protocol features; not part of the running testnet chain. |
| [defi-protocols](https://github.com/wrfcoin/defi-protocols) | Rust DeFi protocol crates (lending, AMM, yield, liquid staking) and a read-only quote service; simulator only, it moves no balances. |
| [storage-providers](https://github.com/wrfcoin/storage-providers) | Rust storage clients and tiering libraries; the testnet profile uses a self-hosted IPFS node. |
| [oracle-reference](https://github.com/wrfcoin/oracle-reference) | Independent reference-verification service for the oracle: serves gridded reference weather values from public model and observation datasets. |
| [meteo-types](https://github.com/wrfcoin/meteo-types) | Canonical Rust types for meteorological observations, kept for reference; the node compiles its own copy inside core4. |
| [forecast-score](https://github.com/wrfcoin/forecast-score) | Forecast verification metrics (the standard scores used in numerical weather prediction); non-authoritative for chain scoring. |

Most repositories are licensed under MIT or Apache-2.0 at your option; each repository's LICENSE file is authoritative.

## Links

- Website and testnet: <https://wrfcoin.com>
- Quickstart: <https://github.com/wrfcoin/docs/blob/main/testnet/quickstart.md>
- Whitepaper: <https://github.com/wrfcoin/docs/tree/main/whitepaper>
- Help and bug reports: <https://github.com/wrfcoin/testnet-support/issues/new/choose>
- Security reports: **security@wrfcoin.com** (please do not open public issues for vulnerabilities); policy at <https://wrfcoin.com/security>
- Contributing: each repository has a `CONTRIBUTING.md` and follows the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) code of conduct.
