# Package Skill Index Promotion - impl-req

## Impl.Abstract

- scope: promote the Package.Skill design concepts from live design artifacts into the durable Agentos public index
- status: implemented
- source artifacts:
    - `notes/live/540-package-skill-design-session.md`
    - `notes/live/542-agentos-skill-roles-design-session.md`
- target surfaces:
    - `skills/agentos-pkg/index/101-index.md`
    - `skills/agentos-pkg/index/104-index.md`
    - `skills/agentos-pkg/index/000-index.md`
    - `notes/index/001-index.md`
- implementation intent: make the package-skill model durable enough that another agent can start `agentos-chatlas-pkg` without relying on live-session-only context
- out of scope: creating `agentos-chatlas-pkg`, migrating Chatlas skills, or completing the full Agentos skill-role review

## Impl.Index

### Package.Skill.Promotion.Scope

- package-skill concepts currently live mainly in `notes/live/540-package-skill-design-session.md`
- `Workflow.Neutral.Skill` and the `agentos-pkg` role live in `notes/live/542-agentos-skill-roles-design-session.md`
- this implementation promotes only the minimal durable index surface needed for package-skill work
- the update should keep blocks compact and index-native; extended examples can stay in live notes until appendix work is needed

### Target.New.Blocks

- add to `skills/agentos-pkg/index/101-index.md`:
    - `Package.Skill`
    - `Package.Aux.Skill`
    - `Workflow.Neutral.Skill`
    - `Package.Skill.Index`
    - `Package.Skill.Router`
    - `Package.Skill.Dependency`
- optional if space and fit remain good:
    - `Package.Skill.Install`
    - `Package.Agent`
- these are skill/package-system concepts, so `101-index.md` is the natural first target

### Target.Updated.Blocks

- update `Agentos.Skills` in `101-index.md` to mention package roots and package auxiliary skills
- update `Usage.Skill` in `101-index.md` to clarify relation to `Workflow.Neutral.Skill`
- update `Workflow.Skill` in `101-index.md` to contrast with `Workflow.Neutral.Skill`
- update `Project.Index.Skill` in `104-index.md` to align with `Package.Aux.Skill` and `Package.Skill.Index`
- update `Index.Surface.Layout` in `104-index.md` if needed so package index paths are explicit and current
- update `000-index.md` routing so all new concepts resolve to `101-index.md`
- update `notes/index/001-index.md` so the local index points to `skills/agentos-pkg/index/000-index.md`

### Promotion.Constraints

- preserve the design intent from the live notes; do not redesign package skills during implementation
- use `Inline.Relatedness` discipline: prefer natural inline `Dotted.Name` mentions; use bracket `Concept.Cite` only when needed
- keep blocks compact; do not paste full live-note discussion into the index
- if a concept seems too broad for the first pass, add a compact block now and leave appendix expansion for later
- run an `Index.Writer.Maintenance.Pass` for edited concepts: at minimum search mentions of updated concepts and fix direct stale references found in target surfaces

## Execution.Plan

### Slice 1 - Add Package Skill Core Blocks

- status: complete
- changes:
    - add `Package.Skill`
    - add `Package.Aux.Skill`
    - add `Workflow.Neutral.Skill`
    - add `Package.Skill.Index`
    - add `Package.Skill.Router`
    - add `Package.Skill.Dependency`
- path:
    - `skills/agentos-pkg/index/101-index.md`
- observable result:
    - package-skill model can be discovered from the public index without opening live notes
- validation:
    - grep `101-index.md` for each new heading
    - ensure blocks are routed in `000-index.md` in Slice 3

### Slice 2 - Add Secondary Blocks If Still Compact

- status: complete
- changes:
    - add `Package.Skill.Install`
    - add `Package.Agent`
- path:
    - `skills/agentos-pkg/index/101-index.md`
- observable result:
    - install and package-agent concepts are available in the durable index
- validation:
    - if adding these makes `101-index.md` too dense, stop and report before writing; otherwise add and route them

### Slice 3 - Update Existing Index Blocks And Routing

- status: complete
- changes:
    - update `Agentos.Skills`
    - update `Usage.Skill`
    - update `Workflow.Skill`
    - update `Project.Index.Skill`
    - update `Index.Surface.Layout` if needed
    - update `000-index.md` routing
- paths:
    - `skills/agentos-pkg/index/101-index.md`
    - `skills/agentos-pkg/index/104-index.md`
    - `skills/agentos-pkg/index/000-index.md`
- observable result:
    - existing skill/index blocks agree with the package-skill model
- validation:
    - search for `Package.Skill`, `Package.Aux.Skill`, and `Workflow.Neutral.Skill` references
    - ensure no new concept heading is missing from `000-index.md`

### Slice 4 - Fix Local Index Pointer

- status: complete
- changes:
    - update `notes/index/001-index.md` public-index pointer from `skills/agentos-index/index/000-index.md` to `skills/agentos-pkg/index/000-index.md`
- path:
    - `notes/index/001-index.md`
- observable result:
    - local index points to the actual migrated public index
- validation:
    - inspect `001-index.md`

### Slice 5 - Maintenance Pass And Report

- status: complete
- changes:
    - search stable markdown surfaces for stale package/index path references relevant to this promotion
    - report any remaining stale references that are out of scope
- validation:
    - `rg "skills/agentos-index/index|skills/agentos-index/appendix|Package.Skill|Package.Aux.Skill|Workflow.Neutral.Skill" skills notes/index`
    - `git -C agentos-md diff --check`

## Impl.Log

- impl-req created from package-skill design session and Agentos skill-role design session
- related live notes explicitly referenced:
    - `notes/live/540-package-skill-design-session.md`
    - `notes/live/542-agentos-skill-roles-design-session.md`
- implemented package-skill promotion:
    - added `Package.Skill`, `Package.Aux.Skill`, `Workflow.Neutral.Skill`, `Package.Skill.Index`, `Package.Skill.Router`, `Package.Skill.Dependency`, `Package.Skill.Install`, and `Package.Agent` to `skills/agentos-pkg/index/101-index.md`
    - updated `Agentos.Skills`, `Usage.Skill`, and `Workflow.Skill` in `101-index.md`
    - updated `Project.Index.Skill` and `Index.Surface.Layout` in `skills/agentos-pkg/index/104-index.md`
    - routed the new concepts in `skills/agentos-pkg/index/000-index.md`
    - updated `notes/index/001-index.md` to point at `skills/agentos-pkg/index/000-index.md`
- maintenance pass updated direct stale `skills/agentos-index/index` and `skills/agentos-index/appendix` references in stable skill surfaces where they referred to the migrated public index
- validation:
    - concept headings and routing were checked with `rg`
    - stale package/index path search was run across `skills` and `notes/index`
    - `git -C agentos-md diff --check` passed
