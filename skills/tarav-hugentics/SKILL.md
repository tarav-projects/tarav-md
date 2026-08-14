---
name: tarav-hugentics
description: "Canonical public control surface for Hugentic sessions. USE WHEN you need session routing, touched-data contextualization, product design, implementation design or execution, capture, reconciliation, parking, status, index research, editing, diagnosis, testing, or maintenance."
---

# Agentos Hugentics

Canonical `Package.Driver` and single public session-control surface for the Agentos Hugentic system.

`Touched.Index` is the global system for contextualizing relevant `Touched.Data`. The Markdown `Agentos.Index.System`, trailing Anchory anchors, and Chatlas support records are its current realization, not its conceptual boundary.

Index capabilities remain a distinct internal subsystem because nearly every Hugentic workflow depends on touched-data contextualization. The caller nevertheless controls the whole session here: product design, implementation design and execution, capture with optional read-only audit, status, parking, and every Index operation route through named modules without requiring another public skill.

This is a `Batchy.Skill`; `Batchy.Router` resolves every run from explicit flags, the live conversation, and declared defaults.

`Hugentic.Capture.Workflow` is the shared public alignment loop. A `Design.Req.Promotion` temporarily retargets that loop without creating another router or workflow identity.

- `-h` / `--help` explicitly routes to `Batchy.Skill.Help` and short-circuits the run.
- a written `--<flag>` is intentional run configuration and must be resolved as such.
- without an explicit route, conversational discovery remains available wherever the applicable row permits it.
- declared `User.Command`s are the only way to cross their explicit workflow gates.
- when an index workflow pauses, print only the commands available at that checkpoint.

## Shared Runtime Contracts

These addressed contracts are always available after `SKILL.md` loads. The universal Batchy contract is copied mechanically from `tarav-batchy-skills`; Hugentics owns only its concrete extensions. Child modules may declare the local addresses as loading dependencies instead of restating their rules.

### Batchy.Skill.Runtime.Contract

This is a `Batchy.Skill`, called like a CLI and resolved by one `Batchy.Router`. This compact contract is materialized from `tarav-batchy-skills`; load that skill when the full convention is needed.

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

### Hugentics.Skill.Arg.Contract

- `Main.Prompt` is the current explicit request or applicable conversational input for the selected module
- `Alignment.Mode` defaults to interactive unless explicit configuration or a routed default selects autonomous operation
- `Depot` and `Chapter` scope Index work without independently selecting an operation

### Hugentics.User.Command.Contract

- approval marks the resolved verbatim proposal approved without writing it
- landing writes only approved material and never implies approval
- `::land-all-approved` fails closed unless one foreground workflow supplies the approved cluster

### Hugentics.Authority.Contract

- treat `Touched.Data` as authoritative only through its qualifying `Touch.Authority.Surface` and current line standing
- distinguish grounded `Touched.Authority`, ungrounded `Index.Presumption`, reviewed state, and demoted history
- follow `Support.Set` references when the index digest is insufficient, disputed, or consequential
- surface contradictions and support gaps as `POI.Instance`s rather than resolving them silently

## Skill.Arg.Section

Only external data consumed by the selected module is a `Skill.Arg`. Operation flags belong to `Batchy.Router` below.

### Skill.Arg::Main.Prompt
- the caller-supplied focus, target, artifact reference, or request body consumed by the selected module
- required: false
- default: the caller's current explicit request or applicable conversation context
- help: "the subject or input for the selected Hugentics operation"
- examples: --search "Index.AGENTS.MD", --design "the Batchy skill framework", --execute 601

### Skill.Arg::Alignment.Mode
- whether declared workflow checkpoints are interactive or autonomous
- required: false
- default: Interactive
- type: enum
- values: `Alignment.Mode::Interactive`, `Alignment.Mode::Autonomous`
- flags: --AUTO, --auto, --autonomous

### Skill.Arg::Depot
- one or more engaged `Index.Depot`s that scope index work
- required: false
- default: task-relevant engaged depots
- flags: --depot
- examples: --depot tarav-pkg, --depot tarav-chatlas-pkg

