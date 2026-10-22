## WRFCoin's public testnet is open

Today, Thursday 22 October 2026, the WRFCoin testnet is public, and so is the code behind it.

WRFCoin is a blockchain for weather data. The idea is simple to say and hard to build: anyone with a weather station, or a phone with a barometer, should be able to contribute observations, have them verified, and be rewarded for the ones that hold up. Forecasts get published against that data, and the people and machines that do useful, checkable work are the ones the chain rewards. I started this in 2018 because the data behind our forecasts comes from too few places, the compute lives behind institutional walls, and the long tail of local observations mostly goes nowhere. WRFCoin is meant to add to the official weather services, not replace them.

Until now the network has run as a closed testnet with a small group of invited participants. From today it is open to anyone.

## What it is, honestly

This is a **test network**. The coins on it are test coins. They have no monetary value, they are not for sale, and nothing here is an investment. The chain may be reset without notice. No mainnet exists and no migration to one is promised. The network is deliberately attacked on a schedule as part of testing, so please attach nothing to it that you cannot afford to lose.

Some things work end to end today. Others are partly built or still only designed, and the documentation says which is which. The [implementation status](https://github.com/wrfcoin/docs/blob/main/STATUS.md) page is the honest list; please read it before you rely on anything.

## What you can do today

- **Watch the chain** at [wrfcoin.com](https://wrfcoin.com): live block height, a weather map, a block explorer, search, the contributor leaderboard, read-only governance, and a forecast page.
- **Open a wallet** on the website, claim some testnet WRF from the faucet, and send it to a friend.
- **Connect a weather station.** An Ambient Weather station links from the website; once the Android app is out, a phone with a barometer becomes a station too. Observations the chain can verify earn testnet WRF.
- **Run a node** that follows the chain, if you like running things. Peering is arranged per operator for now: ask in testnet-support and we will set you up.
- **Read the code.** [Thirteen repositories](https://github.com/wrfcoin) are public today, from the Rust node to the website and the app.

The [quickstart](https://github.com/wrfcoin/docs/blob/main/testnet/quickstart.md) walks through each of these.

## Chain identity

The public testnet is **chain 888** on network `testnet`. Block 1 was minted today at 17:15:35 UTC and its genesis hash is

    553a3758386d9631037d7469686acb4a121ced81dcf5cde256e2d05667c5f332

Verify it against this line before you join a node or trust a wallet build. Earlier closed-testnet balances and activation heights did not carry over.

## How to join

1. Go to [wrfcoin.com](https://wrfcoin.com) and choose **Get started**. Android app: coming soon on the [mobile releases page](https://github.com/wrfcoin/mobile/releases).
2. Create a wallet and write down your 12 recovery words. Nobody can recover them for you, and nobody from the project will ever ask for them.
3. Claim test tokens from the faucet, and connect a station if you have one.
4. When something breaks, and things will break, tell us in [testnet-support](https://github.com/wrfcoin/testnet-support/issues/new/choose). Security problems go to **security@wrfcoin.com**, not to a public issue.

## Thanks

To my family for letting me put weather stations and for helping me along this journey. 


See you on the map.

Tony

---

*Testnet WRF has no monetary value. The network may be reset. See the [terms, privacy notice and security policy](https://wrfcoin.com) linked from the website.*
