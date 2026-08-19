# Chatlas1 Consumer Cutover - One Normal Model - impl-req

## Impl.Abstract

- **Status:** Open. Designed, not executed.
- **Intent:** Finish the Chatlas2 cutover that `527` designed and `542` deferred — retire `chatlas/normalization/session_model/` as the session model and leave one Normal Model in Chatlas.
- **Source:** `527-chatlas2-normal-model-redesign-design-session.md` settled the model, the parallel-system boundary, and the cutover. `542-chatlas2-turns-scan-decode-verify-impl-req.md` lists **"Chatlas1 consumer cutover"** in its out-of-scope. This is that named work.
- **Scope:** the 19 `tarav/chatlas/*.py` modules importing `normalization/`, the substrate/model split inside `normalization/`, and the pairwise chatlas1/chatlas2 module duplicates.
- **Out of scope:** the `^c` anchor transformation (that is `tarav-md` `640`), Normal Model design changes, Raw.Archive layout, Session.Index schema, and any new grounding.
- **Grounding:** none minted. The index freeze (`638` Invariant 1) is in force; `Impl.Index` below carries `Index.Presumption` and cites measurements instead of anchors.
- **Acceptance:** one session model in `tarav/chatlas`; every retained consumer reads it through the canonical Normal Model provider; the suite is green; `tarav index linter` still resolves the depot's grounding.

## Why This Exists

The previous merge (`tarav-py` commits `9e505d6..e067c71`) moved `chatlas2/` to `chatlas/lossless/` and merged the CLI. It cut the dead check path and the duplicate CLI verbs — 3,248 deletions — but it did not touch the two session models. Both are still live:

```
chatlas/normalization/   13,399 lines   19 importers
chatlas/lossless/         7,669 lines    2 importers
```

The split is not old-vs-dead. The index grounds through `lossless/`; chatlas reads chat through `normalization/`. The subsystem that owns the archive and the subsystem that grounds index lines do not agree on what a session is.

The folder rename is what let that pass as finished: `chatlas2` was visibly a second system, `chatlas/lossless/` reads like a component.

## What The Design Already Settled

Do not re-litigate these. `527` decided them.

- `Chatlas2.Normal.Model` is the model. Its shallow semantic floor is the design, not a deficiency — *"Data completeness has priority over total consistency."*
- `509-session-model-design-session.md` — the model behind `normalization/` — is *"the older, more ambitious model … prior design evidence, not inherited Chatlas2 truth."*
- Consumers were designed for: *"Consumers request complete or stream-readable Normal Model content and own no cache validation or recomputation policy; Anchory is one ordinary complete-model consumer."*
- The parallel state was temporary: *"during the experimental cutover."*
- **The substrate survives, the model does not:** *"Current Chatlas remains the raw-archive and session-recovery substrate while Chatlas2 matures."*
- No permanent migration subsystem: anchor records are *"transformed operationally when Chatlas2 cuts over … protected by the depot's Git history rather than maintained as a Chatlas2 subsystem."*

## Impl.Index

### Cutover.Shape

- [DF] `Chatlas1.Consumer.Cutover` is the retirement of `session_model/` as Chatlas's session model, moving retained consumers onto the canonical Normal Model provider.
- [DC] The cutover splits `normalization/` along the line `527` drew: the raw-archive and session-recovery substrate is retained, the session model is deleted.
- [CT] A module that only reads already-built payload fields is a substrate consumer only if the field it reads survives in the Normal Model; otherwise it is a port.
- [PR] Consumer count overstates the work. Measured, only five capabilities cross the boundary; the rest are leaf helpers over a payload dict.
- [RJ] This is not a rewrite of `normalization/`'s consumers into `lossless/`. Modules that duplicate a chatlas2 module are deleted, not ported.

### Measured.Boundary

