# 644 - The Tara Project: Full Notes Inventory (LIVE)

Status: live / open investigation
Date: 2026-08-31
Scope: locate **every** note, path, and reference about **The Tara Project**
across `~/projects`, `Archive.Attic`, and Git history (including deleted paths).

This is an *evidence inventory*, not design truth. Nothing here is promoted
into `tarav-pkg`. Per `tarav-md/AGENTS.md`, treat all of it as non-authoritative
until deliberately promoted.

---

## 0. Summary of the find

**The Tara Project** is the *predecessor* system to Tarav. It is named after
**Taravangian** (*The Stormlight Archive*) — "the relentless pursuit of perfect
knowledge". Its core idea: a unified protocol (**TaraSON**) + independent
recorders + storage substrate for **contextual data**.

Two documents are the canonical origin statements:

| Note | Path | State |
|---|---|---|
| **The Tara Project** (manifesto) | `~/projects/simuleos-project/simuleos-md/notes/archive/260206/T20251121-The.Taras.Project.md` | ON-DISK |
| **The Tara Project Full Stack** (subsystem spec) | `~/projects/tara-project/tara-project-js/notes/inbox/The.Tara.Project.Full.Stack.md` | ON-DISK |

Counts across all Git repos under `~/projects` (markdown, `tara*` paths,
excluding `tarav*` noise):

- **93** paths still ON-DISK
- **145** paths present only in **Git history** (deleted or renamed)
- **6** distinct project trees hold Tara material
- **83** Claude sessions from the now-deleted original monorepo (subagent
  transcripts only — see note 645)

---

## 1. Primary surface — `~/projects/tara-project/`

The dedicated multi-language home. Four Git repos:

```
~/projects/tara-project/
├── tara-project-specs/   <- THE canonical spec surface (most material)
├── tara-project-js/      <- taralib-js, tara-desktop, tara-stdlib-js, contextor
├── tara-project-dart/    <- tara_mobile, taralib_dart
├── tara-project-py/      <- taralib, tara-stdlib-py, tara-cli
└── _DEPRECATED/tara-mobile-old/
```

### 1.1 `tara-project-specs` — appendix surface (all ON-DISK)

`notes/appendix/` — 33 spec appendices:

```
Tara.App.Home            Tara.Archiving              Tara.Archiving.Stack.Binding
Tara.Artifact.Entry      Tara.Artifact.Entry.Stack.Binding
Tara.Artifact.Ref        Tara.Artifact.Tape          Tara.Class.Resolution
Tara.Data.Principles     Tara.DataClass              Tara.Global.Tapes
Tara.HourglassPrinciple  Tara.Index                  Tara.Index.RepresentationEvolution
Tara.Index.Tapes         Tara.Index.TouchEvent       Tara.Integration.Divergence
Tara.Integration.Ontology  Tara.Ontology.Reference
Tara.Project.Hypotheses  Tara.Project.Overview       Tara.Project.Registry
Tara.Record.Field.Conventions  Tara.Reference.Workflows
Tara.Retention.Principles  Tara.Stack.StdLib         Tara.Stack.Taralib
Tara.Tape                Tara.Tape.Language          Tara.Tape.Project
Tara.Tape.Source         Tara.URI                    Tara.Workflow.App.Pattern
```

Also ON-DISK: `notes/appendix/Git.Integration-appendix.md`,
`notes/appendix/Tape.Universe-appendix.md`,
`notes/appendix/Project.Authority.Resolution-appendix.md`,
`skills/tara-proj-specs/SKILL.md`

`notes/live/` (ON-DISK):
```
500-tara-index-principles.md
501-tara-index-v1-migration-protocol.md
502-tara-index-agentos-implementation-mapping.md
504-tara-index-human-grounding-boundary.md
505-design-discussion-tara-principles-2026-03-07.md
514-tara-tapes-ontology-snapshot.md
516-taralib-internal-layering.md
517-tara-record-field-conventions.md
530-tara-core-spec-surface-redesign.md
```

