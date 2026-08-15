# Chatlas2 Normal Model Redesign - design-session

## Session.Abstract

- **Intent:** Redesign Chatlas normalization from first principles around complete retained data, a simple chronological event tape, and a small reliable semantic promise.
- **State:** Active design — the semantic floor, raw-version recognition boundary, first implementation slice, and conformance corpus are in place; durable reference design is active.
- **Scope:** Chatlas2 system boundary, Normal Model floor, raw-model recognition and dispatch, event origin, `Chat.Message`, `Agent.Loaded.Context`, stateless durable references, and progressive resolution.
- **Predecessor:** `509-session-model-design-session.md` records the older, more ambitious model. It is prior design evidence, not inherited Chatlas2 truth.
- **Landing:** This is a live Design.Session. Nothing here is promoted to the stable Chatlas Index by this capture.
- **Next:** Define provider-specific `Event.Address` and `Event.Hash` recipes, then extend the same location-plus-state pattern to `Chat.Message.Ref`.

## Design.Index

### Chatlas2.System

- [DF] `Chatlas2.System` is the parallel experimental system in which the new Chatlas model can mature without constraining current Chatlas. ^c20260814-12u
- [CT] Chatlas2 may depend on current Chatlas code; current Chatlas must not depend on Chatlas2 code. ^c20260814-13u
- [PR] Chatlas mechanics may be reused freely, while inherited semantic judgments are reviewed and may be redesigned or reimplemented. ^c20260814-14u
- [DC] The existing lossless `Raw.Archive`, safe provider discovery and capture, and session identity primitives remain available to Chatlas2. ^c20260814-15u
- [PR] Chatlas2 keeps its CPU implementation deliberately simple; agents may inspect the retained raw artifacts when they need resolution beyond the Normal Model. ^c20260815-16u

****

### Chatlas2.Normal.Model

- [DF] `Chatlas2.Normal.Model` is a provider-neutral, loss-preserving chronological event tape with a deliberately shallow semantic floor. ^c20260814-16u
- [DC] Normalization reviews every retained artifact or independently parseable fragment that may contain otherwise-lost session data; no primary artifact decides what survives. ^c20260814-17u
- [CT] Deduplication fails toward retention: observations are collapsed only when they can be shown to describe the same event; uncertainty preserves both. ^c20260814-18u
- [DC] An event's tape timetag is when the event starts; later observations may add data to that event without changing its start position. ^c20260814-19u
- [PR] Data completeness has priority over total consistency; richer semantic resolution can be added later without discarding the retained event data. ^c20260814-20u

****

### Raw.Model.Recognition

- [DF] `Raw.Model.Versioner` inspects raw structure and content, returns one stable Chatlas-assigned `Raw.Model.Version` or null, and performs no semantic normalization. ^c20260814-21u
- [CT] Provider or CLI versions may inform recognition but never define `Raw.Model.Version` by themselves. ^c20260814-22u
- [DC] A `Raw.Normalizer` declares exactly which `Raw.Model.Version` values it supports and runs only after successful version recognition. ^c20260814-23u
- [DC] Recognition and normalization operate on the smallest independently parseable raw fragment, allowing one session to contain several raw model versions. ^c20260814-24u
- [PR] Versioners evolve with the Normal Model: they recognize only the distinctions required by the model's current reliable promises. ^c20260814-25u
- [DC] Normal Model metadata records the producing repository's last Git commit under the future-proof field name `commit`; no stronger reproducibility model is required initially. ^c20260814-26u

****

### Chatlas2.Event.Origin

- [DF] `Chatlas2.Event.Origin` has two resolved structural types, `User.Event` and `Agent.Event`; `Unresolved.Event` is the preservation state when neither side can be asserted safely. ^c20260815-0u
- [DC] `Agent.Event` deliberately collapses assistant, model, harness, tool, runtime, compaction, and context distinctions at the structural level. ^c20260815-1u
- [CT] Origin is asserted only when the user-side or agent-side boundary can be established; otherwise the event remains unresolved rather than being guessed into a side. ^c20260815-2u
- [DC] Chatlas2's main semantic promise is correct user-side versus agent-side classification whenever it claims that distinction. ^c20260815-3u

****

### Chat.Message

- [DF] `Chat.Message` is an event or event grouping belonging to the primary user-agent message exchange, not everything the harness renders to the user. ^c20260815-4u
- [DC] Every `User.Message` is represented over one or more `User.Event` members. ^c20260815-5u
- [DC] Every `Agent.Message` is represented over one or more `Agent.Event` members. ^c20260815-6u
- [DC] Chatlas2 always provides the complete `User.Message` and `Agent.Message` projection because these are the messages the user sees and reacts to. ^c20260815-7u
- [DC] `Chat.Message` membership is modeled as an annotation or grouping over the event tape rather than as another canonical spine. ^c20260815-8u

****