### Skill.Arg::Chapter
- the `Index.Chapter` selected within the engaged depots
- required: false
- default: design
- flags: --chapter
- examples: --chapter design, --chapter impl

## Batchy.Router

The public flags below call the single running `Batchy.Router`. A trailing value binds `Skill.Arg::Main.Prompt` for the selected module; data-only flags bind their named `Skill.Arg` without selecting a module. This call surface is compiled from the canonical `Routing.Table` below.

| Canonical configuration | Aliases | Resolution | Routed effect |
|---|---|---|---|
| `--index` | - | explicit | contribute the Index namespace/context; with capture and no narrower target, select the reviewed main Index surfaces |
| `--main` | - | explicit | select the reviewed main Index target; with capture, this is operationally equivalent to --index |
| `--search` | `--research`<br>`--ground` | explicit-or-semantic; default: Index namespace when omitted | select Index.Search.Operation.Module; --search, --research, and --ground are operationally equivalent |
| `--capture` | - | explicit-or-semantic | select the shared capture loop and leave its durable target unresolved until another route or conversation supplies it |
| `--agendix` | - | explicit; default: Alignment.Mode::Autonomous | apply the --index --capture --agendix shorthand and use the autonomous alignment default |
| `--design` | - | explicit-or-semantic | select the shared capture loop with Design.Req target knowledge |
| `--edit` | `--write`<br>`--append` | explicit-or-semantic | route through the gated Index landing contract; trailing input binds Main.Prompt and --depot/--chapter bind scope |
| `--reconcile` | - | explicit-or-semantic | run the bulk read-only coverage pass and advance cursors only when reconciliation was explicitly requested |
| `--issues` | `--issue` | explicit-or-semantic | select the grounded Issue.Block lifecycle without inferring review from folder placement |
| `--check` | `--lint` | explicit-or-semantic | select Index.Check.Operation.Module |
| `--type` | - | explicit-or-semantic | load Index.Line.Type.Knowledge.Module |
| `--link` | - | explicit-or-semantic | select Anchory.Link.Operation.Module |
| `--impl` | `--implementation` | explicit-or-semantic | enter Implementation.Workflow.Router.Module and resolve exactly one implementation workflow from flags, input, conversation, or a declared default |
| `--impl --design` | `--impl-design` | explicit-or-semantic; default: implementation input without an `Impl.Req` | select Implementation.Design.Workflow.Module |
| `--impl --review` | `--review` | explicit-or-semantic | select Implementation.Review.Workflow.Module |
| `--impl --execute` | `--execute`<br>`--exec` | explicit-or-semantic; default: `Impl.Req` input | select Implementation.Execute.Workflow.Module |
| `--impl --develop` | `--develop`<br>`--dev` | explicit-or-semantic | select Implementation.Develop.Workflow.Module |
| `--impl --capture` | `--impl-capture` | explicit-or-semantic | select Implementation.Capture.Workflow.Module |
| `--capture --audit` | - | explicit-or-semantic | run Hugentic.Capture.Workflow.Module through its read-only roadmap and stop |
| `--status` | `--chat-status` | explicit-or-semantic | select Chat.Status.Operation.Module |
| `--workflow-status` | - | explicit-or-semantic | select Workflow.Status.Operation.Module |
| `--session-router` | `--what-now`<br>`--what-next` | explicit-or-semantic | select Hugentic.Session.Router.Operation.Module |
| `--park` | `--parking-note` | explicit-or-semantic | select Parking.Note.Operation.Module |
| `--clean` | `--codebase-cleaner`<br>`--cleanup` | explicit-or-semantic | select Codebase.Cleanup.Workflow.Module and enter the Implementation namespace |
| `--AUTO` | `--auto`<br>`--autonomous` | explicit | bind Skill.Arg::Alignment.Mode to Alignment.Mode::Autonomous |
| `--depot` | - | explicit | bind Skill.Arg::Depot and apply it to the selected Index operation |
| `--chapter` | - | explicit | bind Skill.Arg::Chapter and apply it to the selected Index operation |

