> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Chatlas.Query.Surface

- `Chatlas.Query.Surface` is the Chatlas session discovery interface family.
- `agentos chatlas index query` is the base query surface over Chatlas session index rows.
- `agentos chatlas query` is the higher-level session query surface.
- `agentos chatlas query` extends index selection with later query layers such as raw-artifact filtering, standard-model filtering, and row projection.
- The two commands may return different row shapes, but they should expose a consistent top-level query envelope.

****

## Chatlas.Time.Interface

- [DF] `Chatlas.Time.Interface` is the boundary between canonical timestamp data and human- or command-facing time semantics ^c20260807-3u
- [DC] human-facing timestamps render in the operator's local timezone by default; UTC presentation requires an explicit request ^c20260807-4u
- [DC] unzoned timestamps supplied to command and query interfaces are interpreted in the operator's local timezone by default ^c20260807-5u
- [CT] `Z` or an explicit numeric offset selects that timezone for command input, making UTC an explicit rather than implicit choice ^c20260807-6u
- [FR] internal storage and canonical machine-readable data may retain UTC timestamps ^c20260807-7u

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

- [DF] `Workflow.Update` is the update capability of one workflow: bring everything current along the path from `Provider.Home` to that workflow's target, and nothing past it ^c20260714-24u
- plain `agentos chatlas update` is itself a workflow — its target is the `Chatlas.Session.Index` ^c20260714-14u
- [CT] no update touches another workflow's caches — a stale downstream artifact is detected by its own workflow's read-time freshness check and re-derived on demand ^c20260714-19u
- [PR] a stale `Session.Model.Artifact` is an asset, not garbage — `Delta.Normalization::Chatlas` resumes from it; deleting it destroys the resume base ^c20260714-27u
- [FR] a workflow may offer forced re-materialization that ignores freshness — a correctness-testing tool, never the default ^c20260714-25u

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
- a `Provider.Home.Adapter` capability — the adapter owns all provider-home contact, including this gated deletion of captured originals ^c20260714-9u

****

## View.GC

- [DF] `View.GC` is the depot-side maintenance subsystem for deleting stale view caches — orphaned view identities, superseded parameter variants, caches of sessions no longer indexed ^c20260714-23u
- the depot sibling of `Provider.GC`, same grammar: report-first default, destructive deletion behind an explicit apply gate ^c20260714-15u
- eligibility is proven from depot evidence: view manifests checked against current `View.Identity` and the `Chatlas.Session.Index` ^c20260714-12u
- [PR] cache hygiene is an explicit maintenance action, never a side effect of update — deletion gets its own audit trail ^c20260714-28u

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
- lifecycle: `Provider.Home.Adapter` → `Raw.Archive` → `Chatlas.Session.Model` → `Chatlas.Session.Index` → `Chatlas.Query.Surface` → `Chatlas.View.Model` ^c20260714-13u
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
- [CT] provider-native artifacts are not assumed to be append-only; they may append, amend, rewrite, truncate, or otherwise evolve according to provider-specific semantics ^c20260807-59u

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
- [CT] the update pipeline's native scan is the only Chatlas system that reads `Provider.Home`; query and view surfaces answer from the depot ^c20260712-36u

****

## Scan.Scope

- [DF] `Scan.Scope` is the selection an update run hands the `Provider.Home.Adapter`'s scan: which sessions the scan considers — everything configured, one provider, one instance, one session, or an activity window ^c20260714-22u
- [CT] narrowing the scope never changes the mechanics — every scoped run performs the same discover → signature-compare → archive → derive stages over its selection ^c20260714-18u
- [PR] a single-session refresh is the whole pipeline at one-session scope, not a parallel code path ^c20260714-26u
- cold-cache trust and `--full-scan` are comparison policies, orthogonal to scope — scope picks the candidates, policy picks how hard to look at them ^c20260714-11u

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

- [DF] `Provider.Home.Adapter` is the Chatlas component owning all `Provider.Home` contact for one provider family — discovery scan, change signatures, archive copy, home-query diagnostics, and provider-GC eligibility checks ^c20260714-21u
- [CT] it is the only component that touches the `Provider.Home` filesystem — every other Chatlas system answers from the depot or reaches provider data by means of the adapter ^c20260714-17u
- [CT] the adapter provides the files of the `Raw.Archive` ^c20260714-20u
- [PR] one component owning the entire provider-home contact surface keeps the depot boundary auditable ^c20260714-29u

****

## Provider.Home.Query