### Agent.Loaded.Context

- [DF] `Agent.Loaded.Context` is the grouping of events that normalization determines were available to contextualize a specific generated `Agent.Event`. ^c20260815-17u
- [DC] For a generated `Agent.Event`, its `Agent.Loaded.Context` answers which context was used for the corresponding LLM call. ^c20260815-18u
- [DC] Membership asserts that an event was available to the LLM call; it does not assert that the agent noticed or used the event. ^c20260815-19u
- [CT] Normalization constructs each context grouping from the provider transcript and evidence about how that provider forms its LLM calls. ^c20260815-20u
- [PR] Context membership is conservative: an incomplete grouping is preferable to false-positive membership. ^c20260815-21u
- [CT] A context grouping may contain most preceding events, but the model imposes no size or prefix constraint on it. ^c20260815-22u
- [RJ] `Agent.Loaded.Context` does not introduce an `Agent.Execution` concept; it associates directly with the generated `Agent.Event`. ^c20260815-23u
- [RJ] `Normal.Context.Blob` is not part of the model; `Agent.Loaded.Context` groups the minimally parsed events already retained on the tape. ^c20260815-24u

****

### Event.Ref

- [DF] `Event.Address` is a stable, opaque, provider-derived logical event place; it excludes event content and chronological presentation position. ^c20260815-37u
- [DF] `Event.Hash` is a digest assertion over an event's currently normalized content; it excludes address, annotations, native identifiers, and provenance. ^c20260815-38u
- [DF] `Event.Ref` is `{event_address, event_hash}`: it couples stable logical place with a current-state assertion and carries drift validation. ^c20260815-39u
- [CT] Chatlas2 normalization is stateless: current raw artifacts produce the current Normal Model without maintaining normalized state across runs. ^c20260815-40u
- [DF] `Event.Ref.Resolution` is Chatlas's comparison of a stored `Event.Ref` with the currently presented Normal Model. ^c20260815-41u
- [DC] `Event.Ref.Resolution` is `MATCHED` when address and hash agree, `AMENDED` when the address exists with a different current hash, and `MISSING` when the address is absent. ^c20260815-42u
- [DC] Chatlas presents the resolution standing; each consumer decides what policy to apply to it. ^c20260815-43u
- [RJ] Chatlas2 does not retain earlier normalized event states merely to explain amendments; historical artifact debugging belongs to the Raw Archive's Git history. ^c20260815-44u

****

### Chatlas2.Progressive.Resolution

- [DF] `Chatlas2.Progressive.Resolution` is the optional layer of classes, annotations, and groupings added over preserved events as reliable needs emerge. ^c20260814-27u
- [FR] Event classes such as `user.message`, `user.interrupt`, and `agent.message` may be added when their resolution becomes useful and reliable. ^c20260815-9u
- [CT] `User.Turn` and `Assistant.Turn` are optional derived groupings: they may be partial, incomplete, or fuzzy and are not part of the completeness promise. ^c20260815-10u
- [PR] Later resolution enriches the event tape without replacing its retained data, chronological order, or origin assertions. ^c20260814-29u

****

## Session.Notes

- Current Chatlas remains the raw-archive and session-recovery substrate while Chatlas2 matures.
- Provider-native raw artifacts remain the inspection escape hatch when the Normal Model does not yet expose needed resolution.
- The event tape is the completeness spine. Classes, messages, loaded contexts, turns, forks, compactions, and other interpretations are overlays.
- Open: define provider-specific logical-place recipes for `Event.Address`, current-state inputs for `Event.Hash`, and proof rules for folding same-address observations within one normalization run.
- Open: define `Chat.Message.Address`, `Chat.Message.Hash`, and `Chat.Message.Ref` from the same location-plus-state pattern without importing turn-level ambitions.
- Open: define provider-specific reconstruction rules and fixtures for `Agent.Loaded.Context` membership and completeness.
- Open: extend the conformance corpus with each supported provider and `Raw.Model.Version` as compatible versioners and normalizers are added.

## Session.Log

- **2026-08-14:** Traced lost normalized turns to primary-artifact selection and chose all-artifact review, chronological union, and retention-biased deduplication.
- **2026-08-14:** Settled the explicit `Raw.Model.Versioner` recognition and `Raw.Normalizer` dispatch boundary, plus the parallel Chatlas2 system direction.
- **2026-08-15:** Reduced the semantic floor to user-side versus agent-side event origin and the `Chat.Message` projection; kept richer interpretation progressive.
- **2026-08-15:** Captured 29 typed design lines through the autonomous Hugentics design-session route, grounded in Chatlas session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`.
- **2026-08-15:** Added the conservative `Agent.Loaded.Context` promise and retired the canonical context-blob and `Agent.Execution` directions.
- **2026-08-15:** Settled stateless `Event.Ref` drift resolution against the current Normal Model and rejected cross-run normalized observation history.
