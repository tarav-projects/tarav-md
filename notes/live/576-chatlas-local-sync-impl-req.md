# Chatlas Local Sync — Impl.Req

## Impl.Abstract

- **Goal**: bootstrap the project-local chatlas — `agentos chatlas local sync` ports the project's attributed chats into `<project-root>/chatlas/` as `turns`-filtered normal-model objects, so grounding chat information travels with the project (best effort).
- **Scope**: `chatlas local` CLI namespace with `sync` and `status`; relevance = the `Projects.Chats` path-attribution walk only; content = `turns`-filtered session models + session metadata; additive-overwrite write semantics.
- **Out of scope** (v1+, user decisions this session): the grounding relevance tier (anchor-scan → session set — agents check grounding manually for now); any READ path against the local folder (all queries/resolution/linting keep using the global chatlas); pruning (stale chats remain); privacy policy beyond the `turns` filter; resolution precedence on chatlas-less machines.
- **Repos**: `agentos-chatlas-py` only (new `local.py` or similar, `commands.py`, tests). Reinstall note: `uv tool install --reinstall --editable .` from `agentos-cli/` after CLI changes.
- **Source**: design discussion in session `9d194db7…` (2026-07-08/09); index concepts `Chatlas.Session.Model`, `Chatlas.Filter` (the `turns` preset IS the v0 content policy), `Chatlas.View` (model-closed outputs), `Surface.Link.Directionality` (the not-publicly-resolvable exception this feature works toward retiring).
- **Status**: implemented; review pending

## Impl.Index

