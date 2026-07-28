# 513 — Normal.Turn Identity + Anchory v2 — Impl.Req

## Impl.Abstract

**Scope.** Give `Chatlas.Session.Model` a stable, provider-general turn identity (`Normal.Turn`), make user-turn grouping faithful to actual user authorship, re-key `Chatlas.Anchory` records onto that identity, migrate the existing anchor corpus, and repoint the index linter's turn resolution.

**Why.** Anchory members identify turns by `event_id`, which is a tape ordinal (`"event-" + sequence`). Re-materializing an open session re-segments the tape and reassigns ordinals, so landed anchors silently come to point at other turns. Observed: 31 `Anchor.Turn.Missing` linter errors across 4 anchors; root cause traced to positional reassignment with timestamps stable.

**Status.** Executed. Slices 1–4, 6, 7 done; Slice 5 partially done and blocked on a gated skill-surface decision (see `Impl.Log`). Suites green: `agentos-chatlas-py` 216, `agentos-py` 551, `agentos-cli` 62. Default linter byte-clean on `agentos-pkg` and `agentos-chatlas-pkg`. Anchor corpus: 395 anchors / 401 members resolving under `chatlas.support-set.v2`.

**Source context.** Design session captured into `agentos-chatlas-pkg/design/100-design.md`: new blocks `Event.Grouping` and `Normal.Turn`; amended `Session.Event.Tape`, `Chatlas.Anchory`, `Chatlas.Session.Model`.

**Out of scope.**
- copilot-cli normalizer parity (open extension per `Chatlas.Session.Model.Tests`); design must not block on it.
- a separate request/response-cycle grouping — `interaction_ref` is *renamed* to `turn_id` and kept as the turn grouping here; a distinct cycle grouping is a later concept if wanted.
- retiring `Chat.Support.Set` member semantics (still user turns, still ordered, still relevance-sorted).
- the deferred grounding of the five design lines landed this session (blocked on Slice 3; see Impl.Log).

## Impl.Index

### Current.State

- **the turn grouping already exists.** Both normalizers compute `interaction_ref`, and the contract already declares its meaning as *"neutral reference to the user interaction (turn) the event belongs to"* (`agentos-chatlas-py/references/normal-model.contract.json`). It is positional (`interaction-N`), not identity — and misnamed for what it is.
- **the corpus is ready as a test set.** `agentos-chatlas-py/dev/user-script-invariant-test/` holds the `User.Script.Invariant` scripts, 11 accepted provider sessions joined by `identity_hash` (`primes-utility`: 4 codex + 7 claude), the engines (`validate.py`, `projection.py`, `path_source_split.py`, `coverage.py`, `comparative_projection.py`), and the verdict memory (`path-verdicts.md`, `divergence-notes.md`, `coverage-baseline.md`).
- **the boundary rules already differ per provider.** claude: `_claude_record_starts_interaction` in `normalization/session_model/_claude.py:889` — a visible user message that is not tool evidence. codex: `interaction_refs_by_turn_id` in `normalization/session_model/_codex.py:1160` — inherits native `turn_id` wholesale.
- **native handles are populated and survive materialization.** On the `primes-utility` corpus: codex carries `native.turn_id` on 100/101 events; claude carries `native.parent_uuid` (75), `native.message_id` (37), `native.request_id` (37).
- **`event_id` is a stringified duplicate of `sequence`.** `normalization/session_model/events.py:210` emits `f"event-{sequence}"` beside `sequence`; the contract entry says so outright (*"tape-local event identifier, equal to 'event-<sequence>'"*).
- **the contract already tombstones sibling keys.** `retired_keys` holds `$.chat.events[*].message_id` and `$.chat.events[*].request_id` as *"loose provider id at envelope level — converged into native.*"* — precedent for the `event_id` retirement.
- **126 `event_id` references across 15 files**; producers are the 6 normalizer files, consumers are `anchory.py`, `event_query.py`, `event_pattern.py`, `inline.py`, `index_checks.py`, `file_edition_pois.py`, `traceability.py`, `_views.py`, plus `agentos-py/src/agentos/skillware/edition_history.py`.

### Hard.Evidence

