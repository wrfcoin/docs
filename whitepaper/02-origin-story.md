# 2. Origin story

Wrfcoin emerged from a convergence of three observations made over a long weekend in December 2022. The shape of the project has changed substantially since then — twice. Here's the path.

---

## Phase 1: Computing Weather Forecasts (Dec 2022)

The starting point was a curiosity question, not a product idea: *what would it take to run a Weather Research and Forecasting (WRF) model on volunteer-contributed computational power?*

This produced three observations.

**The weather modeling challenge.** Modern forecasts run on petaflop-class supercomputers — institutional infrastructure with limited public access. The compute cost is real and the access is gated.

**The distributed computing precedent.** BOINC has demonstrated for two decades that volunteer compute can solve large-scale problems (Folding@home, Einstein@Home, climate modeling on climateprediction.net). Gridcoin had already shown that BOINC volunteers could be rewarded with cryptocurrency.

**The data fragmentation problem.** Weather data exists in silos — official agencies, personal weather stations (CWOP, Davis nets, Ambient Weather), IoT sensor deployments — but these sources don't contribute to a single decentralized network.

The early framework: IoT devices feed environmental data; volunteers donate compute; weather models run on a distributed network; participants earn tokens. Working name candidates included StormCoin, ClimateCoin, EcoCoin, EarthCoin, and **Skyward** — which became the working name for the next phase.

## Phase 2: Skyward (Jan 2023)

Skyward was the first attempt to design Wrfcoin as a *product*. It had a desktop client, a mobile app, a web dashboard, and an IoT device registration flow. It assumed Ethereum as the smart-contract layer with its own token (WRF) issued as ERC-20.

The architecture explored:

- Distributed storage (Filecoin, IPFS, Storj)
- Decentralized compute (Golem, then-emerging)
- Hybrid cloud fallbacks (Azure/AWS for when the volunteer network was insufficient)
- DEX integrations (Uniswap, SushiSwap, PancakeSwap)
- Advanced cryptographic features (atomic swaps, zk-STARKs for privacy)
- AI-enhanced forecasting (combining traditional WRF runs with ML predictions trained on IoT data for hyperlocal accuracy)

Skyward also introduced the **investors-as-equity-holders, contributors-as-token-earners** distinction that survives in the current design. The reasoning: positioning the token purely as a reward for verifiable work (rather than as a security sold to investors) keeps the token's center of gravity in *utility* rather than *speculation* — and avoids regulatory ambiguity around token sales.

Skyward's biggest weakness, in hindsight, was that it tried to be a generic blockchain platform with a weather product on top. The token economics, the consensus mechanism, and the data model were all generic-blockchain-shaped — they happened to be applied to weather, but they could have been applied to anything.

## Phase 3: Wrfcoin Reboot (Feb 2025)

Two years of intermittent work clarified what Skyward had gotten wrong: by sitting on top of Ethereum and using ERC-20, Wrfcoin had no real lever to optimize for its actual problem domain (high-volume environmental sensor data + accuracy-rewarding consensus). The reboot took the project back to first principles.

The key shifts:

**Wrfcoin became its own L1.** Not a token on someone else's chain — a chain optimized for environmental data publishing. This unlocked the design freedom to define the consensus mechanism (Proof of Publication, see [Consensus](./04-consensus.md)) and to introduce a domain-specific token standard (WRC-20, see [Tokenomics](./05-tokenomics.md)) without ERC-20's constraints.

**A three-layer architecture.** Rather than trying to handle financial transactions, DeFi, and high-frequency sensor data on one chain, the reboot split them. L1 for settlement and governance; L2 rollups for DeFi throughput; DAG-based sidechains for real-time environmental data streaming. *(See [Architecture](./03-architecture.md).)*

**Climate finance as a first-class concern.** The reboot widened Wrfcoin's vision from "decentralized weather forecasting" to "infrastructure layer for environmental data and climate finance." This is what makes WRC-20 (the standard) more important than just the WRF token (the asset) — third parties can build their own carbon-credit, ESG, regenerative-agriculture, and RWA-environmental tokens on Wrfcoin.

**The Meta-OS concept.** Beyond being a blockchain, Wrfcoin is positioned as a coordination layer that can route specialized tasks to other DePIN networks (compute → Render or Akash, storage → Filecoin or Arweave, oracle data → Chainlink) and reward results in WRF. This is the "intelligence layer" framing — Wrfcoin doesn't try to be the best at everything; it tries to be the best at *orchestrating* environmental analysis across the broader DePIN ecosystem.

## Timeline

| Date | Phase | Working name | Key shift |
|------|-------|--------------|-----------|
| Dec 2022 | Phase 1 | "Computing Weather Forecasts" | Initial exploration: WRF + BOINC + Bitcoin |
| Jan 2023 | Phase 2 | Skyward | Product design: desktop client, mobile, IoT, ERC-20 on Ethereum |
| Feb 2025 | Phase 3 | Wrfcoin Reboot | Own L1; PoPub consensus; WRC-20 standard; DAG sidechains for data |
| Mid-2026 *(target)* | Testnet | Wrfcoin | First public network |

## What this history tells you

The shape of Wrfcoin took two years and a complete redesign to settle into something coherent. The current architecture is what survived contact with the question *what is this actually trying to be?* — and the answer was less "a weather app on Ethereum" and more "an environmental information layer with its own consensus, token standard, and coordination role."

The remaining chapters describe what that architecture actually looks like.
