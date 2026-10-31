#!/usr/bin/env wolframscript
(* Load the definition and run Tests.wlt. Exit code 0 when every test passes. *)
dir = DirectoryName[$InputFileName];
Get[FileNameJoin[{dir, "WRFCoinData.wl"}]];
report = TestReport[FileNameJoin[{dir, "Tests.wlt"}]];
Print[report["TestsSucceededCount"], " passed, ", report["TestsFailedCount"], " failed"];
Scan[
  If[#["Outcome"] =!= "Success",
    Print["FAILED (", #["Outcome"], "): ", #["TestID"], "\n  got: ", #["ActualOutput"], "\n  expected: ", #["ExpectedOutput"]]] &,
  Values[report["TestResults"]]];
Exit[If[report["AllTestsSucceeded"], 0, 1]];
