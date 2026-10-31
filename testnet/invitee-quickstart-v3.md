# WRFCoin closed-testnet invitee quickstart (v3)

> **Superseded for chain 888:** use the [public testnet quickstart](quickstart.md). Network: `testnet`; genesis: `553a3758386d9631037d7469686acb4a121ced81dcf5cde256e2d05667c5f332` (published at launch, 2026-10-22). The historical release receipts below do not verify this genesis, balances, faucet policy or station activation.

> **Public launch (2026-10-22):** this closed-testnet guide is kept for history. New participants should use the [public testnet quickstart](quickstart.md).

Supersedes `invitee-quickstart-v2.md`, which stays as history. This guide is ready for owner review; distribution is PENDING the owner’s D7 decision. Join only after the team announces your invitation and confirms the release. Use only the team-provided invitation, APK and website links. These are test tokens on a test network (see **Testnet disclaimer** below). The team will never ask for your recovery words or station API keys. The phone path below needs an Android phone with a barometer. The team confirms which APK is approved before you start.

**Status, honestly.** The website and API tier has been running release r20.2 since 2026-10-07 (about 21:05Z, owner/team-reported): backend `dec7b920`, frontend `fc2e4268`, infra `b049e992`. The earnings leaderboard API is live (public, read-only); the first invitee-facing view is the phone app's **Profile** tab (the **Leaderboard** tab inside it) from the GO APK. There is no website leaderboard page for invitees yet. An advisory reference-shadow sidecar also runs; it changes no invitee step. Test tokens and test earnings have no monetary value.

