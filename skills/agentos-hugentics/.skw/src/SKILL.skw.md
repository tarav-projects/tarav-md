---
name: agentos-hugentics
description: "Canonical public control surface for Hugentic sessions. USE WHEN you need session routing, touched-data contextualization, product design, implementation design or execution, capture, reconciliation, parking, status, index research, editing, diagnosis, testing, or maintenance."
---

# Agentos Hugentics

> $kw: --from Agentos.Index.System --from Alignment.Surface --from Batchy.Router --from Batchy.Skill --from Batchy.Skill.Help --from Capture.Offer --from Demoted.Index.Line --from Design.Req --from Design.Req.Promotion --from Edition.Approval.Token --from Gr.Req --from Hugentic.Capture.Workflow --from Impl.Req --from Index.Agendix --from Index.Appendix --from Index.Chapter --from Index.Depot --from Index.Line --from Index.Ontology --from Index.Presumption --from Index.Skillware --from Line.Type --from Line.Verbatim.Gate --from Live.Index.Line --from Open.Inference --from Package.Driver --from Packages.Master.Agent --from POI.Instance --from Reviewed.Content --from Routing.Table --from Skill.Arg --from Support.Set --from Touch.Authority.Surface --from Touched.Authority --from Touched.Data --from Touched.Decision.Cycle --from Touched.Index --from Touched.Support.Network --from User.Attention --from User.Command --from User.Command.Arg --from User.Command.Section --from User.Command.Trigger
> --dev-from references/index-context-assembly.skw.md
> $kw: ^driver-critical-context --dev-from Cited.Duplication --dev-from Context.Loading.Path --dev-from Package.Driver.Base --dev-from SKILL.Loading
> --supp root driver context is selected by the alignment failure its absence could cause, not by minimizing line count; preserve context whose omission could make the agent misunderstand authority, violate a gate, select the wrong workflow, or lose the session model ^c20260729-48u

Canonical `Package.Driver` and single public session-control surface for the Agentos Hugentic system.

`Touched.Index` is the global system for contextualizing relevant `Touched.Data`. The Markdown `Agentos.Index.System`, trailing Anchory anchors, and Chatlas support records are its current realization, not its conceptual boundary.

Index capabilities remain a distinct internal subsystem because nearly every Hugentic workflow depends on touched-data contextualization. The caller nevertheless controls the whole session here: product design, implementation design and execution, capture, audit, status, parking, and every Index operation route through named modules without requiring another public skill.

This is a `Batchy.Skill`; `Batchy.Router` resolves every run from explicit flags, the live conversation, and declared defaults.

`Hugentic.Capture.Workflow` is the shared public alignment loop. A `Design.Req.Promotion` temporarily retargets that loop without creating another router or workflow identity.

- `-h` / `--help` explicitly routes to `Batchy.Skill.Help` and short-circuits the run.
- a written `--<flag>` is intentional run configuration and must be resolved as such.
- without an explicit route, conversational discovery remains available wherever the applicable row permits it.
- declared `User.Command`s are the only way to cross their explicit workflow gates.
- when an index workflow pauses, print only the commands available at that checkpoint.

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
- examples: --depot agentos-pkg, --depot agentos-chatlas-pkg

### Skill.Arg::Chapter
- the `Index.Chapter` selected within the engaged depots
- required: false
- default: design
- flags: --chapter
- examples: --chapter design, --chapter impl

## Batchy.Router

The public flags below call the single running `Batchy.Router`. A trailing value binds `Skill.Arg::Main.Prompt` for the selected module; data-only flags bind their named `Skill.Arg` without selecting a module. This call surface is compiled from the canonical `Routing.Table` below.

> $kw: ^public-call-surface --routing-view calls --table ^package-driver-router

## Skill.Module Catalog

Canonical module identity is explicit and independent from invocation spelling. `Batchy.Router` rows may use aliases, composed flags, conversational discovery, or defaults to select one canonical module; those routes do not create additional modules. This catalog is compiled from the same canonical table as the public call surface.

> $kw: ^skill-module-catalog --routing-view modules --table ^package-driver-router

Supporting examples such as `references/impl/example.md` are reference assets, not runnable modules.

## User.Command.Section

