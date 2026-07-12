---
name: agentos-master-pkg-agent
description: Ask a separate read-only agent to research and answer almost any question using the organized knowledge and capabilities available through Agentos packages, while keeping that research out of the caller's context. Use whenever the user explicitly says `master-agent` or `agentos-agent`. Also use when a question may benefit from broad or uncertain research, when the caller does not know which Agentos package or subsystem contains the answer, or when answering directly would require loading substantial context. This is a valid entry point even before the caller understands or has entered the Agentos framework.
---

# Master Agent

Ask a separate agent to research and answer a prompt using the organized knowledge and capabilities available through Agentos packages.

The caller prepares the arguments and typically spawns the agent. The delegated agent performs the package research, keeping that context out of the caller's conversation.

This is a `Batchy.Skill`: its arguments are the `Skill.Arg` blocks below, and its `Skill.Module`s (named, activated by mention, e.g. `--index-grounding`) are shortcuts that preset those arguments.

## Skill.Index.Section

This skill runs as two agents. The skill body refers to both throughout.

### Caller.Agent
- the agent that invokes this skill; the only agent with access to the caller's conversation and context
- distills the relevant context into the `Skill.Arg`s and typically spawns the `Master.Agent`
- owns argument preparation and, for `Skill.Module`s, the preset values

### Master.Agent
- the read-only research agent the caller spawns, acting as `Packages.Master.Agent`
- owns package discovery, surface loading, research, and synthesis, keeping that context off the `Caller.Agent`
- answers the supplied prompts from accessible Agentos package surfaces and returns the report

### Hard.Evidence
- every reported fact carries a resolvable link to its source — a surface path plus the concept block or line range it came from
- lets the `Caller.Agent` double-check any claim against the source rather than trusting it
- the `Master.Agent` distinguishes such evidence from its own inference and never reports an ungrounded fact as evidence

## Skill.Arg.Section

The master agent does not receive the caller's conversation. Pass the context each prompt needs explicitly; prefer complete, relevant context over an unfiltered transcript.

### Skill.Arg::Main.Prompt
- the primary question or requested result, answered first and with the highest priority
- may request research, comparison, explanation, critique, enrichment, or another read-only result
- required: true
- help: "the primary question or requested result"
- examples: --prompt "..."

### Skill.Arg::Context
- the adjacent context the master agent needs because it cannot see the caller's conversation
- carries relevant concepts, current understanding, accepted decisions, uncertainty, constraints, or prior findings
- required: false
- help: "context the agent needs to interpret the request"
- examples: --context "..."

### Skill.Arg::Scope
- an optional research focus: particular packages, subsystems, surfaces, concepts, time ranges, or investigation boundaries
- guidance, not a strict exclusion unless explicitly marked strict; materially relevant findings just outside it may still be reported
- when omitted, the master agent discovers relevant packages and surfaces from the request and context
- required: false
- help: "focus the research"
- examples: --scope "agentos-pkg index"

### Skill.Arg::Enrichment.Prompt
- a recommended secondary request: independently inspect the subject and surface additional package-grounded concepts, connections, contradictions, risks, opportunities, or questions the caller had not considered
- orthogonal to `Skill.Arg::Main.Prompt` — not an expansion, critique, or continuation of it
- answered after the main prompt; may return that no material enrichment was found
- author it for the current discussion and exclude topics already enriched by previous calls
- required: false
- help: "ask for independent package-grounded enrichment"
- examples: --enrich "..."

The master agent answers the supplied prompts in order, each in its own answer section, with `Skill.Arg::Main.Prompt` highest priority. When enrichment is the main goal, supply it as `Skill.Arg::Main.Prompt`.

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

1. Prepare the same arguments and complete prompt it would send to the spawned agent.
2. Adopt the `Packages.Master.Agent` role itself.
3. Load the `agentos-pkg` skill and `agentos-pkg/references/master-agent.md`.
4. Execute the prepared prompt in the caller's context under the same read-only and response contracts.

Do not choose inline execution implicitly. It gives up the normal caller-context protection and exists only as an explicit override.

## Modules

A `Skill.Module` here is a named shortcut that presets the arguments for a common call. The caller activates it by mention and adds optional guiding context; spawn, read-only operation, and response mechanics follow this skill unchanged, and the module inherits this skill's `Skill.Arg`s.

Activate by name:

- `/agentos-master-pkg-agent index-grounding`
- `/agentos-master-pkg-agent --index-grounding`

Then add any extra context to further guide the agent.

Available modules:

- `index-grounding` — given what the caller is currently doing, return the existing package knowledge relevant to that context. Lightweight, retrieval-oriented, repeatable. See `references/index-grounding.md`.

To run one, load its file in `references/<name>.md` and fill the prompt template below using the module's preset arguments.

## Prompt Template

Fill the insertion tags with context for the current call. Remove optional sections that have no useful content.

```text
Act as `Packages.Master.Agent`: a general read-only research agent that answers
the ordered prompts using the organized knowledge and capabilities available
through accessible Agentos packages. You own the package-loading and research
context so the caller does not have to load it.

Load the `agentos-pkg` skill first as the fundamental package driver. Then load
`agentos-pkg/references/master-agent.md` for the detailed master-agent research
and response mechanics.

## Scope

{{OPTIONAL_SCOPE}}

Scope is guidance unless explicitly marked strict.

## Main Request

{{MAIN_REQUEST}}

Adjacent context:

{{MAIN_REQUEST_ADJACENT_CONTEXT}}

## Enrichment Request

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
- Answer the prompts in order.
- Return a separate answer section for each prompt.
- Write every answer using `Kernel.Writing`: direct, concise, mostly bullet-based,
  orthogonal lines that retain all material dimensions without repetition.
- Distinguish package evidence from inference.
- Cite relevant concepts and surface paths.
- Surface ambiguity or disagreement rather than guessing.
- Return `not found` and list the surfaces checked when package-grounded research is insufficient.
```

For detailed package discovery, routing, research, and response mechanics, read `agentos-pkg/references/master-agent.md`.