## Skill.Module Catalog

Canonical module identity is explicit and independent from invocation spelling. `Batchy.Router` rows may use aliases, composed flags, conversational discovery, or defaults to select one canonical module; those routes do not create additional modules. This catalog is compiled from the same canonical table as the public call surface.

### Router Modules

| Canonical module | Load target | Routing |
|---|---|---|
| `Implementation.Workflow.Router.Module` | `references/impl.md` | `--impl`, `--implementation`<br>`--clean`, `--codebase-cleaner`, `--cleanup` |

### Workflow Modules

| Canonical module | Load target | Routing |
|---|---|---|
| `Hugentic.Capture.Workflow.Module` | `references/capture.md` | `--capture`<br>`--agendix`; default: Alignment.Mode::Autonomous<br>`--design`<br>`--capture --audit` |
| `Implementation.Design.Workflow.Module` | `references/impl/design.md` | `--impl --design`, `--impl-design`; default: implementation input without an `Impl.Req` |
| `Implementation.Review.Workflow.Module` | `references/impl/review.md` | `--impl --review`, `--review` |
| `Implementation.Execute.Workflow.Module` | `references/impl/execute.md` | `--impl --execute`, `--execute`, `--exec`; default: `Impl.Req` input |
| `Implementation.Develop.Workflow.Module` | `references/impl/develop.md` | `--impl --develop`, `--develop`, `--dev` |
| `Implementation.Capture.Workflow.Module` | `references/impl/impl-capture.md` | `--impl --capture`, `--impl-capture` |
| `Codebase.Cleanup.Workflow.Module` | `references/codebase-cleaner.md` | `--clean`, `--codebase-cleaner`, `--cleanup` |

### Knowledge Modules

| Canonical module | Load target | Routing |
|---|---|---|
| `Index.Agendix.Knowledge.Module` | `references/agendix.md` | `--agendix`; default: Alignment.Mode::Autonomous |
| `Design.Req.Knowledge.Module` | `references/design-req.md` | `--design` |
| `Index.Landing.Knowledge.Module` | `references/edit.md` | `--edit`, `--write`, `--append` |
| `Index.Line.Type.Knowledge.Module` | `references/type.md` | `--type` |
| `Touched.Data.Knowledge.Module` | `references/touched-data.md` | semantic |
| `Touched.Decision.Knowledge.Module` | `references/decision-cycle.md` | semantic |
| `Alignment.Session.Knowledge.Module` | `references/alignment-session.md` | semantic |
| `Implementation.Execution.Practices.Knowledge.Module` | `references/impl/general-practices.md` | semantic |
| `Implementation.Execution.Preferences.Knowledge.Module` | `references/impl/general-preferences.md` | semantic |
| `Agentos.Package.Knowledge.Module` | - | semantic |
| `Index.Block.Example.Knowledge.Module` | - | semantic |

### Operation Modules

| Canonical module | Load target | Routing |
|---|---|---|
| `Index.Search.Operation.Module` | `references/search.md` | `--search`, `--research`, `--ground`; default: Index namespace when omitted |
| `Project.Chat.Reconciliation.Operation.Module` | `references/reconcile.md` | `--reconcile` |
| `Index.Issue.Operation.Module` | `references/issues.md` | `--issues`, `--issue` |
| `Index.Check.Operation.Module` | `references/check.md` | `--check`, `--lint` |
| `Anchory.Link.Operation.Module` | `references/link.md` | `--link` |
| `Chat.Status.Operation.Module` | `references/chat-status.md` | `--status`, `--chat-status` |
| `Workflow.Status.Operation.Module` | `references/workflow-status.md` | `--workflow-status` |
| `Hugentic.Session.Router.Operation.Module` | `references/session-router.md` | `--session-router`, `--what-now`, `--what-next` |
| `Parking.Note.Operation.Module` | `references/parking-note.md` | `--park`, `--parking-note` |

### Context Assembly Modules

| Canonical module | Load target | Routing |
|---|---|---|
| `Hugentic.Index.Context.Assembly.Module` | `references/index-context-assembly.md` | semantic |
| `Hugentic.Capture.Context.Assembly.Module` | `references/index-capture-context.md` | semantic |

