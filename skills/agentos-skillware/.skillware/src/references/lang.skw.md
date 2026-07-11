# agentos-skillware --about (language spec)

The operational spec of the Skillware source language. This module is normative for syntax; the concepts behind it live in `references/doctrine.md`.

## The Src Surface

- `<skill>/.skillware/src/` mirrors the skill tree: `src/references/ground.skw.md` compiles to `references/ground.md` (strip `.skw`); `src/SKILL.skw.md` to `SKILL.md`
- no `.skw.md` = the file is hand-owned; Skillware never touches it — adoption is per-file, a skill can be partially managed
- `.skillware/skillware.json` — settings: `{"depots": [...]}` for `Dotted.Name` resolution, paths relative to the skill root
- `.skillware/lock.json` — build output (output and per-construct hashes); engine-owned, never hand-edit
- `.skillware/AGENTS.md` — engine-stamped on every build, overwrite-always; redirects agents outside skillware activity to src + toolchain

## Construct Grammar

The language has one syntactic form — the `Skillware.Construct`: a declaration callout, arg lines, a flat markdown body, and a mandatory owned closer:

```md
## Grounding Model

> [!skw]- derived
> from: references/search.skw.md#Search Model
> from: Context.Grounding
> intent: adapt the search doctrine to grounding use; keep depot
> routing aligned; do not collapse into a copy of search

- the current derived solution, as ordinary markdown
- develop it here, in src — never on the compiled surface

> [!skw]- end-derived

Hand-written tail in the same section, outside the produced body.
```

- declaration: `> [!skw]- <command>` (the fold marker `-` is optional)
- args: `> key: value` lines directly under the declaration; a bare `> ...` continuation line appends to the previous key; each command declares which keys it accepts
- body: flat markdown at column 0 — never indented; nesting is logical (the parse stack + owned ends), never visual; the body is runnable prose first
- closure is fully explicit: every construct ends with `> [!skw]- end-<command>`; a bare `end` is invalid; a heading closes nothing — a construct still open at a heading or EOF is a finding (bodies cannot span headings)
- multi-close: `> [!skw]- end-a end-b` unwinds the open stack innermost-first; a mismatched or wrongly ordered owner is a finding naming the expected close
- fenced code blocks are inert: a callout inside ``` fences is an example, not a construct
- everything outside constructs is hand-owned prose; a src file with no constructs is a plain passthrough

## Primitives

Position-free leaves — any number per section, anywhere; a construct may not open inside a primitive body:

- `text` — a tagged literal: plain content, no binding; the tag only makes the span addressable
- `copy` — the body is the target's expanded body, verbatim; `agentos skillware build` refreshes it mechanically in src (CPU-owned); args: `from:` (one target)
- `derived` — the body is the agent-authored current solution of the construct's `Derivation.Rule`; the build never touches it — only an agentic re-derive changes it; args: `from:` (repeatable), `intent:` (the rule's context, free prose)

## Structural Commands

Structural commands compose primitives and carry no lock state — their checks are parse findings:

- `router` — a `Semantic.Router` section: its body holds alternating `when`/`then` rows (plus free prose); a row out of order or a `when` with no `then` is a finding
- `when` — a row's key: the situation, as full markdown (paragraphs welcome); valid only inside an open `router`
- `then` — the row's response: what to load or do, as prose; valid only inside an open `router`

```md
## Router Table

> [!skw]- router

> [!skw]- when
When the caller wants to find concepts or retrieve cited index context.

Includes the read-only pass that precedes any edit proposal.
> [!skw]- end-when

> [!skw]- then
Load `references/search.md`.
> [!skw]- end-then

> [!skw]- end-router
```

## Locators

A `from:` value is one of:

- **`path#Region`** — a heading-section body in a file, resolved against the src root first, then the skill root. The region is the section's body: heading excluded, subsections included. A `.skw.md` target is recursively expanded before extraction (innermost first); expansion cycles are an error naming the chain. A plain (non-skw) file yields the raw region body.
- **`Dotted.Name`** — an index block resolved in the configured depots (`skillware.json`); the value is the block's kernel-line body.

## Compilation

- deterministic — no agent in the loop: strip every construct's machinery (declaration, args, owned ends), keep the bodies and all hand prose; blank-line runs collapse; output is trimmed
- `copy` bodies are refreshed in src before targets are emitted; `derived` bodies pass through as materialized
- the compiled target never carries Skillware syntax — zero machinery lands on the runnable surface

## Settings

```json
{
  "depots": ["../agentos-pkg"]
}
```

- `depots` — index depots for `Dotted.Name` resolution, relative to the skill root; list order is search order