- **Cross-provider convergence already holds for clean runs.** On the `User.Script.Invariant` `primes-utility` script, claude and codex both yield exactly the 7 canonical user turns, verbatim-identical, each in its own `interaction_ref` (1–7), with injected AGENTS.md / `environment_context` content excluded from user message events on both sides. The grouping semantic is therefore reachable generally; what is missing is a stable *name* for it.
- **Codex over-merges at the raw level.** In `rollout-…-019f133f-….jsonl`, 8 user records carry only 7 distinct `turn_id`s: the injected instructions record and the first real prompt share one `turn_id`. Inheriting native grouping unrefined is therefore unsafe as a general rule, even though this particular case is already handled downstream.
- **Claude over-splits and mislabels.** A slash-command invocation produces three `role=user` message events at one timestamp, each with its own `interaction_ref` (62/63/64), and `producer.type` is assigned wrongly: the record holding the user's typed arguments is `{name: command, type: system}` while the injected skill body is `{type: human}`. This is an `Unjustified/lossy` normalizer defect in the `Faithfulness.Verdict` sense.
- **Anchor corpus audit (397 members / 394 anchors / 22 sessions).** Before repair: 391 resolved correctly, 5 drifted but uniquely recoverable by `at`+role, 1 ambiguous. All 6 defects belonged to a single still-open session; every closed session's anchors were intact. After the repair pass: 397/397 resolve to their stored user turn.
- **Only 3 of 397 members carry `types` cargo** — the approval-turn machinery is young, so the v2 format change lands cheaply.

### Design.Decisions

- `Normal.Turn` is not a new field: it is `interaction_ref` renamed to `turn_id` and given a stable identity plus an enforced purity rule. The contract already claims turn semantics for it; this work makes the claim true.
- canonical `$.chat.events[*].turn_id` deliberately shares a name with source-native `$.chat.events[*].native.turn_id` (codex). The contract entry must state explicitly that the canonical field is the model's own identity — seeded from native handles, never equal to one by contract — or a reader will take it for a provider passthrough, the very failure `retired_keys` records for envelope-level `message_id`.
- the `User.Script.Invariant` corpus is the primary test instrument, not a convenience. It is the only surface holding the *same* user script across providers, so it is the only thing that can distinguish "the mechanism is general" from "it happens to work on claude". Every slice that touches normalization asserts against it.
- Turn identity is sourced by a general rule, not a shared value. Each `Raw.Normalizer` maps its native handle onto the model's semantic (codex `turn_id`; claude message/parent uuid). Cross-provider identity *equality* is explicitly not a goal — only generality of the mechanism.
- A native grouping that over-merges is refined, never inherited. A provider offering no handle gets a synthesized identity; synthesis is the fallback, not the primary path.
- `producer.type` is the purity classifier for user turns. A user turn admits only human-produced content; command wrappers, system reminders, and injected skill bodies are excluded. Fixing the misassignment is in scope because purity depends on it.
- `event_id` is retired to a contract tombstone; `sequence` remains the sole positional field. Retirement lands *after* migration, since the migration pass reads v1 records keyed on `event_id`.
- Migration is a re-key, not an amend of meaning: each v1 member resolves once against its materialization and is rewritten to that turn's identity, preserving the anchor's hint and cargo.
- The linter is repointed rather than relaxed. The 31 errors were the check working correctly; the fix is a stable key, not a weaker assertion.

### Impl.Agendix

**index → touched** (blocks this implementation must honor, `agentos-chatlas-pkg/design/100-design.md`):

- `Event.Grouping` — tape is SSOT; a grouping is a tag, never a container; groupings are open and orthogonal; partial by nature; a stability contract binds only a grounded grouping.
- `Normal.Turn` — chat-semantic grouping; boundary per turn kind; user-turn purity; identity carries the stability contract; normalizers map native handles; identity not interpretation.
- `Session.Event.Tape` — `sequence` is the only positional field; `event_id` retired; durable references key on a grouping with a stability contract.
- `Chatlas.Anchory` — record format `chatlas.support-set.v2`, members keyed on `Normal.Turn` identity.
- `Chatlas.Session.Model` — the model carries chat data, never a consumer's interpretation.
- `Chatlas.Session.Model.Tests`, `Normalization.Pipeline::Chatlas.Session.Model` — the corpus engines and their three-way triage.
- `agentos-pkg` `Normalization.Pipeline-appendix`: `Under.Normalization`, `Model.Fragment` (topological, not positional), `Normal.Model.Contract`, `Projection.Test`.

