# Agentos Package Skill Surface Alignment - impl-req

## Impl.Abstract

- scope: align the current Agentos package and key auxiliary skill surfaces with the active `agentos-pkg` role design so the skills are usable in parallel on other projects
- status: implemented
- source artifacts:
    - `notes/live/542-agentos-skill-roles-design-session.md`
    - `notes/live/540-package-skill-design-session.md`
    - `notes/live/543-package-skill-index-promotion-impl-req.md`
- target surfaces:
    - `skills/agentos-pkg/SKILL.md`
    - `skills/agentos-pkg/package.md`
    - `skills/agentos-index/SKILL.md`
    - `skills/agentos-hugentics/SKILL.md`
    - `skills/hugentics-designer/SKILL.md`
    - `skills/hugentics-impl-designer/SKILL.md`
    - `skills/hugentics-impl-executer/SKILL.md`
    - `AGENTS.md`
- implementation intent: make `agentos-pkg` the root package orientation surface, make `agentos-index` the single public index aux skill, and align Hugentic workflow-master skills as operational nested aux skills without waiting for the full skill-role design session to finish
- out of scope:
    - deleting deprecated skill directories
    - finalizing `trigger-hugentic-status`, `trigger-capture-audit`, or `trigger-chat-status`
    - completing the full Agentos skill-role review
    - creating or editing `agentos-chatlas-pkg`, `agentos-iterante-pkg`, or `agentos-md-pkg`

## Impl.Index

### Package.Root.Alignment

- `agentos-pkg` is the core `Package.Skill` for Agentos
- root `SKILL.md` should be workflow neutral, but it should still give package-level discoverability, like an `AGENTS.md` for the package/system
- `package.md` is the package router and should stop presenting deprecated surfaces as first-class current routes
- `agentos-usage` is deprecated and should not remain a separate package router

### Index.Aux.Alignment

- `agentos-index` is the single public `Package.Aux.Skill` for the Agentos Index subsystem
- it should be workflow neutral and subpackage-like: load it to understand and use index functions, not to force an operation
- index behavior should be organized as functions rather than separate public skills:
    - research/navigation
    - writing/mutation
    - diagnosis
    - testing
    - maintenance
- `agentos-index-activate`, `agentos-index-writer`, `agentos-index-doctor`, and `agentos-index-test` are deprecated as standalone public aux skills for now; their useful content should be represented as functions inside `agentos-index`
- this pass should not delete those skill directories; leave compatibility surfaces for later cleanup unless a minimal stub update is clearly necessary

### Hugentic.Aux.Alignment

- `agentos-hugentics` is the workflow-neutral subsystem aux skill for the Hugentic Harness
- `hugentics-designer`, `hugentics-impl-designer`, and `hugentics-impl-executer` are operational nested aux skills under `agentos-hugentics`
- loading one of those operational skills means entering the corresponding workflow mode
- trigger-only skills that merely point to these operational aux skills are redundant once useful trigger phrases move into the operational skills
- `trigger-design-session`, `trigger-impl-req`, and `trigger-impl-execution` should not remain the main activation path in current routing text

### Deprecation.Cleanup.Targets

- known stale references found during the readiness pass:
    - `AGENTS.md` still tells agents to load `agentos-usage` and `agentos-index-activate`
    - `skills/agentos-pkg/package.md` still lists deprecated index aux skills and trigger skills as current package routes
    - `skills/agentos-index/SKILL.md` still lists the old index aux split as current auxiliary skills
    - `skills/agentos-hugentics/SKILL.md` still routes through `trigger-design-session`, `trigger-impl-req`, and `trigger-impl-execution`
    - `skills/hugentics-impl-executer/SKILL.md` still recommends `agentos-usage` and `agentos-index-activate`
    - `skills/hugentics-designer/SKILL.md`, `skills/hugentics-impl-designer/SKILL.md`, and `skills/hugentics-impl-executer/SKILL.md` still describe trigger skills as primary activation paths
- project-doctor references to `agentos-usage` are known stale but can be deferred unless touched by the focused pass

## Execution.Plan

### Slice 1 - Align agentos-pkg Root And Router

- status: complete
- changes:
    - update `skills/agentos-pkg/SKILL.md` so it is workflow-neutral but gives package-level subsystem/function visibility
    - update `skills/agentos-pkg/package.md` so current routes reflect:
        - `agentos-pkg` as root package orientation
        - `agentos-index` as single public index aux skill
        - `agentos-hugentics` as Hugentic subsystem aux skill
        - Hugentic workflow masters as operational nested aux skills
    - demote deprecated surfaces into a clearly marked compatibility/deprecated section instead of current primary routing
- paths:
    - `skills/agentos-pkg/SKILL.md`
    - `skills/agentos-pkg/package.md`
- validation:
    - inspect both files
    - `rg "agentos-usage|agentos-index-activate|agentos-index-writer|agentos-index-doctor|agentos-index-test|trigger-design-session|trigger-impl-req|trigger-impl-execution" skills/agentos-pkg`

### Slice 2 - Align agentos-index As Single Index Aux Skill

