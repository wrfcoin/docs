# Testnet operator guide

This repository does not carry a fork of deployment instructions.

The canonical operator guide lives beside the deployment code in the private
[`wrfcoin/infra`](https://github.com/wrfcoin/infra) repository at
`testnet/TESTNET_OPERATOR_GUIDE.md`. That location owns compose files,
environment checks, launch gates, rollback steps, and the generated public
endpoint document.

Until the operator guide is deliberately reviewed for public release:

- do not copy commands from archived versions of this file;
- do not infer that a route on a repository branch is deployed;
- do not publish hostnames, addresses, credentials, or tailnet details;
- do not deploy, restart, or change repository visibility from documentation.

Public readers should use [Implementation status](../STATUS.md). A public join
guide will be linked here only after the endpoint/status work is reviewed and a
human completes the release and visibility gates.