**chat → touched**: deliberately empty. Minting anchors now would register v1 records keyed on `event_id` against a still-open session — manufacturing exactly the drift this artifact retires. Chat grounding for this work is deferred to after Slice 3 and recorded in `Impl.Log`.

## Execution.Plan

### Slice 1 — user-turn purity — **DONE**

Make `producer` classification faithful, so "which event is the user" has a trustworthy answer before anything keys on it.

**Result.** `_CLAUDE_USER_SYSTEM_MARKERS` gained a `skill-body` marker, and a command record carrying non-empty `<command-args>` now classifies `human` (the wrapper is harness formatting around the user's own words; a bare invocation stays `system`). Tests in `tests/test_user_turn_purity.py` (4, RED→GREEN); full suite 212 green. Session-wide effect on the design session: 10 injected skill bodies demoted from `human`, 7 command-with-args records promoted (76 → 73 human user events).

- correct the claude marker table so command wrappers and system reminders classify `producer.type: system`, and the record carrying the user's typed content classifies `human`.
- assert the rule generally: a user turn admits only human-produced content.
- **RED→GREEN**: a test over the known slash-command triple asserts exactly one human-produced user event; RED against current classification.
- **Check (corpus)**: `validate.py`'s acceptance filter still passes on all 11 accepted sessions — user turns stay verbatim-identical and in order. A purity change that breaks the acceptance filter is a normalization error by construction, so the corpus is the guard against over-filtering.
- **Check**: on `primes-utility`, user-turn counts equal the script's 7 on both providers; the triple collapses to one human turn.
- **Observable**: `agentos chatlas views inline --filter turns` no longer surfaces injected records as user turns.

### Slice 2 — turn_id: rename and stable identity — **DONE**

**Result.** `interaction_ref` → `turn_id` across model, contract, and all three normalizers; the old key tombstoned in `retired_keys`. Identity now comes from each provider's native handle: claude the turn-opening record's `uuid` (`claude_turn_id`), codex the native `turn_id` adopted directly, copilot `interactionId` with the provider event id as fallback. No `f"interaction-{n}"` remains anywhere in `src/`. Tests: `tests/test_turn_identity.py` (4, RED→GREEN); suite 216 green. Corpus: all 11 `primes-utility` sessions carry `turn_id` on every event, zero positional values, exactly 7 distinct human user turns per session on both providers.

- rename `interaction_ref` to `turn_id` across model, contract, and consumers; tombstone the old key.
- give it a stable value: the contract entry declares it the model's own turn identity — seeded from native handles, never contractually equal to one — with its null policy for non-turn-bearing events.
- populate it in both normalizers from their native handles (codex `native.turn_id`, claude message/parent uuid), refining any native grouping that over-merges; synthesize where no handle exists.
- **Check**: re-materialize a session at two different tail states; every `turn_id` is unchanged (the direct regression test for the original defect).
- **Check (corpus)**: `Projection.Test` over `primes-utility` — the path resolves for all turn-bearing events on claude *and* codex, absences justified; `Path.Source.Split.Test` shows no source split on it, which is the mechanical proof the mechanism is general rather than provider-shaped.
- **Observable**: `turn_id` present and stable in `session-model.json`.

### Slice 3 — anchory chatlas.support-set.v2 — **DONE**

**Result.** Members key on `turn_id`; schema is `chatlas.support-set.v2`; an ordinal-keyed v1 member is rejected as an unknown field. New `turn_landing_event` resolves a member to its turn's human user message (the touch the `Touched.Index` grounds on), falling back to the turn's first event for general event support sets. `event_neighborhood` and the `--member` CLI now take turn refs; the dead `_event_by_id` is gone. Suite 216 green.

**Semantic consequence recorded:** the old "rejects a non-user member" case changed meaning. A member now names a *turn*, and a turn containing the user's question is a legitimate support turn even if the caller pointed at its assistant reply. Rejection now belongs to turns holding no human user message — the session-scope group is the standing example, and the test asserts that instead.

- member key becomes `<session>:<turn-identity>`; `at` retained for readability and integrity checking.
- update register / resolve / amend and the `--member` CLI surface; `types` cargo (`verbatim_turn`, `approval_turn`) moves to turn refs.
- **RED→GREEN**: registering an ordinal-keyed member is rejected; resolving a v2 record returns the intended turn.
- **Check**: a v2 anchor minted against an open session still resolves after further session growth.

### Slice 4 — corpus migration — **DONE**

**Result.** Depot backed up to `~/Documents/chatlas/anchory.v1-backup-202607280621`, then 391 records migrated to `chatlas.support-set.v2` and 6 `types` cargo refs (`verbatim_turn`/`approval_turn`) rewritten to turn refs. No `at` value moved — the turn's landing event was always the original member event, which confirms the mapping is exact rather than approximate. Verification: 391/391 anchors and 397/397 members resolve through the production path. No v1 record remains.

**The defect, demonstrated fixed on real data.** `c20260726-9u` was minted at `event-2053`; after re-derivation its landing event is `event-2043`. The ordinal moved by ten and the anchor still resolved, because it now keys on the turn.

- one offline pass over all 394 anchors / 397 members: resolve each v1 member against its materialization, write the v2 turn identity, preserve hint, order, and `types`.
- re-audit `c20260726-6u` under the Slice 1 classifier — it is the one member whose correct target the v1 format could not express (currently re-keyed provisionally to the record holding the user's typed args).
- **Check**: 397/397 resolve post-migration; a forced re-materialization changes no resolution.
- **Observable**: no `chatlas.support-set.v1` record remains in the depot.

### Slice 5 — event_id retirement — **BLOCKED, needs user input**

**Partially done.** The durable-reference half landed: `agentos-py`'s `edition_history.py` — the other `Chat.Support.Set` producer — now builds `turn_id` members on `chatlas.support-set.v2` (551 tests green). That closes the last surface where a durable reference could be keyed on an ordinal, which was the retirement's actual purpose.

**Blocked on the rest.** Removing `event_id` from the event envelope was attempted and reverted: it breaks 53 tests, and the breakage is concentrated in `Event.Pattern` — an **agent-facing DSL** whose `event_id` predicate and projection are documented in `agentos-md/skills/agentos-index/references/link.md`, a gated, Skillware-managed surface. Retiring the field is therefore a public contract change requiring an approved skill edit, which an autonomous run cannot self-authorize.

**Assessment: this is now hygiene, not correctness.** With `chatlas.support-set.v2` and `edition_history` both keyed on `turn_id` and both rejecting an `event_id` member, the field can no longer be reached by anything durable. Retiring it prevents future misuse; it does not fix a live defect.

**Superseded by Impl.Req 514.** The blocker was that retirement removes sub-turn addressing with nothing to replace it. `514-event-addressing-impl-req.md` supplies the replacement (`event_hash` plus the `<hash>:<idx>` reference form) and carries the retirement as its final slice.

- stop emitting `event_id`; add it to `retired_keys` beside the existing `message_id` / `request_id` tombstones.
- migrate the consumer surfaces (`event_query`, `event_pattern`, `inline`, `file_edition_pois`, `traceability`, `_views`, `edition_history`) onto `sequence` for order and turn identity for reference.
- **Check**: contract schema-closure passes; no emitted event carries `event_id`; full suite green.
- **Check (corpus)**: `coverage.py` against `coverage-baseline.md` — retiring a duplicate key must not move `Normalization.Coverage`; a drop means real information was dropped with it.

### Slice 6 — linter turn resolution — **DONE**

**Result.** `index_checks.py` resolves cargo refs by turn: `_turn_text` splits on the turn id and the new `_turn_message_text` joins every message the turn carries, so a proposal split across several assistant messages still verifies — the gate now checks the turn, not one event. Default linter over `agentos-pkg` and `agentos-chatlas-pkg`: **0 errors, 0 warnings, 23 checks passed** on both. The 31 `Anchor.Turn.Missing` errors are gone, and they are no longer reachable by re-materialization alone.

- repoint `index_checks.py` (grounding provenance, `Line.Approval`, `Line.Verbatim.Gate`) at v2 turn identity.
- **Check**: default linter run over `agentos-pkg` and `agentos-chatlas-pkg` is byte-clean; the `Anchor.Turn.Missing` class cannot be produced by re-materialization alone.

### Slice 7 — end test: the system grounds its own design — **DONE**

**Result.** Four v2 anchors (`c20260728-0u`…`-3u`) minted against this still-open session, each carrying `tokenized.approval.turn` cargo chaining its `Edition.Approval.Token` (`2e8b6a05`, `4f9d3e27`, `0d5a9e63`, `8e3f1b7d`) to its proposal turn and approval turn. All 21 landed design lines now carry their anchor. Each anchor resolves to its exact `::approve` turn.

- `Line.Verbatim.Gate` over the depot: **0 errors**, and no finding names any `c20260728` anchor — all four token chains verify. The 184 warnings are legacy review-debt on pre-token anchors, untouched by this work.
- **Acceptance met.** After forcing re-materialization of the live session (which has grown considerably since minting), the full corpus resolves: **395 anchors / 401 members, zero failures**, the four new anchors included. An anchor minted during an open session now survives that session continuing — the thing that was impossible when this work started.
- A turn-grouping detail fell out nicely: `8e3f1b7d`'s proposal shares turn `85a8ae44` with `0d5a9e63`'s approval, because the assistant reply proposing the next draft belongs to the user's approval turn. The gate verifies it correctly, since `_turn_message_text` reads the whole turn.
- **`c20260726-6u` resolved.** Slice 1's classifier confirmed `event-1143` (the user's typed command) as the human turn; Slice 4 migrated it to that turn's identity, and it resolves in the acceptance audit. The corpus's one v1-inexpressible member is now expressible.

The closing proof, and the two cases the artifact left open. Both are end-to-end exercises of everything above, not cleanup.

- **ground the five design lines landed this session** — `Event.Grouping`, `Normal.Turn`, and the amendments to `Session.Event.Tape`, `Chatlas.Anchory`, `Chatlas.Session.Model` — by minting v2 anchors against this session's approval turns and tagging the lines. This is the full loop: a live, still-growing session, a tokenized approval turn, a v2 record, a passing `Line.Verbatim.Gate`.
- **resolve `c20260726-6u`** under the Slice 1 classifier and confirm its member. It is the one case in the 397 that v1 structurally could not express, so a correct answer here is the evidence that v2 expresses what v1 could not.
- **Check**: the five lines resolve through `agentos chatlas views inline --anchor <anchor> --filter turns` to their actual approval turns.
- **Check**: re-run the full 397-member audit after the session has grown further; still 397/397, including the anchors minted in this slice.
- **Acceptance**: an anchor minted during an open session survives that session continuing — the exact thing that was impossible when this work started.

### Risks and deviation triggers

- **Live-session churn.** Migration reads materializations that may re-segment mid-pass. Trigger: run migration against sessions quiesced, and re-audit after.
- **Purity regressions elsewhere.** Slice 1 changes what counts as a user turn, which can move existing anchors' targets. Trigger: if the post-Slice-1 audit shows any of the 397 members no longer resolving to a human turn, stop and reconcile before Slice 3.
- **copilot-cli.** Not covered by the corpus. Trigger: if its normalizer has no usable handle, take the synthesized path and record it, do not block.
- **`types` cargo.** Only 3 members carry it; if that grows before Slice 4, extend the migration rather than hand-fixing.

### Acceptance signals

- turn identities stable across re-materialization of an open session (Slice 2 check is the direct answer to the originating defect).
- 397/397 anchors resolve after migration, and continue to resolve after a forced re-materialization.
- default linter output byte-clean; the drift error class is structurally unreachable.
- `primes-utility` corpus: 7 user turns per session on both providers, no injected record among them; `Path.Source.Split.Test` reports no source split on `turn_id`.
- **end test (Slice 7)**: the five design lines this work was designed from are themselves grounded through v2 anchors minted in a live session, and those anchors still resolve after the session grows.

## Impl.Log

- **Deferred grounding.** Five design lines landed this session (`Event.Grouping`, `Normal.Turn`, plus amendments to `Session.Event.Tape`, `Chatlas.Anchory`, `Chatlas.Session.Model`) carry no `Chat.Support.Set`. Minting under v1 against a live session would have created the defect the artifact retires. Promoted to Slice 7: grounding them is the end test, not cleanup.
- **Provisional anchor.** `c20260726-6u` was re-keyed to the event holding the user's typed command arguments, which conflicts with the current `producer.type: human` label on a sibling injected record. Slice 1 decides it, Slice 4 migrates it, Slice 7 confirms it — it is the corpus's one v1-inexpressible member and therefore part of the end test.
- **Pre-existing repair.** The 6 drifted members were amended before this artifact was written, bringing the corpus to a uniform 397/397. That repair is a snapshot under v1, not a fix — it holds only until the next re-segmentation.

### Slice 1

- **Deviation — the corpus harness is stale.** `dev/user-script-invariant-test/validate.py` reports `RED — 10 failing` on every claude session with `envelope leakage: chain_hash, final, source_hash`. Verified pre-existing by stashing the slice change and re-running: identical result. The validator's envelope-key expectation predates the tape-provenance fields, an axis unrelated to purity. **Corrective action taken:** ran the assertion the slice actually names — the acceptance filter — directly against the `primes-utility` corpus. Result: 11/11 sessions, exactly 7 human user turns each, verbatim-identical and in order, on both providers. The purity change does not over-filter. Repairing `validate.py`'s envelope list is out of scope here and belongs to whoever owns the corpus harness.
- **Risk trigger did not fire.** The plan's stop condition was any of the 397 anchor members ceasing to resolve to a human turn after the purity change. Fresh-derivation audit: 397/397 resolve to `producer.type: human`. Execution continues to Slice 2 as planned.
- **Provisional anchor resolved.** `c20260726-6u` → `event-1143` is now the classifier's own answer: the triple resolves `1143 → human`, `1144 → system/skill-body`, `1145 → system/system-reminder`. The earlier re-key stands, no longer on judgement alone. Slice 7 still confirms it under v2.
- **Open.Space.** `agentos-chatlas-py` carries no `.skw` surface, so the executer's code-annotation grounding step has no `Annotation.Point` home. Slice grounding stays in the `Impl.Agendix`; nothing authoritative embedded in code.

### Slices 2–4

- **Codex synthesized fallback was required, not optional.** Rollouts without `internal_chat_message_metadata_passthrough.turn_id` (older captures, and every codex test fixture) produced no turns at all under native-handle-only logic — every event fell to the `session` sentinel. The fallback opens a turn at each user message and names it from the raw record coordinate (`turn-r<record_index>`), which is stable because the raw file is append-only. This is the design's "a provider offering no handle gets a synthesized identity" made concrete.
- **Skill surface realigned — DONE (user-approved follow-up).** `agentos-md/skills/agentos-index` `.skw/src` updated and rebuilt (`link.skw.md`, `back-link.skw.md` → 2 built, `agentos skw check` 0 POIs). Corrections: member refs are `<session-identity>:<turn-id>`; step 2 now says to read `turn_id` off the events an `Event.Pattern` returns, since the pattern language still addresses events while a member addresses the turn; the non-existent `views inline --anchor` is replaced by the real `agentos chatlas anchory resolve <anchor> [--radius N]`; and a note that a proposal and its approval often share one turn, so identical `verbatim_turn`/`approval_turn` refs are legitimate. Both documented resolve forms were run against `c20260728-3u` and verified.
- **Deviation — slice order.** Ran Slice 6 (linter) before Slice 5 (`event_id` retirement). The plan states no dependency between them, and the linter's byte-clean result is the strongest available regression signal, so it was worth having in hand before churning 126 `event_id` consumers.
- **Deviation — view caches do not invalidate on a normalizer change.** `Session.Model.Artifact` views are keyed on raw content, so changing the `Normal.Model` leaves 30k cached `session-model.json` artifacts stale; `agentos chatlas update --trust rebuild` refreshes the session index but not these. **Corrective action taken:** invalidated only the 22 anchor-referenced sessions (via each row's own `depot_path`) and let them re-derive. Full-corpus re-materialization (18G, ~30k views) was deliberately not run — the remaining views are disposable projections that re-derive on demand. Worth a follow-up: view freshness should account for the model's `schema_version`, so a model change invalidates its own corpus instead of relying on a manual pass.