### Design.Decisions *(user-aligned this session)*
- v0 is bootstrap + export only: nothing reads the local folder yet; the global chatlas serves every read
- relevance v0 = path attribution only (`Projects.Chats`: the project's own sessions plus its ancestors' — the existing `--project`/`--project-base` walk semantics); the grounding tier (sessions referenced by the project's anchors) is deliberately NOT wired — agents port those manually when needed
- content v0 = user+assistant visible messages only — implemented as the existing `turns` named filter (`apply_chatlas_filters(model, ("turns",))`); the exported file is still a model object, so future read tooling consumes it unchanged and widening the policy later is config, not migration
- sync semantics: ALWAYS overwrite what it computes, NEVER delete — attributed sessions are written/refreshed in place; files for other sessions (manual agent ports, stale chats) remain untouched; cleanup is a later concern
- do not overspecify the folder layout beyond what sync needs — this is v0 of a system that will grow

### Current.State *(inspect before coding)*
- `Projects.Chats` attribution: `chatlas query --project <path>` matches the indexed `project_path` exactly; the ancestors-union walk is one query per path level (`agentos-md` index, `Projects.Chats` concept) — check how `--project`/`--project-base` behave in `query.py` and reuse, do not reimplement matching
- `turns` filter: `agentos_chatlas/normalization/session_model/filters.py` (`apply_chatlas_filters`, registry `slim`/`messages`/`turns`)
- model load: `load_chatlas_session_model(row, chatlas_root=…)` via `index_query.select_one_chatlas_index_row`/`select_materialization_row` — the pattern `index_checks.py:_load_session_model` uses
- project root discovery: check what `agentos` already provides (e.g. `agentos rev-parse` / `agentos.project`) before inventing one; `sync` should accept an explicit `--project <path>` and default to a discovered root

### Local.Folder *(minimal v0 shape)*
- `<project-root>/chatlas/` — created by sync if absent
- per session: one model JSON (filename keyed by `identity_hash`; exact naming is executer open space) containing the `turns`-filtered session model, plus enough identity metadata to know what it is (the filtered model already carries `session` identity fields — verify that suffices; if not, a small sidecar or manifest is acceptable, keep it minimal)
- a top-level marker/manifest identifying the folder as a chatlas-local surface (versioned, so v1 can migrate) — one small JSON, no schema ambition

### CLI.Surface
- `agentos chatlas local sync [--project <path>]` — compute attributed set, export each session (`turns`-filtered), overwrite in place, report: sessions written, sessions skipped (load failures — best effort, never fatal), total in folder
- `agentos chatlas local status [--project <path>]` — report the computed attributed set vs the folder content: attributed-and-present, attributed-and-missing (sync would add), present-but-not-attributed (manual ports / stale — informational, never flagged for deletion)
- both are read-only against the global chatlas; only `sync` writes, and only under `<project-root>/chatlas/`

## Execution.Plan

*(test-first throughout; reuse the e2e fixture machinery in `tests/test_e2e_chatlas.py` — `AgentosTestEnvironment`, codex rollout writer, `_configure_chatlas`; rollouts carry `cwd`, which drives project attribution)*

### S1 — Attributed-set computation + export core
- what: library function: project path → attributed session rows (reusing query-layer matching) → per session, load model, apply `turns`, write JSON into the folder; the folder marker/manifest
- RED: fixture with two sessions in project A (distinct `cwd`s under it) and one in unrelated project B — sync-core over A exports exactly the two; exported JSON is a valid model object (has `chat.events`, message events only, no `normalization`/`sources` — the `turns` contract); a session whose model fails to load is skipped and reported, not fatal
- check: suite green
- status: done

### S2 — `chatlas local` CLI namespace
- what: `local` subparser with `sync` and `status`; `--project` optional with discovered-root default
- RED: e2e — `chatlas local sync --project <fixture-project>` creates the folder and files; running it twice is idempotent (same content); a manually planted extra file in the folder SURVIVES sync (the never-delete contract); `status` reports the three buckets correctly
- check: suite green; reinstall; scratch-project live smoke
- status: done

### S3 — Live acceptance + docs
- what: run `chatlas local sync --project /Users/pereiro/projects/agentos-project/agentos-md` for real; inspect the folder; `chatlas-commands.md` gains a "Local Chatlas Workflow" section (v0 boundaries stated: export-only, attribution-only, turns-only, never deletes); propose (gated, do not self-write) a `Local.Chatlas`/`Chatlas.Local` concept block for the chatlas index — verbatim draft in the completion report
- check: live folder sane (model JSONs load, turns-only); reference matches real CLI; both existing depots still lint clean (nothing index-side changed)
- status: done

### Acceptance signals
- one command ports a project's attributed chats as portable, model-closed, turns-filtered JSON into the project tree
- re-sync refreshes without deleting anything it didn't compute
- full `agentos-chatlas-py` suite green; `No.Regression.Tests.Allowed` respected

### Risks / deviation triggers
- attribution matching: if `--project` exact-match semantics make the ancestors-union awkward, implement the union in the new code by issuing one query per level (the documented `Projects.Chats` walk) — do NOT change query.py matching semantics
- project-root discovery: if agentos offers no clean discovery primitive, require `--project` explicitly in v0 and note it — do not invent a discovery subsystem inside this req
- size: turns-filtered models are small, but a project with hundreds of attributed sessions may surprise — report counts/bytes in sync output; no limits in v0, note observations in `Impl.Log`

## Impl.Log

- 2026-07-08: created workflow-required checkpoint commits before edits:
  - `agentos-chatlas-py` `efdc5cf`
  - `agentos-chatlas-md` `8eb5dbc`
  - `agentos-md` `af101b3`
- 2026-07-08: implemented `agentos_chatlas.local` with deterministic `chatlas/manifest.json` plus one `<identity_hash>.json` turns-filtered model file per written session.
- 2026-07-08: added `agentos chatlas local sync/status`; explicit `--project` is accepted and omitted `--project` resolves through `require_agentos_project_root`.
- 2026-07-08: deviation resolved: S1 fixture wording suggested descendant cwd matching, but `Projects.Chats` authority says exact selected project plus ancestors. Implementation uses exact query-layer matching and a bounded ancestor walk.
- 2026-07-08: deviation resolved: naive filesystem ancestor walking initially included `/Users` and `/`, over-attributing thousands of broad sessions. Corrected to the selected Agentos project plus contiguous Agentos-project ancestors only; for live `agentos-md`, attribution paths are `agentos-md` and `agentos-project`.
- 2026-07-08: deviation resolved: Abstract said `agentos-chatlas-py` only, but S3 explicitly required docs and audit-log edits. Updated `agentos-chatlas-md/skills/agentos-chatlas-pkg/references/chatlas-commands.md` and this `agentos-md` Impl.Req.
- 2026-07-08: live smoke: `agentos chatlas local sync --project /Users/pereiro/projects/agentos-project/agentos-md` wrote `3114` session files plus manifest under `agentos-md/chatlas/`; `3538` attributed sessions, `424` skipped. Skips were best-effort load failures, mainly existing cached `chatlas-session` schema-version mismatches.
- 2026-07-08: live status: `3114` attributed-and-present, `424` attributed-and-missing, `0` present-but-not-attributed.
- 2026-07-08: verification:
  - `uv run pytest` in `agentos-chatlas-py`: `141 passed`
  - `uv run ruff check src tests` in `agentos-chatlas-py`: passed
  - `uv run ruff check` in `agentos-chatlas-py`: blocked by unrelated pre-existing `dev/user-script-invariant-test/validate.py` unused `sys` import
  - `agentos index linter --depot skills/agentos-pkg`: `0 error(s), 0 warning(s)`
  - `agentos index linter --depot skills/agentos-chatlas-pkg`: `0 error(s), 0 warning(s)`
