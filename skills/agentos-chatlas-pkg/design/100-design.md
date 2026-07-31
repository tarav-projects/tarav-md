> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Chatlas.Query.Surface

- `Chatlas.Query.Surface` is the Chatlas session discovery interface family.
- `agentos chatlas index query` is the base query surface over Chatlas session index rows.
- `agentos chatlas query` is the higher-level session query surface.
- `agentos chatlas query` extends index selection with later query layers such as raw-artifact filtering, standard-model filtering, and row projection.
- The two commands may return different row shapes, but they should expose a consistent top-level query envelope.

****

## Chatlas.Query.Envelope

- `Chatlas.Query.Envelope` is the normalized top-level JSON response shape shared by Chatlas query surfaces.
- The envelope should keep query accounting separate from row projection.
- Shared count fields should use explicit phase names:
  - `index_matched_row_count`
  - `candidate_row_count`
  - `query_matched_row_count`
  - `returned_row_count`
- For `agentos chatlas index query`, the phases collapse because the only query layer is index selection.
- For `agentos chatlas query`, the phases remain layered:
  - index filters select index matches
  - scan limits choose candidates for expensive filters
  - raw and standard-model filters decide final query matches
  - final limit determines returned rows
- Row projection is intentionally independent from the envelope:
  - `agentos chatlas index query` returns full index rows
  - `agentos chatlas query` returns normalized session rows by default

****

## Chatlas.View.Model

- `Chatlas.View.Model` is the unified abstract model for Chatlas views as named operations over session sets
- a view is a named operation applied to a set of sessions, optionally customized by a prompt
- the model treats single-session and multi-session views uniformly
- two production classes: `Programmatic.View` (framework-produced) and `Agentic.View` (agent-produced via staging)
- the framework resolves context, checks freshness, manages dependencies, and commits artifacts
- core concepts: `View.Identity`, `Session.Set`, `View.Workflow`, `View.Class`

****

## View.Identity

- `View.Identity` is the tuple `(View.Name, Session.Set, Driving.Prompt)` that addresses a view instance
- it is the dispatch key — analogous to multiple dispatch in Julia
- `View.Name` is a string — the registered operation name
- `Driving.Prompt` is an optional caller-provided prompt — empty by default, part of identity when present
- `Cache.Key` is derived deterministically from `View.Identity`
- two references to the same `View.Identity` resolve to the same `View.Depot`
- identity is addressing, not content equivalence — the depot may hold different versions over time

****

## Session.Set

- `Session.Set` is a normalized, deduplicated, sorted array of `identity_hash` strings
- it is the argument side of `View.Identity` — the data scope a view operates on
- normalization: extract `identity_hash`, deduplicate, sort lexicographically — automatic at the framework boundary
- any collection resolving to the same canonical array is the same `Session.Set` — a query result, an explicit list, a filtered index
- origin is not part of identity — a `Session.Set` does not remember how it was constructed
- must contain at least one element; size 1 and size N are treated uniformly

****

## View.Workflow

- `View.Workflow` is the protocol a named view operation implements
- it defines what the view does — status checking, artifact production, contract declaration, dependency declaration
- each `View.Name` maps to exactly one `View.Workflow` registration
- the workflow receives resolved session data at runtime — it does not perform session selection
- production is routed by `View.Class`

****

## Workflow.Update

- [DF] `Workflow.Update` is the update capability of one workflow: bring everything current along the path from `Provider.Home` to that workflow's target, and nothing past it ^c20260714-3u
- plain `agentos chatlas update` is itself a workflow — its target is the `Chatlas.Session.Index` ^c20260714-4u
- [CT] no update touches another workflow's caches — a stale downstream artifact is detected by its own workflow's read-time freshness check and re-derived on demand ^c20260714-2u
- [PR] a stale `Session.Model.Artifact` is an asset, not garbage — `Delta.Normalization::Chatlas` resumes from it; deleting it destroys the resume base ^c20260714-2u
- [FR] a workflow may offer forced re-materialization that ignores freshness — a correctness-testing tool, never the default ^c20260714-2u

****

## View.Class

- `View.Class` distinguishes view workflows by their production mode
- the two classes are `Programmatic.View` and `Agentic.View`
- both share the `View.Workflow` common surface — status, artifact contract, name, dependencies
- `Programmatic.View` — production is deterministic and cheap; the framework produces directly, no staging
- `Agentic.View` — production requires an external agent; the framework prepares a staging area and production prompt; the agent writes, the framework commits

****

## Chatlas.Lock.Visibility

