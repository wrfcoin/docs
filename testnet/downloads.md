# Get the software

For the proposed forecaster workflow and its current limits, read [Forecasting on the testnet](forecasting.md).

Use WRFCoin on the web, run a sync node, or build from source. **This is a test
network: testnet WRF has no monetary value and balances may be reset.** Start
with the [public testnet quickstart](quickstart.md).

## Web wallet — no install

Open [wrfcoin.com](https://wrfcoin.com) in your browser to create or import a
wallet, request test tokens, and send or receive WRF. See the
[wallet steps](quickstart.md#1-get-a-wallet). Keep your recovery words offline
and private.

## Sync node — build locally from source

A sync-only full node follows the testnet chain and serves a local API. It does
not produce blocks. You need git, Docker with Compose v2, and the
[infra](https://github.com/wrfcoin/infra) and
[core4](https://github.com/wrfcoin/core4) repositories. WRFCoin node images are
built locally; no prebuilt WRFCoin registry image is offered.

The platform table below is taken from
[`infra/testnet/JOIN_TESTNET.md`](https://github.com/wrfcoin/infra/blob/main/testnet/JOIN_TESTNET.md),
with an explicit Windows entry because that guide does not list Windows.
Linux x86_64 is validated; Intel Mac is supported; Apple Silicon has a native
build path but an end-to-end join is not yet validated.

| Platform | Status | Notes |
|----------|--------|-------|
| **Linux x86_64** | ✅ Supported | Builds natively. |
| **Intel Mac (x86_64)** | ✅ Supported | Builds natively. |
| **Apple Silicon (M1/M2/M3, arm64)** | **Native build, join still unvalidated end-to-end** | The image builds **natively on arm64** — no emulation, no opt-in, same command as everyone else (infra#763). Optionally run `bash join-testnet-sync-node.sh --preflight` first: it refuses unless Docker actually runs a native `aarch64` container, without generating `.env` or starting services. Emulation remains available as `--emulate` if a native build ever fails. Run this from a **native arm64 terminal** — a Rosetta shell reports `x86_64` and would build the slow emulated image; the script detects that and stops. |
| **Windows (including WSL2 / Docker Desktop)** | **Not yet validated** | Not listed in the join guide; no Windows join validation is claimed. |

Before starting, use the [node operator quickstart](quickstart.md#6-running-a-node)
and request the current peer details and snapshot checksum through
[testnet support](https://github.com/wrfcoin/testnet-support/issues/new/choose).
The join path currently requires operator coordination; the platform table is
not evidence that unassisted public-internet joining is available.

## Node status page — in progress

The planned local status page is `http://localhost:8556/dashboard`.
Read [what each status panel means](node-status.md).
It is still under development; do not assume it ships
with your current node build. Until then, inspect chain information locally:

```bash
curl http://localhost:8556/network/info
```

## Android APK — coming soon

The public launch APK is not published yet. Use the web wallet until a signed
build and its SHA-256 checksum appear on
[wrfcoin/mobile GitHub Releases](https://github.com/wrfcoin/mobile/releases).
See the [release preparation guide](https://github.com/wrfcoin/mobile/blob/main/docs/RELEASING.md). A successful unsigned compile is not a public release.

The app provides the wallet and phone-as-a-station flow described in the
[quickstart](quickstart.md#in-the-android-app-coming-soon). Device and public API
acceptance are still release prerequisites. No APK filename, size, checksum or
download button is advertised here before the signed release exists.

## Command-line wallet — source only

Build the CLI from the [core4 source](https://github.com/wrfcoin/core4), using its
Rust toolchain instructions. From the core4 repository root:

```bash
cargo build --release -p wrfcoin_cli
```

No prebuilt CLI binary is offered on this page. Follow the repository's CLI
instructions and confirm the testnet chain/network configuration before use.

## Weather stations

- **Ambient Weather:** connect through the website's **Connect a station** flow;
  see the [station quickstart](quickstart.md#an-ambient-weather-station-website).
  Enter provider credentials only in that form, never in a public issue.
- **Phone as a station:** uses the Android app once the signed release is
  available; follow the [phone steps](quickstart.md#a-phone-as-a-station-android-app-once-available).
- **Radio receivers (`rtl_433`):** experimental; not part of the website's
  self-service station connection flow.

A registered station or uploaded observation is not proof of a reward payment.

## For developers

Browse the [WRFCoin repositories](https://github.com/wrfcoin), including
[core4](https://github.com/wrfcoin/core4),
[backend](https://github.com/wrfcoin/backend),
[frontend](https://github.com/wrfcoin/frontend) and
[mobile](https://github.com/wrfcoin/mobile). Follow each repository's build and
contribution instructions. The node exposes Prometheus metrics at `GET /metrics`
on its local API; use your node's configured access controls.

See [contributing](../CONTRIBUTING.md) and the [implementation status](../STATUS.md)
for documentation and capability boundaries.

## Verify what you download

Use GitHub Releases under the [wrfcoin organization](https://github.com/wrfcoin)
and check the source commit and release notes. For the forthcoming Android
release, download the signed APK and its accompanying `SHA256SUMS` from the same
release. In the directory containing those files:

```bash
sha256sum -c SHA256SUMS
```

On macOS use `shasum -a 256 -c SHA256SUMS`. On Windows use
`certutil -hashfile <file> SHA256` and compare the complete value with the
published checksum. A matching hash checks bytes against the trusted checksum;
it does not by itself establish who signed an APK. Use the signer information
published with the release as well.

For a node, follow the join guide's source and snapshot verification steps.
WRFCoin publishes no prebuilt node images to container registries; the node
image is built locally from source. This does not mean the build avoids upstream
base images or dependency downloads. Do not substitute sample hashes or a
mockup's manifest for published release evidence. A signed download manifest is
not advertised as available here.

If a checksum differs or a download seems suspicious, stop and email
**security@wrfcoin.com**; see the [security policy](https://wrfcoin.com/security).

*Status checked 2026-10-19. Platform status comes from the join guide; Android
publication and the local dashboard remain pending as described above.*
