# Design.Index

`Design.Index` is the conceptual background of the current `Design.Session`.

It captures the relevant conceptual value produced by the session so the agent and user can keep the design grounded while the discussion continues.

## Shape

Use H3 concept blocks under the H2 section:

```md
## Design.Index

### Concept.Name

- fundamentals with the same semantic role as `Index.Block` fundamentals

#### appendix

- rationale, examples, pressure tests, tradeoffs, rejected alternatives, design depth

#### meta

- status, sources, open questions, promotion notes, stale or misaligned markers
```

## Design.Index.Block

Each H3 concept block is a `Design.Index.Block`.

The fundamentals have the same semantic role as `Index.Block` fundamentals: compact meaning, boundaries, relations, judgments, and unresolved conceptual pressure. Draft quality may vary during a session, but the meaning target is the same.

Use `appendix` for extended conceptual material that keeps fundamentals concise without losing valuable discussion signal.

Use `meta` for session mechanics about the concept, such as state, sources, open questions, stale markers, or alignment issues.

## Writing Guidance

- Prefer one block per subject concept.
- Keep fundamentals compact and concept-shaped.
- Move rationale, examples, pressure tests, tradeoffs, rejected alternatives, and design depth into `appendix`.
- Put session mechanics in `meta`, not in fundamentals.
- Preserve user language when wording is part of the design judgment.
- Mark unsettled material explicitly instead of presenting it as settled.
- Do not turn `Design.Index` into a transcript.

## User Gate

`Design.Index` is session state.

In `InChat.Session`, the agent may print refreshed `Design.Index` blocks and let the user correct, accept, or park them.

In `Artifact.Session`, updates are artifact writes and require the artifact user gate.

Actual Agentos Index writes remain governed by the Agentos Index write workflow.