Supporting examples such as `references/impl/example.md` are reference assets, not runnable modules.

## User.Command.Section

This `User.Command.Section` declares the canonical commands below. Each accepted `User.Command.Trigger` resolves to one command, whose nested `User.Command.Arg` blocks govern target resolution.

### User.Command::Approve
- accept an approval-ready index draft in its current form without writing it
- triggers: `::approve`, `::approved`
- available: when `--capture`, direct `--edit`, or a `Capture.Offer` has one or more approval-ready drafts
- action: mark the resolved target approved and unlanded
- policy: index workflows mint and advertise only `::approve <token>`; a bare approval is a supported semantic approval form in the general command model but does not cross this workflow's `Line.Verbatim.Gate`

#### User.Command.Arg::Token
- the fresh `Edition.Approval.Token` printed with the proposed landing content
- required: false
- resolution: Explicit
- examples: `::approve idx-edition:7d2f91c4`
- when present, resolves the proposal it was minted for and upgrades materially equivalent landed lines to CPU-checkable `Reviewed.Content`

#### User.Command.Arg::Target
- the draft, block, line, or revision to approve
- required: true
- resolution: Contextual
- examples: `::approve`, `::approved the block after the correction`, `::approve idx-edition:7d2f91c4`

### User.Command::Land
- write approved, unlanded index material through its declared landing procedure
- triggers: `::land`, `::write`
- available: when the foreground index workflow holds one or more approved, unlanded targets
- action: land the resolved target set; never approve material implicitly
- presentation: workflow modules decide when to suggest landing; in `--capture`, approval normally advances to the next review item while explicit early landing remains valid

#### User.Command.Arg::Target
- the approved item or set to land
- required: true
- resolution: Contextual
- examples: `::land`, `::write all approved blocks`

### User.Command::LandAllApproved
- write the complete approved, unlanded cluster held by one foreground index workflow
- triggers: `::land-all-approved`
- available: when the foreground index workflow holds one or more approved, unlanded targets
- args: none
- action: land every approved, unlanded target in that foreground workflow; never approve material implicitly
- resolution: fail closed unless exactly one foreground index workflow supplies the approved cluster

## Boundary

- this skill is the canonical public entry surface for Hugentic session control, including the global `Touched.Index` system
- it distinguishes the general authority, support, and decision model from the current Markdown/Anchory/Chatlas realization
- it remains a `Workflow.Neutral.Skill` when no explicit arg is selected
- it routes into named modules instead of splitting session control across public skills
- Index modules own Index mechanics; the root owns public workflow selection
- the lower-level `agentos index ...` CLI remains the mechanical implementation surface
- no separate public compatibility entry exists for the Index subsystem

## What The Index Is

- `Touched.Index` curates and densely presents relevant touched data so prior alignment can condition later work
- the authority path is `Touch.Authority.Surface` → `Touched.Data` → `Support.Set` → `Support.Reference` → `Index.Line`
- the support sets of current and historical projections compose `Touched.Support.Network`
- grounded `Live.Index.Line` content carries `Touched.Authority`; ungrounded live content carries weaker `Index.Presumption`
- `Demoted.Index.Line` content is historical rather than current guidance
- contradictory or ambiguous touched positions become `POI.Instance`s and are resolved through `Open.Inference` plus, when needed, a separate gated reconciliation
- the current `Agentos.Index.System` realization is `Index.Skillware` and an `Alignment.Surface` between humans and agents
- it contains `Named.Concepts` written in `Kernel.Block::Index` blocks, organized in `Index.Chapter` files under `Index.Ontology`, routed by `000-INDEX.md`, with `Index.Appendix` depth and `Index.Agendix` leads
- the active chapter defaults to `design`; chapter files are named `NNN-<chapter>.md`
- index work happens over engaged `Index.Depot`s; `--depot` scopes which depots are engaged and `--chapter` scopes within them
- its lines carry `Line.Type` codes (`- [CT] ...`) classifying each line's act; untyped lines are pre-fence legacy
- its current support references are trailing `Anchory.Anchor`s resolving through Chatlas to qualifying user-turn evidence
- chronological chat capture lives in `Chat.Index.Delta` files; `Chat.Index.HEAD` is the chat's current projection
- an ordinary Project line eventually needs an exact Delta home and, when current for that chat, a matching Chat HEAD line
- each `Index.Line.Anchor` dossier asserts the current `Line.Type + body + Anchor.Id` triplet and records independent support, gate, and provenance relationships; Delta materialization and `Line.Home` are derived
- `issues/` holds grounded temporary Project topics; review is proven by the anchor record rather than folder placement
- agents operate it by loading routers, concept blocks, appendix material, and references relevant to the current task

