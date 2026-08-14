# Impl.Req — Appendix

****

## Impl.Req/Artifact.Structure

- `Impl.Abstract` — scope, status, source context — fully agent-maintained, the agent must evaluate changes to it on each design change
- `Impl.Index` — implementation design alignment as `Design.Index.Blocks` — same block format, same evidence tracking, same alignment semantics
- `Execution.Plan` — ordered vertical slices, validation per slice, risks, deviation triggers, acceptance signals, status per slice (updated by implementer)
- `Impl.Log` — progress tracking: deviations, blockers, decisions made in open space (updated by implementer)

****

## Impl.Req/Agent.Chain

- `conceptual.designer.agent` → `impl.designer.agent` → `impl.executer.agent`
- each can be one or several agents
- `conceptual.designer.agent` — produces fundamentals alignment (`What.Design.Session`)
- `impl.designer.agent` — forks toward implementation, writes the `Impl.Req` (`Impl.Index` + `Execution.Plan`), links relevant sources, bakes in principles
- `impl.executer.agent` — loads the `Impl.Req`, runs a minimal re-alignment discussion to recover/double-check alignment, then implements, updating `Impl.Log` as it goes
- all agents in the chain should have `Development.Principles` loaded
