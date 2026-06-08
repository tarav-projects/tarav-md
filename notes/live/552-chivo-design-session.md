# Chivo - design-session

## Session.Abstract

Design `chivo`: a general-purpose, agent-facing registry for LLM workflow reuse. A workflow is `prompt + args → result(s)`. Agents publish their work as `chivo` entries; other agents query the registry before running a new workflow, and may reuse, contest, or supersede prior answers.

The system is framework-level (not chatlas-specific). Chatlas is one potential consumer/producer. Other Agentos packages (paperson, md-library, agentos-iterante, etc.) are equally valid users.

Conceptually it sits at the intersection of three metaphors:
- **Nix/Bazel** — content-addressed, cacheable computation
- **Stack Overflow / Stack Exchange** — multiple answers per "question", ranked, contestable, accumulated
- **Secondary market** — agents reuse others' work and judgment; "usage" is the currency

Name: `chivo` (Cuban slang for cheat sheet — what students write on the back of their arm). The name carries the metaphor without picking a side.

## Design.Index

### Chivo.Concept

- A `chivo` entry is a cached unit of agent work: `(workflow definition, args, resolved prompt, result, metadata)`.
- Agents are both publishers and consumers.
- Entries are not authoritative — they are *prior work others can reuse with judgment*. The system surfaces signals (usage, recency, feedback) but does not filter; the caller decides.

### Chivo.Workflow

- Workflow = `prompt + args`
- `prompt` is natural-language; `args` are structured data
- Args may themselves be prompts (recursive composition)
- System resolves/expands the workflow into a concrete `Running.Prompt` — the actual text handed to an agent
- Workflow produces one or more result files; registered against the workflow key

### Chivo.MultiAnswer.Model

- Each workflow key can have multiple answers
- Agents may contribute new answers when:
  - existing answers don't satisfy
  - prior answers appear outdated
- Old answers are *not replaced* — accumulated. Loss of historical answer = loss of signal.

### Chivo.Lookup.Modes

- **Exact**: content-addressed hash of resolved prompt + args. Cheap, deterministic, primary path.
- **Semantic**: search agent returns plausible candidates over the key domain. Paid, fuzzy, secondary path.
- Both modes coexist. Exact handles "I know what I'm asking for". Semantic handles "is there prior work near this question?".

### Chivo.SearchAgent.Role

- Stacked-agent retrieval: a search agent matches over the key domain, returns candidate list.
- Search agent accepts both mechanistic args and natural-text search prompts (mixed query).
- Search agent does retrieval, **not judgment**. The calling agent has goal context and makes the selection.
- Mirrors retriever/reader split in RAG.

### Chivo.Selection.Reason

- When a caller selects an answer from candidates, it records *why* (free-text).
- Load-bearing feature: this is the primary signal for the next caller reading the same candidate list.
- Required at selection time, not optional.
- Richer than up/down votes.

### Chivo.Usage.Signal

- Usage is "money" — accumulated engagement is the base currency.
- Two strength tiers:
  - **Looked at** (cheap, weak): agent retrieved candidate
  - **Selected** (rich, strong): agent chose this answer over alternatives, with a recorded reason
- Treat distinctly. Don't collapse to one number.
- Caller-dependent: most-used ≠ best, but high usage = active engagement signal.

### Chivo.Feedback.Channels

Three distinct channels with different schemas/costs:

1. **Selection-reason** — required free-text on selection
2. **Comments** — optional free-text, two layers:
   - on the workflow (the question)
   - on a specific answer
3. **Polls** — structured-schema feedback, system-aggregated
   - Calling agents may not see raw poll data
   - System uses polls to inform ranking/recommendations
   - Crosses into "system has opinions" — be intentional about this line

### Chivo.Freshness.Model

- **On-demand refresh**, not scheduled/random:
  - On lookup, system prompts caller: "this answer is N old, consider refreshing"
  - Caller decides
- **Two cost tiers**:
  - **Revalidation** (cheap): "is this conclusion still supported by current evidence?" — small validator agent
  - **Re-run** (expensive): full workflow re-execution
  - Try revalidation first; only re-run if validation fails
- **Old answers are kept**, never replaced — preserves "what used to be true" signal
- **"What world it ran against"** must be captured at publish time (timestamp, dataset version, git SHA, anything else relevant) so freshness can be meaningfully judged

### Chivo.Survivorship.Mitigation

- Acknowledged risk: popular answers stay visible → attract more usage → look more popular, regardless of quality.
- Mitigation: on-demand refresh nudges + piggyback re-analysis on real queries. No random probing.
- "Constant agentic load" framing — smooth the spend, tie to actual usage, not synthetic schedules.

### Chivo.System.Stance

- Storage + retrieval = neutral plumbing
- Poll aggregations = opinions (system surfaces ranking/recommendations to callers)
- Design tension: keep poll-informed signals as **shown to callers**, not **filters applied before they see candidates**. System surfaces opinion, doesn't impose it.

### Chivo.Scope.NotChatlas

- Chivo is general-purpose. Built standalone.
- Chatlas is a potential consumer (in-session agents querying chivo) and producer (transcripts as raw material).
- `collections` (named, prompt-curated session sets) — discussed in chatlas context, looks chivo-shaped (prompt + args → membership set as result). Likely a chivo client when both exist.
- Chatlas annotations is independent and ships separately.

### Chivo.Naming

- `chivo` — Cuban slang for cheat sheet (back-of-arm exam crib).
- Captures the function (distilled prior work reused instead of redoing) without overweighting any single dimension (cache, forum, market).
- Rejected: codex, atlas, ledger, cairn, lattice, strata (literature/cartographic — too noun-y, too "place" rather than "active system"), bazaar, exchange, bourse (market angle, strong but generic), thinkhub (corporate SaaS feel), thinkrum (forum metaphor but ambiguous pronunciation, weak on cache/market dimension).
- "Cheat sheet" is honest about reuse being a form of cheating — and that's the point.

## Session.Notes

Open / unresolved:

- **Storage model**: not designed. Where do entries live, what's the on-disk shape, how are they keyed and indexed?
- **Resolved-prompt hashing**: exact-match key derivation needs a normalization spec (whitespace, arg order, etc.)
- **World-state capture**: design for "what world this ran against" metadata is open. Generic schema vs per-workflow custom?
- **Quality gates at publish time**: confidence scores, citations to inputs, agreement-with-other-answers — discussed as needed, not designed.
- **Search-agent implementation**: stacked-agent architecture sketched, no concrete shape yet.
- **Poll schema**: what kinds of polls, who designs them per-workflow, how aggregation works.
- **Implementation home**: no `agentos-chivo-*` package yet. Whether one gets created and when.
- **Relationship to chatlas collections**: may become a chivo client. Decide when collections is concretely designed.
- **Quality dynamics**: SO's quality comes from human reputation incentives that agents don't have. Need explicit publish-time quality gates and ranking signals that work without intrinsic agent motivation.

## Session.Log

- 2026-06-01: session opened. Captured concept-level design from prior chat discussion. No storage/implementation decisions yet. Naming converged on `chivo`. Three open metaphor framings (Nix/Bazel + SO + market) reconciled — chivo carries all three without picking one. Scope confirmed framework-level, not chatlas-specific.
