> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Alignment.Loop

- `Alignment.Loop` is the general workflow machinery for human-agent convergence
- sequence: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`
- parameterized by phase: `Alignment.Loop:What` (design), `Alignment.Loop:How` (impl design), `Alignment.Loop:Exec` (impl execution, light)

****

## Alignment.User.Turn

- `Alignment.User.Turn` is the turn mode where the user drives and the agent follows
- the agent follows the user's current thread, discusses one topic until convergence, parking, or rejection

****

## Alignment.Maintenance.Turn

- `Alignment.Maintenance.Turn` is the turn mode where the agent drives one session move
- ask next question, consolidate, report status, surface stale state, upgrade, close, split, or hand off
- mode switching is user-gated — the agent may suggest, never silently switch

****

## Alignment.Backend

- `Alignment.Backend` is where session state lives
- `Alignment.Backend:InChat` — state lives in chat, no file overhead
- `Alignment.Backend:Artifact` — state lives in a file-backed artifact, durable and handoff-ready
- parameterized by phase: `Alignment.Backend:InChat:What`, `Alignment.Backend:Artifact:What`, etc.
- `Alignment.Backend:InChat` and `Chat.Surface` are distinct concerns: `Alignment.Backend:InChat` is the active session state — the live chat as it unfolds, "what's in RAM"; `Chat.Surface` is the durable record of past chats — the archived interaction trail

****

## Hard.Evidence

- `Hard.Evidence` is the principle that evidence-based arguments have priority over agent assumptions
- concrete evidence: user instructions, inspected codebase state, active session artifacts, stable project surfaces, `Chat.Surface` content (especially user turns)
- a summary is not `Hard.Evidence` — without a link to the evidence it stands on, it is low-confidence (`We.Distrust.Summaries`)
- when evidence and assumption conflict, evidence wins

****

## We.Distrust.Summaries

- `We.Distrust.Summaries` is the stance that a summary carries low confidence until it links to its source evidence
- a summary is a compressed, derived claim — agent assumption, not `Hard.Evidence`, until grounded
- the link to the source restores confidence — it lets a reader recompute the summary against the evidence
- this is why `Stable.Surface`s prefer pointers and recomputation over cached summaries (`Computed.Status`)

****

## Alignment.Session

- `Alignment.Session` is a shallow container — when these concepts run together in a session, that's an Alignment.Session
- no behavioral protocol of its own — each workflow specialization defines its own `Alignment.Hugentic.Axes` and behavioral detail
- lists and relates the general concepts that compose an alignment session

### concepts

- `Design.Space`, `Alignment.Hugentic.Axis`, `Alignment.Agentic.Axis`, `Alignment.Loop`, `Alignment.User.Turn`, `Alignment.Maintenance.Turn`, `Alignment.Backend`, `Chat.Surface`

### phase semantic roots

- `What.Design` — phase 1, working on the conceptual model
- `How.Design` — phase 2, planning the path
- `Impl.Exec` — phase 3, walking the path

****

## Impl.Req

- `Impl.Req` is an implementation-request artifact — a surface for designing and tracking an implementation plan
- can be produced from any context where implementation guidance is needed
- the impl-req author designs the implementation path — sequence, constraints, checkpoints — not just what to build, but how to build it well
- the plan is pre-shaped so the implementer naturally follows good practices — `Development.Principles` are built into the plan structure, not listed as recommendations
- the goal: if handed to an agent with no other context, the plan itself steers them toward quality work
- self-contained enough for any agent to understand and execute — can link out to other surfaces for extended context
- the fundamentals section is produced through a focused alignment discussion scoped to implementation concerns — same `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation` loop (`Alignment.Loop:How`), but targeting implementation design
- updated by the implementer during execution — serves as a status tracking surface for the implementation
- multiple `Impl.Req` artifacts can spawn from the same design session for different parts of the system

****

## Development.Principles

- `Impl.Req` work spans `How.Design` and `Impl.Exec` — different principles matter at each phase
- `How.Design`: `Deep.Modules`, `Agent.Navigable.Codebase` — shape the implementation design
- `Impl.Exec`: `Vertical.Slice`, `No.Legacy.Allowed`, `No.Regression.Tests.Allowed`, `Test.At.Boundaries`, `RED.GREEN.Test.Suite` — guide execution discipline
- each principle is its own block; the router resolves them

****

## Deep.Modules

- `Deep.Modules` is an architectural principle: small interface, hidden complexity
- a module should do a lot of work behind a simple contract
- the interface is the cost; the functionality behind it is the value

****

## Agent.Navigable.Codebase

- `Agent.Navigable.Codebase` is the structural principle that code should be organized so agents can explore naturally
- clear boundaries, discoverable entry points, self-documenting structure
- agents should be able to orient without reading everything

****

## Vertical.Slice

- `Vertical.Slice` is the preferred shape of implementation work
- a unit of implementation that cuts through the stack as deeply as possible to produce one observable result end-to-end
- the endpoints are chosen by the implementer — a passing test, a CLI command, an artifact output, an API response — but they should be meaningfully far apart in the stack
- the further apart the endpoints, the more real integration is tested — modules exercised as they are actually used, wired together
- design the implementation to reach the first observable endpoint as fast as possible — get to a testable running state first, then expand
- the first slice proves the integration path works; subsequent work extends horizontally: more cases, more features, more edge handling
- each slice should state: what changes, which path through the system it exercises, what observable result should exist, how the result will be checked
- pairs naturally with `Test.At.Boundaries` — test at the outer boundaries of the slice, which are the real system boundaries

****

## No.Legacy.Allowed

- `No.Legacy.Allowed` is an implementation constraint: do not leave stale state behind after implementation
- dead code, outdated artifacts, misleading docs, orphaned config, or superseded surfaces must be cleaned up as part of the implementation
- implementation is not done until the change is clean — no trailing debris
- applies to every `Impl.Req`, not just large refactors
- can only be overridden by an explicit statement — ignoring this is one of the main causes of poor quality implementation results

****

## No.Regression.Tests.Allowed

- `No.Regression.Tests.Allowed` is an implementation constraint: do not add regression tests by default
- a bug fix does not automatically require a new test
- add tests only when the user asks, the `Impl.Req` calls for them, or the behavior is a durable public contract
- when tests are added, follow `Test.At.Boundaries`: test public behavior, not private implementation details
- validation can be a CLI run, manual check, type check, focused command, or existing test suite
- prevents test suites from accumulating one-off bug fossils and private-helper assertions

****

## Test.At.Boundaries

- `Test.At.Boundaries` is the testing guidance for implementation: test through public interfaces, not implementation details
- tests describe observable behavior and survive refactors
- prefer e2e and integration-style tests that exercise the full path of a `Vertical.Slice`
- feedback loops (tests, type checks, manual QA) form the quality ceiling — without them the agent codes blind
- every `Impl.Req` should specify what feedback loops validate the work

****

## Design.Target.Model

- `Design.Target.Model` is the current explicit design model of a system
- not a frozen spec — the current best understanding of the target
- does not live only in the index — the index is a map of the model and holds part of its content
- other surfaces hold design data too: `Index.Appendix`, skills, etc.
- the index is still the entry point for building the design model because it links out to the other surfaces
- `Design.Target.Model` is a distributed model, with the index as the discovery layer

****

## Current.Implementation

- `Current.Implementation` is the current realized state of a system
- may live in code, CLI, skills, data, notes, or any combination depending on the project type

****

## Progress.Gradient

- `Progress.Gradient` is the combined direction of `Forward.Alignment` + `Internal.Alignment` at any point
- the project is never finished — working is moving in the direction of the gradient
- being unfinished is acceptable when a credible gradient exists

****

## Design.Implementation.CoEvolution

- `Design.Implementation.CoEvolution` is the development rhythm of `Forward.Alignment` then `Internal.Alignment`, co-developing design and implementation surfaces
- neither side is frozen — moving forward reveals alignment gaps, aligning surfaces reshapes direction

****

## Kernel.Writing

- `Kernel.Writing` is a portable conceptual writing system for capturing and communicating fundamental signal
- it can be applied retrospectively to an existing corpus or actively during an ongoing conversation
- source material can be chat, argument, codebase, documentation, design artifact, implementation behavior, or observation
- in live use, it helps participants converge by naming topics, separating dimensions, and reducing redundant prose
- in retrospective use, it distills existing material into named conceptual blocks
- its purpose is to turn source material into named conceptual blocks that support future judgment
- each line aims to describe a fundamental dimension of the topic — the view is multi-faceted
- lines aim to be orthogonal — avoid redundancy, prefer independent facts
- language is direct — prefer concise expression, avoid superfluous words
- completeness means covering the fundamental angles of a topic, not explaining every detail
- coverage over compression — losing a fundamental dimension is more costly than an extra line
- space constraints are external — the surface determines the budget, not the philosophy
- the filter: capture material that changes future judgment
- useful material can enter before it has mature structure — capture first, polish later
- `Kernel.Block` is the writing object that embodies `Kernel.Writing`

****

## Kernel.Block

- `Kernel.Block` is the base writing object of `Kernel.Writing`
- its heading is a conceptual commitment — it names what the block is about
- one block is one topic — a single concept, issue, or subject
- it has a defined format of named `Kernel.Block.Section`s: `Kernel.Block.Fundamentals`, `Kernel.Block.Grounding`, `Kernel.Block.Appendix`, `Kernel.Block.Meta`
- only `Kernel.Block.Fundamentals` is required; grounding, appendix, and meta are optional
- its sections separate conceptual content from cited chat evidence and from non-conceptual block data
- it is surface-neutral — the surface it lives on sets what a block may hold and how writing is gated

****

## Kernel.Block.Section

- `Kernel.Block.Section` is a named part of a `Kernel.Block`
- fundamentals are the root `Concept.X` block itself — the block is its fundamentals
- meta is always inblock — non-conceptual data kept with the concept so it loads alongside it
- appendix and grounding are path-children placed outblock by default: `Concept.X/Appendix`, `Concept.X/Grounding`, loaded on demand
- the path is the name; outblock placement (in the appendix) is the default for these depth sections

****

## Kernel.Block.Meta

- `Kernel.Block.Meta` is the meta section of a `Kernel.Block` — non-conceptual data about the block as an object, never its subject
- always inblock — kept with the concept so it loads alongside it (findability)
- the strip-test: remove the line; if the block's conceptual load is unchanged, it belongs in meta
- `alias` is the paradigmatic field: alternate names that widen query hits without changing meaning

****

## Kernel.Block.Fundamentals

- `Kernel.Block.Fundamentals` is the conceptual core of a `Kernel.Block` — the root block, what `Concept.X` is
- it is the only required section; a block is its fundamentals, the rest is optional
- it carries the concept itself: definition, boundaries, judgments, and relations, one dimension per line
- it pays off the heading's conceptual commitment — what the block is about
- it is the compressed prefix of the `Block.Line.Gradient`; extended depth continues in `Concept.X/Appendix`

****

## Kernel.Block.Appendix

- `Kernel.Block.Appendix` is the extended-depth section of a `Kernel.Block`, addressed `Concept.X/Appendix`
- it is `Kernel.Writing` at relaxed constraints: coverage over compression, format-rich allowed
- it holds rationale, edge cases, examples, rejected alternatives — depth past the compressed fundamentals
- it is first-class extended writing, not a hiding place for less-important blocks
- it is the tail of the `Block.Line.Gradient`, loaded on demand (`Appendix.Discovery`)
- distinct from `Appendix.Block`, which is a whole `Kernel.Block` placed in the appendix file