## Routing.Table

This addressed `Routing.Table` is the package driver's single declarative dispatch artifact. Explicit flags select applicable rows directly; conversation and defaults may select rows whose policy permits automatic discovery. Rows compose because the table's selection cardinality is `many`.

Selection cardinality: `many`.

### `^route-index-namespace`

- match: `explicit`
- flags: `--index`
- destinations: `Index.Namespace`
- then: contribute the Index namespace/context; with capture and no narrower target, select the reviewed main Index surfaces

### `^route-index-main`

- match: `explicit`
- flags: `--main`
- destinations: `Index.Main.Target`
- then: select the reviewed main Index target; with capture, this is operationally equivalent to --index

### `^route-index-search`

- match: `explicit-or-semantic`
- flags: `--search`
- aliases: `--research`, `--ground`
- defaults: Index namespace when omitted
- destinations: `Index.Search.Operation.Module`
- loads: `references/search.md`
- when: the caller wants to find concepts, retrieve cited index context, inspect related blocks, discover appendix depth, or ground the visible discussion
- then: select Index.Search.Operation.Module; --search, --research, and --ground are operationally equivalent

### `^route-capture`

- match: `explicit-or-semantic`
- flags: `--capture`
- destinations: `Hugentic.Capture.Workflow.Module`
- loads: `references/capture.md`
- when: the caller wants chat material aligned into a durable target
- then: select the shared capture loop and leave its durable target unresolved until another route or conversation supplies it

### `^route-agendix`

- match: `explicit`
- flags: `--agendix`
- defaults: Alignment.Mode::Autonomous
- destinations: `Hugentic.Capture.Workflow.Module`, `Index.Agendix.Knowledge.Module`
- loads: `references/capture.md`, `references/agendix.md`
- then: apply the --index --capture --agendix shorthand and use the autonomous alignment default

### `^route-product-design`

- match: `explicit-or-semantic`
- flags: `--design`
- destinations: `Hugentic.Capture.Workflow.Module`, `Design.Req.Knowledge.Module`
- loads: `references/capture.md`, `references/design-req.md`
- when: the caller wants product design or organic design work begins outside the Implementation namespace
- then: select the shared capture loop with Design.Req target knowledge

### `^index-write-entry`

- match: `explicit-or-semantic`
- flags: `--edit`
- aliases: `--write`, `--append`
- destinations: `Index.Landing.Knowledge.Module`
- loads: `references/edit.md`
- when: an index or appendix surface is being written or an approved edit needs landing
- then: route through the gated Index landing contract; trailing input binds Main.Prompt and --depot/--chapter bind scope

### `^route-reconcile`

- match: `explicit-or-semantic`
- flags: `--reconcile`
- destinations: `Project.Chat.Reconciliation.Operation.Module`
- loads: `references/reconcile.md`
- when: Project Index lines, support Chat.Indexes, or their reconciliation cursors must be compared or maintained
- then: run the bulk read-only coverage pass and advance cursors only when reconciliation was explicitly requested

### `^route-issues`

- match: `explicit-or-semantic`
- flags: `--issues`
- aliases: `--issue`
- destinations: `Index.Issue.Operation.Module`
- loads: `references/issues.md`
- when: the caller wants to inspect, create, review, resolve, or retire Project Issue.Blocks
- then: select the grounded Issue.Block lifecycle without inferring review from folder placement

