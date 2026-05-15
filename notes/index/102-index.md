## Alignment.Loop

- `Alignment.Loop` is the general workflow machinery for human-agent convergence
- sequence: `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation`
- parameterized by phase: `Alignment.Loop:What` (design), `Alignment.Loop:How` (impl design), `Alignment.Loop:Exec` (impl execution, light)
- see `101-index.md` for `What.Design` specialization
- see `102-index.md` for `How.Design` specialization

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

****

## Hard.Evidence

- `Hard.Evidence` is the principle that evidence-based arguments have priority over agent assumptions during alignment work
- concrete evidence: user instructions, inspected codebase state, active session artifacts, stable project surfaces
- alignment sessions aim to be `Hard.Evidence`-based — more is welcome, but the core alignment axes are the priority

****

## Alignment.Session

- `Alignment.Session` is a shallow container — when these concepts run together in a session, that's an Alignment.Session
- no behavioral protocol of its own — each workflow specialization defines its own `Alignment.Hugentic.Axes` and behavioral detail
- lists and relates the general concepts that compose an alignment session

### concepts

- `Conceptual.Space`, `Alignment.Hugentic.Axis`, `Alignment.Agentic.Axis`, `Alignment.Loop`, `Alignment.User.Turn`, `Alignment.Maintenance.Turn`, `Alignment.Backend`

### phase semantic roots

- `What.Design` — phase 1, working on the conceptual model
- `How.Design` — phase 2, planning the path
- `Impl.Exec` — phase 3, walking the path

****

## Impl.Req

- `Impl.Req` is an implementation-request artifact — a surface for designing and tracking an implementation plan
- can be produced from any context where implementation guidance is needed
- the impl-req author designs the implementation path — sequence, constraints, checkpoints — not just what to build, but how to build it well
- the plan is pre-shaped so the implementer naturally follows good practices — development principles are built into the plan structure, not listed as recommendations (see `102-index.md`)
- the goal: if handed to an agent with no other context, the plan itself steers them toward quality work
- self-contained enough for any agent to understand and execute — can link out to other surfaces for extended context
- the fundamentals section is produced through a focused alignment discussion scoped to implementation concerns — same `Alignment.Question` → `Alignment.Discussion` → `Alignment.Consolidation` loop (`Alignment.Loop:How`), but targeting implementation design
- updated by the implementer during execution — serves as a status tracking surface for the implementation
- multiple `Impl.Req` artifacts can spawn from the same design session for different parts of the system

### artifact structure

- `Impl.Abstract` — scope, status, source context — fully agent-maintained, the agent must evaluate changes to it on each design change
- `Impl.Index` — implementation design alignment as `Design.Index.Blocks` — same block format, same evidence tracking, same alignment semantics
- `Execution.Plan` — ordered vertical slices, validation per slice, risks, deviation triggers, acceptance signals, status per slice (updated by implementer)
- `Impl.Log` — progress tracking: deviations, blockers, decisions made in open space (updated by implementer)

### agent chain

- `conceptual.designer.agent` → `impl.designer.agent` → `impl.executer.agent`
- each can be one or several agents
- `conceptual.designer.agent` — produces fundamentals alignment (`What.Design.Session`)
- `impl.designer.agent` — forks toward implementation, writes the `Impl.Req` (`Impl.Index` + `Execution.Plan`), links relevant sources, bakes in principles
- `impl.executer.agent` — loads the `Impl.Req`, runs a minimal re-alignment discussion to recover/double-check alignment, then implements, updating `Impl.Log` as it goes
- all agents in the chain should have `Development.Principles` loaded

****

## Development.Principles

- `Impl.Req` work spans `How.Design` and `Impl.Exec` — different principles matter at each phase
- `How.Design`: `Deep.Modules`, `Agent.Navigable.Codebase` — shape the implementation design
- `Impl.Exec`: `Vertical.Slice`, `No.Legacy.Allowed`, `Test.At.Boundaries` — guide execution discipline
- see `102-index.md` for definitions

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

## Chatlas.Query.Surface

- `Chatlas.Query.Surface` is the Chatlas session discovery interface family.
- `agentos chatlas index query` is the base query surface over Chatlas session index rows.
- `agentos chatlas query` is the higher-level session query surface.
- `agentos chatlas query` extends index selection with later query layers such as raw-artifact filtering, standard-model filtering, and row projection.
- The two commands may return different row shapes, but they should expose a consistent top-level query envelope.

****

## Chatlas.Query.Envelope

- `Chatlas.Query.Envelope` is the normalized top-level JSON response shape shared by Chatlas query surfaces.
- The envelope should keep query accounting separate from row projection.
- Shared count fields should use explicit phase names:
  - `index_matched_row_count`
  - `candidate_row_count`
  - `query_matched_row_count`
  - `returned_row_count`
- For `agentos chatlas index query`, the phases collapse because the only query layer is index selection.
- For `agentos chatlas query`, the phases remain layered:
  - index filters select index matches
  - scan limits choose candidates for expensive filters
  - raw and standard-model filters decide final query matches
  - final limit determines returned rows
- Row projection is intentionally independent from the envelope:
  - `agentos chatlas index query` returns full index rows
  - `agentos chatlas query` returns normalized session rows by default
