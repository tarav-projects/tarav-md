# Packages.Master.Agent - Appendix

****

## Master.Agent.Arguments

- `Master.Agent.Arguments` is the complete caller-authored input supplied to `Packages.Master.Agent`
- contains an optional `Master.Agent.Scope` and an ordered `Prompt.Bundle`
- may include call-wide context, constraints, or supporting material
- should provide enough adjacent conversational context for the master agent to understand the prompts without having access to the caller's conversation
- the caller may use substantial context when that improves answer quality

****

## Master.Agent.Scope

- `Master.Agent.Scope` is an optional argument that focuses the master agent's research
- may identify particular packages, subsystems, surfaces, concepts, time ranges, or investigation boundaries
- when omitted, the master agent discovers relevant packages and surfaces from the request and adjacent context
- scope guides research without becoming a strict exclusion unless the caller explicitly marks it strict
- the master agent may report materially relevant findings just outside a non-strict scope

****

## Prompt.Bundle

- `Prompt.Bundle` is an ordered collection of related prompts answered during one master-agent call
- prompts in the bundle benefit from the same caller context and loaded package context
- prompts are answered in order
- each prompt receives a separate answer section
- the main prompt has the highest priority
- the initial standard bundle contains `Main.Request.Prompt` followed by an optional `Enrichment.Request.Prompt`

****

## Main.Request.Prompt

- `Main.Request.Prompt` is the primary caller-specific question or requested result
- answered first and with the highest priority
- may request research, comparison, explanation, critique, enrichment, or another read-only result
- should include the context adjacent to the request when that context materially affects interpretation or answer quality

****

## Enrichment.Request.Prompt

- `Enrichment.Request.Prompt` is a recommended but optional caller-authored secondary prompt in a master-agent `Prompt.Bundle`
- asks the master agent to enrich selected parts of the current subject using package-grounded knowledge
- the caller identifies new concepts, major themes, uncertainty, assumptions, or connections that could profit from enrichment
- should account for previous master-agent calls so already-enriched subjects are not repeated unnecessarily
- answered after `Main.Request.Prompt`
- may return that no material enrichment was found

****

## Context.Enrichment.Call

- `Context.Enrichment.Call` is a master-agent usage pattern where the caller makes an `Enrichment.Request.Prompt` the `Main.Request.Prompt`
- used when enriching a current discussion, subject summary, design, or working context is the primary goal
- the caller may summarize the current subject and ask the master agent to report relevant package-grounded concepts, connections, contradictions, risks, or opportunities
- may optionally include another `Enrichment.Request.Prompt` targeting a narrower or secondary enrichment frontier

****

## Master.Agent.Spawn.Preferences

- `Master.Agent.Spawn.Preferences` guides the caller when spawning `Packages.Master.Agent`
- the caller typically owns agent spawning and configures the model, reasoning effort, service tier, tools, timeout, and context passed to the agent
- use a medium-size, context-efficient model because master-agent work is structured package navigation, research, and synthesis
- use Anthropic Haiku or OpenAI `gpt-5.4-mini`; use the closest available equivalent for other providers
- use low or medium reasoning effort
- preserve read-only operation regardless of spawning configuration
- explicit user spawning instructions override these defaults