This `User.Command.Section` declares the canonical commands below. Each accepted `User.Command.Trigger` resolves to one command, whose nested `User.Command.Arg` blocks govern target resolution.

### User.Command::Approve
- accept an approval-ready index draft in its current form without writing it
- triggers: `::approve`, `::approved`
- available: when `--capture`, direct `--edit`, a `Capture.Offer`, or an `--enrich` capture offer has one or more approval-ready drafts
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

> $kw: ^driver-index-literacy --derived
> --from references/touched-data.skw.md#Authority Flow
> --from references/touched-data.skw.md#Support Network
> --from references/touched-data.skw.md#Line Standing
> --from references/touched-data.skw.md#Coherence And Decision Weight
> --from references/touched-data.skw.md#Current Realization
> --intent project the authority model, line standing, and current realization
> --cont into always-loaded driver literacy; retain the distinctions whose
> --cont absence could make an agent misread authority or reason from stale data

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
- agents operate it by loading routers, concept blocks, appendix material, and references relevant to the current task

> $kw. end

## Routing.Table

This addressed `Routing.Table` is the package driver's single declarative dispatch artifact. Explicit flags select applicable rows directly; conversation and defaults may select rows whose policy permits automatic discovery. Rows compose because the table's selection cardinality is `many`.

> $kw: --dev-from Package.Driver.Router
> $kw: ^package-driver-router --routing-table --select many

> $kw: ^route-index-namespace --router-row --table ^package-driver-router
> --flag --index
> --match explicit
> --to Index.Namespace
> --then contribute the Index namespace/context; with capture and no narrower target, select the reviewed main Index surfaces

> $kw: ^route-index-main --router-row --table ^package-driver-router
> --flag --main
> --match explicit
> --to Index.Main.Target
> --then select the reviewed main Index target; with capture, this is operationally equivalent to --index

> $kw: ^route-index-search --router-row --table ^package-driver-router
> --flag --search
> --alias --research
> --alias --ground
> --match explicit-or-semantic
> --default Index namespace when omitted
> --to Index.Search.Operation.Module
> --load references/search.md
> --when the caller wants to find concepts, retrieve cited index context, inspect related blocks, discover appendix depth, or ground the visible discussion
> --then select Index.Search.Operation.Module; --search, --research, and --ground are operationally equivalent

> $kw: ^route-capture --router-row --table ^package-driver-router
> --flag --capture
> --match explicit-or-semantic
> --to Hugentic.Capture.Workflow.Module
> --load references/capture.md
> --when the caller wants chat material aligned into a durable target
> --then select the shared capture loop and leave its durable target unresolved until another route or conversation supplies it

> $kw: ^route-agendix --router-row --table ^package-driver-router
> --flag --agendix
> --match explicit
> --default Alignment.Mode::Autonomous
> --to Hugentic.Capture.Workflow.Module
> --to Index.Agendix.Knowledge.Module
> --load references/capture.md
> --load references/agendix.md
> --then apply the --index --capture --agendix shorthand and use the autonomous alignment default

> $kw: ^route-product-design --router-row --table ^package-driver-router
> --flag --design
> --match explicit-or-semantic
> --to Hugentic.Capture.Workflow.Module
> --to Design.Req.Knowledge.Module
> --load references/capture.md
> --load references/design-req.md
> --when the caller wants product design or organic design work begins outside the Implementation namespace
> --then select the shared capture loop with Design.Req target knowledge

> $kw: ^index-write-entry --router-row --table ^package-driver-router
> --flag --edit
> --alias --write
> --alias --append
> --match explicit-or-semantic
> --to Index.Landing.Knowledge.Module
> --load references/edit.md
> --when an index or appendix surface is being written or an approved edit needs landing
> --then route through the gated Index landing contract; trailing input binds Main.Prompt and --depot/--chapter bind scope

> $kw: ^route-reconcile --router-row --table ^package-driver-router
> --flag --reconcile
> --match explicit-or-semantic
> --to Touched.Decision.Knowledge.Module
> --to Index.Landing.Knowledge.Module
> --load references/decision-cycle.md
> --load references/edit.md
> --when a changed product or implementation must be compared with touched design
> --then contextualize the decision and load the landing contract when a write is selected

