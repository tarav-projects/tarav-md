# agentos-skillware --about (language spec)

The operational spec of the Skillware source language. This module is normative for syntax; the concepts behind it live in `references/doctrine.md`.

## The Src Surface

- `<skill>/.skw/src/` mirrors the skill tree: `src/references/ground.skw.md` compiles to `references/ground.md` (strip `.skw`); `src/SKILL.skw.md` to `SKILL.md`
- no `.skw.md` = the file is hand-owned; Skillware never touches it — adoption is per-file, a skill can be partially managed
- `.skw/skw.json` — settings: `{"depots": [...]}` for `Dotted.Name` resolution, paths relative to the skill root
- `.skw/lock.json` — build output (output and per-construct hashes); engine-owned, never hand-edit
- `.skw/AGENTS.md` — engine-stamped on every build, overwrite-always; redirects agents outside skillware activity to src + toolchain

## Construct Grammar

The language has one syntactic form — the construct, the written form of a `Skw.Annotation`: a `$kw:` declaration, `$kw.` belonging lines, a flat markdown body, and a mandatory owned closer. Every machinery line carries the sigil, riding the host carrier (blockquote in markdown):

```md
## Grounding Model

> $kw: derived ^grounding-model
> $kw. --from references/search.skw.md^search-model
> $kw. --from Context.Grounding
> $kw. --intent adapt the search doctrine to grounding use; keep depot
> $kw. routing aligned; do not collapse into a copy of search

- the current derived solution, as ordinary markdown
- develop it here, in src — never on the compiled surface

> $kw. end-^grounding-model

Hand-written tail in the same section, outside the produced body.
```

- declaration: `> $kw: <command> [^label] [--flag value …]` — CLI-style, inline when short (`> $kw: copy --from references/lib.skw.md#Alpha`); the optional `^label` token gives the span a stable, heading-independent identity; `label ^x` is the explicit command for a labeled literal (command-less declarations are invalid); a label duplicated within one file is a finding
- belonging lines: `> $kw. …` directly under the declaration — `--flag value` adds a flag occurrence (`--from` repeats), a plain continuation appends to the previous flag's value; a non-end `$kw.` line separated from its declaration is a stray-line finding
- flags are the registered trait vocabulary: `--from` (inbound dependency, repeatable), `--intent` (the derivation rule's context), `--to` (outbound send, reserved); only registered flags bound values — an unregistered `--token` mid-value is prose, but in flag position it is a finding
- body: flat markdown at column 0 — never indented; nesting is logical (the parse stack + owned ends), never visual; the body is runnable prose first
- closure is fully explicit: every construct ends with `> $kw. end-<command>` or `> $kw. end-^label` (either owner matches; the label is the more precise); a bare `end` is invalid; a heading closes nothing — a construct still open at a heading or EOF is a finding (bodies cannot span headings)
- multi-close: `> $kw. end-a end-b` unwinds the open stack innermost-first; a mismatched or wrongly ordered owner is a finding naming the expected close; end lines take no args
- fenced code blocks are inert: machinery inside ``` fences is an example, not a construct
- everything outside constructs is hand-owned prose; a src file with no constructs is a plain passthrough
- the parser is a `Closure.Parser`: below its `Parse.Floor` (well-formed machinery, explicit closure, unique labels, sane router rows) it emits parse errors; above the floor everything it does not recognize is opaque text, and nothing else can fail the parse

## Primitives

Position-free leaves — any number per section, anywhere; a construct may not open inside a primitive body:

- `text` — a tagged literal: plain content, no binding; the tag only makes the span addressable (`label ^x` is its labeled spelling)
- `copy` — the body is the target's expanded body, verbatim; `agentos skw build` refreshes it mechanically in src (CPU-owned); flags: `--from` (exactly one)
- `derived` — the body is the agent-authored current solution of the construct's derivation rule; the build never touches it — only an agentic re-derive changes it; flags: `--from` (repeatable), `--intent` (the rule's context, free prose)

## Structural Commands

Structural commands compose primitives and carry no lock state — their checks are parse findings:

- `router` — a `Semantic.Router` section: its body holds alternating `when`/`then` rows (plus free prose); a row out of order or a `when` with no `then` is a finding
- `when` — a row's key: the situation, as full markdown (paragraphs welcome); valid only inside an open `router`
- `then` — the row's response: what to load or do, as prose; valid only inside an open `router`

```md
## Router Table

> $kw: router

> $kw: when
When the caller wants to find concepts or retrieve cited index context.

Includes the read-only pass that precedes any edit proposal.
> $kw. end-when

> $kw: then
Load `references/search.md`.
> $kw. end-then

> $kw. end-router
```

## Locators

A `--from` value is one of:

- **`path#Region`** — a heading-section body in a file, resolved against the src root first, then the skill root. The region is the section's body: heading excluded, subsections included. A `.skw.md` target is recursively expanded before extraction (innermost first); expansion cycles are an error naming the chain. A plain (non-skw) file yields the raw region body.
- **`path^label`** — a labeled span in a src file; **`^label`** alone is file-local (the current src). Labels are heading-independent, so the import survives section renames, and the dependency hash covers only the span — a consumer drifts with its fragment, not the file. Labels live only in src machinery (stripped at compile), so they address src files exclusively; renaming a label breaks importers, which the unresolvable-`--from` POI catches.
- **`Dotted.Name`** — an index block resolved in the configured depots (`skw.json`); the value is the block's kernel-line body.

## Compilation

- deterministic — no agent in the loop: strip every construct's machinery (declaration, belonging lines, owned ends), keep the bodies and all hand prose; blank-line runs collapse; output is trimmed
- `copy` bodies are refreshed in src before targets are emitted; `derived` bodies pass through as materialized
- the compiled target never carries Skillware syntax — zero machinery lands on the runnable surface

## Settings

```json
{
  "depots": ["../agentos-pkg"]
}
```

- `depots` — index depots for `Dotted.Name` resolution, relative to the skill root; list order is search order
