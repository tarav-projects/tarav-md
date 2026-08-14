# Index.Block — Catalog

Worked examples for writing `Index.Block`s: well-formed blocks to imitate, and malformed ones to avoid.

The bar is **line granularity** — each line one fact, one dimension, reorderable, surviving on its own. The rules live in `Index.Block` and `Kernel.Writing`; this file is the concrete form. Read the positives for the shape, the negatives for the failure modes the rules don't catch on their own.

---

## Positive

### Definition-first, atomic lines

```md
## Hard.Evidence

- `Hard.Evidence` is the principle that evidence-based arguments have priority over agent assumptions
- concrete evidence: user instructions, inspected codebase state, active session artifacts, stable project surfaces, `Chat.Surface` content (especially user turns)
- a summary is not `Hard.Evidence` — without a link to the evidence it stands on, it is low-confidence (`We.Distrust.Summaries`)
- when evidence and assumption conflict, evidence wins
```

Why it works:
- line 1 is the `Concept is a …` definition — the heading's conceptual commitment, paid off.
- each line is one dimension; reorder lines 2–4 and nothing breaks.
- the related concept (`Chat.Surface`) is woven inline (`Inline.Relatedness`), not listed as edge metadata.

### Definition + boundary + surface-neutrality

```md
## Kernel.Block

- `Kernel.Block` is the base writing object of `Kernel.Writing`
- its heading is a conceptual commitment — it names what the block is about
- one block is one topic — a single concept, issue, or subject
- it has a defined format of named sections: `Kernel.Block.Fundamentals`, `Kernel.Block.Appendix`, `Kernel.Block.Meta`
- only `Kernel.Block.Fundamentals` is required; grounding, appendix, and meta are optional
- its sections separate conceptual content from cited chat evidence and from non-conceptual block data
- it is surface-neutral — the surface it lives on sets what a block may hold and how writing is gated
```

Why it works:
- abstract conceptual identity, no implementation dump, no count-leading ("four sections").
- carries a boundary line (`surface-neutral` — what the block does *not* decide).
- composition is named via inlined section concepts, not described in long form.

---

## Negative

### Welded line

The most common failure: prose chopped into a bullet, several dimensions joined by em-dashes and "which lets / and demotes" clauses.

```md
- its only mandatory dependency is the `iterante` runtime, which is what lets `mission.py`
  import freely and demotes `iterante` tooling to opt-in (`Iterante.Ctx`)
```

One bullet, three dimensions welded: the mandatory dep, free imports, tooling demotion. Drop a clause and the sentence collapses — it is not reorderable.

**Fixed** — split until each line is one dimension:

```md
- `iterante` is the only mandatory dependency; all others are the author's choice
- `mission.py` may import freely
- `iterante` tooling is opt-in, not the sole channel (`Iterante.Ctx`)
```

### Heading restated as the first bullet

```md
## Account.Identity

- this block is about account identity
- `Account.Identity` is the provider-specific data that binds a captured credential to the right account
```

Line 1 carries no signal — it restates the heading. Drop it; lead with the definition.

### Status / implementation dumped into the block

```md
## Agentos.Agent.Adapter

- `Agentos.Agent.Adapter` exposes slices of a provider instance on a common surface
- status: current — implemented in `agentos-py`, redesign in progress (2026-06)
- resolved: `AgentAdapter` base + `RunCapable`/`AccountStatusCapable`; run behavior is `RunnableMixin`
- pending merge: `Account.Registry` rework for the config/state split
```

Three failures at once:
- `status:` / `pending merge:` are **recomputable state** — on a `Stable.Surface` you inspect to find current state, you don't cache a verdict that decays.
- the `resolved:` line pins the concept to concrete class names — that's `Reference.Implementation` material, it belongs in code, not the index.
- the block became a progress dashboard, which an `Index.Block` must never be.

**Fixed** — keep the concept, drop the cached state and the class wiring:

```md
## Agentos.Agent.Adapter

- `Agentos.Agent.Adapter` exposes slices of a `Provider.Instance`'s capabilities on a common surface
- concrete adapters are named `<Something>.Agent` — the capability surface served, not the full instance
- provider differences are absorbed below the `.Agent` boundary; Agentos sees a uniform interface above it
- one `Provider.Instance` may carry multiple adapters covering different capability slices
```