> $kw: ^route-index-check --router-row --table ^package-driver-router
> --flag --check
> --alias --lint
> --match explicit-or-semantic
> --to Index.Check.Operation.Module
> --load references/check.md
> --when the caller wants deterministic diagnosis, linter findings, or post-edit validation
> --then select Index.Check.Operation.Module

> $kw: ^route-line-type --router-row --table ^package-driver-router
> --flag --type
> --match explicit-or-semantic
> --to Index.Line.Type.Knowledge.Module
> --load references/type.md
> --when the caller wants Line.Type classification understood or proposed
> --then load Index.Line.Type.Knowledge.Module

> $kw: ^route-anchor-link --router-row --table ^package-driver-router
> --flag --link
> --match explicit-or-semantic
> --to Anchory.Link.Operation.Module
> --load references/link.md
> --when the caller needs an Anchory.Anchor minted for chat context
> --then select Anchory.Link.Operation.Module

> $kw: ^route-anchor-back-link --router-row --table ^package-driver-router
> --flag --back-link
> --match explicit-or-semantic
> --to Anchory.Back.Link.Operation.Module
> --load references/back-link.md
> --when the caller wants an existing block grounded backward
> --then select Anchory.Back.Link.Operation.Module

> $kw: ^route-grounding-survey --router-row --table ^package-driver-router
> --flag --gr-survey
> --alias --gr-scout
> --alias --gr-scan
> --alias --gr-linker
> --match explicit-or-semantic
> --to Grounding.Survey.Workflow.Module
> --load references/gr-survey.md
> --when the caller wants a grounding campaign surveyed
> --then select Grounding.Survey.Workflow.Module

> $kw: ^route-grounding-review --router-row --table ^package-driver-router
> --flag --gr-review
> --match explicit-or-semantic
> --to Grounding.Review.Workflow.Module
> --load references/gr-review.md
> --when the caller wants a `Gr.Req` reviewed
> --then select Grounding.Review.Workflow.Module

> $kw: ^route-index-enrichment --router-row --table ^package-driver-router
> --flag --enrich
> --match explicit-or-semantic
> --to Index.Enrichment.Workflow.Module
> --load references/enrich.md
> --when the caller wants a block enriched
> --then select Index.Enrichment.Workflow.Module

> $kw: ^route-implementation-namespace --router-row --table ^package-driver-router
> --flag --impl
> --alias --implementation
> --match explicit-or-semantic
> --to Implementation.Workflow.Router.Module
> --load references/impl.md
> --when the caller supplies the Implementation namespace, a composed implementation call, or one of its declared shortcuts
> --then enter Implementation.Workflow.Router.Module and resolve exactly one implementation workflow from flags, input, conversation, or a declared default

> $kw: ^route-implementation-design --router-row --table ^package-driver-router
> --flag --impl --design
> --alias --impl-design
> --match explicit-or-semantic
> --default implementation input without an `Impl.Req`
> --to Implementation.Design.Workflow.Module
> --load references/impl/design.md
> --when implementation work needs a What/How design or non-`Impl.Req` input must be shaped before execution
> --then select Implementation.Design.Workflow.Module

> $kw: ^route-implementation-review --router-row --table ^package-driver-router
> --flag --impl --review
> --alias --review
> --match explicit-or-semantic
> --to Implementation.Review.Workflow.Module
> --load references/impl/review.md
> --when the caller wants an implementation reviewed
> --then select Implementation.Review.Workflow.Module

> $kw: ^route-implementation-execute --router-row --table ^package-driver-router
> --flag --impl --execute
> --alias --execute
> --alias --exec
> --match explicit-or-semantic
> --default `Impl.Req` input
> --to Implementation.Execute.Workflow.Module
> --load references/impl/execute.md
> --when the caller wants an existing `Impl.Req` executed
> --then select Implementation.Execute.Workflow.Module

> $kw: ^route-implementation-develop --router-row --table ^package-driver-router
> --flag --impl --develop
> --alias --develop
> --alias --dev
> --match explicit-or-semantic
> --to Implementation.Develop.Workflow.Module
> --load references/impl/develop.md
> --when the caller wants one end-to-end implementation run that may design and execute an `Impl.Req`
> --then select Implementation.Develop.Workflow.Module