- `Provider.Home.Query` is the read-only discovery layer over a `Provider.Home`
- finds provider-native sessions or artifacts directly in the provider home, outside the Chatlas archive
- returns provider-home matches or locators, not `Chatlas.Session.Index` rows
- used when freshness or direct source lookup matters before relying on archived material
- does not mutate `Raw.Archive` or `Chatlas.Session.Index`
- [CT] a diagnostic surface, not a query path — `Chatlas.Query.Surface` never routes through it ^c20260712-25u
- a capability of the `Provider.Home.Adapter` — the same discovery machinery exposed as a diagnostic read ^c20260714-10u

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
- [CT] the model carries chat data, never a consumer's interpretation of it — what a turn or event means to a downstream application is that application's read, not a model field ^c20260728-25u
- [PR] the boundary is what keeps the model general: every consumer's semantics would otherwise accrete into the standard until it stopped being about chat ^c20260728-52u

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

- [DF] `Session.Event.Tape` is the canonical ordered ledger of typed event places identified by `Event.Address` ^c20260807-37u
- [CT] an event place is established when the event is first detected and does not depend on the event reaching a final state ^c20260807-39u
- [DC] `Event.Amendment` evolves events at existing places while `Event.Append` extends the ordered address sequence ^c20260807-40u
- the tape is the single source of truth; every higher-level view of the session is a projection derived from it
- one event captures one thing that happened in the session
- an event carries its identity, its order, its kind, who produced it, its content, and a link back to raw evidence
- projections are derived and disposable — rebuildable from the tape, never authoritative on their own
- [DC] the tape materialization is a JSONL file containing one currently observed event state for each `Event.Address`, ordered by `sequence` ^c20260807-47u
- [DC] each tape line carries derivation and integrity metadata beside its payload: `source_refs`, a `source_hash`, and an artifact chain hash; none determines `Event.Address` ^c20260807-48u
- [RJ] guaranteed event finality is not part of `Chatlas.Session.Model`; lifecycle information is expressed through best-effort `Event.Closed.Estimate` ^c20260807-49u
- [FR] incremental normalization may choose its recomputation scope heuristically while preserving the address invariants of `Event.Amendment` and `Event.Append` ^c20260807-54u
- [RJ] serving reads through a checkpoint overlay of shadow events — the tape on disk is always the complete served tape ^c20260712-104u
- [PR] per-line provenance turns staleness detection mechanical: divergence is located at a line, recomputation starts there, never from zero ^c20260712-96u
- [DC] `sequence` carries tape position and is the only positional field — order is a real tape property, identity is not derived from it ^c20260728-30u
- [RJ] `event_id` as a distinct field: it was `"event-" + sequence`, a stringified duplicate whose name invited durable references onto an ordinal — retired to a contract tombstone ^c20260728-55u
- [EX] anchors keyed on `event_id` mis-pointed after re-segmentation: a stored user turn slid three ordinals while its timestamp held, and the position it vacated resolved to a later assistant turn ^c20260728-48u
- [DC] durable references key on an `Event.Grouping` carrying a stability contract — `Normal.Turn` for chat evidence ^c20260728-32u

****

## Event.Address

- [DF] `Event.Address` is the stable opaque locator of one event place in a `Session.Event.Tape` ^c20260807-9u
- [DC] its canonical representation is a hash assigned when a `Raw.Normalizer` first detects the event ^c20260807-12u
- [CT] the address remains fixed while the detected event’s normalized content evolves through amendments ^c20260807-15u
- [CT] an address is deterministic and unique within its `Chatlas.Session.Model` ^c20260807-14u
- [DC] each `Raw.Normalizer` chooses an address derivation appropriate to its provider-native raw model ^c20260807-11u
- [RJ] `Chatlas.Session.Model` does not prescribe a universal set of raw coordinates or native identifiers for address derivation ^c20260807-10u
- [CT] mutable event content cannot determine the address because an amendment may change that content without creating another event ^c20260807-13u

****

## Event.Hash

- [DF] `Event.Hash` is the deterministic content digest of one `Session.Event.Tape` event ^c20260731-200u
- [DC] its canonical input is the event data that `Chatlas.Session.Model` considers the event's content ^c20260731-158u
- [CT] `Event.Hash` excludes `Event.Annotation`, tape position, grouping identity, native identifiers, and derivation bookkeeping ^c20260731-40u
- [PR] the hash projection is a semantic model judgment about what constitutes event content, even when its concrete digest algorithm is an implementation detail ^c20260731-239u
- [CT] moving or re-annotating an unchanged event does not change its `Event.Hash` ^c20260731-94u

****

## Event.Ref

