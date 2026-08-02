# agentos-skillware --about (language spec)

> $kw: --from Context.Loading.Path

The operational spec of the Skillware source language. This module is normative for syntax; the concepts behind it live in `references/doctrine.md`.

## The Src Surface

- `<skill>/.skw/src/` mirrors the skill tree: `src/references/ground.skw.md` compiles to `references/ground.md` (strip `.skw`); `src/SKILL.skw.md` to `SKILL.md`
- no `.skw.md` = the file is hand-owned; Skillware never touches it — adoption is per-file, a skill can be partially managed
- `.skw/skw.json` — package identity and settings: `{"id": "my-skill", "depots": [...], "deps": {...}}`; paths are relative to the skill root
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
- `--context-loading-path` — an addressed, top-of-file declaration of one complete normal runtime loading path for the current target; repeatable `--step` fields name ordered runnable files preceding the implicit target
- `--loading-dep <source-locator>` — addressed runtime content the consuming file fundamentally requires from an earlier step of every declared loading path; repeatable on any annotation and normally carried by `--context-loading-path`
- `--reachable-from <runtime-file>` — a file-point assertion that at least one typed loading path reaches the declaring target from the named local or `@<package>/...` runtime file; repeatable and independently witnessed
- `--unlock-surface` — marks one explicitly addressed context surface represented by one token in the registry named by its single `--from`; takes no value
- `--intent <text>` — the derivation rule's context, free prose; a binding flag's own trailing text folds into it
- `--note [TYPE] <text> ^anchor` — a documentation line: a typed, anchored `Index.Line` carried on the block
- `--supp <text> ^anchor` — the block's own touched lines, anchored
- `--cont <text>` — continues the previous flag generically; orphaned (no previous flag) it is a finding
- `--routing-table` — declares one addressed `Routing.Table`; requires one `--select zero-or-one|one|many`
- `--router-row` — declares one addressed `Batchy.Router.Row`; requires one `--table` owner and one `--match explicit|semantic|explicit-or-semantic`
- `--routing-view calls|modules|full` — emits one deterministic projection of its `--table` into the runnable surface
- `--table <address>` — assigns a row or view to an addressed `Routing.Table`
- `--flag <configuration>` / `--alias <configuration>` — declare a row's canonical explicit configuration and equivalent spellings
- `--match <policy>` — declares whether a row resolves explicitly, semantically, or through either input
- `--default <text>` — declares a lower-authority resolution default for the row, repeatable
- `--to <destination>` — declares a routed destination, repeatable
- `--load <runtime-file>` — declares a typed whole-file loading edge; local paths stay in the package and `@<id>/path` targets a registered package, repeatable and checked during expansion
- a flag-less block is a **content span** (a tagged literal): plain body, no binding — its `^label`/`#address` only makes the span addressable

## Closure is by role

A block closes according to its role:

- a **materializing** block (`--derived`/`--copy`) owns a mandatory `> $kw. end` — its body is the generated target and there is no other way to bound it
- a **declaration-only** block — one carrying dependency roles, `--note`/`--supp`, `--unlock-surface`, a file-level context declaration, or a routing annotation — **self-closes** at its declaration and owns no `end`; following native text stays surface
- a bare `> $kw. end` closes the innermost open content block; a legacy `end-<command>`/`end-^label` closer is a finding directing to migration; a heading closes nothing — a content block still open at a heading or EOF is a finding
- the parser is a `Closure.Parser`: below its `Parse.Floor` (well-formed machinery, explicit closure of content blocks, unique addresses, resolvable table membership, sane router rows) it emits parse errors; above the floor everything it does not recognize is opaque text, and nothing else can fail the parse

## Routing.Table — addressed annotations

A Skillware-managed `Routing.Table` is one addressed `Skw.Annotation`. Every `Batchy.Router.Row` is another addressed annotation that declares table membership explicitly, so the row remains independently referenceable and table structure does not depend on physical nesting.

Rows can expose strict flags and aliases, permit semantic discovery through `--when`, declare defaults, and route to modeled destinations or typed whole-file load targets. A semantic row requires `--when`; an explicit row requires `--flag`; duplicate explicit keys and unresolved local or registered-package loads are findings. `--to` remains the routed effect, `--load` is the graph edge, and `--then` is the operator-readable explanation.

One canonical table may project several runnable views. `calls` shows explicit invocation, `modules` inventories modeled module destinations, and `full` renders the complete addressed row model:

