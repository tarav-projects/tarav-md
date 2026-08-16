# Hugentics Current-Chat Grounding - impl-req

## Impl.Abstract

- **Status:** Implemented and verified.
- **Scope:** Make the current agent chat context the default understanding source for Hugentic chat-backed capture, while using Chatlas2 only to resolve and validate the specific messages selected as evidence.
- **Source alignment:** The current discussion established that transcript reconstruction duplicates context the agent already has; transcript and `Chat.Turn` reads are escalation paths for ambiguity, missing compacted context, explicit historical work, or failed exact lookup.
- **Target:** The managed `tarav-hugentics` Skillware sources and their compiled runtime surfaces.
- **Out of scope:** New Chatlas2 model or CLI primitives, capture cursors, historical-session capture redesign, Anchory schema changes, and changes to Hugentic semantic judgment or landing gates.
- **Acceptance:** A cold agent following Design.Session capture drafts from current context, selects qualifying visible user messages, resolves only those messages to `Chat.Message.Ref`, and does not read the full user/transcript View unless an explicit escalation condition holds.

## Impl.Index

### Current.Chat.As.Understanding.Source

- The live conversation already supplies the default material from which the agent understands the discussion, identifies design deltas, and selects qualifying support.
- Chatlas2 is not the default reconstruction layer for a current-chat capture. Its grounding job begins after semantic support has been selected.
- The minimum path is: understand current context → draft final lines → select visible qualifying user messages → resolve exact `Chat.Message.Ref` members → preview/register one Anchory batch → patch → verify `MATCHED`.

### Escalation

- Read a bounded Chatlas2 message neighborhood or containing `Chat.Turn` when exact message lookup is ambiguous or more associated material is required.
- Read broader transcript projections only when compaction removed necessary context, the selected evidence cannot be resolved from the visible chat, or the user explicitly requests historical capture.
- Raw artifacts remain the final diagnostic fallback; escalation does not change which messages qualify semantically.

### Workflow.Ownership

- Hugentics retains interpretation, evidence qualification, line synthesis, gates, target-specific landing, and artifact mutation.
- Chatlas2 retains exact message lookup, stable references, optional turn expansion, Anchory registration, and drift resolution.
- Apply the rule in the shared linking primitive and Design.Session specialization so later capture targets inherit the same minimal default without duplicating procedure.

## Impl.Agendix

- **Execution authorization:** the current user request, `nice, implement`, in the current Chatlas session, grounded as generic Chatlas2 message support `d20260816-38u`.
- **Touched workflow:** `skills/tarav-hugentics/.skw/src/references/design-session.skw.md`.
- **Shared grounding primitive:** `skills/tarav-hugentics/.skw/src/references/link.skw.md`.
- **Shared capture framing:** `skills/tarav-hugentics/.skw/src/references/capture.skw.md` and, only if needed for global discoverability, `.skw/src/SKILL.skw.md`.

## Execution.Plan

### Vertical.Slice.1 — Current-chat-first grounding contract

- **Status:** Complete.
- **RED:** Demonstrate that the existing Design.Session and linking instructions unconditionally direct the agent to read the complete user View before support selection.
- **GREEN:** Rewrite the managed source so current context supplies understanding and selected visible user messages are resolved directly through `messages find`; name bounded neighborhood, `Chat.Turn`, transcript, and raw reads only as escalating fallbacks.
- **Check:** Search the compiled workflow for unconditional transcript-read instructions and inspect the complete current-chat-first route.

### Vertical.Slice.2 — Managed build and reconciliation

- **Status:** Complete.
- **GREEN:** Build the `tarav-hugentics` Skillware package, inspect generated diffs, and keep source and runtime wording aligned.
- **Check:** Run `tarav skw check --skill skills/tarav-hugentics`, targeted context projection where applicable, and `git diff --check`.
- **Acceptance signal:** The runnable skill describes the minimum workflow without requiring transcript reconstruction, while preserving the existing Chatlas2 message-ref, Anchory batch, landing, and verification contracts.

## Impl.Log

- **2026-08-16:** Produced from the current-chat grounding discussion. No new Chatlas2 mechanics are required for this pass.
- **2026-08-16:** Grounded execution authorization as `d20260816-38u` and checkpointed the complete pre-execution repository state as `e7bc70f`.
- **2026-08-16:** RED confirmed that both Design.Session capture and the shared linking primitive unconditionally instructed the agent to read the complete user View before resolving evidence.
- **2026-08-16:** Replaced that path with current-context understanding, selected-message resolution, and explicit escalation to `Chat.Turn`, Views, or raw artifacts only when necessary. Clarified that legacy chronological `Chat.Index` materialization occurs after semantic work and is not an understanding source.
- **2026-08-16:** Built all managed surfaces successfully. Skillware context projection for `references/design-session.md` passed; touched targets report no drift. Package check retains six pre-existing `Derived.Stale` advisories on unrelated alignment/implementation modules.
