> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Project.Discovery.System

- `Project.Discovery.System` resolves a command or workflow to an `Agentos.Project` target
- separates three concerns: project identity, project discovery, and command policy
- discovery modes:
    - implicit: parent-walk from start path until `Agentos.Project.Marker` is found
    - explicit: `--project <path>` targets that path; bare `--project` targets current directory
    - `--project-base <basename>` is a safety check — verifies the resolved project root's directory basename matches
- project-aware commands must require at least one explicit selector — must not silently target when all selectors are omitted
- implicit discovery failure must not auto-initialize a project — creation requires explicit user targeting

****

## Agentos.Skills

- `Agentos.Skills` defines skill selection, routing, and import behavior for Agentos projects
- a source contributes discoverable skills: direct path (`{ "path": "..." }`), project-backed (`{ "project": "..." }`), or package
- a profile is an ordered selection of sources plus one or more local depots
- profile resolution: project-local `.agentos/config.json` override → global default profile → hardcoded default
- importing materializes selected skills into depots as managed symlinks
- imported skills may include `Package.Skill` roots and `Package.Aux.Skill` aliases into package subsystems or workflows
- `agentos skills ...` is a project command — uses `Agentos.Project` targeting

****

## Usage.Surface

- `Usage.Surface` is the usage-useful subset of `Public.Surface`
- the surfaces that help external agents and humans understand how to use a project
- includes skills, CLI help, index notes, and other documentation surfaces
- not every surface in `Public.Surface` is equally usage-centric by design

****

## Package.Skill

- `Package.Skill` is a self-contained agentic public surface for a package, project, or subsystem
- like a software package rather than a script: an integrated collection of subsystems for a coherent task area
- collects public markdown knowledge, routing, setup guidance, workflows, references, and agent-facing operating material
- acts as the package-level orientation and routing surface for public agentic knowledge
- supports compact single-skill and split multi-skill layouts under the same semantic concept
- may expose `Package.Aux.Skill` surfaces that add caller intention while pointing back to the package root or subsystem

****

## Package.Driver

- `Package.Driver` is the minimal context an agent must load from a `Package.Skill` to be able to work with that package
- typically the package `SKILL.md` file, including the skill's description as advertised in the skill list
- enough for the agent to orient and route into narrower surfaces (e.g. `Package.Skill.Router`, `Package.Skill.Index`, `Package.Aux.Skill`) when needed
- `Package.Driver:<Package>` names the driver of a specific package, e.g. `Package.Driver:Agentos.Pkg`
- the standard route any agent uses to enter a package — including any package-agnostic agent that takes the package as an argument
- when the driver is not enough, the agent loads narrower surfaces declared by the `Package.Skill.Router`

****

## Package.Aux.Skill

- `Package.Aux.Skill` is a specialized skill associated with a `Package.Skill` but not itself the package root
- adds caller intention, workflow framing, operational behavior, subsystem focus, or convenience access without becoming a separate package root
- points back to the package root or package subsystem that provides the durable context
- may act as an entry point, alias, `Aux.Workflow.Skill`, install helper, doctor, test runner, or package-agent launcher
- should duplicate package knowledge only through `Cited.Duplication`
- can be workflow-neutral or operational depending on whether it orients the caller or runs a specific workflow

****

## Workflow.Neutral.Skill

- `Workflow.Neutral.Skill` provides orientation or package context without steering the caller into a workflow
- loading it should not change the caller's current task, action mode, or execution path
- contains information, routing, boundaries, and references rather than commands or task procedures
- useful for `Package.Skill` roots because package roots welcome many caller intentions transparently
- contrasts with `Aux.Workflow.Skill`, which intentionally guides a recurring task

****

## Package.Skill.Index

- `Package.Skill.Index` is the conceptual index subsystem of a `Package.Skill`
- organizes package concepts, names, concept blocks, appendix pages, and reference paths for agent use
- is part of the package skill rather than a separate package
- can be exposed through a `Package.Aux.Skill` such as `<package>-index`
- lets agents enter the package through conceptual lookup rather than a task workflow

****

## Package.Skill.Router

- `Package.Skill.Router` is the orientation layer inside a `Package.Skill`
- acts as an internal table of contents for package knowledge and capabilities
- stays transparent to caller workflow: it helps the caller find surfaces without prompting a task-flow change
- maps task kinds, concepts, workflows, references, package agents, install surfaces, and auxiliary skills to their package locations
- lets `Package.Aux.Skill` aliases carry workflow intention while the package router remains neutral

