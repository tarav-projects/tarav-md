---
name: agentos-batchy-skills
description: Workflow-neutral conventions base for building Agentos package skills — skill taxonomy, the Batchy calling convention, argument parsing, and placement rules. USE WHEN authoring or upgrading an Agentos skill and you need the shared conventions a proper skill should follow, or when another skill or agent needs to learn how Agentos skills are structured. Loading it orients; it does not run a build workflow.
---

# Agentos Batchy Skills

The conventions base for building Agentos skills. This is a `Workflow.Neutral.Skill`: it teaches how a proper Agentos `Package.Skill` is shaped and called, then routes to the canonical concept blocks. Loading it does not steer the caller into a task.

It exists so all `agentos-pkg` skills share one homogeneous framework instead of each reinventing structure, argument passing, and help.

This is a `Batchy.Skill`, called like a CLI and resolved by one `Batchy.Router`. This compact contract is materialized from `agentos-batchy-skills`; load that skill when the full convention is needed.

- `-h` / `--help` prints callable help into the chat and stops without running
- a written `--<flag>` is intentional run configuration and must be resolved as such
- explicit configuration wins over compatible inferred or default configuration for the same route
- conversational discovery and declared defaults apply only where the applicable router row permits them
- every non-help run with custom configuration first prints its resolved `Batchy.Skill.Banner`
- only external data consumed by the selected behavior is a `Skill.Arg`; operation and module selection remain router effects
- compatible routes may compose, but aliases and composed flags do not create new module identities
- load only selected `Skill.Module`s and the additional context they explicitly require
- declared `User.Command`s are the only way to cross their explicit workflow gates
- when a configured run, command target, or required argument remains materially ambiguous, ask rather than guess

## Boundary

- This skill defines conventions; it does not execute a skill-building workflow.
- For source mining, design discussion, and applying a new or upgraded skill, use `agentos-skills-ingenier`.
- For behavioral testing of a skill, use `agentos-testground`.
Route index or appendix concept writes through `agentos-hugentics --edit`, bind the requested change and index scope, and load its edit contract. Follow `Kernel.Writing`; do not mutate the gated surface until its approval and landing transitions resolve.
- Conventions are conventions an agent knows, not a Bash parser. Clear natural-language calls remain valid wherever the applicable `Batchy.Router.Row` permits automatic discovery.

## Skill Model

The skill taxonomy and roles are canonical in the `agentos-pkg` index (`design/101-design.md`). Read the blocks rather than restating them:

- `Package.Skill` — the self-contained agentic surface for a package or subsystem.
- `Package.Driver` — the minimal load (usually `SKILL.md`) to orient and route.
- `Package.Aux.Skill` — a specialized skill hanging off a package, pointing back to its root.
- `Workflow.Neutral.Skill` vs `Aux.Workflow.Skill` — orient-only vs steer-into-a-task. Choose deliberately; a base or router is neutral, an operation is not.
- `Package.Driver.Router` — the package driver's entry `Routing.Table`; `Package.Skill.Index`, `Package.Skill.Install`, and `Package.Skill.Dependency` are the other package-skill subsystems.
- `Skill.Explicit.Args` — the arguments a skill needs before it can do useful work, and its missing-argument behavior.

## Batchy Convention

Every Agentos skill is a `Batchy.Skill` — called like a terminal command and configured through one `Batchy.Router`. `-h` help is universal; custom flags, arguments, the banner, routing tables, and modules appear only when the skill needs them. The convention is canonical in the index and detailed for authors in the reference:

- `Batchy.Skill` — the universal skill design style; a skill interpreted as a CLI-style command, with `-h` always available.
- `Batchy.Router` — the single runtime router; it resolves run configuration from explicit flags, the live conversation, and declared defaults.
- `Batchy.Skill.Flag` — a `--<flag>` token explicitly configuring the current run; only this written form carries flag semantics.
- `Batchy.Router.Row` — one configured route, including which resolution inputs are permitted and which destination receives the result.
- `Routing.Table` — the declarative router artifact consumed by `Batchy.Router`; on a Skillware-managed surface, the table and each addressed `Batchy.Router.Row` are `Skw.Annotation`s, and generated call/module views derive from that one table.
- `Usage.Pattern.Routing` — a `Batchy.Router.Row` style whose semantic situation key routes a recurring usage pattern.
- `Batchy.Skill.Template` — the canonical skeleton every Batchy skill instantiates.
- `Batchy.Skill.Contract` — the in-skill mini-course restating the convention standalone (a `Cited.Duplication`).
- `Skill.Arg` — one named unit of external run data, written as a `### Skill.Arg::<Name>` kernel block; it owns the data identity and contract while `Batchy.Router` resolves its value.
- `Skill.Arg.Section` — the section of the skill holding its `Skill.Arg` blocks.
- `Batchy.Skill.Help` — the non-executing `-h`/`--help` call assembled from reachable router configuration, arguments, modules, and routing tables.
- `Batchy.Skill.Banner` — the resolved-run-configuration report printed before the routed effects of a non-help run.
- `Skill.Module` — a named, encapsulated subsystem (file or section) that `Batchy.Router` may select and load without representing it as an argument.
- `User.Command` — an explicit `::`-prefixed transition available at declared workflow points.
- `User.Command.Trigger` — one accepted spelling for a canonical command; several triggers may invoke the same command.
- `User.Command.Arg` — one command input, resolved by its declared `Explicit`, `Contextual`, or `Defaulted` policy.
- `User.Command.Section` — the command declarations a workflow-bearing skill exposes.

Detail is split by audience: running a Batchy skill → [references/batchy-skill-run.md](references/batchy-skill-run.md); building one → [references/batchy-skill-designer.md](references/batchy-skill-designer.md).

## Authoring Conventions

- Advertise triggering with a `USE WHEN` clause in the frontmatter `description`.
- Keep `SKILL.md` lean; push depth into `references/` and load it only when needed (progressive disclosure).
- Separate always-on guidance from on-demand expertise.
- Put deterministic or repetitive steps in scripts or CLI calls, not prose.
- Duplicate package knowledge only through `Cited.Duplication`, citing origin blocks.
- Place each piece by `Natural.Placement`: conceptual truth in the index, depth in the appendix or references, behavior in the skill body.
- Name concepts in `Dotted.Notation` so they are referenceable from skill text and the index.
- Declare explicit workflow transitions in a `User.Command.Section`; keep natural conversation free while their gates remain unresolved.

## References

- [references/batchy-skill-run.md](references/batchy-skill-run.md) — operating a Batchy skill (runner-facing).
- [references/batchy-skill-designer.md](references/batchy-skill-designer.md) — building a Batchy skill (designer-facing).
- `agentos-pkg` index `design/101-design.md` — skill model and Batchy concept blocks.
- the derived Hugentics Index write contract above — how to write the index blocks a skill's concepts live in
