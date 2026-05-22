# Agentos Skill Roles - design-session

## Session.Abstract

- intent: revisit the role and design of each current Agentos skill to build a clear mental model of `agentos-pkg`
- active focus: classify skills as `agentos-pkg` core surfaces, `Package.Aux.Skill` surfaces, dependent package skills, external/general skills, or local/project-specific concerns
- source context: `agentos-pkg` skeleton and first index-content migration are in place
- state: active
- next: review the package-root and index auxiliary-skill group first

## Design.Index

### Agentos.Skill.Role.Review

- session-local review of every skill currently present under `skills/`
- goal is package mental modeling, not immediate implementation
- each skill should be classified by package relationship and future action
- each reviewed skill gets a dedicated `Design.Index` block
- likely outcomes: keep as package root, keep as `Package.Aux.Skill`, absorb content into `agentos-pkg`, move to dependent package, park as local concern, or leave external/general
- content migration is separate from role classification
- reviewed auxiliary skills use block names like `Package.Aux.Skill:<skill-name>`

### Agentos.Package.Skill.Rings

- `agentos-pkg` core: package-owned content and package root surfaces
- `Package.Aux.Skill`: package-associated top-level skill that adds specialized intention, operation, workflow, or subsystem focus while pointing into `agentos-pkg`
- dependent package skill: skill that should belong to a future package such as `agentos-chatlas-pkg` or `agentos-iterante-pkg`
- external/general skill: reusable skill that may depend on Agentos conventions but is not Agentos core
- local/project concern: material specific to `agentos-md` and better suited for `notes/index/` or a future `agentos-md-pkg`

### Package.Aux.Skill.Visibility

- a `Package.Aux.Skill` is a visibility and attention surface for a `Package.Skill`
- skill names and descriptions appear in agent context, so auxiliary skills help agents discover available package subsystems, operations, and workflows before loading the package root
- the package root `SKILL.md` should provide similar discoverability after load: it acts like an `AGENTS.md` for the package or system
- aux skill `SKILL.md` files provide tuned intro prompts for a subsystem, operation, or workflow
- this improves routing, context economy, and task alignment without creating a new package authority
- auxiliary skills may be kept physically separate when visibility, triggerability, or tuned prompting is valuable
- duplicated context they carry should use `Cited.Duplication` back to authoritative package concepts

### Package.Aux.Skill.Mode

- `Package.Aux.Skill` does not imply workflow-neutral behavior
- some auxiliary skills are workflow-neutral subsystem surfaces that orient the caller without changing task flow
- some auxiliary skills are operational workflow surfaces; loading them means the agent is entering that workflow mode
- operational auxiliary skills are tuned execution prompts, not data-only documentation surfaces
- `Workflow.Neutral.Skill` is therefore a property of some skills, not the default for all auxiliary skills

### Workflow.Neutral.Skill

- `Workflow.Neutral.Skill` is a skill that provides orientation or package context without steering the caller into a workflow
- loading it should not change the caller's current task, action mode, or execution path
- contains information, routing, and boundaries rather than commands or task procedures
- useful for `Package.Skill` roots because package roots should welcome many caller intentions transparently
- contrasts with `Workflow.Skill`, which intentionally guides a recurring task

#### meta

- emerged from `agentos-pkg` root design

### Skill.Role:agentos-pkg

- `agentos-pkg` is the root `Package.Skill` for Agentos core
- its root `SKILL.md` is a `Workflow.Neutral.Skill`
- owns package-level public Agentos knowledge and routing
- currently contains the Agentos Index subsystem directly: `index/`, `appendix/`, `references/`, `testing/`
- routes existing Agentos public skills as package surfaces or auxiliary skills
- should absorb general Agentos framework content before narrower package skills are split out

#### meta

- current action: keep as package root
- future action: enrich `package.md` as the package router while keeping `SKILL.md` workflow-neutral
- boundary note: local `agentos-md` implementation concerns belong in `notes/index/` or future `agentos-md-pkg`, not in `agentos-pkg`

### Package.Aux.Skill:agentos-index

