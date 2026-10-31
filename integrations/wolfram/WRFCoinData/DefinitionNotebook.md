# WRFCoinData: Definition Notebook content

Paste each section below into the matching section of a new Function Repository definition notebook
(see [the README](../README.md) for the steps). Code cells are Wolfram Language input cells.
Text in *italics* inside the usage lines are template arguments: use the notebook's "Template Input"
button for them.

---

## Title

WRFCoinData

## Description

Get weather observations and network status from the public WRFCoin testnet

(Imperative verb first, no final period, as the Function Repository style guide asks.)

## Definition

Paste the whole of [`WRFCoinData.wl`](WRFCoinData.wl) from `ClearAll[WRFCoinData];` to the end
(everything under the `Definition` heading). It uses only built-in symbols; the helper functions
(`wrfGet`, `wrfDate`, ...) are private to the definition and are not user-facing.

## Usage

- `WRFCoinData[]` gives a `Dataset` of the public weather stations on the WRFCoin testnet.
- `WRFCoinData["`*station*`"]` gives a `Dataset` of the station's most recent on-chain observations.
- `WRFCoinData["`*station*`", "`*property*`"]` gives *property* for the station: a `TimeSeries` of quantities for a measured variable, `"Observations"` or `"Location"`.
- `WRFCoinData[{`*station1*`, `*station2*`, ...}, "`*property*`"]` gives an `Association` of *property* for several stations.
- `WRFCoinData["`*prop*`"]` gives the network-wide property *prop*, such as `"NetworkStatus"` or `"CoverageZones"`.
- `WRFCoinData["Balance", "`*address*`"]` gives the spendable and lifetime-earned balance of a testnet address, in WRF.

## Details & Options

- WRFCoin is a weather-data blockchain. Station owners commit each reading on chain and reveal it a few blocks later; independent attesters confirm it. The public testnet (chain 888) produces a block about every 77 seconds.
- WRFCoinData reads only the public, unauthenticated read API of https://wrfcoin.com. No account, key or sign-in is needed.
- A *station* is its public alias: `"st_"` followed by 12 lowercase hexadecimal digits. Station locations are published at 0.1 degree (about 11 km), never the exact position.
- Station properties:

| | |
|---|---|
| `"Observations"` | `Dataset` of recent readings (oldest first) with time, block height, every measured variable, provenance and attester quorum |
| `"Location"` | `GeoPosition` of the station at 0.1 degree |
| `"Temperature"` | air temperature (`"DegreesCelsius"`) |
| `"Humidity"` | relative humidity (`"Percent"`) |
| `"Pressure"` | station pressure (`"Hectopascals"`) |
| `"WindSpeed"` | wind speed (`"Meters"/"Seconds"`) |
| `"WindDirection"` | wind direction (`"AngularDegrees"`) |
| `"Precipitation"` | precipitation (`"Millimeters"`) |
| `"RainRate"` | rain rate (`"Millimeters"/"Hours"`) |
| `"DewPoint"` | dew point (`"DegreesCelsius"`) |
| `"UVIndex"` | UV index (pure number) |
| `"PM25"` | fine particulate matter (`"Micrograms"/"Meters"^3`) |

- Network properties:

| | |
|---|---|
| `"Stations"` | `Dataset` of stations: alias, name, location, status, last update, quality score |
| `"NetworkStatus"` | `Association`: producing status, tip height, tip age, blocks per minute, peers |
| `"ChainStatus"` | `Association`: chain ID, height, target block time, validators, transaction counts |
| `"CoverageZones"` | `Dataset` of sparse-coverage zones (center, radius, reward multiplier, station count) |
| `"RecentBlocks"` | `Dataset` of the most recent blocks (height, hash, time, transaction count), newest first |

- `WRFCoinData["Properties"]` lists every property by kind.
- A variable a station does not measure is `Missing["NotAvailable"]`, never 0. A measured-variable property with no values at all gives `Missing["NotAvailable"]` instead of a `TimeSeries`.
- `"Balance"` gives exact numbers of WRF (1 WRF = 10^8 base units). The public balance read can be switched off on a server; then the result is a `Failure` with status code 404.
- The public API allows about 30 reads per minute per client address. A rate-limited read gives `Failure["WRFCoinRateLimited", ...]`; any other HTTP error gives `Failure["WRFCoinHTTPError", ...]` with its `"StatusCode"`.
- This is a test network: it may be reset, and its coins have no monetary value.
- The following options can be given:

| | | |
|---|---|---|
| `"BaseURL"` | `"https://wrfcoin.com"` | site whose public read API is used |
| `TimeConstraint` | `30` | seconds to wait for each answer |

## Examples

### Basic Examples

Get the public weather stations on the testnet:

```wl
WRFCoinData[]
```

Get the recent on-chain observations of one station:

```wl
WRFCoinData["st_057d50adbb07"]
```

Get the station's air temperature as a time series and plot it:

```wl
DateListPlot[WRFCoinData["st_057d50adbb07", "Temperature"]]
```

### Scope

Get the network status:

