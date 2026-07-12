# Packages.Master.Agent - Appendix

The caller-facing arguments of the master agent are declared as `Skill.Arg` blocks in the `agentos-master-pkg-agent` skill's `Skill.Arg.Section` (`Skill.Arg::Main.Prompt`, `Skill.Arg::Context`, `Skill.Arg::Scope`, `Skill.Arg::Enrichment.Prompt`). This appendix covers the depth that is not an argument.

****

## Context.Enrichment.Call

- `Context.Enrichment.Call` is a master-agent usage pattern where the caller supplies an enrichment request as `Skill.Arg::Main.Prompt`
- used when enriching a current discussion, subject summary, design, or working context is the primary goal
- the caller may summarize the current subject and ask the master agent to report relevant package-grounded concepts, connections, contradictions, risks, or opportunities
- may optionally include a `Skill.Arg::Enrichment.Prompt` targeting a narrower or secondary enrichment frontier

****

## Master.Agent.Spawn.Preferences

- `Master.Agent.Spawn.Preferences` guides the caller when spawning `Packages.Master.Agent`
- the caller typically owns agent spawning and configures the model, reasoning effort, service tier, tools, timeout, and context passed to the agent
- use a medium-size, context-efficient model because master-agent work is structured package navigation, research, and synthesis
- use Anthropic Haiku or OpenAI `gpt-5.4-mini`; use the closest available equivalent for other providers
- use low or medium reasoning effort
- preserve read-only operation regardless of spawning configuration
- explicit user spawning instructions override these defaults
