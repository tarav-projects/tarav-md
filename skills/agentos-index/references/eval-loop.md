# Eval Loop

## Index.Runtime.Semantics

- the index has execution behavior, not just storage behavior
- when an index is active, it is executed in real time — concepts are loaded, resolved, grounded, and gaps are detected
- the runtime is lazy: concepts are loaded on demand, not preloaded
- the agent judges context to decide what needs full loading vs. acknowledgment vs. parking

****

## Index.Call

- `Index.Call` is the execution primitive of the index
- initiated by a trigger, then processed through the `Index.Eval.Loop`

The agent evaluates context to decide dispatch intensity:

- concept is central to current discussion → full eval (load blocks, ground)
- referenced in passing → lightweight check (confirm existence)
- unknown but peripheral → park as `Unresolved.Index.Name`
- unknown and central → flag, suggest capture

****

## Index.Call.Trigger

- `Index.Call.Trigger` is the mechanism that initiates an `Index.Call`
- multiple trigger types feed into the same `Index.Eval.Loop`

### Dotted.Name.Trigger

- the primary, natural trigger
- when a human uses `Dotted.Notation` in conversation, it is a signal — not decoration
- it means: "I am referring to a concept that should be grounded"
- `Dotted.Notation` is the main API of the index

### Agent.Reasoning.Trigger

- the agent proactively fires `Index.Calls` during its own reasoning
- the agent is a first-class caller of the index, not just a reactive processor
- examples: checking design constraints, encountering unfamiliar names in files, verifying understanding

### Explicit.Query.Trigger

- direct invocation via skill or CLI
- `agentos index find --query "..."` — deterministic lookup
- a skill explicitly loads index blocks as part of its workflow
- user asks the agent to "check the index for X"

****

## Index.Eval.Loop

- `Index.Eval.Loop` is the sequential evaluation pipeline that processes an `Index.Call`
- every trigger follows the same pipeline

```
Trigger → Index.Call → Index.Eval.Loop:

1. Index.Name.Resolution
   - try to match the name against the ontology registry
   - exact match → proceed to step 2
   - approximate match → confirm with human, then proceed
   - no match → proceed to step 3

2. Retrieval + Grounding (resolved path)
   - load relevant Index.Blocks into agent context
   - inject the concept definition so both parties reason from the same base
   - conversation is now grounded on this concept

3. Gap.Detection (unresolved path)
   - is this clearly a new concept? → Emergence.Signal
   - is it approximate to an existing concept? → re-attempt resolution
   - is it peripheral to current discussion? → park as Unresolved.Index.Name

4. Suggestion (when Emergence.Signal)
   - agent holds the concept in working memory
   - may propose capture to user (respecting User.Gated.Index)
   - if user confirms → enters Ontology.Workflows (Registration or Promotion)

5. Parking (when peripheral/unresolved)
   - store as Unresolved.Index.Name in session working list
   - available for later resolution if more context emerges
   - may surface if it keeps recurring
```

### Loading behavior

- **default**: load block fundamentals only (~600 chars) — minimal context cost, enough for grounding
- **agent escalates by judgment**: may load full block, related blocks, or full note if concept is central
- **related concepts**: don't auto-load the whole graph — follow links only when judgment says it's needed
- consistent with lazy evaluation: load on demand, escalate on judgment

### Grounding manifestation

- grounding is reported as a lightweight footer at the end of the agent's response
- format: `> Index: loaded `Concept.A`, `Concept.B` | unresolved: `Unknown.Name``
- the agent responds naturally first, then reports index operations at the end
- gives transparency without interrupting conversation flow

### Gap detection aggressiveness (MVP)

- passive by default: unresolved names are parked and shown in the footer
- agent only suggests registration when:
    - the same unresolved name appears 3+ times in the session
    - or the user explicitly asks about it
- avoids interrupting flow with premature registration prompts

****

## Index.Activation

- `Index.Activation` is the mechanism that turns on `Index.Runtime.Semantics` for a session
- the index runtime is opt-in — it does not magically activate in every conversation
- activation is handled by `agentos-index-activate` — a dedicated bootstrap skill

### Activation chain

```
AGENTS.md: "Load the agentos-index-activate skill at the start of a session."
    → agentos-index-activate loads
    → bootstrap: reads 000-index.md routing table (minimal context)
    → activates Index.Eval.Loop behavior for the session
    → loads agentos-index-trigger for ongoing detection
```

### Activation paths

- **automatic**: AGENTS.md prompts skill load → agent activates on session start
- **manual**: user explicitly invokes `agentos-index-activate` at any point
- **recovery**: if auto-activation fails, the user can trigger it manually

### Manual fallback principle

- all index skills must be user-callable as a fallback
- agent fails to detect a Dotted.Name → user invokes `agentos-index-resolution`
- agent doesn't suggest registration → user invokes `agentos-index-writer`
- agent didn't bootstrap → user invokes `agentos-index-activate`
- the agent automation is the happy path; manual invocation is the safety net
