---
name: hugentics-impl-executer
description: "impl.executer.agent workflow master — load and execute Impl.Req artifacts through disciplined, incremental implementation. Covers Alignment.Loop:Exec, deviation handling, and execution references."
---

# Hugentics Impl Executer

Workflow master for the `impl.executer.agent` — the third phase of the Hugentic Harness.

Load an `Impl.Req` artifact and execute it through disciplined, incremental implementation. The agent runs a minimal realignment discussion to recover alignment, then implements following `Vertical.Slice` ordering from the `Execution.Plan`.

## Activation

Activate this skill when the user wants to execute an implementation plan or approved `Impl.Req`.

Typical activation phrases include "implement this", "execute the plan", "build this", or an explicit `hugentics-impl-executer` invocation.

Do not use for exploratory design (use `hugentics-designer`), debugging, or open-ended refactoring.

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

- **`agentos-pkg`** — workflow-neutral Agentos package orientation. Load when working inside an Agentos project.
- **`agentos-index`** — index-grounded context and index functions. Load when the task needs index research, writing, diagnosis, testing, or maintenance.


## Alignment.Loop:Exec

Before execution, the agent runs a minimal re-alignment discussion to recover/double-check alignment:

- `Alignment.Question:Exec` — review the `Impl.Index`, check understanding, surface ambiguities
- `Alignment.Discussion:Exec` — discuss final touches, clarify constraints, resolve open questions
- `Alignment.Consolidation:Exec` — update `Impl.Req` with adjustments, then proceed to execution

The `Alignment.Loop:Exec` is lighter than the full `Alignment.Loop:How` — it is a recovery check, not a full design pass.

### Alignment.Mode

This skill respects the caller's `Alignment.Mode` (see `agentos-hugentics/references/alignment-session.md`). Default is `Interactive`.

- `Interactive` — at each declared `Alignment.Checkpoint` the agent may prompt the user (the plan-confirmation and deviation checkpoints below).
- `Autonomous` — no prompting; the agent resolves every checkpoint itself and executes slices end-to-end.

A caller wanting "one confirm at the `Impl.Req` boundary, then hands-off execution" provides that confirmation at its own boundary checkpoint and invokes this skill in `Autonomous`.

Deviation contract is set by mode (see [Deviation Handling](#3-deviation-handling)).

## Git Checkpoint

Before the first implementation edit, create a mandatory git checkpoint so the entire execution has a rollback floor.

- If the worktree is dirty, commit all existing changes so the checkpoint captures the repo exactly as found.
- When rational boundaries are clear, divide the existing changes into multiple coherent commits with accurate messages.
- When boundaries are ambiguous, use one explicit checkpoint commit rather than guessing at the history.
- If the worktree is clean, create an empty checkpoint commit so the rollback point is still explicit.
- Use a clear message such as `chore: checkpoint before hugentics-impl-executer` (callers may override the message — e.g. `chore: checkpoint before hugentics-codebase-cleaner`).
- If the repo is not a git repo, has unresolved conflicts, or the checkpoint cannot be completed, stop and surface the blocker before any implementation edits.

The checkpoint is required regardless of `Alignment.Mode`. It is the only commit phase in this workflow: after implementation begins, do not create or suggest commits during per-slice execution or at completion. This rule overrides generic commit preferences in the loaded references. Mention the checkpoint commit or commits in the completion summary so the user has a clear rollback handle.

## Core Workflow

### 1. Orientation

Before writing code:

- Load recommended skills based on the task context.
- If the input is an `Impl.Req`, re-read it now. Treat any previous read as potentially stale.
- Run the realignment loop, scaled by `Alignment.Mode`.
- Restate what is being implemented in design-level prose.
- Read existing code in the target area. Understand what is already there.
- The plan confirmation is a declared `Alignment.Checkpoint`: in `Interactive`, confirm the plan with the user before coding; in `Autonomous`, the caller's invocation is the authorization — proceed.

Then run `Alignment.Checkpoint:Executable` — read the `Impl.Req` cold and confirm it is still executable here and now:

- the files, modules, and symbols it targets still exist
- the named feedback loops and `RED.GREEN.Test.Suite` checks are runnable in this environment
- the current code still matches what the plan assumes — no drift since the `Impl.Req` was written
- the plan is followable without the original design chat

If something is off, treat it as a gap: resolve it yourself where you can (re-read, locate moved code, adjust a command); under `Alignment.Mode:Interactive` raise unresolved mismatches to the user before editing; under `Autonomous` record in `Impl.Log` and proceed only if you can do so faithfully, aborting if the plan is no longer executable. This is a light "still executable?" gate, not a re-run of the designer's `Alignment.Checkpoint:Readiness` check.

- Create the [Git Checkpoint](#git-checkpoint) before the first implementation edit. Mandatory in all modes.

### 2. Per-Slice Execution

Follow `Vertical.Slice` ordering from `Execution.Plan`. When the `Impl.Req` calls for a `RED.GREEN.Test.Suite`, drive each covered slice test-first: write the slice's failing test first, then implement to pass — one behavior at a time, never all tests up front. For each slice:

1. **Read** the target files.
2. **Test — RED.** For a slice the `RED.GREEN.Test.Suite` covers, write the failing behavior test first and confirm it fails for the right reason. Skip only where the plan marks the slice as untested.
3. **Implement — GREEN.** Write the minimal change to pass.
4. **Verify** no unintended side effects (check scope of changes); existing tests still pass — `No.Regression.Tests.Allowed` still applies, no regression-test slop.
5. **Report** brief status: what was done, what is next.
6. **Update** `Impl.Log` with deviations, decisions made in open space, and blockers. Do not record what changed in code — that is in the diff.

Leave all implementation changes uncommitted for user review.

### 3. Deviation Handling

Design-reality mismatch is a declared `Alignment.Checkpoint` with the activation condition "design did not fit reality" — not an ad-hoc halt. When it fires, the response depends on `Alignment.Mode`:

- `Interactive` — **stop.** Flag the deviation to the user with a concrete description of the mismatch. Propose options: adjust the design, adjust the implementation, or revisit in a design session. Wait for user direction before continuing.
- `Autonomous` — record the deviation in `Impl.Log` and continue with the most faithful corrective action. Abort only on hard failure (cannot proceed without external input). Surface all deviations in the completion summary.

In all modes: do not silently adapt. The `Impl.Log` is the audit trail.

### 4. Completion

After all slices are done:

- Brief summary of what was built.
- List any deviations encountered and how they were resolved.
- Note anything deferred or left for follow-up.
- Update `Impl.Req` state and append to `Impl.Log` — record only deviations from the plan, decisions made in open space, and blockers. If it is visible in the git diff, it does not belong in the log.
- Cite concrete files, notes, or surfaces when relevant.
- Distinguish clearly between accepted decisions, open questions, and out-of-scope items.
- Confirm the `RED.GREEN.Test.Suite` is green and the existing suite still passes.
- Apply `No.Legacy.Allowed` — clean up dead code, outdated artifacts, misleading docs.
- Report the checkpoint commit or commits. Do not commit or suggest committing the completed implementation.

## Core Principles

- **Work from the plan.** Follow the agreed execution order. Do not reorder or skip without user approval.
- **Small, verifiable slices.** Each slice should be independently reviewable and testable.
- **Test-first where the suite calls for it.** Build the `RED.GREEN.Test.Suite` red-then-green, one behavior at a time; never all tests up front. `No.Regression.Tests.Allowed` and `Test.At.Boundaries` still govern which tests exist and what they assert.
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
