# Chatlas View Model - design-session

## Session.Abstract

- **Intent:** Design the `Chatlas.View.Model` — the unified abstract model for Chatlas views as named operations over session sets.
- **State:** Active — first block captured, candidate concept list open.
- **Active focus:** All candidate concepts captured.
- **Next:** Review full Design.Index for coherence. Consider consolidation or impl-req handoff.

## Design.Index

### View.Identity

- `View.Identity` is the tuple `(View.Name, Session.Set, Driving.Prompt)` that addresses a view instance
- it is the dispatch key — how you select which view you are talking about
- a view is selected by its name and all its arguments, analogous to multiple dispatch
- `View.Name` is a string — the registered operation name
- `Session.Set` is a normalized, deduplicated sequence of session identifiers sorted by `identity_hash`
- the canonical session identifier within the set is `identity_hash`
- `Driving.Prompt` is an optional caller-provided prompt — empty by default
- `Cache.Key` is derived deterministically from `View.Identity`
- two references to the same `View.Identity` resolve to the same storage depot
- the depot may contain different versions over time — identity is addressing, not content equivalence

### Session.Set

- `Session.Set` is a normalized, deduplicated, sorted array of `identity_hash` strings
- it is the argument side of `View.Identity` — the data scope a view operates on
- normalization: extract `identity_hash` from each session, deduplicate, sort lexicographically
- normalization is automatic at the framework boundary
- any collection of sessions that resolves to the same canonical array is the same `Session.Set` — a query result, an explicit id list, a filtered index
- a `Session.Set` does not remember how it was constructed — origin is not part of identity
- the view framework treats size 1 and size N uniformly
- `Session.Set` must contain at least one element
- the full session data is resolved separately and passed to the workflow as runtime context

### View.Workflow

- `View.Workflow` is the protocol a named view operation implements
- it defines what the view does — how it checks status, produces artifacts, and describes its contract
- each `View.Name` maps to exactly one `View.Workflow` registration
- a workflow declares its name, artifact contract, and dependencies
- a workflow implements status checking — is the materialized view fresh, stale, or missing?
- the workflow receives resolved session data at runtime — it does not perform session selection

### View.Class

- `View.Class` distinguishes view workflows by their production mode
- the two classes are `Programmatic.View` and `Agentic.View`
- both share the `View.Workflow` common surface — status, artifact contract, name, dependencies
- the framework routes production based on which class a workflow belongs to

### Programmatic.View

- `Programmatic.View` is a view whose production is programmatic
- the framework produces it directly — no agent, no staging
- production is deterministic and cheap relative to the session data

### Agentic.View

- `Agentic.View` is a view whose production requires an external agent
- the framework prepares a production prompt and a staging area
- an agent produces the artifact; the framework commits the result

### View.Context

- `View.Context` is the resolved runtime state the framework provides to a workflow
- it binds a `View.Identity` to everything the workflow needs to operate
- it contains: the workflow, the session data, the cache key, and the storage location
- the framework resolves context before calling any workflow method
- the workflow does not resolve its own context — it receives it
- context resolution is where `Session.Set` normalization happens
- the context is a standardized object — workflows receive a uniform interface
- from the context, a workflow can call back into the framework — including resolving other views

### Context.Resolution

- `Context.Resolution` is the framework step that produces a `View.Context` from a `View.Identity`
- it normalizes the `Session.Set`, computes the `Cache.Key`, resolves the storage depot, and binds the workflow
- resolution does not eagerly resolve dependencies — it produces a context the workflow can operate from
- dependency resolution is on-demand — a workflow that depends on another view resolves it through the framework at runtime
- this keeps context lightweight and avoids resolving unused dependency trees

### Cache.Key

- `Cache.Key` is a deterministic hash derived from `View.Identity`
- same identity always produces the same key
- computed, never assigned — a pure function of `View.Identity`

### View.Depot

- `View.Depot` is the storage location for a materialized view instance
- derived from `View.Name` and `Cache.Key`
- the depot holds the current materialized version — it is not a history

### Driving.Prompt

- `Driving.Prompt` is an optional caller-provided prompt that customizes an `Agentic.View` production
- empty by default — most views don't use it
- when present, it is part of `View.Identity` — different prompts produce different views
- the prompt is stored in the view manifest or artifact for traceability
- the framework can expose registered prompts for exploration
- prompt discipline is the caller's responsibility — the framework does not normalize prompt text

### View.Freshness

- `View.Freshness` is whether a materialized view is up to date with its inputs
- states: `fresh`, `stale`, `missing`
- `fresh` — the depot content was produced from the current inputs
- `stale` — the depot has content but inputs have changed since production
- `missing` — no materialized content in the depot
- freshness is checked by comparing fingerprints — a hash of the inputs at production time vs current inputs
- for `Programmatic.View`, stale triggers automatic re-production
- for `Agentic.View`, stale signals that production is needed but does not auto-trigger
- each workflow defines how it fingerprints its inputs

### View.Dependency

- `View.Dependency` is a view that a workflow requires as input to its own production
- a dependency is another view — it has its own `View.Identity`, `View.Depot`, and `View.Freshness`
- dependencies are declared by the workflow, resolved on demand through the `View.Context`
- freshness propagates through dependencies — if a dependency is stale, the dependent view is stale
- dependency chains are acyclic — a view cannot transitively depend on itself

### Artifact.Contract

- `Artifact.Contract` is what a view declares it will produce
- it names the primary artifact and any required artifacts
- it declares the content type
- the contract is part of the workflow registration — it does not change per invocation
- the framework validates that production satisfies the contract before committing

### View.Stage

- `View.Stage` is a temporary working directory where an external agent writes its output
- the framework creates the stage before agent production begins
- the stage is isolated from the depot — the agent cannot corrupt a previous materialization
- a stage carries metadata: which view, which parameters, which artifact contract
- staging only applies to `Agentic.View`

### View.Commit

- `View.Commit` is the framework step that promotes a stage into the depot
- it validates that the stage satisfies the `Artifact.Contract`
- it records observed dependency fingerprints for `View.Freshness`
- it atomically replaces the depot content
- only the framework commits — the agent writes to the stage, never to the depot directly
- for `Programmatic.View`, the framework writes to the depot directly — no staging needed

## Session.Notes

## Session.Log

- 2026-05-20: Session opened. View.Identity block captured from in-chat alignment.
- 2026-05-20: Session.Set block captured.
- 2026-05-20: View.Workflow, View.Class, Programmatic.View, Agentic.View blocks captured.
- 2026-05-20: View.Context and Context.Resolution blocks captured.
- 2026-05-20: Cache.Key, View.Depot, Driving.Prompt blocks captured. View.Identity updated to triple.
- 2026-05-20: View.Freshness block captured.
- 2026-05-20: View.Dependency block captured.
- 2026-05-20: Artifact.Contract block captured.
- 2026-05-20: View.Stage and View.Commit blocks captured. All candidate concepts covered.
