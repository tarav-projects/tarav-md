# Agentos Skill Role Consolidation - impl-req

## Impl.Abstract

- scope: implement the completed Agentos skill-role design inventory by consolidating skill names, package ownership, cited-duplication surfaces, and durable package knowledge
- status: ready for execution
- source artifacts:
    - `notes/live/542-agentos-skill-roles-design-session.md`
    - `notes/live/545-agentos-pkg-skill-surface-alignment-impl-req.md`
    - `skills/agentos-pkg/package.md`
    - `skills/agentos-pkg/index/000-index.md`
    - `skills/agentos-pkg/index/100-index.md`
    - `skills/agentos-pkg/index/101-index.md`
    - `skills/agentos-pkg/index/104-index.md`
- implementation intent: move from role design to usable skill/package surfaces without doing every future redesign at once
- out of scope:
    - fully redesigning `agentos-project-doctor`
    - fully redesigning `agentos-codebase-cleanup`
    - fully redesigning `agentos-git-commit`
    - fully designing `hugentics-issue-tracker`
    - implementing all future package splits beyond the surfaces named here
    - deleting old compatibility skill directories before dependent references are updated

## Impl.Index

### Skill.Role.Inventory.Result

- the skill-role inventory in `notes/live/542-agentos-skill-roles-design-session.md` is complete
- all reviewed skills now have a role decision: keep, rename/reframe, absorb, park, move, or classify under a dependent package
- implementation should preserve the role decisions without reopening design unless current files contradict the design enough to block execution

### Natural.Placement.For.Skills

- `Natural.Placement:Skills` is the main implementation rule for operational skills
- skills are natural code-like workflow surfaces for procedures, gates, role framing, tool use, and execution-shaped guidance
- durable concept material belongs in package index blocks, appendix pages, or references
- skill-local duplicated context should use `Cited.Duplication` so related surfaces can be found, checked for drift, and aligned
- implementation should not treat skills as bad places for knowledge; it should move or cite content according to the natural surface for each facet

### Durable.Agentos.Index.Work

- promote `Agentos.Live.Note` and `Agentos.Live.Script` into the durable `agentos-pkg` index
- ensure `Multi.Index.Operation` remains routed and aligned with `Index.Agent`
- update or deprecate `Usage.Skill` in the durable index so package roots are the general usage/orientation surfaces
- absorb file-numbering content into `File.Numbering.Protocol`:
    - compact semantics in index block
    - design depth and rationale in appendix
    - operational procedure, CLI usage, target flags, and caveats in a package reference

### Agentos.Package.Skill.Surface.Work

- `agentos-pkg` remains the root `Package.Skill`
- `agentos-index` remains the single public index aux skill; old index activate/writer/doctor/test roles are functions inside it
- `agentos-hugentics` remains the workflow-neutral Hugentic subsystem map
- Hugentic operational skills remain separate when they provide workflow mode, tuned prompting, gates, or status/capture behavior
- package routers and root skills should route current names and mark old names only as compatibility/deprecated when needed

### Rename.And.Reframe.Targets

- Hugentic trigger shims:
    - `trigger-design-session` -> absorbed into `hugentics-designer`
    - `trigger-impl-req` -> absorbed into `hugentics-impl-designer`
    - `trigger-impl-execution` -> absorbed into `hugentics-impl-executer`
- Hugentic operational status/capture:
    - `trigger-hugentic-status` -> `hugentics-workflow-status`
    - `trigger-chat-status` -> `hugentics-chat-status`
    - `trigger-capture-audit` -> `hugentics-capture-audit`
- live surface protocol:
    - `agentos-live-scripts-base` -> `agentos-live-script`
    - `agentos-live-note-base` remains temporarily named until `Agentos.Live.Note` / `Agentos.Live.Script` promotion settles the public name
- Agentos utilities:
    - `agentos-skills-miner-ingenier` -> `agentos-skills-ingenier`
    - `codebase-general-cleanup` -> `agentos-codebase-cleanup`
    - `git-commit-trigger` -> `agentos-git-commit`
- Chatlas services:
    - `agentos-session-continue` -> `chatlas-session-continue`
    - `agentos-session-zip-transcript` -> `chatlas-session-zip-transcript`

### Absorb.Move.And.Park.Targets

- absorb `agentos-usage` into `agentos-pkg`
- absorb `chatlas-usage` into `agentos-chatlas-pkg`
- absorb `agentos-file-numbering-base` into `agentos-pkg`
- classify `agentos-chatlas-retention-audit` under `agentos-chatlas-pkg`
- move `flutter-adb-usage` to `/Users/pereiro/projects/csc-reactor-project/csc-reactor/csc-reactor-specs/skills`
- park `agentos-project-doctor` as a cited surface of `agentos-pkg` for a separate doctor/diagnosis design session

### Execution.Risk

- renames can break skill invocation references, package routers, project `AGENTS.md`, and current available-skill metadata
- some old skill directories may need to remain as compatibility stubs until references are updated
- Chatlas-owned moves should respect the current `agentos-chatlas-md` package state rather than inventing package structure
- do not perform broad deletion before a reference search proves the old surface is no longer routed as current

## Execution.Plan

### Slice 1 - Promote Durable Concepts And References

- status: pending
- changes:
    - add or update durable blocks for `Agentos.Live.Note`, `Agentos.Live.Script`, and `Natural.Placement:Skills`
    - ensure `Multi.Index.Operation` is routed and `Index.Agent` references it
    - update/deprecate `Usage.Skill` so package roots replace usage skills as general orientation surfaces
    - create or update file-numbering appendix/reference surfaces for design depth and operational procedure