- `Chatlas.Lock.Visibility` is the rule that Chatlas never performs an actual lock action in silence
- Chatlas acquires a lock only when coordination is required; fresh reads remain lock-free and print no lock messages
- every operation that acquires, waits for, or releases a lock prints that action to `stderr`
- lock lifecycle messages are emitted by shared locking functions so callers cannot accidentally acquire a silent lock
- every lock lifecycle message includes the exact lock-file path needed for agent inspection
- Chatlas does not silently break, delete, or recover locks
- visible lock state is the recovery mechanism: agents inspect the reported lock path and decide what action is appropriate

****

## Provider.GC

- `Provider.GC` is the Chatlas maintenance subsystem for deleting provider-home originals after Chatlas has captured them.
- provider homes are ingestion sources; Chatlas raw archive is the retained dataset once archive coverage is proven.
- command shape: `agentos chatlas gc --provider copilot-cli`.
- eligibility is proven from Chatlas-owned evidence: indexed backing artifacts, raw archive paths, manifests, and source checks.
- unknown, unindexed, failed-parse, missing-archive, or mismatched originals are not delete candidates.
- dry-run/report mode is the default; destructive deletion requires an explicit apply gate.
- the goal is faster `agentos chatlas update` by shrinking old provider-home scan surfaces.
- a `Provider.Home.Adapter` capability — the adapter owns all provider-home contact, including this gated deletion of captured originals ^c20260714-6u

****

## View.GC

- [DF] `View.GC` is the depot-side maintenance subsystem for deleting stale view caches — orphaned view identities, superseded parameter variants, caches of sessions no longer indexed ^c20260714-5u
- the depot sibling of `Provider.GC`, same grammar: report-first default, destructive deletion behind an explicit apply gate ^c20260714-5u
- eligibility is proven from depot evidence: view manifests checked against current `View.Identity` and the `Chatlas.Session.Index` ^c20260714-5u
- [PR] cache hygiene is an explicit maintenance action, never a side effect of update — deletion gets its own audit trail ^c20260714-5u

****

## Cold.Session.Cache

- `Cold.Session.Cache` is a Chatlas update-cache optimization for already-known old sessions.
- it applies after provider discovery; discovery still runs and finds current sessions.
- a session becomes cold when its provider activity timestamp is older than the cold cutoff, initially `30d`.
- normal update may trust cold cache entries and skip expensive source-signature comparison.
- recent sessions and sessions with newer provider activity stay hot and get normal comparison.
- `--full-scan` disables the cold shortcut and recomputes cache signatures.
- there is no automatic random or scheduled full audit; full passes are explicit operator actions.

****

## Session.Identity

- `Session.Identity` is the set of properties that uniquely identify one session across the `Chatlas.Dataset`
- composed of three components: provider family, configured instance, and provider-native session id
- `Session.Identity.Hash` is a deterministic hash of those three components — the compact canonical identifier
- stable across dataset refreshes — identity does not change when the provider updates session content
- distinct from content fingerprint — identity answers "which session", content fingerprint tracks "what it currently contains"

****

## Chatlas.Session.Index

- `Chatlas.Session.Index` is the queryable metadata surface over all archived sessions in the `Chatlas.Dataset`
- each session is one index row — a metadata record derived from raw archive content during the indexing phase
- partitioned by `Provider.Instance` — each provider/instance pair has its own index partition
- derived, not manually maintained — rebuilt from the raw archive on each delta scan
- index selection is the first filtering layer of `Chatlas.Query.Surface`
- index rows carry `Session.Identity`, content fingerprint, project association, timestamps, and extractability flags

****

## Chatlas.Dataset

- `Chatlas.Dataset` is the Agentos-maintained dataset of chat sessions collected from AI assistant providers
- lifecycle: `Provider.Home.Adapter` → `Raw.Archive` → `Chatlas.Session.Model` → `Chatlas.Session.Index` → `Chatlas.Query.Surface` → `Chatlas.View.Model` ^c20260714-0u
- user-scoped, not project-scoped — queries can filter by project but the dataset spans all projects
- the raw archive is the authoritative preservation layer; all derived surfaces rebuild from it

****

## Raw.Archive

- `Raw.Archive` is the preservation layer that stores provider-native session artifacts verbatim
- every session discovered during native scan gets its artifacts copied into the archive before any normalization
- the source of truth for what the provider actually produced — normalization is derived, raw is authoritative
- organized by `Provider.Instance` — each provider/instance pair has its own archive partition
- raw artifacts are overwritten in place when the provider updates them — git captures version history
- retention scope is governed by `Chatlas.Retention.Policy`

****

## Chatlas.Retention.Policy

