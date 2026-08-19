# Tarav2 Migration, Master Plan - impl-req

## Impl.Abstract

- **Status:** Open. Design surface for the whole migration; no step executed from here yet. The index is **frozen** — see `Migration.Freeze`.
- **Kind:** A **master `Impl.Req`** — the same artifact structure at a lower resolution. Its `Execution.Plan` steps are not executable work; each step is *designed here at the general level and emitted as a detailed executer `Impl.Req` child*. Both levels carry a design job: this one over the general picture, the child over its specific topic.
- **Scope:** The convergence of tarav1 onto the tarav2 semantic model across four surfaces — the `tarav` CLI/lib (skw, chatlas, index), the `tarav-pkg` index, the `tarav-hugentics` skill, and the chatlas depot.
- **Out of scope:** canvas, iterante, projects-center, testground, and the remaining package skills. They are not part of this migration and no step here touches them.
- **Predecessors:** `631`–`635` built tarav2; `637` began the reconciliation with `tarav2 index import`. This artifact states the arc those seven imply but never wrote down.
- **Destination in one line:** **a single `tarav` system** — one CLI, one index model, one depot — aligned far enough to run `Test.Block` e2e work. Not fully content-aligned; sufficiently aligned.
- **Acceptance:** every surface below meets its stated destination condition, and no step's outcome rests on a decision still open in `Impl.Log`.
- **Revision:** this plan is expected to change. A child's execution may reveal a problem that modifies it; that is a normal outcome, not a plan failure.

## Impl.Index

### Migration.System.Scope

- [DF] the tarav2 migration system is four surfaces: the tarav CLI/lib carrying skw, chatlas and the index, the tarav-pkg index, the tarav-hugentics skill, and the chatlas depot ^c20260819-0u
- [DC] canvas, iterante, projects-center, testground, and the remaining package skills are out of the migration scope ^c20260819-1u
- [DF] tarav1 names the current live tarav rather than a deprecated fork ^c20260819-2u
- [CT] the tarav-pkg index is both where the new design lands and a surface being migrated to that design ^c20260819-3u
- [DC] landing the new design on tarav-pkg does not require aligning the index content already there ^c20260819-4u
- [CT] the chatlas depot is a live surface actively storing chats, so migrating it may not interrupt storage ^c20260819-5u
- [CT] tarav-hugentics is migrated and reimplemented as a surface in the same way the tarav-pkg index is ^c20260819-6u

****

### Master.Impl.Req

- [DF] the master impl-req is a low-resolution Impl.Req: the same structure at a coarser resolution, carrying its own design part ^c20260819-7u
- [DF] the master impl-req is a desk for planning the big steps and accumulating the tasks against them ^c20260819-11u
- [DC] a master step is designed at the general level and emitted as a detailed executer Impl.Req child ^c20260819-8u
- [DC] both levels carry a design job, the master over the general picture and the child over its specific topic ^c20260819-9u
- [DC] a master step records a pointer to its child artifact rather than a copy of the child's status ^c20260819-12u
- [RJ] a separate progress tracker restating child status is excluded, since the child artifact already carries it ^c20260819-14u
- [DC] what belongs to the master and what belongs to a child is decided in conversation rather than by a standing rule ^c20260819-13u
- [CT] executing a child may reveal a problem that modifies the master, so the master is revised by feedback rather than fixed at authoring ^c20260819-10u

****

### Migration.Freeze

Ungrounded — landed after the freeze, so these lines carry `Index.Presumption` until the freeze lifts.

- [DC] grounding and index writing stop across the whole system until the core engine runs end to end, replacing the earlier "tarav1 keeps working and is not modified" invariant
- [CT] a frozen index is a fixed migration target: the bar-check meter only reads as progress if its denominator holds still
- [DF] the freeze covers minting anchors and grounding index lines, and nothing else
- [DC] chat storage, tarav1 code, and tarav2 engine exercise stay open, because freezing any of them would block the freeze's own lift condition
- [DC] the lift condition is an executed e2e grounding of a reviewed test line through the normal CLI running the tarav2 design
- [RJ] "until the core engine works well" is rejected as a lift condition: it is a value with no error bar and nobody but its author can evaluate it
- [CT] during the freeze the index stops being the alignment surface and `Impl.Req` artifacts carry the design record instead, which is deferral rather than loss only if the backlog is named
- [DC] the only grounding performed during the freeze is the `Test.Block` run, which exists to test the system rather than to record knowledge
- [CT] everything else authored during the freeze stays ungrounded and carries `Index.Presumption`, including this artifact's own new blocks