- [DF] `Event.Ref` is a durable reference to one event place carrying an assertion about an observed state of that event ^c20260807-16u
- [DC] its canonical object carries `event_address` and `event_hash` ^c20260807-17u
- [CT] `event_address` locates the event place while `event_hash` asserts the event content observed there ^c20260807-20u
- [EX] a consumer comparing the assertion with current content may describe an equal hash as `MATCHED` ^c20260807-18u
- [EX] a consumer may describe an existing address with different current content as `AMENDED` ^c20260807-19u
- [EX] a consumer may describe an address absent from the inspected model as `MISSING` ^c20260807-21u
- [CT] `sequence` may aid presentation or diagnostics but is not part of durable event identity ^c20260807-22u

****

## Event.Closed.Estimate

- [DF] `Event.Closed.Estimate` is the normalized event field expressing Chatlas’s best-effort estimate that an event is closed at the observed raw-data horizon ^c20260807-38u
- [CT] the estimate does not guarantee that the provider completed the event or that later raw evidence cannot amend it ^c20260807-41u
- [DC] each `Raw.Normalizer` decides how to derive the estimate from its provider-native observations ^c20260807-42u
- [FR] consumers may use the estimate when choosing recomputation or verification scope ^c20260807-43u
- [EX] a delta consumer may combine closed estimates with a bounded suffix check, such as re-evaluating the last portion of the tape ^c20260807-44u
- [CT] the estimate does not determine `Event.Address`, event count, or event identity ^c20260807-45u
- [CT] `Event.Hash` excludes `Event.Closed.Estimate` because the estimate describes normalization confidence rather than event content ^c20260807-46u

****

## Event.Amendment

- [DF] `Event.Amendment` is a provider-normalizer classification for a raw-model change treated as further evolution of already-detected event places ^c20260807-23u
- [DC] each `Raw.Normalizer` owns both amendment classification and the semantics of the resulting field changes ^c20260807-25u
- [CT] if a raw-model change is classified only as an `Event.Amendment`, the ordered sequence of `Event.Address` values remains identical across normalization ^c20260807-24u
- [CT] an `Event.Amendment` cannot change normalized event count or order ^c20260807-26u
- [FR] an amendment may add, remove, or change normalized event fields while preserving each event’s address ^c20260807-27u
- [CT] an amendment changes `Event.Hash` whenever it changes fields covered by that hash ^c20260807-28u
- [RJ] inserting, removing, or reordering normalized event places cannot be classified as an `Event.Amendment` ^c20260807-29u
- [PR] provider conformance tests should compare materializations before and after representative native amendments ^c20260807-34u

****

## Event.Append

- [DF] `Event.Append` is a provider-normalizer classification for a raw-model change that introduces newly detected event places after the existing normalized tape ^c20260807-35u
- [DC] each `Raw.Normalizer` determines append equivalence from the semantics of its provider-native raw model ^c20260807-32u
- [CT] after an `Event.Append`, the complete prior sequence of `Event.Address` values remains an unchanged prefix of the new sequence ^c20260807-33u
- [CT] an append cannot change the address of any previously detected event place ^c20260807-30u
- [RJ] a change that inserts, removes, or reorders an existing event place cannot be classified solely as an `Event.Append` ^c20260807-31u
- [PR] provider conformance tests should compare materializations before and after representative native appends ^c20260807-36u

****

## Event.Annotation

- [DF] `Event.Annotation` is normalization-owned derived metadata attached to a `Session.Event.Tape` event without changing the event's content ^c20260731-197u
- [DC] an event carries annotations through an optional top-level `annotations` object ^c20260731-134u
- [CT] absence of `annotations` means the event carries no annotations ^c20260731-64u
- [DC] each annotation kind is a key whose value is a kind-specific object ^c20260731-147u
- [DC] annotation kinds are open and independent; one event may carry several kinds ^c20260731-137u
- [DC] annotation assignment is normalization work owned by the corresponding `Raw.Normalizer` ^c20260731-136u
- [CT] annotations remain outside `Event.Hash` because they annotate event content rather than constitute it ^c20260731-70u

****

## Event.Grouping

- [DF] `Event.Grouping` is a semantic collection of `Session.Event.Tape` events derived through `Event.Annotation` ^c20260731-199u
- [DC] a grouping annotation kind assigns an identifier to its member events; events carrying the same kind and identifier form one group ^c20260731-127u
- [CT] the tape remains the single source of truth; collecting a group is software over annotations, never an authoritative container ^c20260731-110u
- [DC] grouping kinds are open and orthogonal; one event may participate in several independent groupings ^c20260728-35u
- [CT] grouping is partial; an event may belong to no group of a given kind ^c20260728-21u
- [DC] normalization owns each grouping kind's semantic and annotation assignment ^c20260728-38u
- [EX] `Normal.Turn` is the chat-semantic grouping; a request/response cycle may be another ^c20260731-222u

