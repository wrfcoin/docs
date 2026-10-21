# 1. Vision

## The problem

Weather forecasting today is a remarkable technical achievement built on a few brittle assumptions.

First, that the data flows in from a small number of sources — official meteorological agencies, satellites, weather balloons, a handful of aggregator networks. Personal weather stations exist (CWOP, for instance) but they're loosely federated, inconsistently used, and rarely contribute to the forecasts most people rely on.

Second, that the compute happens in a few supercomputers running models like WRF and ECMWF's IFS. These are extraordinary pieces of infrastructure, but they live behind institutional walls. The cost to run them is real, the access is gated, and the models themselves are not always transparent.

Third, that the public should *trust* the result. For decades, this trust has been earned. But the institutions producing forecasts are increasingly under budget pressure, talent flight, and the pressure of needing to issue *something* in the face of growing climate uncertainty. The trust is not unconditional and it isn't permanent.

The fragmentation, the opacity, and the centralization are not malicious — they're inherited from a pre-internet, pre-blockchain era of how science gets done. But they're showing strain.

## The opportunity

Three things have changed.

**1. Sensors got cheap.** A reasonable personal weather station costs less than a nice dinner. IoT sensors for soil moisture, air quality, water levels, and a hundred other environmental variables are commodity hardware. The data exists; what's missing is a coordination layer to aggregate it.

**2. Compute got distributed.** Projects like BOINC proved years ago that volunteer-contributed computation can solve large-scale problems — climate modeling, protein folding, astrophysics. More recently, decentralized compute networks (Render, Akash, Bittensor) have shown that the volunteer model can be commercialized through token incentives.

**3. Cryptographic coordination matured.** Blockchains aren't only good for moving money. They're good for *coordination without a central party* — for letting strangers contribute to a shared resource and be fairly compensated for the value they add. That capability didn't exist when WRF was designed.

The opportunity is not to *replace* official weather services. It's to *augment* them with a decentralized, hyperlocal, community-governed layer of data and compute that fills the gaps the institutions can't.

## The aspiration

Wrfcoin's long-term aspiration is to become the **infrastructure layer for environmental data and climate information** — a global, decentralized data commons where:

- Anyone can contribute environmental data (from a personal weather station, a soil sensor, a verified observation)
- Anyone can contribute computational resources (running model forecasts, validating others' work)
- Anyone can build climate or environmental applications on top (carbon credits, agricultural forecasting, disaster response, ESG instruments)
- The data and the analysis are *trustworthy* because the protocol makes it costly to be wrong and rewarding to be right
- Participants are fairly compensated for the value they contribute

This is a public good in the economic sense — non-rivalrous, hard to exclude. The mechanism that builds it is decentralized incentives.

## What Wrfcoin is *not*

It's not a speculation vehicle. The token (WRF) exists to align incentives for data quality, not to enable trading.

It's not anti-NOAA, anti-ECMWF, or anti-NWS. The institutional forecasting infrastructure remains essential. Wrfcoin is additive — it provides the coordination layer for the *long tail* of environmental data that institutions can't economically collect.

It's not a single-app blockchain. The protocol is general; the first application is weather forecasting; the eventual ecosystem includes agriculture, real-world asset risk assessment, climate-finance instruments, and any domain where verified environmental data is load-bearing.

## What this means for the architecture

A blockchain whose validators are rewarded for *publishing verifiable environmental data* needs three things:

1. A consensus mechanism that pays for accuracy and information production, not just computation or capital. *(See [Consensus](./04-consensus.md).)*
2. A multi-tiered architecture that handles financial settlement separately from high-frequency sensor data. *(See [Architecture](./03-architecture.md).)*
3. A token standard that lets third parties build environmental and climate applications without re-inventing the wheel. *(See [Tokenomics](./05-tokenomics.md).)*

The next chapters describe each of these.
