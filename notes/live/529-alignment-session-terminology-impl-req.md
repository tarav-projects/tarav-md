# Alignment.Session Terminology Migration — Impl.Req

## Impl.Abstract

- scope: migrate old alignment/session terminology across index notes and skills to the new Alignment.Session model
- source: design-session 523, block `Alignment.Session.Design`
- status: draft — alignment in progress
- target surfaces: `agentos-md` index notes and skills

## Impl.Index

### 121.Renames

- `121-Design.Session.md` block renames:
  - `Design.Session` → `What.Design.Session`
  - `Session.Runtime.Loop` → `Alignment.Loop:What`
  - `InChat.Design.Session` → `Alignment.Backend:InChat:What`
  - `Artifact.Design.Session` → `Alignment.Backend:Artifact:What`
- internal reference updates:
  - `Design.Alignment.Question` → `Alignment.Question:What`
  - `Design.Enrichment.Discussion` → `Alignment.Discussion:What`
  - `Design.Consolidation` → `Alignment.Consolidation:What`
  - `User.Assistant.Turn` → `Alignment.User.Turn`
  - `Session.Maintenance.Turn` → `Alignment.Maintenance.Turn`
  - `Design.Alignment.Core` → `Alignment.Hugentic.Axis:What`
- add reference to general `Alignment.Session` pattern (new note)

### 123.Renames

- `123-Impl.Req.md` updates:
  - line 11: `Design.Alignment.Question → Design.Enrichment.Discussion → Design.Consolidation` → `Alignment.Question:How → Alignment.Discussion:How → Alignment.Consolidation:How`
  - line 24-28 agent chain: `conceptual.designer.agent` → `What.Design` phase language, `Design.Session` → `What.Design.Session`, "minimal re-alignment discussion" → `Alignment.Loop:Exec (light)`

### 001.Renames

- `001-ontology.md` updates:
  - `Session.Runtime.Loop` → `Alignment.Loop`, point to new general note (e.g. `126-Alignment.Session.md`)

### hugentics-designer.SKILL.Renames

- `skills/hugentics-designer/SKILL.md` updates:
  - frontmatter + intro: `Design.Session` → `What.Design.Session`
  - `first phase` → `What.Design phase`
  - loop steps: `Design.Alignment.Question → Design.Enrichment.Discussion → Design.Consolidation` → `Alignment.Question:What → Alignment.Discussion:What → Alignment.Consolidation:What`
  - `Session.Runtime.Loop` → `Alignment.Loop:What`
  - `InChat.Design.Session` → `Alignment.Backend:InChat:What`
  - `Artifact.Design.Session` → `Alignment.Backend:Artifact:What`
  - `User.Assistant.Turn` → `Alignment.User.Turn`
  - `Session.Maintenance.Turn` → `Alignment.Maintenance.Turn`
  - general pattern reference: point to `agentos-hugentics` (not index notes — skills are Public.Surfaces, index notes are Local.Surfaces)

### hugentics-impl-designer.SKILL.Renames

- `skills/hugentics-impl-designer/SKILL.md` updates:
  - frontmatter: `Impl.Alignment.Loop` → `Alignment.Loop:How`
  - `second phase` → `How.Design phase`
  - `Impl.Alignment.Loop` → `Alignment.Loop:How`
  - `Session.Runtime.Loop` → `Alignment.Loop` (general reference)
  - `Impl.Alignment.Question` → `Alignment.Question:How`
  - `Impl.Enrichment.Discussion` → `Alignment.Discussion:How`
  - `Impl.Consolidation` → `Alignment.Consolidation:How`
  - `design session` / `Design.Session` → `What.Design.Session`
  - `fundamentals design` → `What.Design`

## Execution.Plan

### Index Notes

1. `notes/index/121-Design.Session.md`
2. `notes/index/123-Impl.Req.md`
3. `notes/index/001-ontology.md`

### Skill SKILL.md Files

4. `skills/hugentics-designer/SKILL.md`
5. `skills/hugentics-impl-designer/SKILL.md`
6. `skills/hugentics-impl-executer/SKILL.md`

### Skill Reference Files (hugentics-designer/references/)

7. `references/session-runtime.md`
8. `references/interview.md`
9. `references/discussion.md`
10. `references/inchat-session.md`
11. `references/artifact-session.md`
12. `references/artifact.md`
13. `references/design-index.md`
14. `references/session-interruptions.md`
15. `references/consolidation-plan-example.md`

### New Files (potential)

16. New index note for general `Alignment.Session` concepts (e.g. `126-Alignment.Session.md`)
17. New/updated harness reference at `agentos-hugentics/references/`

## Impl.Log

(to be filled during execution)