****

## Event.Group.Hash

- [DF] `Event.Group.Hash` is the deterministic content digest of one `Event.Grouping` ^c20260731-198u
- [DC] its canonical input is the ordered sequence of member `Event.Hash` values in tape order ^c20260731-159u
- [CT] it excludes the grouping annotation kind and identifier ^c20260731-87u
- [CT] changing member content, membership, or order changes the group hash ^c20260731-75u
- [CT] assigning the same unchanged members another group identifier does not change the group hash ^c20260731-73u
- [CT] `Event.Group.Hash` asserts grouped content rather than group identity; content-equivalent groups may share a hash ^c20260731-39u

****

## Normal.Turn

- [DF] `Normal.Turn` is the normalization-owned `Event.Grouping` for one chat-semantic turn ^c20260731-210u
- [DC] it is realized through `annotations.normal_turn.id`, whose value is a `Normal.Turn.Id` ^c20260731-155u
- [CT] assigning `Normal.Turn` groups existing `Session.Event.Tape` events; it does not change their generation, payload, role, producer, sequence, or meaning ^c20260731-72u
- [DF] `Normal.Turn::User.Turn` groups normalized events carrying the data supplied in one user interaction ^c20260731-209u
- [DC] a `Raw.Normalizer` assigns `User.Turn` membership from normalized event semantics rather than inheriting provider record boundaries or raw role labels ^c20260731-124u
- [CT] a `User.Turn` has no semantic relationship to preceding or following assistant activity ^c20260731-49u
- [EX] user-turn data may include text, images, files, attachments, and structured command arguments ^c20260731-228u
- [PR] user-turn purity protects `User.Authority`; grouping assistant or injected data into a `User.Turn` corrupts that authority boundary ^c20260731-241u
- [DC] `Normal.Turn::Assistant.Turn` is grouped independently and may span reasoning, messages, tool activity, and response metadata ^c20260731-118u
- [DC] each `Raw.Normalizer` maps native handles onto the semantic; a native grouping that over-merges is refined, never inherited ^c20260728-33u
- [CT] Chatlas supplies turn grouping and identity, never turn interpretation; consumer meanings such as `Turn.Type` remain outside the model ^c20260728-19u

****

## User.Turn.Purity

- [DF] `User.Turn.Purity` is the integrity requirement that `Normal.Turn::User.Turn` contain only data submitted through the session’s user-input boundary in one interaction ^c20260809-2u
- [CT] user attribution identifies the user-input boundary; it does not claim that a human authored or typed the data ^c20260809-1u
- [DC] `Raw.Normalizer` assigns user-turn membership from normalized input semantics and provenance rather than provider transport roles ^c20260809-3u
- [RJ] provider-generated, assistant-generated, developer-injected, preset, and synthetic recap content cannot enter a `User.Turn` merely because its raw record carries role `user` ^c20260809-4u
- [CT] content excluded from `User.Turn` remains first-class on `Session.Event.Tape` under an event semantic matching its actual source role ^c20260809-6u
- [CT] a query match outside a qualifying `User.Turn` cannot be reported as a user-turn match ^c20260809-5u
- [PR] when evidence cannot support user-input attribution, Chatlas preserves the event and raw provenance without promoting it into a `User.Turn` ^c20260809-7u
- [DC] contaminating user-turn data with non-user-input material is normal-model data corruption ^c20260809-8u

****

## Normal.Turn.Id

- [DF] `Normal.Turn.Id` is an opaque session-local label assigned to one `Normal.Turn` ^c20260731-207u
- [CT] a `Normal.Turn.Id` must be unique within its `Chatlas.Session.Model` ^c20260731-47u
- [PR] stability is desirable because it reduces reference repairs, but correctness does not depend on it ^c20260731-238u
- [CT] `Normal.Turn.Id` locates a grouping; by itself it does not assert the grouping's content ^c20260731-41u

****

## Normal.Turn.Ref

- [DF] `Normal.Turn.Ref` is the durable, self-verifying reference to one `Normal.Turn` ^c20260731-208u
- [DC] its canonical object carries `session`, `turn_id`, `turn_hash`, and `at` ^c20260731-160u
- [DC] `session` locates the expected `Chatlas.Session.Model` ^c20260731-119u
- [DC] `turn_id` locates the expected `Normal.Turn` within that session ^c20260731-121u
- [DC] `turn_hash` is the turn's `Event.Group.Hash` and asserts its grouped content ^c20260731-120u
- [CT] `at` is readability and diagnostic metadata, not the turn's identity or selection mechanism ^c20260731-45u
- [CT] resolution verifies the assertion by recomputing the current group hash and comparing it with `turn_hash` ^c20260731-98u