- `Chatlas.Retention.Policy` is the set of per-provider retention decisions that govern what raw artifacts the `Raw.Archive` keeps
- the fundamental objective is capturing user interactions — direct user turns and anything visible to the user during the session
- materialized as audit reports — each report captures current decisions for one provider's artifact families
- there is no standalone policy document — the audit reports are the living policy
- produced through the `Chatlas.Retention.Audit` workflow skill

****

## Chatlas.Update.Pipeline

- `Chatlas.Update.Pipeline` is the decomposed form of `agentos chatlas update`
- bulk update runs the pipeline across all configured `Provider.Instance` inputs
- targeted update runs the same mechanics for one provider instance, provider-home locator, or known `Session.Identity`
- targeted refresh is not a separate system — it is an atomized invocation of the existing update mechanics
- the pipeline preserves the lifecycle invariant: `Provider.Home` → `Raw.Archive` → `Chatlas.Session.Index`
- [CT] the update pipeline's native scan is the only Chatlas system that reads `Provider.Home`; query and view surfaces answer from the depot ^c20260712-9u

****

## Scan.Scope

- [DF] `Scan.Scope` is the selection an update run hands the `Provider.Home.Adapter`'s scan: which sessions the scan considers — everything configured, one provider, one instance, one session, or an activity window ^c20260714-2u
- [CT] narrowing the scope never changes the mechanics — every scoped run performs the same discover → signature-compare → archive → derive stages over its selection ^c20260714-2u
- [PR] a single-session refresh is the whole pipeline at one-session scope, not a parallel code path ^c20260714-2u
- cold-cache trust and `--full-scan` are comparison policies, orthogonal to scope — scope picks the candidates, policy picks how hard to look at them ^c20260714-2u

****

## Provider.Home

- `Provider.Home` is the local provider-native data home of one `Provider.Instance`
- the concrete observable source Chatlas reads when discovering provider-native sessions
- may include files, folders, databases, caches, logs, or known paths interpreted together as the configured home
- provider-native — its layout, artifact names, schemas, and update behavior are defined by the provider, not by Chatlas
- Chatlas reads from `Provider.Home`; it does not own or mutate it
- `Raw.Archive` is the preserved downstream copy of selected provider-home artifacts

****

## Provider.Home.Adapter

- [DF] `Provider.Home.Adapter` is the Chatlas component owning all `Provider.Home` contact for one provider family — discovery scan, change signatures, archive copy, home-query diagnostics, and provider-GC eligibility checks ^c20260714-1u
- [CT] it is the only component that touches the `Provider.Home` filesystem — every other Chatlas system answers from the depot or reaches provider data by means of the adapter ^c20260714-0u
- [CT] the adapter provides the files of the `Raw.Archive` ^c20260714-1u
- [PR] one component owning the entire provider-home contact surface keeps the depot boundary auditable ^c20260714-0u

****

## Provider.Home.Query

- `Provider.Home.Query` is the read-only discovery layer over a `Provider.Home`
- finds provider-native sessions or artifacts directly in the provider home, outside the Chatlas archive
- returns provider-home matches or locators, not `Chatlas.Session.Index` rows
- used when freshness or direct source lookup matters before relying on archived material
- does not mutate `Raw.Archive` or `Chatlas.Session.Index`
- [CT] a diagnostic surface, not a query path — `Chatlas.Query.Surface` never routes through it ^c20260712-9u
- a capability of the `Provider.Home.Adapter` — the same discovery machinery exposed as a diagnostic read ^c20260714-6u

****

## Chatlas.Session.Model

- `Chatlas.Session.Model` is the standard with which Chatlas represents any session's information
- provider-neutral: one model normalized inward from many provider-native session formats
- directionality: Chatlas knows provider formats and normalizes them into one; providers know nothing about this model
- producer: the `Normal.Assembler` of `Normalization.Pipeline::Chatlas.Session.Model` writes it — there is no provider-side conformance
- provider-native formats are inspiration for the model's expressiveness, not an input contract it must accept
- not overfitted to any single provider — the model carries no provider-named canonical fields
- expressive enough to represent most of what a provider provides — each provider's content maps into a neutral concept the model defines
- provider-specific richness with no neutral concept lives in `native` / `source_refs` — recoverable, never canonical
- consumers are read-side: search, summary, replay, UI, `Chatlas.View.Model`
- its namespace is reified as `Chatlas.Session.Model.Contract` — the machine-readable path table model consumers and corpus tests share
- [CT] the model carries chat data, never a consumer's interpretation of it — what a turn or event means to a downstream application is that application's read, not a model field ^c20260728-3u
- [PR] the boundary is what keeps the model general: every consumer's semantics would otherwise accrete into the standard until it stopped being about chat ^c20260728-3u

