# Tarav2 Index Model Alignment - impl-req

## Impl.Abstract

- **Status:** Implemented and verified. Linter clean on the migrated depot; 91 tests green; `ruff` clean.
- **Scope:** Align the tarav2 implementation with the stated index model: scope as one `Skw.Address.Schema` address covering both `Kernel.Block` and `Skw.Annotation` attachment points, complete `Index.Line.Record`s for lines on any surface, one unified store, the agent/user index split as the appendix/agendix analogue, and a user-tier index alongside the project one.
- **Source alignment:** The user restated the model directly. Minimally the index is *lines supported by a support set* — annotation plus evidence of `Touched.Authority`. `Line.Type` declares what to extract; lines are grouped under a scope that may be a `Kernel.Block` **or another annotation attachment point**; the agent/user split governs *what enters the index*; and an `Index.Line` is more than a line — it is the object describing the index entry.
- **Targets:** `tarav2/tarav2-py/src/tarav2/`, its tests, and the seeded `tarav2-pkg` depot.
- **Out of scope:** Making `Touched.Data` shippable with a project. Grounding data belongs to the user; the index carries line content and support *refs* only, and links breaking on a shipped surface is accepted for now. No chatlas-to-project-surface migration.
- **Acceptance:** A line can be recorded and linted identically whether it lives in a chapter block or on a skw annotation; records are complete; one store; agent and user indexes are separate with a one-directional promotion path; the linter is clean on the migrated depot.

## Impl.Index

### Index.Line.Record

- [DF] an `Index.Line` is more than a line: it is the object describing the index entry, carrying both the line content and the description of how it indexes the `Touch.Authority.Surface`.
- [CT] the record must be complete — it contains everything about the line, and is not shrunk by deriving fields from any one surface.
- [DC] the record splits into the assertion (`line.type`, `line.body`, `scope`) and the indexing (`anchor`, `support`, `occurrences`).
- [CT] maintaining both a surface and a record is acceptable work, and the redundancy is itself an assertion: an agent that does not know the system writes only one, an expert writes both.
- [RJ] deriving `line_type`, `body`, and `scope` from a surface is rejected; the data is distributed across surfaces, so no surface is privileged enough to derive from.
- [DC] the simplest correct shape is one JSON file per line record in a folder.

### Index.Scope

- [DF] a line's scope is one address in `Skw.Address.Schema`, not a depot/chapter/concept triple.
- [DC] a `Block.Path` addresses a `Kernel.Block`; a `Locator.Name` addresses a `Skw.Annotation` attachment point.
- [CT] index lines attach to any skw annotation through the same mechanism as the markdown index.
- [PR] name syntax does not change the named entity's semantics, so one resolver serves both address kinds.

### Index.Store

- [DC] record and anchory are redundant and unify into one store; the record carries its own anchor.
- [RJ] a second identity plus an anchor→id lookup table is rejected; it existed only because two stores held the same fact.
- [DC] the record keeps a stable `id` distinct from its anchor so identity survives an anchor change.

### Index.Review.Split

- [DF] the agent/user split governs what enters the index: the user index holds entries the user reviewed; the agent index is maintained end to end by the agent.
- [CT] agent-index entries are still grounded on `User.Turn`s; unreviewed does not mean ungrounded.
- [DC] the split is the appendix/agendix analogue from the prior model, so `Reviewed.Cite.Closure` carries over: the user index may not depend on the agent index.
- [DC] promotion is one-directional — agent index, then review, then user index.

### Index.Geography

- [DF] the project/user axis is geographic: where the data physically sits.
- [DC] every project has a project index; a user may additionally register a user index that is a full index held outside the project folder.
- [CT] the split separates what ships with the project from what stays local to the user machine.

### Grounding.Boundary

- [CT] grounding data such as the `Chat.Surface` belongs to the user, so the index must not leak it.
- [DC] the index carries line content and refs to support sets, nothing more.
- [FR] a shipped surface whose support cannot resolve is accepted for now; making `Touched.Data` shippable is explicitly deferred.

## Impl.Log