### `^route-index-check`

- match: `explicit-or-semantic`
- flags: `--check`
- aliases: `--lint`
- destinations: `Index.Check.Operation.Module`
- loads: `references/check.md`
- when: the caller wants deterministic diagnosis, linter findings, or post-edit validation
- then: select Index.Check.Operation.Module

### `^route-line-type`

- match: `explicit-or-semantic`
- flags: `--type`
- destinations: `Index.Line.Type.Knowledge.Module`
- loads: `references/type.md`
- when: the caller wants Line.Type classification understood or proposed
- then: load Index.Line.Type.Knowledge.Module

### `^route-anchor-link`

- match: `explicit-or-semantic`
- flags: `--link`
- destinations: `Anchory.Link.Operation.Module`
- loads: `references/link.md`
- when: the caller needs an Anchory.Anchor minted for chat context
- then: select Anchory.Link.Operation.Module

### `^route-implementation-namespace`

- match: `explicit-or-semantic`
- flags: `--impl`
- aliases: `--implementation`
- destinations: `Implementation.Workflow.Router.Module`
- loads: `references/impl.md`
- when: the caller supplies the Implementation namespace, a composed implementation call, or one of its declared shortcuts
- then: enter Implementation.Workflow.Router.Module and resolve exactly one implementation workflow from flags, input, conversation, or a declared default

### `^route-implementation-design`

- match: `explicit-or-semantic`
- flags: `--impl --design`
- aliases: `--impl-design`
- defaults: implementation input without an `Impl.Req`
- destinations: `Implementation.Design.Workflow.Module`
- loads: `references/impl/design.md`
- when: implementation work needs a What/How design or non-`Impl.Req` input must be shaped before execution
- then: select Implementation.Design.Workflow.Module

### `^route-implementation-review`

- match: `explicit-or-semantic`
- flags: `--impl --review`
- aliases: `--review`
- destinations: `Implementation.Review.Workflow.Module`
- loads: `references/impl/review.md`
- when: the caller wants an implementation reviewed
- then: select Implementation.Review.Workflow.Module

### `^route-implementation-execute`

- match: `explicit-or-semantic`
- flags: `--impl --execute`
- aliases: `--execute`, `--exec`
- defaults: `Impl.Req` input
- destinations: `Implementation.Execute.Workflow.Module`
- loads: `references/impl/execute.md`
- when: the caller wants an existing `Impl.Req` executed
- then: select Implementation.Execute.Workflow.Module

### `^route-implementation-develop`

- match: `explicit-or-semantic`
- flags: `--impl --develop`
- aliases: `--develop`, `--dev`
- destinations: `Implementation.Develop.Workflow.Module`
- loads: `references/impl/develop.md`
- when: the caller wants one end-to-end implementation run that may design and execute an `Impl.Req`
- then: select Implementation.Develop.Workflow.Module

### `^route-implementation-capture`

- match: `explicit-or-semantic`
- flags: `--impl --capture`
- aliases: `--impl-capture`
- destinations: `Implementation.Capture.Workflow.Module`
- loads: `references/impl/impl-capture.md`
- when: the caller wants implementation evidence captured
- then: select Implementation.Capture.Workflow.Module

### `^route-capture-read-only`

- match: `explicit-or-semantic`
- flags: `--capture --audit`
- destinations: `Hugentic.Capture.Workflow.Module`
- loads: `references/capture.md`
- when: the caller wants the capture map without entering proposal, approval, or landing work
- then: run Hugentic.Capture.Workflow.Module through its read-only roadmap and stop

### `^route-chat-status`

- match: `explicit-or-semantic`
- flags: `--status`
- aliases: `--chat-status`
- destinations: `Chat.Status.Operation.Module`
- loads: `references/chat-status.md`
- when: the caller wants to reconnect with the current chat and its todo state
- then: select Chat.Status.Operation.Module

### `^route-workflow-status`

