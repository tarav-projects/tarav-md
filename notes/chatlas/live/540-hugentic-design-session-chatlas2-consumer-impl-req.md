# Hugentic Design.Session Chatlas2 consumer - impl-req

## Impl.Abstract

- **scope:** reconnect the smallest real Hugentic consumer—`--capture --design-session` transcript reading and line grounding—to Chatlas2 Views, Chat.Message lookup, and Chatlas2 Anchory
- **status:** implemented and verified; implementation remains uncommitted after checkpoints `10940b9`, `867e750`, and `009184e`
- **source:** the explicit autonomous implementation invocation in Codex session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`
- **targets:** the Skillware source of `Hugentic.Capture.Workflow.Module` and `Design.Session.Knowledge.Module`, their compiled skill surfaces, one real Chatlas2-backed line in the active Chatlas2 design session, and maintained design records
- **out of scope:** changing the shared ontology/appendix/agendix linking route; replacing current Chatlas session discovery; porting `Capture.Plan`, Chat.Index, replay, zip-transcript, gates, reconciliation, or every existing anchor; adding a compatibility shim or migration subsystem
- **acceptance:** an agent loading `--capture --design-session` is explicitly directed to read `user`/`transcript` through Chatlas2, locate exact user support as `Chat.Message.Ref`, batch-register final lines through Chatlas2 Anchory, and verify the resulting `d…` references; the managed skill builds cleanly and one existing design line is manually exercised end to end

## Impl.Agendix

- **touched (authorization):** autonomously migrate the next minimal consumer after the initial Chatlas2 Views slice. ^c20260816-24u
- **touched (design):** `Chatlas2.Views` is a disposable public read projection over the canonical Normal Model. `527-chatlas2-normal-model-redesign-design-session.md` → `Chatlas2.Views` ^c20260816-23u
- **touched (design):** `Chat.Message.Ref` couples stable message place with current message state and resolves against the current model. `527-chatlas2-normal-model-redesign-design-session.md` → `Chat.Message.Ref` ^c20260815-46u
- **touched (design):** the first Chatlas2 Anchory consumer stores exact user-message refs in an isolated `chatlas2` namespace. `534-chatlas2-design-session-support-impl-req.md`
- **structural:** `references/design-session.skw.md` is the canonical managed source for the compiled Design.Session landing specialization; direct target edits are forbidden

## Impl.Index

### Consumer boundary

- migrate only the Design.Session target specialization; the shared `Anchory.Link.Operation.Module` remains the current-Chatlas route for reviewed Index and agendix consumers
- current-session discovery may continue through `tarav-chatlas-my-session-id` because it is discovery mechanics, not Normal Model semantics
- after session resolution, Design.Session capture reads `tarav chatlas2 views get --view user`; it escalates to `transcript` only when primary exchange context is required
- exact support discovery uses `tarav chatlas2 messages find --side user`; its returned `member_ref` is the complete `{session, message_address, message_hash}` assertion rendered as CLI sugar

### Landing and failure behavior

- one-line landing may use Chatlas2 Anchory preview/register directly; a multi-line landing uses one `tarav.chatlas2.anchor-batch.v1` preview/register pass with exact final typed bodies and stable client IDs
- returned `d…` anchors are attached to the Design.Index lines and verified through `tarav chatlas2 anchory resolve`
- unsupported or unresolved Chatlas2 evidence does not silently fall back to old turn-based grounding; the material remains in `Session.Notes` and the retained raw archive remains available for inspection
- no historical anchor fleet is migrated; the trial deliberately rewrites exactly one already-touched Design.Session line so Git provides the comparison boundary

### Existing dirty state

- the mandatory checkpoints will capture the completed uncommitted Chatlas2 Views slice in `tarav-py` and its design documentation in `tarav-chatlas-md`
- `tarav-md` also contains pre-existing user-owned `tarav-live-surfaces` Skillware changes; the execution workflow requires the dirty repository checkpoint to preserve all of them without alteration

## Execution.Plan

### Vertical.Slice 1 - RED managed consumer contract

- prove the compiled Design.Session specialization contains no Chatlas2 read/grounding instructions
- add the minimum target-specific route to `capture.skw.md` and `design-session.skw.md`, including the exact Views, message lookup, batch schema, registration, resolution, and no-fallback semantics
- observable: a cold agent can execute the Design.Session route without consulting the old turn-based linking pipeline
- check: targeted source/compiled assertions, Skillware build, context audit, and package check

### Vertical.Slice 2 - Real line grounding trial

- locate the user message that authorized `Chatlas2.Views` through the new Chatlas2 message path
- preview/register the existing `Chatlas2.Views` design line with the returned Chat.Message member ref, replace only that line's old support anchor with the returned `d…` anchor, and resolve it after the edit
- observable: one maintained Design.Session line is backed by a MATCHED user Chat.Message.Ref and its stored attachment assertion agrees with the final line
- check: Chatlas2 Anchory resolve, exact line inspection, and Markdown diff check

### Vertical.Slice 3 - Reconciliation and regression

- record the implemented consumer boundary in the active design session and this Impl.Req
- verify the Hugentics managed skill, focused Chatlas2 suite, architecture checks, conformance corpus, full repository tests proportionate to changed Python state, Ruff/diff checks, and Git status
- observable: Design.Session uses Chatlas2 while other capture destinations and current Chatlas mechanics remain unchanged
- check: Skillware status/check, pytest, corpus verify/check, and final diff review

## Impl.Log

- **2026-08-16 — execution gate:** autonomous design and execution are authorized and grounded as `^c20260816-24u`
- **2026-08-16 — inspected boundary:** the shared capture workflow delegates landing to `Design.Session.Knowledge.Module`, but that specialization still describes exact current-Chatlas user turns and an unspecified anchor batch; the common link module remains deeply turn/gate-oriented and must not be switched for unrelated consumers
- **2026-08-16 — Skillware baseline:** `tarav-hugentics` is fully managed from `.skw/src`; its package check has six pre-existing derived-stale advisories outside the Design.Session and capture targets
- **2026-08-16 — managed route:** the capture module now delegates Design.Session chat semantics explicitly, while the Design.Session module specifies the exact Chatlas2 user/transcript Views, message lookup, one/batch registration, resolution, and no-fallback behavior; the shared link module is unchanged
- **2026-08-16 — Skillware reconciliation:** the first build exposed malformed note syntax and expected derived drift in dependent digests; the annotations were corrected and the directly affected capture/root derivations were re-derived, returning the package to its exact six-POI baseline
- **2026-08-16 — real workflow trial:** Chatlas2 `user` view returned 127 current-session user messages; exact lookup selected one qualifying `Chat.Message.Ref`, registration minted `d20260816-18u`, read-back returned `MATCHED`, user-side, and `at_matches=true`, the stored attachment hash agreed with the final line, and repeated registration reused the same anchor
- **2026-08-16 — design capture:** the implemented consumer boundary itself was grounded through the new route as `d20260816-19u`
- **2026-08-16 — verification:** all 1,967 repository tests pass; focused Chatlas2 plus architecture coverage passes 66 tests; all 21 conformance captures verify and normalize; Skillware context resolution succeeds and its check retains exactly the six pre-existing advisory IDs with no new POIs; focused Ruff and all repository diff checks pass. Repository-wide Ruff remains blocked only by the pre-existing unused `local_storage_paths` import in `src/tarav/skills/routing.py`
- **2026-08-16 — blocker standing:** none