### meta

- aliases: `Session.Normal.Model` (session-scoped long form), `Normal.Model` (its role name as the target model of `Normalization.Pipeline::Chatlas.Session.Model`)

****

## Chatlas.Session.Model.Contract

- `Chatlas.Session.Model.Contract` is the `Normal.Model.Contract` of `Chatlas.Session.Model` — its namespace reified as a machine-readable path table
- lives in the code repo beside its producers: `agentos-chatlas-py/references/normal-model.contract.json`
- one artifact, two consumers: `Raw.Normalizer`s target it, `Chatlas.Session.Model.Tests` loads its judgments and verdicts from it

****

## Chatlas.Session.Model.Tests

- `Chatlas.Session.Model.Tests` is the testing surface of `Chatlas.Session.Model` — the model is validated against its own corpus, with the assembled instances as evidence
- grounded in the corpus-test concepts of the agentos-pkg Normalization.Pipeline appendix (`Projection.Test`, `Path.Source.Split.Test`, `Normalization.Coverage`, `Under.Normalization`) — the concepts live there, this block indexes their chatlas instantiation
- the engines load their judgments from `Chatlas.Session.Model.Contract` — one load point keeps model, contract, and tests from drifting apart
- failures triage three-way: normalizer defect, model gap, or genuine source condition — the tests are a convergence engine, not a gate
- runs are operated as `Run.Req` copies of the templates in `agentos-chatlas-py/notes/templates/`; the marked copy is the run report
- current state: workspace `agentos-chatlas-py/dev/user-script-invariant-test/` — engines `validate.py` (script invariants), `projection.py`, `path_source_split.py` (+ schema closure), `coverage.py`, `comparative_projection.py` (script-pair skeletons); verdict memory beside them (`path-verdicts.md`, `divergence-notes.md`, `coverage-baseline.md`); corpus = User.Script.Invariant script sessions (claude-code + codex; copilot-cli runs are an open extension) plus random archive samples

****

## Session.Event.Tape

- `Session.Event.Tape` is the canonical structure of a `Chatlas.Session.Model` — an append-only, ordered ledger of typed events
- the tape is the single source of truth; every higher-level view of the session is a projection derived from it
- one event captures one thing that happened in the session
- an event carries its identity, its order, its kind, who produced it, its content, and a link back to raw evidence
- projections are derived and disposable — rebuildable from the tape, never authoritative on their own
- [DC] the tape is a jsonl file: one frozen event per line, appended in order ^c20260712-12u
- [DC] each tape line carries provenance beside its payload: `source_refs` to the raw records it derives from, a `source_hash` over those records, a finality flag, and a chain hash over the line and its predecessor ^c20260712-12u
- [DF] a final line's validity depends only on its source records — its `source_hash` re-verifies it; a non-final line consumed end-of-file context (open tool groups, run status, last-prompt residue) and is recomputed on every delta pass ^c20260712-12u
- [DC] tail revision is truncate-and-reappend: cut the tape at the last final line, re-derive the volatile tail plus new events, append ^c20260712-12u
- [RJ] serving reads through a checkpoint overlay of shadow events — the tape on disk is always the complete served tape ^c20260712-12u
- [PR] per-line provenance turns staleness detection mechanical: divergence is located at a line, recomputation starts there, never from zero ^c20260712-12u
- [DC] `sequence` carries tape position and is the only positional field — order is a real tape property, identity is not derived from it ^c20260728-1u
- [RJ] `event_id` as a distinct field: it was `"event-" + sequence`, a stringified duplicate whose name invited durable references onto an ordinal — retired to a contract tombstone ^c20260728-1u
- [EX] anchors keyed on `event_id` mis-pointed after re-segmentation: a stored user turn slid three ordinals while its timestamp held, and the position it vacated resolved to a later assistant turn ^c20260728-1u
- [DC] durable references key on an `Event.Grouping` carrying a stability contract — `Normal.Turn` for chat evidence ^c20260728-1u

****

## Event.Hash

- [DF] `Event.Hash` is the deterministic content digest of one `Session.Event.Tape` event ^c20260731-22u ^c20260731-23u
- [DC] its canonical input is the event data that `Chatlas.Session.Model` considers the event's content ^c20260731-22u ^c20260731-23u
- [CT] `Event.Hash` excludes `Event.Annotation`, tape position, grouping identity, native identifiers, and derivation bookkeeping ^c20260731-22u ^c20260731-23u
- [PR] the hash projection is a semantic model judgment about what constitutes event content, even when its concrete digest algorithm is an implementation detail ^c20260731-22u ^c20260731-23u
- [CT] moving or re-annotating an unchanged event does not change its `Event.Hash` ^c20260731-22u ^c20260731-23u

