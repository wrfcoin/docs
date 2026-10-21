# Contributing

Read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.
For vulnerabilities, use the private [security reporting policy](SECURITY.md).

## Build and checks

Generate documentation from the repository root using the README commands:

```sh
python3 wiki/scripts/generate_wiki_manifest.py --wiki-root wiki --output wiki/data/wiki-manifest.json
python3 wiki/scripts/generate_wiki.py --wiki wiki --output site/wiki.html
python3 scripts/generate_library.py --wiki-manifest wiki/data/wiki-manifest.json
```

Preview changed Markdown and generated HTML, check links, and review generated diffs before committing. Keep factual claims tied to the dated [implementation status](STATUS.md).

## Branch and pull request flow

1. Search existing issues and PRs before starting work.
2. Create a focused branch from current `main` (use a fork when available).
3. Add or update relevant tests for behavior changes and run the checks above.
4. Open a PR describing what changed, why, and the checks you ran. Include `Refs #N` for the relevant issue.
5. Address review feedback before a maintainer merges the PR.

Documentation-only changes require a rendered preview and link checks. State any checks you could not run; do not label skipped checks as passing. Keep secrets and personal information out of commits, logs, and screenshots.
