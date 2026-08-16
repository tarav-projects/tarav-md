# Skill.Design.Workflow.Module

Use this module to turn a capability idea or research findings into an implementation-ready skill design. Discussion remains read-only.

## Design Frame

Resolve the smallest coherent design:

- package role and boundary: `Package.Skill`, `Package.Driver`, `Package.Aux.Skill`, or another justified surface
- trigger clause: concrete `USE WHEN` language that separates adjacent skills
- external data: only genuine `Skill.Arg`s, with missing-value behavior
- behavior selection: one `Batchy.Router`, canonical rows, aliases, defaults, and composition rules
- progressive disclosure: named `Skill.Module`s with natural placement and explicit load routes
- workflow gates: declared `User.Command`s only where conversation must pause before a transition
- artifact placement: runtime guidance in `SKILL.md`, depth in references, deterministic work in scripts, reusable outputs in assets, platform metadata in its native surface
- Skillware graph: roots, real dependencies, copied contracts, derived consumers, build outputs, and checks when the target is managed
- evaluation: a few representative calls or a `tarav-testground` scenario when routing behavior is consequential

Do not invent routes, modules, scripts, or resources merely to make the design look complete. A single-operation skill may remain small.

## Discussion Loop

1. State the proposed direction first.
2. Explain only the decisions that materially constrain implementation.
3. Surface tradeoffs and unresolved choices without front-loading exhaustive detail.
4. Revise the current proposal as the user reacts; invalidate the prior proposal when its boundary or behavior changes materially.
5. When one proposal and target are implementation-ready, pause with `::apply` as the available transition.

The module does not write. A new explicit development request may select `Skill.Develop.Workflow.Module` directly; inside this paused workflow, only `::apply` crosses the apply gate.
