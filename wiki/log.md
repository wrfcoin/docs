# WRFCoin Wiki Log

Append-only record of wiki maintenance, source ingests, queries, and lint passes. Single-line prefix format so `grep "^## \[" log.md | tail -10` gives a clean recent-activity view.

```markdown
## [YYYY-MM-DD] ingest | Source Title

- Source: `path/or/url`
- Pages touched: [[page-a]], [[page-b]]
- Summary: One or two sentences.
- Follow-ups: Open questions or next actions.
```

## [2026-05-25] migrate | Docs repo organization

- Source: Linux-side staging wiki and the existing `wrfcoin/docs` clone.
- Pages touched: the historical agent guide (no longer published), [[index]], `wiki/data/wiki-manifest.json`, `site/wiki.html`, `site/library.html`.
- Summary: Migrated the wiki into the private docs repo, updated generator paths to be repo-local, and kept the generated site surfaces as committed browsing artifacts.
- Follow-ups: Run a dedicated lint pass to replace placeholder README pages and ingest current product-repo docs into synthesis pages.

## [2026-05-18] migrate | v1 → v2 schema upgrade

- Source: Third-agent ingest plan; instrument-showcase v2 schema reference.
- Pages touched: the historical agent guide (no longer published), [[index]], directory contract (removed `architecture/`, `operations/`, `security/`; added `economics/`, `implementation/`, `governance/`, `release/`, `data/`, `scripts/`).
- Summary: Wiki upgraded to v2 frontmatter schema. New directory contract aligned to the whitepaper's chapter structure. QMD retrieval-layer section preserved and extended with cross-domain library-bridge wiring.
- Follow-ups: First-pass content ingest (next entries).

## [2026-05-18] scaffold | Manifest generator and library bridge

- Source: `scripts/generate_library.py` consumes `wiki-manifest.json` at three candidate paths.
- Pages touched: `scripts/generate_wiki_manifest.py`, `data/wiki-manifest.json`, `site/library.html`.
- Summary: Created the wiki-manifest generator (parses YAML frontmatter, emits `wrfcoin-wiki-manifest-v1`). Ran it. Ran the cross-domain library generator with `--wiki-manifest` pointing at it. `library.html` now reports wiki coverage from this wiki's frontmatter.
- Follow-ups: Add an aggregate open-questions script to companion the manifest generator.

## [2026-05-18] ingest | Whitepaper chapter 01 — Vision

- Source: `whitepaper/01-vision.md`
- Pages touched: [[vision]]
- Summary: Created framing page from chapter 01. Captured the three-brittle-assumptions / three-changes framing and the three architectural requirements the vision implies. 5 open questions raised, mostly around whether vision claims (institutional trust under climate pressure, long-tail data volume, additive-not-replacement) are anchored to evidence vs aspirational.
- Follow-ups: Resolve the "first 12-month proof-of-life metric" question once a hyperlocal use case is committed to in [[release/testnet-roadmap]].

## [2026-05-18] ingest | Whitepaper chapter 02 — Origin Story

- Source: `whitepaper/02-origin-story.md`
- Pages touched: [[origin-story]]
- Summary: Created framing page from chapter 02. Three project phases (Phase 1 Dec 2022, Skyward Jan 2023, Reboot Feb 2025) with the Reboot identified as the design-defining moment. 5 open questions raised, mostly around what survived from Skyward, Meta-OS specificity, and the legal/governance status of the investor-vs-contributor distinction.
- Follow-ups: Cross-reference Meta-OS framing against actual core4 / sprint state to determine whether it's a Phase-3 deliverable or a cross-cutting capability.

## [2026-05-18] ingest | Whitepaper chapter 03 — Three-Layer Architecture

- Source: `whitepaper/03-architecture.md`
- Pages touched: [[protocol/architecture]]
- Summary: Created protocol page from chapter 03. L1 (settlement) + L2 (rollups) + Data Sidechains (DAG) split. 7 open questions raised: L2 type, DAG protocol identity, batch cadence, cross-layer slashing, data-sidechain code location, public API interface, IoT submission permissioning.
- Follow-ups: Highest-leverage open items are cross-layer slashing protocol and DAG protocol identity. Both block [[synthesis/cross-section-tradeoffs]] tradeoffs #1 and #2.

## [2026-05-18] ingest | Whitepaper chapter 04 — Proof of Publication

