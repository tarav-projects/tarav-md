# Chatlas2 Hugentic grounding - impl-req

## Impl.Abstract

- **status:** Complete
- **scope:** provide the smallest Chatlas2 grounding records required by the existing Hugentic capture and implementation workflows, then reconnect those workflows without changing the Chatlas2 Normal Model
- **source:** the active Chatlas2 redesign discussion and the current Chatlas/Hugentics implementation
- **authorization:** implement the agreed `Chat.Message.Ref`-first grounding boundary. ^d20260816-20u
- **targets:** `tarav-py/src/tarav/chatlas2/`, runtime Index-reader composition, focused tests, and the canonical Skillware sources for Hugentic grounding routes
- **out of scope:** Normal Model changes, raw normalizer changes, bulk anchor-data migration, Chat.Index redesign, and removal of current Chatlas
- **acceptance:** Hugentic grounding writers can use Chatlas2 for support-only lines, reviewed lines, Issue context, parking notes, and implementation provenance; mixed old/new anchors remain readable during the experiment; all records resolve from current `Chat.Message.Ref` assertions

## Impl.Index

### Grounding.Boundary

- Chatlas2 continues to promise the chronological event tape, event origin, `Chat.Message`, durable message refs, loaded context, and raw fallback.
- Hugentic semantics belong above that boundary. Support, review gates, line attachment, Issue context, and implementation provenance must not become Normal Model concepts.
- Current Chatlas is behavioral evidence: preserve necessary information and validation while redesigning record and CLI vocabulary around `Chat.Message.Ref`.

### Grounding.Records

- A generic message-support record carries an ordered nonempty support set of user `Chat.Message.Ref` assertions. It has no Index-line attachment and serves Impl.Agendix, execution authorization, and Impl.Log provenance.
- A line dossier carries an attachment assertion plus independent `support`, `gates`, and `provenance` relationships.
- Support members are qualifying user messages. Gate proposal and approval members are independently resolved messages: proposal is agent-side, approval is user-side. Tokenized review additionally verifies token presence, explicit approval, order, and materially equivalent line content.
- Provenance retains predecessor anchors and Issue identities. These relationships are consumer semantics over Chatlas2 refs.
- Stored diagnostic `at` remains redundant evidence and never participates in message identity.

### Migration.Boundary

- Keep the `chatlas2` Anchory namespace and `d` prefix while the model matures.
- Existing support-only Chatlas2 line dossiers remain readable; new rich records use an explicit schema revision.
- Runtime readers dispatch by stored application/schema so `c` and `d` anchors can coexist. No persistent migration subsystem is introduced.
- Hugentic managed sources move their grounding instructions to Chatlas2, but chronological Chat.Index mechanics remain current-Chatlas work.

## Execution.Plan

### Slice 1 - Grounding records

- Add RED tests for a generic message-support anchor, rich line relationships, agent/user gate validation, rich batch idempotence, and resolution standing.
- Implement the records and CLI surface inside `tarav.chatlas2`; reuse the canonical Normal Model provider and current message operations.
- Keep support and gate parsing explicit and shallow.
- **check:** focused Chatlas2 Anchory and CLI tests.

### Slice 2 - Mixed readers

- Add Chatlas2 support/review resolvers and line-relationship projection over current Normal Models.
- Compose namespace-aware Index support, review, manifest, and grounding checks at the runtime boundary without introducing a current-Chatlas → Chatlas2 dependency.
- Verify old `c` and new `d` records independently and together.
- **check:** focused Index issues, line manifest, linter, runtime, and Chatlas2 bridge tests.

### Slice 3 - Hugentic routes

- Update canonical Skillware sources for `--link`, agendix, reviewed Index landing, Issue capture, parking notes, implementation design/execute/capture, touched-data reading, search, and capture context.
- Describe target-specific use of generic support anchors versus line dossiers; do not add a second capture engine.
- Build managed outputs from source and verify no capture-grounding producer still instructs agents to mint current-Chatlas turn anchors.
- **check:** Skillware build/check/context plus focused text assertions.

### Slice 4 - Integration

- Run focused Python tests, architecture tests, the Chatlas2 conformance corpus, Ruff on changed Python, Skillware validation, and the broad repository suite proportionate to the final diff.
- Update this artifact with slice standing, deviations, verification, and deferred work.

## Impl.Agendix

- **touched:** the smallest grounding record is determined per Hugentic workflow from existing `Chat.Message.Ref`, not by expanding the Chatlas2 core. ^d20260816-20u
- **design:** `Chat.Message.Ref` is stable place plus current state. `527-chatlas2-normal-model-redesign-design-session.md` → `Chat.Message.Ref`.
- **design:** the canonical Normal Model provider remains the transparent source for all resolution. `527-chatlas2-normal-model-redesign-design-session.md` → `Normal.Model.Cache`.

## Impl.Log

- **2026-08-16 — execution gate:** autonomous development authorized by the current invocation. ^d20260816-20u
- **2026-08-16 — checkpoint deviation:** the generic workflow requests a Git checkpoint, but project policy forbids commits without explicit user instruction; execution proceeds without a commit and preserves all existing dirty changes.
- **2026-08-16 — slice 1:** added generic message-support records plus v2 line dossiers with independent support, gates, and provenance; kept v1 line dossiers readable. A live v1/v2 coexistence trial exposed and fixed a double-normalization bug in equivalence scanning.
- **2026-08-16 — slice 2:** composed mixed `c…`/`d…` support, review, line-manifest, approval, drift, and grounding readers at the runtime boundary without a current-Chatlas reverse dependency.
- **2026-08-16 — slice 3:** migrated canonical Hugentic Skillware grounding instructions across capture, linking, parking, Issue, search, touched-data, and implementation routes; rebuilt all managed outputs. Skillware check returns only the six pre-existing derived-stale advisories and no diagnostics.
- **2026-08-16 — slice 4:** 125 focused integration tests passed; v1/v2 coexistence is covered in Anchory scanning and Index-linter resolution; Ruff is clean; the conformance corpus reports 21 captures and 21 passing artifacts; the full Python suite reports 1,975 passed.
- **2026-08-16 — live grounding trials:** generic message-support registration minted `d20260816-20u`; v2 line-dossier registration minted `d20260816-21u`, resolved its user message as `MATCHED`, and now grounds the active Chatlas2 design line.
- **2026-08-16 — completion:** no Chatlas2 Normal Model or normalizer changes were required. Persistent anchor-data migration and chronological Chat.Index redesign remain outside this implementation.
