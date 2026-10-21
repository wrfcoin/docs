# WRFCoin closed-testnet invitee quickstart

This guide is ready for owner review; distribution is PENDING the owner’s D7 decision. Join only after the team announces your invitation and confirms the release. Use only the team-provided invitation, APK and website links. These are test tokens. The team will never ask for your recovery words or station API keys. The phone path below needs an Android phone with a barometer. The team confirms which release is ready before you start.

1. **Join and install.** Accept the Tailscale invitation with your invited account and keep Tailscale connected. Invitees belong to `wrfcoin-invitees`; app access is TCP port 9444 only. Install the APK from the trusted link and compare its supplied checksum. For an update, keep your existing app and data. If Android refuses the update, ask for a compatible APK; do not uninstall a wallet until its recovery backup and address are recorded.
2. **Back up one wallet.** Open **Earnings → Create Wallet → Generate Wallet**. Write down the **12 recovery words**, in order, offline and privately. Tap **I've written it down**, complete the requested word checks, then **Complete Setup**. For an existing wallet, choose **Import / Restore Wallet** and compare its restored address with your saved address. Keep the same wallet for your phone station and any later browser access. Use **Sign in** if prompted and approve locally with your fingerprint or PIN. Never send the words to support or paste them into a browser's storage, chat or email.
3. **Give collection consent.** Open **Collect → Privacy center** using the shield in the top bar. Enable sensor and approximate-location consent and the requested Android location permission. Turn **Collection Paused** on so it reads **Collecting Data**, then tap **Collect Now** once and approve the wallet request. Registration alone does not activate your station or earn a reward.
4. **Wait for activation.** If your station is awaiting activation, pause collection and wait for the team's activation announcement. Return with the same wallet signed in; let resume sync finish, then use **Refresh station status**. Unavailable or cached status does not confirm activation. After activation is confirmed, resume collection and collect a fresh reading. Saved readings expire; reconnect and sync promptly. A notice that earlier saved readings were removed means they were ineligible and cannot earn payment; collect again after that operation finishes.
5. **Check the first reading.** **Sync Progress & Rewards** reports readings synced to the backend. Upload, acceptance, attestation and payment are separate stages. A pending reading has not yet earned. Check **Earnings**: **Weather pending** and **Weather paid** distinguish the reported stages, and **Total earned** reports reward totals in WRF. Wait for accepted, rewarded reading evidence and chain confirmation; collection is not a payment guarantee. A faucet grant can change your balance without being weather earnings.
6. **Claim test tokens only when invited to.** The faucet opens separately after r19, block 33000 and the team's activation/funding checks. Use **Earnings → Get Testnet Tokens**. Check **Tokens will be sent to** is your saved address, tap **Request Testnet Tokens**, answer the challenge, then **Claim Tokens** once. Keep the returned transaction hash and follow pending or cooldown instructions. Address claims have a 24-hour cooldown; additional shared-network/device caps apply. Use the displayed service amount; do not expect a particular grant or submit repeated claims. You can register and await activation before the faucet opens.

## Browser joining when the team announces it

The website is a separate link from the phone API. The app's 9444-only access does not open a dashboard port. Begin browser joining when the team announces that release, at the exact `/onboarding` page, and use the same wallet as your phone.

Choose **Create New Wallet** or **Import Recovery Phrase**. Set and confirm a **Browser password** of at least 8 characters, then choose **Generate Recovery Words** or **Review Backup**. Write down your 12 words privately and complete backup verification before connecting. Your words are kept only encrypted in this browser, unlocked by your password. The browser copy is not your backup: a forgotten password or cleared browser data cannot recover it; keep your written words to restore the wallet. When a vault already exists, use **Unlock Wallet** with your browser password. Never paste the words anywhere else or send them to support.

The exact `/wallet` page shows **Your WRFCoin address** and your own phone-station status; it does not promise a browser reward balance. For an Ambient Weather station, `/connect-station` and `/earn` open the same station flow. Use the same signed-in wallet, enter **Ambient API Key** and **Ambient Application Key** only in the approved form, select your account's device and choose a public station name without personal details. Do not send keys to support. Follow **Confirm & register**, keep the station ID, and wait for the displayed observation/attestation/reward progress. An Android phone still collects its readings in the APK; connecting Ambient does not register a phone station.

