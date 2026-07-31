---
name: agentos-hugentics
description: "Canonical public control surface for Hugentic sessions. USE WHEN you need session routing, touched-data contextualization, product design, implementation design or execution, capture, reconciliation, parking, status, index research, editing, diagnosis, testing, or maintenance."
---

# Agentos Hugentics

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

The public flags below call the single running `Batchy.Router`. A trailing value binds `Skill.Arg::Main.Prompt` for the selected module; data-only flags bind their named `Skill.Arg` without selecting a module.

| Explicit configuration | Routed effect |
|---|---|
| `--index` | contribute the Index namespace/context; with capture and no narrower target, select the reviewed main Index surfaces |
| `--main` | select the reviewed main Index target for the applicable Index workflow; with capture, equivalent to `--index` |
| `--search`, `--research`, `--ground` | select `Index.Search.Operation.Module`; omitting `--index` uses its declared namespace default |
| `--capture` | select `Hugentic.Capture.Workflow.Module`; leave the durable target unresolved until another route or conversation supplies it |
| `--agendix` | shorthand for `--index --capture --agendix`; add `Index.Agendix.Knowledge.Module` and the autonomous default |
| `--design` | select `Hugentic.Capture.Workflow.Module` with `Design.Req.Knowledge.Module` as target knowledge |
| `--edit`, `--write`, `--append` | route directly through `Index.Landing.Knowledge.Module` |
| `--reconcile` | compose `Touched.Decision.Knowledge.Module` with `Index.Landing.Knowledge.Module` when a write is selected |
| `--check`, `--lint` | select `Index.Check.Operation.Module` |
| `--type` | select `Index.Line.Type.Knowledge.Module` |
| `--link` | select `Anchory.Link.Operation.Module` |
| `--back-link` | select `Anchory.Back.Link.Operation.Module` |
| `--gr-survey`, `--gr-scout`, `--gr-scan`, `--gr-linker` | select `Grounding.Survey.Workflow.Module` |
| `--gr-review` | select `Grounding.Review.Workflow.Module` |
| `--enrich` | select `Index.Enrichment.Workflow.Module` |
| `--implementation`, `--impl` | contribute the Implementation namespace; its router resolves a workflow from a composed flag, input, conversation, or default |
| `--impl --design` | select `Implementation.Design.Workflow.Module`; shortcut: `--impl-design` |
| `--impl --review` | select `Implementation.Review.Workflow.Module`; shortcut: `--review` |
| `--impl --execute` | select `Implementation.Execute.Workflow.Module`; shortcuts: `--execute`, `--exec` |
| `--impl --develop` | select `Implementation.Develop.Workflow.Module`; shortcuts: `--develop`, `--dev` |
| `--impl --capture` | select `Implementation.Capture.Workflow.Module`; shortcut: `--impl-capture` |
| `--capture-audit` | select `Capture.Audit.Operation.Module` |
| `--status`, `--chat-status` | select `Chat.Status.Operation.Module` |
| `--workflow-status` | select `Workflow.Status.Operation.Module` |
| `--session-router`, `--what-now`, `--what-next` | select `Hugentic.Session.Router.Operation.Module` |
| `--park`, `--parking-note` | select `Parking.Note.Operation.Module` |
| `--clean`, `--codebase-cleaner`, `--cleanup` | select `Codebase.Cleanup.Workflow.Module`, then enter the Implementation namespace |
| `--AUTO`, `--auto`, `--autonomous` | bind `Skill.Arg::Alignment.Mode` |
| `--depot` | bind `Skill.Arg::Depot` |
| `--chapter` | bind `Skill.Arg::Chapter` |

## Skill.Module Catalog

Canonical module identity is explicit and independent from invocation spelling. `Batchy.Router` rows may use aliases, composed flags, conversational discovery, or defaults to select one canonical module; those routes do not create additional modules.

### Router Modules

| Canonical module | Managed source | Role |
|---|---|---|
| `Agentos.Hugentics.Package.Driver.Router` | `SKILL.md` | public router for the complete Hugentics call surface |
| `Implementation.Workflow.Router.Module` | `references/impl.md` | internal router entered through the `--impl` namespace |

### Workflow Modules

