# Master Agent Prompting - design-session

## Session.Abstract

- Goal: design `agentos-master-pkg-agent`, the caller skill that teaches an agent how to prompt and invoke `Packages.Master.Agent`
- Public framing: ask a separate read-only agent almost anything while keeping research out of the caller's context
- Actual grounding contract: answers come from accessible `Package.Skill` surfaces, including the general capabilities routed through `agentos-pkg`
- Current focus: design the arguments and prompt structure supplied by the caller
- Implementation is intentionally incremental; only the skill description has been written

## Design.Index

****

## Agentos.Master.Package.Agent.Skill

- `agentos-master-pkg-agent` is an operational `Package.Aux.Skill` that teaches callers how to invoke `Packages.Master.Agent`
- its public discovery language may oversell the agent as an ask-anything agent so callers can enter the Agentos framework before knowing which package or subsystem they need
- explicit user triggers include `master-agent` and `agentos-agent`
- the delegated agent remains read-only and package-grounded
- the skill primarily teaches the caller how to construct strong `Master.Agent.Arguments`
- detailed master-agent mechanics should live in `agentos-pkg/references/master-agent.md`

### meta

- status: partially converged
- implementation surface: `skills/agentos-master-pkg-agent/SKILL.md`

****

## Master.Agent.Arguments

- `Master.Agent.Arguments` is the complete caller-authored input supplied to `Packages.Master.Agent`
- contains an optional `Master.Agent.Scope` and an ordered `Prompt.Bundle`
- may include call-wide context, constraints, or supporting material
- should provide enough adjacent conversational context for the master agent to understand the prompts without having access to the caller's conversation
- the caller may use substantial context when that improves answer quality

### meta

- status: partially converged

****

## Master.Agent.Scope

- `Master.Agent.Scope` is an optional argument that focuses the master agent's research
- may identify particular packages, subsystems, surfaces, concepts, time ranges, or investigation boundaries
- when omitted, the master agent discovers relevant packages and surfaces from the request and adjacent context
- scope guides research without becoming a strict exclusion unless the caller explicitly marks it strict
- the master agent may report materially relevant findings just outside a non-strict scope

### meta

- status: partially converged

****

## Prompt.Bundle

- `Prompt.Bundle` is an ordered collection of related prompts answered during one master-agent call
- prompts in the bundle benefit from the same caller context and loaded package context
- prompts are answered in order
- each prompt receives a separate answer section
- the main prompt has the highest priority
- the initial standard bundle contains `Main.Request.Prompt` followed by an optional `Enrichment.Request.Prompt`

### meta

- status: partially converged

****

## Main.Request.Prompt

- `Main.Request.Prompt` is the primary caller-specific question or requested result
- answered first and with the highest priority
- may request research, comparison, explanation, critique, enrichment, or another read-only result
- should include the context adjacent to the request when that context materially affects interpretation or answer quality

### meta

- status: partially converged

****

## Enrichment.Request.Prompt

- `Enrichment.Request.Prompt` is a recommended but optional caller-authored secondary prompt in a master-agent `Prompt.Bundle`
- asks the master agent to enrich selected parts of the current subject using package-grounded knowledge
- the caller identifies new concepts, major themes, uncertainty, assumptions, or connections that could profit from enrichment
- should account for previous master-agent calls so already-enriched subjects are not repeated unnecessarily
- answered after `Main.Request.Prompt`
- may return that no material enrichment was found

### meta

- status: partially converged

****

## Context.Enrichment.Call

- `Context.Enrichment.Call` is a master-agent usage pattern where the caller makes an `Enrichment.Request.Prompt` the `Main.Request.Prompt`
- used when enriching a current discussion, subject summary, design, or working context is the primary goal
- the caller may summarize the current subject and ask the master agent to report relevant package-grounded concepts, connections, contradictions, risks, or opportunities
- may optionally include another `Enrichment.Request.Prompt` targeting a narrower or secondary enrichment frontier

### meta

- status: partially converged

****

## Master.Agent.Spawn.Preferences

- `Master.Agent.Spawn.Preferences` guides the caller when spawning `Packages.Master.Agent`
- the caller typically owns agent spawning and configures the model, reasoning effort, service tier, tools, timeout, and context passed to the agent
- use a medium-size, context-efficient model because master-agent work is structured package navigation, research, and synthesis
- use Anthropic Haiku or OpenAI `gpt-5.4-mini`; use the closest available equivalent for other providers
- use low or medium reasoning effort
- preserve read-only operation regardless of spawning configuration
- explicit user spawning instructions override these defaults

### meta

- status: converged

## Session.Notes

### Settled Principles

- The caller should provide context adjacent to the prompt without summarizing the entire session by default.
- A broad session-subject summary is valid when used intentionally for `Context.Enrichment.Call`.
- The caller can be extensive because the delegated agent receives a separate context window.
- Context should be relevant and structured rather than an unfiltered transcript.
- The master agent answers from accessible package surfaces and may return `not found`, though this should be rare across the Agentos package ecosystem.
- The caller may optionally focus the master agent through `Master.Agent.Scope`.
- An `Enrichment.Request.Prompt` is recommended but optional.
- The caller typically spawns the master agent using a medium-size, context-efficient model with low or medium reasoning effort.

### Open Questions

- What call-wide fields exist outside `Master.Agent.Scope` and `Prompt.Bundle`?
- Does each prompt support prompt-local adjacent context and extras?
- What exact answer structure corresponds to an ordered `Prompt.Bundle`?
- What mechanics belong in `SKILL.md` versus `references/master-agent.md`?
- How should the caller resolve packages before invoking the master agent?
- Should `Prompt.Bundle` and related concepts eventually become Agentos index blocks?

## Session.Log

- Started from the design and index writing of `Packages.Master.Agent`, `Multi.Package.Operation`, and the revised `Package.Agent`.
- Created `skills/agentos-master-pkg-agent/SKILL.md` with the approved discovery description.
- Upgraded the ongoing design discussion to an artifact-backed `What.Design.Session`.
- Added `Master.Agent.Scope` as an optional argument and converged the initial prompt bundle vocabulary around `Main.Request.Prompt` and `Enrichment.Request.Prompt`.
- Converged `Master.Agent.Spawn.Preferences` around direct, efficient defaults: Anthropic Haiku or OpenAI `gpt-5.4-mini`, with low or medium reasoning effort.