## When something is unavailable

**Not available**, unavailable, loading, pending or a blank reported value means the app lacks confirmed evidence for that item. It does not mean zero rewards or a successful operation. Keep Tailscale connected, check sign-in and try the displayed refresh action later. Do not generate another wallet or repeat a pending claim to work around it. Unsupported previews such as DAG data can remain unavailable while the supported reading path works.

Send the team the exact message, app version and station ID or public wallet address if relevant. Leave out recovery words, API keys, location details and screenshots that contain them. Send remains hidden in the invitee release.

## Availability checklist

Before joining, ask the team to confirm each applicable item. Unchecked items are pending, not release evidence.

- [ ] **Invitation and distribution — PENDING:** owner D7 approval, invited account and approved links supplied.
- [ ] **Phone release — PENDING:** approved APK version, checksum and compatible-update receipt supplied. This guide does not identify a shipped build.
- [ ] **Website release — PENDING:** served frontend/backend revisions and exact-page checks supplied by the owner after r19 deployment; merged source alone does not satisfy this item.
- [ ] **Activation — PENDING:** team’s chain activation receipt, station’s own activation status and supported fresh-reading path confirmed. Registration and backend sync do not confirm payment.
- [ ] **Faucet — PENDING:** block 33000/E0f binding, r19, funding and the team’s opening announcement confirmed; use the displayed amount, never an assumed grant.
- [ ] **First reward — PENDING:** accepted observation, attestation, reward and chain-confirmation evidence supplied for your own station. Pending is not paid.

The station map/list and public observation, quality and submission details are **off by default** at the website edge. Their absence is expected until the owner separately enables and verifies them. Chain status and recent block lists can answer from a responding node; an outage is unavailable. Transaction lists, lookup by hash, validator lists and legacy chain stats answer **HTTP 501 by design** on the website API. A recorded transaction hash is useful for support, but this website does not promise a working lookup. Coverage-zone responses may be fallback data; do not treat them as measured coverage. Node snapshot downloads and the status document depend on owner publication; missing artifacts can return 404. None of these surfaces confirms a reward or invites public signup. Send stays hidden.

## Owner source map (not a served-release receipt)

This appendix gives the distribution reviewer a source map for every route named here. Invitees use the supplied links and app controls; they need not call APIs. Source-admitted means the configured edge can forward a request, not that the runtime service is available. Method, path, authentication and query restrictions all still apply.

Historical revisions below are plain-text provenance; pre-snapshot commits are
not available in the public repository and do not establish current behavior.

Pinned source: `infra9005a8f6`, `backend898039ee`, `frontend912dc733`. The canonical edge is `testnet/edge/public_onboarding.caddy`; its generated API table is `testnet/PUBLIC_ENDPOINTS.md`. UI pages use the frontend fallback in Caddyfile.funnel/Caddyfile, not an API matcher. Exact `/wallet` is admitted by that fallback and PUBLIC_ONBOARDING_PATHS; the absence of its name from the API table does not establish a denial. Deep variants of the other three joining pages remain blocked.

Backend handler paths below are under `server/`; line anchors refer to the pinned backend. Mounts in `enhanced_unified_api_optimized.ts`: weather1519, onboarding1565, blockchain1512, capabilities1609, station detail276; wallet auth is handled in the entrypoint. These are handler-presence classifications, separate from edge admission and owner runtime receipts.

