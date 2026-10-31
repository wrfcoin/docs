(* Tests for WRFCoinData. Run with:  wolframscript -file RunTests.wls
   The "offline" group stubs URLRead with recorded public answers (shapes captured from
   https://wrfcoin.com on 2026-10-31), so it needs no network. The "live" group reads the
   public testnet and is skipped unless the environment variable WRFCOIN_LIVE_TESTS is "1". *)

(* ---- recorded public answers (trimmed) ---- *)
wrfTestFixtures = <|
  "/api/weather/stations" -> <|"stations" -> {
      <|"alias" -> "st_057d50adbb07", "name" -> "Duluth, MN weather station", "latitude" -> 46.8, "longitude" -> -92,
        "status" -> "live", "lastDataUpdate" -> "2026-10-31T22:15:00.000Z", "isActive" -> True, "qualityScore" -> 100|>,
      <|"alias" -> "st_da86a72ab29d", "name" -> "Weather station st_da86a72ab29d", "latitude" -> 37.4, "longitude" -> -121.9,
        "status" -> "stale", "lastDataUpdate" -> "2026-10-31T20:59:44.000Z", "isActive" -> True, "qualityScore" -> 100|>},
    "total" -> 2, "hasMore" -> False, "nextCursor" -> Null, "source" -> "wrfcoin-contributors"|>,
  "/api/stations/st_057d50adbb07/observations" -> <|"observations" -> {
      <|"timestamp" -> "2026-10-31T22:50:00.000Z", "observedAt" -> 1793487000, "height" -> 10345,
        "commitId" -> "1e7716597469d1a9a2835d995b8569808210c18d5324d7da8ab3d05c920c08ca", "temperatureC" -> 7.8,
        "humidityPct" -> Null, "pressureHpa" -> 997.3, "windSpeedMs" -> 1.6, "windDirectionDeg" -> Null,
        "rainRateMmHr" -> Null, "precipitationMm" -> 0, "dewpointC" -> Null, "uvIndex" -> Null, "pm25UgM3" -> Null,
        "provenanceClass" -> "real", "attestation" -> <|"approvals" -> 3, "has_quorum" -> True|>|>,
      <|"timestamp" -> "2026-10-31T22:45:00.000Z", "observedAt" -> 1793486700, "height" -> 10345,
        "commitId" -> "9048ea84e6ee904bcee44023b4fa624f1ad6e4eee9b3e9a869987e62234cb3bb", "temperatureC" -> 7.7,
        "humidityPct" -> Null, "pressureHpa" -> 997.3, "windSpeedMs" -> 1.1, "windDirectionDeg" -> Null,
        "rainRateMmHr" -> Null, "precipitationMm" -> 0, "dewpointC" -> Null, "uvIndex" -> Null, "pm25UgM3" -> Null,
        "provenanceClass" -> "real", "attestation" -> <|"approvals" -> 3, "has_quorum" -> True|>|>},
    "source" -> "core4", "order" -> "descending-height"|>,
  "/api/explorer/summary" -> <|"state" -> "ok", "status" -> "producing", "height" -> 10348, "tipAgeSeconds" -> 21,
    "blocksPerMinute" -> 0.78, "blocksSampled" -> 30, "peerCount" -> 3, "faucetFunded" -> True,
    "generatedAt" -> "2026-10-31T22:56:58.144Z"|>,
  "/api/weather/coverage-zones" -> <|"source" -> "chain", "zones" -> {
      <|"lat" -> 37, "lng" -> -121, "radius" -> 111, "type" -> "sparse", "rewardMultiplier" -> 1.5, "stationCount" -> 1|>,
      <|"lat" -> 47, "lng" -> -93, "radius" -> 111, "type" -> "sparse", "rewardMultiplier" -> 1.5, "stationCount" -> 2|>}|>,
  "/api/blockchain/blocks" -> <|"success" -> True, "blocks" -> {
      <|"height" -> 10313, "hash" -> "eb87f1b1", "timestamp" -> "2026-10-31T22:11:42+00:00", "transactions" -> 1|>,
      <|"height" -> 10314, "hash" -> "64bfec24", "timestamp" -> "2026-10-31T22:12:59+00:00", "transactions" -> 2|>}|>,
  "/api/public/balance/0x7d29000000000000000000000000000000000cb2" ->
    <|"address" -> "0x7d29000000000000000000000000000000000cb2", "balance" -> "1250000000", "height" -> 10343, "earned" -> "50000000"|>
|>;

wrfTestPath[req_] := StringReplace[req["URL"], StartOfString ~~ "https://wrfcoin.com" -> ""];

(* URLRead stand-in: 200 with the recorded body, 429 under "/rate-limited", 404 for anything else *)
SetAttributes[withRecordedAPI, HoldFirst];
withRecordedAPI[expr_] := Block[{URLRead},
  URLRead[req_, ___] := With[{p = wrfTestPath[req]},
    Which[
      StringStartsQ[p, "/rate-limited"], <|"StatusCode" -> 429, "BodyByteArray" -> StringToByteArray["{}"]|>,
      KeyExistsQ[wrfTestFixtures, p], <|"StatusCode" -> 200, "BodyByteArray" -> ExportByteArray[wrfTestFixtures[p], "RawJSON"]|>,
      True, <|"StatusCode" -> 404, "BodyByteArray" -> StringToByteArray["Not found"]|>
    ]
  ];
  expr
];

(* ================= offline ================= *)

VerificationTest[
  withRecordedAPI[Normal[WRFCoinData[][All, "Alias"]]],
  {"st_057d50adbb07", "st_da86a72ab29d"},
  TestID -> "stations-aliases"
]

VerificationTest[
  withRecordedAPI[Normal[WRFCoinData["Stations"]][[1, "Location"]]],
  GeoPosition[{46.8, -92}],
  TestID -> "stations-location-is-geoposition"
]

VerificationTest[
  withRecordedAPI[DateObjectQ[Normal[WRFCoinData["Stations"]][[1, "LastUpdate"]]]],
  True,
  TestID -> "stations-last-update-is-date"
]

VerificationTest[
  withRecordedAPI[Normal[WRFCoinData["st_057d50adbb07"][All, "Temperature"]]],
  {Quantity[7.7, "DegreesCelsius"], Quantity[7.8, "DegreesCelsius"]},
  TestID -> "observations-sorted-oldest-first-with-units"
]

VerificationTest[
  withRecordedAPI[Normal[WRFCoinData["st_057d50adbb07", "Observations"]][[1, "Humidity"]]],
  Missing["NotAvailable"],
  TestID -> "json-null-is-missing-not-zero"
]

VerificationTest[
  withRecordedAPI[Normal[WRFCoinData["st_057d50adbb07", "Observations"]][[2, "AttesterQuorum"]]],
  True,
  TestID -> "observations-attester-quorum"
]

VerificationTest[
  withRecordedAPI[
    With[{ts = WRFCoinData["st_057d50adbb07", "Pressure"]},
      {Head[ts], ts["PathLength"], ts["FirstValue"]}]],
  {TemporalData, 2, Quantity[997.3, "Hectopascals"]},
  TestID -> "pressure-time-series"
]

VerificationTest[
  withRecordedAPI[WRFCoinData["st_057d50adbb07", "Humidity"]],
  Missing["NotAvailable"],
  TestID -> "all-null-series-is-missing"
]

VerificationTest[
  withRecordedAPI[WRFCoinData["st_057d50adbb07", "Location"]],
  GeoPosition[{46.8, -92}],
  TestID -> "station-location"
]

VerificationTest[
  withRecordedAPI[WRFCoinData["st_aaaaaaaaaaaa", "Location"]],
  Missing["NotFound", "st_aaaaaaaaaaaa"],
  {WRFCoinData::nostation},
  TestID -> "unknown-station-location"
]

VerificationTest[
  withRecordedAPI[KeyTake[WRFCoinData["NetworkStatus"], {"Status", "Height", "TipAge", "Peers"}]],
  <|"Status" -> "producing", "Height" -> 10348, "TipAge" -> Quantity[21, "Seconds"], "Peers" -> 3|>,
  TestID -> "network-status"
]

VerificationTest[
  withRecordedAPI[Normal[WRFCoinData["CoverageZones"][All, {"Center", "Radius"}]][[2]]],
  <|"Center" -> GeoPosition[{47, -93}], "Radius" -> Quantity[111, "Kilometers"]|>,
  TestID -> "coverage-zones"
]

VerificationTest[
  withRecordedAPI[Normal[WRFCoinData["RecentBlocks"][All, "Height"]]],
  {10314, 10313},
  TestID -> "recent-blocks-newest-first"
]

VerificationTest[
  withRecordedAPI[WRFCoinData["Balance", "0x7D29000000000000000000000000000000000CB2"]],
  <|"Address" -> "0x7d29000000000000000000000000000000000cb2", "Balance" -> 25/2, "Earned" -> 1/2, "Height" -> 10343|>,
  TestID -> "balance-exact-wrf-from-base-units"
]

VerificationTest[
  withRecordedAPI[Keys[WRFCoinData[{"st_057d50adbb07", "st_da86a72ab29d"}, "Temperature"]]],
  {"st_057d50adbb07", "st_da86a72ab29d"},
  {WRFCoinData::http},
  TestID -> "listable-over-stations"
]

VerificationTest[
  withRecordedAPI[FailureQ[WRFCoinData["st_057d50adbb07", "Colour"]]],
  True,
  {WRFCoinData::badprop},
  TestID -> "unknown-station-property"
]

VerificationTest[
  FailureQ[WRFCoinData["st_NOT_AN_ALIAS"]],
  True,
  {WRFCoinData::badstation},
  TestID -> "malformed-alias-makes-no-request"
]

VerificationTest[
  FailureQ[WRFCoinData["Balance", "0x123"]],
  True,
  {WRFCoinData::badaddr},
  TestID -> "malformed-address-makes-no-request"
]

VerificationTest[
  withRecordedAPI[WRFCoinData["Stations", "BaseURL" -> "https://wrfcoin.com/rate-limited"]],
  Failure["WRFCoinRateLimited", _],
  {WRFCoinData::ratelimit},
  SameTest -> MatchQ,
  TestID -> "rate-limit-is-failure"
]

VerificationTest[
  withRecordedAPI[WRFCoinData["Balance", "0x0000000000000000000000000000000000000001"]],
  Failure["WRFCoinHTTPError", KeyValuePattern["StatusCode" -> 404]],
  {WRFCoinData::http},
  SameTest -> MatchQ,
  TestID -> "http-404-is-failure-never-zero"
]

VerificationTest[
  Keys[WRFCoinData["Properties"]],
  {"Network", "Station", "Account"},
  TestID -> "properties"
]

(* ================= live (opt-in) ================= *)

If[Environment["WRFCOIN_LIVE_TESTS"] === "1",
  VerificationTest[
    MatchQ[WRFCoinData["NetworkStatus"], KeyValuePattern[{"Height" -> _Integer?Positive}]],
    True,
    TestID -> "live-network-status"
  ];
  VerificationTest[
    With[{s = WRFCoinData[]}, Head[s] === Dataset && Length[s] > 0],
    True,
    TestID -> "live-stations"
  ]
]