- Index.Presumption: the user tier is placed at `~/.tarav2/` rather than `~/.tarav/`, matching the tarav2 home already resolved by `config.py`. The instruction said `~/.tarav`; keeping tarav2 state out of tarav1's home avoids two systems writing one directory.
- Index.Presumption: the agent/user split is realized as two record folders (`agent/`, `user/`) rather than a field, matching the physical `homes/` split and keeping the guard a path check.
- Index.Presumption: anchor→record resolution scans the record folder. At index volumes (human-paced, low volume by the model's own premise) this is cheaper than maintaining a second store; if it ever matters, a derived cache can be added without touching the model.

## Execution.Plan

### Slice 1 — Scope as an address
Replace `BlockScope` with `Scope` over `Skw.Address.Schema`: `Block.Path` and `Locator.Name` kinds, parse/render/resolve-to-surface.
**Check:** RED-then-GREEN — both address kinds parse, render round-trip, and resolve to a surface path.

### Slice 2 — Unified store, complete records
Fold anchory into the record store. Record shape: `id`, `scope`, `line{type,body}`, `indexing{anchor,support,occurrences}`, `tail`, `label`. Anchor allocation and anchor→record lookup move into the store.
**Check:** allocation is monotonic per day; anchor resolves to its record; records round-trip.

### Slice 3 — Agent/user index split
Two record roots (`agent/`, `user/`), promotion `agent → user`, and the `Reviewed.Cite.Closure` check.
**Check:** promotion moves an entry; a user entry supported only by an agent entry is a POI.

### Slice 4 — User-tier index
Project index plus an optional user index under the user tier, both readable as one logical index.
**Check:** a line registered in the user tier is found by search and lint, and is absent from the project folder.

### Slice 5 — Skw attachment points end to end
Records for skw-hosted lines; `index write` takes a scope address.
**Check:** a line on a skw annotation gets a record and passes the same checks as a chapter line.

### Slice 6 — Linter over the aligned model
Update the catalog for the new scope, store, and split; drop checks that no longer have a referent.
**Check:** `--list-checks` reflects the model; the migrated depot is clean.

### Slice 7 — Migrate and clean
Migrate the 21 seeded records; delete `.tarav2/anchors/`, `.tarav2/chat-index/`, `~/.tarav2/archive/`.
**Check:** linter clean; no orphan directories.

## Slice Status

| # | Slice | Status | Check |
|---|---|---|---|
| 1 | Scope as an address | done | both kinds parse, round-trip, resolve; 14 tests |
| 2 | Unified store, complete records | done | anchory folded in; mint, resolve, round-trip; 21 tests |
| 3 | Agent/user index split | done | two roots, one-directional promote, `Reviewed.Cite.Closure` |
| 4 | User-tier index | done | user-tier entry absent from the project folder, visible to reads |
| 5 | Skw attachment points end to end | done | annotation-scoped entry written and linted like a chapter line |
| 6 | Linter over the aligned model | done | 18 checks incl. `scope-resolves`, `scope-kind`, `review-closure` |
| 7 | Migrate and clean | done | 21 entries migrated; `record/`, `anchory/`, `anchors/`, `chat-index/`, `~/.tarav2/archive/` removed |

## Verification

```text
tarav2 index write --scope "@src/tarav2/scope.py/parse_scope" --type DF --body "…"
   → ln_0181…  ^d20260818-0u  @src/tarav2/scope.py/parse_scope  [agent]
tarav2 index write --scope "tarav2-pkg/design#Index.Geography" --review user --tier user
   → landed in ~/.tarav2/index/user/, absent from the project folder
tarav2 index record            both tiers visible as one logical index
tarav2 index promote <id>      agent → user, no duplicate left behind
tarav2 index linter            clean — 21 record(s), 21 surface line(s), 18 check(s)
pytest                         91 passed
ruff check src/ tests/         All checks passed
```

## What Changed From The Prior Build

- `BlockScope{depot, chapter, concept}` → `Scope` over `Skw.Address.Schema`, so a
  `Kernel.Block` and a `Skw.Annotation` attachment point are the same field with the same
  resolver.
- Record and anchory unified into one `IndexStore`. Anchor allocation is a directory scan;
  anchor→entry is a lookup over the same files. `AnchorDepot`, the `ln_↔anchor` table, and
  the `Anchor.Unregistered` check are gone.
- Record shape is now explicitly two halves — `line{type,body}` + `scope` as the assertion,
  `indexing{anchor,support,occurrences}` as how it indexes the authority surface — and it is
  complete rather than partly derived.
- Store roots are `<tier>/index/{agent,user}/`, realizing both the review split and the
  geographic axis in the same layout.
- Dead fields removed: `statement_hash` on the anchor record, `occurrences[].hash`, and the
  `Chat.Index` writer and its leftovers.
