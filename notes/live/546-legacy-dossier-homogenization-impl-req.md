# Homogenize The Legacy Anchor Dossiers Into The Chatlas2 Model - impl-req

## Impl.Abstract

- **Status:** Open. Designed and dry-run; not executed.
- **Intent:** Convert every referenced `chatlas` anchor dossier into the `chatlas2` model, so one grounding format remains and nothing needs the legacy resolver.
- **Source:** `527-chatlas2-normal-model-redesign-design-session.md` — *"Anchor records will be transformed operationally when Chatlas2 cuts over. Migration mechanics are written for the actual data at that moment, checked for completeness, and protected by the depot's Git history rather than maintained as a Chatlas2 subsystem."* This is that transformation.
- **Scope:** 2,364 referenced `^c` anchors carrying 4,432 joinable refs across 44 sessions, spanning four repos.
- **Out of scope:** deleting anything, the `chatlas1` consumer cutover (`545`), the tarav-pkg folder migration (`640`), and grounding anything not already grounded.
- **Grounding:** none minted. The index freeze (`638` Invariant 1) is in force.
- **Acceptance:** every referenced anchor resolves in the `chatlas2` namespace with semantics preserved, verified by an exact join rather than asserted; the `chatlas` namespace is left intact.

## Why This Exists

`545` originally planned to keep `chatlas/anchory.py` alive until `640` had read the legacy dossiers through it. That preserved two formats to serve one migration and made the retirement *order* load-bearing — the same coupling that stalled the previous merge.

Converting the data once removes the ordering problem instead of sequencing around it. Afterwards `640` reads one format, `545` Slice 5 becomes an ordinary deletion, and no compatibility resolver is ever written.

**The data is kept.** Migration writes the `chatlas2` namespace and leaves `chatlas` untouched; `anchory-backups/` is the existing precedent.

## Impl.Index

### Migration.Shape

- [DF] `Dossier.Homogenization` is the one-time conversion of legacy `chatlas` anchor dossiers into `chatlas2` records, preserving semantics rather than re-deriving them.
- [DC] The dossier envelope is already identical across namespaces — `attachment`, `relationships.support/gates/provenance`, `at` on every member. Only the member coordinates and `app`/`schema` differ, so this is a member-level rewrite, not a re-grounding.
- [CT] A ref that does not join exactly is reported, never snapped onto the nearest candidate.
- [PR] Because the join key is exact, the run is auditable ref by ref instead of trusted in bulk.
- [RJ] No compatibility resolver and no maintained migration subsystem. The script runs, is checked, and is discarded; git history holds the before state.

### Join.Key

- [DF] `Legacy.Support.Join` maps a legacy `{session, turn_id, turn_hash, at}` ref onto a Chatlas2 coordinate by matching the session, the exact event `started_at`, and the resolved turn text.
- [EX] Text alone is ambiguous: on `^c20260712-21u` the member text `"approve"` matches three user messages in the same session.
- [EX] `at` disambiguates exactly — one candidate's `started_at` matched to the millisecond.
- [EX] Dry run over all 4,432 refs: **2,300 exact, 0 ambiguous, 0 partial.** Wherever the join could be attempted it was exact.

### Side.Asymmetry

- [EX] Every user-side ref joined: `support` 1,877/1,877 and `approval_turn` 423/423 exact.
- [EX] Every agent-side ref failed: `proposal_turn` **423/423** no-join. The failure is categorical, not data quality.
- [DC] The cause is structural: a legacy proposal ref addresses the agent turn's *first* event, and that event frequently belongs to no `Chat.Message` at all — `527` scopes `Chat.Message` to *"the primary user-agent message exchange, not everything the harness renders."*
- [EX] Probed on `c20260803-56u`: the event exists at exactly the legacy `at` with `origin: agent`, sits in **zero** `Chat.Message`, and in **exactly one** agent `Chat.Turn` carrying `turn_address` and `turn_hash`.
- [DC] Therefore a migrated gate's proposal side is a `Chat.Turn` reference and its approval side a `Chat.Message` reference. `527` supports this directly: `Chat.Turn` is *"the semantic blob boundary for that turn's provider data"*, and grounding identifies communicated evidence through `Chat.Message.Ref`.
- [PR] This is a semantic improvement, not a workaround. A gate's proposal *is* an agent turn; expressing it as a message ref was always the weaker fit.

### Blocked.Sessions

