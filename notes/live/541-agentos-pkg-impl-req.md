# Agentos Package Skill Skeleton - impl-req

## Impl.Abstract

- scope: create the first `tarav-pkg` Package.Skill skeleton in `agentos-md/skills/tarav-pkg/`
- status: implemented
- source context: `notes/live/540-package-skill-design-session.md`; user alignment on `Package.Skill`, `Package.Entry.Skill`, `Cited.Duplication`, and Agentos package split
- implementation intent: structural migration only; respect existing content for now
- target package: `tarav-pkg` only
- out of scope: `tarav-chatlas-pkg`, `tarav-iterante-pkg`, `agentos-md-pkg`, and any broad content rewrite

## Impl.Index

### Agentos.Package.Skill.Skeleton

- create `skills/tarav-pkg/` as the initial `Package.Skill` for Agentos core
- first architecture:
    - `SKILL.md`
    - `package.md`
    - `index/`
    - `appendix/`
    - `references/`
- the move is structural, not editorial
- existing Agentos public skill content is respected for now
- local-only Agentos-md concerns do not move into `tarav-pkg`; they should be routed toward local index or future local package work

### Workflow.Neutral.SKILL

- `tarav-pkg/SKILL.md` must be workflow neutral
- it should contain package identity and orientation information only
- it should not include commands, execution steps, or task-specific workflow instructions
- the goal is transparency to whatever caller task loads it
- operational instructions belong in `package.md`, `references/`, or entry/workflow skills, not in the package root `SKILL.md`

### Package.Control.Surface

- `package.md` is the first package-control surface
- it holds the package router, package boundaries, dependency notes, install notes, package agents, and entry-skill map
- it keeps control-plane material out of workflow-neutral `SKILL.md`
- it can later split into `package/*.md` only when size or lifecycle pressure justifies it

### Content.Preservation

- do not absorb current public Agentos skills by rewriting their content in this first slice
- do not move or delete existing skills
- represent current public Agentos skills as package subsystems or entry surfaces by reference
- content consolidation, cited duplication, and entry skill rewrites are later slices
- if content looks too local to `agentos-md`, record it as a local-index candidate rather than placing it in `tarav-pkg`

## Execution.Plan

### Slice 1 - Create Package Skeleton

- status: completed
- changes:
    - add `skills/tarav-pkg/SKILL.md`
    - add `skills/tarav-pkg/package.md`
    - add empty placeholder directories:
        - `skills/tarav-pkg/index/`
        - `skills/tarav-pkg/appendix/`
        - `skills/tarav-pkg/references/`
- observable result:
    - `tarav-pkg` exists as a loadable skill directory
    - root `SKILL.md` is workflow neutral and points to `package.md`
- validation:
    - inspect `SKILL.md` and confirm it contains no commands or workflow steps
    - inspect `package.md` and confirm it names the package boundary and current absorbed surfaces by reference

### Slice 2 - Add Package Router In package.md

- status: completed
- changes:
    - define `tarav-pkg` as Agentos core Package.Skill
    - list current public Agentos skill surfaces absorbed by the package as existing subsystems or entry surfaces
    - distinguish package identity from `agentos-md` repository identity
    - document that `agentos-hugentics-pkg` is not created now; Hugentics and Index stay inside `tarav-pkg` for this pass
- observable result:
    - an agent loading `tarav-pkg` can find existing Agentos usage, index, Hugentics, live-note, impl, and project-doctor surfaces
- validation:
    - verify listed skill paths exist
    - verify no current skill content was rewritten as part of the router slice

### Slice 3 - Record Local Boundary

- status: completed
- changes:
    - add a local-boundary section in `package.md`
    - state that local `agentos-md` concerns belong in `notes/index/` or future `agentos-md-pkg`, not in `tarav-pkg`
    - mark this as a routing rule, not a migration of existing content
- observable result:
    - implementation agents have a rule for avoiding package/local mixing
- validation:
    - confirm the rule is explicit in `package.md`

## Impl.Log

- impl-req created for `tarav-pkg` skeleton only
- accepted structure: `SKILL.md`, `package.md`, `index/`, `appendix/`, `references/`
- accepted constraint: root `SKILL.md` is workflow neutral and contains information only
- accepted constraint: first move is structural; respect existing content for now
- implemented Slice 1 — created `skills/tarav-pkg/` with workflow-neutral `SKILL.md`, `package.md`, and placeholder `index/`, `appendix/`, `references/` directories
- implemented Slice 2 — added package router sections in `package.md` that reference existing Agentos public skill surfaces without rewriting them
- implemented Slice 3 — added local boundary rule: `agentos-md` concerns belong in `notes/index/` or future `agentos-md-pkg`, not in `tarav-pkg`
- validation passed — root `SKILL.md` contains no command snippets or workflow steps; all referenced skill paths in `package.md` exist
- follow-up migration executed — moved Agentos Index `index/`, `appendix/`, `references/`, and `testing/` content from `agentos-index` into `tarav-pkg`
- follow-up migration executed — converted `agentos-index` and companion `agentos-index-*` skills into package entry skills pointing to `tarav-pkg` surfaces
