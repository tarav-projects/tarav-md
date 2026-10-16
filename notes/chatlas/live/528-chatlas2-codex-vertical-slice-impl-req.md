# Chatlas2 Codex Vertical Slice - impl-req

## Impl.Abstract

- **scope:** implement the first executable Chatlas2 vertical slice for Codex: raw-model recognition, one compatible normalizer, loss-preserving multi-artifact assembly, minimal event origin, `Chat.Message`, conservative `Agent.Loaded.Context`, source references, commit metadata, and one-session JSON inspection
- **status:** implemented and verified
- **source:** `527-chatlas2-normal-model-redesign-design-session.md` plus autonomous develop invocation ^c20260815-26u
- **target:** `tarav-py`, using the maintained `tarav.chatlas2` namespace
- **out of scope:** providers other than Codex; migration or mutation of current Chatlas; persistent Chatlas2 artifacts; rich event classes, turns, forks, compaction semantics, or complete context reconstruction
- **acceptance:** the public CLI builds an inspectable model from every recognized Codex transcript artifact recorded for one current-Chatlas session, keeps uncertain observations, exposes complete recognized `Chat.Message`s, and never creates a current-Chatlas → Chatlas2 dependency

## Impl.Agendix

- **touched (chat / execution gate):** the autonomous `--impl --dev --AUTO` invocation authorizes this complete design-and-execute pass ^c20260815-26u
- **touched (chat / system boundary):** Chatlas2 is parallel, may reuse current Chatlas mechanics, and must not be imported by current Chatlas ^c20260814-12u ^c20260814-13u ^c20260814-14u ^c20260814-15u
- **touched (chat / normal model):** chronological retained union, all relevant fragments, retention-biased deduplication, event-start timing, and completeness over consistency ^c20260814-16u ^c20260814-17u ^c20260814-18u ^c20260814-19u ^c20260814-20u
- **touched (chat / recognition):** structural version recognition returns a Chatlas version or null; dispatch only reaches a compatible normalizer; output metadata records `commit` ^c20260814-21u ^c20260814-22u ^c20260814-23u ^c20260814-24u ^c20260814-25u ^c20260814-26u
- **touched (chat / semantic floor):** resolved origins are `User.Event` or `Agent.Event`; uncertain origin remains `Unresolved.Event` ^c20260815-0u ^c20260815-1u ^c20260815-2u ^c20260815-3u
- **touched (chat / projections):** `Chat.Message` and `Agent.Loaded.Context` are groupings over the event tape, with context membership conservative under uncertainty ^c20260815-4u ^c20260815-5u ^c20260815-6u ^c20260815-7u ^c20260815-8u ^c20260815-17u ^c20260815-18u ^c20260815-19u ^c20260815-20u ^c20260815-21u ^c20260815-22u ^c20260815-23u ^c20260815-24u
- **touched (index):** `Raw.Archive`, `Chatlas.Session.Index`, and `Normalization.Pipeline::Chatlas.Session.Model` define the reusable archive/index boundary; `Dependency.Profile.Split`, `Vertical.Slice`, and `Test.At.Boundaries` govern package direction and verification
- **structural:** this request is the implementation handoff derived from `notes/live/527-chatlas2-normal-model-redesign-design-session.md`; the live session remains design evidence, not a runtime dependency
- **open space:** exact v1 JSON field names and conservative Codex call-boundary inference remain provisional implementation choices, bounded by the captured promises and public tests

## Impl.Index

### Chatlas2.Package.Boundary

- create one isolated `tarav.chatlas2` package inside the maintained modular monolith
- Chatlas2 may import current Chatlas selection and archive mechanics
- current `tarav.chatlas` must not import `tarav.chatlas2`
- runtime composition may register both public command surfaces

### Chatlas2.Normal.Model.V1

- the canonical spine is one chronologically sorted `events` array
- every recognized raw Codex record is retained in an event; minimally parsed origin is `user`, `agent`, or `unresolved`
- exact duplicate observations collapse only when raw content and provider record position agree across artifacts
- collapsed events retain every raw source observation; uncertainty creates another event
- top-level annotations hold `chat_messages` and `agent_loaded_contexts` groupings over event ids
- model metadata contains only the producer `commit`; each source records its recognized raw model version or unrecognized standing

### Codex.Raw.Model.V1

