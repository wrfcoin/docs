# WRFCoin in the Wolfram Language

This folder holds `WRFCoinData`, a function for the
[Wolfram Function Repository](https://resources.wolframcloud.com/FunctionRepository/) that reads
public WRFCoin testnet data into the Wolfram Language: the station list, each station's recent
on-chain observations as `TimeSeries` of quantities, network status, coverage zones, recent blocks
and the public balance of an address.

It uses only the public, unauthenticated read API of https://wrfcoin.com. It needs no account and no
key, and it reads no personal data: station locations are published at 0.1 degree (about 11 km).

| File | What it is |
| --- | --- |
| [`WRFCoinData/WRFCoinData.wl`](WRFCoinData/WRFCoinData.wl) | The definition (the notebook's Definition section) |
| [`WRFCoinData/DefinitionNotebook.md`](WRFCoinData/DefinitionNotebook.md) | Every other notebook section, ready to paste: description, usage, details and options, examples, metadata |
| [`WRFCoinData/Tests.wlt`](WRFCoinData/Tests.wlt) | `VerificationTest`s: offline (recorded answers, no network) and opt-in live tests |
| [`WRFCoinData/RunTests.wls`](WRFCoinData/RunTests.wls) | Loads the definition and runs the tests from a terminal |

## Status

**Not yet run on a Wolfram kernel.** The files were written without an activated Wolfram Engine.
They parse cleanly (checked with the Mathics3 parser), and the routes and JSON shapes they read were
checked against https://wrfcoin.com on 2026-10-31. Run the tests once on a real kernel before
submitting (step 2 below).

## Public routes it reads

All are `GET`, admitted by the public edge (`testnet/edge/public_onboarding.caddy` in
[wrfcoin/infra](https://github.com/wrfcoin/infra)) and limited to about 30 reads per minute per client.

| Property | Route |
| --- | --- |
| `"Stations"`, `"Location"` | `/api/weather/stations` |
| station observations and series | `/api/stations/<alias>/observations` |
| `"NetworkStatus"` | `/api/explorer/summary` |
| `"ChainStatus"` | `/api/blockchain/status` |
| `"CoverageZones"` | `/api/weather/coverage-zones` |
| `"RecentBlocks"` | `/api/blockchain/blocks` |
| `"Balance"` | `/api/public/balance/<address>` |

## How to submit (owner, under your own Wolfram ID)

Nothing here submits anything. The submission is made by the owner, signed in with his own Wolfram ID.

1. **Get a kernel.** Use Mathematica / Wolfram Desktop, or activate the free Wolfram Engine already
   installed on the workstation (`wolframscript -activate`, sign in with your Wolfram ID; the free
   Engine licence covers development use).
2. **Run the tests.** In this folder run `wolframscript -file WRFCoinData/RunTests.wls`. It prints
   `N passed, 0 failed` and exits 0 when all pass. To include the live tests against wrfcoin.com,
   run it with `WRFCOIN_LIVE_TESTS=1`. Fix anything that fails before going on.
3. **Make the definition notebook.** In Mathematica / Wolfram Desktop choose
   *File > New > Repository Item > Function Repository Item*. A template opens with one section
   per heading in [`DefinitionNotebook.md`](WRFCoinData/DefinitionNotebook.md).
4. **Fill it in.** Paste each section from `DefinitionNotebook.md`, and paste the definition from
   `WRFCoinData.wl` (from `ClearAll[WRFCoinData];` to the end) into the Definition section. In the
   Usage lines, mark the arguments with the toolbar's *Template Input* button. Evaluate each Examples
   cell so the notebook carries its output.
5. **Check and preview.** Use the toolbar's *Check* button (style checks) and *Preview* (in the
   notebook, or *Deploy > Locally/To the Cloud* to try `ResourceFunction[...]` before submitting).
6. **Submit.** Use *Submit to Repository*. Read and accept the contributor terms it shows. Wolfram
   reviewers may ask for changes by email; once accepted, the function is used as
   `ResourceFunction["WRFCoinData"]`.

Keep the submitted notebook (`WRFCoinData-definition.nb`) next to these files after submitting, so
later updates start from it.

## Naming

The Function Repository asks for names that are specific and say what the function does. Functions
that bring an outside data source into the language are commonly named `<Source>Data` after the
built-in `*Data` functions (`WeatherData`, `CountryData`). `WRFCoinData` follows that pattern, and the
property argument picks stations, series or network status. The alternative `WRFCoinStationData`
would fit if the network properties were dropped.
