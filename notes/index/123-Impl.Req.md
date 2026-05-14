# Impl.Req

## Impl.Req

- `Impl.Req` is an implementation-request artifact — a surface for designing and tracking an implementation plan
- can be produced from any context where implementation guidance is needed
- the impl-req author designs the implementation path — sequence, constraints, checkpoints — not just what to build, but how to build it well
- the plan is pre-shaped so the implementer naturally follows good practices: `Vertical.Slice`, `No.Legacy.Allowed`, `Test.At.Boundaries` are built into the plan structure, not listed as recommendations
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