- `agentos-index` is the public `Package.Aux.Skill` for the Agentos Index subsystem of `agentos-pkg`
- functions as a workflow-neutral index subpackage skill: loading it orients the caller to index purpose, structure, and available functions without forcing an operation
- supports `Index.Agent` behavior: the caller may navigate the index itself or spawn a subagent to avoid context pollution
- primary function is index research: extract, cite, and return index knowledge relevant to the current chat/task context
- also routes optional operations such as writing, diagnosis, testing, and maintenance through a functionality table
- the key distinction is not separate skills; it is separate index functions
- may absorb narrower index auxiliary skills when their behavior can be represented as function rows instead of separate public skills
- keeps authoritative concept content in `agentos-pkg/index/`, appendix depth in `agentos-pkg/appendix/`, and operational detail in `agentos-pkg/references/`

#### meta

- current action: keep as auxiliary skill
- future action: collapse current index auxiliary skills into `agentos-index`; recreate narrower auxiliary skills later only if a concrete operational need emerges

### Package.Aux.Skill:agentos-index-activate

- `agentos-index-activate` is a deprecated `Package.Aux.Skill` for the Agentos Index subsystem of `agentos-pkg`
- its former role was explicit `Index.Runtime` bootstrap
- this role is now absorbed by `agentos-index` orientation and `Index.Agent` context-collection behavior
- should not remain a primary public entry point
- existing references should migrate toward `agentos-index` for index orientation or direct `Index.Agent` collection for task-specific context
- operational launch details may remain in `agentos-pkg/references/launch-runtime.md` as internal/reference material

#### meta

- current action: deprecate
- future action: remove or fold into `agentos-index` after dependent references are updated
- implementation note: project startup guidance still references `agentos-index-activate`; that should be updated when this role decision is implemented

### Package.Aux.Skill:agentos-index-writer

- `agentos-index-writer` is a deprecated standalone `Package.Aux.Skill` for the Agentos Index subsystem of `agentos-pkg`
- its role is still important: gated mutation of the Agentos Index
- the role should be represented as a writing function inside `agentos-index`, not as a separate public skill by default
- writing still needs explicit workflow control: placement checks, overlap checks, wording approval, routing updates, and `Index.Writer.Maintenance.Pass`
- the function remains user-gated; collapsing the skill must not weaken write approval or maintenance discipline

#### meta

- current action: collapse into `agentos-index`
- future action: recreate as a narrower auxiliary skill only if a concrete operational need for a separate public handle emerges

### Package.Aux.Skill:agentos-index-doctor

- `agentos-index-doctor` is a deprecated standalone `Package.Aux.Skill` for the Agentos Index subsystem of `agentos-pkg`
- its role is index diagnosis: structural checks, routing checks, staleness review, coherence review, coverage gaps, and placement drift
- the role should be represented as a diagnosis function inside `agentos-index`, not as a separate public skill by default
- diagnosis remains report-only unless the user explicitly invokes a write function

#### meta

- current action: collapse into `agentos-index`
- future action: recreate as a narrower auxiliary skill only if testing or automation needs a separate public handle

### Package.Aux.Skill:agentos-index-test

- `agentos-index-test` is a deprecated standalone `Package.Aux.Skill` for the Agentos Index subsystem of `agentos-pkg`
- its role is runtime verification for a package index surface
- the role should be represented as a testing function inside `agentos-index`, not as a separate public skill by default
- testing may still use package `testing/` files, subagents, and reports; only the public skill split is collapsed

#### meta

- current action: collapse into `agentos-index`
- future action: recreate as a narrower auxiliary skill only if repeated automation needs a separate public handle

### Deprecated.Skill:agentos-usage

- `agentos-usage` is deprecated and should not be treated as a `Package.Aux.Skill`
- its former role was general Agentos usage orientation
- that role belongs to `agentos-pkg`: the package root and package router should guide agents to documentation, index surfaces, references, workflows, and package functions
- should not remain a second package router or competing documentation authority

#### meta

- current action: deprecate
- future action: remove or replace with direct `agentos-pkg` guidance in project startup surfaces

### Package.Aux.Skill:agentos-hugentics