| Method and route | Edge / canonical handler | Availability |
| --- | --- | --- |
| GET `/onboarding` | Exact page bypasses deep-path guards; frontend `src/routes/walletRoutes.jsx:18` → OnboardingPage | Source-admitted; owner served-build receipt PENDING |
| GET `/wallet` | Frontend fallback; `src/config/contractSurfacePolicy.ts:83`, `walletRoutes.jsx:17` → OwnWalletAddress | Own address/status only; served receipt PENDING |
| GET `/connect-station` | Exact page bypasses deep-path guards; `src/routes/earnRoutes.jsx` → ConnectStationPage | Ambient joining; served receipt PENDING |
| GET `/earn` | Exact page bypasses deep-path guards; `src/routes/earnRoutes.jsx` → ConnectStationPage | Same station flow; served receipt PENDING |
| GET `/api/auth/nonce/{addr}` | `wallet_nonce`, entrypoint887 | Exact 0x +40 hex address; nonce challenge, no payment |
| POST `/api/auth/wallet-login` | `wallet_login`, entrypoint897 | Signed challenge; session required for owner actions |
| POST `/api/auth/refresh` | `wallet_refresh`, entrypoint904 | Refresh authentication required |
| POST `/api/onboarding/faucet/challenge` | `faucet_challenge`, `routes/onboarding-routes.ts:474` | Challenge only, no grant |
| POST `/api/onboarding/faucet/claim` | `faucet_claim`, `routes/onboarding-routes.ts:529` | Owner opening/funding/E0f prerequisites PENDING |
| POST `/api/weather/stations/verify-key` | `station_verify`, `routes/weather-routes.js:435` | Wallet authentication required; approved form only |
| POST `/api/weather/stations` | `station_register`, `routes/weather-routes.js:291` | Wallet authentication; registration is not activation |
| GET `/api/weather/stations/{id}/reward-progress` | `station_reward_progress`, `routes/weather-routes.js:467` | Authenticated owner-scoped chain-evidence projection; pending is not paid |
| GET `/api/weather/stations/mobile` | `station_mobile_status`, `routes/weather-routes.js:427` | Wallet JWT, own row only, no query; status is not payment |
| GET `/api/weather/coverage-zones` | `weather_coverage_zones`, `routes/weather-routes.js:546` | Can return fallback after DB failure587; not measured assurance |
| GET `/api/weather/stations` | `public_readonly_stations`, `routes/weather-routes.js:635` | Default404; requires exact PUBLIC_READONLY_API=on and no query |
| GET `/api/stations/{id}/observations` | `public_readonly_station_detail`, `routes/station-detail-routes.ts:351` | Default404; same switch; no query or exactly limit=1 |
| GET `/api/stations/{id}/quality` | `public_readonly_station_detail`, `routes/station-detail-routes.ts:452` | Default404; same switch/query restriction |
| GET `/api/stations/{id}/submissions` | `public_readonly_station_detail`, `routes/station-detail-routes.ts:493` | Default404; same switch/query restriction |
| GET `/api/blockchain/status` | `chain_status`, `routes/blockchain-routes.js:58` | Actual node-backed status while responding; nullable fields stay unknown |
| GET `/api/blockchain/blocks` | `chain_blocks`, `routes/blockchain-routes.js:123` | Recent bounded block list; node outage unavailable |
| GET `/api/blockchain/transactions` | `chain_transactions`, `routes/blockchain-routes.js:270` | HTTP501 by design |
| GET `/api/blockchain/transactions/{hash}` | `chain_transaction_detail`, `routes/blockchain-routes.js:278` | HTTP501 by design; exact64 hex with optional0x |
| GET `/api/blockchain/validators` | `chain_validators`, `routes/blockchain-routes.js:286` | HTTP501 by design |
| GET `/api/blockchain/stats` | `chain_stats`, `routes/blockchain-routes.js:302` | HTTP501 by design |
| GET `/api/build` | `public_build`, `routes/capabilities-routes.ts:399` | Build stamp; owner comparison PENDING |
| GET `/api/capabilities` | `public_capabilities`, `routes/capabilities-routes.ts:426` | Readiness inventory; not proof of an operation/payment |
| GET `/join/manifest.json` | `join_artifacts`, edge file_server at `/srv/join`; publish-join-snapshot.sh | Owner publication PENDING; absent files404 |
| GET `/join/snapshot.tar.gz` | Same static publication/mount | Owner publication PENDING; does not direct invitees to run a node |
| GET `/status.json` | `public_status`, edge file_server at `/srv/status`; probe_public_uptime.sh | Owner probe output PENDING; absent file404 |

Identifiers use the edge’s declared character/length restrictions. No other API operation is implied by sharing a route family. No owner receipts, APK, deployed hashes or live observations have been supplied in this guide; the checklist remains visibly pending until the owner fills it. The repository stays private through this testnet, and the owner decides when and how invitees receive the guide.
