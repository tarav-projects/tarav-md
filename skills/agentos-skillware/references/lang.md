# agentos-skillware --about (language spec)

The operational spec of the Skillware source language. This module is normative for syntax; the concepts behind it live in `references/doctrine.md`.

## The Src Surface

- `<skill>/.skillware/src/` mirrors the skill tree: `src/references/ground.skw.md` compiles to `references/ground.md` (strip `.skw`); `src/SKILL.skw.md` to `SKILL.md`
- no `.skw.md` = the file is hand-owned; Skillware never touches it — adoption is per-file, a skill can be partially managed
- `.skillware/skillware.json` — settings: `{"depots": [...]}` for `Dotted.Name` resolution, paths relative to the skill root
- `.skillware/lock.json` — build output (output and per-recipe hashes); engine-owned, never hand-edit
- `.skillware/AGENTS.md` — engine-stamped on every build, overwrite-always; redirects agents outside skillware activity to src + toolchain

## Recipe Grammar

A `.skw.md` is markdown plus `[!skw]` callout recipes. A recipe is a blockquote placed **first in its section**; the produced body sits *outside* the callout, as ordinary markdown, from the callout to a `> [!skw] end` one-liner or the next heading:

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

Hand-written tail in the same section, outside the produced body.
```

- first line: `> [!skw]- <verb>` (the fold marker `-` is optional); verbs: `copy`, `derived`, and the `end` closer
- field lines: `> key: value`; a bare `> ...` continuation line appends to the previous field
- `from:` — repeatable, one source per line; `intent:` — the `Derivation.Rule` context, free prose
- the produced body ends at `> [!skw] end` or at the next ATX heading; a heading always closes an open body
- sections without a recipe are hand-owned prose; a src file with no recipes is a plain passthrough
- fenced code blocks are inert: a callout inside ``` fences is an example, not a recipe

## Verbs

- `copy` — the body is the target's expanded body, verbatim; `agentos skillware build` refreshes it mechanically in src (CPU-owned)
- `derived` — the body is the agent-authored current solution of the recipe's rule; the build never touches it — only an agentic re-derive changes it

## Locators

A `from:` value is one of:

- **`path#Region`** — a heading-section body in a file, resolved against the src root first, then the skill root. The region is the section's body: heading excluded, subsections included. A `.skw.md` target is recursively expanded before extraction (innermost first); expansion cycles are an error naming the chain. A plain (non-skw) file yields the raw region body.
- **`Dotted.Name`** — an index block resolved in the configured depots (`skillware.json`); the value is the block's kernel-line body.

## Compilation

- deterministic — no agent in the loop: strip the callout machinery, keep the produced bodies and all hand prose; blank-line runs collapse; output is trimmed
- `copy` bodies are refreshed in src before targets are emitted; `derived` bodies pass through as materialized
- the compiled target never carries Skillware syntax — zero machinery lands on the runnable surface

## Settings

```json
{
  "depots": ["../agentos-pkg"]
}
```

- `depots` — index depots for `Dotted.Name` resolution, relative to the skill root; list order is search order