****

### Migration.Manual.Discipline

- [DC] the migration is performed manually and is not tooled beyond what the destination itself needs, because tooling built for a one-time path is thrown away with the path
- [CT] maximal flexibility is worth more than automation here: every step's design is expected to change under what the previous step taught
- [DC] a known finding is dismissed by an agent reading the output rather than by teaching the checker an exception, per `Dumb.Code.Is.Better`
- [CT] no surface is immutable during development: anything can be deleted from anywhere once it has served its purpose

****

### Depot.Convergence

Ungrounded — landed after the freeze, so these lines carry `Index.Presumption` until the freeze lifts.

- [DC] tarav-pkg converts to the new model in place and tarav2-pkg dissolves into it, rather than tarav2-pkg staging until a fold at the end
- [RJ] staging tarav2-pkg through the migration is rejected: it keeps two live definitions of one concept alive for the whole migration, which is what the depot boundary rule exists to prevent
- [DF] the destination is a single tarav system — one CLI, one index model, one depot
- [CT] the alignment target is sufficiency for `Test.Block` e2e work, not full content alignment
- [DC] surface conversion and content alignment are separate steps: structure converges early because the engine needs it, content converges lazily against the bar-check meter
- [CT] tarav-pkg must carry a `HEAD.Surface`-capable layout before the e2e run, because act 1 of the battery lands a gated line on one

****

### Test.Block

- [DF] `Test.Block.<run-stamp>` is a block on the tarav-pkg index that exercises the whole capture chain against live data
- [DC] it is captured as an ordinary block through the ordinary loop, because a fixture captured specially tests a path nobody uses
- [DC] the run-stamp is derived from the run's date and session rather than chosen at random, so the block name is evidence of when and where it ran
- [CT] a per-run name also avoids anchor and label collision, so several runs can stand before anything needs cleaning
- [DC] it is deleted when it has served its purpose, like anything else during development

## Destination

What "migrated" means per surface, as a condition someone can check.

### `tarav` CLI/lib

One surface. `tarav` is the only CLI; its index layer runs the tarav2 model — `Index.Line.Record`, `Line.History`, manifest-gated `Touch.Authority`, the scope axis — while skw, chatlas, and anchory remain tarav1's and are reused unchanged.

**Check:** the index commands an operator actually runs resolve to the tarav2 record model, no `tarav2` CLI remains, and no chatlas/skw/anchory behaviour was reimplemented to get there.

### `tarav-pkg` index

The one depot. Its surfaces carry a `HEAD.Surface`-capable layout, parse under the tarav2 kernel/scope model, and `tarav2-pkg`'s records have folded in. Every line landed *after* the cut carries a record; lines already there stay as linter bar findings.

**Check:** `tarav index linter` over `tarav-pkg` reports zero `STRUCTURAL` failures, a block can be landed on a declared `HEAD.Surface`, and `tarav2-pkg` no longer exists. The `line-typed` / `record-grounded` count is the outstanding content debt, and it is a number that falls rather than a task list that rots. Take the baseline with the command, not from this document.

### `tarav-hugentics`

The driver skill's routes and references describe the implemented CLI, and its own index content is recorded under the tarav2 model.

**Check:** no md surface in the skill names a command the CLI does not have. Its kernel lines have records.

### chatlas depot

The archive is `~/Documents/chatlas` — already user-tier and git-backed, which is what the chat `Touch.Authority.Manifest` requires. The project-local `tarav-md/chatlas/` export was a derived projection of it and has been deleted. Nothing here needs migrating; what remains is confirming the degradation rule holds.

**Check:** a fresh clone with no user tier can read the project and its index; only grounding degrades. Chat storage was never interrupted.

## Invariants

Constraints every child inherits. A child that violates one is wrong, not merely different.

