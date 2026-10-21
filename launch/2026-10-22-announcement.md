# DRAFT: WRFCoin public testnet launch announcement

> **DRAFT for the owner's edit.** Written in the owner's voice from facts in the public repositories and the live website on 2026-10-19. Square brackets mark places for the owner to fill in or cut. Nothing here should be posted until the owner has read it through. Suggested channels: the GitHub organization profile, a pinned discussion or issue in wrfcoin/testnet-support, and the website.

---

## WRFCoin's public testnet is open

Today, Thursday 22 October 2026, the WRFCoin testnet is public, and so is the code behind it.

WRFCoin is a blockchain for weather data. The idea is simple to say and hard to build: anyone with a weather station, or a phone with a barometer, should be able to contribute observations, have them verified, and be rewarded for the ones that hold up. Forecasts get published against that data, and the people and machines that do useful, checkable work are the ones the chain rewards. I started this in 2018 because the data behind our forecasts comes from too few places, the compute lives behind institutional walls, and the long tail of local observations mostly goes nowhere. WRFCoin is meant to add to the official weather services, not replace them.

Until now the network has run as a closed testnet with a small group of invited participants. From today it is open to anyone.

## What it is, honestly

This is a **test network**. The coins on it are test coins. They have no monetary value, they are not for sale, and nothing here is an investment. The chain may be reset without notice. No mainnet exists and no migration to one is promised. The network is deliberately attacked on a schedule as part of testing, so please attach nothing to it that you cannot afford to lose.

Some things work end to end today. Others are partly built or still only designed, and the documentation says which is which. The [implementation status](https://github.com/wrfcoin/docs/blob/main/STATUS.md) page is the honest list; please read it before you rely on anything.

## What you can do today

- **Watch the chain** at [wrfcoin.com](https://wrfcoin.com): live block height, a weather map, a block explorer, search, the contributor leaderboard, read-only governance, and a forecast page.
- **Open a wallet** on the website, claim some testnet WRF from the faucet, and send it to a friend. [OWNER: say "or in the Android app" only if the APK and its SHA-256 are published before posting.]
- **Connect a weather station.** An Ambient Weather station links from the website; once the Android app is out, a phone with a barometer becomes a station too. Observations the chain can verify earn testnet WRF.
- **Run a node** that follows the chain, if you like running things. Peering is arranged per operator for now: ask in testnet-support and we will set you up.
- **Read the code.** [Thirteen repositories](https://github.com/wrfcoin) are public today, from the Rust node to the website and the app.

The [quickstart](https://github.com/wrfcoin/docs/blob/main/testnet/quickstart.md) walks through each of these.

## How to join

1. Go to [wrfcoin.com](https://wrfcoin.com) and choose **Get started**. Android app: coming soon on the [mobile releases page](https://github.com/wrfcoin/mobile/releases). [OWNER: confirm the APK + SHA-256 are published before posting, or keep "coming soon".]
2. Create a wallet and write down your 12 recovery words. Nobody can recover them for you, and nobody from the project will ever ask for them.
3. Claim test tokens from the faucet, and connect a station if you have one.
4. When something breaks, and things will break, tell us in [testnet-support](https://github.com/wrfcoin/testnet-support/issues/new/choose). Security problems go to **security@wrfcoin.com**, not to a public issue.

## Thanks

[Owner to edit.] To the invitees who ran the closed testnet: you found the bugs that mattered, you kept your stations reporting through resets, and you were patient with a network that was being attacked on purpose. Thank you. To everyone who contributed code, reviews, hardware and time over the past eight years: this is your launch too.

[Optional, owner's call: a personal line about the date.]

See you on the map.

[Owner's name]

---

*Testnet WRF has no monetary value. The network may be reset. See the [terms, privacy notice and security policy](https://wrfcoin.com) linked from the website.*