****

## Session.Model.Artifact

- [DF] `Session.Model.Artifact` is the on-disk form of one `Chatlas.Session.Model` — a per-session folder of purpose-split files rather than one monolithic document ^c20260712-74u
- [DC] the folder holds a mutable head (`session.json`), the current `Session.Event.Tape` materialization (`events.jsonl`), and sibling derived projections ^c20260807-50u
- [CT] an artifact update may rewrite event states while preserving the address invariants of `Event.Amendment` and `Event.Append` ^c20260807-53u
- [CT] artifact layout and rewrite strategy do not determine event identity ^c20260807-52u
- [PR] purpose-split files keep mutable aggregates and disposable projections independent from the canonical event tape ^c20260807-55u
- [CT] `Session.Model.Artifact` freshness depends on both its raw-source observation and the applicable normalizer and model-contract revision ^c20260807-61u
- [RJ] unchanged raw artifacts do not make a cached session model fresh after a semantic normalization change that can affect its materialization ^c20260807-62u

****

## Session.Lineage

- [DF] `Session.Lineage` is the relation model connecting event origins, branches, and continuations within or across `Session.Identity` instances ^c20260806-111u
- [DC] each session retains its own linear-chronological `Session.Event.Tape`; lineage edges form the graph projected over those tapes ^c20260806-112u
- [CT] an event may reference a prior event as its origin within the same session or across a session boundary ^c20260806-113u
- [DF] a compaction-continuation edge connects the session containing the covered history to its continuation through shared `Compaction.Event` evidence ^c20260806-114u
- [CT] cross-session lineage is derived only from shared provider evidence such as boundary identifiers, logical parents, or preserved-segment references ^c20260806-115u
- [RJ] traversable lineage does not merge or duplicate predecessor events into the continuation tape ^c20260806-116u
- [CT] every event and `Normal.Turn` on every lineage path remains first-class data in its original `Session.Event.Tape` ^c20260808-37u
- [RJ] `Session.Lineage` does not classify any event or path as active, current, abandoned, inactive, or default ^c20260808-38u
- [DC] lineage relations describe provider-evidenced origins and continuations without assigning status to the resulting paths ^c20260808-39u
- [PR] preserving every `Normal.Turn::User.Turn` across branching is a primary requirement of `Session.Lineage` ^c20260808-40u
- [FR] consumers may select, rank, or project lineage paths and heads according to their own tasks ^c20260808-42u

****

## Lineage.Branch

- [DF] `Lineage.Branch` is the `Session.Lineage` structure formed when multiple event continuations share an earlier event origin ^c20260808-41u
- [DC] each continuation relation connects its event to the evidenced origin through an `Event.Ref` ^c20260808-43u
- [CT] branch relations are derived only from provider-native lineage evidence ^c20260808-44u
- [CT] `Session.Event.Tape` preserves recording chronology while lineage relations project the branching graph over its event places ^c20260808-46u
- [RJ] creating a branch relation does not invalidate, demote, or change the authority of events on another branch ^c20260808-47u
- [EX] continuations `A → B → C` and `A → D` form a branch at `A`; `B`, `C`, and `D` remain equally first-class events ^c20260808-45u

****

## Lineage.Rollback

- [DF] `Lineage.Rollback` is a provider-evidenced event recording that a continuation resumed from an earlier event origin after later events had already been recorded ^c20260807-63u
- [DC] the rollback event occupies its own chronological place on `Session.Event.Tape` and references the evidenced origin ^c20260807-64u
- [CT] rollback does not undo, delete, demote, or change the authority of previously recorded events or turns ^c20260807-66u
- [CT] rollback does not identify any resulting lineage path as active, current, or preferred ^c20260807-65u
- [CT] implicit branching without provider evidence of a rollback operation is represented through `Lineage.Branch`, not through a synthetic rollback event ^c20260807-68u
- [EX] a provider-native `thread_rolled_back` record may normalize as `Lineage.Rollback` while all affected turns remain first-class history ^c20260807-67u

****

## Compaction.Event

- [DF] `Compaction.Event` is the `Session.Event.Tape` event that records a provider compacting a conversation-history region into continuation context ^c20260806-100u
- [DC] it identifies the source-history boundary and the resulting continuation session when the raw evidence makes either addressable ^c20260806-101u
- [CT] it carries available operation facts such as trigger, time, token counts, preserved-segment coordinates, and preserved-message references ^c20260806-102u
- [DC] it references its produced `Compaction.Summary`; the operation and generated content remain separate events ^c20260806-103u
- [RJ] compaction is not flattened into an opaque session update or inferred from summary text alone ^c20260806-104u

