# WRFCoin public testnet quickstart

> **Chain 888 publication:** balances restart from the new genesis; previous-chain balances and activation heights do not carry over. The owner must publish the genesis hash and confirm the cut before this guide is used.

For the proposed forecaster workflow and its current limits, read [Forecasting on the testnet](forecasting.md).

WRFCoin is a public blockchain for weather data. Personal weather stations and phones contribute observations, forecasts are published against them, and the chain rewards the contributions it can verify. The public testnet opened on **2026-10-22**.

> **This is a test network.** It may be reset without notice. Balances and tokens have no monetary value. No migration to a mainnet is promised or implied. The network is deliberately attacked on a schedule as part of testing, so use only disposable test assets. Nobody on the team will ever ask for your recovery words or your station's API keys.

This guide covers the website at **<https://wrfcoin.com>** and the Android app. **Android app status:** the launch build is not published yet. Until it appears on the [wrfcoin/mobile Releases page](https://github.com/wrfcoin/mobile/releases), use the website; the app sections below describe what the app does once it is available.

For software availability, platform status and checksum instructions, see
[Get the software](downloads.md).

[Read the facts page](facts.md) for release, platform, network and validation boundaries.

## 1. Get a wallet

You need one wallet. Create it on the website (or, once the app is available, in the Android app), then keep using the same wallet everywhere. A wallet is a 12-word recovery phrase; the words are the wallet. Write them down, in order, somewhere offline and private. Anyone who has them can spend from the wallet, and nobody can restore a wallet for you without them.

### On the website

1. Open <https://wrfcoin.com> and choose **Get started** from the menu.
2. Choose **Create New Wallet**, or **Import Recovery Phrase** if you already have a wallet from the app.
3. Set a **Browser password** (at least 8 characters) and confirm it. This password only encrypts the copy kept in this browser; it is not part of your recovery phrase and cannot recover the wallet if you lose the words.
4. **Back up your recovery words.** Write down the 12 words, confirm you have stored them outside the browser, and complete the word check.
5. Choose **Save and Connect Wallet**. Next time, **Unlock Wallet** with your browser password.

Clearing the browser's site data removes the browser copy. That is fine as long as you have your words: import them again.

### In the Android app (coming soon)

