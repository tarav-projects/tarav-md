# agentos-skillware --about (language spec)

The operational spec of the Skillware source language. This module is normative for syntax; the concepts behind it live in `references/doctrine.md`.

## The Src Surface

- `<skill>/.skw/src/` mirrors the skill tree: `src/references/ground.skw.md` compiles to `references/ground.md` (strip `.skw`); `src/SKILL.skw.md` to `SKILL.md`
- no `.skw.md` = the file is hand-owned; Skillware never touches it — adoption is per-file, a skill can be partially managed
- `.skw/skw.json` — settings: `{"depots": [...], "unlock_registries": [...]}` for `Dotted.Name` resolution and explicit `Poi.Unlock.Token` registry imports; paths are relative to the skill root
- `.skw/lock.json` — build output (output and per-construct hashes); engine-owned, never hand-edit
- `.skw/AGENTS.md` — engine-stamped on every build, overwrite-always; redirects agents outside skillware activity to src + toolchain

## Block Grammar

The language has one syntactic form — the **block**, the written form of a `Skw.Annotation`. A block is `> $kw:` open fence, `> --flag` belonging lines, a native body, and — for a content block — a `> $kw. end` closer. The `$kw` sigil rides the host carrier (blockquote in markdown) only on the two **fence** lines; every other machinery line is a self-marked `--flag`:

```md
## Grounding Model

> $kw: ^grounding-model --derived
> --from references/search.skw.md^search-model
> --from Context.Grounding
> --intent adapt the search doctrine to grounding use; keep depot
> --cont routing aligned; do not collapse into a copy of search

- the current derived solution, as ordinary markdown
- develop it here, in src — never on the compiled surface

> $kw. end

Hand-written tail in the same section, outside the produced body.
```

- **open fence**: `> $kw: [address] [--flags]` — the address (optional, orthogonal) is the block's identity; inline flags are legal when short (`> $kw: --copy --from references/lib.skw.md#Alpha`)
- **belonging lines**: `> --flag value` directly under the open — each self-marked by `--`; `--from` repeats; `--cont value` appends to the previous flag's value; a non-`--` `$kw.` line, or a stray `--flag` line separated from its open, is a finding
- **address**: one explicit `Skw.Address.Schema` locator — `#region` (relative, resolved against the current surface), `path#region` (absolute, cited from elsewhere), or `^label` (a src-only span, stripped at compile). It is the block's identity, not a second id; a duplicated address in one file is a finding
- **body**: native surface text at column 0 — never indented; nesting is logical (the parse stack + owned ends), never visual
- **fenced code blocks are inert**: machinery inside ``` fences is an example, not a block

## Features are flags

The binding mode and every other feature is an additive `--flag`; there are no command words:

- `--derived` — the body is the agent-authored current solution of the block's derivation rule; the build never touches it, only an agentic re-derive does (materializing)
- `--copy` — the body is the target's expanded body, verbatim; `agentos skw build` refreshes it mechanically in src, CPU-owned; exactly one `--from` (materializing)
- `--pointer` — a by-reference binding (non-materializing)
- `--from <locator>` — a generic inbound dependency edge (`Skw.Ann.Dependency`), repeatable
- `--dev-from <locator>` — whole-target builder context; the developing agent loads it, while the compiled surface need not mention it
- `--cite <locator>` — a dependency that must remain explicit in the compiled surface; a missing visible citation raises `uncited-dependency`
- `--context-assembly` — a line-1, self-closing file declaration marking the complete `.skw.md` module as a `Context.Assembly.Module`; its repeatable `--from` values define its direct package-local coverage boundary
- `--unlock-surface` — marks one explicitly addressed context surface represented by one token in the registry named by its single `--from`; takes no value
- `--intent <text>` — the derivation rule's context, free prose; a binding flag's own trailing text folds into it
- `--note [TYPE] <text> ^anchor` — a documentation line: a typed, anchored `Index.Line` carried on the block
- `--supp <text> ^anchor` — the block's own touched lines, anchored
- `--cont <text>` — continues the previous flag generically; orphaned (no previous flag) it is a finding
- `--to <locator>` — reserved; parsed and preserved, no behavior yet
- a flag-less block is a **content span** (a tagged literal): plain body, no binding — its `^label`/`#address` only makes the span addressable

## Closure is by role

A block owns an `end` by its role, in three cases:

- a **materializing** block (`--derived`/`--copy`) owns a mandatory `> $kw. end` — its body is the generated target and there is no other way to bound it
- a **router** block (one that acquires `--when`/`--then` children) owns a `> $kw. end`; its rows **peer-close** at the next row or the parent's end
- a **declaration-only** block — one carrying dependency roles, `--note`/`--supp`, `--unlock-surface`, or the file-level `--context-assembly` marker — **self-closes** at its declaration and owns no `end`; following native text stays surface
- a bare `> $kw. end` closes the innermost open content block; a legacy `end-<command>`/`end-^label` closer is a finding directing to migration; a heading closes nothing — a content block still open at a heading or EOF is a finding
- the parser is a `Closure.Parser`: below its `Parse.Floor` (well-formed machinery, explicit closure of content blocks, unique addresses, sane router rows) it emits parse errors; above the floor everything it does not recognize is opaque text, and nothing else can fail the parse

## Router — composition by nesting

A `Semantic.Router` is a block whose children are nameless `--when`/`--then` **rows**, each carrying a native-text body (the situation / the response). Rows alternate; a row out of order or a `--when` with no `--then` is a finding. One `> $kw. end` closes the router; the rows peer-close:

```md
## Router Table

> $kw: ^search-router

> $kw: --when
When the caller wants to find concepts or retrieve cited index context.

Includes the read-only pass that precedes any edit proposal.

> $kw: --then
Load `references/search.md`.

> $kw. end
```

## Context Assemblies

A `Context.Assembly.Module` is deliberately file-grain and large enough to hold all builder context for its declared scope:

```md
> $kw: --context-assembly
> --from Concept.One
> --from references/policy.md#Rules

# Complete Context

The complete multi-section context module continues as normal markdown.
```

- the marker must be the first line and carries no address; the `.skw.md` path is the module identity
- the marker's `--from` values are the assembly-covered sources inside its direct package-local context boundary
- any dependency role that targets an assembly-covered source should carry a companion `--dev-from <assembly.skw.md>`; otherwise `check` raises the suppressible `context-assembly-bypass` POI
- v1 coverage is direct and package-local; transitive and cross-package coverage supervision are not inferred
- the assembly declaration is stripped at compile like all Skillware machinery, while the complete module body becomes the runnable context surface

## Locators

A dependency-role (or address) value is one of:

- **`path#Region`** — a heading-section body in a file, resolved against the src root first, then the skill root. The region is the section's body: heading excluded, subsections included. A `.skw.md` target is recursively expanded before extraction (innermost first); expansion cycles are an error naming the chain. A plain (non-skw) file yields the raw region body.
- **`path^label`** — a labeled span in a src file; **`^label`** alone is file-local (the current src). Labels are heading-independent, so the import survives section renames, and the dependency hash covers only the span — a consumer drifts with its fragment, not the file. Labels live only in src machinery (stripped at compile), so they address src files exclusively; renaming a label breaks importers, which the unresolvable-`--from` POI catches.
- **`Dotted.Name`** — an index block resolved in the configured depots (`skw.json`); the value is the block's kernel-line body.
- **`@<id>/path`** — a cross-package address: `<id>` names a `Skw.Pkg.Dependency` in `skw.json` `deps`, resolving to another package; the tail (`path#Region` or `path^label`) then resolves inside that package's own src exactly as a local locator would. This is the only way a `--from` leaves its own package — a raw relative path escaping the package (e.g. `../other/...`) is rejected, not resolved.

## Compilation

- deterministic — no agent in the loop: strip every block's machinery (open fence, belonging flag lines, owned ends), keep the bodies and all hand prose; blank-line runs collapse; output is trimmed
- `--copy` bodies are refreshed in src before targets are emitted; `--derived` bodies pass through as materialized
- `--dev-from` and `--cite` targets resolve through the same locator machinery; on derived recipes their hashes participate in stale detection
- the compiled target never carries Skillware syntax — zero machinery lands on the runnable surface

## Settings

```json
{
  "depots": ["../agentos-pkg"],
  "deps": {"agentos-pkg": "../agentos-pkg"},
  "unlock_registries": ["../context-provider/.skw/unlock-tokens.json"]
}
```

- `depots` — index depots for `Dotted.Name` resolution, relative to the skill root; list order is search order
- `deps` — the `Skw.Pkg.Dependency` registry: an `id → package-root` map (relative to the skill root) whose entries resolve both `@<id>/…` file addresses and `Dotted.Name`s in that package's depot
- `unlock_registries` — explicit context-provider registries used to gate blessing; no directory scanning or implicit global registry

Each provider owns `.skw/unlock-tokens.json`. Schema v1 is strict: every entry contains only one opaque token, one addressed src surface, and the POI kinds it unlocks:

```json
{
  "schema_version": 1,
  "tokens": [
    {
      "token": "skw-unlock:9f4c2a7d8e31",
      "surface": "references/check.skw.md^bless-context",
      "unlocks": ["derived-stale"]
    }
  ]
}
```

The token appears only in the registry. The represented source points back to that registry:

```md
> $kw: ^bless-context --unlock-surface
> --from .skw/unlock-tokens.json
```