> $kw: ^route-implementation-capture --router-row --table ^package-driver-router
> --flag --impl --capture
> --alias --impl-capture
> --match explicit-or-semantic
> --to Implementation.Capture.Workflow.Module
> --load references/impl/impl-capture.md
> --when the caller wants implementation evidence captured
> --then select Implementation.Capture.Workflow.Module

> $kw: ^route-capture-audit --router-row --table ^package-driver-router
> --flag --capture-audit
> --match explicit-or-semantic
> --to Capture.Audit.Operation.Module
> --load references/capture-audit.md
> --when the caller asks whether significant session material remains uncaptured
> --then select Capture.Audit.Operation.Module

> $kw: ^route-chat-status --router-row --table ^package-driver-router
> --flag --status
> --alias --chat-status
> --match explicit-or-semantic
> --to Chat.Status.Operation.Module
> --load references/chat-status.md
> --when the caller wants to reconnect with the current chat and its todo state
> --then select Chat.Status.Operation.Module

> $kw: ^route-workflow-status --router-row --table ^package-driver-router
> --flag --workflow-status
> --match explicit-or-semantic
> --to Workflow.Status.Operation.Module
> --load references/workflow-status.md
> --when the caller wants a structured checkpoint against an active workflow
> --then select Workflow.Status.Operation.Module

> $kw: ^route-session-router --router-row --table ^package-driver-router
> --flag --session-router
> --alias --what-now
> --alias --what-next
> --match explicit-or-semantic
> --to Hugentic.Session.Router.Operation.Module
> --load references/session-router.md
> --when the caller is unsure what workflow should handle the chat or routing guidance would reduce confusion
> --then select Hugentic.Session.Router.Operation.Module

> $kw: ^route-parking-note --router-row --table ^package-driver-router
> --flag --park
> --alias --parking-note
> --match explicit-or-semantic
> --to Parking.Note.Operation.Module
> --load references/parking-note.md
> --when the caller wants to park a sidequest thought and return to the current session
> --then select Parking.Note.Operation.Module

> $kw: ^route-codebase-cleanup --router-row --table ^package-driver-router
> --flag --clean
> --alias --codebase-cleaner
> --alias --cleanup
> --match explicit-or-semantic
> --to Codebase.Cleanup.Workflow.Module
> --to Implementation.Workflow.Router.Module
> --load references/codebase-cleaner.md
> --load references/impl.md
> --when the caller wants a codebase cleanup designed and executed through one gated handoff
> --then select Codebase.Cleanup.Workflow.Module and enter the Implementation namespace

> $kw: ^route-alignment-mode --router-row --table ^package-driver-router
> --flag --AUTO
> --alias --auto
> --alias --autonomous
> --match explicit
> --to Skill.Arg::Alignment.Mode
> --then bind Skill.Arg::Alignment.Mode to Alignment.Mode::Autonomous

> $kw: ^route-depot-arg --router-row --table ^package-driver-router
> --flag --depot
> --match explicit
> --to Skill.Arg::Depot
> --then bind Skill.Arg::Depot and apply it to the selected Index operation

> $kw: ^route-chapter-arg --router-row --table ^package-driver-router
> --flag --chapter
> --match explicit
> --to Skill.Arg::Chapter
> --then bind Skill.Arg::Chapter and apply it to the selected Index operation

> $kw: ^route-touched-data --router-row --table ^package-driver-router
> --match semantic
> --to Touched.Data.Knowledge.Module
> --load references/touched-data.md
> --when a consumer needs the authority, support-network, line-standing, or current-realization model behind Index operations
> --then load Touched.Data.Knowledge.Module

> $kw: ^route-decision-cycle --router-row --table ^package-driver-router
> --match semantic
> --to Touched.Decision.Knowledge.Module
> --load references/decision-cycle.md
> --when an operation makes a decision or changes a target product
> --then contextualize touched constraints, act through the open region, and reconcile changed surfaces

> $kw: ^route-index-context-assembly --router-row --table ^package-driver-router
> --match semantic
> --to Hugentic.Index.Context.Assembly.Module
> --load references/index-context-assembly.md
> --when developing any managed Hugentics Index surface
> --then load the complete Index context assembly before selecting direct dependencies, derivations, citations, or runtime-facing content

