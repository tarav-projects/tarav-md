# agentos-skillware --dev (build)

> $kw: --from Context.Loading.Path

Make a skill's Skillware-managed surfaces match their sources. The builder never generates a surface from scratch — building means compiling `.skw/src/` and reconciling drift.

## Commands

- `agentos skw build --skill <path>` — the deterministic compile: refresh `copy` bodies in src, compile every `.skw.md` to its target, write `lock.json`, stamp `.skw/AGENTS.md`
- `agentos skw status --skill <path>` — inventory: managed files, recipe counts, lock state
- `agentos skw context --skill <path>` — audit every `--reachable-from` assertion visible in the package graph and print its typed witness path
- `agentos skw context --skill <path> --target <runnable-file>` — resolve local `Context.Loading.Path` declarations or a package-qualified target's reachability witness, validate applicable dependencies, and assemble each path-specific `Projected.Context`
- all take `--json` for machine-readable output

## What Build Does

1. Expands each src file: locators resolved, `.skw.md` targets recursively expanded, cycles rejected.
2. Refreshes `copy` bodies **in src** — the mechanical half of maintenance; `derived` bodies pass through untouched.
3. Emits each target: callout machinery stripped, blank runs collapsed, output trimmed.
4. Writes the lock and stamps `AGENTS.md` (engine-owned, overwrite-always).

## The Lock Model

- per target file: the output hash, plus per-recipe state — verb, body hash, and role-qualified dependency hashes; `--dev-from` and `--cite` participate alongside generic `--from`
- **derived dependency hashes persist until the body itself changes**: a rebuild carries the old dep hashes forward while the derived body is unchanged, so building can never silently bless a stale derivation — only an actual re-derive (a body change) re-blesses
- the lock is engine-owned; never hand-edit it

## Discipline

- all work happens in src — never edit a compiled file directly; `check` reports hand edits as findings
- src edits are workspace edits; content reaches the runnable surface only through `build`
- writing to src for a gated package still follows the package's own edit gates — propose, get approval, then rebuild
- after a build, run `agentos skw check` — a build that leaves `derived-stale` flags has surfaced agentic work, not completed it (`references/check.md`)
