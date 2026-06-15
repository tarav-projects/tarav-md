---
name: agentos-design-implementation
description: Guide disciplined implementation of a design or plan. Auto-loads when asked to implement a converged design, build from a spec, or execute a plan. Pairs with agentos-design-session.
---

# Design Implementation

Translate a design or plan into code through disciplined, incremental execution.

## Trigger Boundary

Use this skill when:

- The user says "implement", "build this", "let's build it", "execute the plan", or similar.
- A converged design from `agentos-design-session` is being acted on.
- The user provides a clear spec or plan and asks for implementation.

Do not use it for exploratory design (use `agentos-design-session`), debugging, or open-ended refactoring.

## References

This skill separates orchestration (this file) from knowledge (reference files).

### Loading rules

- **Always load:** all `references/general-*.md` files. These contain universal practices and preferences.
- **Load by context:** other reference files based on the task at hand.
  - `references/language-*.md` — load when working in the matching language (detect from file extensions in the target area).
  - `references/pattern-*.md` — load when the task matches the pattern domain (CLI, API, data model, UI, etc.).

### Adding references

To extend this skill, add a new file under `references/` and document its loading condition here. Keep each reference file short and opinionated — a curated list, not a tutorial.

## Recommended Skills

Load these before starting implementation work:

- **`agentos-pkg`** — minimal Agentos orientation (CLI, skills, index routing). Load when working inside an Agentos project.
- **`agentos-index-activate`** — activates the index runtime so you ground on project concepts. Load when the project has `notes/index/`.
- **`agentos-artifact-impl-req`** — understands impl-req format. Load when the input is an impl-req.
- **`agentos-artifact-design-summary`** — understands design-summary format. Load when the input is a design summary.

These are recommendations, not hard requirements. Use judgment — skip what's clearly irrelevant to the current task.

## Core Workflow

### 1. Orientation

Before writing code:

- Load recommended skills (see above) based on the task context.
- If the input is an `impl-req` or `design-summary` artifact, re-read it now. Treat any previous read as potentially stale.
- Restate what is being implemented in design-level prose. Do not print code during the understanding step.
- Read existing code in the target area. Understand what is already there.
- Propose a chunked execution order: small, independently verifiable units of work.
- Confirm the plan with the user before coding.

### 2. Per-Chunk Execution

For each chunk:

1. **Read** the target files.
2. **Implement** the change.
3. **Verify** no unintended side effects (check scope of changes).
4. **Report** brief status: what was done, what is next.
5. **Commit checkpoint** — suggest a commit per the repo's commit policy.

### 3. Deviation Handling

If the implementation reveals that the design does not fit reality:

- **Stop.** Do not silently adapt or invent workarounds.
- Flag the deviation to the user with a concrete description of the mismatch.
- Propose options: adjust the design, adjust the implementation, or revisit in `agentos-design-session`.
- Wait for user direction before continuing.

### 4. Completion

After all chunks are done:

- Brief summary of what was built.
- List any deviations encountered and how they were resolved.
- Note anything deferred or left for follow-up.

## Core Principles

- **Work from the plan.** Follow the agreed execution order. Do not reorder or skip phases without user approval.
- **Small, verifiable chunks.** Each chunk should be committable and testable on its own.
- **Read before writing.** Always understand existing code before modifying it.
- **No gold-plating.** Implement what the design says. No bonus features, no speculative abstractions, no "while I'm here" refactors.
- **Surface deviations early.** Do not silently adapt when something does not match the plan.
- **Staleness check.** Re-read source artifacts before acting. If the artifact changed since your earlier read, surface the difference before coding.
- **Load and follow references.** The `references/` files contain accumulated best practices — read and apply them.

## Evidence Priority

When interpreting what to implement, use this priority:

1. The user's current explicit directions.
2. Confirmed understanding from the current discussion.
3. The source artifact (`impl-req`, `design-summary`, or spec).
4. Current codebase state, diffs, and referenced surfaces.

If these conflict, newer explicit user direction wins. If the codebase appears to have drifted from the source artifact, surface that before coding.

## Handoff Standards

- Cite concrete files, notes, or code surfaces when relevant.
- Distinguish clearly between accepted decisions, open questions, and out-of-scope items.
- If the implementation consumed an `impl-req`, update it after execution (see `agentos-artifact-impl-req`).

## Interaction Model

- Keep updates brief. Status after each chunk, not running commentary.
- If the user starts questioning the design mid-implementation, suggest switching back to `agentos-design-session` rather than redesigning inline.
- Flag blockers immediately rather than guessing around them.

## Example Prompts That Should Trigger This Skill

- "implement it"
- "build this"
- "let's implement the design"
- "execute the plan"
- "start building"

## Exit Condition

Exit this skill when implementation is complete, or when the user switches to design discussion, debugging, or a different task.
