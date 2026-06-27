# agentos-index router write integration - impl-req

## Impl.Abstract

- **scope:** refactor `agentos-index` into the single public `Workflow.Neutral.Skill` for the Agentos Index subsystem, with explicit `Batchy.Skill` args for `--search` and `--write`
- **scope:** integrate the current `agentos-index-writer` content into `agentos-index` `Skill.Module`s and remove `agentos-index-writer` as a standalone public skill
- **scope:** align stable index-surface references so `agentos-index` is the canonical entry surface for index work and the search/load model is routing-first selective loading
- **out of scope:** integrating later modules such as `--ground`, `--diagnose`, or `--test`
- **out of scope:** broad cleanup of every index-adjacent appendix or reference file beyond the search/write merge and directly affected stable callers
- **status:** completed
- **source:** 2026-06-27 chat design on `agentos-index` as a `Batchy.Skill` router with `--search` and `--write`; current stable surfaces inspected in `agentos-md/skills/agentos-index/SKILL.md`, `agentos-md/skills/agentos-index-writer/SKILL.md`, `agentos-md/skills/agentos-batchy-skills/SKILL.md`, `agentos-md/skills/agentos-pkg/index/101-index.md`, `agentos-md/skills/agentos-pkg/index/107-index.md`, `agentos-md/skills/agentos-pkg/references/launch-runtime.md`

## Impl.Index

### Agentos.Index.Public.Entry

- `agentos-index` must be the single public `Package.Aux.Skill` for the Agentos Index subsystem
- `agentos-index-writer` must stop existing as a parallel public entry surface
- public callers and context hooks should point to `agentos-index` for both search and write work
- `No.Legacy.Allowed` applies to the public skill model here: once `agentos-index` absorbs the write role, the old writer skill should be removed rather than preserved as a compatibility surface

### Agentos.Index.Batchy.Router

- `agentos-index` should remain a `Workflow.Neutral.Skill`
- the root `SKILL.md` should act as the router and driver for the index subsystem
- `--search` and `--write` should be the first explicit `Skill.Arg`s
- each arg should activate a named `Skill.Module`
- the root skill should orient and route when no explicit arg is selected, not force an operation

### Agentos.Index.Module.Layout

- `agentos-index` should keep `SKILL.md` lean and push operational depth into on-demand `Skill.Module`s
- the first modules should be `search` and `write`
- the preferred first implementation is reference-backed modules under `agentos-md/skills/agentos-index/references/`
- the root skill should expose a small router table mapping the public index tasks to the corresponding modules

### Agentos.Index.Search.Model

- the canonical search/load model is routing-first selective loading
- the older full-index preload model in `agentos-pkg/references/launch-runtime.md` is stale
- the `search` module should define router-first lookup, selective block loading, appendix discovery/loading rules, citation behavior, and unresolved-name handling
- after the refactor, stable surfaces should treat `agentos-index` as the canonical entry place for working with the index system

### Agentos.Index.Write.Model

- the write guidance currently in `agentos-index-writer` should move into the `write` module of `agentos-index`
- the `write` module should carry the durable operating guidance needed for approved index and appendix edits: write gates, naming, placement, write loop, and post-write maintenance
- quality-calibration depth such as `agentos-pkg/references/index-block-catalog.md` should stay as reference depth rather than being copied into the root skill
- stable surfaces that currently name `agentos-index-writer` should be updated to name `agentos-index`

## Execution.Plan

### Slice 1 — Turn `agentos-index` into the public Batchy router

- add a small `Skill.Arg.Section` to `agentos-md/skills/agentos-index/SKILL.md`
- define `Skill.Arg:Search` and `Skill.Arg:Write`
- rewrite the root skill so it is clearly the neutral router/driver for the index subsystem rather than a thin orientation note plus redirect
- make `-h` / `--help` render the new public args through the `Skill.Arg.Section` as a normal `Batchy.Skill.Help` surface
- path: `agentos-index/SKILL.md` frontmatter + root body
- observable: the root skill presents `--search` and `--write` as the canonical public entrypoints
- check: read `agentos-index/SKILL.md` alone and confirm writing no longer routes to `agentos-index-writer`, and `-h` / `--help` is specified in terms that expose `--search` and `--write`
- status: completed

### Slice 2 — Create the `search` and `write` modules

- create `Skill.Module` surfaces for `search` and `write`
- use reference-file modules for the first pass, e.g. `agentos-md/skills/agentos-index/references/search.md` and `agentos-md/skills/agentos-index/references/write.md`
- move routing-first lookup, citation behavior, and appendix-loading rules into the `search` module
- move the writer essentials from `agentos-index-writer` into the `write` module
- path: `agentos-index/SKILL.md` router + new `references/search.md` + new `references/write.md`
- observable: the root skill stays short while both operations are fully reachable through explicit Batchy args
- check: each module can be read independently and covers its operation without depending on `agentos-index-writer`
- status: completed

### Slice 3 — Remove `agentos-index-writer` and patch stable callers

- delete `agentos-md/skills/agentos-index-writer/SKILL.md` after its content is integrated
- patch stable surfaces that still present `agentos-index-writer` as current, especially `agentos-md/skills/agentos-index/SKILL.md` and `agentos-md/skills/agentos-batchy-skills/SKILL.md`
- patch the stable index blocks in `agentos-md/skills/agentos-pkg/index/104-index.md` that still name `agentos-index-writer` as operational detail for `Write.Trigger.Gated` and `Content.Verbatim.Gated`
- path: index skill surfaces, directly affected stable callers, and directly affected stable index blocks
- observable: stable package docs present `agentos-index` as the single public route for index writing
- check: `rg "agentos-index-writer" agentos-md/skills` returns no hits outside deprecated or historical surfaces
- status: completed

### Slice 4 — Align the canonical load model

- update or replace `agentos-md/skills/agentos-pkg/references/launch-runtime.md` so it matches the new `agentos-index --search` model
- remove the old “load the full index first” runtime as stable guidance
- path: `agentos-pkg` stable references that define index runtime/loading behavior
- observable: no stable reference contradicts routing-first selective loading
- check: read `agentos-index/SKILL.md` and `launch-runtime.md` together and confirm they describe one coherent search/load model
- status: completed

## Impl.Log

- 2026-06-27: Created from accepted chat design to make `agentos-index` the single public Batchy router skill for the index subsystem and absorb `agentos-index-writer` into explicit modules.
- 2026-06-27: Executed inside the `agentos-md` git repo because the umbrella `agentos-project` root is not itself a git repository; all touched implementation surfaces for this request lived under `agentos-md`.
- 2026-06-27: Replaced `agentos-index` root skill with a Batchy router shape, added `search` and `write` reference-backed modules, deleted `agentos-index-writer`, patched stable callers, and rewrote `agentos-pkg/references/launch-runtime.md` to the routing-first selective load model.
