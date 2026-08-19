# Tarav2 Hugentic Bootstrap - impl-req

## Impl.Abstract

- **Status:** Implemented and verified. `Bootstrap.Closure.Test` passes; index linter clean; 79 tests green; `ruff` clean.
- **Scope:** Build `tarav2` as a self-hosting Hugentic system: a git-backed authority archive, the `Touched.Index.Record` coordination model, anchor mint/resolve, two materialization surfaces, and the three routes (`--capture`, `--edit`, `--search`) needed to run its own index. Delivered as `tarav2-py` (library + `tarav2` CLI) and `tarav2-md` (driver skill + `tarav2-pkg` depot).
- **Source alignment:** The redesign is motivated by a changed semantic model, not by code rot. Tarav1 predates `Touched.Index.Record`, `Line.History`, manifest-gated authority, and the project/user scope axis. Chatlas ports nearly clean; the index layer mostly does not.
- **Root:** `~/projects/taravangian-project/tarav2` as the root folder for all tarav2 subsystems.
- **Out of scope:** Parity with tarav1's full routing table (impl design/review/execute/develop/harvest, issues, parking notes, session router, codebase cleaner, testground, status modules). Those keep working in tarav1. Also out: `Chat.Index.Delta` chronological receipts, multi-user merge, journals, Obsidian client, the approval gate, export, and the `Index.Ontology` graph.
- **Acceptance (`Bootstrap.Closure.Test`):** `tarav2` captures a real session into `tarav2-pkg`, lines land with anchors, `tarav2 search` resolves them back to the exact supporting user turns, and no step routes through tarav1.

## Impl.Index

### Scope.Axis

- [DF] `Project.Scope` is data belonging to the project's shared understanding; `User.Scope` is data belonging to the user across all their projects.
- [CT] the axis is not public/private: `homes/ceo/chapters/` is personal and project-scoped, while a journal is user-authored and user-scoped.
- [CT] a fresh clone with no `~/.tarav2` must use the project and read its index; grounding degrades, nothing else does.
- [DC] project tier lives at `<project>/.tarav2/`; user tier lives at `~/.tarav2/`.

### Touch.Authority

- [DF] `Touch.Authority.Manifest` declares that a surface is of a given type and carries `Touch.Authority`.
- [CT] git-backing is a qualification criterion: a surface that cannot be git-backed cannot carry `Touch.Authority`.
- [DC] every qualification predicate therefore has one shape — which commits on this repo/path qualify.
- [DF] `Edition.Relation::Commit.Is.Edition` means the user authored the commit and the git author attributes touch; `Edition.Relation::Commit.Records.Edition` means capture committed on the user's behalf and the git author is meaningless for attribution.
- [CT] chat is `Commit.Records.Edition`; file surfaces such as journal and vault are `Commit.Is.Edition`.
- [CT] an agent write into `homes/<user>/` is a violation detectable by path alone, without reading line semantics.

### Index.WIP.Surface

- [CT] the Index is a `WIP.Surface` and anything in it may be changed.
- [CT] drift is a signal to work rather than a violation, so reconciliation yields a work queue and never a verdict.
- [CT] index content carries assertions, and the minimum bar for a retained line is that it is typed and User.Touched grounded.
- [DC] reconciliation is neutral about which side of a divergence stands; a surface edit is as legitimate as a record edit.
- [DC] a line authored directly on a surface is adopted into the record rather than rejected as an orphan.

### Touched.Index.Record

- [DF] `Touched.Index.Record` is the coordination layer: line identity, support, history membership, HEAD selection, and surface occurrences.
- [CT] the record is a model, not a file format; a canonical JSON schema defines its shape while storage remains free.
- [RJ] the record is not the owner of surface content and does not make surfaces into rebuildable projections of itself.
- [CT] addressing belongs to the model, not to storage, so file count and backing store stay unconstrained.
- [CT] hashes are computed over the canonical model form, never over bytes on disk, so storage reorganization cannot manufacture drift.
- [DC] any backing store must cheaply answer four questions: which line is this, what supports it, what is its history, where is it materialized.
- [DF] `Line.History` is `HEAD.Line` (current valid expression) plus `Tail.Lines` (earlier valid expressions); the distinction is current-vs-earlier validity, never correct-vs-incorrect.
- [DC] index entities are identity-addressed (`id`/`hash`/`label`) because the Index is a `WIP.Surface`; authority surfaces are content-addressed through git because they are immutable.
- [DC] an incorrectly extracted line is removed rather than demoted; git preserves the mistake outside the semantic model.

