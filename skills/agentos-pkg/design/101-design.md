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

- `Package.Driver` is the minimal context an agent must receive across the `Context.Loading.Path` to be able to work with a `Package.Skill`
- it is distributed across loading tiers: a cold slice may live in a `Cold.Loading.Surface`, the package `SKILL.md` arrives through `SKILL.Loading`, and deeper routes are selected through `Dynamic.Loading`
- the package `SKILL.md` is the canonical runnable driver surface; cold-loading surfaces may project enough driver context to make the package reachable from cold
- functionally it has two parts: `Package.Driver.Base` (always-on orientation) plus `Package.Driver.Router` (routes onward)
- `Package.Driver:<Package>` names the driver of a specific package, e.g. `Package.Driver::Agentos.Pkg`
- the standard route any agent uses to enter a package — including any package-agnostic agent that takes the package as an argument
- when base and router are not enough, the agent descends into the narrower surfaces the router declares

****

## Package.Driver.Base

- `Package.Driver.Base` is the explicit operating explanation carried in the driver itself
- always loaded whenever the `Package.Driver` is loaded — the package's always-on core
- carries the package protocol plus the fundamental vocabulary downstream surfaces assume
- must hold enough vocabulary that its own `Package.Driver.Router` keys are matchable
- minimal by discipline: only what the common paths need, not everything useful

****

## Context.Loading.Path

- `Context.Loading.Path` is the tiered path by which context enters an agent, ordered from guaranteed-at-cold to pulled-on-demand
- each tier is a distinct loading mechanism with its own guarantee level; a later tier becomes reachable only once earlier tiers have loaded what it needs
- tier 1 `Cold.Loading` — context guaranteed present from a cold start
- tier 2 `SKILL.Loading` — context that arrives whole when a skill is loaded
- tier 3 `Dynamic.Loading` — context pulled selectively, on demand
- the path bootstraps itself: each tier loads the keys and surfaces the next tier needs to act

****

## Agentos.AGENTS.Section

- [DF] `Agentos.AGENTS.Section` is the structured Agentos section inside an `AGENTS.md` `Cold.Loading` surface
- [DC] its canonical section heading is `## Agentos`
- [CT] it may carry any Agentos-managed context agents should receive from `AGENTS.md`, including configuration, package-driver hints, subsystem routing, and local policy
- [CT] configuration is a primary use, not the boundary of the section
- [DC] nested `AGENTS.md` surfaces override parent `Agentos.AGENTS.Section` values by nearest-scope precedence
- [CT] `Agentos.AGENTS.Section` is linter-controlled because it participates in `Cold.Loading`, where accidental or conflicting context is paid by every session
- [PR] subsections should be named by subsystem, so each package can own and lint its own Agentos-facing content

****

## Cold.Loading

- `Cold.Loading` is the `Context.Loading.Path` tier guaranteed present from a cold start, before the agent takes any action
- it loads through the `Cold.Loading.Hook`s an agent always sees on entry — skill descriptions and `AGENTS.md`
- the guarantee comes from redundant placement: the same context is wired into many `Context.Hook`s so the system cannot miss it
- it is the bootstrap tier — it carries the minimal vocabulary and routing keys the later tiers need to act at all
- only `Workflow.Neutral.Skill` orientation belongs here — non-steering, safe to always load; its cost is paid every session, so it stays minimal
- [CT] `Cold.Loading` surfaces are linter-controlled because they shape every agent run before task-specific routing begins

****

## Cold.Loading.Hook

- [DF] `Cold.Loading.Hook` is a `Context.Hook` that the harness loads automatically before the agent acts
- [CT] it injects a `Cold.Loading.Surface`
- [EX] project-root `AGENTS.md` is a `Cold.Loading.Hook` when the harness reads it before the agent acts
- [EX] skill descriptions are `Cold.Loading.Hook`s when the harness advertises them before skill selection
- [CT] its loaded content is linter-controlled because every session receives it

****

## Cold.Loading.Surface

- [DF] `Cold.Loading.Surface` is a surface whose content is guaranteed present at `Cold.Loading`
- [CT] it is identified by harness loading behavior, not only by file name or path
- [EX] a project-root `AGENTS.md` loaded before the agent acts is a `Cold.Loading.Surface`
- [CT] a `Context.Hook` is the injection mechanism; `Cold.Loading.Surface` is the loaded content surface
- [CT] `Package.Driver` content may be projected into a `Cold.Loading.Surface` when the package must be reachable from cold
- [CT] `Cold.Loading.Surface`s are linter-controlled because every session pays their context cost

****

## SKILL.Loading

