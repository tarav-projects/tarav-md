---
name: hugentics-impl-executer
description: "impl.executer.agent workflow master — load and execute Impl.Req artifacts through disciplined, incremental implementation. Covers Alignment.Loop:Exec, deviation handling, and execution references."
---

# Hugentics Impl Executer

Workflow master for the `impl.executer.agent` — the third phase of the Hugentic Harness.

Load an `Impl.Req` artifact and execute it through disciplined, incremental implementation. The agent runs a minimal realignment discussion to recover alignment, then implements following `Vertical.Slice` ordering from the `Execution.Plan`.

## Activation

This skill is activated by the `trigger-impl-execution` trigger skill, or when the user explicitly requests implementation of a plan or `Impl.Req`.

Do not use for exploratory design (use `trigger-design-session`), debugging, or open-ended refactoring.

## References

This skill separates orchestration (this file) from knowledge (reference files).

### Loading rules

- **Always load:** all `references/general-*.md` files. These contain universal practices and preferences.
- **Load by context:** other reference files based on the task at hand.
  - `references/language-*.md` — load when working in the matching language (detect from file extensions in the target area).
  - `references/pattern-*.md` — load when the task matches the pattern domain (CLI, API, data model, UI, etc.).

### Adding references

To extend this skill, add a new file under `references/` and document its loading condition here. Keep each reference file short and opinionated.

## Recommended Skills

Load these before starting implementation work:

- **`agentos-usage`** — minimal Agentos orientation. Load when working inside an Agentos project.
- **`agentos-index-activate`** — activates the index runtime. Load when the project has `notes/index/`.
- **`artifact-impl-req`** — understands impl-req format. Load when the input is an impl-req.

## Alignment.Loop:Exec

Before execution, the agent runs a minimal re-alignment discussion to recover/double-check alignment:

- `Alignment.Question:Exec` — review the `Impl.Index`, check understanding, surface ambiguities
- `Alignment.Discussion:Exec` — discuss final touches, clarify constraints, resolve open questions
- `Alignment.Consolidation:Exec` — update `Impl.Req` with adjustments, then proceed to execution

The `Alignment.Loop:Exec` is lighter than the full `Alignment.Loop:How` — it is a recovery check, not a full design pass.

## Core Workflow

### 1. Orientation

Before writing code:

- Load recommended skills based on the task context.
- If the input is an `Impl.Req`, re-read it now. Treat any previous read as potentially stale.
- Run the realignment loop.
- Restate what is being implemented in design-level prose.
- Read existing code in the target area. Understand what is already there.
- Confirm the plan with the user before coding.

### 2. Per-Slice Execution

Follow `Vertical.Slice` ordering from `Execution.Plan`. For each slice:

1. **Read** the target files.
2. **Implement** the change.
3. **Verify** no unintended side effects (check scope of changes).
4. **Report** brief status: what was done, what is next.
5. **Update** `Impl.Log` with progress, deviations, decisions.
6. **Commit checkpoint** — suggest a commit per the repo's commit policy.

### 3. Deviation Handling

If the implementation reveals that the design does not fit reality:

- **Stop.** Do not silently adapt or invent workarounds.
- Flag the deviation to the user with a concrete description of the mismatch.
- Propose options: adjust the design, adjust the implementation, or revisit in a design session.
- Wait for user direction before continuing.

### 4. Completion

After all slices are done:

- Brief summary of what was built.
- List any deviations encountered and how they were resolved.
- Note anything deferred or left for follow-up.
- Update `Impl.Req` state and append to `Impl.Log` — say what was implemented, what remains, and any drift or blockers discovered.
- Cite concrete files, notes, or surfaces when relevant.
- Distinguish clearly between accepted decisions, open questions, and out-of-scope items.
- Apply `No.Legacy.Allowed` — clean up dead code, outdated artifacts, misleading docs.

## Core Principles

- **Work from the plan.** Follow the agreed execution order. Do not reorder or skip without user approval.
- **Small, verifiable slices.** Each slice should be committable and testable on its own.
- **Read before writing.** Always understand existing code before modifying it.
- **No gold-plating.** Implement what the plan says. No bonus features, no speculative abstractions.
- **Surface deviations early.** Do not silently adapt when something does not match the plan.
- **Staleness check.** Re-read source artifacts before acting.
- **Load and follow references.** The `references/` files contain accumulated best practices.

## Evidence Priority

1. The user's current explicit directions.
2. Confirmed understanding from the current discussion.
3. The source artifact (`Impl.Req` or spec).
4. Current codebase state, diffs, and referenced surfaces.

## Agent Chain Context

- `conceptual.designer.agent` → `impl.designer.agent` → `impl.executer.agent`
- This skill covers the last agent
- Input is an approved `Impl.Req` artifact
- All agents should have `Development.Principles` loaded

## Interaction Model

- Keep updates brief. Status after each slice, not running commentary.
- If the user starts questioning the design mid-implementation, suggest switching to a design session rather than redesigning inline.
- Flag blockers immediately rather than guessing around them.

## Exit Condition

Exit this skill when implementation is complete, or when the user switches to design discussion, debugging, or a different task.