- `agentos-hugentics` is a `Package.Aux.Skill` for `agentos-pkg`
- its role is the public auxiliary skill for the Hugentic Harness subsystem
- is a workflow-neutral subsystem surface: loading it gives the Hugentic map without entering a specific Hugentic workflow mode
- adds caller intention: the caller wants the Hugentic workflow map, not general Agentos package orientation
- should remain public because Hugentics is an important Agentos subsystem with its own workflow family
- points back to `agentos-pkg` as the package SSOT for shared Agentos concepts
- may later move into `agentos-hugentics-pkg` if the Hugentic subsystem needs its own package root

#### meta

- current action: keep as auxiliary skill inside `agentos-pkg`
- future action: revisit package split only if Hugentics grows beyond `agentos-pkg`

### Hugentic.Aux.Skill.Modularity

- `agentos-hugentics` is the workflow-neutral subsystem aux skill for the Hugentic Harness
- Hugentic workflow skills can remain physically separate when they improve `Package.Aux.Skill.Visibility`
- they are nested auxiliary surfaces under `agentos-hugentics`, which is itself rooted in `agentos-pkg`
- `hugentics-designer`, `hugentics-impl-designer`, and `hugentics-impl-executer` are operational nested aux skills
- loading an operational nested aux skill means the agent is entering that workflow mode
- their main value is tuned execution prompting, triggerability, context economy, and operation-specific gates
- they should not become independent authorities for Hugentic concepts
- durable concepts remain rooted in `agentos-pkg`; duplicated local workflow context should use `Cited.Duplication`
- trigger-only skills that merely point to these operational aux skills are redundant once activation language is moved into the operational skills

#### meta

- current action: keep as design rule for reviewing `hugentics-designer`, `hugentics-impl-designer`, and `hugentics-impl-executer`

### Package.Aux.Skill:hugentics-designer

- `hugentics-designer` is a nested `Package.Aux.Skill` under `agentos-hugentics`
- its role is the tuned prompt and workflow master for `What.Design.Session` / `Main.Designer.Agent`
- is not workflow-neutral; loading it means the agent is entering Hugentic design-session mode
- not a separate package authority; it exists because its description and `SKILL.md` prompt strongly shape agent behavior
- should carry phase-specific activation language, routing, references, gates, and cited duplicated context
- durable Hugentic concepts remain rooted in `agentos-pkg`

#### meta

- current action: keep as nested auxiliary skill
- implementation note: keep linked to `agentos-hugentics` as subsystem map
- implementation note: absorb useful trigger phrases from `trigger-design-session`

### Package.Aux.Skill:hugentics-impl-designer

- `hugentics-impl-designer` is a nested `Package.Aux.Skill` under `agentos-hugentics`
- its role is the tuned prompt and workflow master for Impl.Req design / `impl.designer.agent`
- is not workflow-neutral; loading it means the agent is entering implementation-design mode
- not a separate package authority; it exists because its description and `SKILL.md` prompt strongly shape agent behavior
- should carry phase-specific activation language, routing, references, artifact rules, gates, and cited duplicated context
- durable Hugentic and implementation-design concepts remain rooted in `agentos-pkg`

#### meta

- current action: keep as nested auxiliary skill
- implementation note: keep linked to `agentos-hugentics` as subsystem map
- implementation note: absorb useful trigger phrases from `trigger-impl-req`

### Package.Aux.Skill:hugentics-impl-executer

- `hugentics-impl-executer` is a nested `Package.Aux.Skill` under `agentos-hugentics`
- its role is the tuned prompt and workflow master for Impl.Req execution / `impl.executer.agent`
- is not workflow-neutral; loading it means the agent is entering implementation-execution mode
- not a separate package authority; it exists because its description and `SKILL.md` prompt strongly shape agent behavior
- should carry phase-specific activation language, routing, execution gates, references, and cited duplicated context
- durable Hugentic and implementation-execution concepts remain rooted in `agentos-pkg`

#### meta

- current action: keep as nested auxiliary skill
- implementation note: absorb useful trigger phrases from `trigger-impl-execution`
- implementation note: its current recommended skills still mention deprecated `agentos-usage` and `agentos-index-activate`; update when implementing this design