****

## Event.Annotation

- [DF] `Event.Annotation` is normalization-owned derived metadata attached to a `Session.Event.Tape` event without changing the event's content ^c20260731-21u ^c20260731-24u
- [DC] an event carries annotations through an optional top-level `annotations` object ^c20260731-21u ^c20260731-24u
- [CT] absence of `annotations` means the event carries no annotations ^c20260731-21u ^c20260731-24u
- [DC] each annotation kind is a key whose value is a kind-specific object ^c20260731-21u ^c20260731-24u
- [DC] annotation kinds are open and independent; one event may carry several kinds ^c20260731-21u ^c20260731-24u
- [DC] annotation assignment is normalization work owned by the corresponding `Raw.Normalizer` ^c20260731-21u ^c20260731-24u
- [CT] annotations remain outside `Event.Hash` because they annotate event content rather than constitute it ^c20260731-22u ^c20260731-24u

****

## Event.Grouping

- [DF] `Event.Grouping` is a semantic collection of `Session.Event.Tape` events derived through `Event.Annotation` ^c20260731-22u ^c20260731-25u
- [DC] a grouping annotation kind assigns an identifier to its member events; events carrying the same kind and identifier form one group ^c20260731-22u ^c20260731-25u
- [CT] the tape remains the single source of truth; collecting a group is software over annotations, never an authoritative container ^c20260731-22u ^c20260731-25u
- [DC] grouping kinds are open and orthogonal; one event may participate in several independent groupings ^c20260728-0u ^c20260731-25u
- [CT] grouping is partial; an event may belong to no group of a given kind ^c20260728-0u ^c20260731-25u
- [DC] normalization owns each grouping kind's semantic and annotation assignment ^c20260728-0u ^c20260731-25u
- [EX] `Normal.Turn` is the chat-semantic grouping; a request/response cycle may be another ^c20260731-22u ^c20260731-25u

****

## Event.Group.Hash

- [DF] `Event.Group.Hash` is the deterministic content digest of one `Event.Grouping` ^c20260731-22u ^c20260731-26u
- [DC] its canonical input is the ordered sequence of member `Event.Hash` values in tape order ^c20260731-22u ^c20260731-26u
- [CT] it excludes the grouping annotation kind and identifier ^c20260731-22u ^c20260731-26u
- [CT] changing member content, membership, or order changes the group hash ^c20260731-22u ^c20260731-26u
- [CT] assigning the same unchanged members another group identifier does not change the group hash ^c20260731-22u ^c20260731-26u
- [CT] `Event.Group.Hash` asserts grouped content rather than group identity; content-equivalent groups may share a hash ^c20260731-22u ^c20260731-26u

****

## Normal.Turn

- [DF] `Normal.Turn` is the normalization-owned `Event.Grouping` for one chat-semantic turn ^c20260731-22u ^c20260731-27u
- [DC] it is realized through `annotations.normal_turn.id`, whose value is a `Normal.Turn.Id` ^c20260731-21u ^c20260731-27u
- [CT] assigning `Normal.Turn` groups existing `Session.Event.Tape` events; it does not change their generation, payload, role, producer, sequence, or meaning ^c20260731-15u ^c20260731-27u
- [DF] `Normal.Turn::User.Turn` groups normalized events carrying the data supplied in one user interaction ^c20260731-15u ^c20260731-27u
- [DC] a `Raw.Normalizer` assigns `User.Turn` membership from normalized event semantics rather than inheriting provider record boundaries or raw role labels ^c20260731-15u ^c20260731-27u
- [CT] a `User.Turn` has no semantic relationship to preceding or following assistant activity ^c20260731-15u ^c20260731-27u
- [EX] user-turn data may include text, images, files, attachments, and structured command arguments ^c20260731-15u ^c20260731-27u
- [PR] user-turn purity protects `User.Authority`; grouping assistant or injected data into a `User.Turn` corrupts that authority boundary ^c20260731-15u ^c20260731-27u
- [DC] `Normal.Turn::Assistant.Turn` is grouped independently and may span reasoning, messages, tool activity, and response metadata ^c20260731-15u ^c20260731-27u
- [DC] each `Raw.Normalizer` maps native handles onto the semantic; a native grouping that over-merges is refined, never inherited ^c20260728-0u ^c20260731-27u
- [CT] Chatlas supplies turn grouping and identity, never turn interpretation; consumer meanings such as `Turn.Type` remain outside the model ^c20260728-0u ^c20260731-27u

