# Alignment.Session Terminology Migration — Impl.Req

## Impl.Abstract

- scope: migrate old alignment/session terminology across index notes and skills to the new Alignment.Session model
- source: design-session 523, block `Alignment.Session.Design`
- status: complete
- target surfaces: `agentos-md` index notes and skills

## Impl.Index

### Alignment.Session.New

- `Alignment.Session` is a shallow container — "when these concepts run together in a session, that's an Alignment.Session"
- no behavioral protocol of its own
- lists and relates the general concepts: `Conceptual.Space`, `Alignment.Hugentic.Axis`, `Alignment.Agentic.Axis`, `Alignment.Loop`, `Alignment.User.Turn`, `Alignment.Maintenance.Turn`, `Alignment.Backend`
- each workflow specialization defines its own Hugentic.Axes and behavioral detail

### Phase.Semantic.Roots

- `What.Design` — phase 1, working on the conceptual model (was `Fundamentals Design`)
- `How.Design` — phase 2, planning the path (was `Implementation Design`)
- `Impl.Exec` — phase 3, walking the path (was `Implementation Execution`)

### Terminology.Map

- `Design.Session` → `What.Design.Session`
- `Session.Runtime.Loop` → `Alignment.Loop` (general) / `Alignment.Loop:What` (design specialization)
- `Design.Alignment.Question` → `Alignment.Question:What`
- `Design.Enrichment.Discussion` → `Alignment.Discussion:What`
- `Design.Consolidation` → `Alignment.Consolidation:What`
- `User.Assistant.Turn` → `Alignment.User.Turn`
- `Session.Maintenance.Turn` → `Alignment.Maintenance.Turn`
- `InChat.Design.Session` / `InChat.Session` → `Alignment.Backend:InChat:What`
- `Artifact.Design.Session` / `Artifact.Session` → `Alignment.Backend:Artifact:What`
- `Design.Alignment.Core` → `Alignment.Hugentic.Axis:What`
- `Impl.Alignment.Loop` → `Alignment.Loop:How`
- `Impl.Alignment.Question` → `Alignment.Question:How`
- `Impl.Enrichment.Discussion` → `Alignment.Discussion:How`
- `Impl.Consolidation` → `Alignment.Consolidation:How`
- `Realignment.Loop` → `Alignment.Loop:Exec` (light)
- `Realignment.Question` → `Alignment.Question:Exec`
- `Realignment.Discussion` → `Alignment.Discussion:Exec`
- `Realignment.Consolidation` → `Alignment.Consolidation:Exec`
- `Alignment.Space` → `Conceptual.Space` (primary), `Alignment.Space` (synonym)
- `Alignment.Focus` → `Alignment.Hugentic.Axis`

### Surface.Constraint

- skills are Public.Surfaces, index notes are Local.Surfaces
- skills reference other skills, not index notes
- general pattern in skills: point to `agentos-hugentics`, not `127-Alignment.Session.md`

## Execution.Plan

### Slice 1: New files

1. `notes/index/127-Alignment.Session.md` — shallow container index note
2. `skills/agentos-hugentics/references/alignment-session.md` — public surface mirror

### Slice 2: Index notes

3. `notes/index/121-Design.Session.md` — rename all four blocks + internal references per Terminology.Map
4. `notes/index/123-Impl.Req.md` — update loop step names and agent chain language
5. `notes/index/001-ontology.md` — `Session.Runtime.Loop` → `Alignment.Loop`
6. `notes/index/000-index.md` — update entries if block names changed in 121

### Slice 3: Skill SKILL.md files

7. `skills/hugentics-designer/SKILL.md` — full terminology update + point to `agentos-hugentics` for general pattern
8. `skills/hugentics-impl-designer/SKILL.md` — terminology update per Terminology.Map
9. `skills/hugentics-impl-executer/SKILL.md` — terminology update per Terminology.Map

### Slice 4: Skill reference files (hugentics-designer/references/)

10. `references/session-runtime.md` → rename to `references/alignment-loop.md`, full terminology update
11. `references/interview.md` — terminology update + `Alignment.Space` → `Conceptual.Space`
12. `references/discussion.md` — `Session.Maintenance.Turn` → `Alignment.Maintenance.Turn`
13. `references/inchat-session.md` → rename to `references/backend-inchat.md`, full terminology update
14. `references/artifact-session.md` → rename to `references/backend-artifact.md`, full terminology update
15. `references/artifact.md` — `Artifact.Session` → `Alignment.Backend:Artifact:What`
16. `references/design-index.md` — backend terminology update
17. `references/session-interruptions.md` — backend terminology update
18. `references/consolidation-plan-example.md` — backend terminology update

### Slice 5: Harness presentation skill

19. `skills/agentos-hugentics/SKILL.md` — update workflow map table phases + add `Alignment.Session` to related concepts

## Impl.Log

- status: complete
- deviation: `126-Alignment.Session.md` → `127-Alignment.Session.md` (126 was taken by `Chatlas.Query.md`)
- Slice 1: created `127-Alignment.Session.md` (index note) + `agentos-hugentics/references/alignment-session.md` (public surface)
- Slice 2: updated `121-Design.Session.md` (4 blocks renamed), `123-Impl.Req.md` (loop terminology), `001-ontology.md` (5 entries rewritten + Alignment.Session added), `000-index.md` (121 entry updated + 127 added)
- Slice 3: updated `hugentics-designer/SKILL.md` (full rewrite), `hugentics-impl-designer/SKILL.md` (Impl.Alignment.Loop → Alignment.Loop:How), `hugentics-impl-executer/SKILL.md` (Realignment → Alignment.Loop:Exec)
- Slice 4: renamed `session-runtime.md` → `alignment-loop.md`, `inchat-session.md` → `backend-inchat.md`, `artifact-session.md` → `backend-artifact.md`; updated `interview.md`, `discussion.md`, `artifact.md`, `design-index.md`, `session-interruptions.md`, `consolidation-plan-example.md`
- Slice 5: updated `agentos-hugentics/SKILL.md` (phase names, artifact table, added Alignment.Session to related concepts)
