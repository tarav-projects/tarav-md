# Chatlas2 Claude human-origin recovery - impl-req

## Impl.Abstract

- **scope:** recover three audited Claude human-input forms—accepted suggestions, typed list content, and legacy-shaped user records inside prompt-source-capable artifacts—and classify timed Claude records as `Unresolved.Event` whenever neither user-side nor agent-side origin can be asserted
- **status:** implemented and verified; implementation remains uncommitted after recovery checkpoints `da6bba8` and `a4b1e36`
- **source:** full active Raw Archive audit plus the explicit autonomous develop invocation in Codex session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`
- **target:** Claude Chatlas2 normalizer, focused normalization tests, conformance checks, and maintained Chatlas2 guidance
- **out of scope:** normalizing untimed `last-prompt`; asserting origin for ambiguous `queue-operation` or unmatched attachments; adding a new Normal Model concept; redesigning the provider-neutral event or message schema; changing Codex normalization
- **acceptance:** every audited direct human input becomes a `User.Event` and user `Chat.Message`; known assistant/harness records remain `Agent.Event`; ambiguous timed records become `Unresolved.Event`; existing message identity, chronological union, raw-evidence, and loaded-context behavior remains valid

## Impl.Agendix

- **touched (authorization):** execute the audited Claude human-origin repair autonomously. ^c20260816-20u
- **touched (design):** origin is asserted only when the user-side or agent-side boundary is established; uncertainty remains unresolved. `527-chatlas2-normal-model-redesign-design-session.md` → `Chatlas2.Event.Origin` ^c20260815-2u
- **touched (design):** Chatlas2 provides the complete primary user/agent `Chat.Message` projection. `527-chatlas2-normal-model-redesign-design-session.md` → `Chat.Message` ^c20260815-7u
- **touched (design):** raw-version partitions keep mappings simple, while one supported family may declare optional fields at stable paths. `527-chatlas2-normal-model-redesign-design-session.md` → `Raw.Model.Recognition` ^c20260815-54u
- **structural:** the prompt-source-capable Claude artifact may contain legacy-shaped records; record-local structural evidence selects the applicable direct mapping without changing artifact provenance

## Impl.Index

### Human-input recognition

- `promptSource=suggestion_accepted` is a primary user message when Claude explicitly records `origin.kind=human`
- `promptSource=typed` or `queued` accepts string content or list content containing textual blocks; text blocks form the provider-neutral transcript projection while the retained raw artifact remains the escape hatch for images and richer blocks
- inside a prompt-source-capable artifact, a user record with no `promptSource` uses the existing legacy direct-message mapping; records carrying a prompt source never fall through to legacy inference
- message address remains the native Claude record UUID and message hash remains derived from its member event state

### Conservative origin

- recognized primary inputs and explicit human-origin records are `User.Event`
- assistant output and structurally identified Claude harness/system/tool records are `Agent.Event`
- ambiguous timed records—including originless queue operations and unmatched attachments—are `Unresolved.Event`, not guessed agent-side
- unresolved events remain chronologically retained and referenceable but do not become `Chat.Message` members

## Execution.Plan

### Vertical.Slice 1 - RED human-input variants

- add focused failing tests for accepted suggestions, typed text-plus-image content, and legacy-shaped direct messages inside a prompt-source-capable artifact
- observable: each audited form is absent or agent-classified before implementation
- check: run the focused Claude test selection and confirm the expected assertion failures
- status: complete

### Vertical.Slice 2 - Direct recognition and conservative origin

- add the minimum record-local Claude predicates and text projection needed by the three mappings
- replace the Claude default-agent fallback with explicit user, explicit agent, and unresolved classification
- observable: audited human records produce user events/messages; ambiguous attachment and queue-operation records remain unresolved; known assistant/system/tool behavior remains agent-side
- check: focused Claude pipeline tests and complete Chatlas2 test suite
- status: complete

### Vertical.Slice 3 - Archive and documentation reconciliation

- re-run the supported Claude conformance corpus and an active-archive classification audit over explicit human markers
- update architecture, agent guidance, and the active Chatlas2 design session with the implemented boundary
- observable: no audited explicit human record remains agent-classified, no corpus capture regresses, and guidance matches implementation
- check: corpus verification, repository suite, Ruff, Skillware, and Git diff checks
- status: complete

## Impl.Log

- **2026-08-16 — execution gate:** autonomous development is authorized and grounded as `^c20260816-20u`
- **2026-08-16 — audit baseline:** Claude has 21 unique accepted-suggestion records, 10 unique typed list-content records, and 589 unique legacy-shaped direct messages in prompt-source-capable artifacts that the current normalizer does not project as user messages
- **2026-08-16 — design decision:** preserve the existing two opaque Claude raw-version identities; the prompt-source-capable family handles its observed optional legacy-shaped records through their own discriminator rather than inventing a version axis or changing stable addresses
- **2026-08-16 — RED/GREEN:** three focused regressions first failed on missing human variants, missing mixed-family recovery, and guessed agent origins; all 15 Claude pipeline tests pass after the direct mappings and explicit origin resolver
- **2026-08-16 — archive deviation:** the first mixed-family fallback also selected 154 unique `isMeta` harness records; a second RED regression narrowed fallback to the audited non-meta human set
- **2026-08-16 — archive verification:** 21 accepted-suggestion observations, 12 typed-list observations, 665 mixed legacy-direct observations, and 177,466 ambiguous timed observations across 6,025 retained Claude artifacts all resolve to their intended user/message or unresolved standing with zero failures
- **2026-08-16 — conformance:** all 21 registered captures verify and normalize; the complete Chatlas2 plus architecture suite passes 65 tests
- **2026-08-16 — live trial:** forced normalization of Claude session `890050c4-9473-4b4f-ab2f-a67c54d57894` now returns the previously absent accepted suggestion `enhance the skill then commit all` exactly once as a user `Chat.Message`
- **2026-08-16 — repository verification:** all 1,966 tests pass; focused Ruff and diff checks pass; Skillware reports 30 pre-existing POIs and none target Chatlas2. Repository-wide Ruff remains blocked only by the pre-existing unused `local_storage_paths` import in `src/tarav/skills/routing.py`
- **2026-08-16 — blocker standing:** none
