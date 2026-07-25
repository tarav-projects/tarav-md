# 512 - Chatlas Event.Pattern Query Backend v1 - Impl.Req

## Impl.Abstract

- **Goal:** add a backend-neutral `Event.Pattern` query path that can discover relational turn patterns through either an authoritative normal-model scan or a disposable SQLite candidate index.
- **Status:** ready for execution.
- **Target:** `agentos-chatlas-py`.
- **Observable workflow:** find an assistant turn containing candidate text immediately followed by a user turn with exact approval text, then return the selected events from the current `Chatlas.Session.Model`.
- **Authority rule:** backends return coordinates only. Every candidate is reloaded and fully re-evaluated against the current normal model, and public event payloads are projected only from that model.
- **Source context:** `agentos-chatlas-pkg/design/100-design.md` blocks `Chatlas.Query.Surface`, `Chatlas.Session.Model`, and `Session.Event.Tape`; candidate blocks in `skills/agentos-chatlas-pkg/agendix/Chatlas.Query.Surface-agendix.md`; develop authorization and design support at `^c20260725-38u`.

### Scope

- In: an immutable structured `Event.Pattern` model, JSON parser, and authoritative evaluator.
- In: a candidate-backend protocol, normal-model scan backend, and disposable SQLite backend.
- In: explicit SQLite rebuild and freshness/coverage metadata.
- In: one CLI query workflow for adjacent visible turns with backend selection.
- In: authoritative revalidation, projection, and fallback behavior tests.
- Out: raw SQL as a public interface, arbitrary relation algebra, incremental SQLite maintenance during normal Chatlas update, duplicate-anchor linting, and rewrites of existing query commands.

## Impl.Index

### Event.Pattern.Contract

- `Event.Pattern` is the provider-independent logical request. Backend capabilities do not alter its meaning.
- V1 predicates are `role`, `kind`, `event_id`, `text_exact`, and `text_contains`.
- A pattern contains one or more ordered steps over visible turns. V1 relational matching means consecutive events in the normal model's visible-turn projection.
- V1 selection is `all`, `first`, or `latest`; projection is `match`, `first`, or `last`; cardinality is `many`, `one`, or `zero-or-one`.
- Invalid fields, values, or structurally empty patterns fail clearly before backend execution.

### Query.Backend.Contract

- A backend receives an `Event.Pattern` plus query scope and returns candidate session/event coordinates with coverage metadata.
- Candidate references contain no event text, role, timestamp, or other public payload.
- `NormalModelScanBackend` is the semantic reference backend and authoritative fallback.
- `SQLiteCandidateBackend` is a disposable discovery accelerator. Its schema and SQL are private implementation details.
- Backend capability mismatch, incomplete coverage, or unprovable freshness selects the scan backend rather than weakening query semantics.

### Authority.And.Projection

- Candidate coordinates are resolved against the current `Chatlas.Session.Model`.
- The complete pattern is re-evaluated against current model events before a match is accepted.
- Selection and cardinality are applied to authoritative matches, not trusted backend rows.
- Public results contain normal-model event projections. SQLite content is never returned as an event payload.

### SQLite.Freshness

- The derived database records a schema version and corpus fingerprint.
- The fingerprint is computed from the current session-index inventory using stable session identity plus available change indicators.
- An explicit rebuild transaction replaces the disposable projection from current normal models.
- `auto` uses SQLite only when schema, coverage, and corpus fingerprint match; otherwise it scans authoritative models.
- Explicit `sqlite` requests remain correctness-preserving: an unusable SQLite projection falls back to scan and reports the backend actually used.

### CLI.Surface

- Add a focused `agentos chatlas events` command group rather than expanding the existing session-row query contract.
- `agentos chatlas events index` rebuilds the disposable SQLite projection.
- `agentos chatlas events query --pattern-json <json> --backend auto|scan|sqlite` evaluates a structured pattern.
- Existing Chatlas session selectors should be reused where practical to constrain the corpus.
- The JSON result reports requested/used backend and authoritative matches; it does not expose raw SQL or SQLite rows.

