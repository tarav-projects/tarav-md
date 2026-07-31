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

- [DF] `Dynamic.Loading` is the `Context.Loading.Path` tier that pulls context selectively on demand rather than guaranteeing it ^c20260730-28u
- [DC] it loads only the context selected for the live situation, keeping the active context minimal ^c20260730-28u
- [DC] dynamic module selection is performed by `Batchy.Router`; selection may resolve from an explicit flag, the live conversation, or a `Routing.Table` ^c20260731-10u
- [CT] argument binding may supply external data consumed by a loaded module, but binding data is not itself a context-loading effect ^c20260731-10u
- [CT] dynamic loading can select only against routing keys and module targets made reachable through earlier `Cold.Loading` or `SKILL.Loading` tiers ^c20260730-28u
- [FR] additional routing and pull mechanisms may extend `Dynamic.Loading` without changing the guarantees of earlier loading tiers ^c20260730-28u

****

## Package.Aux.Skill

- `Package.Aux.Skill` is a specialized skill associated with a `Package.Skill` but not itself the package root
- adds caller intention, workflow framing, operational behavior, subsystem focus, or convenience access without becoming a separate package root
- points back to the package root or package subsystem that provides the durable context
- may act as an entry point, alias, `Aux.Workflow.Skill`, install helper, doctor, test runner, or package-agent launcher
- should duplicate package knowledge only through `Cited.Duplication`
- can be workflow-neutral or operational depending on whether it orients the caller or runs a specific workflow

****

## Workflow.Neutral

- [DF] `Workflow.Neutral` is the property of a surface that provides context — rules, structure, routing, boundaries — without steering the caller into a workflow; loading it does not change the caller's current task, action mode, or execution path ^c20260715-4u
- [CT] a `Workflow.Neutral` surface may describe a workflow, but frames it conditionally — "if you are in this situation, you must ..." — never as an imperative to act now ^c20260715-4u
- [CT] a workflow surface takes control of the session; a `Workflow.Neutral` surface only informs whatever module has control ^c20260715-4u
- [DF] `Workflow.Neutral.Skill` is the property held by a whole skill — useful for `Package.Skill` roots because roots welcome many caller intentions transparently ^c20260715-4u
- [DF] `Workflow.Neutral.Module` is the property held by a single `Skill.Module` — the fundamental unit: a skill with only a SKILL.md is a skill with one module ^c20260715-4u
- [CT] contrasts with `Aux.Workflow.Skill`, which intentionally guides a recurring task ^c20260715-4u

****

## Package.Skill.Index

- `Package.Skill.Index` is the conceptual index subsystem of a `Package.Skill`
- organizes package concepts, names, concept blocks, appendix pages, and reference paths for agent use
- is part of the package skill rather than a separate package
- can be exposed through a `Package.Aux.Skill` such as `<package>-index`
- lets agents enter the package through conceptual lookup rather than a task workflow

****

## Package.Driver.Router

- [DF] `Package.Driver.Router` is the specialized entry `Routing.Table` carried by a `Package.Driver` ^c20260731-9u
- [DC] it is consumed by the skill’s `Batchy.Router`, not run as an independent router ^c20260731-9u
- [DC] its rows map package-relevant situations to the surfaces that handle them ^c20260731-9u
- [CT] its destinations may select a `Skill.Module`, a nested `Package.Driver`, or another `Routing.Table` ^c20260731-9u
- [CT] an unmatched situation leaves the table unresolved and allows broader skill routing to continue ^c20260731-9u
- [CT] it remains workflow-neutral: it routes without forcing the caller into a workflow ^c20260731-9u

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
- should still use `agentos-hugentics --ground` for unknown, custom, or exploratory index context needs
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