- `SKILL.Loading` is the `Context.Loading.Path` tier that arrives whole when a skill is loaded
- the `SKILL.md` file is its unit — the single discrete loading step between `Cold.Loading` and `Dynamic.Loading`
- it is atomic: loading a skill brings its entire `SKILL.md` at once, all-or-nothing, with no finer selection
- whatever an author wants present the moment a skill is in context belongs in its `SKILL.md`
- it sets up the next tier: the keys and routes loaded here are what `Dynamic.Loading` selects against

****

## Dynamic.Loading

- `Dynamic.Loading` is the `Context.Loading.Path` tier that pulls context selectively, on demand, rather than guaranteeing it
- it loads only what the live situation calls for, keeping context minimal
- two sub-modes today: `Semantic.Router` selection — the agent matches the situation against router keys an earlier tier loaded — and explicit `Batchy.Skill` call — a `Skill.Arg` names the `Skill.Module` to pull (e.g. `--edit`)
- it depends on earlier tiers: it can only select against the routers and keys that `Cold.Loading` or `SKILL.Loading` already brought
- it is open-ended: new pull mechanisms (auto-triggers, agent-initiated fetches) extend this tier without changing the earlier ones

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

## Package.Driver.Router

- `Package.Driver.Router` is the entry `Semantic.Router` the driver carries at the package `SKILL.md` — the first router an agent meets
- maps situations to the package surfaces that handle them: task kinds, concepts, workflows, references, package agents, install surfaces, and `Package.Aux.Skill`
- its keys read in the loaded `Package.Driver.Base` vocabulary; an unmatched situation falls back to the package's general routing
- composes like any `Semantic.Router`: a row may point to a `Skill.Module`, a nested skill's own `Package.Driver`, or a deeper router
- stays transparent: it routes without forcing a workflow, letting `Package.Aux.Skill` aliases carry workflow intention while the router stays neutral

****

## Package.Manifest

- `Package.Manifest` is the settings file of a `Skill.Package` — the config for its (agentic) package manager
- artifact: `package.md` at the package root; data consulted by tooling, not orientation loaded into context (that is the `Package.Driver`)
- declares what the package depends on: other `Skill.Package`s and the external CLIs/tools it needs
- declares how to resolve each dependency when missing — a source and version, e.g. a git repo URL + ref — so the manager can fetch it
- `Skill.Package`s are `Agentos.Skillware` units; like any software they need a package manager, and this is its manifest
- named generically and kept extensible — dependencies are the first content; more package-level settings can land here later

****

## Project.Manifest

- `Project.Manifest` is a project's declaration of the `Package.Skill`s and indexes it engages — the project peer of `Package.Manifest`
- it lives in the project's `AGENTS.md`
- with `Package.Manifest` it forms the dependency graph `Index.Discovery` walks
- it is optional — without it, `Index.Discovery` falls back to searching for `000-INDEX.md`

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
- the caller sends a prompt and a target package; the master agent loads the target's `Package.Driver`, follows the `Package.Driver.Router` as needed, scans the surfaces, and returns an answer with citations
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
- each package is entered through its `Package.Driver` and traversed through its `Package.Driver.Router`
- avoids exhaustive loading; searches likely relevant package surfaces first
- returned answers cite package-qualified concepts and surface paths
- ambiguity and disagreement between packages are surfaced rather than silently resolved

****

## Package.Agent

- `Package.Agent` is an optional read-only agent specialized for answering prompts about a specific `Package.Skill`
- exists when specialization makes it more efficient or reliable than `Packages.Master.Agent` for that package
- loads the package's `Package.Driver` and follows its `Package.Driver.Router`, while adding package-specific prompting, configuration, or knowledge-routing behavior
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
- may be deployed from `Usage.Pattern.Routing` when a hot path deserves its own skill surface

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
- universal: every skill is a `Batchy.Skill`; `-h` help is always available, while arguments, banner, and modules appear only when the skill needs them
- a convention, not a mandate — a clear natural prompt always works; for one obvious argument the agent just grabs it, flags grow valuable as parameter count grows
- when a skill takes arguments, they are declared as `Skill.Arg` blocks inside its `Skill.Arg.Section`
- each argument has a canonical name (e.g. `Skill.Arg::Target.Project`); loose flags, abbreviations, and positionals resolve to it
- tokens are written `--flag`-style by preference so they read as commands inside natural text (`do a --run on stripe-pkg`); loose forms still resolve
- switch flags map to `::` type-statement values (`Addressing.Sigil.Vocabulary`) (`--AUTO` -> `Alignment.Mode::Autonomous`) ^20260712-6
- a skill's files and sections are `Skill.Module`s — named parts loaded on mention; a `Skill.Arg` may carry an `action` that activates one
- missing required arguments follow `Skill.Explicit.Args`: ask or orient, never guess; declared defaults fill silently
- exposes terminal-style help through `Batchy.Skill.Help`