- [EX] `session_model/` is 11,799 lines, of which **8,199 are the three provider normalizers** (`_copilot` 3000, `_claude` 2843, `_codex` 2356). Chatlas2 covers the same two live providers in **948** (`claude` 558, `codex` 390).
- [EX] `provenance.py` (137) and `source_refs.py` (131) have **no consumer outside** `normalization/`; `traceability.py` (209) is referenced only by one test.
- [EX] `chatlas/line_manifest.py` (358 lines) has **zero importers** — `lossless/line_manifest.py` already replaced it.
- [DC] Exactly five capabilities are consumed across the boundary: `file_touch`, `delta.set_trust_tier`, `artifact`, `hashes.session_identity_hash`, and `_views`.
- [PR] Three of those five (`delta.set_trust_tier`, `artifact`, `hashes`) are archive/session-recovery substrate, so they are relocated rather than ported.

### Copilot.Decision

- [EX] `copilot-cli` holds **23,702 raw files** — the largest provider in the archive by file count — and Chatlas2 has no Copilot normalizer.
- [EX] It is dormant: **0 files since 2026-08-01**, last activity 2026-07-29, against claude-code 2026-08-19 and codex 2026-08-17.
- [EX] Of the index's **2,466** support members, **zero** resolve to a Copilot session; all are codex (1,181) and claude-code (1,285) across 41 distinct sessions.
- [DC] Copilot normalization is therefore not load-bearing for grounding; it is a chat-*reading* capability over dormant history.
- [CT] Dropping 3,000 lines of Copilot normalization is a decision the user takes, not a silent consequence of the cutover. Slice 7 states the options and stops.

### Sequencing.Constraint

- [DC] `640` must import the `^c` dossiers **before** `chatlas/anchory.py` is retired: resolving a legacy dossier to its message text needs the model that minted it.
- [CT] This is the operational transformation `527` specified. Both systems stand until it completes, then the old side goes — the sequence is the design, not an accident.
- [RJ] Do not build a compatibility resolver so the two can be retired in either order. That is the maintained migration subsystem `527` rejected.

## Execution.Plan

Slices are ordered by cost and by what unblocks what. Slices 1–3 are independent of `640`; slices 5–6 are not.

### Slice 1 — Delete the dead module
`chatlas/line_manifest.py`, 358 lines, zero importers, superseded by `lossless/line_manifest.py`.
**Check:** suite green; `tarav chatlas` help unchanged; `grep -rn "chatlas.line_manifest"` empty.

### Slice 2 — Delete the internally-consumed-only model parts
`provenance.py`, `source_refs.py` have no external consumer. `traceability.py` has only a test — read the test first and decide whether the constraint it asserts belongs on the Normal Model's `Event.Ref` instead; if it does, move the assertion, do not delete it.
**Check:** suite green after the test is either ported or removed with its subject.

### Slice 3 — Provider-neutral leaf helpers
Give the Normal Model equivalents of `normal_turn_kind`, `normal_turn_id`, `content_text`, `visible_message_texts`, `apply_chatlas_filters`, `compute_event_hash`, then move `event_pattern`, `event_query`, `recents`, `tagger`, `touch_heuristics`, `normal_turn`, `local`, `query` onto them.
These are pure functions over a payload; the port is mechanical **except** where a field has no Normal Model counterpart — that is a real finding and belongs in `Impl.Log`, not a silent shim.
**Check:** each ported module's own tests pass unchanged; any behavior that could not be preserved is named.

### Slice 4 — Extract the substrate
Carve `index_row/`, `artifact.py`, `hashes.py`, and `delta.set_trust_tier` out of `normalization/` into a substrate home that carries no session model. Consumers: `index_writer`, `session_cache`, `_command_support`, `hook_consumers`.
`527` says this survives; the point of the slice is that it stops living inside the package being deleted.
**Check:** the substrate module imports nothing from `session_model/`; archive update and session-index write paths still work end to end.