****

## Compaction.Summary

- [DF] `Compaction.Summary` is synthetic message content produced during a `Compaction.Event` to stand in for covered conversation history ^c20260806-105u
- [DC] it is normalized as a message with semantic role `system` ^c20260806-106u
- [CT] its producer is `provider` or `assistant`, never `human` ^c20260806-107u
- [RJ] a provider-native `user` transport role does not become canonical user authorship; the raw role remains recoverable through provenance ^c20260806-108u
- [CT] it receives no `Normal.Turn::User.Turn` membership and therefore cannot serve as user authority ^c20260806-109u
- [FR] views may expose it for replay, context inspection, and discovery while preserving its synthetic origin ^c20260806-110u

****

## Normalization.Pipeline::Chatlas.Session.Model

- `Normalization.Pipeline::Chatlas.Session.Model` is the Chatlas instantiation of `Normalization.Pipeline` — provider sessions normalized into `Chatlas.Session.Model`
- `Normal.Model` = `Chatlas.Session.Model`; its `Session.Event.Tape` is the ordered structure assembled fragments build
- `Raw.Source`s are provider session artifacts (transcripts, rollouts, index files); `Raw.Normalizer`s are per-provider (claude-code, codex, copilot, …)
- the native→neutral decision lives as code in the `Raw.Normalizer` and as neutral-side commitments in `Chatlas.Session.Model.Contract` — the code is the descriptor of the mapping
- `Normalizer.Context` is provider-scoped — one provider's session artifacts, loaded once per assembly
- the `Normal.Assembler` produces the target a caller needs over `Chatlas.Session.Model`: a lite session ref, an index row, or a full session
- two assembly regimes meet here — flat session metadata merges by path; `Session.Event.Tape` events assemble by order + `Session.Lineage`
- [CT] `Raw.Normalizer`s read raw only from the `Raw.Archive` — never from provider-home paths ^c20260714-16u

****

## Delta.Normalization::Chatlas

- [DF] `Delta.Normalization::Chatlas` is the application of `Delta.Normalization` to `Normalization.Pipeline::Chatlas.Session.Model`, enabled by stable event addresses and source-aware rematerialization ^c20260807-51u
- [PR] cost scales with what changed, not with session size — the active session pays for its new turns, not its history ^c20260712-92u
- [CT] full re-derivation reads `Raw.Archive`, honoring the depot boundary: delta passes never read `Provider.Home` ^c20260712-32u

****

## Normalization.Delta.Checkpoint::Chatlas

- [DF] `Normalization.Delta.Checkpoint::Chatlas` is the per-session cache of an observed raw-data horizon and the state needed to resume a selected delta strategy ^c20260807-56u
- [CT] the checkpoint lives outside `Chatlas.Session.Model` and cannot assert event finality or determine event identity ^c20260807-58u
- [FR] a delta strategy may combine source verification, `Event.Closed.Estimate`, and bounded tape revisitation when selecting its recomputation scope ^c20260807-57u
- [CT] `Normalization.Trust.Tier::Chatlas` states whether a caller accepts heuristic reuse or requires stronger source verification ^c20260807-60u
- [DC] it lives with the scanner's derivation caches under the Chatlas depot, beside — never inside — the `Session.Model.Artifact` ^c20260712-42u

****

## Normalization.Trust.Tier::Chatlas

- [DF] `Normalization.Trust.Tier::Chatlas` is the tier choice surfaced through the Chatlas update ladder — callers of `agentos chatlas update` pick how much verification a refresh pays for ^c20260712-72u
- [PR] applications choose their point: a fast caller accepts a possibly-stale normal model; a caller needing certainty pays for verify or rebuild ^c20260712-90u
- [CT] `Raw.Archive` preservation is what licenses the cheap tiers — a stale or wrong normal model is recoverable, lost raw is not ^c20260712-23u

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
- the anchor key convention is the composed grammar `c<YYYYMMDD>-<N>u`: the `chatlas` namespace prefix, the primary support turn's date, a daily counter, and the user-evidence tag ^c20260718-33u
- [DC] every newly minted Chatlas anchor carries `u` because every `Chat.Support.Set` member is a user turn; surrounding assistant content is recovered through neighborhood reading ^c20260718-43u
- [CT] Index grounding-provenance lint rejects a resolved Chatlas citation whose key does not carry the `u` user-evidence tag ^c20260725-47u
- Chatlas owns the `Anchory.Record` payload and the traversal from record to session and turn neighborhood
- [CT] the record format is `chatlas.support-set.v2`: an ordered `members` list whose entries identify exact turns by full session identity plus `Normal.Turn` identity, retaining `at` only for readability and integrity checking ^c20260728-28u
- registration validates every member resolves to a visible user turn and copies its event timestamp; it never selects a turn by timestamp proximity
- [DC] registration echoes every member neighborhood — the minting agent double-checks the complete support set before tagging lines
- [CT] a chat anchor resolves to its `Chat.Support.Set`; you land on the set and read the neighborhoods ^c20260715-8u
- record format: `appendix/Chatlas.Anchory-appendix.md`
- [PR] chatlas anchory and the chatlas query language are one system, co-designed — anchors are native selectors of the query language ^c20260708-18u
- [DC] the anchor key's date is the evidence turn's date, not the minting date — a wrong date means a new anchor, never an amendment ^c20260706-3u
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