****

## Normal.Turn.Id

- [DF] `Normal.Turn.Id` is an opaque session-local label assigned to one `Normal.Turn` ^c20260731-16u ^c20260731-28u
- [CT] a `Normal.Turn.Id` must be unique within its `Chatlas.Session.Model` ^c20260731-16u ^c20260731-28u
- [PR] stability is desirable because it reduces reference repairs, but correctness does not depend on it ^c20260731-16u ^c20260731-28u
- [CT] `Normal.Turn.Id` locates a grouping; by itself it does not assert the grouping's content ^c20260731-16u ^c20260731-28u

****

## Normal.Turn.Ref

- [DF] `Normal.Turn.Ref` is the durable, self-verifying reference to one `Normal.Turn` ^c20260731-16u ^c20260731-29u
- [DC] its canonical object carries `session`, `turn_id`, `turn_hash`, and `at` ^c20260731-16u ^c20260731-29u
- [DC] `session` locates the expected `Chatlas.Session.Model` ^c20260731-16u ^c20260731-29u
- [DC] `turn_id` locates the expected `Normal.Turn` within that session ^c20260731-16u ^c20260731-29u
- [DC] `turn_hash` is the turn's `Event.Group.Hash` and asserts its grouped content ^c20260731-22u ^c20260731-29u
- [CT] `at` is readability and diagnostic metadata, not the turn's identity or selection mechanism ^c20260731-16u ^c20260731-29u
- [CT] resolution verifies the assertion by recomputing the current group hash and comparing it with `turn_hash` ^c20260731-16u ^c20260731-29u

****

## Session.Model.Artifact

- [DF] `Session.Model.Artifact` is the on-disk form of one `Chatlas.Session.Model` — a per-session folder of purpose-split files rather than one monolithic document ^c20260712-11u
- [DC] the folder holds a small mutable head (`session.json` — identity, session payload, sources, normalization meta), the append-only `Session.Event.Tape` (`events.jsonl`), and the projections as sibling derived files ^c20260712-11u
- [DC] the head is freely rewritten on update; only the tape carries append discipline ^c20260712-11u
- [RJ] a single-file model with a head line inside the tape — rewriting the head would break the tape's append-only economics ^c20260712-11u
- [PR] mutable aggregates live in cheap-to-rewrite surfaces (head, index row); append-only surfaces hold only frozen content ^c20260712-11u

****

## Session.Lineage

- `Session.Lineage` is how a `Chatlas.Session.Model` represents branching and forking — event-level references on the linear tape, not a tree spine
- the canonical tape is linear-chronological — the order events were recorded, not a branching tree
- an event may reference a prior event as its origin; the tree is a projection derived from those references, never the spine
- the active/visible path is the default read; abandoned branches stay on the tape as preserved evidence

****

## Normalization.Pipeline::Chatlas.Session.Model

- `Normalization.Pipeline::Chatlas.Session.Model` is the Chatlas instantiation of `Normalization.Pipeline` — provider sessions normalized into `Chatlas.Session.Model`
- `Normal.Model` = `Chatlas.Session.Model`; its `Session.Event.Tape` is the ordered structure assembled fragments build
- `Raw.Source`s are provider session artifacts (transcripts, rollouts, index files); `Raw.Normalizer`s are per-provider (claude-code, codex, copilot, …)
- the native→neutral decision lives as code in the `Raw.Normalizer` and as neutral-side commitments in `Chatlas.Session.Model.Contract` — the code is the descriptor of the mapping
- `Normalizer.Context` is provider-scoped — one provider's session artifacts, loaded once per assembly
- the `Normal.Assembler` produces the target a caller needs over `Chatlas.Session.Model`: a lite session ref, an index row, or a full session
- two assembly regimes meet here — flat session metadata merges by path; `Session.Event.Tape` events assemble by order + `Session.Lineage`
- [CT] `Raw.Normalizer`s read raw only from the `Raw.Archive` — never from provider-home paths ^c20260714-1u

****

## Delta.Normalization::Chatlas

- [DF] `Delta.Normalization::Chatlas` is the application of `Delta.Normalization` to `Normalization.Pipeline::Chatlas.Session.Model`, enabled by the append-friendly `Session.Event.Tape` ^c20260712-14u
- [PR] cost scales with what changed, not with session size — the active session pays for its new turns, not its history ^c20260712-14u
- [CT] full re-derivation reads `Raw.Archive`, honoring the depot boundary: delta passes never read `Provider.Home` ^c20260712-9u

