# Agentos.Surfaces

## Stable.Surface

- `Stable.Surface` is a durable, authoritative surface where a specific facet of project knowledge lives
- all `Stable.Surfaces` have equal authority — no surface is positioned as more important than another
- misalignments between surfaces are resolved context-dependently, not by a fixed hierarchy
- the system must be aligned — drift is a problem to solve, not a hierarchy to invoke

****

## Stable.Md.Surface

- `Stable.Md.Surface` is the markdown subset of `Stable.Surfaces`
- the set of `.md` stable surfaces in a project: index notes, docs, skills, AGENTS.md, and similar

****

## Natural.Placement

- `Natural.Placement` is the principle that each surface holds the facet of a concept that is natural to its function
- the full description of a concept is distributed across surfaces — each complements the others
    - index → conceptual grounding (what it is, why, how it connects) and discovery (where to find it)
    - docs → extended design rationale, narrative, depth
    - skills → operational behavior, workflows
    - code → the implementation itself (the code IS the description)
- each surface should mostly contain what the other surfaces don't
- a well-maintained system has no drift between surfaces AND has content balanced by the nature of each surface
- content that feels unnatural in a surface is probably misplaced
- the anti-pattern is duplication across surfaces — the pattern is complementary coverage

****

## Placement.Balance

- `Placement.Balance` is the equilibrium state of content across surfaces
- the system is balanced when moving content from one surface to another would feel less natural than its current placement
- a diagnostic signal: if you can imagine content fitting better in another surface, the system is not yet balanced
- complementary to `Natural.Placement` — natural placement is the principle, placement balance is the resulting state

****

## Surface.Link.Directionality

- `Public.Surface` (skills) can be referenced from `Local.Surface` (index notes), not the reverse
- skills must not point to index notes — local agents discover index data through index workflows (e.g. `agentos-index-activate`, `agentos-index-trigger`)
- see appendix `125-Agentos.Surfaces.md`
