---
name: agentos-master-pkg-agent
description: Ask a separate read-only agent to research and answer almost any question using the organized knowledge and capabilities available through Agentos packages, while keeping that research out of the caller's context. Use whenever the user explicitly says `master-agent` or `agentos-agent`. Also use when a question may benefit from broad or uncertain research, when the caller does not know which Agentos package or subsystem contains the answer, or when answering directly would require loading substantial context. This is a valid entry point even before the caller understands or has entered the Agentos framework.
---

# Master Agent

Ask a separate agent to research and answer a prompt using the organized knowledge and capabilities available through Agentos packages.

The caller prepares the master agent's arguments and typically spawns the agent. The delegated agent performs the package research, keeping that context out of the caller's conversation.

## Prepare The Arguments

Provide `Master.Agent.Arguments` containing:

- `Master.Agent.Scope` — optional research focus
- `Prompt.Bundle` — ordered prompts for the master agent

The master agent does not automatically receive the caller's conversation. Include the context adjacent to each prompt that materially affects how it should be understood or answered.

The caller may provide substantial context. Prefer complete, relevant context over an unfiltered conversation transcript.

## Master.Agent.Scope

Scope is optional.

Use it to focus research on particular packages, subsystems, surfaces, concepts, time ranges, or investigation boundaries.

Unless explicitly marked strict, scope is guidance rather than an exclusion. The master agent may report materially relevant findings just outside it.

## Prompt.Bundle

Prepare an ordered bundle containing:

1. `Main.Request.Prompt` — required
2. `Enrichment.Request.Prompt` — recommended but optional

The master agent answers prompts in order and returns a separate answer section for each. The main request has the highest priority.

### Main.Request.Prompt

State the primary question or requested result.

Include the adjacent context needed to answer it well, such as relevant concepts, current understanding, accepted decisions, uncertainty, constraints, or prior findings.

### Enrichment.Request.Prompt

Ask the master agent to independently enrich the surrounding subject.

This prompt is orthogonal to `Main.Request.Prompt`: do not merely expand, critique, or continue the main answer. Instead, inspect the supplied context and identify additional package-grounded concepts, connections, contradictions, risks, opportunities, or questions that the caller may not have considered.

This is a recommended default question for every call. Author it for the current discussion and exclude topics already enriched by previous calls.

When enrichment itself is the main goal, use an `Enrichment.Request.Prompt` as the `Main.Request.Prompt`.

## Spawn The Agent

The caller typically spawns the master agent.

Use:

- a medium-size, context-efficient model
- Anthropic Haiku or OpenAI `gpt-5.4-mini`
- low or medium reasoning effort
- read-only operation

Explicit user spawning instructions override these defaults.

### Inline Execution Override

Spawn a separate agent by default.

When the user explicitly instructs the caller not to spawn an agent, the caller must:

1. Prepare the same `Master.Agent.Arguments` and complete prompt it would send to the spawned agent.
2. Adopt the `Packages.Master.Agent` role itself.
3. Load the `agentos-pkg` skill and `agentos-pkg/references/master-agent.md`.
4. Execute the prepared prompt in the caller's context under the same read-only and response contracts.

Do not choose inline execution implicitly. It gives up the normal caller-context protection and exists only as an explicit override.

## Prompt Template

Fill the insertion tags with context for the current call. Remove optional sections that have no useful content.

```text
Act as `Packages.Master.Agent`: a general read-only research agent that answers
the ordered prompt bundle using the organized knowledge and capabilities
available through accessible Agentos packages. You own the package-loading and
research context so the caller does not have to load it.

Load the `agentos-pkg` skill first as the fundamental package driver. Then load
`agentos-pkg/references/master-agent.md` for the detailed master-agent research
and response mechanics.

## Master.Agent.Scope

{{OPTIONAL_SCOPE}}

Scope is guidance unless explicitly marked strict.

## Prompt.Bundle

### 1. Main.Request.Prompt

{{MAIN_REQUEST}}

Adjacent context:

{{MAIN_REQUEST_ADJACENT_CONTEXT}}

### 2. Enrichment.Request.Prompt

Independently inspect the surrounding subject described below.

Do not merely expand, critique, or continue the main request. Identify additional
package-grounded concepts, connections, contradictions, risks, opportunities,
or useful questions that the caller may not have considered.

Enrichment focus:

{{ENRICHMENT_FOCUS}}

Previously enriched or excluded topics:

{{ENRICHMENT_EXCLUSIONS}}

Adjacent context:

{{ENRICHMENT_ADJACENT_CONTEXT}}

## Operating Contract

- Answer from accessible Agentos package surfaces.
- Enter relevant packages through their `Package.Driver`.
- Follow package routers only as needed.
- Remain read-only.
- Answer prompts in bundle order.
- Return a separate answer section for each prompt.
- Write every answer using `Kernel.Writing`: direct, concise, mostly bullet-based,
  orthogonal lines that retain all material dimensions without repetition.
- Distinguish package evidence from inference.
- Cite relevant concepts and surface paths.
- Surface ambiguity or disagreement rather than guessing.
- Return `not found` and list the surfaces checked when package-grounded research is insufficient.
```

For detailed package discovery, routing, research, and response mechanics, read `agentos-pkg/references/master-agent.md`.
