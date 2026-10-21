# Forecasting on the public testnet

**Not yet published — 2026-10-19:** the reference forecast kit is proposed post-launch work, not yet on core4 main or available as a public installation; this page describes its intended workflow, not a deployed forecasting service or a promise of credit.

Testnet tokens have no monetary value, and the network may reset. Read the [quickstart](quickstart.md) and [launch facts](facts.md) before preparing a submission.

## Installation: wait for the public kit

The intended location is `tools/forecast-kit` in the [core4 repository](https://github.com/wrfcoin/core4). No install command is offered until that directory and its matching CLI are published on public main. Private development PR references and commit hashes do not transfer to the new public snapshot repository.

The proposed requirements are Python 3.10+ and the matching `wrfcoin` CLI; optional learned-model prediction also needs NumPy, ONNX Runtime and a published model. When available, follow the kit's public README and verify its version before running it. The workflow below is a preview of that kit, not a substitute installer.

## What is available and what is pending

The proposed kit fetches observations, predicts, and writes files plus **validate-only** CLI commands; it does not submit transactions. The wallet owner decides whether to submit each commit and reveal. Source preparation, transaction acceptance, finalization and credited rewards are separate outcomes.

Above-baseline receipts need the receipt signer deployed with an authorized oracle key and a scoring policy; signer source alone does not establish that service. Without an accepted receipt, consensus uses baseline forecast skill **0.1**, not a guarantee of payment.

Stations lacking humidity cannot supply truth for a three-variable learned forecast: predictions can fall back to the variables present, but scoring only those reported variables is **pending** integration and validation, not a shipped payout promise.

## 1. Fetch observations

The proposed `fetch-observations` step supports the public backend's short chain tail, a node's longer history using a Reader credential, or a local CSV. An hourly read can grow a deduplicated local store without submitting anything.

Public aliases and on-chain station IDs are different: identify the correct on-chain ID from the selected observation's commit status and use that ID consistently in the forecast and manifest. Never submit a forecast still labelled with an alias or placeholder. Do not put credentials, private locations or full configuration files in shared reports.

## 2. Predict

The proposed `predict` step writes `forecast.json` and `window.json` for a six-hour-ahead forecast. The learned model needs a complete 24-hour input window; incomplete inputs or missing model data trigger a labelled persistence fallback. Missing observations are a data limitation, not evidence of model skill.

## 3. Prepare and validate a commit

The proposed `prepare-commit` step writes `data.json`, `manifest.json`, `commit.json` and a `commit.sh` script that calls `wrfcoin forecast commit --validate-only`. Once the matching CLI is public, validation will parse/sign the request locally and return `submitted: false`; it is not transaction submission.

Use the correct station, forecast window, wallet address and chain binding. The wallet must be bound to the node's Contributor credential, and its owner-controlled signing key file must have mode 0600. Compare the CLI's returned commit ID with `commit.json` and stop if they differ.

## 4. The owner submits and later reveals

After reviewing the generated files, destination node and chain binding, the wallet owner can submit through `wrfcoin forecast commit` using the published CLI's documented authentication, without `--validate-only`. This is a chain write; retain the response and transaction ID rather than treating successful local validation as submission.

Wait until the forecast's target time before the proposed `prepare-reveal` step. It checks the prepared files and produces a validate-only `wrfcoin forecast reveal` command; attach an oracle receipt only if one has been issued for this commit and manifest. Structural binding checks are not proof of oracle authorization or final consensus acceptance. Do not bypass the target-time check for a real submission.

After reviewing the validation result, the owner may submit the reveal through the matching CLI without `--validate-only`. The preparation kit itself must remain read-only with respect to the chain.

## 5. Read the receipt, status and credit

Keep the manifest digest, commit ID, transaction IDs and any signed receipt together. The proposed `status` command reads commit status; inspect the receipt's skill and oracle identity, check that status, and separately inspect wallet history for credit. Neither a model score nor a submission response proves credit. If status or history is unavailable, record it as unknown rather than inventing a reward.

## Skill and truth

Skill measures forecast error relative to a reference, usually on a 0–1 scale, but the prototype's per-forecast climatology comparison and the library's RMSE-based metric are different definitions. Consensus consumes an authorized signed receipt; it does not independently observe the weather. A station's attested later observation is not the same evidence as an independent reference analysis.

The detailed scorer truth-source note is proposed at `docs/forecast/scorer-truth-source.md` in core4, but it is **not yet published on main**, so a public link is pending. That note must establish the metric definition, truth source, missing-variable policy and reference limitations before readers treat a skill value as comparable across methods. For broader implemented-versus-planned boundaries, see [implementation status](../STATUS.md).

## A bounded weekly routine for an agent

- Hourly: fetch observations for a small station watch list, without submitting.
- At most N times per station per day: predict and prepare/validate files for the owner's review queue.
- After each target time: prepare/validate the reveal, adding a receipt only if the oracle issued one.
- Daily: check pending commit status and reconcile credited wallet history.
- Weekly: compare held-out predictions with a persistence reference and record the metric definition, coverage and missing data before changing models.

The planned workload is `N × station count × 7` commits per week, not a quota grant; respect current node limits and keep compute and submission budgets separate. Quota and anti-gaming implementation remain separate work. No cron job should silently turn validation into spending or chain submission.

Return to [software availability](downloads.md) or ask a non-sensitive question through [testnet support](https://github.com/wrfcoin/testnet-support).