| Canonical module | Managed source | Routing |
|---|---|---|
| `Hugentic.Capture.Workflow.Module` | `references/capture.md` | `--capture`; also selected by target shortcuts such as `--design` and `--agendix` |
| `Grounding.Survey.Workflow.Module` | `references/gr-survey.md` | `--gr-survey` and its declared aliases |
| `Grounding.Review.Workflow.Module` | `references/gr-review.md` | `--gr-review` |
| `Index.Enrichment.Workflow.Module` | `references/enrich.md` | `--enrich` |
| `Implementation.Design.Workflow.Module` | `references/impl/design.md` | `--impl --design`; shortcut `--impl-design`; implementation default for non-`Impl.Req` input |
| `Implementation.Review.Workflow.Module` | `references/impl/review.md` | `--impl --review`; shortcut `--review` |
| `Implementation.Execute.Workflow.Module` | `references/impl/execute.md` | `--impl --execute`; shortcuts `--execute`, `--exec`; implementation default for `Impl.Req` input |
| `Implementation.Develop.Workflow.Module` | `references/impl/develop.md` | `--impl --develop`; shortcuts `--develop`, `--dev` |
| `Implementation.Capture.Workflow.Module` | `references/impl/impl-capture.md` | `--impl --capture`; shortcut `--impl-capture` |
| `Codebase.Cleanup.Workflow.Module` | `references/codebase-cleaner.md` | `--clean`, `--codebase-cleaner`, `--cleanup` |

### Knowledge Modules

| Canonical module | Managed source | Consumer |
|---|---|---|
| `Design.Req.Knowledge.Module` | `references/design-req.md` | capture runs targeting `Design.Req` |
| `Index.Landing.Knowledge.Module` | `references/edit.md` | any ontology or appendix write |
| `Index.Agendix.Knowledge.Module` | `references/agendix.md` | any agendix landing |
| `Touched.Data.Knowledge.Module` | `references/touched-data.md` | index-grounded reasoning |
| `Touched.Decision.Knowledge.Module` | `references/decision-cycle.md` | decisions and reconciliation |
| `Alignment.Session.Knowledge.Module` | `references/alignment-session.md` | workflows with declared alignment checkpoints |
| `Index.Line.Type.Knowledge.Module` | `references/type.md` | line classification and typing proposals |
| `Implementation.Execution.Practices.Knowledge.Module` | `references/impl/general-practices.md` | implementation execution workflows |
| `Implementation.Execution.Preferences.Knowledge.Module` | `references/impl/general-preferences.md` | implementation execution workflows |

### Operation Modules

| Canonical module | Managed source |
|---|---|
| `Index.Search.Operation.Module` | `references/search.md` |
| `Index.Check.Operation.Module` | `references/check.md` |
| `Anchory.Link.Operation.Module` | `references/link.md` |
| `Anchory.Back.Link.Operation.Module` | `references/back-link.md` |
| `Capture.Audit.Operation.Module` | `references/capture-audit.md` |
| `Chat.Status.Operation.Module` | `references/chat-status.md` |
| `Workflow.Status.Operation.Module` | `references/workflow-status.md` |
| `Hugentic.Session.Router.Operation.Module` | `references/session-router.md` |
| `Parking.Note.Operation.Module` | `references/parking-note.md` |

### Context Assembly Modules

| Canonical module | Managed source | Availability |
|---|---|---|
| `Hugentic.Index.Context.Assembly.Module` | `references/index-context-assembly.md` | build-time development context; not a public route |
| `Hugentic.Capture.Context.Assembly.Module` | `references/index-capture-context.md` | capture preparation context; not an independent public route |

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

## Routing.Table

This `Routing.Table` is the package driver's declarative dispatch artifact. Explicit flags select applicable rows directly; conversation and defaults may select rows whose policy permits automatic discovery.

- `--edit`, `--write`, and `--append` explicitly select the gated index or appendix edit route
- their trailing value binds `Skill.Arg::Main.Prompt`; `--depot` and `--chapter` contribute the applicable index scope
- load `references/edit.md` and do not mutate a gated surface until its declared approval and landing transitions resolve

When a consumer needs the general authority, support-network, line-standing, and current-realization model behind every index operation.

Load `references/touched-data.md`.

When an operation makes a decision or changes a target product.

Load `references/decision-cycle.md` to contextualize touched constraints, act through the remaining open region, and reconcile changed surfaces.

When the caller wants to find concepts, retrieve cited index context, inspect related blocks, discover appendix depth, or ground the visible discussion; `--search`, `--research`, `--ground`, and their `--index`-prefixed forms are operationally equivalent and select this route.

Load `references/search.md`.

When the caller wants product design or organic design work begins; outside the Implementation namespace, `--design` explicitly selects a `Design.Req` target for the shared capture workflow.

Load `references/capture.md` and `references/design-req.md`.

When the caller writes `--index` to contribute Index namespace/context to a run; a compatible flag or the conversation supplies the operation focus.

Apply the Index namespace/context to the selected focus. With capture and no narrower target, resolve the reviewed main Index surfaces; when no operation focus resolves, leave it unresolved and continue permitted conversational discovery.