- [DF] `Batchy.Skill` is the design style every Agentos skill follows: the skill is interpreted by an agent as a callable CLI-like surface ^c20260731-10u
- [DC] every Agentos skill is a `Batchy.Skill`; custom flags, arguments, modules, and a run banner appear only when the skill needs them ^c20260731-10u
- [DC] `Batchy.Router` resolves the configuration of each skill run ^c20260731-10u
- [DC] `-h` and `--help` are built-in `Batchy.Skill.Flag`s that route to `Batchy.Skill.Help` and short-circuit the run ^c20260731-10u
- [CT] a clear natural-language call remains valid wherever the applicable rows permit automatic discovery ^c20260731-10u
- [CT] a written `Batchy.Skill.Flag` must be resolved as explicit routing configuration ^c20260731-10u
- [CT] a resolved route may bind a `Skill.Arg`, select a `Skill.Module`, or contribute or continue routing through a `Routing.Table` ^c20260731-10u
- [DC] arguments are declared as `Skill.Arg` blocks inside the skill's `Skill.Arg.Section` ^c20260731-10u
- [DC] files and sections form the skill's addressable `Skill.Module`s ^c20260731-10u
- [CT] unresolved required arguments follow `Skill.Explicit.Args`: ask or orient, never guess; declared defaults fill silently ^c20260731-10u

### meta

- detail: `agentos-batchy-skills/references/batchy-skill-designer.md`

****

## Batchy.Skill.Flag

- [DF] `Batchy.Skill.Flag` is a `--<flag>` token that explicitly calls `Batchy.Router` with configuration for the current run ^c20260731-10u
- [DC] writing a `Batchy.Skill.Flag` means "I am configuring this run intentionally" ^c20260731-10u
- [CT] only the `--<flag>` form carries flag semantics ^c20260731-10u
- [CT] the applicable `Batchy.Router.Row` determines whether the flag key resolves exactly, through configured aliases, or through a semantic keyword family ^c20260731-10u
- [CT] a flag route may bind a `Skill.Arg`, select a `Skill.Module`, or contribute or continue routing through a `Routing.Table` ^c20260731-10u
- [CT] a flag may carry an explicit value or act as a switch whose routed value is declared by the skill ^c20260731-10u
- [DC] a `Batchy.Skill.Flag` may contribute partial routing context, such as a namespace, without independently selecting a complete run ^c20260731-32u
- [EX] `agentos-hugentics --index --capture` configures one run toward the index surface and capture-oriented routing ^c20260731-10u

****

## Batchy.Skill.Template

- [DF] `Batchy.Skill.Template` is the canonical skeleton every `Batchy.Skill` instantiates so Agentos skills share one adaptable shape ^c20260730-23u
- [DC] the skill opens with a `Batchy.Skill.Contract` and carries a `Skill.Trigger.Clause` in its frontmatter description ^c20260730-23u
- [CT] a `Skill.Index.Section` appears only when the skill needs local concept definitions ^c20260730-23u
- [CT] a `Skill.Arg.Section` appears only when the skill accepts external run data; its blocks may carry the applicable `Batchy.Router` configuration ^c20260731-10u
- [CT] `Skill.Module`s follow `Natural.Placement` and remain addressable routing targets without being represented as arguments ^c20260731-10u
- [CT] additional prompt-context and multi-level routes are declared through `Routing.Table`s ^c20260731-10u
- [DC] the template has no dedicated flag section: each custom flag is declared with the primitive or `Routing.Table` row that owns its effect ^c20260731-10u
- [CT] a `User.Command.Section` appears only when the skill exposes explicit workflow transitions ^c20260730-23u
- [CT] unused optional sections and modules are omitted rather than emitted empty ^c20260730-23u
- [DC] the copy-pasteable skeleton lives in `agentos-batchy-skills/references/batchy-skill-designer.md` ^c20260730-23u

****

## Batchy.Skill.Contract

- [DF] `Batchy.Skill.Contract` is the compact in-skill statement of the Batchy calling convention that a `Batchy.Skill` carries ^c20260730-24u
- [DC] it is a `Cited.Duplication` of the canonical convention and points to `agentos-batchy-skills` for depth ^c20260730-24u
- [DC] it declares that the containing skill is a `Batchy.Skill` ^c20260730-24u
- [DC] it states the universal built-in rule: `-h` and `--help` route to `Batchy.Skill.Help` and short-circuit the run ^c20260730-24u
- [CT] when the skill exposes custom `Batchy.Skill.Flag`s, the contract states that they are explicit routing configuration whose declarations live with the routing primitives that own their effects ^c20260730-24u
- [CT] when the skill exposes custom flags or arguments, the contract states how `Batchy.Skill.Banner` reports their resolved run configuration ^c20260730-24u
- [CT] when the skill exposes `User.Command`s, the contract states that only declared commands may cross their explicit workflow gates ^c20260730-24u
- [CT] the contract carries only the clauses applicable to that skill beyond the universal built-in rule ^c20260730-24u
- [DC] it sits near the top of the skill body, before optional sections and modules ^c20260730-24u

