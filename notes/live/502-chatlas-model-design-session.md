# Chatlas Model - design-session

## Session.Abstract

- **Intent:** Revisit and extend the Chatlas index model — define the foundational conceptual layer, review existing blocks, create new blocks.
- **State:** Active — foundational concept blocks captured; provider-home/update alignment in progress.
- **Active focus:** Provider.Instance, Provider.Home, Provider.Home.Query, and atomized update mechanics.
- **Scope:** The full Chatlas mental model: dataset identity, raw archive, session indexing, query, views, export.
- **Next:** Visit the aligned concepts one by one and decide which belong in public Chatlas index blocks versus general Agentos index blocks.

## Design.Index

### Chatlas.Dataset

- `Chatlas.Dataset` is the Agentos maintained dataset of chat sessions collected from AI assistant providers
- lifecycle: native scan → raw archive → session indexing → query → view → export
- the raw archive preserves provider-native artifacts; the normalization layer derives canonical session representations
- the session index is the queryable metadata surface over all archived sessions
- views are named operations over session sets — the analytical and export layer
- the dataset is user-scoped, not project-scoped — queries can filter by project
- core subsystems: `Raw.Archive`, `Session.Index`, `Chatlas.Query.Surface`, `Chatlas.View.Model`

### Raw.Archive

- `Raw.Archive` is the preservation layer that stores provider-native artifacts verbatim
- every session discovered during native scan gets its raw artifacts copied into the archive before any normalization
- the archive is the source of truth for what the provider actually produced — normalization is derived, raw is authoritative
- organized by `Provider.Instance` — each provider/instance pair has its own archive partition
- raw artifacts are overwritten in place when the provider updates them — git captures version history
- the `Normalization.Layer` reads from the raw archive to derive canonical session representations
- retention scope is governed by `Chatlas.Retention.Policy` — what to keep, what to exclude, what to defer

### Provider.Instance Alignment

- `Provider.Instance` is a general Agentos concept, not a Chatlas-owned concept
- for Chatlas, `Provider.Instance` is the concrete configured agent instance that owns the upstream provider-native data Chatlas can scan
- a provider instance is provider-specific by nature — each provider family has ad hoc runtime, config, home, and artifact mechanics
- the provider home is part of provider-instance identity, not a detachable child collection
- if an agent changes home, that is a different `Provider.Instance`
- Chatlas partitions raw archive and session index material by `Provider.Instance`

### Provider.Home

- `Provider.Home` is the local provider-native data home of one `Provider.Instance`
- it is the concrete observable source Chatlas reads when discovering provider-native sessions
- it may include files, folders, databases, caches, logs, or known paths interpreted together as the configured home for that instance
- it is provider-native — its layout, artifact names, schemas, and update behavior are defined by the provider, not by Chatlas
- Chatlas reads from `Provider.Home`; Chatlas does not own or mutate it
- `Chatlas.Raw.Archive` is the preserved downstream copy of selected provider-home artifacts

### Provider.Home.Query

- `Provider.Home.Query` is the read-only discovery/query layer over a `Provider.Home`
- it finds provider-native sessions or artifacts directly in the provider home, outside the Chatlas archive
- it returns provider-home matches or locators, not Chatlas session index rows
- it is used when freshness or direct source lookup matters before relying on archived Chatlas material
- it does not mutate `Chatlas.Raw.Archive` or `Chatlas.Session.Index`

### Chatlas.Update.Pipeline

- `Chatlas.Update.Pipeline` is the decomposed form of `agentos chatlas update`
- bulk update runs the pipeline across configured `Provider.Instance` inputs
- targeted update runs the same mechanics for one provider instance, provider-home locator, or known session identity
- targeted refresh is not a separate conceptual system — it is an atomized invocation of the existing update mechanics
- the pipeline preserves the lifecycle invariant: `Provider.Home` → `Chatlas.Raw.Archive` → `Chatlas.Session.Index` → views/export