- [DF] `Chat.Support.Set` is the nonempty set of exact `User.Turn`s an agent judges to support one grounded statement ^c20260802-184u
- [DC] its current record preserves members as a duplicate-free, relevance-ordered list so readers can consume the strongest support first ^c20260802-156u
- [DC] membership alone gives a turn its base-support role; a member with no `Turn.Type` annotation is plain support ^c20260802-159u
- [DC] a member may carry one or more `Turn.Type` annotations for additional roles without losing its base-support standing ^c20260802-141u
- [CT] annotations do not select support, change membership, or impose an ordering key ^c20260802-111u
- [DC] one set may contain a single turn or several turns when the statement spans them ^c20260802-161u
- [CT] the current Index-grounding realization accepts visible user turns only; assistant content is recovered through their neighborhoods ^c20260802-134u
- [PR] anchor the authority turns and read their neighborhoods — the user turn carries touch while surrounding content supplies context ^c20260802-204u
- [DC] registration echoes every member neighborhood for agent verification ^c20260802-165u
- [CT] `Chat.Support.Set` realizes `Support.Set` for chat evidence without restricting the general support model to chat ^c20260802-107u

### meta

- aliases: `Anchor.Support.Turns`, `Anchor.Landing.Turns`

****

## Turn.Type

- [DF] `Turn.Type` is an optional semantic annotation on a `Chat.Support.Set` member naming an additional role the turn plays ^c20260802-190u
- [DC] absence of annotations means base support only ^c20260802-146u
- [DC] one member may carry multiple `Turn.Type` annotations ^c20260802-160u
- [CT] annotations are orthogonal to support membership and relevance order ^c20260802-110u
- [DC] the vocabulary is soft and extensible; each type consumer owns validation of its cargo ^c20260802-178u
- [EX] `semantic.approval.turn` marks an agent-judged approval member ^c20260802-195u
- [EX] `tokenized.approval.turn` marks a CPU-verifiable verbatim approval member and carries its token, proposal turn, and approval turn ^c20260802-196u

****

## Chat.Touched.Index

- [DF] `Chat.Touched.Index` is the per-session projection of `Touched.Index` involved in one `Chat.Surface` ^c20260803-74u
- [CT] its evidence is closed over the target chat; external material participates only insofar as it is observable within that chat's causal context ^c20260803-73u
- [DC] its chronological model is formed by `Chat.Index.Delta`s and its present-facing model by `Chat.Index.HEAD` ^c20260804-32u
- [DC] qualifying user turns delimit captured touched changes while preceding assistant and tool context may inform their interpretation without independently supplying touch ^c20260803-77u
- [CT] material merely loaded into a chat does not create a Delta without a qualifying user touch event ^c20260803-76u
- [CT] each Delta's extraction may be maintained using evidence within its fixed horizon but not later evidence ^c20260803-78u
- [DC] repeated exact line content may retain its `Support.Reference`; changed `Line.Type` or body requires support reevaluation and a new reference ^c20260803-79u

****

## Chat.Index