1. **Join and install.** Accept the Tailscale invitation with your invited account and keep Tailscale connected. Invitees belong to `wrfcoin-invitees`; app access is TCP port 9444 only (the phone app talks to the team's API at port 9444, path `/api`, over Tailscale; this is for tailnet invitees only). Install the APK from the trusted link and compare its supplied checksum. For an update, keep your existing app and data. If Android refuses the update, ask for a compatible APK; do not uninstall a wallet until its recovery backup and address are recorded.
2. **Back up one wallet.** Open **Earnings → Create Wallet → Generate Wallet**. Write down the **12 recovery words**, in order, offline and privately. Tap **I've written it down**, complete the requested word checks, then **Complete Setup**. For an existing wallet, choose **Import / Restore Wallet** and compare its restored address with your saved address. Keep the same wallet for your phone station and any later browser access. Use **Sign in** if prompted and approve locally with your fingerprint or PIN. Never send the words to support or paste them into a browser's storage, chat or email.
3. **Give collection consent.** Open **Collect → Privacy center** using the shield in the top bar. Enable sensor and approximate-location consent and the requested Android location permission. Turn **Collection Paused** on so it reads **Collecting Data**, then tap **Collect Now** once and approve the wallet request. Registration alone does not activate your station or earn a reward.
4. **Wait for activation.** If your station is awaiting activation, pause collection and wait for the team's activation announcement. Return with the same wallet signed in; let resume sync finish, then use **Refresh station status**. Unavailable or cached status does not confirm activation. After activation is confirmed, resume collection and collect a fresh reading. Saved readings expire; reconnect and sync promptly. A notice that earlier saved readings were removed means they were ineligible and cannot earn payment; collect again after that operation finishes.
5. **Check the first reading.** **Sync Progress & Rewards** reports readings synced to the backend. Upload, acceptance, attestation and payment are separate stages. A pending reading has not yet earned. Check **Earnings**: **Weather pending** and **Weather paid** distinguish the reported stages, and **Total earned** reports reward totals in WRF. Wait for accepted, rewarded reading evidence and chain confirmation; collection is not a payment guarantee. A faucet grant can change your balance without being weather earnings.
6. **Claim test tokens only when invited to.** For chain 888, wait for the service opening and funding announcement; the previous genesis activation is not evidence for this chain. Use **Earnings → Get Testnet Tokens**. Check **Tokens will be sent to** is your saved address, tap **Request Testnet Tokens**, answer the challenge, then **Claim Tokens** once. Keep the returned transaction hash and follow pending or cooldown instructions. Follow the displayed claim cooldown. Per-wallet and shared network-wide daily caps also apply; consult the current service policy. Use the displayed service amount; do not expect a particular grant or submit repeated claims. You can register and await activation before claiming.

## Browser joining when the team announces it

The website is a separate link from the phone API. The app's 9444-only access does not open a dashboard port. Begin browser joining when the team announces that release, at the exact `/onboarding` page, and use the same wallet as your phone.

Choose **Create New Wallet** or **Import Recovery Phrase**. Set and confirm a **Browser password** of at least 8 characters, then choose **Generate Recovery Words** or **Review Backup**. Write down your 12 words privately and complete backup verification before connecting. Your words are kept only encrypted in this browser, unlocked by your password. The browser copy is not your backup: a forgotten password or cleared browser data cannot recover it; keep your written words to restore the wallet. When a vault already exists, use **Unlock Wallet** with your browser password. Never paste the words anywhere else or send them to support.

The exact `/wallet` page shows **Your WRFCoin address** and your own phone-station status; it does not promise a browser reward balance. For an Ambient Weather station, `/connect-station` and `/earn` open the same station flow. Use the same signed-in wallet, enter **Ambient API Key** and **Ambient Application Key** only in the approved form, select your account's device and choose a public station name without personal details. Do not send keys to support. Follow **Confirm & register**, keep the station ID, and wait for the displayed observation/attestation/reward progress. An Android phone still collects its readings in the APK; connecting Ambient does not register a phone station.

## When something is unavailable

**Not available**, unavailable, loading, pending or a blank reported value means the app lacks confirmed evidence for that item. It does not mean zero rewards or a successful operation. Keep Tailscale connected, check sign-in and try the displayed refresh action later. Do not generate another wallet or repeat a pending claim to work around it. Unsupported previews such as DAG data can remain unavailable while the supported reading path works.

Report ordinary bugs at [the private testnet-support issues page](https://github.com/wrfcoin/testnet-support/issues) using your invited GitHub account; access is granted when you are invited. Send security concerns directly to [tony@wrfcoin.com](mailto:tony@wrfcoin.com) with `[SECURITY]` in the subject, rather than posting them in an issue; expect an acknowledgement within two business days. Include the exact message and app version, plus a station ID or public wallet address only if relevant. Never include recovery words, API keys, tokens, location details or screenshots that contain them. Wallet **Send** is ON for invitees in the GO APK (owner ruling 2026-10-07; the owner enables it per build, so an earlier test APK may not show it): use **Send** on the wallet screen, check the recipient address character by character, and use small test amounts. A submitted send cannot be undone, and the testnet may be reset.

## Public station reads and the leaderboard (ON)

Station reads are **on** at the website edge (owner ruling 2026-10-05, `PUBLIC_READONLY_API=on`, live since r20). The public station list and each station's observations, quality, submissions, earnings and ownership-state reads answer. Anonymous readers see station coordinates coarsened to 0.1 degrees and address a station only by its public alias (`st_` plus 12 hex characters), never by its raw id. The edge admits only exact queries: the list, earnings and ownership take none; observations, quality and submissions take none or exactly `limit=1`. A request with another query (for example `limit=100`) answers 404. These reads are visible to anyone who can reach the edge, so use a neutral public station name. Released weather days are also archived to IPFS (r20.1); this changes no invitee step.

**Earnings leaderboard.** The public read-only API has been live since r20.2 (owner ruling 2026-10-06). Invitees see it in the phone app's **Profile** tab (the **Leaderboard** tab inside it) from the GO APK (mobile#417); the website also has a read-only leaderboard page (below). It shows chain earnings, with earnings as the default view. The edge admits one exact query shape, `metric=<earnings|submissions|quality_score|streak>&period=<7d|30d|all>&limit=<1..30>` in that order; anything else (no query, another order, extra parameters, any country/region/near filter) answers 404. When the leaderboard cannot be read, the app shows an error with **Retry**, not an empty board. A row on it is not a payment confirmation for your station.

**Web leaderboard page:** `https://wrfcoin-testnet.taila1c049.ts.net/leaderboard/contributors`. It is read-only and shows the same chain earnings as the phone's Leaderboard tab. No sign-in is needed.

## Testnet disclaimer

This is the team's canonical text (core4 [`docs/TESTNET_DISCLAIMER.md`](https://github.com/wrfcoin/core4/blob/main/docs/TESTNET_DISCLAIMER.md), current source path):

> This is a test network. It may be reset without notice. Balances and tokens have no monetary value. No migration to mainnet is promised or implied. Please attach no production bridges, exchange listings or irreplaceable assets.
>
> This experimental network is an adversarial test environment: it is deliberately attacked on a schedule. Please use only disposable test assets.

## Station owner actions (after the station-protection switch-on)

On chain 888, station owner actions require confirmation against the new genesis schedule; previous-chain activation receipts do not establish availability. In the approved phone app, open **Collect** and use **Security** to report a lost or stolen station, unfreeze it when it is safe, or deactivate/reactivate it. To transfer a station, the new owner opens **Accept** and shares their receive code; the current owner uses **Transfer**, reviews the request, and shares it back for the new owner to accept. Use the wallet that owns the station; unfreeze a frozen station before transferring it. A submitted request is pending until the network ledger confirms the change. If status is unavailable, wait and check again; do not treat submission as confirmation.

## Availability checklist

Evidence-backed items cite what supports them. PENDING items need the owner or you. Unchecked items are not release evidence.

- [x] **Website release:** served r20.8 revisions are backend `4d27c8da6a1ea16cb48caa82b81493bb2ca788d4`, frontend `c97d5232` and infra `c9badeec` (live since 2026-10-13 20:44Z; `GET /api/build` shows the backend stamp `4d27c8da…`, checked 2026-10-15).
- [ ] **Chain 888 faucet:** owner to confirm opening, funding and current caps; use the displayed amount. The 250.36 WRF node bond grant is separate from ordinary wallet claims.
- [x] **Activation and first reward proven for the owner’s own phone station:** team-reported 22 real decisions and 15.24 WRF earned. This proves the path works; it is **not** evidence for your station.
- [ ] **Invitation and distribution — PENDING (owner):** D7 approval, invited account and approved links supplied.
- [x] **Phone release:** owner-accepted APK `wrfcoin-accept-20261013-ac7a027-9444.apk`, SHA-256 `c9279fb5fbc01086af9d9cbebfde5c819f907e8c6615ad2af3482816daf89634`. It was installed 2026-10-13 as an in-place update (same signer, data kept). Owner acceptance 2026-10-15: wallet, Send, leaderboard and data collection.
- [ ] **Your activation — PENDING (each invitee):** team’s activation receipt and your station’s own status confirmed. Registration and backend sync do not confirm payment.
- [ ] **Your first reward — PENDING (each invitee):** accepted observation, attestation, reward and chain-confirmation evidence for your own station. Pending is not paid.
- [x] **Leaderboard API:** served by backend `dec7b920` (`weather-leaderboard-routes.ts`) behind the edge matcher at infra `b049e992` (`public_onboarding.caddy:333-341`); owner/team-reported live with r20.2. This is the API only.
- [x] **Leaderboard (website):** `/leaderboard/contributors` is served by frontend `c97d5232` (r20.8) and answered HTTP 200 on 2026-10-15.
- [x] **Leaderboard (phone):** the Profile > Leaderboard tab (mobile#417) confirmed by the owner on the acceptance APK `ac7a027` (2026-10-15).
- [ ] **Chain 888 Wallet Send:** owner to confirm a matching-chain release and settled transfer. Send only to the recipient's own wallet-screen address; legacy receive-only addresses remain unsuitable.
- [ ] **Chain 888 station owner actions:** owner to confirm the recorded activation schedule and runtime availability.

Chain status and recent block lists can answer from a responding node; an outage is unavailable. Transaction lists, lookup by hash, validator lists and legacy chain stats answer **HTTP 501 by design**. A recorded transaction hash is useful for support, but this website does not promise a working lookup. Coverage-zone responses may be fallback data; do not treat them as measured coverage. Node snapshot downloads and the status document depend on owner publication; missing artifacts can return 404. None of these surfaces confirms a reward or invites public signup. A send on chain has settled live in team testing. Send was hidden in earlier invitee builds (owner ruling 2026-09-30) and is ON in the GO APK (owner ruling 2026-10-07).

## Owner source map (main source, not a served-release receipt)

Historical revisions and line numbers below are retained as plain-text provenance.
Their pre-snapshot commits are not available in the public repository; these
references do not establish current source or deployed behavior.

This appendix gives the distribution reviewer a source map for every route named here. Invitees use the supplied links and app controls; they need not call APIs. Source-admitted means the configured edge can forward a request, not that the runtime service is available. Method, path, authentication and query restrictions all still apply.

**Pins.** *Served release r20.2* (what invitees reach today, owner/team-reported): `infra b049e992`, `backend dec7b920`, `frontend fc2e4268`. All line anchors below refer to these. The edge file `testnet/edge/public_onboarding.caddy` changed from the r20.1 pin (infra 4be5b223): the leaderboard, station-ownership and owner-action matchers were added and line numbers moved.

The canonical edge is `testnet/edge/public_onboarding.caddy`. It fails closed on non-canonical paths (lines 66-71) and ends with a `/api/*` 404 (417-419). UI pages use the frontend fallback, not an API matcher; exact `/wallet` is admitted by that fallback and `PUBLIC_ONBOARDING_PATHS`. Deep variants of the other three joining pages stay blocked (`@wallet_secret_entry`, 405). The station-read gate defaults to `off` in compose (`docker-compose.edge.yml:62`, `docker-compose.funnel-edge.yml:55`); `on` is the deployed owner setting and is not visible in source. The backend coarsens anonymous coordinates to 0.1 degrees (`weather-routes.js:655` comment); the edge comments now say the reads are live.

Backend handler paths are under `server/`. Mounts in `enhanced_unified_api_optimized.ts`: blockchain 1524, weather 1531, onboarding 1577, capabilities 1621, leaderboard 1626, station detail 286, station owner 288; wallet auth is handled in the entrypoint.

| Method and route | Edge / canonical handler | Availability |
| --- | --- | --- |
| GET `/onboarding` | Exact page; frontend `src/routes/walletRoutes.jsx:18` → OnboardingPage | Source-admitted; served-build receipt via `/api/build` |
| GET `/wallet` | Frontend fallback; `src/config/contractSurfacePolicy.ts:83`, `walletRoutes.jsx:17` → OwnWalletAddress | Own address/status only |
| GET `/connect-station` | Exact page; `src/routes/earnRoutes.jsx:25` → ConnectStationPage | Ambient joining |
| GET `/earn` | Exact page; `src/routes/earnRoutes.jsx:15` → ConnectStationPage | Same station flow |
| GET `/api/auth/nonce/{addr}` | `wallet_nonce` (caddy 73-79), entrypoint 899 | Exact 0x +40 hex address; nonce challenge, no payment |
| POST `/api/auth/wallet-login` | `wallet_login`, entrypoint 909 | Signed challenge |
| POST `/api/auth/refresh` | `wallet_refresh`, entrypoint 916 | Refresh authentication required |
| POST `/api/onboarding/faucet/challenge` | `faucet_challenge`, `routes/onboarding-routes.ts:494` | Challenge only, no grant |
| POST `/api/onboarding/faucet/claim` | `faucet_claim` (caddy 105-111), `routes/onboarding-routes.ts:560`; 24h address cooldown `:71`; daily caps `infra testnet/services/faucet/server.js:53-54` | Chain 888 opening, funding and current limits require owner confirmation |
| POST `/api/weather/stations/verify-key` | `station_verify`, `routes/weather-routes.js:435` | Wallet authentication; approved form only |
| POST `/api/weather/stations` | `station_register`, `routes/weather-routes.js:291` | Wallet authentication; registration is not activation |
| GET `/api/weather/stations/{id}/reward-progress` | `station_reward_progress`, `routes/weather-routes.js:467` | Authenticated owner-scoped; pending is not paid |
| GET `/api/weather/stations/mobile` | `station_mobile_status`, `routes/weather-routes.js:427` | Wallet JWT, own row only, no query |
| GET `/api/weather/coverage-zones` | `weather_coverage_zones`, `routes/weather-routes.js:546` | Can return fallback after DB failure (587); not measured assurance |
| GET `/api/weather/stations` | `public_readonly_stations` (caddy 286-294), `routes/weather-routes.js:635` | ON; no query; alias ids, 0.1° coordinates |
| GET `/api/stations/{alias}/observations` | `public_readonly_station_detail` (caddy 296-304), `routes/station-detail-routes.ts:369` | ON; no query or exactly `limit=1`; alias only |
| GET `/api/stations/{alias}/quality` | same matcher, `routes/station-detail-routes.ts:470` | ON; same query rule |
| GET `/api/stations/{alias}/submissions` | same matcher, `routes/station-detail-routes.ts:511` | ON; same query rule |
| GET `/api/stations/{alias}/earnings` | `public_readonly_station_earnings` (caddy 312-320), `routes/station-detail-routes.ts:664` | ON; no query at all |
| GET `/api/stations/{alias}/ownership` | `public_readonly_station_ownership` (caddy 350-358), `routes/station-owner-routes.ts:432` | ON; no query; alias only; ownership state, no coordinates |
| POST `/api/stations/{alias}/owner-actions` | `station_owner_actions` (caddy 138-148; own rate zone 518-526), `routes/station-owner-routes.ts:349` | Relays one wallet-signed owner transaction; no query; 8 KiB body cap; the node ignores owner transactions until the features are scheduled (see **Station owner actions**) |
| GET `/api/weather/leaderboard` | `public_readonly_weather_leaderboard` (caddy 333-341), `routes/weather-leaderboard-routes.ts:247` | ON; exactly `metric=…&period=…&limit=1..30` in that order, else 404 |
| GET `/api/blockchain/status` | `chain_status`, `routes/blockchain-routes.js:58` | Node-backed while responding |
| GET `/api/blockchain/blocks` | `chain_blocks`, `routes/blockchain-routes.js:123` | Recent bounded list; node outage unavailable |
| GET `/api/blockchain/transactions` | `chain_transactions`, `routes/blockchain-routes.js:270` | HTTP 501 by design |
| GET `/api/blockchain/transactions/{hash}` | `chain_transaction_detail`, `routes/blockchain-routes.js:278` | HTTP 501 by design; exact 64 hex with optional0x |
| GET `/api/blockchain/validators` | `chain_validators`, `routes/blockchain-routes.js:286` | HTTP 501 by design |
| GET `/api/blockchain/stats` | `chain_stats`, `routes/blockchain-routes.js:302` | HTTP 501 by design |
| GET `/api/build` | `public_build`, `routes/capabilities-routes.ts:399` | Build stamp |
| GET `/api/capabilities` | `public_capabilities`, `routes/capabilities-routes.ts:426` | Readiness inventory; not proof of payment |
| GET `/join/manifest.json`, `/join/snapshot.tar.gz` | `join_artifacts`, edge file_server at `/srv/join` | Owner publication; absent files 404 |
| GET `/status.json` | `public_status`, edge file_server at `/srv/status` | Absent file 404 |

**Leaderboard source (r20.2).** Served by `server/routes/weather-leaderboard-routes.ts` at backend dec7b920 (`metric=earnings` default, line 247; country/region/near filters rejected for earnings, 291-293); the frontend has leaderboard components at fc2e4268, but its public build mounts no leaderboard page (the phone Profile tab is the invitee view). The edge admits it through `@public_readonly_weather_leaderboard` (caddy 333-341), gated on `PUBLIC_READONLY_API=on` like the station reads. The reference-shadow sidecar is advisory and changes no invitee step (infra#1281, merged).

Identifiers use the edge’s declared character/length restrictions. No other API operation is implied by sharing a route family. The repository stays private through this testnet, and the owner decides when and how invitees receive the guide.