### Support.Resolution

- [CT] unresolvable support has three distinguishable states: `archive_absent` is benign, `missing` is real debt, and `mismatch` is a POI.
- [DC] a `Support.Reference` records which archive it needs, so a miss reports the required archive rather than failing opaquely.
- [CT] `Kernel.Writing` is load-bearing rather than stylistic: the index must condition judgment standalone because the archive is user-scoped and normally absent for any reader but its author.

### Depot.Boundary

- [CT] `tarav2-pkg` holds only what is new or changed in tarav2 and never restates `tarav-pkg`'s model.
- [DC] where tarav2 changes an existing concept, the line lives in `tarav2-pkg` and names the `tarav-pkg` concept it revises.
- [RJ] encoding the storage format in a package name is rejected; the package is `tarav2-pkg`, not `tarav2-v1-pkg`.

### Tarav1.Alignment

- [PR] a difference from tarav1 must be traceable to a named model change, or to an integration that genuinely does not fit; everything else is reuse.
- [DC] tarav2 depends on `tarav` and reuses Chatlas2 normalization, its git-backed archive, Anchory, the index parser, canonical statement hashing, and skw.
- [CT] agents edit index surfaces with ordinary file primitives; there is no landing API, capture pipeline, or adopt command.
- [DC] conformance lives in one linter with a check catalog, tiers, and `--check`/`--skip`/`--list-checks` selectors, so growing the system means adding a check rather than a command.
- [DC] `bless` accepts one exact POI by stable id, so silencing a known case never weakens the check for other lines.
- [CT] skw is integrated into the new index mechanics while its design and command surface stay unchanged: its `--note`/`--supp` lines are read as index lines by the same catalog.
- [DF] index surfaces use tarav1's separator-anchored `Kernel.Block` format; a `## Concept` heading without its `****` separator parses as prose.

### Minimality

- [CT] `Chat.Index.Delta` is dropped from the MVP because the record already knows support sets and surface occurrences, which is what Deltas approximated with files.
- [PR] where ported code and the new model conflict, the model wins and the code is dropped rather than adapted.
- [DF] `Bootstrap.Closure.Test` is the MVP completion criterion: tarav2 captures, anchors, and resolves its own index without tarav1.

## Impl.Log

- [PR] the target root is not a git repository, so the mandatory execution git checkpoint cannot be created; `tarav2/` is a new empty tree with no prior state at risk, so execution proceeds and initializes tarav2's own archive repositories instead.
- Index.Presumption: the record's concrete field set (`LineRecord`/`LineEdition`/`SupportRef`/`SurfaceOccurrence`) is `Open.Inference` derived from the settled model above; it was not separately user-reviewed field by field.
- Index.Presumption: the minimal Claude/Codex normalizers extract user/assistant messages with stable coordinates rather than porting tarav1's full event-tape fidelity; whole-turn drift digests are deferred.
- Index.Presumption: `message_id` derives from `(session_id, ordinal, role, text)`. Appending to a live session preserves every earlier id — verified across a re-ingest that grew 80→85 messages with support still resolving — but *removing* or re-filtering an earlier message would shift ordinals and break ids. A purely content-plus-position-independent coordinate was not adopted because duplicate message text is common.
- Deviation (resolved): `tarav2 capture` failed on first run because `ops/__init__.py` re-exports `capture` as a function, shadowing the submodule for `from .ops import capture`. Fixed by importing concrete names in `cli.py`.
- Deviation (resolved): `reconcile` resolved `chat:<session>` occurrences as project-relative paths, reporting all 19 landed chat materializations as `Surface.Absent`. Found by running the reconciler against the live depot. Fixed with `resolve_surface_path`, which addresses the two surface kinds distinctly; regression tests added.
- The `Chat.Index.Delta` cut is confirmed in practice: `Chat.Index.HEAD` upserts by anchor, and no `deltas/` directory is produced or needed.
- **Design correction (user, post-implementation):** the first build encoded record-as-owner with surfaces as rebuildable projections. Corrected to the settled 629 model — the Index is a `WIP.Surface`, drift is a signal to work, and the bar is typed + User.Touched grounded. Four concrete gaps followed and were closed: `reconcile` never read surfaces (so hand-authored lines were invisible); `Surface.Drift` was worded as though the record were right; there was no adopt path; the bar was expressed nowhere. Added `ops/adopt.py` (`adopt`, `ground`), rewrote `reconcile` as a neutral work queue that scans surfaces independently, and replaced the POI vocabulary with `WorkClass`/`WorkItem`.