1. **The index is frozen.** No new anchors are minted and no new index lines are grounded, anywhere, until the lift condition below is met. The exception is the write that ends the freeze — the `Test.Block` run, captured as an ordinary block. Work authored during the freeze is written ungrounded and stays that way; grounding is spent on testing the system, not on recording knowledge.
2. **The freeze covers index writing only.** Chat storage keeps running, tarav1 code stays editable, and tarav2 engine exercise stays open. Freezing any of those would block the lift condition.
3. **Do not overtool the migration.** Steps are performed manually. Build tooling only where the *destination* needs it, never to make a one-time migration path more comfortable — that tooling is discarded with the path, and it costs the flexibility the plan depends on.
4. **Reuse over reimplementation.** A difference from tarav1 must be traceable to a named model change, or it is not a difference worth having.
5. **Content alignment is not a precondition for design landing.** The new design may land on a surface whose existing content is still unaligned.
6. **The chatlas depot keeps storing chats throughout.** No step may take it offline.
7. **No agent state.** Every standing stays derived; a step that would introduce a stored flag deciding standing contradicts `634`/`635` and is out.

### Lift condition

The freeze lifts when this has actually run, not when it looks ready:

> A reviewed test line is captured to a `Test.Block.<run-stamp>` on the `tarav-pkg` index, end to end, **using the normal CLI** — the hugentics capture loop, a token round-trip, `::approve`, landing, anchor mint, dossier, chat-index backprop — with the **tarav2 design** underneath.

The line's content is irrelevant; `- [DF] this is a test line` is sufficient. What is being tested is the chain, not the sentence.

## Ordering Constraints

The non-obvious part, and the reason the step list is ordered as it is.

Everything before the e2e run is there because the e2e run cannot happen without it. That is the whole ordering principle: the plan front-loads exactly the convergence the lift condition presupposes, and defers everything else past it.

- **Package convergence is a precondition, not a conclusion.** The lift condition says *normal CLI, tarav2 design*, which is only satisfiable if tarav2 **is** tarav's index layer. Convergence therefore moves ahead of the e2e run instead of waiting to learn from it.
- **Surface conversion precedes the e2e run, content alignment follows it.** Act 1 lands a gated line on a `HEAD.Surface`, and `tarav-pkg` has no layout that can be one today — no `homes/`, against a sole pattern of `skills/*/homes/*/chapters/*.md`. So the *structural* half of the tarav-pkg migration is a precondition; the ~1600 anchored lines are not, and stay lazy against the bar-check meter.
- **Doc reconciliation follows convergence**, because convergence changes the command names the docs must describe. Reconciling first means writing `tarav2 index …` and immediately rewriting it to `tarav index …`.
- **The capture loop precedes the e2e run**, because tarav2 has no capture loop at all today. It can record, revise, gate, lint and import; it cannot run the conversation that produces a gated line.
- **Surface conversion does not violate the freeze.** Converting layout and minting records is not minting anchors or grounding lines — `637`'s importer lands records ungrounded by design. Steps 4–5 are compatible with a frozen index.
- **`tarav-hugentics` precedes `tarav-pkg`** — a fortieth of the exposure for the same shape of work, and `637` already rehearsed its import.
- **Everything after the lift is deferrable.** Content alignment and the chatlas confirmation have no downstream dependents; they are ordered last because nothing waits on them.

## Execution.Plan

Coarse steps. Each is designed here, then emitted as a child `Impl.Req`.

Coarse steps. Each is designed here, then emitted as a child `Impl.Req`. Steps 1–5 are the convergence the lift condition presupposes; Step 6 lifts the freeze; 7–9 follow it.

### Step 1 — Converge the package surface
One surface, `tarav`. `tarav2-py` becomes tarav's index layer; the `tarav2` CLI name is scaffolding with an expiry date and nothing may be built against it. Also retires the `tarav2/AGENTS.md` claim that tarav1 "is not modified by tarav2 work" — convergence modifies it, and that surface is the only place still asserting otherwise.
**Result:** `tarav index ...` resolves to the tarav2 record model; no separate `tarav2` entry point remains.

