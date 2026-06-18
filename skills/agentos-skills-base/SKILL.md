---
name: agentos-skills-base
description: Workflow-neutral conventions base for building Agentos package skills — skill taxonomy, the Batchy calling convention, argument parsing, and placement rules. USE WHEN authoring or upgrading an Agentos skill and you need the shared conventions a proper skill should follow, or when another skill or agent needs to learn how Agentos skills are structured. Loading it orients; it does not run a build workflow.
---

# Agentos Skills Base

The conventions base for building Agentos skills. This is a `Workflow.Neutral.Skill`: it teaches how a proper Agentos `Package.Skill` is shaped and called, then routes to the canonical concept blocks. Loading it does not steer the caller into a task.

It exists so all `agentos-pkg` skills share one homogeneous framework instead of each reinventing structure, argument passing, and help.

## Boundary

- This skill defines conventions; it does not execute a skill-building workflow.
- For source mining, design discussion, and applying a new or upgraded skill, use `agentos-skills-ingenier`.
- For behavioral testing of a skill, use `agentos-testground`.
- For writing the index blocks a skill's concepts live in, use `agentos-index-writer` and follow `Kernel.Writing`.
- Conventions are conventions an agent knows, not rigid mandates — a clear prompt is always honored.

## Skill Model

The skill taxonomy and roles are canonical in the `agentos-pkg` index (`index/101-index.md`). Read the blocks rather than restating them:

- `Package.Skill` — the self-contained agentic surface for a package or subsystem.
- `Package.Driver` — the minimal load (usually `SKILL.md`) to orient and route.
- `Package.Aux.Skill` — a specialized skill hanging off a package, pointing back to its root.
- `Workflow.Neutral.Skill` vs `Aux.Workflow.Skill` — orient-only vs steer-into-a-task. Choose deliberately; a base or router is neutral, an operation is not.
- `Package.Skill.Router`, `Package.Skill.Index`, `Package.Skill.Install`, `Package.Skill.Dependency` — the internal subsystems of a package skill.
- `Skill.Explicit.Args` — the arguments a skill needs before it can do useful work, and its missing-argument behavior.

## Batchy Convention

Every Agentos skill is a `Batchy.Skill` — called like a terminal command. `-h` help is universal; arguments, banner, and subcommands appear only when the skill needs them. The convention is canonical in the index and detailed for authors in the reference:

- `Batchy.Skill` — the universal skill design style; a skill interpreted as a CLI-style command, with `-h` always and flag arguments when it has them.
- `Batchy.Skill.Template` — the canonical skeleton every Batchy skill instantiates.
- `Batchy.Skill.Contract` — the in-skill mini-course restating the convention standalone (a `Cited.Duplication`).
- `Skill.Arg` — one argument of the skill, written as a `### Skill.Arg:<Name>` kernel block.
- `Skill.Arg.Section` — the section of the skill holding its `Skill.Arg` blocks.
- `Batchy.Skill.Help` — the non-executing `-h`/`--help` call rendered from the skill's `Skill.Arg` blocks.
- `Batchy.Skill.Banner` — the resolved-argument banner printed as the first step of every run.
- `Batchy.SubCommand` — a `Dotted.Name` subroutine, explicitly activated, inheriting the container's arguments.

Authoring detail, the `Skill.Arg.Section` format, resolution rules, and worked examples: [references/batchy-skills.md](references/batchy-skills.md).

## Authoring Conventions

- Advertise triggering with a `USE WHEN` clause in the frontmatter `description`.
- Keep `SKILL.md` lean; push depth into `references/` and load it only when needed (progressive disclosure).
- Separate always-on guidance from on-demand expertise.
- Put deterministic or repetitive steps in scripts or CLI calls, not prose.
- Duplicate package knowledge only through `Cited.Duplication`, citing origin blocks.
- Place each piece by `Natural.Placement`: conceptual truth in the index, depth in the appendix or references, behavior in the skill body.
- Name concepts in `Dotted.Notation` so they are referenceable from skill text and the index.

## References

- [references/batchy-skills.md](references/batchy-skills.md) — the Batchy authoring guide.
- `agentos-pkg` index `index/101-index.md` — skill model and Batchy concept blocks.
- `agentos-index-writer` — how to write the index blocks a skill's concepts live in.