```wl
WRFCoinData["NetworkStatus"]
```

Show every station on a map:

```wl
GeoListPlot[Normal[WRFCoinData[][All, "Location"]], GeoLabels -> Automatic]
```

Get one variable for several stations at once:

```wl
WRFCoinData[Normal[WRFCoinData[][All, "Alias"]], "Pressure"]
```

Show the sparse-coverage zones, where new stations earn a bonus:

```wl
GeoGraphics[{Opacity[0.3], Red,
  GeoDisk[#Center, #Radius] & /@ Normal[WRFCoinData["CoverageZones"]]}]
```

Get a testnet address's spendable and lifetime-earned balance:

```wl
WRFCoinData["Balance", "0x7d29000000000000000000000000000000000cb2"]
```

List the available properties:

```wl
WRFCoinData["Properties"]
```

### Options

#### BaseURL

Read a local node's backend instead of the public site:

```wl
WRFCoinData["NetworkStatus", "BaseURL" -> "http://127.0.0.1:4001"]
```

#### TimeConstraint

Wait at most 5 seconds for an answer:

```wl
WRFCoinData["ChainStatus", TimeConstraint -> 5]
```

### Applications

Compare a station's temperature with the nearest station in Wolfram's own weather data:

```wl
loc = WRFCoinData["st_057d50adbb07", "Location"];
wrf = WRFCoinData["st_057d50adbb07", "Temperature"];
ref = WeatherData[loc, "Temperature", {wrf["FirstDate"], wrf["LastDate"]}];
DateListPlot[{wrf, ref}, PlotLegends -> {"WRFCoin station", "WeatherData (nearest)"}]
```

Summarise how far the station is from the reference over the window:

```wl
MeanAround[QuantityMagnitude[wrf["Values"]]] - Mean[QuantityMagnitude[ref["Values"]]]
```

How often the network produces a block:

```wl
blocks = Normal[WRFCoinData["RecentBlocks"]];
Mean[-Differences[#Time & /@ blocks]]
```

### Properties and Relations

Every observation row carries the block height it landed in and the commit id that proves it:

```wl
Normal[WRFCoinData["st_057d50adbb07"]][[-1, {"Height", "CommitID"}]]
```

### Possible Issues

Variables a station does not measure are missing, not zero:

```wl
WRFCoinData["st_057d50adbb07", "Humidity"]
```

The public API is rate limited; reading too often gives a Failure:

```wl
Table[WRFCoinData["NetworkStatus"], 40] // Count[_Failure]
```

A malformed station alias makes no request:

```wl
WRFCoinData["st_123"]
```

### Neat Examples

Map the newest readings, coloured by temperature:

```wl
st = Normal[WRFCoinData[]];
temps = AssociationMap[WRFCoinData[#, "Temperature"]["LastValue"] &, #Alias & /@ st];
GeoBubbleChart[(#Location -> QuantityMagnitude[temps[#Alias]]) & /@
  Select[st, QuantityQ[temps[#Alias]] &], ColorFunction -> "TemperatureMap"]
```

## Source & Additional Information

### Contributed By

Tony Koop (WRFCoin)

### Keywords

- weather
- weather stations
- blockchain
- citizen science
- observations
- meteorology
- testnet

### Categories

- External Interfaces & Connections
- Earth Sciences (or the closest category the notebook offers)

### Related Symbols

- WeatherData
- WeatherForecastData
- TimeSeries
- GeoPosition
- URLRead
- Dataset

### Related Resource Objects

(none)

### Source/Reference Citation

WRFCoin public testnet read API, https://wrfcoin.com (documentation: https://github.com/wrfcoin/docs).

### Links

- https://wrfcoin.com
- https://github.com/wrfcoin/docs
- https://github.com/wrfcoin/docs/tree/main/integrations/wolfram

### Tests

Paste the `VerificationTest[...]` expressions from [`Tests.wlt`](Tests.wlt), together with the
`wrfTestFixtures`, `wrfTestPath` and `withRecordedAPI` definitions above them. The offline tests
replace `URLRead` with recorded answers, so they pass without network access; the two live tests
run only when `WRFCOIN_LIVE_TESTS=1`.

### Compatibility

#### Wolfram Language Version

13.0 (uses `URLRead` with `TimeConstraint`, `ImportByteArray[..., "RawJSON"]`, `DateObject` with a time zone, `Dataset`, `TimeSeries`)

#### Operating System

All

#### Environments

Desktop, Cloud (needs outbound HTTPS to wrfcoin.com)

### Author Notes

WRFCoin is a weather-data network where each station reading is committed on chain, revealed a few
blocks later and confirmed by independent attesters. This function reads only the public read API,
which publishes station locations at 0.1 degree and never personal data. The network is a public
testnet: it may be reset, and its coins have no monetary value.

### Submission Notes

The function reads a public HTTPS API that needs no key. All its routes are documented in
https://github.com/wrfcoin/docs/tree/main/integrations/wolfram. The offline tests stub `URLRead`
with recorded answers so they do not depend on the network.