The app turns a phone with a barometer into a weather station as well as holding a wallet. When the launch build is published on the [wrfcoin/mobile Releases page](https://github.com/wrfcoin/mobile/releases), install it from there and compare the file's SHA-256 checksum with the one published next to it before installing. Install only builds published there or linked from <https://wrfcoin.com>.

1. Open **Earnings → Create Wallet → Generate Wallet**. Write down the 12 recovery words in order, tap **I've written it down**, complete the word checks, then **Complete Setup**.
2. If you already have a wallet, choose **Import / Restore Wallet** and check that the restored address matches the one you saved.
3. Approve wallet requests locally with your fingerprint or PIN when the app asks.

Do not uninstall the app, or clear the browser, until the recovery words and the address are written down.

## 2. Get test tokens from the faucet

The faucet gives testnet WRF so you can try transactions. Follow the currently displayed amount, cooldown and per-wallet/shared caps; old-chain limits do not establish the new service policy. A pending request is not a confirmed payment. Testnet WRF has no monetary value.

The proposed one-time grant pays **250.36 WRF to the bond owner account**, requested with a claim signed by your node's bond server key. The owner must then submit the bond Deposit; the faucet does not escrow the grant or force the Deposit. It is **OFF until announced**. See the deployed flow for availability and current limits; this guide does not verify deployment or invent a claim endpoint. Recheck against the merged faucet implementation before publication. The ordinary wallet faucet is a separate flow.

During launch week, request the bond grant from the operator by opening a **Node operator help** issue in [wrfcoin/testnet-support](https://github.com/wrfcoin/testnet-support/issues/new/choose); there is no self-serve bond-grant route this week.

- **Website:** on the **Get started** page, scroll to **Fund Your Wallet** (the testnet faucet), answer the verification challenge, and claim. **Tokens Claimed!** confirms that the request was accepted.
- **Android app (once available):** open **Earnings → Get Testnet Tokens**, check that **Tokens will be sent to** shows your own address, tap **Request Testnet Tokens**, answer the challenge, then **Claim Tokens** once.

Keep the transaction hash the faucet returns in case you need support. If the page says the faucet is not funded, or a claim is pending or in cooldown, wait rather than claiming again.

## 3. Receive and send WRF

Open **Wallet** from the website menu (or the wallet screen in the app).

- **Receive.** The page shows **Your WRFCoin address** with a QR code and a **Copy address** button. Give that address to whoever is sending to you. Addresses look like `0x` followed by 40 hex characters.
- **Balance and earnings.** The wallet page shows your balance, reward totals (**Weather pending**, **Weather paid**, **Total earned**) and recent activity. A pending reward has not been paid yet.
- **Send.** Choose **Send WRF**, enter the recipient's address and the amount, choose **Review transfer**, enter your wallet password for this send, and choose **Confirm & Send**. The page then reports *Submitted; settlement is not yet confirmed*: the transfer is on its way, and your balance updates once the chain includes it.

Transfers are transparent (sender, recipient and amount are visible on chain) and cannot be reversed. Check the full address, character by character, and use small test amounts first. Always ask the recipient for the address shown on their own wallet page: an address copied from an older record may be a legacy receive-only address that can no longer send.

## 4. Connect a weather station

There are two ways to contribute weather data today.

### A phone as a station (Android app, once available)

1. In the app, open **Collect → Privacy center** (the shield icon in the top bar). Enable sensor and approximate-location consent and grant the location permission Android asks for.
2. Switch **Collection Paused** off so it reads **Collecting Data**, then collect a first reading from the **Collect** screen and approve the wallet request.
3. **Sync Progress & Rewards** shows readings synced to the network. Registration, upload, acceptance, attestation and payment are separate stages; a synced reading has not necessarily earned anything yet.

Saved readings expire, so keep the phone connected and let it sync. If the app removes earlier saved readings, they were not eligible; collect again.

### An Ambient Weather station (website)

1. Open **Connect a station** from the website menu, with your wallet unlocked.
2. Choose the **Ambient Weather** provider and enter your **Ambient API Key** and **Ambient Application Key** in that form only. Never paste them into an issue, a chat or an email. The page reports **Your keys are valid.** when they verify.
3. Pick the device from your Ambient account, give the station a public name with no personal details, and choose **Confirm & register**. Keep the station ID.
4. The station page then shows reward progress: observations received, attested, and rewarded.

Station readings, quality and earnings are public. Anyone can see a registered station on the **Weather map** and **Explore** pages, identified by its public alias (`st_` plus 12 hex characters) with its coordinates rounded to 0.1 degrees. Choose a neutral station name.

Other station brands and radio (RTL-SDR) receivers are not part of the self-service flow yet. If you have one, say so in a [feature request](https://github.com/wrfcoin/testnet-support/issues/new/choose).

### How rewards work

The chain pays for observations it can verify. A reading is accepted, attested by the network's oracle attesters, scored for quality, and then rewarded; each stage is reported separately on the wallet and station pages. Registering a station, or syncing a reading, is not a payment. The chain can penalize a contributor who repeatedly submits low-quality data.

## 5. Look around

Everything on these pages is readable without a wallet:

- **Weather map:** stations and coverage on a map.
- **Explore** and **Block explorer:** stations, the latest blocks and network activity.
- **Search:** find a block, transaction, address or station.
- **Leaderboard:** top contributors and what they have earned on chain.
- **Governance:** proposals and the treasury, read-only.
- **Forecast:** current conditions and a 7-day forecast for a place.

The **Terms**, **Privacy**, **API terms** and **Security** pages, linked from the bottom of the home page, are the rules of the testnet. Read them before you depend on anything here.

## 6. Running a node

You do **not** need a node to hold a wallet or connect a station. Node operators run a **sync-only full node**: it syncs from genesis by default (a matching snapshot is optional), follows the chain from the network's peers, keeps a full copy of the blocks, serves a local API, and can submit transactions. It does not produce blocks; block production on the testnet is done by the team's registered producer nodes, so a sync node cannot fork the network and has no signing keys to protect.

What it takes: a computer that stays on (a Linux box, a Mac or an old laptop with about 8 GB of RAM), Docker with Compose v2, and a clone of [wrfcoin/infra](https://github.com/wrfcoin/infra) and [wrfcoin/core4](https://github.com/wrfcoin/core4) side by side. The node image is built from source on your machine; the first build takes 10 to 40 minutes. The join script in `infra/testnet/` writes a local configuration, pins the node to chain ID **888**, network **testnet**, and starts a full sync. A snapshot is optional on the fresh chain. Verify the owner-published genesis hash `553a3758386d9631037d7469686acb4a121ced81dcf5cde256e2d05667c5f332` before joining; this placeholder must be replaced, not pasted as a hash. The seed is `/dns4/seed.wrfcoin.com/tcp/9000`. Plan **250.36 WRF** for bond funding and lifecycle fees; the one-time bond grant above is conditional on service availability.

The public bootstrap is `/dns4/seed.wrfcoin.com/tcp/9000`. Verify the published chain 888 pins before joining. For peering trouble or an operator-provided fallback, open a **Node operator help** issue in [wrfcoin/testnet-support](https://github.com/wrfcoin/testnet-support/issues/new/choose). A snapshot is optional; verify its chain, genesis and manifest before use.

### See what your node is doing

Today, inspect the local chain summary from the computer running your node
(with `curl` and `jq` installed):

```bash
curl -s localhost:8556/network/info | jq
```

Compare the reported chain identity with your current join instructions. Watch
height and sync state over successive readings; a positive peer count alone
does not establish that the node has caught up.

For launch week, a browser status page is in progress at
`http://localhost:8556/dashboard`.
It may not exist in your installed build yet. Read
[what each status panel means](node-status.md), including which host values need
an operator token and the current token-handoff limitation.

For Prometheus, the node exposes `GET /metrics` on its local API, subject to its
configured access controls. Keep that API local; do not expose it publicly to
view the dashboard.

## 7. Where to get help

- **Questions, problems and bug reports:** open an issue in [wrfcoin/testnet-support](https://github.com/wrfcoin/testnet-support/issues/new/choose). There are templates for wallet help, faucet help, station connection help, node operator help, bug reports and feature requests. Include what you did, what you expected, what happened (the exact message), and the app version or page. A public wallet address, transaction hash or station ID is optional.
- **Security problems:** email **security@wrfcoin.com** instead of opening a public issue. The policy is at <https://wrfcoin.com/security>. No bug bounty is promised.
- **Documentation:** [wrfcoin/docs](https://github.com/wrfcoin/docs), starting with [Implementation status](../STATUS.md) for what is implemented, partial and planned.

**Never share** your recovery words, private keys, browser password, station API keys, access tokens, precise location, or screenshots that show any of these. Nobody who is helping you needs them.

## What "unavailable" means

If a page shows *unavailable*, *pending*, *loading* or a blank value, the site does not have confirmed data for that item right now. It does not mean your balance is zero or that an operation failed. Wait and use the page's refresh or retry action. Do not create a second wallet or repeat a pending claim to work around it.

---

*Last reviewed 2026-10-19 against the live website and the public repositories. The dated [status matrix](../STATUS.md) is authoritative for what is implemented versus planned.*