****

## Skill.Arg

- [DF] `Skill.Arg` is a named unit of external run data that a `Batchy.Skill` declares it accepts or needs to function ^c20260731-7u
- [DC] its fundamentals define the data’s meaning; its settings define the data contract through `required`, `default`, and `type` ^c20260731-7u
- [DC] a `Skill.Arg` is written as a `### Skill.Arg::<Name>` kernel block inside the skill’s `Skill.Arg.Section` ^c20260731-7u
- [CT] behavior that depends on a required `Skill.Arg` may execute only after its value resolves ^c20260731-7u
- [CT] `Skill.Arg` owns the external-data identity and contract; `Batchy.Router` resolves its value ^c20260731-7u
- [DC] `Batchy.Skill.Help` and `Batchy.Skill.Banner` render argument meaning and resolved values from `Skill.Arg` blocks ^c20260731-7u

****

## Skill.Arg.Section

- [DF] `Skill.Arg.Section` is the section of a `Batchy.Skill` that declares its accepted external run data as `Skill.Arg` blocks ^c20260730-25u
- [CT] it appears only when the skill accepts external run data; a zero-argument skill omits it ^c20260730-25u
- [DC] each argument is a `### Skill.Arg::<Name>` kernel block nested in the section ^c20260730-25u
- [DC] `Batchy.Skill.Help` renders argument documentation from these blocks, while `Batchy.Skill.Banner` renders their resolved run values ^c20260730-25u

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

- [DF] `Batchy.Skill.Help` is the non-executing help surface selected by the built-in `-h` and `--help` flags of a `Batchy.Skill` ^c20260730-26u
- [DC] it is available on every `Batchy.Skill`, including skills with no custom flags or arguments ^c20260730-26u
- [CT] loading a skill silently orients the agent; selecting `Batchy.Skill.Help` deliberately presents help to the caller ^c20260730-26u
- [DC] selecting it short-circuits the run before any other routed effect executes ^c20260730-26u
- [DC] its output begins with a concise explanation of the skill and then presents its callable usage ^c20260730-26u
- [DC] callable help is assembled from the `Batchy.Router` configuration reachable through `Skill.Arg` blocks, `Skill.Module` targets, and `Routing.Table`s ^c20260731-10u
- [CT] argument-bound flags include their `Skill.Arg` meaning, value shape, required state, and default when applicable ^c20260730-26u
- [CT] a skill with no custom flags or arguments states that it accepts no custom run configuration ^c20260730-26u
- [DC] the help route has precedence over every other flag supplied in the same call ^c20260730-26u

****

## Skill.Module

- [DF] `Skill.Module` is the unit of skill-software: a named, encapsulated subsystem with an addressable identity and hidden internals ^c20260731-7u
- [CT] a concrete `Skill.Module` may be a file or a section, placed according to `Natural.Placement` ^c20260731-7u
- [DC] the module name provides a stable routing target without exposing its internal organization ^c20260731-7u
- [CT] `Skill.Module` owns the subsystem boundary and content; `Batchy.Router` selects and loads it ^c20260731-7u
- [PR] loading only the modules selected for the current situation provides progressive disclosure while keeping the skill’s full capability surface addressable ^c20260731-7u
- [PR] Skillware capabilities extend `Skill.Module`s without changing their fundamental subsystem identity ^c20260731-7u

****

## Batchy.Skill.Banner