## Session.Notes

### Traversal Tracker

#### Ring 1 - agentos-pkg Core / Existing Auxiliary Skills

- [x] `agentos-pkg`
- [x] `agentos-index`
- [x] `agentos-index-activate`
- [x] `agentos-index-writer`
- [x] `agentos-index-doctor`
- [x] `agentos-index-test`

#### Ring 2 - Likely agentos-pkg-Owned, Not Yet Absorbed

- [x] `agentos-usage`
- [x] `agentos-hugentics`
- [x] `hugentics-designer`
- [x] `hugentics-impl-designer`
- [x] `hugentics-impl-executer`
- [ ] `trigger-design-session`
- [ ] `trigger-impl-req`
- [ ] `trigger-impl-execution`
- [ ] `trigger-hugentic-status`
- [ ] `trigger-capture-audit`
- [ ] `trigger-chat-status`
- [ ] `artifact-design-session`
- [ ] `artifact-impl-req`
- [ ] `artifact-design-summary`
- [ ] `artifact-issue-report`
- [ ] `agentos-live-note-base`
- [ ] `agentos-live-scripts-base`
- [ ] `agentos-file-numbering-base`
- [ ] `agentos-project-doctor`

#### Ring 3 - Likely Dependent Package Skills

- [ ] `chatlas-usage`
- [ ] `agentos-chatlas-retention-audit`
- [ ] `agentos-session-continue`
- [ ] `agentos-session-zip-transcript`
- [ ] `agentos-skills-miner-ingenier`

#### Ring 4 - External / General / Ambiguous

- [ ] `codebase-general-cleanup`
- [ ] `git-commit-trigger`
- [ ] `flutter-adb-usage`

### Review Protocol

For each skill or skill group:

1. inspect current role and dependencies
2. decide package relationship
3. decide desired future action
4. capture a dedicated skill role block in `Design.Index`
5. update the traversal checkbox

## Session.Log

- session opened to revisit Agentos skill roles after creating `agentos-pkg` and migrating Agentos Index content into it
- initial skill inventory captured as traversal tracker
- review protocol updated — every reviewed skill gets a dedicated `Design.Index` block
- `agentos-pkg` reviewed — package root retained; `Workflow.Neutral.Skill` concept introduced
- `Package.Aux.Skill` accepted as the general concept name; entry is one possible auxiliary-skill function, not the general role
- `agentos-index` reviewed — retained as a workflow-neutral `Package.Aux.Skill` and specific entry point to the Agentos Index subsystem
- `agentos-index-activate` reviewed — deprecated as a standalone aux skill because its bootstrap role is absorbed by `agentos-index` and `Index.Agent` context collection
- `agentos-index` reframed as the single public index auxiliary skill; index research, writing, diagnosis, testing, and maintenance are index functions rather than separate public skills by default
- `agentos-index-writer`, `agentos-index-doctor`, and `agentos-index-test` reviewed — collapse into `agentos-index`, while preserving their roles as function rows and allowing future re-splitting only for concrete operational needs
- `agentos-usage` reviewed — deprecated entirely, not retained as a `Package.Aux.Skill`; `agentos-pkg` should guide agents to documentation and package surfaces
- `agentos-hugentics` reviewed — retained as an important subsystem `Package.Aux.Skill` inside `agentos-pkg`
- `Package.Aux.Skill.Visibility` captured — aux skills are visibility, attention, and tuned-prompt surfaces; package root `SKILL.md` should act like an `AGENTS.md` for the package/system
- `Package.Aux.Skill.Mode` captured — aux skills can be workflow-neutral subsystem surfaces or operational workflow surfaces
- Hugentic nested-skill direction captured — keep operational workflow skills separate when tuned execution prompting, triggerability, and gates are valuable, while rooting authority in `agentos-pkg`
- `hugentics-designer`, `hugentics-impl-designer`, and `hugentics-impl-executer` reviewed — retained as operational nested auxiliary skills under workflow-neutral `agentos-hugentics`
