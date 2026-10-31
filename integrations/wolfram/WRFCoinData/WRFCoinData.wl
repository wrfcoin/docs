(* ::Package:: *)

(* ::Title:: *)
(*WRFCoinData*)

(* ::Text:: *)
(*Get public weather-station observations and network status from the WRFCoin public testnet.*)
(*Source of the Definition section of the Wolfram Function Repository submission (see README.md).*)
(*Reads only the public, unauthenticated read API of https://wrfcoin.com. No key, no account.*)

(* ::Section:: *)
(*Definition*)

ClearAll[WRFCoinData];

Options[WRFCoinData] = {"BaseURL" -> "https://wrfcoin.com", TimeConstraint -> 30};

WRFCoinData::badprop = "`1` is not a known WRFCoinData property. Known properties: `2`.";
WRFCoinData::badstation = "`1` is not a WRFCoin station alias (\"st_\" followed by 12 lowercase hexadecimal digits).";
WRFCoinData::badaddr = "`1` is not a WRFCoin address (\"0x\" followed by 40 hexadecimal digits).";
WRFCoinData::http = "The WRFCoin API answered HTTP `1` for `2`.";
WRFCoinData::ratelimit = "The WRFCoin public API is rate limited (about 30 reads per minute per client). Try again in a minute.";
WRFCoinData::nostation = "No public station with alias `1` was found.";

(* ---- Property lists ---- *)

wrfNetworkProperties = {"Stations", "NetworkStatus", "ChainStatus", "CoverageZones", "RecentBlocks"};

(* Station series: property -> {JSON key, unit} *)
wrfSeriesSpec = <|
  "Temperature" -> {"temperatureC", "DegreesCelsius"},
  "Humidity" -> {"humidityPct", "Percent"},
  "Pressure" -> {"pressureHpa", "Hectopascals"},
  "WindSpeed" -> {"windSpeedMs", "Meters"/"Seconds"},
  "WindDirection" -> {"windDirectionDeg", "AngularDegrees"},
  "Precipitation" -> {"precipitationMm", "Millimeters"},
  "RainRate" -> {"rainRateMmHr", "Millimeters"/"Hours"},
  "DewPoint" -> {"dewpointC", "DegreesCelsius"},
  "UVIndex" -> {"uvIndex", None},
  "PM25" -> {"pm25UgM3", "Micrograms"/"Meters"^3}
|>;

wrfStationProperties = Join[{"Observations", "Location"}, Keys[wrfSeriesSpec]];

wrfAliasQ[s_String] := StringMatchQ[s, RegularExpression["st_[0-9a-f]{12}"]];
wrfAliasQ[_] := False;

wrfAddressQ[s_String] := StringMatchQ[s, RegularExpression["0x[0-9a-fA-F]{40}"]];
wrfAddressQ[_] := False;

(* ---- HTTP: GET one public read route, parse JSON, or return a Failure ---- *)

wrfGet[path_String, opts : OptionsPattern[WRFCoinData]] :=
  Module[{base, url, resp, code, data},
    base = StringReplace[OptionValue[WRFCoinData, {opts}, "BaseURL"], "/" ~~ EndOfString -> ""];
    url = base <> path;
    resp = URLRead[
      HTTPRequest[url, <|"Method" -> "GET", "Headers" -> {"Accept" -> "application/json"}|>],
      TimeConstraint -> OptionValue[WRFCoinData, {opts}, TimeConstraint]
    ];
    If[FailureQ[resp], Return[resp, Module]];
    code = resp["StatusCode"];
    Which[
      code === 429,
        Message[WRFCoinData::ratelimit];
        Failure["WRFCoinRateLimited", <|
          "MessageTemplate" :> WRFCoinData::ratelimit, "StatusCode" -> code, "URL" -> url|>],
      code =!= 200,
        Message[WRFCoinData::http, code, url];
        Failure["WRFCoinHTTPError", <|
          "MessageTemplate" :> WRFCoinData::http, "MessageParameters" -> {code, url},
          "StatusCode" -> code, "URL" -> url|>],
      True,
        data = Quiet[ImportByteArray[resp["BodyByteArray"], "RawJSON"]];
        If[AssociationQ[data] || ListQ[data],
          data,
          Failure["WRFCoinBadResponse", <|
            "MessageTemplate" -> "The answer from `URL` was not JSON.", "MessageParameters" -> <|"URL" -> url|>|>]
        ]
    ]
  ];

(* ---- Value helpers: JSON null and absent keys become Missing, never 0 ---- *)

wrfMissing = Missing["NotAvailable"];

wrfQuantity[x_?NumericQ, None] := x;
wrfQuantity[x_?NumericQ, unit_] := Quantity[x, unit];
wrfQuantity[_, _] := wrfMissing;

wrfValue[a_Association, key_String] :=
  Replace[Lookup[a, key, wrfMissing], Null -> wrfMissing];

(* ISO 8601 text ("2026-10-31T22:15:00.000Z", "...+00:00") to a DateObject in its own offset *)
wrfDate[s_String] :=
  Module[{m, tz},
    m = StringCases[s,
      RegularExpression["^(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2}):(\\d{2}):(\\d{2}(?:\\.\\d+)?)(Z|[+-]\\d{2}:\\d{2})?$"] :>
        {"$1", "$2", "$3", "$4", "$5", "$6", "$7"}];
    If[m === {}, Return[wrfMissing, Module]];
    m = First[m];
    tz = Which[
      m[[7]] === "" || m[[7]] === "Z", 0,
      True, (If[StringTake[m[[7]], 1] === "-", -1, 1]) *
        (ToExpression[StringTake[m[[7]], {2, 3}]] + ToExpression[StringTake[m[[7]], {5, 6}]]/60)
    ];
    DateObject[Join[ToExpression /@ m[[1 ;; 5]], {ToExpression[m[[6]]]}], "Instant", "Gregorian", tz]
  ];
wrfDate[_] := wrfMissing;

wrfTime[o_Association] :=
  If[NumericQ[wrfValue[o, "observedAt"]],
    FromUnixTime[wrfValue[o, "observedAt"], TimeZone -> 0],
    wrfDate[wrfValue[o, "timestamp"]]
  ];

wrfGeo[lat_?NumericQ, lon_?NumericQ] := GeoPosition[{lat, lon}];
wrfGeo[__] := wrfMissing;

(* base units (decimal string, 8 decimals) to an exact number of WRF *)
wrfCoins[s_String] /; StringMatchQ[s, DigitCharacter ..] := FromDigits[s]/10^8;
wrfCoins[_] := wrfMissing;

(* ---- Network-wide reads ---- *)

wrfNetwork["Stations", opts___] :=
  Module[{data = wrfGet["/api/weather/stations", opts]},
    If[FailureQ[data], data,
      Dataset[
        <|
          "Alias" -> wrfValue[#, "alias"],
          "Name" -> wrfValue[#, "name"],
          "Location" -> wrfGeo[wrfValue[#, "latitude"], wrfValue[#, "longitude"]],
          "Status" -> wrfValue[#, "status"],
          "LastUpdate" -> wrfDate[wrfValue[#, "lastDataUpdate"]],
          "Active" -> wrfValue[#, "isActive"],
          "QualityScore" -> wrfValue[#, "qualityScore"]
        |> & /@ Replace[Lookup[data, "stations", {}], Except[_List] -> {}]
      ]
    ]
  ];

wrfNetwork["NetworkStatus", opts___] :=
  Module[{d = wrfGet["/api/explorer/summary", opts]},
    If[FailureQ[d], d,
      <|
        "Status" -> wrfValue[d, "status"],
        "Height" -> wrfValue[d, "height"],
        "TipAge" -> wrfQuantity[wrfValue[d, "tipAgeSeconds"], "Seconds"],
        "BlocksPerMinute" -> wrfValue[d, "blocksPerMinute"],
        "Peers" -> wrfValue[d, "peerCount"],
        "FaucetFunded" -> wrfValue[d, "faucetFunded"],
        "Generated" -> wrfDate[wrfValue[d, "generatedAt"]]
      |>
    ]
  ];

wrfNetwork["ChainStatus", opts___] :=
  Module[{d = wrfGet["/api/blockchain/status", opts]},
    If[FailureQ[d], d,
      <|
        "ChainID" -> wrfValue[d, "chainId"],
        "Network" -> wrfValue[d, "network"],
        "Height" -> wrfValue[d, "blockHeight"],
        "TargetBlockTime" -> wrfQuantity[wrfValue[d, "blockTime"], "Seconds"],
        "ActiveValidators" -> wrfValue[d, "activeValidators"],
        "TotalTransactions" -> wrfValue[d, "totalTransactions"],
        "PendingTransactions" -> wrfValue[d, "pendingTransactions"],
        "Status" -> wrfValue[d, "status"],
        "Peers" -> wrfValue[d, "peerCount"],
        "Updated" -> wrfDate[wrfValue[d, "lastUpdated"]]
      |>
    ]
  ];

wrfNetwork["CoverageZones", opts___] :=
  Module[{d = wrfGet["/api/weather/coverage-zones", opts]},
    If[FailureQ[d], d,
      Dataset[
        <|
          "Center" -> wrfGeo[wrfValue[#, "lat"], wrfValue[#, "lng"]],
          "Radius" -> wrfQuantity[wrfValue[#, "radius"], "Kilometers"],
          "Type" -> wrfValue[#, "type"],
          "RewardMultiplier" -> wrfValue[#, "rewardMultiplier"],
          "Stations" -> wrfValue[#, "stationCount"]
        |> & /@ Replace[Lookup[d, "zones", {}], Except[_List] -> {}]
      ]
    ]
  ];

wrfNetwork["RecentBlocks", opts___] :=
  Module[{d = wrfGet["/api/blockchain/blocks", opts]},
    If[FailureQ[d], d,
      Dataset[
        SortBy[
          <|
            "Height" -> wrfValue[#, "height"],
            "Hash" -> wrfValue[#, "hash"],
            "Time" -> wrfDate[wrfValue[#, "timestamp"]],
            "Transactions" -> wrfValue[#, "transactions"]
          |> & /@ Replace[Lookup[d, "blocks", {}], Except[_List] -> {}],
          -Replace[#Height, Except[_?NumericQ] -> 0] &
        ]
      ]
    ]
  ];

(* ---- Station reads ---- *)

wrfObservationsRaw[alias_String, opts___] :=
  Module[{d = wrfGet["/api/stations/" <> alias <> "/observations", opts]},
    If[FailureQ[d], d, Select[Replace[Lookup[d, "observations", {}], Except[_List] -> {}], AssociationQ]]
  ];

wrfObservationRow[o_Association] :=
  Join[
    <|"Time" -> wrfTime[o], "Height" -> wrfValue[o, "height"]|>,
    AssociationThread[
      Keys[wrfSeriesSpec],
      wrfQuantity[wrfValue[o, #[[1]]], #[[2]]] & /@ Values[wrfSeriesSpec]
    ],
    <|
      "Provenance" -> wrfValue[o, "provenanceClass"],
      "AttesterQuorum" -> Replace[
        wrfValue[Replace[wrfValue[o, "attestation"], Except[_Association] -> <||>], "has_quorum"],
        Except[True | False] -> wrfMissing],
      "CommitID" -> wrfValue[o, "commitId"]
    |>
  ];

wrfStation[alias_String, "Observations", opts___] :=
  Module[{obs = wrfObservationsRaw[alias, opts]},
    If[FailureQ[obs], obs,
      Dataset[SortBy[wrfObservationRow /@ obs, Replace[#Time, d_DateObject :> AbsoluteTime[d]] &]]
    ]
  ];

wrfStation[alias_String, "Location", opts___] :=
  Module[{d = wrfGet["/api/weather/stations", opts], hit},
    If[FailureQ[d], Return[d, Module]];
    hit = SelectFirst[Replace[Lookup[d, "stations", {}], Except[_List] -> {}], AssociationQ[#] && Lookup[#, "alias"] === alias &];
    If[MissingQ[hit],
      Message[WRFCoinData::nostation, alias]; Missing["NotFound", alias],
      wrfGeo[wrfValue[hit, "latitude"], wrfValue[hit, "longitude"]]
    ]
  ];

wrfStation[alias_String, prop_String, opts___] /; KeyExistsQ[wrfSeriesSpec, prop] :=
  Module[{obs = wrfObservationsRaw[alias, opts], key, unit, pairs},
    If[FailureQ[obs], Return[obs, Module]];
    {key, unit} = wrfSeriesSpec[prop];
    pairs = Select[
      {wrfTime[#], wrfValue[#, key]} & /@ obs,
      DateObjectQ[#[[1]]] && NumericQ[#[[2]]] &
    ];
    If[pairs === {}, wrfMissing,
      TimeSeries[{#[[1]], wrfQuantity[#[[2]], unit]} & /@ SortBy[pairs, AbsoluteTime[#[[1]]] &]]
    ]
  ];

(* ---- Account read (public balance; returns 404 while the server has it switched off) ---- *)

wrfBalance[address_String, opts___] :=
  Module[{d = wrfGet["/api/public/balance/" <> ToLowerCase[address], opts]},
    If[FailureQ[d], d,
      <|
        "Address" -> wrfValue[d, "address"],
        "Balance" -> wrfCoins[wrfValue[d, "balance"]],
        "Earned" -> wrfCoins[wrfValue[d, "earned"]],
        "Height" -> wrfValue[d, "height"]
      |>
    ]
  ];

(* ---- Public signatures ---- *)

WRFCoinData[opts : OptionsPattern[]] := WRFCoinData["Stations", opts];

WRFCoinData["Properties", OptionsPattern[]] :=
  <|"Network" -> wrfNetworkProperties, "Station" -> wrfStationProperties, "Account" -> {"Balance"}|>;

WRFCoinData[prop_String, opts : OptionsPattern[]] /; MemberQ[wrfNetworkProperties, prop] :=
  wrfNetwork[prop, opts];

WRFCoinData[alias_String?wrfAliasQ, opts : OptionsPattern[]] :=
  WRFCoinData[alias, "Observations", opts];

WRFCoinData[alias_String?wrfAliasQ, prop_String, opts : OptionsPattern[]] :=
  If[MemberQ[wrfStationProperties, prop],
    wrfStation[alias, prop, opts],
    Message[WRFCoinData::badprop, prop, wrfStationProperties];
    Failure["WRFCoinUnknownProperty", <|
      "MessageTemplate" :> WRFCoinData::badprop, "MessageParameters" -> {prop, wrfStationProperties}|>]
  ];

WRFCoinData[aliases : {__String?wrfAliasQ}, prop_String, opts : OptionsPattern[]] :=
  AssociationMap[WRFCoinData[#, prop, opts] &, aliases];

WRFCoinData["Balance", address_String, opts : OptionsPattern[]] :=
  If[wrfAddressQ[address],
    wrfBalance[address, opts],
    Message[WRFCoinData::badaddr, address];
    Failure["WRFCoinBadAddress", <|
      "MessageTemplate" :> WRFCoinData::badaddr, "MessageParameters" -> {address}|>]
  ];

WRFCoinData[s_String, ___] /; StringStartsQ[s, "st_"] && ! wrfAliasQ[s] := (
  Message[WRFCoinData::badstation, s];
  Failure["WRFCoinBadStation", <|"MessageTemplate" :> WRFCoinData::badstation, "MessageParameters" -> {s}|>]
);

WRFCoinData[prop_String, OptionsPattern[]] /; ! StringStartsQ[prop, "st_"] := (
  Message[WRFCoinData::badprop, prop, Join[wrfNetworkProperties, {"Properties", "Balance"}]];
  Failure["WRFCoinUnknownProperty", <|
    "MessageTemplate" :> WRFCoinData::badprop,
    "MessageParameters" -> {prop, Join[wrfNetworkProperties, {"Properties", "Balance"}]}|>]
);
