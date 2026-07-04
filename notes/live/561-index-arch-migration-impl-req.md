# Index Architecture Migration — Impl.Req

## Impl.Abstract

- **Goal**: migrate the Agentos index **structure** to the generalized layout converged in `notes/live/540-index-architecture-redesign-design-session.md` — chapters + `000-INDEX.md` router + appendix.
- **Split**: this is the **arch migration only**. It moves and renames files/folders and fixes path references. It does **not** change block content, concept names, or wording. The content upgrade (redesigned blocks, `write`→`edit`, `Conceptual.Space`→`Design.Space`, new concepts) is a **separate later `Impl.Req`**, governed by `Natural.Placement`.
- **Operating contract** (`540` Session.Notes): *structure-free / content-gated*. Every step here is structural — no `Content.Verbatim.Gated` block edits. If a step would change wording, it is out of scope.
- **Order**: chatlas is the **pilot** (small, already half-reshaped), then `agentos-pkg`.
- **Source**: `540` (grounding session `99144906-781e-43cc-9d27-b40f166e2acf`).
- **Status**: S0 resolved — proceeding. Decision: the `agentos index linter` encodes the *old* index model and **is not used for validation during this migration**; the linter/tooling update to the new model is a **separate later effort**. Migration validation is agent-convention (routing + appendix resolve by reading), not the linter.

## Impl.Index

### Migration.Target.Layout
- the target is the layout in `540` `Agentos.Index.System/Index.Surface.Layout`, already realized in chatlas as the reference:
  - `<pkg>/000-INDEX.md` — concept→file lookup, sectioned by chapter
  - `<pkg>/design/NNN-design.md` — default chapter (flat, numbered)
  - `<pkg>/appendix/Concept.Name-appendix.md` — shared depth
- reference implementation to copy: `agentos-chatlas-md/skills/agentos-chatlas-pkg/` (has `design/`, `appendix/`, currently `ROUTER.md`).

### Router.Rename
- the router filename is **`000-INDEX.md`** (locked in `540`; not `ROUTER.md`). `INDEX` is the name; `000-` is the grep marker for `Index.Discovery`.
- chatlas currently ships `ROUTER.md` → rename to `000-INDEX.md` as part of the pilot.
- one router name per depot; no separate public/local router files.

### Numbering.Unchanged
- the `NNN` file-numbering system is **kept as-is** — out of scope, revisit later. `100-index.md` → `design/100-design.md` keeps `100`. Do not renumber, do not collapse ranges.

### Blast.Radius
- current state (inspected): `agentos-pkg/index/` holds `000-index.md`..`107-index.md` + `AGENTS.md`; `agentos-pkg/appendix/` has 26 files.
- ~30 files across skills reference `index/` or `000-index.md` and must be updated: `agentos-project-doctor` (7 refs), `agentos-index` (SKILL, `references/search.md`, `references/write.md`), `hugentics-designer` (`artifact.md`, `index-view.md`, `concept-discovery.md`, `writing-craft.md`), `agentos-pkg` (`SKILL.md`, `appendix/*`, `references/testground-format.md`, `testing/*`), `agentos-batchy-skills`, `agentos-live-surfaces`, `agentos-hugentics`.
- these are **path** references (structural). Updating them is in scope; changing any concept text around them is not.

### Driver.Dependency *(S0 resolved)*
- **no runtime driver** hardcodes index paths — the index is agent-read by convention (SKILL.md text points the way); confirmed by `agentos index` exposing only a `linter` subcommand.
- the only structural-aware tool is `agentos index linter`, which takes explicit `--index`/`--appendix` paths — but it **hardcodes the old model**: router `000-index.md`/`001-index.md` *inside* the index dir, and `NNN-index.md` filenames. The target layout fails it.
- **decision**: the linter is **not used for validation during this migration**; its update to the new model (chapters, `000-INDEX.md`, `NNN-<chapter>.md`) is a separate later effort. Validation here is agent-convention.

### Scope.Boundary
- **in**: the two package-skill depots — `agentos-chatlas-pkg` (pilot) and `agentos-pkg`.
- **out (this Impl.Req)**: the `agentos index linter` / index tooling update to the new model (separate later effort — the linter still encodes the old model and is not used here); the project-local `notes/index/` depot (its unified-router shape — `notes/000-INDEX.md` vs `notes/design/` — needs a separate confirm); all content/wording changes; numbering rework; the `Alignment.*.Axis` reconcile.

## Execution.Plan

### S0 — Verify the driver supports the target layout *(blocking, inspection-only)*
- what changes: nothing yet — locate what resolves the index folder and router filename (the `Package.Driver`/loader, likely in the agentos CLI).
- observable result: a cited answer to "does the loader accept `<pkg>/000-INDEX.md` + `<pkg>/design/`?"
- check: load the already-migrated chatlas skill and confirm its index resolves; identify whether the router filename is hardcoded.
- deviation trigger: if the driver requires a specific filename other than `000-INDEX.md` or hardcodes `index/` → **stop**, raise; the driver change becomes a prerequisite slice (may be out of repo).
- **RESULT (resolved)**: no runtime driver (agent-convention loading). `agentos index linter` hardcodes the old model but is **not used for validation this migration** (decision). S0 clears; proceed.