### Step 2 — Reconcile the md surfaces with the converged CLI
`tarav2-pkg/000-INDEX.md` and four of five `tarav2-hugentics` references name `search`, `resolve`, `record`, `reconcile`, `adopt`, `ground`, `capture`, `edit`, `anchory resolve` — a vocabulary the root `AGENTS.md` explicitly retired. `index lines` also crashes at `cli.py:236` on a missing `SurfaceLine.anchor`.
**Result:** no md surface names a command that does not exist; `index lines` runs.

### Step 3 — Bring the capture loop onto the tarav2 model
tarav2 has no capture loop. The hugentics loop — roadmap, focus, propose, token approval, land, backpropagate — must run against the tarav2 record model.
**Result:** the loop produces a tarav2 `LineRecord` from a real conversation.

### Step 4 — Convert `tarav-hugentics` to the new surface model
The rehearsal. 6 blocks, 32 kernel lines — a fortieth of the exposure, same shape of work, and `637` already ran the import into a scratch project.
**Result:** the skill's surfaces are `HEAD.Surface`-capable and its kernel lines have records; expected debt classes are the only findings.

### Step 5 — Convert `tarav-pkg` and dissolve `tarav2-pkg`
The structural half only: a `HEAD.Surface`-capable layout, surfaces parsing under the tarav2 model, and `tarav2-pkg`'s 49 records folded in. **Content is not aligned here** — that is Step 8. This is the step that makes the e2e run possible at all.
**Result:** a block can be landed on a declared `HEAD.Surface` of `tarav-pkg`; `tarav2-pkg` no longer exists.

### Step 6 — MVP: the `Test.Block` e2e run
Acts 1–2 of the battery, green, through the normal CLI. **This step lifts the freeze.**
**Result:** the gate round-trip is shown workable in practice, or its defect is found before any content depends on it.

### Step 7 — The full battery
Acts 3–5. Turns "it worked once" into "it stays working."
**Result:** the negative checks are shown to fire against live data, not only fixtures.

### Step 8 — Content alignment on `tarav-pkg`
Lazy, unbounded, and running after the freeze lifts. Record and ground lines as they are touched rather than in bulk; the bar-check count is the progress meter.
**Result:** content debt is a falling number, taken from the linter rather than from a checklist.

### Step 9 — Confirm the chatlas degradation rule
The archive is already user-tier and git-backed and the project-local export is deleted, so nothing migrates. What remains is checking that a fresh clone with no user tier reads the project and its index with only grounding degraded.
**Result:** the degradation rule is verified rather than assumed.

## Test.Battery

Acts, and what must hold after each. The battery is the set of assertions, not the narrative of steps — each act is followed by named checks with a computable verdict.

**MVP is acts 1–2.** The battery is 1–5, re-runnable by deleting the block.

| # | Act | Must then hold | Check with no live instance today |
|---|---|---|---|
| 1 | capture a test line | grounded · gated · on a `HEAD.Surface` | `landing-evidenced` |
| 2 | revise it | trace of 2 · equivalence claim · old wording off HEAD | `equivalence-*`, `materialization-standing` |
| 3 | demote — move it off the surface | TAIL derived · `Landing.Unhonored` **fires** | `landing-honored` |
| 4 | forge — fabricate a gate token | `Gate.Contradicted` **fires** | `gate-verifies` |
| 5 | delete the block whole | the run is repeatable; coverage findings are read and dismissed | — |

Acts 1–2 prove the pipe is connected. **Acts 3–5 prove the checker fires when it should**, which is the half that matters: a battery that only walks the happy path is the exact failure this system indexed — green suite, wrong system, missing test.

## Step Status

Status lives in the child. This table points; it does not copy.

| # | Step | Child |
|---|---|---|
| 1 | converge the package surface | *not designed* |
| 2 | reconcile md surfaces with the CLI | *not designed* |
| 3 | capture loop on the tarav2 model | *not designed* |
| 4 | convert `tarav-hugentics` | *not designed* |
| 5 | convert `tarav-pkg`, dissolve `tarav2-pkg` | *not designed* |
| 6 | MVP `Test.Block` e2e — **lifts the freeze** | *not designed* |
| 7 | full battery | *not designed* |
| 8 | content alignment on `tarav-pkg` | *not designed* |
| 9 | confirm the chatlas degradation rule | *not designed* |

