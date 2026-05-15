# Impl.Req

## Impl.Req

- `Impl.Req` is an implementation-request artifact — a surface for designing and tracking an implementation plan
- can be produced from any context where implementation guidance is needed
- the impl-req author designs the implementation path — sequence, constraints, checkpoints — not just what to build, but how to build it well
- the plan is pre-shaped so the implementer naturally follows good practices — development principles are built into the plan structure, not listed as recommendations (see `125-Development.Principles.md`)
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
- see `125-Development.Principles.md` for definitions