- match: `explicit-or-semantic`
- flags: `--workflow-status`
- destinations: `Workflow.Status.Operation.Module`
- loads: `references/workflow-status.md`
- when: the caller wants a structured checkpoint against an active workflow
- then: select Workflow.Status.Operation.Module

### `^route-session-router`

- match: `explicit-or-semantic`
- flags: `--session-router`
- aliases: `--what-now`, `--what-next`
- destinations: `Hugentic.Session.Router.Operation.Module`
- loads: `references/session-router.md`
- when: the caller is unsure what workflow should handle the chat or routing guidance would reduce confusion
- then: select Hugentic.Session.Router.Operation.Module

### `^route-parking-note`

- match: `explicit-or-semantic`
- flags: `--park`
- aliases: `--parking-note`
- destinations: `Parking.Note.Operation.Module`
- loads: `references/parking-note.md`
- when: the caller wants to park a sidequest thought and return to the current session
- then: select Parking.Note.Operation.Module

### `^route-codebase-cleanup`

- match: `explicit-or-semantic`
- flags: `--clean`
- aliases: `--codebase-cleaner`, `--cleanup`
- destinations: `Codebase.Cleanup.Workflow.Module`, `Implementation.Workflow.Router.Module`
- loads: `references/codebase-cleaner.md`, `references/impl.md`
- when: the caller wants a codebase cleanup designed and executed through one gated handoff
- then: select Codebase.Cleanup.Workflow.Module and enter the Implementation namespace

### `^route-alignment-mode`

- match: `explicit`
- flags: `--AUTO`
- aliases: `--auto`, `--autonomous`
- destinations: `Skill.Arg::Alignment.Mode`
- then: bind Skill.Arg::Alignment.Mode to Alignment.Mode::Autonomous

### `^route-depot-arg`

- match: `explicit`
- flags: `--depot`
- destinations: `Skill.Arg::Depot`
- then: bind Skill.Arg::Depot and apply it to the selected Index operation

### `^route-chapter-arg`

- match: `explicit`
- flags: `--chapter`
- destinations: `Skill.Arg::Chapter`
- then: bind Skill.Arg::Chapter and apply it to the selected Index operation

### `^route-touched-data`

- match: `semantic`
- destinations: `Touched.Data.Knowledge.Module`
- loads: `references/touched-data.md`
- when: a consumer needs the authority, support-network, line-standing, or current-realization model behind Index operations
- then: load Touched.Data.Knowledge.Module

### `^route-decision-cycle`

- match: `semantic`
- destinations: `Touched.Decision.Knowledge.Module`
- loads: `references/decision-cycle.md`
- when: an operation makes a decision or changes a target product
- then: contextualize touched constraints, act through the open region, and reconcile changed surfaces

### `^route-index-context-assembly`

- match: `semantic`
- destinations: `Hugentic.Index.Context.Assembly.Module`
- loads: `references/index-context-assembly.md`
- when: developing any managed Hugentics Index surface
- then: load the complete Index context assembly before selecting direct dependencies, derivations, citations, or runtime-facing content

### `^route-capture-context-assembly`

- match: `semantic`
- destinations: `Hugentic.Capture.Context.Assembly.Module`
- loads: `references/index-capture-context.md`
- when: a capture run needs its complete preparation context
- then: load Hugentic.Capture.Context.Assembly.Module

### `^route-alignment-session`

- match: `semantic`
- destinations: `Alignment.Session.Knowledge.Module`
- loads: `references/alignment-session.md`
- when: the caller needs the shared alignment frame or checkpoint vocabulary
- then: load the applicable workflow and knowledge modules with Alignment.Session.Knowledge.Module

### `^route-implementation-execution-knowledge`

- match: `semantic`
- destinations: `Implementation.Execution.Practices.Knowledge.Module`, `Implementation.Execution.Preferences.Knowledge.Module`
- loads: `references/impl/general-practices.md`, `references/impl/general-preferences.md`
- when: an implementation execution workflow needs shared practices and preferences
- then: load the shared implementation execution knowledge modules

### `^route-package-knowledge`