Prior work feeding this plan: `631`, `632`, `633`, `634`, `635`, `637`.

## Impl.Log

### Open decisions

None outstanding. The accumulator is empty — every decision the step list rested on has been taken. New ones land here as steps expose them.

### Settled

- **Package convergence: one surface, `tarav`.** Settled by the lift condition, which requires the normal CLI to run the tarav2 design. Rejected alternative: two retained CLIs — it cannot satisfy the lift condition without duplicating the capture loop.
- **`tarav2-pkg` dissolves into `tarav-pkg`, converted in place.** The destination is a single tarav system, aligned far enough to run `Test.Block` e2e work. Rejected alternative: staging `tarav2-pkg` until a fold at the end — it keeps two live definitions of one concept alive for the whole migration, which is exactly what the depot boundary rule was written to prevent, and a single converged store makes that unavoidable rather than merely untidy.
- **The chatlas depot needs no tier migration.** `~/Documents/chatlas` is the archive: already user-tier, already git-backed, which is what the chat `Touch.Authority.Manifest` requires. `tarav-md/chatlas/` was a derived export written by `tarav chatlas local sync` — 3115 files, git-tracked, deleted as stale. The earlier reading of it as a scope-axis contradiction was wrong: a regenerable projection sitting project-side is not grounding data held at the wrong tier.

### Deferred by the freeze

Capture candidates accumulated and waiting for the freeze to lift. Named here so this is deferral rather than loss:

```text
new concepts   Signal.Not.Semantics · Documentation.Is.The.Code · Proof.Of.Touch
revisions      Accountable.Assertion · Constraint.Steering
grounding      the ^c legacy question — a chat-legacy Touch.Authority.Manifest is the designed answer
```

### Index.Presumption

- The linter's bar checks (`line-typed`, `record-typed`, `record-grounded`, `scope-resolves`) can serve as the content-migration progress meter, making a separate migration checklist unnecessary. Agent inference from the checks' stated meaning — *work not yet done, not an error* — not a user decision.
- `tarav-hugentics` is closer to a re-authoring than a migration, and the volume gap against `tarav-pkg` is what makes it the right rehearsal target. Measured, but the conclusion drawn from it is inference.

### Notes

- The `Migration.Freeze`, `Migration.Manual.Discipline`, and `Test.Block` blocks above are **ungrounded by design**, not by omission. They were written after the freeze, and the freeze grounds nothing except the `Test.Block` run — grounding is being spent on testing the system, not on recording knowledge. They stay under `Index.Presumption` until the backlog is landed.
- This artifact's own `^c` anchors are chatlas1-namespace and ungated — the `Anchor.LegacySigil` class Steps 4–5 exist to retire. Not a defect in the plan, but the plan should not add more of them.
- The agent-home `HEAD.Surface` exclusion is hardcoded in `HeadSurfaces.contains()` rather than declared in `head-surfaces.json`. This looks like a design/implementation gap but is not: `637` records it as a deliberate rule replacing `634`'s hand-narrowed config, asserted by `test_the_agent_home_is_never_a_head_surface`. Noted here so the next reader does not re-open it.
- **Corrected measurements.** The earlier figures in this artifact were wrong; take baselines from the commands, not from here.

  ```text
  tarav index blocks --depot skills/tarav-pkg         347 blocks, 2232 kernel lines, gr-density 0.5901
  tarav index blocks --depot skills/tarav-hugentics     6 blocks,   32 kernel lines, gr-density 0.0625
  grep typed lines, tarav-pkg                         1941 typed / 1623 anchored across 127 md files
  grep typed lines, tarav-hugentics                     50 typed /   40 anchored across  69 md files
  chatlas export (deleted)                            3115 files, 35M — derived, not the archive
  tarav2                                              171 tests, 29 checks over 49 records, 0 failed / 1 blocked
  ```

  The two denominators differ on purpose: `tarav index blocks` counts kernel lines inside recognized blocks; the grep counts typed lines anywhere, including references that are not index surfaces. `637` imported 29 lines from `tarav-hugentics`, consistent with the block census rather than the grep.
