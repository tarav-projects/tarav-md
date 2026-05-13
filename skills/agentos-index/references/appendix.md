# Appendix

## Index.Appendix

- `Index.Appendix` is the stable opt-in depth surface for the Agentos Index
- it lives at `notes/appendix/`
- it carries durable conceptual material that is too large or explanatory for default `Index.Block` grounding
- it is part of the index system, but not part of `Context.Minimal.Surface`
- agents load appendix material only when the task needs extended reasoning, examples, tradeoffs, or provenance

The appendix exists to keep `Index.Blocks` small and executable without discarding valuable design depth.

****

## Index.Appendix.Block

- `Index.Appendix.Block` is an appendix-only block hosted in `notes/appendix/`
- it has no fundamentals section because fundamentals live in the paired `Index.Block`
- it carries extended material: examples, use cases, rationale, pressure tests, pros/cons, rejected alternatives, and design depth
- it has no line-count ceiling, but line-length discipline still applies
- it is stable design truth, not a scratch note, transcript, task list, or changelog

An appendix block should be reachable from its concept's index block or note so agents can discover depth without loading it by default.

****

## Appendix.Placement

- use `Index.Block` for compact grounding that agents should load by default
- use `Index.Appendix.Block` for durable depth that would make the default block too large
- use skills for operational workflow instructions
- use code and CLI help for exact mechanical behavior
- use live notes for temporary session state and working material

Appendix material belongs in `notes/appendix/` when it is stable enough to preserve but too detailed for the minimal index surface.

****

## Appendix.Promotion

- appendix material commonly starts in chat, live notes, design-session artifacts, skills, or code review discussion
- when promoted from `Design.Index.Block`, fundamentals compress into the `Index.Block`
- the `#### appendix` section promotes to an `Index.Appendix.Block`
- the `#### meta` section does not promote as design truth unless it contains a separate durable concept or workflow note
- promotion is a maintenance activity and remains subject to index write gates

Promotion should preserve the user's wording when the wording carries design judgment.

****

## Appendix.Routing

- each appendix file should correspond to the owning index note when possible
- appendix notes receive their own stable numeric prefix like any other note
- appendix note prefixes use the same rolling `100-499` range as index notes
- do not duplicate the paired index note's number unless allocation naturally returns that number
- the filename slug may mirror the paired index note: `NNN-Concept.Name.md`
- related appendix blocks should cluster under the same appendix file when they extend the same index note
- the paired `Index.Block` or note should link to appendix material through outlinks or an equivalent explicit pointer
- `000-index.md` should remain a minimal router and should not list every appendix block by default

The routing goal is discoverability on demand: an agent grounded in fundamentals can find the deeper material without carrying it in every context.