### Slice 5 — Resolve the pairwise duplicates  *(after `640`)*
`anchory`, `chat_index`, `chat_index_plan`, `event_ref`, `query`, and the `_views`/`views` pair each exist in both. Chatlas2's version wins — `527` routes grounding through Chatlas2 records.
**Blocked by:** `640` Slices 1–4. Do not start before the `^c` import lands.
**Check:** one implementation each; `tarav index linter` still resolves the depot's grounding; a sample of migrated records still resolves to message text.

### Slice 6 — Delete `session_model/`
Including the claude and codex normalizers, once slices 3–5 leave nothing pointing at them.
**Check:** `chatlas/normalization/` contains no session model; the architecture test asserts no module outside `lossless/` builds a session model.

### Slice 7 — Copilot, as a stated decision
Present the measurement (23,702 raw files, 0 grounding, dormant since 2026-07-29) and the three options: write a Chatlas2 Copilot normalizer, drop Copilot read support and keep the raw archived, or keep `_copilot.py` alive as a read-only island.
**Check:** the decision is recorded here before slice 6 deletes anything Copilot-related. This slice does not choose autonomously.

### Slice 8 — `file_touch`
`file_touch_invocations` / `tool_contains_invocations` feed `query` and `inline`; `543` put tool/file-touch semantics out of Chatlas2 scope, so the Normal Model has no counterpart.
Either express it over the event tape or retire the two call sites. Do not shim.
**Check:** whichever is chosen, `tarav chatlas query` and the inline views behave as before or the change is documented.

## Slice Status

| # | Slice | Blocked by | Status |
|---|---|---|---|
| 1 | delete `chatlas/line_manifest.py` | — | not started |
| 2 | delete internally-consumed-only parts | — | not started |
| 3 | provider-neutral leaf helpers | — | not started |
| 4 | extract the substrate | — | not started |
| 5 | resolve pairwise duplicates | `640` 1–4 | not started |
| 6 | delete `session_model/` | 3,4,5,7 | not started |
| 7 | Copilot decision | — | not started (needs user) |
| 8 | `file_touch` | — | not started |

## Verification

- `uv run python -m pytest -q` green at every slice boundary.
- `uv run ruff check src tests` clean.
- `tarav index linter` over `tarav-md` still reports its checks passing with no drop in resolved records.
- `tarav chatlas` exposes one session model: no command reads `session_model/`.
- Final line count: `normalization/` reduced to substrate only.

## Impl.Log

- **Measured at authoring (2026-08-19).** `normalization/` 13,399 lines / 19 importers; `lossless/` 7,669 / 2 importers (`chatlas/commands.py`, `index/chatlas.py`). Provider normalizers 8,199 old vs 948 new. Take fresh counts before executing.
- **`Index.Presumption`:** the leaf-helper port (slice 3) is assumed mechanical because the helpers are pure functions over a payload dict. Not verified field-by-field against the Normal Model. If a field is missing, slice 3 grows and slice 6 waits.
- **`Index.Presumption`:** slice 5 assumes chatlas2's `anchory`/`chat_index` are functionally complete against their chatlas1 counterparts. They are smaller (1064 vs 1671, 537 vs 1037); the difference is presumed to be the ambitious model's extras, not lost capability. Verify before deleting.
- **Waiver (Autonomous mode):** no anchors minted and no `Chat.Index` backpropagation attempted for this artifact. The index freeze (`638` Invariant 1) forbids writing new grounding until the core engine converges. `Impl.Index` above is unanchored by intent, not by omission.
- **Deviation noted, not fixed:** `tarav-py/AGENTS.md` still documents the distribution as `agentos-py` with `agentos ...` commands throughout. It is stale against the completed rename. Out of this scope; worth its own pass, and `AGENTS.md` requires updating when this cutover lands.
- The previous merge's real error was scoping to the CLI surface and reporting "absorbed." The CLI was one surface; the model is the system. This artifact exists so the second attempt is measured against consumers, not against `tarav --help`.