****

## Package.Skill.Dependency

- `Package.Skill.Dependency` is the package surface that declares dependencies needed by a `Package.Skill`
- may live as a `Package.Skill.Router` section or as a `references/` file, depending on package size
- covers agentic dependencies: concepts, workflows, routers, install steps, references, or service surfaces provided by another package skill
- external concepts should use qualified names when crossing package boundaries, for example `<package>-skill/Bla.Concept`
- gives agents a formal place to discover which outside package surfaces may need to be loaded, installed, or consulted

****

## Package.Skill.Install

- `Package.Skill.Install` is the installation layer of a `Package.Skill`
- like an install script: performs the setup the package requires
- may create or update auxiliary skills, package-local indexes, references, generated files, software dependencies, CLIs, or local configuration
- may delegate deterministic parts to tools or scripts when available
- belongs to the agentic package surface, but does not make the skill the owner of all implementation code
- should make side effects explicit before changing files

****

## Packages.Master.Agent

- `Packages.Master.Agent` is a general read-only agent that can answer prompts about any `Package.Skill` it is pointed at
- the caller sends a prompt and a target package; the master agent loads the target's `Package.Driver`, follows the `Package.Skill.Router` as needed, scans the surfaces, and returns an answer with citations
- the caller's context is protected — the master agent pays the cost of loading the target package's surfaces, not the caller
- not bound to one package — operates against any `Package.Skill` it has access to
- target package resolution: explicit argument wins; otherwise inferred from project context (e.g. project `AGENTS.md` declaring packages in use); when ambiguous, surfaces the ambiguity rather than guesses
- read-only by design: returns answers, citations, and surface paths; does not edit, install, or run package operations
- failure mode: when the answer is not in the package, returns "not found" plus the surfaces it checked — never hallucinates
- always available as the default; specialized `Package.Agent` instances may exist when a package shows the master is insufficient
- callers invoke through a `Package.Aux.Skill` such as `agentos-master-pkg-agent` that carries the spawn mechanism, prompt-writing guidance, and model configuration

****

## Multi.Package.Operation

- `Multi.Package.Operation` is the ability of `Packages.Master.Agent` to answer prompts requiring context from multiple packages
- explicit target packages constrain the operation; otherwise relevant packages may be inferred from project context
- each package is entered through its `Package.Driver` and traversed through its `Package.Skill.Router`
- avoids exhaustive loading; searches likely relevant package surfaces first
- returned answers cite package-qualified concepts and surface paths
- ambiguity and disagreement between packages are surfaced rather than silently resolved

****

## Package.Agent

- `Package.Agent` is an optional read-only agent specialized for answering prompts about a specific `Package.Skill`
- exists when specialization makes it more efficient or reliable than `Packages.Master.Agent` for that package
- loads the package's `Package.Driver` and follows its `Package.Skill.Router`, while adding package-specific prompting, configuration, or knowledge-routing behavior
- answers using package surfaces with citations and surface paths; does not edit, install, or run package operations
- failure mode: returns "not found" plus the surfaces checked rather than inventing an answer
- callers may invoke it through a package-specific `Package.Aux.Skill` named `<package>-pkg-agent`
- packages do not need to define a `Package.Agent`; `Packages.Master.Agent` remains the default

****

## Aux.Workflow.Skill

- `Aux.Workflow.Skill` is a `Package.Aux.Skill` oriented around executing a recurring workflow
- it is the non-workflow-neutral counterpart: loading it steers the caller into a specific operation
- can include the conceptual framing it needs inline when that improves execution
- uses `Cited.Duplication` to carry known context directly instead of searching the index on every run
- becomes a contextualized execution surface rather than only a thin router
- should cite origin blocks for duplicated concept material
- should still use `agentos-index` for unknown, custom, or exploratory index context needs
- contrasts with `Workflow.Neutral.Skill`, which provides orientation without steering the caller's current task
- may be deployed from a `Package.Skill.UsagePattern` when a hot path deserves its own skill surface

****

## Skill.Explicit.Args

- `Skill.Explicit.Args` is the set of arguments a skill needs from the caller to operate
- like non-zero-arg functions: some skills need data before they can do useful work
- skills with explicit args should declare them in the skill description and in a dedicated section of the skill body
- the description should advertise args so an agent knows what to provide before loading
- the skill body should clarify behavior when args are missing: orient (workflow-neutral), ask, or noop — never guess
- zero-arg call on a workflow-neutral skill with explicit args: the skill loads its orientation context but does not perform an operation
- zero-arg call on an operational skill with explicit args: noop or orient, never assume a target
- examples: `agentos-testground` needs a target package

