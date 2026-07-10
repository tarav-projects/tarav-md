# agentos-skill-pkg-builder --skillware-checks

Report whether each Skillware-managed surface still holds. See `references/skillware.md` for the src and recipe format.

## Pass

0. Run the CPU check and take its verdicts as given:

   ```
   agentos skillware check --skill <path> [--json]
   ```

   Per compiled file: `ok` / `never-built` / `stale-build` (rebuild) / `hand-edited` (a finding to resolve case-by-case), plus per-recipe flags: `copy-drift` (build repairs) and `derived-stale` (a dependency changed since the solution was written).

1. For each `derived-stale` flag — the only agentic work — open the src file, read the recipe's `from:` targets and `intent:`, and re-derive the body *in src* so it faithfully transforms the current dependencies.
2. Re-run `agentos skillware build`, then `check` — a re-derived body re-blesses its dependency hashes; a clean run ends the pass.
3. `hand-edited` findings are judgment calls: sometimes the hand edit is noise to rebuild over, sometimes it is content that belongs in src — move it, then rebuild.

## Output

- the CPU report, then the re-derive actions taken (or proposed, where writes are gated)
- src edits are workspace edits; compiled-surface content changes ship through `build`
