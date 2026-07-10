# Skillware

Skillware is the skill-development compilation system: a skill's runnable files are produced from `.skillware/src/**/*.skw.md` sources. The src surface is the pollutable workspace — all specification, dependency, and derivation material lives there; zero machinery lands on the compiled surface.

## The Src Surface

- `<skill>/.skillware/src/` mirrors the skill tree: `references/ground.skw.md` compiles to `references/ground.md` (strip `.skw`)
- no `.skw.md` = the file is hand-owned; Skillware never touches it
- settings in `.skillware/skillware.json` — `{"depots": [...]}` for `Dotted.Name` resolution (paths relative to the skill root)
- `.skillware/lock.json` is build output (dep and output hashes); never hand-edit it

## Recipes

A `.skw.md` is markdown plus `[!skw]` callout recipes. A recipe is a blockquote placed first in a section; the produced body sits *outside* the callout, as ordinary markdown, from the recipe to a `> [!skw] end` one-liner or the next heading:

```md
## Grounding Model

> [!skw]- derived
> from: references/search.skw.md#Search Model
> from: Context.Grounding
> intent: adapt the search doctrine to grounding use; keep depot
> routing aligned; do not collapse into a copy of search

- the current derived solution, as ordinary markdown
- develop it here, in src — never on the compiled surface

> [!skw] end

Hand-written tail in the same section, outside the derived body.
```

- `copy` — the body is the target's expanded body; `agentos skillware build` refreshes it mechanically
- `derived` — the body is the agent-authored current solution; only an agentic re-derive changes it
- `from:` locators: `path#Region` (src-root then skill-root; a `.skw.md` target is recursively expanded), or a bare `Dotted.Name` index block resolved in the configured depots
- sections without a recipe are hand-owned prose; a src file with no recipes is a plain passthrough

## The Toolchain

- `agentos skillware build --skill <path>` — refresh copy bodies in src, compile targets, write the lock
- `agentos skillware check --skill <path>` — drift verdicts, exits non-zero on findings (see `references/skillware-checks.md`)
- `agentos skillware status --skill <path>` — inventory of managed files, recipes, lock state

## Discipline

- never hand-edit a compiled file — develop in src and rebuild; `check` reports hand edits as findings
- a failed check is a drift finding with no predefined winner — resolution is case-by-case; a particular workflow may set auto-regeneration as its own rule
- build never blesses a stale `derived` body: its dependency hashes persist in the lock until the body itself is re-derived
