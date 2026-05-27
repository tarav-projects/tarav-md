# Usage.Workflow: Index.Query

Read-only retrieval from the Agentos Index — the agent searches for concepts, collects context, and returns cited results. No mutation, no gates. [`Usage.Workflow`, `Index.Agent`]

## Situation

The agent or user needs conceptual grounding, design context, or navigational information from the index. No writing or mutation is involved.

## Mode Selection

### Direct

The agent loads the full index into its own context and works with it directly.

Best when the full index in context adds value beyond answering the immediate question — the agent is working *with* the index, not just *querying* it.

#### When to use

- working on the index itself (writing blocks, maintenance, diagnosis)
- a design discussion where multiple concepts interact and the agent benefits from seeing the full picture
- the agent expects multiple queries in the same session — loading once is cheaper than spawning repeatedly
- the query is exploratory — the agent doesn't know which concepts are relevant yet and needs to browse

#### How

The agent loads `index/000-index.md` (routing table), then the relevant flat files, appendix pages, and references needed for the task. The full index is ~5 flat files — loading all of them is acceptable when the session will use multiple concepts.

### Subagent

A subagent is spawned to do the index work. The caller's context is protected from full-index loading.

Best when the caller just needs an answer or a few cited blocks without polluting its own context.

#### When to use

- the caller needs an answer but doesn't need the full index in context
- grounding a discussion with a few specific concepts
- checking whether a concept exists or how it's defined
- collecting context for a handoff, report, or artifact
- the caller is in a workflow (design session, implementation) and wants to stay focused

#### How

The caller spawns a subagent and provides:

- **the prompt** — what the subagent should find or answer
- **caller context** — chat summary, already-loaded blocks, topic scope, or any framing that helps the subagent avoid re-discovering what the caller already knows

The subagent loads `Index.Query.Agent.md` from this folder, which contains everything it needs to operate. The subagent returns cited results; the caller integrates them.

## Result Expectations

Regardless of mode, query results follow the same shape:

- results are cited — every returned concept references its source block and flat file
- results distinguish discovered context from inference — if the agent inferred something not in the index, it says so
- when depth was loaded from appendix, the appendix source is cited
- paraphrasing without citation is not acceptable — the caller needs traceability

## Cross-Index Queries

When the query may span multiple indexes (e.g., `agentos-pkg` + `agentos-chatlas-pkg`), the agent searches likely relevant indexes first, loads only useful blocks, and qualifies concepts from non-default indexes with package names (e.g., `agentos-chatlas-pkg/Session.Archive`). [`Multi.Index.Operation`, `Index.Depot`]