### S1 — Pilot: chatlas router rename
- what changes: `agentos-chatlas-pkg/ROUTER.md` → `000-INDEX.md`; update refs in `SKILL.md` (lines describing `ROUTER.md`→`design/`), `design/AGENTS.md`, and the 3 `chatlas-grounding-agent` refs.
- path it exercises: a fresh load of `agentos-chatlas-pkg` resolves its index via `000-INDEX.md`.
- observable result: chatlas index loads and routes with no `ROUTER.md` remaining.
- check: `grep -rn "ROUTER.md" agentos-chatlas-md/` returns nothing; load the skill, resolve one concept end-to-end; `000-INDEX.md` exists and lists every `design/` concept.

### S2 — agentos-pkg structural reshape
- what changes:
  - `agentos-pkg/index/` → `agentos-pkg/design/`
  - `design/100-index.md`..`107-index.md` → `design/100-design.md`..`107-design.md` (numbers kept)
  - `index/000-index.md` → `agentos-pkg/000-INDEX.md` (case-sensitive move — use `git mv`, two-step if needed on case-insensitive FS)
  - `index/AGENTS.md` → `design/AGENTS.md`
  - `appendix/` unchanged in place
  - update all ~30 path references from the Blast.Radius (structural only)
- path it exercises: a fresh load of `agentos-pkg` resolves its index via `000-INDEX.md` over `design/`.
- observable result: `agentos-pkg` matches the target layout; index loads and routes; no reference points at `index/` or `000-index.md`.
- check: `grep -rn "index/\|000-index.md" agentos-md/skills` returns only intentional/historical mentions (e.g. `index-migration/` archives); load the skill and resolve a concept; the router lists every `design/` concept and every appendix route still resolves (`Appendix.Discovery`).

### S3 — Compliance pass
- what changes: reconcile any stragglers surfaced by the checks (stale paths, a missed ref, an appendix route).
- observable result: both depots pass a layout+routing check; no broken concept or appendix paths.
- check (agent-convention, **not** the linter): every `Dotted.Name` in `000-INDEX.md` points to an existing `design/NNN-design.md`; every appendix file still resolves by `Appendix.Discovery`; `grep` for old paths (`index/`, `000-index.md`) is clean. The `agentos index linter` is intentionally not run — it encodes the old model (deferred tooling update).

### Acceptance signals
- chatlas and `agentos-pkg` both load via `000-INDEX.md` over `design/` + `appendix/`.
- no reference in the md repos points at the old `index/` folder or `000-index.md` router (excluding archives).
- concept routing and appendix discovery work unchanged — content and numbering untouched.

### Risks / deviation triggers
- **driver hardcodes paths** (S0) — prerequisite driver change; stop and raise.
- **case-only rename** of `000-index.md` → `000-INDEX.md` on a case-insensitive FS — use `git mv` / two-step.
- **wide ref ripple** (S2) — a missed path reference silently breaks a downstream skill; the `grep`-clean check guards this.
- **hidden content coupling** — if a "path" edit forces a wording change, it belongs to the content-upgrade Impl.Req; note and defer.

## Impl.Log

- **S0 DEVIATION → BLOCK (autonomous run, before any edit).** No runtime driver hardcodes index paths (index is agent-read by convention; the linter takes explicit `--index`/`--appendix` paths). BUT `agentos index linter` encodes the *old* index model: it only recognizes a router named `000-index.md`/`001-index.md` *inside* the index dir (`Index.Linter/Router.Missing`), and hardcodes `NNN-index.md` filenames (`Index.Linter/Index.InvalidFilename`). The target layout (`000-INDEX.md` at pkg root, `design/NNN-design.md`) fails the linter, so S3 compliance is unreachable as specified. chatlas's prior markdown migration already throws these 2 findings — it passes agent-convention reading, not tooling. Fix is `agentos` CLI code, outside `agentos-md`/`agentos-chatlas-md`. Conclusion: the 540 index *model* is not implemented in the tooling; file migration is premature. Halted before the git checkpoint (also: checkpoint wants a commit, colliding with the standing no-auto-commit rule). Awaiting direction (tooling-first vs expand-scope vs redefine-compliant vs re-open-naming).
- **S0 RESOLVED (user decision)**: update the linter too, but **later** — the linter is not used for validation during this migration. Target layout (`000-INDEX.md`, `design/NNN-design.md`) stays; tooling catches up separately. S3 validation switched to agent-convention checks. Proceeding (pending the git-checkpoint / commit-policy call before edits).
