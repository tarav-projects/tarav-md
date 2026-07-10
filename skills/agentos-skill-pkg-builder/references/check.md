# agentos-skill-pkg-builder --check

The umbrella check runner. Read-only. Runs every registered check over the package and aggregates the results into one report.

## Registered Checks

- `--skillware-checks` (`references/skillware-checks.md`) — do the Skillware-managed surfaces still hold? (CPU pass via `agentos skillware check`, agentic pass for stale `derived` bodies)
- `--inline-drift` (`references/inline-drift.md`) — does any surface contradict a concept it mentions?
- more checks may register here without changing the public entry surface

## Pass

1. Run each registered check module; scope flows through (`--skill`, `--target`).
2. Aggregate into one report, grouped by check, cited by source and target.
3. Never writes — reconciliation and fixes are separate, gated steps.

Run a single check directly with its own arg (`--skillware-checks`, `--inline-drift`) when you do not want the full sweep.