- status: complete
- changes:
    - update `skills/agentos-index/SKILL.md` as the single workflow-neutral public aux skill for the Agentos Index subsystem
    - add a functionality table or equivalent sections for research/navigation, writing, diagnosis, testing, and maintenance
    - describe `Index.Agent` behavior: the caller may navigate itself or spawn a subagent to avoid context pollution; returned context should cite source blocks
    - stop presenting `agentos-index-activate`, `agentos-index-writer`, `agentos-index-doctor`, and `agentos-index-test` as the current public aux model
- path:
    - `skills/agentos-index/SKILL.md`
- validation:
    - inspect the updated skill
    - verify the old aux split is no longer presented as current routing

### Slice 3 - Align Hugentic Subsystem And Workflow Masters

- status: complete
- changes:
    - update `skills/agentos-hugentics/SKILL.md` so it is the workflow-neutral subsystem map and routes directly to operational workflow-master skills
    - update `skills/hugentics-designer/SKILL.md` to absorb useful phrases from `trigger-design-session` and stop presenting the trigger skill as the activation path
    - update `skills/hugentics-impl-designer/SKILL.md` to absorb useful phrases from `trigger-impl-req` and stop presenting the trigger skill as the activation path
    - update `skills/hugentics-impl-executer/SKILL.md` to absorb useful phrases from `trigger-impl-execution`, stop presenting the trigger skill as the activation path, and replace deprecated recommended skills with current guidance
- paths:
    - `skills/agentos-hugentics/SKILL.md`
    - `skills/hugentics-designer/SKILL.md`
    - `skills/hugentics-impl-designer/SKILL.md`
    - `skills/hugentics-impl-executer/SKILL.md`
- validation:
    - inspect updated Activation sections
    - `rg "trigger-design-session|trigger-impl-req|trigger-impl-execution|agentos-usage|agentos-index-activate" skills/agentos-hugentics skills/hugentics-designer skills/hugentics-impl-designer skills/hugentics-impl-executer`

### Slice 4 - Update Project Startup Guidance

- status: complete
- changes:
    - update `AGENTS.md` so sessions load `agentos-pkg` for Agentos package orientation
    - replace startup `agentos-index-activate` guidance with `agentos-index` / index-function guidance
    - keep routing into the relevant maintained project before edits
- path:
    - `AGENTS.md`
- validation:
    - inspect `AGENTS.md`
    - ensure it no longer instructs loading deprecated `agentos-usage` or `agentos-index-activate`

### Slice 5 - Focused Maintenance Pass

- status: complete
- changes:
    - search for stale references in the touched package/Hugentic/startup surfaces
    - report remaining stale references that are intentionally deferred
    - update this Impl.Req `Impl.Log`
- validation:
    - `rg "agentos-usage|agentos-index-activate|agentos-index-writer|agentos-index-doctor|agentos-index-test|trigger-design-session|trigger-impl-req|trigger-impl-execution|Package.Entry.Skill" AGENTS.md skills`
    - `git -C agentos-md diff --check`

## Impl.Log

- impl-req created from active Agentos skill-role design session
- readiness pass found that package and aux skill surfaces still expose deprecated startup, index, and trigger routes
- implementation should be a small forward pass only; the broader design session remains active and unresolved for remaining skills
- implemented package surface alignment:
    - updated `skills/agentos-pkg/SKILL.md` with workflow-neutral package subsystem visibility
    - updated `skills/agentos-pkg/package.md` so current routes point to `agentos-pkg`, `agentos-index`, `agentos-hugentics`, and Hugentic workflow masters
    - demoted `agentos-usage`, split index aux skills, and trigger-only activation skills into a compatibility/deprecated section
- implemented index aux alignment:
    - updated `skills/agentos-index/SKILL.md` as the single workflow-neutral public index aux skill
    - added index functions for research/navigation, writing/mutation, diagnosis, testing, and maintenance
    - described `Index.Agent` behavior and citation expectations
- implemented Hugentic alignment:
    - updated `skills/agentos-hugentics/SKILL.md` as a workflow-neutral subsystem map
    - updated `skills/hugentics-designer/SKILL.md`, `skills/hugentics-impl-designer/SKILL.md`, and `skills/hugentics-impl-executer/SKILL.md` so activation routes live in the workflow masters instead of trigger-only skills
    - updated `skills/hugentics-designer/references/impl-req.md` to hand off directly to `hugentics-impl-designer`
- implemented startup guidance alignment:
    - updated `AGENTS.md` to start with `agentos-pkg` and use `agentos-index` for index-grounded context and index functions
- maintenance pass:
    - updated direct stale package-index references in `skills/agentos-pkg/index/000-index.md`, `skills/agentos-pkg/index/104-index.md`, `skills/agentos-pkg/index/AGENTS.md`, `skills/agentos-pkg/appendix/Agentos.Surfaces-appendix.md`, and `skills/agentos-pkg/testing/activation-recall-01.md`
    - remaining stale references are intentionally deferred in deprecated compatibility skill directories, deprecated compatibility sections, and project-doctor surfaces called out as deferred by this Impl.Req
    - validation searches and `git -C agentos-md diff --check` passed
