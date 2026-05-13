# Hugentics Skill Surface Reorganization - impl-req

## Impl.Abstract

- **scope:** reorganize the agentos-md skill surface to match the new Hugentic Harness model
- **status:** not started
- **source:** design session 523 (index reindex) — big picture workflow convergence

## Impl.Index

### Skill.Surface.Model

- the new skill surface has three layers: presentation, triggers, workflow masters
- `agentos-hugentics` is the single entry point to the hugentic harness — a presentation skill that maps the landscape
- trigger skills are lightweight, user-invoked — they steer the agent and ensure the right master loads
- workflow master skills are documentation portals — full instructions for running a workflow, including artifact formats
- artifact pointer skills follow the same shape as triggers — point to the master that defines the format
- `agentos-usage` stays as the general agentos orientation, lists `agentos-hugentics` as a subsystem reference
- `agentos-index` stays as a separate subsystem peer to `agentos-hugentics`

### New.Skill.Surface

- presentation: `agentos-hugentics`
- workflow masters: `hugentics-designer`, `hugentics-impl-designer`, `hugentics-impl-executer`
- triggers: `trigger-design-session`, `trigger-impl-req`, `trigger-impl-execution`
- artifact pointers: `artifact-design-session`, `artifact-impl-req`, `artifact-design-summary`, `artifact-issue-report`

### Migration.Safety

- all migrated skills are first copied to `skills/_DEPRECATED/` — nothing is lost
- originals are not deleted until new skills are created and content is migrated
- the system is never broken mid-migration

### Content.Migration.Map

- `agentos-design-session` → content migrates to `hugentics-designer`
- `agentos-design-implementation` → content migrates to `hugentics-impl-executer`
- `agentos-artifact-impl-req` → content migrates to `hugentics-impl-designer`
- `agentos-artifact-design-summary` → artifact pointer to owner TBD
- `agentos-artifact-issue-report` → artifact pointer to owner TBD
- `agentos-usage` → updated in place (add `agentos-hugentics` reference)

### Unchanged.Skills

- index subsystem: `agentos-index`, `agentos-index-activate`, `agentos-index-trigger`, `agentos-index-writer`, `agentos-index-doctor`, `agentos-index-resolution`, `agentos-index-appendix-base`
- base/protocol: `agentos-canvas-base`, `agentos-live-note-base`, `agentos-live-scripts-base`, `agentos-file-numbering-base`
- session utilities: `agentos-session-status`, `agentos-session-continue`, `agentos-session-zip-transcript`
- meta: `agentos-skills-miner-ingenier`, `agentos-project-doctor`, `codebase-general-cleanup`, `git-commit-trigger`

## Execution.Plan

### Slice 1 — Safety: deprecate originals

- copy the following skill folders to `skills/_DEPRECATED/`:
  - `agentos-design-session`
  - `agentos-design-implementation`
  - `agentos-artifact-impl-req`
  - `agentos-artifact-design-summary`
  - `agentos-artifact-issue-report`
- validation: all originals exist in `_DEPRECATED/`, originals still in place

### Slice 2 — Create `agentos-hugentics`

- create `skills/agentos-hugentics/SKILL.md`
- content: presentation skill — map of the harness, list of workflows, agents, triggers, pointers to masters
- source: canvas big picture + design session 523 convergence
- validation: skill file exists, describes the full landscape

### Slice 3 — Create `hugentics-designer` + trigger + artifact pointer

- create `skills/hugentics-designer/SKILL.md` — Main.Designer.Agent workflow master
- create `skills/trigger-design-session/SKILL.md` — trigger pointing to `hugentics-designer`
- create `skills/artifact-design-session/SKILL.md` — artifact pointer to `hugentics-designer`
- migrate content from `_DEPRECATED/agentos-design-session/SKILL.md`
- validation: master contains the design session workflow logic, trigger and artifact pointer are lightweight

### Slice 4 — Create `hugentics-impl-designer` + trigger + artifact pointer

- create `skills/hugentics-impl-designer/SKILL.md` — impl.designer.agent workflow master
- create `skills/trigger-impl-req/SKILL.md` — trigger pointing to `hugentics-impl-designer`
- create `skills/artifact-impl-req/SKILL.md` — artifact pointer to `hugentics-impl-designer`
- migrate content from `_DEPRECATED/agentos-artifact-impl-req/SKILL.md`
- validation: master contains the impl-req design workflow, trigger and artifact pointer are lightweight

### Slice 5 — Create `hugentics-impl-executer` + trigger

- create `skills/hugentics-impl-executer/SKILL.md` — impl.executer.agent workflow master
- create `skills/trigger-impl-execution/SKILL.md` — trigger pointing to `hugentics-impl-executer`
- migrate content from `_DEPRECATED/agentos-design-implementation/SKILL.md`
- validation: master contains the execution workflow, trigger is lightweight

### Slice 6 — Artifact pointer stubs

- create `skills/artifact-design-summary/SKILL.md` — pointer stub, owner TBD
- create `skills/artifact-issue-report/SKILL.md` — pointer stub, owner TBD
- migrate any format definitions from `_DEPRECATED/` equivalents
- validation: pointer stubs exist, content preserved

### Slice 7 — Update `agentos-usage`

- update `skills/agentos-usage/SKILL.md` to reference `agentos-hugentics` as a subsystem
- validation: `agentos-usage` lists `agentos-hugentics` alongside `agentos-index`

### Slice 8 — Remove originals

- remove the original skill folders (now replaced by new surface):
  - `agentos-design-session`
  - `agentos-design-implementation`
  - `agentos-artifact-impl-req`
  - `agentos-artifact-design-summary`
  - `agentos-artifact-issue-report`
- validation: no duplicate skills, `_DEPRECATED/` still has backups

## Impl.Log

(empty — not started)