## Execution.Plan

### Slice 1 — Root scaffold and scope resolution
Create `tarav2/`, `tarav2/AGENTS.md`, `tarav2-py` package skeleton with `pyproject.toml` (`tarav2` script), and `config.py` resolving the project tier (`<project>/.tarav2/`) and user tier (`~/.tarav2/`).
**Check:** `tarav2 --help` runs; `tarav2 config show` prints both tiers.

### Slice 2 — Touch.Authority manifests and path guard
`authority/manifest.py` (model, registry, git-backing criterion, edition relation, attribution) and `authority/guard.py` (agent-write path guard over `homes/<user>/`).
**Check:** RED-then-GREEN test — registering a non-git-backed surface is refused; an agent write into `homes/ceo/` is refused.

### Slice 3 — Chatlas archive
`chatlas/` — minimal Claude and Codex normalizers producing stable message coordinates, a git-backed archive writer, and a query surface.
**Check:** normalize a real session; messages queryable by session and id; archive commit exists.

### Slice 4 — Touched.Index.Record
`record/` — `model.py`, `identity.py` (canonical-form hashing), `store.py` (JSONL-backed, interface-neutral), `reconcile.py` (drift → POIs).
**Check:** RED-then-GREEN — the four questions answerable; storage reorganization does not change a hash.

### Slice 5 — Anchors
`anchors/` — mint, register, resolve; joins a record line to its support.
**Check:** mint an anchor, resolve it back to exact chat messages, detect a triplet mismatch.

### Slice 6 — Surfaces
`surfaces/` — kernel line parser, `project_index.py` (homes layout), `chat_index.py` (HEAD only).
**Check:** parse a chapter file into typed lines; materialize and re-read a HEAD.

### Slice 7 — Ops and CLI
`ops/` — capture, edit, search; wired into the `tarav2` CLI.
**Check:** each command runs end to end against the seeded depot.

### Slice 8 — Skills and depot seed
`tarav2-md/skills/tarav2-hugentics/` driver skill and `tarav2-md/skills/tarav2-pkg/` depot with `homes/{ceo,agent}`.
**Check:** depot registers; router resolves a concept to its chapter file.

### Slice 9 — Bootstrap closure
Run the `Bootstrap.Closure.Test` end to end and record the result.
**Check:** capture → anchors → search resolves to exact user turns, entirely under tarav2.

## Slice Status

| # | Slice | Status | Check |
|---|---|---|---|
| 1 | Root scaffold and scope resolution | done | `tarav2 config` / `init` print both tiers |
| 2 | Touch.Authority manifests and path guard | done | 12 tests: non-git-backed refused, agent write into `homes/ceo/` refused |
| 3 | Chatlas archive | done | real session normalized: 85 messages, 26 touched, git commit |
| 4 | Touched.Index.Record | done | 24 tests: four questions, canonical hashing, HEAD/Tail, reconcile |
| 5 | Anchors | done | 11 tests: idempotent mint, batch, triplet drift detection |
| 6 | Surfaces | done | 14 tests: parser, homes asymmetry, guard, HEAD upsert, no deltas |
| 7 | Ops and CLI | done | 17 tests + 11 CLI subcommands |
| 8 | Skills and depot seed | done | `tarav2-hugentics` + 4 references; `tarav2-pkg` router |
| 9 | Bootstrap closure | **passed** | 19 grounded lines captured, resolved to exact turns, reconcile clean |
| 10 | WIP-surface correction | done | surface scan, neutral reporting, the bar made explicit |
| 11 | Tarav1 alignment cut | done | ops/ deleted, tarav1 reused, 16-check linter, 5 CLI groups; 79 tests |

