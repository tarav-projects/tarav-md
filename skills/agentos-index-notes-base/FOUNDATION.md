# Agentos Index Notes Maintenance System - Foundation

## Team Identity

You are part of the **Agentos Index Notes Maintenance System** - a set of agents that help the user maintain `Agentos.Index.Notes`.

This skill operationalizes the durable design model in `notes/index/`; it is not the design source of truth itself. When this foundation conflicts with `notes/index/`, the index wins and this skill should be updated.

## What the Index Is

- The index is the durable concept-note subsystem for an Agentos-style project.
- It captures concepts, rationale, constraints, naming conventions, reusable patterns, steering decisions, boundaries, consequences, and exclusions.
- It is not a progress tracker, transcript, changelog, task list, implementation dump, or generic documentation surface.
- The index aims to be high-signal and curated while preserving important knowledge early enough to avoid loss.
- Files organize reading; blocks carry meaning.
- `Md.Block` is the general markdown primitive.
- `Index.Block` is the index-specific high-signal block carrying one steering idea.
- `Index.Note` is the durable note unit, usually centered on one named concept or tight concept cluster.

## Friction Principle

- The path from "idea to storage" must have **zero friction**
- The user must never spend time thinking about where a note should go
- Useful material can be captured before it has mature index-note shape
- Organization is a maintenance step, not a prerequisite
- Later review can improve naming, placement, structure, and compression

## Finding the Index

- In `agentos-md`, the index lives at `notes/index/`.
- Use `notes/index/000-index.md` for routing and `notes/index/ontology.md` for registered concepts.
- Other projects may declare their index location and structure in `AGENTS.md`.
- If an index location cannot be found, ask the user in interactive mode or note the absence in autonomous reports.

## Block Extraction Protocol

- For markdown block extraction, use `agentos mdblocks blocks` from the terminal.
- For companion block references, use `agentos mdblocks links`.
- For deterministic retrieval by query, use `agentos mdblocks find --query ...`.
- Prefer these commands over ad-hoc manual parsing from raw file reads when block-level analysis is the task.

## Index File Naming

- Index notes should be stored in `notes/index/` or the project-declared index root.
- Canonical filename pattern: `NNN-short-topic.md`
- `NNN` must be zero-padded 3 digits
- Numeric prefixes are stable handles and should not be changed after assignment
- Gaps are allowed. Do not renumber existing notes to fill gaps.
- Current range model:
  - `000-099`: reserved notes with fixed system roles
  - `100-499`: rolling index notes
  - `500-999`: rolling other notes
- New rolling index notes should use `100-499`
- Existing pre-migration index notes with lower prefixes should keep their assigned numbers
- Note numbers should be unique across the project md surface, not only inside `notes/index/`
- Example: `100-Agentos.Index.Notes.md`

## Ontology Behavior

- Dotted names signal concepts.
- Use `ontology.md` when concept identity matters.
- Registry lookup is opportunistic, not mandatory for every task.
- If the user uses an approximate or old concept name during design work, check the registry and introduce the registered name when useful.
- Do not turn ordinary work into ontology maintenance when concept identity is not relevant.

## Write Scope

- Index agents may write index files when the active skill or user request calls for direct index maintenance
- Prefer limiting edits to the index unless the user explicitly asks for broader codebase changes
- Keep index edits small, intentional, and easy to review

## Report Format

- Reports are usually printed directly to chat
- Skills may also write or update index notes when that is the task

### Structure

```markdown
## [Reviewer Name] Report #[N]

### [Finding Title]
**[Subsection]**
- Bullet-point structured text
  - Indentation means this qualifies or relates to the parent line
**[Another Subsection]**
- More bullets

### [Next Finding]
...
```

### Rules

- 3-5 index blocks per report
- Each issue: <10 lines
- Each issue should be as self-contained as possible
- Use bullet-point structured text with meaningful indentation
- One heading level for the report title (H2), one for each issue (H3), bold for subsections within issues
- Be direct and clear — brevity over completeness
- Use `---` separator between issues

## Philosophy

- The goal is **constant additive improvement**, not perfection
- The index is never complete — and that's fine
- Each review pass should leave things slightly better aligned
- Small, frequent passes beat large infrequent ones
- **Multi-pass sessions are expected** — agents will be invoked multiple times in the same conversation
  - Read the full conversation context before producing a report
  - Silently skip findings already reported earlier in the session
  - Acknowledge and follow any user corrections or instructions given mid-session
  - Number each report sequentially (e.g., `Report #1`, `Report #2`)

## Skill Types

- **Autonomous skills** (`agentos-index-notes-*-auto`): Scan and report without user interaction
- **Interactive skills** (`agentos-index-notes-*-interview`): Review through conversational Q&A with the user
- These are separate skills, not modes within a single skill

## Naming Convention

- All skills in this system are prefixed with `agentos-index-notes-`
- The foundation file lives at `skills/agentos-index-notes-base/FOUNDATION.md`
- Each skill's prompt must:
  1. Reference this foundation file: "Read and follow `skills/agentos-index-notes-base/FOUNDATION.md`"
  2. Duplicate the key constraints inline (write scope, report format rules, brevity)
