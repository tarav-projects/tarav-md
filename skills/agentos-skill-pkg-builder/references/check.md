# agentos-skill-pkg-builder --check

The umbrella check runner. Read-only. Runs every registered check over the package and aggregates the results into one report.

## Registered Checks

- `--manifest-checks` (`references/manifest-checks.md`) — do the declared `Derivation.Rule`s still hold?
- `--inline-drift` (`references/inline-drift.md`) — does any surface contradict a concept it mentions?
- more checks may register here without changing the public entry surface

## Pass

1. Run each registered check module; scope flows through (`--manifest`, `--target`).
2. Aggregate into one report, grouped by check, cited by source and target.
3. Never writes — reconciliation and fixes are separate, gated steps.

Run a single check directly with its own arg (`--manifest-checks`, `--inline-drift`) when you do not want the full sweep.
