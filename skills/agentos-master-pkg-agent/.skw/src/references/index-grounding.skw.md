# Module: index-grounding

A `Skill.Module` is a named shortcut that presets the parent skill's arguments for a common call. The caller activates it by mention and adds optional guiding context; everything else — spawn, read-only contract, response mechanics — follows the base `agentos-master-pkg-agent` skill unchanged. The module inherits the parent skill's `Skill.Arg`s and does not redefine them.

`index-grounding` is the lightweight, repeatable retrieval call: the caller states what it is currently doing, and the master agent returns the existing package knowledge relevant to that context.

## When To Use

- Pull existing, package-grounded context relevant to the caller's current work.
- Retrieval-oriented, not generative: surface what already exists, ranked by relevance, pointing at concrete surfaces.
- Cheap and repeatable — activate it any time the caller suspects it is missing context.
- Distinct from `Skill.Arg::Enrichment.Prompt`, which generates adjacent concepts, risks, or questions the caller had not considered. Grounding only retrieves; it does not need an enrichment prompt.

## Caller Input

The module reads the parent skill's inherited `Skill.Arg`s. The caller supplies:

- `Skill.Arg::Context` — what the caller is currently doing: task, current understanding, decisions in play, open questions. This is the material the module grounds against. **Default: the `Caller.Agent` summarizes the live session context itself** — it does not ask the user. Only the `Caller.Agent` can see the caller conversation, so distilling the relevant slice into `Skill.Arg::Context` is its job. Summarize the relevant context, do not dump the transcript.
- `Skill.Arg::Scope` — optional. Focus the search on particular packages, subsystems, surfaces, or concepts.

The caller does not author `Skill.Arg::Main.Prompt` — the module presets it.

## Preset Arguments

The module presets the parent skill's `Skill.Arg`s as follows:

- `Skill.Arg::Main.Prompt` — preset to the fixed grounding request in the template below.
- `Skill.Arg::Context` — passes through from the caller; it is the context the request grounds against.
- `Skill.Arg::Scope` — passes through when the caller provides one.
- `Skill.Arg::Enrichment.Prompt` — omitted by default.

## Output Contract

This module is `Hard.Evidence`-driven so the caller can double-check every claim. This raises the citation bar above the base skill: where the base master agent cites only when it materially helps, grounding makes a link **mandatory per fact**.

The master agent returns relevant package-grounded material for the supplied context:

- ranked by relevance to the caller's context, most relevant first.
- **every fact carries a resolvable link** — a surface path plus the concept block or line range — so the caller can open it and verify.
- each item states, in one line, why it is relevant to the caller's current work.
- includes directly relevant concepts, decisions, constraints, and prior findings.
- prefers pointing at existing surfaces over re-explaining their full content.
- distinguishes package evidence from inference; never reports an ungrounded fact as evidence.
- returns `not found` with the surfaces checked when nothing relevant exists.

## Prompt Template

Fill the parent skill's prompt template, using this as the main request, the caller's `Skill.Arg::Context` as the adjacent context, and omitting the enrichment request section.

```text
## Main Request (index-grounding)

The caller is grounding its current work. It does not want a new answer or analysis;
it wants the existing package knowledge relevant to what it is doing.

What the caller is currently doing (`Skill.Arg::Context`):

{{CONTEXT}}

Return the package-grounded material relevant to this context. This is `Hard.Evidence`
driven: every fact must carry a resolvable link so the caller can verify it.

- rank items by relevance, most relevant first
- for every fact, give a resolvable link — a surface path plus the concept block or line range
- for each item, give one line on why it is relevant to the caller's current work
- include relevant concepts, decisions, constraints, and prior findings
- prefer pointing at existing surfaces over re-explaining them in full
- distinguish package evidence from inference; never report an ungrounded fact as evidence
- return `not found` with the surfaces checked when nothing relevant exists
```

> $kw: --from Hard.Evidence
> $kw: --from Skill.Arg
> $kw: --from Skill.Module