- the versioner recognizes a structural Codex rollout JSONL envelope and returns one stable Chatlas-assigned version or null
- the Codex normalizer explicitly declares that one supported version
- input-like Codex records are accumulated conservatively for the next contiguous generated-output group
- a loaded-context membership is emitted only for inputs that the raw sequence supports as available; missing context is preferred to speculative membership
- non-message raw records remain on the tape even when no higher-resolution annotation is produced

### Chatlas2.Inspection.Surface

- `tarav chatlas2 normalize` selects exactly one Codex session through current `Chatlas.Session.Index`
- `--session-id` or `--identity-hash` identifies the session
- `--json` emits the complete Normal Model; text mode emits a compact count summary
- unrecognized transcript artifacts remain listed as source references and are never silently presented as normalized coverage

## Execution.Plan

### Slice 1 - Establish the Codex model boundary

- add boundary tests for structural version recognition, minimal event origin, and conservative context membership
- implement the Chatlas2 model types plus Codex v1 versioner and compatible normalizer
- observable: a raw Codex rollout fragment becomes a chronological model fragment with events, message groups, loaded-context groups, and raw observations
- check: RED then GREEN focused tests under `tests/chatlas2/`
- risk: classifying harness-injected role-user messages as human; resolve only known Codex message shapes and leave unknown origins unresolved
- status: complete

### Slice 2 - Assemble every archived Codex transcript

- collect transcript artifacts from the selected row and all archived versions instead of reading `primary_backing_artifact`
- dispatch each recognized fragment, merge exact same-position observations, retain uncertain duplicates, and sort by event start time
- observable: two archived Codex rollouts with an overlapping prefix produce one prefix plus the complete continuation, with both sources attached to collapsed prefix events
- check: RED then GREEN public pipeline test; assert chronology, retention, source observations, `Chat.Message`, and conservative context results
- risk: one path appearing through several archive versions; deduplicate source paths before normalization
- status: complete

### Slice 3 - Expose and document the vertical slice

- register the isolated `chatlas2 normalize` command at the runtime composition root
- add a public CLI boundary test using an isolated current-Chatlas archive/index
- update `ARCHITECTURE.md`, `AGENTS.md`, and `tests/test_architecture.py` for the new namespace and one-way dependency
- observable: `tarav chatlas2 normalize --session-id <codex-id> --json` emits the complete inspectable model
- check: focused Chatlas2 suite, architecture suite, Ruff, Skillware project check, and a live read against the current Codex session
- deviation trigger: if current Chatlas cannot expose every archived transcript without mutation, stop before inventing a second archive reader
- status: complete

## Impl.Log

- **2026-08-15 — execution gate:** autonomous design and execution authorized ^c20260815-26u
- **2026-08-15 — design-reality deviation:** the request named `agentos.chatlas2`, but the maintained distribution is installed from `src/tarav`; implementation uses `tarav.chatlas2` so the package is real and architecture-testable rather than an uninstalled sibling namespace
- **2026-08-15 — checkpoint:** the mandated pre-edit checkpoint was recorded at commit `a54e0b332e3a7904872b3bbfd6c2de722f1f7f83`; all Chatlas2 implementation changes remain uncommitted after that boundary
- **2026-08-15 — slice 1:** added the Codex structural versioner, exact compatibility declaration, minimal event classes, raw observations, `Chat.Message`, and conservative `Agent.Loaded.Context`; the focused model tests passed
- **2026-08-15 — slice 2:** assembly now reviews the selected row plus every archived version, deduplicates transcript paths, merges only exact same-position observations, and sorts by event-start timestamp; overlapping-prefix and uncertainty-retention tests passed
- **2026-08-15 — slice 3:** registered `tarav chatlas2 normalize`, added CLI and one-way architecture tests, documented the experiment, and grounded every new code surface through Skillware dependencies
- **2026-08-15 — verification:** 39 Chatlas2, architecture, archive/index selection, and identity tests passed; Ruff passed; the five new Skillware dependency findings were resolved, leaving only unrelated pre-existing project POIs
- **2026-08-15 — live inspection:** the current indexed Codex session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8` produced 1 recognized source, 1,976 chronological events, 135 `Chat.Message`s, and 401 conservative context annotations; every annotation reference and raw source reference resolved. The earlier `a80aca81-3174-4b84-8574-97a9216b8a42` session was not present in the currently configured index, so it was not used as the live fixture
- no blockers
