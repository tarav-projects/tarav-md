# Chatlas1 Consumer Cutover - One Normal Model - impl-req

## Impl.Abstract

- **Status:** Open. Slices 1, 2, and 4a executed; 3 reclassified; 5–8 open.
- **Intent:** Finish the Chatlas2 cutover that `527` designed and `542` deferred — retire `chatlas/normalization/session_model/` as the session model and leave one Normal Model in Chatlas.
- **Source:** `527-chatlas2-normal-model-redesign-design-session.md` settled the model, the parallel-system boundary, and the cutover. `542-chatlas2-turns-scan-decode-verify-impl-req.md` lists **"Chatlas1 consumer cutover"** in its out-of-scope. This is that named work.
- **Scope:** the 19 `tarav/chatlas/*.py` modules importing `normalization/`, the substrate/model split inside `normalization/`, and the pairwise chatlas1/chatlas2 module duplicates.
- **Out of scope:** the dossier homogenization itself (its own artifact — see `Dossier.Homogenization`), Normal Model design changes, Raw.Archive layout, Session.Index schema, and any new grounding.
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
- [DC] **Decided (user, 2026-08-19): Copilot stays unsupported. Chatlas2 targets claude-code and codex.** The 23,702 raw files remain archived and unreadable through the Normal Model; `_copilot.py` is deleted with the rest of `session_model/`.
- [PR] The archive is git-backed and lossless, so leaving a provider unreadable is reversible: a Copilot normalizer can be written later against the same raw files.

### Dossier.Homogenization

- [DC] **Decided (user, 2026-08-19):** the legacy dossiers are *migrated*, not read in place. Convert every referenced `chatlas` dossier into the `chatlas2` model, keeping the same semantics, so one format remains.
- [RJ] This replaces the earlier sequencing plan, which kept `chatlas/anchory.py` alive until `640` had read through it. That preserved two formats to serve one migration and left the retirement order load-bearing.
- [CT] The data is kept. Migration writes the `chatlas2` namespace and leaves the `chatlas` namespace intact; `anchory-backups/` is the existing precedent for that.
- [EX] Scope is larger than `640` states: **2,364 distinct `^c` anchors** carrying **2,600 support members** across **44 sessions**, of which 915 dossiers are gated — spread over `tarav-md` (1,867), `tarav-chatlas-md` (423), `tarav-py` (172, as `$kw` annotations in source), and `notes/` (13).
- [DC] `tarav-py`'s 172 anchors are `Skw.Annotation` support on code surfaces; `640` covers depot markdown only, so the migration is not a subset of `640`.
- [EX] 1,305 of the store's 3,669 dossiers are referenced by nothing. They are neither migrated nor deleted.

### Join.Key

- [DF] `Legacy.Support.Join` maps a legacy `{session, turn_id, turn_hash, at}` member onto a Chatlas2 `{session, message_address, message_hash}` ref by matching side, exact message text, and `started_at`.
- [EX] Probed on `^c20260712-21u`: the session resolves in the Normal Model, and its member text `"approve"` matches **three** user messages — text alone is ambiguous.
- [EX] The member's `at` (`2026-07-12T00:47:44.993Z`) matches exactly one candidate's `started_at` to the millisecond. The pair is exact.
- [PR] Because the join key is exact, every member either resolves to exactly one message or is reported. The migration is auditable at 2,600 of 2,600 rather than trusted.
- [CT] A member that does not join exactly is reported, never guessed onto the nearest candidate.

## Execution.Plan

Slices are ordered by cost and by what unblocks what. Slices 1–3 are independent of `640`; slices 5–6 are not.

### Slice 1 — Delete the dead module
`chatlas/line_manifest.py`, 358 lines, zero importers, superseded by `lossless/line_manifest.py`.
**Check:** suite green; `tarav chatlas` help unchanged; `grep -rn "chatlas.line_manifest"` empty.

### Slice 2 — Retire the isolated model parts  *(done, narrowed)*
`traceability.py` was the only genuinely isolated one. `provenance.py` and `source_refs.py` have no *external* consumer but are used throughout `session_model/` internally — they die with it in slice 6, not standalone.
Before deleting `traceability.py`, its one durable constraint was carried to the Normal Model: a stored `Event.Ref` must survive reordering, because `Event.Address` is a place and not a position. Verified RED against a positional-lookup probe — it was the only test in the file that failed, which is what made it worth carrying.
**Check:** suite green after the constraint is ported and the old subject removed.

### Slice 3 — Turn and message helpers  *(reclassified: design port, not mechanical)*
The authoring presumption was wrong and execution disproved it. These helpers are not pure functions over a neutral payload — they read **old-model event annotations**: `normal_turn_kind`/`normal_turn_id` read `event.annotations.normal_turn`, and `visible_message_texts` additionally requires `event.surfaces.transcript == "visible"`.
The Normal Model has no such annotations. It expresses both ideas as first-class collections — `Chat.Turn` and the `Chat.Message` projection — which `527` settled as *"the messages the user sees and reacts to."* So each consumer must be re-expressed against the collection, deciding what "which turn is this event in" means for it.
Only `content_text` is genuinely portable as-is.
**Sequence with slice 5.** These consumers overlap the pairwise duplicates, so port each one where its module is decided, not ahead of it.
**Check:** each consumer's tests pass against the collection-based expression; anything not preservable is named, never shimmed.

