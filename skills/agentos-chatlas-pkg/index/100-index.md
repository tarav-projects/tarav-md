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

## Grounding.Miner

- `Grounding.Miner` is an agent that produces `Grounding.Request`s from chat and index evidence — candidate evidence, not authority.
- it has two levels that mine in opposite directions.
- L1 mines chat-to-reqs: it reads one chat session and emits a session `Grounding.Request` of `Grounding.Material` records, detected by heuristic with or without named blocks.
- L2 mines block-to-reqs: it targets one kernel block, searches the L1 session layer, confirms against the actual chat turn, then appends a block `Grounding.Request`.
- the L1 session layer acts as a hand-built retrieval index over chats — how MVP mining avoids a vector backend on constrained hardware.
- output is append-only and per-turn deduped; mining is shared across chats via a re-mine cooldown.
- it neither creates nor destroys information — it surfaces high-signal turns/sessions, converging toward exhausting the design signal in the chats.
- both levels produce `Grounding.Request`s; neither writes the index.

****

## Grounding.Miner.Locality

- `Grounding.Miner.Locality` is the placement rule for miner output — `Natural.Placement` applied to the pipeline: the two levels derive from different sources, so they live on different surfaces.
- L1 → `Chatlas.Depot`: L1 reads only the `Chat.Surface`, never a project, and serves every project; its output is derived chat data stored in the depot at `~/Documents/chatlas/grounding/`.
- L2 → target project: L2 is keyed by a project's `Index.Block`s and writes into that project's `### grounding`, so `<block-name>-gr-req.jsonl` lives in the target project (skill arg).
- L1's recorded `blocks` strings may name project concepts, but L1 only stores the strings — never resolving them — so L1 stays project-agnostic.
- relation: L1 is the shared retrieval index in the depot; L2 is a per-project consumer of it — many L2s, one L1.

****

## Grounding.Material

- `Grounding.Material` is a chat turn (or turn span) carrying durable design signal worth grounding — the fundamental core of L1 detection.
- membership is governed by `Grounding.Material.Catalog`.
- the miner neither creates nor destroys information: it surfaces high-signal turns/sessions; chats stay the SSOT.
- system goal: converge toward exhausting all design signal in the chats — coverage grows over passes, not one-shot.
- detection is heuristic, not exhaustive: a miss is a recoverable gap, never corruption.
- requires no named block; block-agnostic material is still recorded, and one turn can yield multiple records.

****

## Grounding.Material.Catalog

- `Grounding.Material.Catalog` is the maintained, ever-growing list of positive and negative criteria defining `Grounding.Material`.
- it is never assumed complete.
- it refines from a high-signal feedback sample: turns approved into a `### grounding` section, fed back into the catalog.