> $kw: ^route-capture-context-assembly --router-row --table ^package-driver-router
> --match semantic
> --to Hugentic.Capture.Context.Assembly.Module
> --load references/index-capture-context.md
> --when a capture run needs its complete preparation context
> --then load Hugentic.Capture.Context.Assembly.Module

> $kw: ^route-alignment-session --router-row --table ^package-driver-router
> --match semantic
> --to Alignment.Session.Knowledge.Module
> --load references/alignment-session.md
> --when the caller needs the shared alignment frame or checkpoint vocabulary
> --then load the applicable workflow and knowledge modules with Alignment.Session.Knowledge.Module

> $kw: ^route-implementation-execution-knowledge --router-row --table ^package-driver-router
> --match semantic
> --to Implementation.Execution.Practices.Knowledge.Module
> --to Implementation.Execution.Preferences.Knowledge.Module
> --load references/impl/general-practices.md
> --load references/impl/general-preferences.md
> --when an implementation execution workflow needs shared practices and preferences
> --then load the shared implementation execution knowledge modules

> $kw: ^route-package-knowledge --router-row --table ^package-driver-router
> --match semantic
> --to Agentos.Package.Knowledge.Module
> --when the caller needs package-level understanding of the Index subsystem
> --then load the relevant agentos-pkg design, appendix, or reference surface

> $kw: ^route-index-block-examples --router-row --table ^package-driver-router
> --match semantic
> --to Index.Block.Example.Knowledge.Module
> --when the caller needs concrete examples of good and bad block shape
> --then load agentos-pkg/references/index-block-catalog.md

> $kw: ^route-index-testground --router-row --table ^package-driver-router
> --match semantic
> --to Agentos.Testground.Package.Skill
> --when the caller needs behavioral testing of Index entry paths, selection behavior, or usage patterns
> --then load agentos-testground

> $kw: ^full-routing-table --routing-view full --table ^package-driver-router

## Index Operating Behavior

> $kw: --derived
> --from references/touched-data.skw.md#Line Standing
> --from references/touched-data.skw.md#Coherence And Decision Weight
> --from references/decision-cycle.skw.md#Contextualize
> --from references/decision-cycle.skw.md#Act
> --from references/decision-cycle.skw.md#Reconcile
> --from references/search.skw.md#Search Model
> --from references/search.skw.md#Citation Behavior
> --from references/capture.skw.md#User.Command Checkpoints
> --from references/capture.skw.md#Landing
> --from references/edit.skw.md#Edit Gates
> --from references/edit.skw.md#User.Command Transitions
> --intent assemble the risk-critical operating contract that must already be
> --cont present when the driver loads: authority-aware reasoning, routing-first
> --cont search, explicit gates, unambiguous commands, and separate reconciliation

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
- keep command targets foregrounded; targeted commands fail closed on ambiguous targets, and `::land-all-approved` fails closed unless one foreground index workflow owns the cluster
- use file mutation only when the applicable surface gate is satisfied
- keep action separate from index reconciliation: open inference may advance other work without silently rewriting touched positions
- run a linter check after applying an approved index or appendix edit

For delegated read-only research that protects the caller's context, use `Packages.Master.Agent` against the relevant package or packages.

> $kw. end

## Hugentic System Model

`Hugentic.Capture.Workflow.Module` owns the shared public alignment loop. `Design.Req.Knowledge.Module`, `Index.Landing.Knowledge.Module`, and `Index.Agendix.Knowledge.Module` configure durable targets without becoming parallel workflow identities.

The Implementation namespace contains explicit design, review, execute, develop, and capture workflow modules. The namespace, its aliases, and its input-sensitive defaults are routing behavior; they do not create duplicate modules.

Any active workflow may be interrupted for capture, audit, consolidation, `Design.Req.Promotion`, implementation handoff, parking, splitting, or status work. Completion reconciles and maintains changed artifact state before continuation; it never restores a stale prior state.

## When To Load This Skill

- when a session needs index-grounded context or a custom index research pass
- when the user wants to control, inspect, interrupt, or resume a Hugentic session
- when the user is unsure what to do next and needs ranked workflow routes
- when designing or realizing a target product
- when editing, diagnosing, testing, or maintaining the index
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