- [DF] `Batchy.Skill.Banner` is the resolved-run-configuration report a `Batchy.Skill` presents before executing routed effects ^c20260730-27u
- [CT] a skill with custom flags or arguments presents the banner as the first step of each non-help run; a skill with no custom run configuration may omit it ^c20260730-27u
- [DC] each supplied `Batchy.Skill.Flag` is shown with its resolved routing effect: argument binding, module selection, or contributed routing context ^c20260730-27u
- [DC] resolved `Skill.Arg` values are shown with their canonical argument names ^c20260730-27u
- [CT] the banner distinguishes caller-supplied flags and values, filled defaults, and semantically resolved configuration ^c20260730-27u
- [DC] it is informational rather than a checkpoint: it exposes the interpretation without requesting confirmation ^c20260730-27u
- [PR] exposing resolved routing before execution makes a semantic misinterpretation visible before its effects occur ^c20260730-27u
- [DC] selecting `Batchy.Skill.Help` short-circuits before the banner ^c20260730-27u
- [DC] the target skill restates its banner rule through `Cited.Duplication` when the banner applies ^c20260730-27u

****

## User.Command

- [DF] `User.Command` is a formal user-authored instruction that advances or redirects a declared workflow transition ^c20260725-1u
- [DC] its canonical form is `::<command line>` ^c20260725-1u
- [DC] each command has one canonical identity and one or more equivalent `User.Command.Trigger`s ^c20260725-6u
- [FR] a `User.Command` may appear anywhere in a user turn; it does not need to begin a line ^c20260725-1u
- [CT] a skill declares which `User.Command`s exist and the workflow points where each is available ^c20260725-1u
- [CT] natural conversation may interrupt or reshape a workflow, but a gated transition remains unresolved until a valid explicit `User.Command` ^c20260725-1u
- [CT] the agent prints available commands when the workflow pauses or status is requested, not after ordinary conversational turns ^c20260725-1u
- [CT] a command executes only when its target, availability, and required arguments resolve clearly ^c20260725-1u
- [CT] ambiguity makes the agent ask for the missing command input without advancing the workflow ^c20260725-1u
- [PR] `User.Command` supplies deterministic workflow transitions inside natural conversation while the agent maintains coherence across free-form turns ^c20260725-1u
- [CT] later conversation may invalidate a pending command by changing the transition or proposal it addresses ^c20260725-1u
- [DC] printed commands render in resolved, copy-pasteable form — targets pre-filled from the foreground draft and approved set — with the `::<command> [target]` template form used only when nothing resolves yet ^c20260725-42u
- [CT] when several targets could receive a command, each resolved invocation prints as its own line, so selecting a line both disambiguates and stays copy-pasteable ^c20260725-42u

****

## User.Command.Trigger

- [DF] `User.Command.Trigger` is one accepted `::`-prefixed spelling that invokes a canonical `User.Command` ^c20260725-6u
- [CT] several triggers may resolve to the same command; every trigger shares that command's availability, arguments, action, and workflow transition ^c20260725-6u
- [CT] trigger choice carries no additional state or semantics beyond selecting the canonical command ^c20260725-6u

****

## User.Command.Arg

- [DF] `User.Command.Arg` is one declared input a `User.Command` requires before execution ^c20260725-1u
- [DC] each argument uses one resolution policy: `Explicit`, `Contextual`, or `Defaulted` ^c20260725-1u
- [CT] `Explicit` arguments must appear in the user's command turn ^c20260725-1u
- [CT] `Contextual` arguments may resolve from the conversation or foreground workflow only when unambiguous ^c20260725-1u
- [CT] `Defaulted` arguments use their declared value when absent ^c20260725-1u
- [CT] an unresolved required argument prevents execution and causes the agent to ask for it ^c20260725-1u
- [DC] an Explicit `User.Command.Arg` may carry an `Edition.Approval.Token` — echoing the command is then at once the workflow transition and the `Verbatim.User.Gated` review evidence for the edition it approves ^c20260726-2u

****

## User.Command.Section

- [DF] `User.Command.Section` is the section of a skill that declares its `User.Command` blocks ^c20260725-1u
- [CT] each command declaration names its canonical identity, triggers, available workflow points, action, and `User.Command.Arg`s ^c20260725-6u
- [CT] command declarations make a skill's user-controlled workflow transitions inspectable before execution ^c20260725-1u