### 1.2 `tara-project-js` (ON-DISK)

```
notes/inbox/The.Tara.Project.Full.Stack.md      <- KEY
notes/inbox/tara-record.spec.md
notes/inbox/tara-tape.spec.md
notes/index/taraproject.vision.md               <- KEY
notes/index/Tara.Stack.Ideas.1.md
notes/index/Tara.Stack.Ideas.2.md
notes/index/Tara.Stack.Ideas.3.md
notes/index/the.hourglass.principle.md
notes/index/taralib-design-principles.md
notes/index/tara-stdlib-js.md
notes/index/tara-tapes-repo.md
notes/index/tara.record.invariants.md
notes/index/tara-proj-specs-interaction.md
notes/index/000-tara-desktop-control-center.md
notes/index/index.md
notes/live/112-taralib-quality-review.md
notes/live/114-contextor-bootstrap-plan.md
notes/live/500-tara-control-center-discovery-model.md
notes/live/501-control-center-inventory-archive-action.md
notes/live/505-tara-stdlib-js-split-plan.md
notes/live/archive/101-plan.md
notes/live/archive/102-plan.md
notes/live/archive/102-plan-prompt.md
notes/live/archive/107-tara-vscode-ext-seed-prompt.md
notes/live/archive/108-tarastack-design-plan.md
notes/live/archive/109-tara-model-report.md
notes/live/archive/110-tara-stack-vs-base.md
apps/tara-desktop/AGENTS.md
apps/tara-desktop/README.md
apps/tara-desktop/notes/index/001-Tara.Integration.Ontology.md
apps/tara-desktop/notes/live/500-tara-desktop-architecture.md
apps/tara-desktop/notes/live/501-tara-explorer-design.md
apps/tara-desktop/notes/live/502-tara-mobile-sync-subsystem.md
apps/tara-desktop/notes/live/503-tara-mobile-sync-implementation-plan.md
apps/tara-desktop/notes/live/504-auto-puller-trivia-spaced-repetition.md
apps/vscode-tara-puller-extenssion/AGENTS.md
packages/taralib-js/README.md
packages/tara-contextor-ts/README.md
packages/tara-stdlib-js/notes/live/500-recording-buffer-and-mark-plan.md
packages/taralib-js/src/stack/global/managers/home-manager.ts   (code ref)
```

### 1.3 `tara-project-dart` (ON-DISK)

```
apps/tara_mobile/AGENTS.md
apps/tara_mobile/README.md
apps/tara_mobile/notes/index/000-artifact-ref.md
apps/tara_mobile/notes/live/500-tara-mobile-setup-guide.md
apps/tara_mobile/notes/live/501-tara-mobile-workflow-architecture.md
apps/tara_mobile/notes/live/502-notes-inline-workflow-mvp.md
apps/tara_mobile/notes/live/503-notes-inline-camera-artifact-plan.md
apps/tara_mobile/notes/live/504-notes-inline-tag-tape-system.md
apps/tara_mobile/notes/live/505-notes-inline-layout-refactor.md
apps/tara_mobile/notes/live/506-notes-inline-machine-system-design.md
notes/live/000-tara-mobile-old-git-history.md
packages/taralib_dart/notes/live/500-stdlib-dart-update-plan-2026-04-05.md
_DEPRECATED/tara-mobile-old/notes/live/500-tara-mobile-setup-guide.md
_DEPRECATED/tara-mobile-old/notes/live/501-tara-mobile-workflow-architecture.md
```

### 1.4 `tara-project-py` (ON-DISK)

```
notes/index/001-Tara.Integration.Ontology.md
```

---

## 2. Origin surface — `simuleos-project` (ON-DISK)

The Tara Project was *born* in Simuleos notes, Nov 2025:

```
simuleos-md/notes/archive/260206/T20251121-The.Taras.Project.md          <- MANIFESTO
simuleos-md/notes/archive/260206/T20251123-The.Tara.Kernel.Model.md      <- KERNEL MODEL
simuleos-md/notes/archive/260206/T20251120-Taravangian.note.md           <- NAME ORIGIN
simuleos-md/notes/archive/260206/T20251121-ContextRecord.kernel.md
simuleos-md/notes/archive/260206/T20251121-conceptual.map.kernel.md
simuleos-md/notes/archive/260206/T20251121-what.is.an.issue.kernel.md
simuleos-md/notes/archive/260206/T20251121-Two.dimemsions.of.contextuality.md
simuleos-md/notes/archive/260206/T20251122-git.integration.md
simuleos-md/notes/archive/260206/T20251123-Layered.Architecture.md
simuleos-md/notes/archive/260206/T20251123-notes.md
simuleos-md/notes/archive/260206/T20251119-design.notes.md
simuleos-md/notes/archive/260206/T20251104-context-record.md
simuleos-md/notes/archive/260206/T20251105-design.notes.md
simuleos-md/notes/live/601-tapes-raw-query-design.md
simuleos-md/skills/simuleos-pkg/appendix/Tara.Integration.Ontology-appendix.md
```

All under Git commit `8b169494ce96cb68fe6aebcaf859d6f4b34d9512`.

---

## 3. Downstream / sibling references (ON-DISK)

```
~/projects/FamilyInc-project/IoCapitalist/notes/live/502-tape-integration-roadmap.md
~/projects/spec-surfaces/notes/index/005-naming-dot-notation.md
~/projects/spec-surfaces/notes/index/000-index.md
~/projects/spec-surfaces/skills/spec-surfaces/SKILL.md
~/Documents/workspaces/csc-reactor/csc-reactor-specs/notes/index/core/003-tara-integration-ontology.md
```

### Tarav lineage carriers (ON-DISK)

```
~/projects/taravangian-project/tarav-md/_DEPRECATED/agentos-py-notes-index/002-Tara.Integration.Ontology.md
~/projects/taravangian-project/tarav-py/notes/live/archived/510-tara-tapes-subsystem-plan.md
~/projects/_DEPRECATED/agentos-project/agentos-md/_DEPRECATED/agentos-py-notes-index/002-Tara.Integration.Ontology.md
~/projects/_DEPRECATED/agentos-project/agentos-py.disabled/notes/live/archived/510-tara-tapes-subsystem-plan.md
~/projects/_DEPRECATED/agentos-project/_DEPRECATED/agentos-iterante-py/_DEPRECATED/iterante1/live/migrated-agentos-index/002-Tara.Integration.Ontology.md
```

### Obsidian vault (ON-DISK)

```
~/Documents/Obsidian/notebook/vault/Idea logs - Tara - applications.md
~/Documents/Obsidian/notebook/vault/Week Plan - TaraKernel - 2025.12.20.md
~/Documents/Obsidian/notebook/vault/Assay - My AI Assistant.md      (mentions Tara)
~/Documents/Obsidian/notebook/vault/SourceConcat - context.md       (mentions Tara)
~/Documents/Obsidian/notebook/vault/josePereiro - Desk.md           (mentions Tara)
~/Documents/Obsidian/notebook/vault/Desk - Main -  josePereiro.md   (mentions Tara)
~/Documents/Obsidian/notebook/vault/Tasks001 - Desk - josePereiro.md (mentions Tara)
```

### Older desktop plan notes (ON-DISK)

```
~/Documents/workspaces/main-workspace/notes/live/500-tara-desktop-hello-plan.md
~/Documents/workspaces/main-workspace/notes/live/501-tara-desktop-hello-implementation-plan.md
```

---

## 4. GIT-HISTORY ONLY (deleted from working tree)

These exist **only** in Git objects. Recoverable with
`git show <commit>:<path>`.

### 4.1 `tara-project-js` — the highest-value losses