****

## Package.Skill.UsagePattern

- `Package.Skill.UsagePattern` is a named situation/response pair that captures a common or important usage path through a package
- like a compiler hot path: the package identifies frequent usage situations and provides an optimized, documented route for each
- each pattern has: a trigger situation (what the user asks or needs) and an expected agent behavior path (which surfaces get loaded, in what order, and what the agent produces)
- patterns live in the package's `usage-patterns/` folder as named objects
- from a usage pattern, a package can optionally deploy: a router entry in `Package.SKILL`, an `Aux.Workflow.Skill`, or a testground test
- patterns do not replace the general path — the `Package.SKILL` decision router remains the fallback for situations not captured as a pattern
- new patterns emerge from real usage: chatlas transcripts, repeated user questions, observed agent failures, or reality-weighted test results
- a usage pattern is testable by nature: the situation is the test prompt, the expected behavior path is the behavior tiers

****

## Package.Skill.UsagePattern.Test

- `Package.Skill.UsagePattern.Test` evaluates whether the package delivers the expected behavior for a named usage pattern
- the test prompt is derived from the pattern's situation; the behavior tiers are derived from the pattern's expected response path
- tests run through the `agentos-testground` system: isolated CLI session, chatlas trace capture, tier evaluation
- because the pattern already defines situation and response, generating a test is nearly mechanical
- test results feed back into pattern refinement: if the agent fails, the pattern documentation or the package surfaces may need improvement
- patterns without tests are still useful as documentation; patterns with tests are verified documentation

****

## Skill.Source

- `Skill.Source` is a direct skill root or package-like expansion that contributes discoverable skills
- types: direct path (`{ "path": "..." }`), project-backed (`{ "project": "..." }`), or package (`{ "package": [...] }`)
- project-backed sources scan `<project>/skills` and may publish export packages

****

## Skill.Export.Package

- `Skill.Export.Package` is a named skill package published by a project-backed source

****

## Skill.Profile

- `Skill.Profile` is an ordered selection of sources plus one or more local depots
- resolution: project-local `.agentos/config.json` override → global default profile → hardcoded default

****

## Skill.Depot

- `Skill.Depot` is a project-local directory where imported skill symlinks are materialized
- depots tend to be non-Agentos standard paths — for instance, `.agents/skills`

****

## Selected.Skills

- `Selected.Skills` is the catalog computed from the resolved `Skill.Profile` before depot sync

****

## Imported.Skills

- `Imported.Skills` is the `Selected.Skills` after import syncs depots

****

## Batchy.Skill

- `Batchy.Skill` is the design style every Agentos skill follows — a skill interpreted as a CLI-style command
- universal: every skill is a `Batchy.Skill`; `-h` help is always available, while arguments, banner, and subcommands appear only when the skill needs them
- a convention, not a mandate — a clear natural prompt always works; for one obvious argument the agent just grabs it, flags grow valuable as parameter count grows
- when a skill takes arguments, they are declared as `Skill.Arg` blocks inside its `Skill.Arg.Section`
- each argument has a canonical name (e.g. `Skill.Arg:Target.Project`); loose flags, abbreviations, and positionals resolve to it
- tokens are written `--flag`-style by preference so they read as commands inside natural text (`do a --run on stripe-pkg`); loose forms still resolve
- switch flags map to `Dotted.Parameterized.Notation` values (`--AUTO` -> `Alignment.Mode:Autonomous`)
- missing required arguments follow `Skill.Explicit.Args`: ask or orient, never guess; declared defaults fill silently
- exposes terminal-style help through `Batchy.Skill.Help`

### meta

- detail: `agentos-skills-base/references/batchy-skills.md`

****

## Batchy.Skill.Template

- `Batchy.Skill.Template` is the canonical skeleton every `Batchy.Skill` instantiates, so all Agentos skills share one shape
- opens with a `Batchy.Skill.Contract` block — the in-skill mini-course on the convention
- then, when the skill takes arguments, a `Skill.Arg.Section` of `### Skill.Arg:<Name>` blocks
- then optional `Batchy.SubCommand`s, each a nested Batchy skill loaded on demand
- requires a `Skill.Trigger.Clause` (`USE WHEN`) in the frontmatter description
- adapts per skill: a zero-argument skill omits the `Skill.Arg.Section`, a single-operation skill omits subcommands; the `Batchy.Skill.Contract` and `Skill.Trigger.Clause` are always present
- the copy-pasteable skeleton lives in `agentos-skills-base/references/batchy-skills.md`

