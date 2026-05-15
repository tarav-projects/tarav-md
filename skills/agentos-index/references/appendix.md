# Appendix

## Index.Appendix

- `Index.Appendix` is the stable opt-in depth surface for the Agentos Index — the `Extended.Index.Scope`
- it lives at `notes/appendix/`
- it carries durable conceptual material that is too large or explanatory for default `Kernel.Block:Index` grounding
- it is part of the index system, but not part of `Context.Minimal.Surface`
- agents load appendix material only when the task needs extended reasoning, examples, tradeoffs, or provenance

The appendix exists to keep index blocks small and executable without discarding valuable design depth.

****

## Kernel.Block:Appendix

- `Kernel.Block:Appendix` is `Kernel.Block` placed in `notes/appendix/` — extended material for a concept
- `Kernel.Writing` at relaxed space constraints — depth over compression
- it carries extended material: examples, use cases, rationale, pressure tests, pros/cons, rejected alternatives, and design depth
- it has no line-count ceiling, but line-length discipline still applies
- it is stable design truth, not a scratch note, transcript, task list, or changelog
- aliases: `Appendix.Block`

Discovery is implicit — agents check if `notes/appendix/Concept.Name-appendix.md` exists by convention.

****

## Appendix.Placement

- use `Kernel.Block:Index` for compact grounding that agents should load by default
- use `Kernel.Block:Appendix` for durable depth that would make the default block too large
- use skills for operational workflow instructions
- use code and CLI help for exact mechanical behavior
- use live notes for temporary session state and working material

Appendix material belongs in `notes/appendix/` when it is stable enough to preserve but too detailed for the minimal index surface.

****

## Appendix.Promotion

- appendix material commonly starts in chat, live notes, design-session artifacts, skills, or code review discussion
- when promoted from `Kernel.Block:Design.Session`, fundamentals compress into the `Kernel.Block:Index`
- the `### appendix` section promotes to a `Kernel.Block:Appendix`
- the `### meta` section does not promote as design truth unless it contains a separate durable concept or workflow note
- promotion is a maintenance activity and remains subject to index write gates

Promotion should preserve the user's wording when the wording carries design judgment.

****

## Appendix.File.Convention

- appendix files are named by concept: `Concept.Name-appendix.md`
- no numeric prefix — the `Dotted.Name` is the stable handle
- discovery is implicit — agents check if the file exists by convention, no outlink required
- each appendix file corresponds to an owning concept or tight concept cluster
- related appendix blocks should cluster under the same file when they extend related concepts
- created on demand — no empty files, no pre-planning

The routing goal is discoverability on demand: an agent grounded in fundamentals can find the deeper material without carrying it in every context.