- paths:
    - `skills/agentos-pkg/index/000-index.md`
    - `skills/agentos-pkg/index/100-index.md`
    - `skills/agentos-pkg/index/101-index.md`
    - `skills/agentos-pkg/index/104-index.md`
    - `skills/agentos-pkg/appendix/`
    - `skills/agentos-pkg/references/`
- validation:
    - inspect concept blocks and routing
    - `rg "Agentos.Live.Note|Agentos.Live.Script|Natural.Placement:Skills|Multi.Index.Operation|Usage.Skill|File.Numbering.Protocol" skills/agentos-pkg`

### Slice 2 - Align agentos-pkg Root, Router, And Index Aux Surfaces

- status: pending
- changes:
    - update `agentos-pkg` router to reflect current skill names, deprecated names, absorbed surfaces, and dependent package operations
    - ensure `agentos-index` presents research, writing, diagnosis, testing, and maintenance as functions
    - remove old usage-skill routing as a current path
- paths:
    - `skills/agentos-pkg/SKILL.md`
    - `skills/agentos-pkg/package.md`
    - `skills/agentos-index/SKILL.md`
    - `AGENTS.md`
- validation:
    - inspect package router and startup guidance
    - search for stale current-routing references to `agentos-usage`, split index aux skills, and usage-skill language

### Slice 3 - Align Hugentic Skills And Artifact Surfaces

- status: pending
- changes:
    - keep `agentos-hugentics` as workflow-neutral subsystem map
    - ensure `hugentics-designer`, `hugentics-impl-designer`, and `hugentics-impl-executer` own their activation language
    - create or rename status/capture skills as `hugentics-workflow-status`, `hugentics-chat-status`, and `hugentics-capture-audit`
    - keep artifact skills workflow-neutral and cited-duplicated from package/workflow concepts
    - keep `hugentics-issue-tracker` as planned role only unless implementation explicitly needs a stub
- paths:
    - `skills/agentos-hugentics/`
    - `skills/hugentics-designer/`
    - `skills/hugentics-impl-designer/`
    - `skills/hugentics-impl-executer/`
    - `skills/trigger-*`
    - `skills/artifact-*`
- validation:
    - inspect activation sections and artifact pointer text
    - search for trigger-only skills still presented as current public routes

### Slice 4 - Align Live Surface And Utility Skills

- status: pending
- changes:
    - update `agentos-live-note-base` as a live-note protocol aux skill for `Agentos.Live.Note`
    - rename/reframe `agentos-live-scripts-base` to `agentos-live-script`
    - absorb `agentos-file-numbering-base` into package index/appendix/reference surfaces
    - rename/reframe `agentos-skills-miner-ingenier` to `agentos-skills-ingenier`
    - rename/reframe `codebase-general-cleanup` to `agentos-codebase-cleanup`
    - rename/reframe `git-commit-trigger` to `agentos-git-commit`
    - make operational skills cited-duplication surfaces where they repeat package concepts
- paths:
    - `skills/agentos-live-note-base/`
    - `skills/agentos-live-scripts-base/`
    - `skills/agentos-file-numbering-base/`
    - `skills/agentos-skills-miner-ingenier/`
    - `skills/codebase-general-cleanup/`
    - `skills/git-commit-trigger/`
- validation:
    - inspect renamed or updated `SKILL.md` files
    - search package router and skill references for old names

### Slice 5 - Move Or Classify Dependent Package Skills

- status: pending
- changes:
    - absorb `chatlas-usage` into `agentos-chatlas-pkg` index, appendix, or references
    - classify/update `agentos-chatlas-retention-audit` as Chatlas package aux skill
    - rename/reframe `agentos-session-continue` to `chatlas-session-continue`
    - rename/reframe `agentos-session-zip-transcript` to `chatlas-session-zip-transcript`
    - move `flutter-adb-usage` to `/Users/pereiro/projects/csc-reactor-project/csc-reactor/csc-reactor-specs/skills`
- paths:
    - `skills/chatlas-usage/`
    - `skills/agentos-chatlas-retention-audit/`
    - `skills/agentos-session-continue/`
    - `skills/agentos-session-zip-transcript/`
    - `skills/flutter-adb-usage/`
    - `/Users/pereiro/projects/agentos-project/agentos-chatlas-md/`
    - `/Users/pereiro/projects/csc-reactor-project/csc-reactor/csc-reactor-specs/skills`
- validation:
    - inspect target package structures before moving
    - verify old names are not presented as current routes after moves
    - preserve content during moves

### Slice 6 - Focused Reference And Compatibility Cleanup

- status: pending
- changes:
    - update references across `AGENTS.md`, package routers, skill descriptions, and skill bodies
    - leave compatibility stubs only where needed to avoid breaking current invocation paths
    - report any deferred old-name references and why they remain
    - update this Impl.Req `Impl.Log`
- validation:
    - `rg "agentos-usage|chatlas-usage|Usage.Skill|trigger-design-session|trigger-impl-req|trigger-impl-execution|trigger-hugentic-status|trigger-capture-audit|trigger-chat-status|agentos-live-scripts-base|agentos-file-numbering-base|agentos-skills-miner-ingenier|codebase-general-cleanup|git-commit-trigger|agentos-session-continue|agentos-session-zip-transcript|flutter-adb-usage" AGENTS.md skills notes/index notes/live`
    - `git -C agentos-md diff --check`

## Impl.Log

- impl-req created from completed Agentos skill-role design session
- source design session reports all inventory rings reviewed and no unchecked traversal items
- implementation should proceed as a consolidation pass, not a redesign pass
- high-risk areas are skill renames, cross-package moves, and stale references in package routers or skill descriptions