- [DF] `Chat.Index` is the materialized per-session surface of one `Chat.Touched.Index` ^c20260803-71u
- [DC] it lives at `<chatlas-root>/session-index/<identity-hash>/` ^c20260804-27u
- [DC] its primary materialized layout is `deltas/` and `HEAD.md`; the surface directory is the complete `Chat.Index` and carries no descriptor file ^c20260806-0u
- [DC] each `deltas/<turn-id>.md` file materializes exactly one `Chat.Index.Delta` identified by its `Delta.Horizon.Turn` ^c20260804-29u
- [DC] Delta order is derived by resolving each file’s `Delta.Horizon.Turn` against the authoritative Chatlas tape; filenames and timestamps do not establish ordering ^c20260806-1u
- [RJ] `Chat.Index` does not persist managed-file inventory, capture status, or findings; structure and state are derived from the Markdown surface, authoritative chat, and read-only audit ^c20260806-2u
- [DC] `HEAD.md` materializes the session's `Chat.Index.HEAD` ^c20260804-30u
- [CT] materialization on `Chat.Index` does not itself establish `Reviewed.Content`; grounding and review standing remain line-local ^c20260803-75u
- [RJ] the legacy `Chat.Ontology` and `Chat.Appendix` split does not define the redesigned `Chat.Index` layout ^c20260804-31u

****

## Chat.Index.Delta

- [DF] `Chat.Index.Delta` is a maintained chronological extraction of one or more touched changes ending at one `Delta.Horizon.Turn` ^c20260804-1u
- [DF] `Delta.Horizon.Turn` is the qualifying `User.Turn` whose causal position closes the evidence available to one `Chat.Index.Delta` ^c20260804-2u
- [CT] a delta may interpret the causal prefix ending at its horizon turn but not later evidence ^c20260803-52u
- [FR] agents may create one delta per qualifying user turn or group several touched events into one meaningful delta ^c20260804-3u
- [CT] the evidence horizon remains fixed while the extraction may be extended, corrected, or reorganized ^c20260803-48u
- [DC] delta order is established by position on the chat tape; `Normal.Turn.Ref` supplies identity while timestamps remain diagnostic metadata ^c20260803-51u
- [DC] the heading form is `Chat.Index.Delta/<turn-id> @ <timestamp>`; the horizon turn is not necessarily the delta's sole support ^c20260803-50u
- [CT] when the horizon turn exposes a timestamp, omitting it raises a blessable `POI.Instance` ^c20260803-47u
- [PR] delta lines attach preferentially to concepts visible within their evidence horizon and capture semantic change without unnecessarily restating earlier deltas ^c20260803-49u

****

## Chat.Index.HEAD

- [DF] `Chat.Index.HEAD` is the agent-maintained present-facing model resolved for one chat from its transcript and `Chat.Index.Delta`s ^c20260804-4u
- [CT] it interprets the complete chat context available within its evidence horizon rather than mechanically unioning or folding isolated delta lines ^c20260803-53u
- [FR] its maintaining agent may select existing delta lines or synthesize better line content from the chat evidence ^c20260804-8u
- [CT] every ordinary model line in `Chat.Index.HEAD` must eventually be materialized exactly in a `Chat.Index.Delta`; missing Delta coverage raises a `POI.Instance` rather than preventing the HEAD-first edition ^c20260804-7u
- [PR] a HEAD-authored ordinary model line reconciles backward into the appropriate Delta so the HEAD is not its first durable home in the reconciled state ^c20260804-6u
- [CT] a `POI.Line` may originate in `Chat.Index.HEAD` as maintenance state, but it owns a `Support.Set` grounding its claim about the indexed lines it evaluates ^c20260804-5u
- [DC] the subject lines' support sets provide the qualifying user-turn evidence from which the `POI.Line` constructs its own support set ^c20260804-9u
- [CT] its currentness is local to that chat's evidence horizon; later chats may revise the same ideas without rewriting the earlier `Chat.Index.HEAD` ^c20260803-54u
- [CT] one `Chat.Index.HEAD` may support several Project HEADs, while each project selects its present model independently ^c20260804-10u
- [RJ] resolving a `Chat.Index.HEAD` does not create a general line-to-line dependency or provenance network ^c20260803-55u

****

## Line.Home

- [DF] `Line.Home` is the canonical `Chat.Index.Delta` materialization selected as the home of one exact `Index.Line` content ^c20260804-40u
- [DC] it identifies the owning chat session and Delta coordinate ^c20260804-25u
- [DC] when exact line content has several known Delta materializations, its default `Line.Home` is the oldest evidenced materialization ^c20260804-41u
- [RJ] an independent home registry does not duplicate the home derived from exact Delta containment and authoritative tape order ^c20260806-3u
- [CT] identical line content may be materialized on several touched-index surfaces while retaining one canonical home ^c20260803-58u
- [CT] home is independent from `Support.Set`, review standing, and membership in any HEAD ^c20260806-4u
- [CT] a line may advance on a HEAD before receiving its home; missing Delta coverage raises a reconciliation `POI.Instance` rather than an authoring error ^c20260804-26u
- [RJ] assigning a home does not assert that the home contains the first known observation of the line content ^c20260803-64u