## Verification

```text
tarav2 ingest 9f41aa0e-…      claude: 85 messages, 26 touched, commit 5183c1fe
tarav2 capture --depot tarav2-pkg   19 lines landed, ^c20260818-0u … -18u
tarav2 search "scope" -v      4 lines, all grounded, each resolved to its user turn
tarav2 resolve ^c20260818-6u  triplet MATCHED, support resolved
tarav2 reconcile              clean — 19 record(s) checked
pytest                        85 passed
ruff check src/ tests/        All checks passed
```

After the WIP-surface correction, the reverse direction was verified live — two lines written
by hand straight into a chapter, then brought to the bar:

```text
(hand edit of homes/agent/chapters/100-design.md)
tarav2 reconcile   Work/Surface.Unanchored (2) — 19 record(s), 21 surface line(s)
tarav2 adopt       adopted 2, anchors written back, "2 need grounding"
tarav2 ground      grounded on m15c838a9462ef383 (the correcting user turn)
tarav2 reconcile   no work outstanding — 21 record(s), 21 surface line(s)
tarav2 resolve ^d20260818-20u   triplet MATCHED, resolved to that exact turn
pytest             99 passed
```

The closure condition held: capture, anchoring, and resolution all ran under `tarav2`, with
tarav1 used only to author the code.

## The Tarav1 Alignment Cut

The first build over-changed. Four rewrites were not traceable to any model change and were
replaced by reuse of `tarav`:

| Rewritten | Replaced by |
|---|---|
| thin chatlas normalizer (~390 LOC) | `tarav.chatlas2` — normalization, providers, git-backed archive, and `message_address`, which also removed the ordinal-dependent coordinate flaw |
| bespoke anchor system (253 LOC) | `tarav.anchory` — atomic allocation, namespaces, tags, amend, scan |
| kernel parser (150 LOC) | `tarav.index.model.parser` — typed nodes and inline spans |
| `record/identity.py` hashing | `tarav.index.model.identity` — canonical statement/triplet hashing |

Deleted outright as overtooling: `ops/capture.py`, `ops/edit.py`, `ops/adopt.py`, and the
bespoke half of the CLI. Agents edit surfaces; the linter checks them.

`reconcile` became `tarav2 index linter`: 16 checks, two tiers, selectors, and `bless`.
The CLI went from 13 flat subcommands to 5 groups. Source dropped from ~3,900 to 2,530 LOC
while the check catalog grew.

Findings the cut produced, all of them conformance to existing tarav1 behavior rather than
workarounds:

- index blocks are **separator-anchored**; the seeded chapter omitted `****`, so every kernel
  line had been parsing as prose and the linter reported `0 surface lines`;
- Anchory refuses allocation until a namespace declares its single-letter prefix in
  `meta.json` — that prefix *is* the `d` sigil, composed with the date;
- `scan_anchory_source` takes an explicit regex;
- Anchory's `resolve` is total, returning `None` rather than raising on junk.

Swapping to Chatlas2 addressing invalidated the seeded records' support ids and anchors. The
linter surfaced both (23 `Support.Mismatch`, 21 `Anchor.Unregistered`); all 21 records were
re-grounded onto real addresses and their anchors registered, and the run is clean.

## Deferred

Journals, Obsidian client, the manifest approval gate, archive export, multi-user merge,
`Index.Ontology`, appendix/agendix depth, and the assertion-bond scoring loop that would
feed `What.Do.You.Want`.
