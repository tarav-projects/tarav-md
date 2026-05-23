****

## Flat.File.Design

- semantic file names create placement friction — every new concept requires deciding which file it belongs to
- placement friction slows writing and creates false groupings that age poorly
- flat anonymous files eliminate the decision: append to the last file, done
- the routing table (`000-index.md`) absorbs the cost — one place to update, always loaded
- organizing is a separate concern handled by `Concept.Scoping` — a concept can belong to multiple namespaces without moving between files
- splitting an overfull file is deferred to maintenance — not a writing concern

****

## Universal.Block.Structure

- `Kernel.Block` is the single block structure: fundamentals + `### appendix` + `### meta`
- parameterized by surface using `Dotted.Parameterized.Notation` — e.g. `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design`
- each parameterization inherits the full structure — what varies is the surface context and its constraints
- `Kernel.Writing` applies uniformly — the philosophy is the same, the surface sets the budget

****

## Meta.Unification

- `### meta` is the single non-conceptual section of a `Kernel.Block` — aliases, findability, outlinks, status, open questions
- the dividing rule: fundamentals and appendix are about the concept; meta is about the block itself
- fewer sections means less structural overhead per block

****

## Implicit.Appendix.Discovery

- appendix files live at `appendix/` (public: `skills/agentos-pkg/appendix/`, local: `notes/appendix/`)
- files are concept-named: `Concept.Name-appendix.md`
- discovery is implicit — an agent checks if the file exists by convention, no outlink maintenance needed
- the naming convention is the routing mechanism
- created on demand: if a concept needs depth, the file appears; no pre-planning, no empty shells

****

## Writing.Organizing.Decoupling

- `Kernel.Writing` defines how to capture a concept — the philosophy is surface-independent
- space constraints are external — the surface determines the budget, not the philosophy
- the same writing discipline applies everywhere: index, appendix, session artifacts, etc.
- organizing happens through `Concept.Scoping`, not through file structure or writing decisions
