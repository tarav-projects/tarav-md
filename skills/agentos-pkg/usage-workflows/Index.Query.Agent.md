# Index.Query.Agent

Operational guide for an agent performing an index query. Load this file when you are the agent doing the retrieval — either directly or as a spawned subagent.

This file is self-sufficient — it carries everything you need to search the index and return good results. [`Usage.Workflow`, `Index.Agent`]

## Index Structure

The Agentos Index is a flat set of concept blocks organized across anonymous files.

- **Routing table** (`index/000-index.md`) — maps every concept name to its flat file. Always start here. Entries use `Dotted.Notation` (e.g., `Kernel.Writing`, `Index.Architecture`). Entries annotate appendix depth: `Concept.Name[+N]` when appendix pages exist.
- **Flat index files** (`100-index.md`, `101-index.md`, ...) — anonymous containers of concept blocks separated by `****`. Each block is anchored by an H2 heading naming the concept.
- **Appendix** (`appendix/Concept.Name-appendix.md`) — on-demand depth for any concept. Check if it exists when the index block isn't sufficient. No outlink required — the naming convention is the discovery mechanism.
- **Local index** (`notes/index/`) — project-local concepts with their own router (`001-index.md`) and range (`300-499`). Same format.

## Search Procedure

1. Read `index/000-index.md` — find the concept names relevant to the query.
2. Load the flat file(s) containing those concepts.
3. If a block references other concepts that matter for the query, follow them.
4. If a block's depth is insufficient, check `appendix/Concept.Name-appendix.md` for extended content.
5. If the query may involve project-local concepts, also check `notes/index/001-index.md`.

Search is a cascade — start narrow (routing table → specific blocks), widen only as needed (related blocks → appendix → local index).

## Query Quality

- name concepts in `Dotted.Notation` when possible — the routing table resolves names directly
- specific queries outperform vague ones — "what is `Vertical.Slice`?" finds faster than "tell me about implementation"
- if the caller provided context (chat summary, loaded blocks, topic scope), use it to narrow the search — don't re-discover what's already known

## Returning Results

- **cite sources** — every returned concept references its source block and flat file (e.g., "`Vertical.Slice` from `102-index.md`")
- **distinguish discovery from inference** — if you inferred something not stated in the index, say so explicitly
- **cite appendix sources** — when depth was loaded from appendix, name the appendix file
- **do not paraphrase without citation** — the caller needs traceability to verify and maintain
- **return the useful content, not just pointers** — the caller should be able to use your results without loading the index themselves
- **be concise** — return what the query needs, not a dump of everything loaded

## Cross-Index Queries

When the query may span multiple indexes:

- search the most likely relevant index first (usually the active project's package index)
- load only useful blocks from secondary indexes
- qualify concepts from non-default indexes with package names (e.g., `agentos-chatlas-pkg/Session.Archive`)
- if concepts disagree across indexes, surface the disagreement — do not silently merge

## Boundaries

- this is read-only — do not write to the index, propose blocks, or modify routing
- do not invent concept names that don't exist in the index — if a concept is missing, say it's not indexed
- if the query cannot be answered from the index, say so and suggest where the answer might live (code, skills, live notes)