- Source: `whitepaper/04-consensus.md`
- Pages touched: [[protocol/proof-of-publication]]
- Summary: Created protocol page from chapter 04. Four roles (contributors, validators, forecasters, verifiers), stake-and-slash for first two, reputation-weighted for forecasters, audit-of-audits for verifiers. 8 open questions raised, four of them lifted verbatim from the whitepaper's own "what's still being designed" list.
- Follow-ups: Sybil resistance is the highest-priority open item. Cross-link to [[synthesis/cross-section-tradeoffs]] tradeoff #1 PoPub-latency-vs-economics and tradeoff #2 sidechain-autonomy.

## [2026-05-18] ingest | Whitepaper chapter 05 — WRF & WRC-20

- Source: `whitepaper/05-tokenomics.md`
- Pages touched: [[economics/wrf-token]]
- Summary: Created economics page from chapter 05. WRF utility token (4 roles: reward, stake, governance, settlement), WRC-20 ecosystem standard with first-class data-linkage / validation-gates / impact-metadata, investor-equity-vs-contributor-token split, DeFi explicitly deferred. 8 open questions raised, dominated by deferred parameters + missing WRC-20 specification document.
- Follow-ups: Locate or commission the WRC-20 specification document; resolve slashing-destination (also open in [[protocol/proof-of-publication]]).

## [2026-05-18] ingest | Whitepaper chapter 06 — Tech Stack

- Source: `whitepaper/06-tech-stack.md`
- Pages touched: [[implementation/tech-stack]]
- Summary: Created implementation page from chapter 06. Rust + Cargo workspace, conservative cryptography (SHA-256 / Ed25519 / BIP-39; the original chapter also listed Bech32, which was later corrected — addresses are `0x` + hex SHA3-256), libp2p planned post-testnet, supply-chain tooling on every CI build. 8 open questions raised. Most material: whitepaper workspace structure (`core/network/wallet/cli`) does not match the actual `~/wrfcoin/core4/` workspace (`shared-protocol/native-chain/consensus-engines/p2p/privacy/...`).
- Follow-ups: Whitepaper-vs-core4 workspace drift is the most actionable open item. Either update the whitepaper or write a synthesis page that maps both views.

## [2026-05-18] ingest | Whitepaper chapter 07 — Testnet Roadmap

- Source: `whitepaper/07-roadmap.md`
- Pages touched: [[release/testnet-roadmap]]
- Summary: Created release page from chapter 07. Four phases (Foundation / Weather Oracle / Meta-OS / Ecosystem). Testnet target mid-2026. Capability-gated, not date-fixed. 9 open questions raised. Phase 1 completion status is the most pressing — the whitepaper text predates the current Linux-side state (node host testnet operating, 1555+ blocks, second peer online) which looks like Phase-1 endgame.
- Follow-ups: Declare Phase 1 complete with explicit evidence pointers, or describe the gap that keeps it open.

## [2026-05-18] answer-as-page | Open Questions Rollup

- Source: All seven first-ingest pages.
- Pages touched: [[synthesis/open-questions-rollup]]
- Summary: Aggregated all 50 chapter-page open questions + 1 self-rollup-meta question into one page, grouped by source page, with a Theme Index that clusters them into 7 themes (anti-collusion, cross-layer slashing, tokenomics parameters, phase definitions, workspace drift, governance/legal posture, aspirational framing).
- Follow-ups: Add a `scripts/aggregate_open_questions.py` companion to the manifest generator so this page rebuilds mechanically.

## [2026-05-18] answer-as-page | Cross-Section Design Tradeoffs

- Source: All seven first-ingest pages.
- Pages touched: [[synthesis/cross-section-tradeoffs]]
- Summary: Surfaced 5 load-bearing design tensions that span chapters: (1) PoPub data-publication latency vs validator economics, (2) sidechain autonomy vs L1 settlement guarantees, (3) WRC-20 standard scope vs developer ergonomics, (4) anti-speculation tokenomics vs liquidity / network effects, (5) single-developer pace vs Phase-2 ambition. Each names where the tension shows up across chapters, what the design seems to want, and what would close the tradeoff.
- Follow-ups: As project commits to specific positions, file resolutions as separate `synthesis/<slug>.md` pages and strikethrough the tension above.
## [2026-09-20] ingest | Public documentation truth-status refresh

- Source: readiness evidence, current whitepaper chapters, and implementation references.
- Pages touched: [[index]], [[protocol/architecture]], [[protocol/proof-of-publication]], [[economics/wrf-token]], [[implementation/tech-stack]], [[release/testnet-roadmap]].
- Summary: Separated implemented, partial, planned, and not-offered capabilities; recorded the deployed-versus-main gap; pinned the ed25519/legacy-secp256k1 boundary; removed the obsolete minimal-TCP and date-target framing.
- Follow-ups: Re-check public reachability only after the infra endpoint/status work is deployed and human visibility gates are complete.
