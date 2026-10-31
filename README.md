# WRFCoin Docs

Guides, implementation status and protocol background for people joining the WRFCoin weather-data testnet.

## Public testnet


Public launch: **2026-10-22**. This is a test network. It may be reset without notice. Balances and tokens have no monetary value. No migration to mainnet is promised or implied. Please attach no production bridges, exchange listings or irreplaceable assets.

- [WRFCoin website](https://wrfcoin.com)
- [Start with the quickstart](testnet/quickstart.md)
- [Help and bug reports](https://github.com/wrfcoin/testnet-support)
- [Security reporting](SECURITY.md)

[Read the facts page](testnet/facts.md).

## Start here

| I want to… | Read this |
| --- | --- |
| Try a wallet, faucet or weather station | [Public testnet quickstart](testnet/quickstart.md). |
| Get the software and verify a download | [Downloads and platform status](testnet/downloads.md); signed artifacts are not yet published. |
| Understand my node's status | [Node status guide](testnet/node-status.md), with current commands and dashboard availability boundaries. |
| Know what is implemented | [Implementation status](STATUS.md), including dated evidence and planned capabilities. |
| Understand the protocol's goals | [Whitepaper](whitepaper/01-vision.md); vision is not a shipping commitment. |
| Find background and open questions | [Wiki](wiki/index.md). |
| Run a sync node | [Operator guide](testnet/operator-guide.md), pointing to the canonical join instructions. |
| Read WRFCoin data in the Wolfram Language | [WRFCoinData for the Wolfram Function Repository](integrations/wolfram/README.md). |
| Browse the generated documentation | [Library](site/library.html) and [wiki browser](site/wiki.html). |

## Today and planned

**Today:** quickstart, software/platform guidance, node-status explanations, the implementation matrix and protocol background are available in this repository. New wallets use ed25519; legacy secp256k1 addresses are receive-only. Documentation and source availability do not establish live service readiness.

**Planned or experimental:** the whitepaper's L2 rollups, DAG sidechain and marketplaces are not current testnet products. Signed software downloads are not yet published. Use each guide's availability notes and the status matrix instead of treating architecture chapters as a feature list.

The public code/documentation snapshots begin with a filtered source commit; their earlier development history stays private. Publishing repositories and deploying their contents are separate steps.

## Repository Layout

```text
whitepaper/       Protocol vision and chapter narrative.
wiki/             Source markdown for the maintained WRFCoin wiki.
testnet/          Operator guide and testnet integration notes.
development/      Design and contributor-facing reference notes.
site/             Generated HTML surfaces.
data/             Curated generated manifests.
cache/            Cached repo/testnet state used by generators.
scripts/          Library/testnet/repo-state generators.
```

## Generate The Site

From the repo root:

```bash
python3 wiki/scripts/generate_wiki_manifest.py --wiki-root wiki --output wiki/data/wiki-manifest.json
python3 wiki/scripts/generate_wiki.py --wiki wiki --output site/wiki.html
python3 scripts/generate_library.py --wiki-manifest wiki/data/wiki-manifest.json
```

The generated HTML is committed intentionally so the docs can be browsed without running the scripts first.

## Status

Testnet, not production. Architecture and implementation notes evolve with the WRFCoin repos. The dated [status matrix](STATUS.md) is authoritative for implemented-versus-planned language in this repository. The wallet key scheme for new wallets is ed25519; legacy secp256k1 addresses are receive-only.

## License

Documentation is licensed under CC BY 4.0; code samples in other WRFCoin repositories are MIT OR Apache-2.0.

See [LICENSE](LICENSE).

---

_Note: issue and pull-request numbers mentioned in this repository refer to a private archive that predates this public repository; they are not links into this repo._