### Slice 4 — Extract the substrate  *(4a done)*
Carve `index_row/`, `artifact.py`, `hashes.py`, and the trust tier out of `normalization/` into substrate homes that carry no session model.
**4a (done):** `Normalization.Trust.Tier` now lives in `chatlas/trust_tier.py`. It is six lines of `ContextVar` that two callers were reaching through a 622-line module that imports `_claude`, `artifact`, `provenance`, and `source_refs`. `_command_support` and `hook_consumers` are now fully severed from `normalization/`.
**4b:** `index_row/`, `artifact.py`, `hashes.py` — consumers `index_writer`, `session_cache`.
**Check:** each substrate module imports nothing from `session_model/`; archive update and session-index write paths still work end to end.

### Slice 5 — Resolve the pairwise duplicates  *(after the dossier migration)*
`anchory`, `chat_index`, `chat_index_plan`, `event_ref`, `query`, and the `_views`/`views` pair each exist in both. Chatlas2's version wins.
**Blocked by:** the dossier homogenization, which is its own artifact — it spans four repos, includes code surfaces `640` does not cover, and `640` itself becomes a consumer of its output. Once every referenced anchor is a `chatlas2` dossier, nothing reads the legacy resolver and this slice is an ordinary deletion.
**Check:** one implementation each; `tarav index linter` still resolves the depot's grounding; a sample of migrated anchors resolves to the same message text as before.

### Slice 6 — Delete `session_model/`
Including the claude and codex normalizers, once slices 3–5 leave nothing pointing at them.
**Check:** `chatlas/normalization/` contains no session model; the architecture test asserts no module outside `lossless/` builds a session model.

### Slice 7 — Copilot  *(decided)*
Leave Copilot unsupported. `_copilot.py` (3,000 lines) goes with `session_model/` in slice 6; the raw files stay archived.
**Check:** no Copilot-specific carve-out survives in the cutover; slice 6 deletes it as ordinary model code, and the raw archive is untouched.

### Slice 8 — `file_touch`  *(decided: retire)*
`file_touch_invocations` / `tool_contains_invocations` walk `chat.tool_invocations`, a typed collection only the old model projects. **Decided (user, 2026-08-19): retire it**, and reimplement over the event tape if a use case appears.
Remove the filters from `tarav chatlas query` and the inline views. Do not keep a thin `tool_invocations` projection alive to feed them — that resurrects a slice of the ambitious model under a smaller name, which is how the first merge produced `lossless/`.
**Check:** the two call sites are gone, not stubbed; the raw archive is untouched, so a later reimplementation has its source.

## Slice Status

| # | Slice | Blocked by | Status |
|---|---|---|---|
| 1 | delete `chatlas/line_manifest.py` | — | **done** |
| 2 | retire isolated model parts | — | **done** (narrowed) |
| 3 | turn and message helpers | 5 | reclassified — design port |
| 4a | extract `Normalization.Trust.Tier` | — | **done** |
| 4b | extract `index_row`/`artifact`/`hashes` | — | not started |
| 5 | resolve pairwise duplicates | dossier migration | not started |
| 6 | delete `session_model/` | 3,4,5,7 | not started |
| 7 | Copilot decision | — | **decided** — leave unsupported |
| 8 | `file_touch` | — | **decided** — retire |

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
- **Executed 2026-08-19.** Importers of `normalization/` went 19 → 16; `chatlas/line_manifest.py` (358 lines, zero importers) and `session_model/traceability.py` deleted; `chatlas/trust_tier.py` added. Suite 2057 → 2052 (six old traceability tests retired, one durable constraint carried forward), ruff clean.
- **Deviation — slice 2 narrowed.** `provenance.py` and `source_refs.py` were planned as free deletions on the evidence that nothing outside `normalization/` imports them. That evidence was incomplete: `source_refs` has twelve internal importers and `provenance` two. External-consumer count is not a deletability test when the package still stands. They move to slice 6.
- **Deviation — slice 3 presumption disproved.** The authoring `Index.Presumption` held that the leaf helpers were mechanical because they are pure functions over a payload dict. They are pure, but the payload is the *old model*: `annotations.normal_turn` and `surfaces.transcript` are shapes the Normal Model deliberately does not have. Reclassified as a design port and sequenced with slice 5 rather than ahead of it. This is the presumption doing its job — it was written to be checkable and it failed the check.
- **`Index.Presumption` (open):** slice 4b is assumed as clean as 4a. `index_row/` is a separate subpackage and `hashes.py` is 54 lines, but `artifact.py` (98) was not read before this estimate.
- The previous merge's real error was scoping to the CLI surface and reporting "absorbed." The CLI was one surface; the model is the system. This artifact exists so the second attempt is measured against consumers, not against `tarav --help`.