****

## Normalization.Delta.Checkpoint::Chatlas

- [DF] `Normalization.Delta.Checkpoint::Chatlas` is the per-session checkpoint of `Delta.Normalization::Chatlas` — the frozen/volatile boundary in the raw record stream plus the state to resume derivation past it ^c20260712-15u
- [DC] it lives with the scanner's derivation caches under the Chatlas depot, beside — never inside — the `Session.Model.Artifact` ^c20260712-15u

****

## Normalization.Trust.Tier::Chatlas

- [DF] `Normalization.Trust.Tier::Chatlas` is the tier choice surfaced through the Chatlas update ladder — callers of `agentos chatlas update` pick how much verification a refresh pays for ^c20260712-16u
- [PR] applications choose their point: a fast caller accepts a possibly-stale normal model; a caller needing certainty pays for verify or rebuild ^c20260712-16u
- [CT] `Raw.Archive` preservation is what licenses the cheap tiers — a stale or wrong normal model is recoverable, lost raw is not ^c20260712-16u

****

## Chat.Semantic.From.File.Content

- `Chat.Semantic.From.File.Content` means Chatlas derives chat meaning from the provider artifact's own content
- chat semantic fields include timestamps, identity, lineage, messages, tool events, titles, paths, and activity signals
- external storage signals are not chat evidence — filesystem metadata is the common negative example
- `Raw.Normalizer`s may use external storage signals for artifact management, but not to populate `Chatlas.Session.Model` or semantic `Chatlas.Session.Index` fields
- if provider content does not carry a semantic value, Chatlas should emit absence or an explicit content-derived fallback
- rebuilding the same artifact content in another archive, checkout, or storage backend should produce the same chat semantics

****

## Chatlas.Anchory

- `Chatlas.Anchory` is the Chatlas application of `Anchory.System` — anchors standing for turn neighborhoods on the `Chat.Surface`
- its `Anchory.Depot` lives at `<chatlas-root>/anchory/`; every action uses the active Chatlas depot
- the anchor key convention is the composed grammar `c<YYYYMMDD>-<N>u`: the `chatlas` namespace prefix, the primary support turn's date, a daily counter, and the user-evidence tag ^c20260718-3u
- [DC] every newly minted Chatlas anchor carries `u` because every `Chat.Support.Set` member is a user turn; surrounding assistant content is recovered through neighborhood reading ^c20260718-3u
- [CT] Index grounding-provenance lint rejects a resolved Chatlas citation whose key does not carry the `u` user-evidence tag ^c20260725-2u
- Chatlas owns the `Anchory.Record` payload and the traversal from record to session and turn neighborhood
- [CT] the record format is `chatlas.support-set.v2`: an ordered `members` list whose entries identify exact turns by full session identity plus `Normal.Turn` identity, retaining `at` only for readability and integrity checking ^c20260728-2u
- registration validates every member resolves to a visible user turn and copies its event timestamp; it never selects a turn by timestamp proximity
- [DC] registration echoes every member neighborhood — the minting agent double-checks the complete support set before tagging lines
- [CT] a chat anchor resolves to its `Chat.Support.Set`; you land on the set and read the neighborhoods ^c20260715-5u
- record format: `appendix/Chatlas.Anchory-appendix.md`
- [PR] chatlas anchory and the chatlas query language are one system, co-designed — anchors are native selectors of the query language ^c20260708-2u
- [DC] the anchor key's date is the evidence turn's date, not the minting date — a wrong date means a new anchor, never an amendment ^c20260706-0u
****

## Chatlas.View

- [DF] `Chatlas.View` is a closed operation on the model space: normal model objects + env + prompt → a normal model object
- [CT] a view always returns a `Chatlas.Session.Model` object or fragment — the output vocabulary never leaves the model space
- [DC] closure makes views composable: any view's output is a legal input to any view
- [DC] the prompt term admits agentic views — an agent-driven transformation is still a view when its result is a model object
- [DC] materialized products are views too: the legacy named-view system will be reworked so every product is a model object; rendering to human formats is a terminal step outside the algebra

****

## Chatlas.Filter

- [DF] `Chatlas.Filter` is the shape-preserving view: a normal model object in, the same shape out, content reduced
- [DC] filters compose freely, applied in order; a named filter is a registered preset
- [DC] parameterized selection (`--contains`, `--role`, `--around`) runs on the same filter pipeline behind ergonomic flags
- [EX] `turns`: message events only, provenance plumbing stripped — the grounding reader's preset

****

## Chatlas.Local