- match: `semantic`
- destinations: `Agentos.Package.Knowledge.Module`
- when: the caller needs package-level understanding of the Index subsystem
- then: load the relevant tarav-pkg design, appendix, or reference surface

### `^route-index-block-examples`

- match: `semantic`
- destinations: `Index.Block.Example.Knowledge.Module`
- when: the caller needs concrete examples of good and bad block shape
- then: load tarav-pkg/references/index-block-catalog.md

### `^route-index-testground`

- match: `semantic`
- destinations: `Agentos.Testground.Package.Skill`
- when: the caller needs behavioral testing of Index entry paths, selection behavior, or usage patterns
- then: load tarav-testground

## Index Operating Behavior

An agent operating the index should:

- apply `Touched.Decision.Cycle` to material decisions: contextualize, surface incoherence as POIs, act through the remaining open region, and reconcile changed products
- search routing surfaces in the engaged `Index.Depot`s first, then load only relevant concept blocks, appendix material, or references
- distinguish grounded live lines, ungrounded live lines, and demoted history; apply `Touched.Authority`, `Index.Presumption`, or no current decision weight accordingly
- read down the `User.Attention` gradient — reviewed live blocks and appendix first, then unreviewed grounded leads and finally original authority surfaces
- respect `--depot` as an `Index.Depot` scope; otherwise use task-relevant engaged depots
- respect `--chapter` as an `Index.Chapter` scope inside engaged depots; default chapter is `design`
- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- treat the prompt as a focus argument and compare the current visible discussion against the index whenever there is discussion state to ground
- make a `Capture.Offer` when work surfaces new aligned content: propose typed line content and its landing operation at the moment, with destination options (index main, appendix, agendix, decline) — never self-write on a gated surface
- use `--capture` when the user wants the chat's content worked through the shared loop; its durable target remains unresolved until conversation or a compatible route supplies it, while `--index` and `--main` select the reviewed main Index target, `--design` selects `Design.Req`, and `--agendix` selects `Index.Agendix`
- resolve `::approve` / `::approved` to `User.Command::Approve`, but in index workflows mint, render, and require the proposal's explicit token; if the user gives a bare approval, leave the verbatim gate unresolved and reprint the exact tokenized command; resolve `::land` / `::write` to targeted `User.Command::Land`, and `::land-all-approved` to zero-argument `User.Command::LandAllApproved`; `--write` remains a skill argument while `::write` is an in-workflow transition
- during interactive capture, add approved drafts to the approved cluster and continue reviewing the roadmap; do not make immediate landing the default next move
- when a landing contains several lines, batch their anchor preview and registration and apply the returned line-to-anchor mapping in one surface patch; do not shell-loop the single-line path
- keep command targets foregrounded; targeted commands fail closed on ambiguous targets, and `::land-all-approved` fails closed unless one foreground index workflow owns the cluster
- use file mutation only when the applicable surface gate is satisfied
- keep action separate from index reconciliation: open inference may advance other work without silently rewriting touched positions
- run a linter check after applying an approved index or appendix edit

For delegated read-only research that protects the caller's context, use `Packages.Master.Agent` against the relevant package or packages.

## Hugentic System Model

`Hugentic.Capture.Workflow.Module` owns the shared public alignment loop. `Design.Req.Knowledge.Module`, `Index.Landing.Knowledge.Module`, and `Index.Agendix.Knowledge.Module` configure durable targets without becoming parallel workflow identities.

The Implementation namespace contains explicit design, review, execute, develop, and capture workflow modules. The namespace, its aliases, and its input-sensitive defaults are routing behavior; they do not create duplicate modules.

Any active workflow may be interrupted for capture, optionally configured as a read-only audit, consolidation, `Design.Req.Promotion`, implementation handoff, parking, splitting, or status work. Completion reconciles and maintains changed artifact state before continuation; it never restores a stale prior state.

## When To Load This Skill

- when a session needs index-grounded context or a custom index research pass
- when the user wants to control, inspect, interrupt, or resume a Hugentic session
- when the user is unsure what to do next and needs ranked workflow routes
- when designing or realizing a target product
- when editing, diagnosing, testing, or maintaining the index
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