Repo: `~/projects/tara-project/tara-project-js`

| Path | Recover from |
|---|---|
| `notes-inbox/The.Tara.Project.Full.Stack.md` | `3371d94756c2c72745c89ef169fc7eb8d85f5179` (2026-01-21) |
| `notes-index/taraproject.vision.md` | `3371d94` |
| `notes-index/tarason-fullstack.md` | `5ac945ef267304744c4fee255c26b4d534893428` (2026-01-21) |
| `notes-index/Tara.Stack.Ideas.1.md` | `3371d94` |
| `notes-index/Tara.Stack.Ideas.2.md` | `3371d94` |
| `notes-index/tara-record.spec.md` | `3371d94` |
| `notes-index/tara-tape.spec.md` | `3371d94` |
| `notes-index/taralib-design-principles.md` | `3371d94` |
| `notes-live/107-tara-vscode-ext-seed-prompt.md` | `3371d94` |
| `notes-live/108-tarastack-design-plan.md` | `3371d94` |
| `notes/index/tara-record.spec.md` | in history |
| `notes/index/tara-tape.spec.md` | in history |
| `notes/live/107-tara-vscode-ext-seed-prompt.md` | in history (survives at `notes/live/archive/`) |
| `notes/live/108-tarastack-design-plan.md` | in history (survives at `notes/live/archive/`) |
| `notes/live/109-tara-model-report.md` | `2fec31cfc88a44148d877a00f9a225ad313b574f` (survives at `archive/`) |
| `notes/live/110-tara-stack-vs-base.md` | in history (survives at `archive/`) |
| `apps/tara-desktop/notes/live/501-tape-navigator-design.md` | in history — **no surviving copy** |
| `packages/tara-cli/README.md` | in history |
| `packages/taraproject-cli/README.md` | in history |
| `packages/vscode-tara-puller-extenssion/AGENTS.md` | in history |
| `packages/vscode-tara-puller-001-extenssion/AGENTS.md` | in history |

Note: `notes-inbox/` / `notes-index/` / `notes-live/` was the **pre-migration
flat layout**, later renamed to `notes/inbox/`, `notes/index/`, `notes/live/`.
`Tara.Stack.Ideas.3.md` last appears at `726172b986d98c611161d46f62ce64fc8655ac2d`.

### 4.2 `tara-project-specs` — 118 history-only paths

Repo: `~/projects/tara-project/tara-project-specs`

These are almost entirely **reorganization churn**, not content loss. Three
successive layouts were collapsed into today's `notes/appendix/`:

```
notes/index.stage/{core,stack,supplemental}/...   (staging layout, retired)
notes/index/{core,stack,supplemental}/...         (numbered layout, retired)
notes/index/1NN-tara-*.md                         (flat numbered, retired)
        -> notes/appendix/Tara.*-appendix.md      (current, ON-DISK)
```