### meta

- detail: `agentos-batchy-skills/references/batchy-skill-designer.md`

****

## Batchy.Skill.Template

- `Batchy.Skill.Template` is the canonical skeleton every `Batchy.Skill` instantiates, so all Agentos skills share one shape
- opens with a `Batchy.Skill.Contract` block — the in-skill mini-course on the convention
- then, optionally, a `Skill.Index.Section` defining the skill's own key concepts
- then, when the skill takes arguments, a `Skill.Arg.Section` of `### Skill.Arg:<Name>` blocks
- then any `Skill.Module`s — named files or sections loaded on mention, optionally fronted by a `Skill.Arg` carrying an `action`
- requires a `Skill.Trigger.Clause` (`USE WHEN`) in the frontmatter description
- adapts per skill: a zero-argument skill omits the `Skill.Arg.Section`, a single-operation skill needs no extra modules; the `Batchy.Skill.Contract` and `Skill.Trigger.Clause` are always present
- the copy-pasteable skeleton lives in `agentos-batchy-skills/references/batchy-skill-designer.md`

****

## Batchy.Skill.Contract

- `Batchy.Skill.Contract` is the in-skill mini-course a `Batchy.Skill` carries — a compact restatement of the convention so the skill complies without `agentos-batchy-skills` loaded
- a `Cited.Duplication`: it duplicates the canonical convention into the skill and cites it for depth
- declares the skill is a `Batchy.Skill` and points to `agentos-batchy-skills` for the full convention
- help rule (always): `-h`/`--help` short-circuits to `Batchy.Skill.Help`, printing the help into the chat instead of running
- banner rule (when it has arguments): a run begins by printing the `Batchy.Skill.Banner` of resolved arguments; a zero-argument skill has none
- resolution rule: loose flags, abbreviations, positionals, and module mentions map to canonical `Skill.Arg` or `Skill.Module` names
- a zero-argument skill carries only the help rule; arg-bearing skills carry all three
- sits at the top of the skill body, ahead of any `Skill.Arg.Section`

****

## Skill.Arg

- `Skill.Arg` is a single argument of a `Batchy.Skill`, written as a kernel block
- named with `::` type statements (`Addressing.Sigil.Vocabulary`): `Skill.Arg::Context`, `Skill.Arg::Main.Prompt` ^20260712-6
- its fundamentals state what the argument means; bullet settings carry its calling metadata
- settings: `required`, `default`, `type` (switch vs valued), `help`, `examples`, `aliases` (non-obvious only), `action`
- `action` (optional): the behavior the arg activates when set — usually loads a `Skill.Module`; a switch (`--dry-run`) layers behavior, a selector whose values are operations (`Command:Run`) picks one
- an arg with an `action` is how a former subcommand is expressed; no dedicated subcommand structure is needed
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

## Skill.Index.Section

- `Skill.Index.Section` is the optional section of a `Batchy.Skill` that defines the skill's own key concepts
- a `Skill.Arg.Section` sibling: a named SKILL section holding one kind of block
- entries are compact concept blocks — a `Dotted.Name` heading plus a few orthogonal lines, like tiny `Index.Block` entries
- scoped to one skill, with no local router; distinct from the package-wide `Package.Skill.Index`
- included only when a skill hinges on a few defined terms, e.g. a two-agent skill defining `Caller.Agent` and `Master.Agent`

### meta

- detail: `agentos-batchy-skills/references/batchy-skill-designer.md`

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

## Skill.Module

- `Skill.Module` is the unit of skill-software — a named, encapsulating subsystem of a skill: a file or section, addressable by name, with hidden internals
- addressable ⇒ loadable on demand — naming a module brings it into context (progressive disclosure)
- it is the substrate Skillware's subsystems build on — a subsystem adds a capability to modules without changing what a module is

****

## Batchy.Skill.Banner

- `Batchy.Skill.Banner` is the resolved-argument banner a `Batchy.Skill` prints as the first step of any run
- shows the mapping from supplied flags to canonical arguments (`--AUTO` -> `Alignment.Mode::Autonomous`) and the values used
- distinguishes supplied values from filled defaults, so the caller sees what was inferred
- informational, not a checkpoint: it echoes the interpretation, it does not ask for confirmation
- makes fuzzy flag resolution auditable — a misread is visible before side effects
- printed on every run except the non-executing `-h` call
- a short banner section in the target skill restates the convention via `Cited.Duplication`, improving compliance
