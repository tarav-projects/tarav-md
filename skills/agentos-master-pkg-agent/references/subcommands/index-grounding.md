# SubCommand: index-grounding

A `Batchy.SubCommand` is a named shortcut that presets the arguments the caller would otherwise author by hand. The caller activates it by name and adds optional guiding context; everything else — spawn, read-only contract, response mechanics — follows the base `agentos-master-pkg-agent` skill unchanged, and the subcommand inherits this skill's `Skill.Arg`s.

`index-grounding` is the lightweight, repeatable retrieval call: the caller states what it is currently doing, and the master agent returns the existing package knowledge relevant to that context.

## Purpose

- Pull existing, package-grounded context that is relevant to the caller's current work.
- Stay retrieval-oriented, not generative: surface what already exists, ranked by relevance.
- Be cheap and repeatable — call it any time the caller suspects it is missing context.

## Distinction From Enrichment

- `index-grounding` is inbound retrieval: "given what I am doing, what relevant package knowledge already exists?" The answer points the caller at existing surfaces.
- `Skill.Arg:Enrichment.Prompt` is generative: adjacent concepts, risks, contradictions, or questions the caller had not considered.
- A grounding call does not need an enrichment prompt. Keep it focused on relevance.

## Caller Input

The caller supplies one required slot and may add optional guidance:

- `Grounding.Context` — required. A prompt describing what the caller is currently doing: the task, current understanding, decisions in play, and open questions.
- `Skill.Arg:Scope` — optional. Focus the search on particular packages, subsystems, surfaces, or concepts.
- additional free guidance — optional. Anything that further steers what counts as relevant.

## Preset Arguments

The subcommand presets this skill's `Skill.Arg`s as follows:

- `Skill.Arg:Main.Prompt` is the grounding request below, parameterized by `Grounding.Context`.
- no `Skill.Arg:Enrichment.Prompt` is included by default.
- `Skill.Arg:Scope` passes through when the caller provides one.

## Output Contract

The master agent returns relevant package-grounded material for the supplied context:

- ranked by relevance to `Grounding.Context`, most relevant first.
- each item names the package surface and a concrete path the caller can open.
- each item states, in one line, why it is relevant to the caller's current work.
- include directly relevant concepts, decisions, constraints, and prior findings.
- prefer pointing at existing surfaces over re-explaining their full content.
- return `not found` with the surfaces checked when nothing relevant exists.

## Prompt Template

Fill the base skill's prompt template, using this as the main request and omitting the enrichment request section.

```text
## Main Request (index-grounding)

The caller is grounding its current work. It does not want a new answer or analysis;
it wants the existing package knowledge relevant to what it is doing.

Caller's current context (`Grounding.Context`):

{{GROUNDING_CONTEXT}}

Return the package-grounded material relevant to this context:

- rank items by relevance, most relevant first
- for each item, name the package surface and a concrete path the caller can open
- for each item, give one line on why it is relevant to the caller's current work
- include relevant concepts, decisions, constraints, and prior findings
- prefer pointing at existing surfaces over re-explaining them in full
- return `not found` with the surfaces checked when nothing relevant exists
```