When the caller writes `--main` with an applicable Index workflow.

Select the reviewed main Index target. With capture, this is operationally equivalent to `--index` and constrains landing to `Index.Ontology` or `Index.Appendix`.

When developing any managed Hugentics Index surface.

Load the complete `references/index-context-assembly.md` before selecting direct dependencies, derivations, citations, or runtime-facing content.

When the user wants the chat's content captured; outside the Implementation namespace, `--capture` selects the shared loop without resolving its durable target, while `--index` or `--main` selects the reviewed main Index target and `--agendix` selects its autonomous agendix preset.

Load `references/capture.md`.

When a capture run needs its complete preparation context.

Load `references/index-capture-context.md`.

When an index or appendix surface is being written or an approved edit needs landing; `--edit`, `--write`, and `--append` explicitly select this route.

Load `references/edit.md`.

When a changed product or implementation must be compared with touched design; `--reconcile` explicitly selects this route.

Load `references/decision-cycle.md`, then `references/edit.md` when a write is selected.

When the caller wants deterministic diagnosis, linter findings, or post-edit validation; `--check` and `--lint` explicitly select this route.

Load `references/check.md`.

When the caller wants `Line.Type` classification understood, read, or proposed; `--type` explicitly selects this route.

Load `references/type.md`.

When material lands on the agendix or the caller needs the agendix surface understood.

Load `references/agendix.md`.

When a caller needs an `Anchory.Anchor` minted for chat context; `--link` explicitly selects this route.

Load `references/link.md`.

When the caller wants an existing block grounded backward; `--back-link` explicitly selects this route.

Load `references/back-link.md`.

When the caller wants a grounding campaign surveyed; `--gr-survey`, `--gr-scout`, `--gr-scan`, and `--gr-linker` explicitly select this route.

Load `references/gr-survey.md`.

When the caller wants a `Gr.Req` reviewed; `--gr-review` explicitly selects this route.

Load `references/gr-review.md`.

When the caller wants a block enriched; `--enrich` explicitly selects this route.

Load `references/enrich.md`.

When the caller supplies the `--impl` or `--implementation` namespace, a composed implementation call, or one of its declared shortcuts. Inside that namespace, `--design` and `--capture` select `Implementation.Design.Workflow.Module` and `Implementation.Capture.Workflow.Module`; they do not select the root Design.Req target or shared capture route.

Load `references/impl.md`, then resolve exactly one canonical implementation workflow module from the namespaced flag, shortcut, input, conversation, or declared default.

When the caller asks whether significant session material remains uncaptured; `--capture-audit` explicitly selects this route.

Load `references/capture-audit.md`.

When the caller wants to reconnect with the current chat and its todo state; `--status` and `--chat-status` explicitly select this route.

Load `references/chat-status.md`.

When the caller wants a structured checkpoint against an active workflow; `--workflow-status` explicitly selects this route.

Load `references/workflow-status.md`.

When the caller is unsure what workflow should handle the chat, or routing guidance would reduce confusion; `--session-router`, `--what-now`, and `--what-next` explicitly select this route.

Load `references/session-router.md`.

When the caller wants to park a sidequest thought and return to the current session; `--park` and `--parking-note` explicitly select this route.

Load `references/parking-note.md`.

When the caller wants a codebase cleanup designed and executed through one gated handoff; `--clean`, `--codebase-cleaner`, and `--cleanup` explicitly select this route.

Load `references/codebase-cleaner.md`, then `references/impl/`.

When the caller needs the shared alignment frame or checkpoint vocabulary.

Load `references/alignment-session.md`; also load the applicable workflow and knowledge modules rather than a separate harness model.

When the caller supplies `--depot` or `--chapter`.

Bind `Skill.Arg::Depot` or `Skill.Arg::Chapter` and apply the resolved scope to the selected index operation.

When the caller needs package-level understanding of the index subsystem.

Load the relevant `agentos-pkg/design/`, `agentos-pkg/appendix/`, or `agentos-pkg/references/` surface.

When the caller needs concrete examples of good and bad block shape.

Load `agentos-pkg/references/index-block-catalog.md`.

When the caller needs behavioral testing of index entry paths, selection behavior, or usage patterns.

Load `agentos-testground`.

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
- keep command targets foregrounded; targeted commands fail closed on ambiguous targets, and `::land-all-approved` fails closed unless one foreground index workflow owns the cluster
- use file mutation only when the applicable surface gate is satisfied
- keep action separate from index reconciliation: open inference may advance other work without silently rewriting touched positions
- run a linter check after applying an approved index or appendix edit

For delegated read-only research that protects the caller's context, use `Packages.Master.Agent` against the relevant package or packages.

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