- [EX] 9 of 44 sessions do not build in the Normal Model at all, carrying **1,709 refs (39%)**.
- [EX] The dominant cause is `Chatlas2 Codex artifact must contain exactly one native session scope` — a codex artifact holding several `session_meta` records, which chatlas1 reads and chatlas2 refuses. One claude-code session fails artifact recognition separately.
- [DC] This is a Chatlas2 normalizer gap the migration exposed, not a data defect: the sessions are intact and readable by the old model.
- [CT] Fixing `_session_scope` to derive scope positionally cannot move any existing `Event.Address`, because every affected session currently fails to build and therefore has no addresses in use.
- [DC] The migration cannot complete before this is fixed, so it is the first slice.

### Reach

- [EX] Referenced anchors: `tarav-md` 1,867, `tarav-chatlas-md` 423, `tarav-py` 172, `notes/` 13 — 2,364 distinct.
- [DC] `tarav-py`'s 172 are `Skw.Annotation` support on code surfaces, which `640` does not cover. This migration is therefore not a subset of `640`; `640` is a consumer of it.
- [EX] 1,305 of the store's 3,669 dossiers are referenced by nothing. They are neither migrated nor deleted.

## Execution.Plan

### Slice 1 — Teach the Codex normalizer multi-scope artifacts
`lossless/codex.py:_session_scope` fails closed when an artifact carries several `session_meta` records. Derive each record's scope from the `session_meta` in effect at its position instead of requiring exactly one.
**Check:** all 9 previously-unavailable sessions build; a regression test asserts a two-scope artifact normalizes and that each event's address carries its own scope. No address in an already-building session changes — assert that over the conformance corpus.

### Slice 2 — The join, as a reusable read-only resolver
One function: legacy ref → `{status, coordinate}` where status is `EXACT`, `AMBIGUOUS`, `NO_JOIN`, or `SESSION_UNAVAILABLE`. User-side refs resolve to `Chat.Message`, agent-side to `Chat.Turn`.
It reads both models and writes nothing.
**Check:** re-run over all 4,432 refs and publish the status histogram. Target: 4,432 EXACT, 0 otherwise. Anything else is named before slice 3 runs.

### Slice 3 — Gate the proposal side on `Chat.Turn`
The `chatlas2` gate record currently spells both sides as message refs. Admit a turn reference for the proposal side.
**Check:** a migrated gate round-trips through `parse_line_anchor_dossier`; an existing chatlas2 gate is unaffected; `tarav index linter`'s gate check still verifies a live `^d` anchor.

### Slice 4 — Convert, in one auditable run
For each referenced anchor, build the `chatlas2` dossier from the legacy one: same `attachment.triplet_hash`, same provenance, joined support members, joined gates. Write to the `chatlas2` namespace under the anchor's existing id.
**Check:** every written dossier parses; support member count matches the legacy dossier exactly; the run reports converted / skipped / failed and fails loudly rather than partially.

### Slice 5 — Verify against the source surfaces
For a sample across all four repos, resolve each anchor in both namespaces and assert the support text is identical.
**Check:** text equality on the sample; `tarav index linter` unchanged on `tarav-md`; the `chatlas` namespace byte-identical to before.

### Slice 6 — Hand the result to `640` and `545`
Record in both that one format now stands.
**Check:** `640` Slice 1 reads `chatlas2` dossiers only; `545` Slice 5 is unblocked.

## Slice Status

| # | Slice | Status |
|---|---|---|
| 1 | Codex multi-scope artifacts | not started |
| 2 | the join resolver | not started |
| 3 | turn-ref gate proposal side | not started |
| 4 | the conversion run | not started |
| 5 | verify against source surfaces | not started |
| 6 | unblock `640` and `545` | not started |

## Impl.Log

- **Dry run, 2026-08-19.** 2,364 anchors / 4,432 refs / 44 sessions. Result: `exact:support` 1,877, `exact:approval_turn` 423, `no_join:proposal_turn` 423, `new_model_unavailable` 1,709. Zero ambiguous, zero partial.
- The perfect complementarity — user-side 100% exact, agent-side 100% failed — is what identified the cause as structural rather than data quality. A mixed result would have looked like noise and been "fixed" by loosening the join.
- **Deviation from `545`.** `545` framed this as a sequencing constraint (keep the old resolver until `640` reads through it). The user rejected that in favor of migrating the data. `545`'s `Dossier.Homogenization` block records the change; this artifact is its execution.
- **`Index.Presumption`:** slice 1 is assumed safe for existing addresses because affected sessions do not currently build. Verified by reasoning, not yet by running the conformance corpus against the change.
- **`Index.Presumption`:** the 1,305 unreferenced dossiers are assumed to be genuinely orphaned rather than referenced by a surface the scan missed. The scan covered `*.md` and `*.py` across the project excluding `.skw/`, `_DEPRECATED`, and `.git`.
- **Waiver:** no anchors minted and no backpropagation attempted, per the index freeze.
