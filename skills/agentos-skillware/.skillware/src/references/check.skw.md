# agentos-skillware --check

Report whether a skill's Skillware-managed surfaces still hold, and prescribe the response each finding demands. **Read-only** — this module never writes; acting on the report is a follow-up into `--dev`.

## The Pass

1. Run the CPU check and take its verdicts as given:

   ```
   agentos skillware check --skill <path> [--json]
   ```

2. Report the verdicts, grouped by file, with each flagged recipe named.
3. Prescribe per verdict (below) — proposals, not actions.
4. Exit state: the command exits non-zero on any finding; a clean run is the quiet norm.

## Verdicts

> [!skw]- derived
> from: Import.Management
> intent: expand the block's check/verdict realization lines into the
> operational verdict table — what each verdict means and which response
> it demands; keep the no-silent-blessing rule explicit

Per compiled file:

- `ok` — surface matches src, lock, and dependencies; nothing to do
- `never-built` — src exists but no lock entry; run `build`
- `stale-build` — the on-disk target matches the lock but a recompile differs (src moved); run `build`
- `hand-edited` — the on-disk target differs from the lock: someone edited the compiled surface; a judgment call — sometimes noise to rebuild over, sometimes content that belongs in src (move it, then rebuild)

Per recipe:

- `copy-drift` — a copy body no longer equals its target's expansion; mechanical: `build` repairs it
- `derived-stale` — a dependency changed since the derived body was written; **agentic**: open the src, read the recipe's `from:` targets and `intent:`, and re-derive the body in src so it faithfully transforms the current dependencies

The no-silent-blessing rule: a rebuild carries a stale derivation's old dependency hashes forward while its body is unchanged — `derived-stale` survives any number of builds and clears only when the body is actually re-derived. Dependency targets are `Skw.Address.Schema` names; an unresolvable target is a finding, not a verdict.

> [!skw]- end-derived

## The Re-Derive Pass

For each `derived-stale` flag — the only agentic work in the pass:

1. Open the src file; read the recipe's `from:` targets (current state) and its `intent:`.
2. Re-derive the body in src: the intent is the rule, the fresh targets are the inputs.
3. `agentos skillware build`, then `check` — the body change re-blesses the dependency hashes; a clean run ends the pass.
4. For a gated package, the re-derived wording passes the package's edit gates before landing.

## Boundary

- this module reports and prescribes; it never applies — `--dev` owns src edits and rebuilds
- a drift finding has no predefined winner: source, derivation, or hand edit may each be the truth — resolution is case-by-case
