# Public testnet facts

Launch briefing: **2026-10-22**; source and owner-plan review: **2026-10-19**; software availability updated **2026-10-31**. Not a live-network audit.

- **Test assets:** testnet WRF has no monetary value, the network may reset, and no mainnet migration is promised ([quickstart](quickstart.md)).
- **Signed releases:** signed downloads are not yet published, and the owner's signing-key/keystore step is scheduled after launch without a promised release date. The Windows node preview 3 installer (v0.3.0) is published **unsigned** with a SHA-256 checksum, so Windows SmartScreen warns before it runs ([software availability](downloads.md)).
- **Platforms:** Linux and macOS join with Docker; only Linux x86_64 has join validation recorded, Intel Mac is supported and Apple Silicon joining is unvalidated. Windows uses a native preview installer, not WSL or Docker, and is not yet a validated join platform ([platform table](downloads.md#sync-node--docker-on-linux-and-macos)). Joining as a sync node needs no invite.
- **Source history:** core4, backend, frontend, mobile, infra, smart-contracts and docs begin publicly with a filtered source snapshot to keep private operational and development records private, and subsequent development continues in those public repositories ([publication status](../STATUS.md#testnet-access)).
- **Capabilities:** implemented code, partial integrations and experimental or planned capabilities are different categories, and source presence does not establish deployed availability ([implementation status](../STATUS.md)).
- **Producers:** the owner's launch configuration has three owner-run block producers, so this is a permissioned testnet for now and joining as a sync node does not grant block-production authority ([sync-node guide](quickstart.md#6-running-a-node)).
- **PR checks:** the public-launch CI policy uses hosted runners for pull requests and reserves heavier self-hosted suites for main/manual runs, so a passing PR proves only the checks actually executed at that head, not live deployment, device acceptance, payouts or launch readiness ([contribution and evidence guidance](https://github.com/wrfcoin/core4/blob/main/CONTRIBUTING.md)).
- **No-Origin default:** the node defaults `WRFCOIN_API_ALLOW_NO_ORIGIN` to `1` for clients such as curl, subject to Host checks and separate browser/admin-origin rules; this is not an authentication bypass ([origin policy](https://github.com/wrfcoin/core4/blob/main/native-chain/src/bin/launch_api/routes/origin.rs)).
- **Operator credential:** the node configures one operator bearer credential through `WRFCOIN_OPERATOR_TOKEN` for administrative access, distinct from contributor, oracle and reader roles ([token configuration](https://github.com/wrfcoin/core4/blob/main/native-chain/src/bin/launch_api/main.rs)).
- **Node dashboard:** each node serves its own dashboard at `http://127.0.0.1:8556/dashboard`; it is on core4 main and in the Windows preview 3 installer. Its Content-Security-Policy is `default-src 'none'` with inline script/style allowances, same-origin connections and data images ([source](https://github.com/wrfcoin/core4/blob/main/native-chain/src/bin/launch_api/routes/status_page.rs)).

The producer count and signing schedule are owner-reported launch facts; they are not independently measured here.

For current access and support, use the [quickstart](quickstart.md), [node-status guide](node-status.md) and [testnet support](https://github.com/wrfcoin/testnet-support); report vulnerabilities privately through [SECURITY.md](../SECURITY.md).