Full history-only list (recoverable, all in this repo's Git objects):

```
notes/index.stage/002-tara-ontology.md
notes/index.stage/core/102-tara-hourglass-principle.md
notes/index.stage/core/103-tara-tapes-spec-v0.md
notes/index.stage/core/106-tara-index-spec-v0.md
notes/index.stage/core/107-tara-index-touch-event-spec-v0.md
notes/index.stage/core/108-tara-index-tapes-spec-v0.md
notes/index.stage/core/109-tara-index-representation-evolution-spec-v0.md
notes/index.stage/core/110-tara-git-integration-spec-v0.md
notes/index.stage/core/111-tara-git-refs-spec-v0.md
notes/index.stage/core/112-tara-data-principles.md
notes/index.stage/core/113-tara-retention-principles.md
notes/index.stage/core/114-tara-reference-workflows.md
notes/index.stage/core/115-tara-tape-uri-protocol.md
notes/index.stage/core/116-tara-workflow-app-pattern.md
notes/index.stage/core/117-tara-archiving-spec-v0.md
notes/index.stage/core/119-tara-artifact-entry-spec-v0.md
notes/index.stage/core/121-tara-git-self-hosting-profile-v0.md
notes/index.stage/core/124-tara-tape-source.md
notes/index.stage/core/131-tara-tape-language-spec-v0.md
notes/index.stage/core/132-tara-reliability-by-construction.md
notes/index.stage/core/143-tara-artifact-ref-spec-v0.md
notes/index.stage/core/148-tara-tape-project-spec-v0.md
notes/index.stage/stack/104-tara-dataclass-spec-v0.md
notes/index.stage/stack/105-tara-class-resolution.md
notes/index.stage/stack/118-tara-project-registry.md
notes/index.stage/stack/125-tara-app-home-convention.md
notes/index.stage/stack/126-tara-global-tapes.md
notes/index.stage/stack/140-tara-stack-taralib-spec-v0.md
notes/index.stage/stack/142-tara-stack-stdlib-spec-v0.md
notes/index.stage/stack/144-tara-artifact-tape-spec-v0.md
notes/index.stage/stack/145-tara-record-field-conventions.md
notes/index.stage/stack/146-tara-archiving-stack-binding.md
notes/index.stage/stack/147-tara-artifact-entry-stack-binding.md
notes/index.stage/supplemental/100-tara-project-overview.md
notes/index.stage/supplemental/101-tara-project-hypotheses.md
notes/index.stage/supplemental/127-tara-integration-ontology.md
notes/index.stage/supplemental/133-tara-integration-divergence.md
notes/index/002-tara-ontology.md
notes/index/100-tara-project-overview.md
notes/index/101-tara-project-hypotheses.md
notes/index/102-tara-hourglass-principle.md
notes/index/103-tara-tapes-spec-v0.md
notes/index/104-tara-dataclass-spec-v0.md
notes/index/105-tara-class-resolution.md
notes/index/106-tara-index-spec-v0.md
notes/index/107-tara-index-touch-event-spec-v0.md
notes/index/108-tara-index-tapes-spec-v0.md
notes/index/109-tara-index-representation-evolution-spec-v0.md
notes/index/110-tara-git-integration-spec-v0.md
notes/index/111-tara-git-refs-spec-v0.md
notes/index/112-tara-data-principles.md
notes/index/113-tara-retention-principles.md
notes/index/114-tara-reference-workflows.md
notes/index/115-tara-uri-spec-v0.md
notes/index/116-tara-workflow-app-pattern.md
notes/index/117-tara-archiving-spec-v0.md
notes/index/118-tara-project-registry.md
notes/index/119-tara-artifact-entry-spec-v0.md
notes/index/121-tara-git-self-hosting-profile-v0.md
notes/index/124-tara-tape-source.md
notes/index/125-tara-app-home-convention.md
notes/index/126-tara-global-tapes.md
notes/index/127-tara-integration-ontology.md
notes/index/131-tara-tape-language-spec-v0.md
notes/index/132-tara-reliability-by-construction.md
notes/index/133-tara-integration-divergence.md
notes/index/140-tara-stack-taralib-spec-v0.md
notes/index/142-tara-stack-stdlib-spec-v0.md
notes/index/143-tara-artifact-ref-spec-v0.md
notes/index/144-tara-artifact-tape-spec-v0.md
notes/index/145-tara-record-field-conventions.md
notes/index/146-tara-archiving-stack-binding.md
notes/index/147-tara-artifact-entry-stack-binding.md
notes/index/148-tara-tape-project-spec-v0.md
notes/index/core/102-tara-hourglass-principle.md
notes/index/core/103-tara-tapes-spec-v0.md
notes/index/core/104-tara-dataclass-spec-v0.md
notes/index/core/105-tara-class-resolution.md
notes/index/core/106-tara-index-spec-v0.md
notes/index/core/107-tara-index-touch-event-spec-v0.md
notes/index/core/108-tara-index-tapes-spec-v0.md
notes/index/core/109-tara-index-representation-evolution-spec-v0.md
notes/index/core/110-tara-git-integration-spec-v0.md
notes/index/core/111-tara-git-refs-spec-v0.md
notes/index/core/112-tara-data-principles.md
notes/index/core/113-tara-retention-principles.md
notes/index/core/114-tara-reference-workflows.md
notes/index/core/115-tara-tape-uri-protocol.md
notes/index/core/116-tara-workflow-app-pattern.md
notes/index/core/117-tara-archiving-spec-v0.md
notes/index/core/119-tara-artifact-entry-spec-v0.md
notes/index/core/119-tara-artifact-ref-spec-v0.md
notes/index/core/121-tara-git-self-hosting-profile-v0.md
notes/index/core/124-tara-tape-source.md
notes/index/core/131-tara-tape-language-spec-v0.md
notes/index/core/132-tara-reliability-by-construction.md
notes/index/core/143-tara-artifact-ref-spec-v0.md
notes/index/core/148-tara-tape-project-spec-v0.md
notes/index/stack/104-tara-dataclass-spec-v0.md
notes/index/stack/105-tara-class-resolution.md
notes/index/stack/118-tara-project-registry.md
notes/index/stack/125-tara-app-home-convention.md
notes/index/stack/126-tara-global-tapes.md
notes/index/stack/140-tara-stack-taralib-spec-v0.md
notes/index/stack/142-tara-stack-stdlib-spec-v0.md
notes/index/stack/144-tara-artifact-tape-spec-v0.md
notes/index/stack/145-tara-record-field-conventions.md
notes/index/stack/146-tara-archiving-stack-binding.md
notes/index/stack/147-tara-artifact-entry-stack-binding.md
notes/index/supplemental/100-tara-project-overview.md
notes/index/supplemental/101-tara-project-hypotheses.md
notes/index/supplemental/127-tara-integration-ontology.md
notes/index/supplemental/133-tara-integration-divergence.md
```

**Specs with no surviving `notes/appendix/` equivalent** (real candidates for
recovery — content may only exist in history):

```
110-tara-git-integration-spec-v0.md          -> survives only as Git.Integration-appendix.md
111-tara-git-refs-spec-v0.md                 -> NO appendix equivalent
121-tara-git-self-hosting-profile-v0.md      -> NO appendix equivalent
132-tara-reliability-by-construction.md      -> NO appendix equivalent
002-tara-ontology.md                         -> partially -> Tara.Ontology.Reference-appendix.md
```

### 4.3 Other repos, history-only

```
tarav-md:  notes/index/migrated-agentos-index/002-Tara.Integration.Ontology.md
tarav-md:  notes/live/migrated-agentos-index/002-Tara.Integration.Ontology.md
tarav-py:  notes/index/002-Tara.Integration.Ontology.md
tarav-py:  notes/live/510-tara-tapes-subsystem-plan.md   (survives at notes/live/archived/)
```

---

## 5. Archive.Attic — checked, NO Tara Project deposit

`~/Documents/tarav/attic/deposits/` holds exactly three deposits, **none** of
which is Tara Project material:

| Deposit | UUID | Content |
|---|---|---|
| `20260826T030536Z-chatlas` | `d3d9c3bb-3f13-4058-b52b-29397fd72dab` | legacy Chatlas depot |
| `20260826T213706Z-tarav-skills-reboot` | `e1636df6-0910-40eb-bd64-0aee93b06db2` | pre-reboot `tarav-md/skills` |
| `20260830T134506Z-canvas-system-retirement` | `000fe6c0-de1c-482e-90f5-ece714566a03` | `tarav-canvas-md` + `tarav-canvas-js` |

**Indirect Tara evidence inside the chatlas deposit:** the raw provider
sessions under
`deposits/20260826T030536Z-chatlas/material/archive/20260515T025035Z/raw/`
(`.codex-jp/sessions/`, `.copilot/session-state/`) contain many Tara Project
conversations. These are *chat provenance*, not notes. Per the Attic
boundary rules they are not valid Diagram evidence.

`tarav-hugentics` was inspected: it has **no `--attic` mode**. The Attic
workflow lives in `tarav-pkg --attic`
(`tarav-md/skills/tarav-pkg/references/attic.md`), with
`references/legacy-skill-mine.md` governing the 2026-08-26 skill reboot mine.

---

## 6. Lost / deleted repositories

**`~/Documents/js/taraproject-js-monorepo` — GONE.** The original JS monorepo.
Broken symlink remains at
`~/Documents/workspaces/20260213-obajs/taraproject-js-monorepo`.

**83 Claude sessions** (+2 in the vscode-puller project) are represented at:

```
~/Documents/workspaces/trackagents/depot/claude/projects/
  -Users-pereiro-Documents-js-taraproject-js-monorepo/
  -Users-pereiro-Documents-js-taraproject-js-monorepo-packages-vscode-tara-puller-extenssion/
```

Also in the trackagents depot:

```
~/Documents/workspaces/trackagents/depot/agents/skills/tara-proj-specs/
~/Documents/workspaces/trackagents/depot/agents/skills/tara-track-agents-001/
~/Documents/workspaces/trackagents/depot/claude/tasks/taraproject-js-monorepo-tasks/
```

Caveat (see note 645): these directories hold **subagent transcripts only**
(164 `.jsonl`); the 83 **parent transcripts are absent**, and all 83 sessions
are missing from both Chatlas and Archive.Attic.

This is the single richest **unrecovered** Tara Project source.

---

## 7. Not duplicates (symlinks resolved)

```
~/Documents/workspaces/main-workspace/tara-project -> ~/projects/tara-project
```

---

## 8. Open threads

1. Recover `apps/tara-desktop/notes/live/501-tape-navigator-design.md` — the
   only tara-project-js note with **no surviving working-tree copy**.
2. Recover the four `tara-project-specs` specs with no appendix equivalent
   (§4.2): git-refs, git-self-hosting-profile, reliability-by-construction,
   and the original `002-tara-ontology.md`.
3. Mine the 83 monorepo Claude sessions in the trackagents depot — the
   deleted `taraproject-js-monorepo` exists nowhere else. Coverage analysed
   in note 645: all 83 are absent from Chatlas and from Archive.Attic.
4. Decide whether the Tara Project corpus deserves its own **Archive.Attic
   Deposit**, since it is currently spread across 6 live repos with no
   conservation event.
5. Extract Tara references from the Obsidian vault (7 files) — these are the
   only non-repo-native idea logs.

---

## 9. Reproduce this sweep

```bash
# on-disk, Tara-named markdown (excludes tarav noise)
find ~/projects -iname "*tara*" -name "*.md" \
  -not -path "*/node_modules/*" -not -path "*/.git/*" \
  | grep -viE "/tarav|taravangian"

# git-history sweep across every repo
cd ~/projects
for d in $(find . -maxdepth 3 -name ".git" -type d | grep -v node_modules); do
  r=$(dirname "$d")
  git -C "$r" log --all --pretty=format: --name-only 2>/dev/null \
    | sort -u | grep -iE "tara" | grep -viE "tarav" | grep -iE "\.md$" \
    | while read -r p; do
        [ -f "$r/$p" ] && echo "[ON-DISK] $r/$p" || echo "[GONE] $r/$p"
      done
done

# recover a deleted note
git -C ~/projects/tara-project/tara-project-js \
  show 3371d94:notes-inbox/The.Tara.Project.Full.Stack.md
```

---

## 10. Related

- `645-trackagents-migration-chatlas-coverage.md` — whether the trackagents
  depot sessions (incl. the Tara monorepo) are present in Chatlas.