```md
## Router Table

> $kw: ^package-router --routing-table --select many

> $kw: ^search-route --router-row --table ^package-router
> --flag --search
> --alias --research
> --alias --ground
> --match explicit-or-semantic
> --default Index namespace when omitted
> --to Index.Search.Operation.Module
> --load references/search.md
> --when the caller wants to find concepts or retrieve cited index context
> --then load the search module and perform a read-only grounding pass

> $kw: ^public-calls --routing-view calls --table ^package-router
> $kw: ^module-catalog --routing-view modules --table ^package-router
> $kw: ^full-router --routing-view full --table ^package-router
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

## Context Loading Paths

`Context.Loading.Path` declarations model the whole-file context a skill consumer normally accumulates before and through one managed target:

```md
> $kw: ^capture-path --context-loading-path
> --step AGENTS.md
> --step SKILL.md
> --loading-dep SKILL.skw.md^runtime-contract
> --loading-dep SKILL.skw.md^command-contract

# Capture Module
```

- declarations occupy the file point, require an explicit address, and may repeat so alternative paths remain independently projectable
- `--step` values are skill-root-relative runnable files in loading order; the declaring file's compiled target is the implicit final step
- every local path contains `SKILL.md`; existing skill-local `AGENTS.md` files may precede it, while `.skw/AGENTS.md` is builder-only and cannot participate
- steps after `SKILL.md` must be connected by `Routing.Table --load` edges; Skillware reports an unrealized edge rather than inferring one from prose
- every `--loading-dep` must be a local addressed `.skw.md` locator whose compiled provider file occurs earlier on every projected path and actually contains the resolved addressed body
- loading dependencies declare consumer assumptions, not build derivation: they do not replace `--from`, `--dev-from`, or `--cite`
- `--dev-from` and `Context.Assembly.Module` remain builder-context mechanisms and never become runtime loading edges
- `agentos skw context --skill <skill> --target <runnable-file> [--json]` returns each path's ordered steps, edge provenance, satisfied loading dependencies, per-file content, and assembled `Projected.Context`; it never unions alternatives
- `agentos skw context --skill <root-skill>` audits every reachable package's `--reachable-from` assertion and returns one deterministic witness path per assertion
- a package-qualified `--target @<id>/path` projects that target's reachability witnesses, while an unqualified target continues to project its declared local paths
- `--reachable-from` is existential: one graph path must contain the named predecessor; `--loading-dep` remains universal over every declared path reaching its consumer
- workspace prefixes, inline satisfaction modes, and semantic loading dependencies remain deferred beyond the current model

## Locators

A dependency-role (or address) value is one of:

- **`path#Region`** — a heading-section body in a file, resolved against the src root first, then the skill root. The region is the section's body: heading excluded, subsections included. A `.skw.md` target is recursively expanded before extraction (innermost first); expansion cycles are an error naming the chain. A plain (non-skw) file yields the raw region body.
- **`path^label`** — a labeled span or addressed self-closing routing annotation in a src file; **`^label`** alone is file-local (the current src). Span dependencies resolve their native body; routing annotations resolve a canonical nonempty field representation, so changing a row's flags, matching policy, destinations, or loads invalidates its consumers. Labels are heading-independent, so the import survives section renames and a consumer drifts with its addressed fragment rather than the file. Labels live only in src machinery (stripped at compile), so they address src files exclusively; renaming a label breaks importers, which the unresolvable-`--from` POI catches.
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
  "id": "my-skill",
  "depots": ["../agentos-pkg"],
  "deps": {"agentos-pkg": "../agentos-pkg"},
  "unlock_registries": ["../context-provider/.skw/unlock-tokens.json"]
}
```

- `id` — the stable package identity used by runtime graph nodes and checked against every importing registry key
- `depots` — index depots for `Dotted.Name` resolution, relative to the skill root; list order is search order
- `deps` — the `Skw.Pkg.Dependency` registry: an `id → package-root` map (relative to the skill root) whose entries resolve both `@<id>/…` file addresses and `Dotted.Name`s in that package's depot
- `unlock_registries` — explicit context-provider registries used to gate blessing; no directory scanning or implicit global registry

Each provider owns `.skw/unlock-tokens.json`. Schema v1 is strict: every entry contains only one opaque `Poi.Unlock.Token`, one addressed src surface, and the POI kinds it unlocks:

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

> $kw: --from Batchy.Router.Row --from Closure.Parser --from Index.Line --from Routing.Table --from Skw.Address.Schema --from Skw.Annotation --from Skw.Ann.Dependency --from Skw.Pkg.Dependency --from Poi.Unlock.Token