### Chatlas.Retention.Policy

- `Chatlas.Retention.Policy` is the set of per-provider retention decisions that govern what raw artifacts the `Raw.Archive` keeps
- the fundamental objective is capturing user interactions — user direct turns and anything visible to the user during the session
- the policy is materialized as audit reports — each report captures current decisions for one provider's artifact families
- there is no standalone policy document — the audit reports are the living policy
- produced through the `Chatlas.Retention.Audit` workflow skill

#### appendix

##### Retention Tiers

- tier1 (transcript fidelity) — artifacts required to reconstruct the conversation as the user experienced it; the non-negotiable core
- tier2 (behavioral analysis) — artifacts useful for understanding agent behavior, tool use, model patterns; direct, high-signal content that extends coverage beyond the visible conversation
- tier3 (telemetry) — usage metrics, timing, cost data outside session scope; completeness-oriented

##### Decision Categories

- `retain_raw_required` — must archive; needed for normalization or transcript reconstruction
- `retain_raw_optional_future` — not needed now, but may become useful; archive if cheap
- `telemetry_outside_session` — telemetry data that doesn't belong in session scope; track separately or defer
- `exclude` — do not archive

##### Audit Reports

- one report per provider captures current retention decisions for that provider's artifact families
- reports are delta-aware — compare against previous audit to surface new, superseded, or unresolved findings
- each artifact family gets: sample paths, count/size estimates, tier classification, raw decision, rationale
- report template: `agentos-chatlas-pkg/references/retention-audit-report-template.md`

##### Evidence Sources

- previous audit reports for the same provider
- live provider home artifacts (filesystem inspection)
- current Chatlas raw archive state
- code surfaces that consume raw artifacts (normalization, export)

### Chatlas.Session.Index

- `Chatlas.Session.Index` is the queryable metadata surface over all archived sessions in the `Chatlas.Dataset`
- each session is represented by an index row — a metadata record derived during the indexing phase of the dataset lifecycle
- partitioned by `Provider.Instance` — each provider/instance pair maintains its own index partition
- the index is rebuilt from raw archive content on each delta scan — it is derived, not manually maintained
- index selection is the first filtering layer of `Chatlas.Query.Surface`
- index rows carry session identity, content fingerprint, provider metadata, project association, timestamps, and extractability flags

### Session.Identity

- `Session.Identity` is the set of properties sufficient to uniquely identify a session across the `Chatlas.Dataset`
- composed of provider, instance, and session id — together they determine one session
- `Session.Identity.Hash` is a deterministic hash computed from these properties — the compact canonical identifier
- `Session.Identity.Hash` is used by `Session.Set`, query surfaces, and view addressing
- stable across dataset refreshes — a session's identity does not change when its content is updated by the provider
- distinct from `Session.Content` — identity is which session, content fingerprint tracks what it contains

## Session.Notes

- Move `agentos-chatlas-retention-audit/assets/report-template.md` to `agentos-chatlas-pkg/references/retention-audit-report-template.md`. The skill should cite the package reference.
- Rejected framing: a `Provider.Instance` does not have one primary `Provider.Home` with possible additional homes. That was wrong because provider home participates in instance identity. A different home means a different provider instance.

## Session.Log

- 2026-05-22: Session opened. Scope: full Chatlas mental model revisit. Chatlas.Dataset block captured from in-chat alignment.
- 2026-05-22: Raw.Archive block captured.
- 2026-05-22: Chatlas.Retention.Policy block captured with appendix (tiers, decisions, audit shape, evidence).
- 2026-05-22: Provider.Instance block written directly to agentos-pkg/index/104-index.md (general Agentos concept, not Chatlas-specific).
- 2026-05-22: Chatlas.Session.Index block captured.
- 2026-05-22: Session.Identity block captured.
- 2026-05-24: Captured corrected Provider.Instance/Provider.Home alignment, Provider.Home.Query, and Chatlas.Update.Pipeline as atomized update mechanics.