- [DF] `Chatlas.Local` is a project-local Chatlas export surface that carries attributed chat evidence inside an Agentos project tree
- [CT] its session set is `Projects.Chats`: the selected Agentos project plus contiguous Agentos-project ancestors
- [DC] its content shape is `Chatlas.Session.Model` JSON reduced by `Chatlas.Filter/turns`
- [PR] it gives grounding-relevant turns a stable project-relative home while global Chatlas remains the canonical query, resolution, and grounding depot
- [DC] sync refreshes computed session files by `identity_hash` and preserves other local files in the surface

****

## Chat.Support.Set

- [DF] `Chat.Support.Set` is the ordered, relevance-sorted set of `Chat.Surface` user turns that support an anchored statement ^c20260716-1u
- [CT] support turns are user turns only — the authority moments; assistant content is recovered by neighborhood reading ^c20260715-5u
- [DC] a support set may hold a single turn when one turn is the actual support, or many when the fact spans them ^c20260715-5u
- [DC] the set is relevance-sorted — a reader consumes top-down, as deep as its budget allows ^c20260715-5u
- [DC] support turns may be typed: a `Turn.Type` names the role a turn plays for the annotated statement, orthogonal to the sort order ^c20260716-2u
- [DC] an untyped member is plain evidence — the default role; typed members carry specific duties ^c20260716-2u
- [EX] `Turn.Type::Project.Index.Gate` — the turn where the user approved the line's verbatim text onto the index ^c20260716-2u ^c20260716-10u
- [PR] types make gates checkable: a surface's gate can require a turn of a given type in every line's set — presence is CPU-lintable, correspondence stays an agent check ^c20260716-2u
- [PR] anchor the authority, read the content around it — the user reaction is the touch event; the idea it reacts to is the neighborhood ^c20260715-5u
- [DC] registration echoes the set's neighborhoods for the minting agent to verify ^c20260715-5u
- [DC] the support set is a general primitive: any anchored statement has one, whatever surface it lives on; specializations name the subject — `Support.Set::Index.Line` is an `Index.Line`'s set ^c20260716-15u

### meta

- aliases: `Support.Set`, `Anchor.Support.Turns`, `Anchor.Landing.Turns`

****

## Turn.Type

- [DF] `Turn.Type` is the role a member turn plays inside a `Chat.Support.Set` — a per-member tag, orthogonal to the set's relevance sort ^c20260716-3u
- [DC] the untyped member is the default: plain evidence for the annotated statement ^c20260716-3u
- [DC] the vocabulary is soft and extensible (`Concept.Hardness`) — a new type is an index edit, mirroring `Line.Type.Vocabulary` ^c20260716-3u
- [DC] gates consume types by name: a surface gate may require a turn of a given type in every line's set; the linter checks presence, the agent checks correspondence ^c20260716-3u
- [DC] gate types follow the surface: each `Verbatim.User.Gated` surface names its own gate type — `Turn.Type::<Surface>.Gate` ^c20260716-10u
- [EX] `Turn.Type::Project.Index.Gate` — the turn that opened the project index gate for a line's verbatim text; required by the `Project.Index`'s gated surfaces ^c20260716-10u

### meta

- aliases: `Turn.Type::Index.Approved` (of `Turn.Type::Project.Index.Gate`)

****

## Chat.Agendix

- [DF] `Chat.Agendix` is the agendix of a chat: `Index.Line`s attached to the chat itself — the `Touched.Surface.Index` member whose attachment point is the `Chat.Surface` ^c20260717-2u
- [DC] a line grounds through its `Chat.Support.Set`: a claim may involve several turns — the set carries them all ^c20260717-1u
- [DC] one member is the attachment turn — the line's tape position and ordering key, typed `Turn.Type::Attachment`; a single-turn set attaches where it grounds ^c20260717-1u ^c20260717-2u
- [DC] its axes: ungated, tape-ordered — lines sort by their attachment turn, a kernel pass over the chat length, not a relevance sort ^c20260713-7u
- [CT] terminal: it never drains — nothing promotes out of it; it digests the chat where the chat is, an inbox for no one ^c20260713-6u
- [DC] consumers cite the chat evidence, never the agendix line — a reading aid over the source, a cache with no authority of its own ^c20260713-6u
- [DC] on a closed chat the digest converges: a finished tape admits a stable, complete pass ^c20260713-6u
- [DC] provenance is hard: every line anchored to its turns — the agendix of a chat is chat indexing in the most literal sense ^c20260713-7u
- lint follows the gate pattern: exactly one attachment per line is CPU-checkable presence ^c20260717-1u
