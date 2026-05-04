---
name: agentos-index-notes-base
description: "Agentos Index Notes System: Shared foundation for index maintenance agents. Use when the user mentions `index-note`, or when creating, updating, or reviewing any `agentos-index-notes-*` skill to enforce system-wide constraints, report format, and naming conventions."
---

# Agentos Index Notes Base

Read and follow `skills/agentos-index-notes-base/FOUNDATION.md` before proceeding.

Use this skill as the operational baseline for all `agentos-index-notes-*` skills.

The durable design source of truth is `notes/index/`, especially:

- `notes/index/100-Agentos.Index.Notes.md`
- `notes/index/ontology.md`
- `notes/index/102-Dotted.Notation.md`

## Workflow

### Phase 1: Load Foundation

1. Read `skills/agentos-index-notes-base/FOUNDATION.md`
2. Treat it as operational guidance derived from `notes/index/`
3. If it conflicts with `notes/index/`, follow the index and report the drift

### Phase 2: Enforce Shared Constraints

1. Apply the foundation as operational guidance for index behavior
2. Allow index-note writes when the active skill or user request calls for direct index maintenance
3. Keep findings and note content concise, structured, and directly actionable

### Phase 3: Align Skill Design

1. Ensure new index skills follow `agentos-index-notes-*` naming
2. Ensure each skill duplicates required key constraints inline
3. Ensure any deviation from the foundation is explicit and justified
