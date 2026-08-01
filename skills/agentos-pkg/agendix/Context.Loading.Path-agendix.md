****

## Context.Loading.Path/Agendix/Context.Loading.Model

- [DF] `Context.Loading.Model` is the candidate central model for expressing, projecting, and checking how context accumulates while an agent enters and runs a skill ^c20260801-5u
- [DF] `Context.Loading.Path` is a language for expressing ordered context accumulation, not only the resulting chain of loaded files ^c20260801-4u
- [DC] the path language has a harness-provided anatomy containing `AGENTS.md`, `SKILL.Description`, `User.Turn`, and `SKILL.md` ^c20260801-4u
- [CT] skills extend the dynamic portion of the path with whole-file loading steps selected or prompted during the run ^c20260801-4u
- [CT] a path expression treats appearance order as modeled loading order; this is a useful approximation rather than a runtime guarantee ^c20260801-4u
- [DF] `Projected.Context` is the accumulated context that `Context.Loading.Model` computes for one target file on one loading path ^c20260801-5u
- [DC] a Skillware context command should resolve every complete path to a target, verify its routing and prompted-loading links, assemble each path projection in order, evaluate dependencies, and present the result with step provenance ^c20260801-5u
- [CT] a file may be reachable through multiple loading paths; its projections remain path-specific and must not be silently unioned into unsupported assumptions ^c20260801-5u
- [PR] a complete path composes `Workspace.Context.Path` with `Skill.Local.Context.Path` at the transition into `SKILL.md` ^c20260801-6u
- [CT] external `AGENTS.md` parents cannot be inferred portably from a skill file and therefore require explicit workspace or agent-root declarations ^c20260801-6u
- [CT] a skill may declare what its `Workspace.Context.Path` must provide before the skill-local path begins; externally bound `Skill.Arg` values are one such contribution ^c20260801-6u
- [CT] context dependencies distinguish content available on an earlier path step from content required in the skill-local path or inlined in the consuming file ^c20260801-7u
- [CT] an inline requirement is not satisfied only because an earlier prompt asked the agent to load the required content ^c20260801-7u
- [FR] `Workspace.Context.Path`, `Skill.Local.Context.Path`, and their exact boundary names remain provisional while the model is exercised against real skill paths ^c20260801-6u
