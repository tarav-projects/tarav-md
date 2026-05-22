> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

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

## Index.Agent

- `Index.Agent` is a role for collecting, interpreting, and returning context from the index
- can be performed by a dedicated specialist agent or temporarily by a workflow agent
- the caller sends a prompt; the `Index.Agent` scans the index, does the work, and returns a result
- the caller's context is protected — the `Index.Agent` pays the cost of loading the full index, not the caller
- useful for discovery, uncertain queries, custom context extraction, and index-grounded synthesis
- not required as the default prelude when a workflow already knows its needed cited context
- must cite source blocks in returned context so summaries remain traceable and maintainable
- not a fixed API — handles any reasonable prompt against the index
- backed by the `agentos-index-agent` skill: index conventions, block structure, routing, CLI tools, appendix discovery
- can run on a medium-size model — structured, scoped work
- the caller retains direct index access when the index *is* the work target
- the caller can pass context in the prompt — a chat summary, already-loaded blocks, a topic, a question
- common patterns: grounding (pass chat summary, get relevant blocks), search (find blocks by topic), placement (where to write a new block), filtering (return namespace members minus already-loaded blocks)

****

## Index.Depot

- `Index.Depot` is a concrete index instance — the set of files with index blocks, their appendix, and a router
- built on the `Agentos.Index.Framework` — follows the same block structure, routing, writing, and discovery conventions
- one depot = public part (skill-packaged, portable) + local part (`notes/index/`, project-specific)
- each depot is self-contained — its own router(s), its own flat files, its own appendix
- a concept lives in exactly one depot — the depot that naturally owns it
- composability: an agent loads multiple depots to build its working index
- the `Index.Agent` works across all loaded depots — it scans whatever routers are available

### meta

- aliases: `Agentos.Index.Depot`