****

## Batchy.Skill.Contract

- `Batchy.Skill.Contract` is the in-skill mini-course a `Batchy.Skill` carries — a compact restatement of the convention so the skill complies without `agentos-skills-base` loaded
- a `Cited.Duplication`: it duplicates the canonical convention into the skill and cites it for depth
- declares the skill is a `Batchy.Skill` and points to `agentos-skills-base` for the full convention
- help rule (always): `-h`/`--help` short-circuits to `Batchy.Skill.Help`, printing the help into the chat instead of running
- banner rule (when it has arguments): a run begins by printing the `Batchy.Skill.Banner` of resolved arguments; a zero-argument skill has none
- resolution rule (when it has arguments): loose flags, abbreviations, and positionals map to canonical `Skill.Arg` names
- a zero-argument skill carries only the help rule; arg-bearing skills carry all three
- sits at the top of the skill body, ahead of any `Skill.Arg.Section`

****

## Skill.Arg

- `Skill.Arg` is a single argument of a `Batchy.Skill`, written as a kernel block
- named with `Dotted.Parameterized.Notation`: `Skill.Arg:Context`, `Skill.Arg:Main.Prompt`
- its fundamentals state what the argument means; bullet settings carry its calling metadata
- settings: `required`, `default`, `type` (switch vs valued), `help`, `examples`, `aliases` (non-obvious only)
- the canonical name is used unambiguously in the skill body; loose flags resolve to it
- lives as a `###` block inside the skill's `Skill.Arg.Section`
- `Batchy.Skill.Help` and `Batchy.Skill.Banner` render from these blocks

****

## Skill.Arg.Section

- `Skill.Arg.Section` is the section of a `Batchy.Skill` that holds its arguments
- present only when the skill takes arguments; a zero-argument skill has none
- each argument is a `### Skill.Arg:<Name>` block nested in the section
- block-based, never a markdown table — these blocks are the single declaration of the skill's arguments
- the agent resolves loose flags, abbreviations, and positionals against them to the canonical `Skill.Arg` name
- the source that `Batchy.Skill.Help` and `Batchy.Skill.Banner` render from

****

## Batchy.Skill.Help

- `Batchy.Skill.Help` is the `-h`/`--help` call of a `Batchy.Skill` — prints the skill's help into the chat instead of running
- available on every skill, including zero-argument ones — the universal half of the convention
- distinct from loading the skill: loading silently orients the agent, `-h` is a deliberate help output to the user
- a non-executing call: it short-circuits the skill, orienting the caller without performing the operation
- leads with a one-paragraph explanation of what the skill is and does, then the usage
- usage is rendered from the skill's `Skill.Arg` blocks; a zero-argument skill states it takes none
- available regardless of other supplied flags — `-h` always wins over execution

****

## Batchy.SubCommand

- `Batchy.SubCommand` is a `Dotted.Name` subroutine of a `Batchy.Skill`, explicitly activated by name
- lives as a section or a file in the skill folder; loaded only when called — lazy activation keeps context lean
- selected like an argument that activates a subroutine rather than passing data (`--index-write` ≈ activate `Index.Write`)
- the agent resolves loose forms (`--index-write`, `INDEX-WRITE`, `index-write`) to the canonical subcommand name
- each subcommand is itself a `Batchy.Skill`: its own `Skill.Arg.Section` and `Batchy.Skill.Help`
- a subcommand inherits the container skill's arguments, and adds its own on top
- help composes — top-level `-h` lists subcommands; `<subcommand> -h` renders that subcommand's `Skill.Arg` blocks
- the skill designer keeps argument and subcommand names sufficiently distinct so activation is unambiguous

****

## Batchy.Skill.Banner

- `Batchy.Skill.Banner` is the resolved-argument banner a `Batchy.Skill` prints as the first step of any run
- shows the mapping from supplied flags to canonical arguments (`--AUTO` -> `Alignment.Mode:Autonomous`) and the values used
- distinguishes supplied values from filled defaults, so the caller sees what was inferred
- informational, not a checkpoint: it echoes the interpretation, it does not ask for confirmation
- makes fuzzy flag resolution auditable — a misread is visible before side effects
- printed on every run except the non-executing `-h` call
- a short banner section in the target skill restates the convention via `Cited.Duplication`, improving compliance