## Impl.Agendix

- [touched] `agentos-chatlas-pkg/design/100-design.md#Chatlas.Query.Surface`
- [touched] `agentos-chatlas-pkg/design/100-design.md#Chatlas.Session.Model`
- [touched] `agentos-chatlas-pkg/design/100-design.md#Session.Event.Tape`
- [touched] `skills/agentos-chatlas-pkg/agendix/Chatlas.Query.Surface-agendix.md#Candidate.Event.Pattern` ^c20260725-35u
- [touched] `skills/agentos-chatlas-pkg/agendix/Chatlas.Query.Surface-agendix.md#Candidate.Chatlas.Query.Backend` ^c20260725-35u
- [touched] develop authorization and supporting design turns ^c20260725-38u

## Execution.Plan

### Slice 1 - Event.Pattern and authoritative evaluator

- Add the typed pattern model, strict JSON decoding, visible-turn projection, relational matcher, selection, projection, and cardinality validation.
- Keep the evaluator independent of candidate storage and CLI parsing.
- **RED:** tests demonstrate adjacent assistant-containing/user-exact matching, invalid pattern rejection, selection, and cardinality behavior are absent.
- **GREEN:** the tests pass over synthetic `Chatlas.Session.Model` fixtures.
- **Observable:** one structured pattern returns deterministic event-id sequences from a normal model.
- **Status:** pending.

### Slice 2 - Backend protocol and SQLite candidate discovery

- Add coordinate-only candidate/result types and backend protocol.
- Implement the scan backend as the semantic reference.
- Add derived SQLite materialization with schema metadata, corpus fingerprint, and candidate discovery for the V1 predicates/relation.
- **RED:** parity, tampered-row, and stale-fingerprint tests fail before implementation.
- **GREEN:** scan and fresh SQLite discover equivalent candidates; a SQLite false positive is rejected after authoritative reload; stale SQLite falls back to scan and still finds new matches.
- **Observable:** rebuilding then querying with `sqlite` uses SQLite for discovery while results remain authoritative.
- **Status:** pending.

### Slice 3 - End-to-end CLI workflow

- Register `events index` and `events query`, structured pattern input, backend selection, reusable session scope, and JSON result envelope.
- Return selected event projections assembled from current normal models with backend diagnostics.
- **RED:** CLI behavior test fails because the command group is absent.
- **GREEN:** an assistant candidate followed by exact user approval is found through scan and SQLite; returned content reflects the normal model rather than a tampered derived row.
- **Observable:** the complete rebuild/query workflow runs through `agentos chatlas events`.
- **Status:** pending.

### Slice 4 - Regression and documentation pass

- Document the command and pattern JSON in the Chatlas package skill/reference surface that owns CLI usage.
- Run targeted tests, full package tests, and scoped lint.
- Verify existing `query`, `views inline`, indexing, and anchory behavior remain unchanged.
- **Status:** pending.

### Acceptance.Signals

- A single structured relational pattern has identical meaning under scan and SQLite discovery.
- SQLite candidates cannot establish a match or provide public event payloads.
- A stale or incomplete derived database cannot cause a false negative because query execution falls back to authoritative scanning.
- The CLI exposes backend-neutral JSON patterns, not SQL.
- Targeted and existing Chatlas tests pass.

### Risks.And.Deviation.Triggers

- If current session-index fields cannot establish a safe corpus fingerprint, use a conservative fingerprint or always fall back; do not infer freshness.
- If normal-model event structure lacks stable visible-turn ordering or identifiers, record the mismatch before changing event semantics.
- If SQLite cannot express a supported V1 predicate exactly, it may return a broader candidate set; authoritative re-evaluation must remain exact.
- Stop rather than adding provider-specific pattern fields or making the SQLite projection authoritative.

## Impl.Log

- 2026-07-25: Impl.Req created in autonomous develop mode. The first version deliberately limits relations to adjacent visible turns while preserving a backend abstraction for later vocabulary.
