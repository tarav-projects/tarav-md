# Design.Index

This detailed product-design module is owned by `agentos-hugentics --design`.

> $kw: --dev-from references/index-context-assembly.skw.md

`Design.Index` is the conceptual background of the current `What.Design.Session`. Each block is a `Design.Block` and applies `Kernel.Writing` discipline — see `writing-craft.md` for the full craft surface.

It captures the relevant conceptual value produced by the session so the agent and user can keep the design grounded while the discussion continues.

## Shape

Use H3 concept blocks under the H2 section:

```md
## Design.Index

### Concept.Name

- fundamentals with the same semantic role as `Index.Block` fundamentals

#### grounding

- optional chat evidence for grounded session-local claims

#### appendix

- rationale, examples, pressure tests, tradeoffs, rejected alternatives, design depth

#### meta

- status, sources, open questions, promotion notes, stale or misaligned markers
```

## Design.Index.Block

Each H3 concept block is a `Design.Index.Block` — a `Design.Block` placed in this section.

The fundamentals carry the same semantic role as `Index.Block` fundamentals: compact meaning, **boundaries** (what the concept is NOT), **relations** to other concepts (use `Inline.Relatedness`), **judgments** made explicit, and **unresolved conceptual pressure** marked as open. Draft quality may vary during a session, but the meaning target is the same.

Use `appendix` for extended conceptual material — rationale, pressure tests, rejected alternatives — that keeps fundamentals concise without losing valuable discussion signal.

Use `grounding` for chat evidence that grounds the block while the session is active or prepares it for index promotion.

Use `meta` for session mechanics about the concept: aliases, status, sources, open questions, stale markers, alignment issues.

## Writing Guidance

- Prefer one block per subject concept.
- Each fundamental line should target a distinct facet — definition, boundary, judgment, relation, or open pressure. Orthogonal lines, no redundancy, one dimension per line — never weld several facets into one bullet. See `Kernel.Writing` in `writing-craft.md`, the welded-vs-atomic contrast there, and the exemplar blocks in `index-view.md` for the granularity bar.
- Move rationale, examples, pressure tests, tradeoffs, rejected alternatives, and design depth into `appendix`.
- Put session mechanics in `meta`, not in fundamentals.
- Preserve user language when wording is part of the design judgment — paraphrasing user-tone into agent-tone erases authority (see `design-anti-patterns.md` / paraphrased user judgment).
- Mark unsettled material explicitly under `meta` `open:` instead of presenting it as settled.
- Mark assumption-based lines as such; promote to evidence-backed when the user confirms or evidence lands (`Hard.Evidence`).
- Do not turn `Design.Index` into a transcript.

## User Gate

`Design.Index` is session state.

In `Alignment.Backend::InChat::What`, the agent may print refreshed `Design.Index` blocks and let the user correct, accept, or park them.

In `Alignment.Backend::Artifact::What`, updates are artifact writes and require the artifact user gate.

Actual Agentos Index writes remain governed by the Agentos Index write workflow.

> $kw: --from Design.Block
> $kw: --from Design.Index.Block
> $kw: --from Hard.Evidence
> $kw: --from Index.Block
> $kw: --from Inline.Relatedness
> $kw: --from Kernel.Writing
> $kw: --from What.Design.Session
