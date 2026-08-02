> $kw: ^implementation-review-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-skill-arg-contract

# Implementation.Review.Workflow.Module

Review an `Impl.Req` from outside its design context: verify its claims against `Hard.Evidence`, check it is well formed and ready for execution, and produce an in-chat report.

The module exists for the blind-spot check: the designer's context is where the blind spots live — unstated assumptions the designer "knows", stale references, decisions hidden inside steps. The intended usage is a fresh agent reviewing an `Impl.Req` it did not design. A cold read is the test of "self-contained enough for any agent to execute".

This module is **read-only**: it writes no files, edits no artifact, flips no status. Its only output is the report. Acting on findings stays with the caller.

## Input

- an `Impl.Req` (path, note number, or supplied content) — required; without one, orient and stop

## Review Loop

### 1. Cold read first

Read the `Impl.Req` end to end **before** opening any linked design artifact, source file, or referenced surface. Note everything that confuses, surprises, or requires knowledge the document does not supply — first-pass confusion is data: it is what the executer will feel. Keep these notes; they seed the findings.

### 2. Evidence audit

> $kw: --derived --from Hard.Evidence
> --intent the claim-grading protocol: verify each load-bearing claim
> --cont against the world as it is now; verified/stale/unverifiable grades

Walk the claims in `Impl.Abstract` and `Impl.Index` (especially any `Current.State` section) and verify each against the world as it is **now**:

- cited files, modules, symbols, and line references exist as described
- referenced commands run (help/dry paths — never mutating ones)
- the code the plan assumes matches the actual code — staleness is the killer failure: an `Impl.Req` can be well formed and wrong because the target moved since it was written
- referenced artifacts (design notes, sessions, index concepts) resolve

Grade each checked claim: **verified** / **stale** (was true, no longer) / **unverifiable** (no way to check from here). Sample proportionally to risk — every load-bearing claim gets checked; incidental color does not.

> $kw. end

### 3. Readiness audit

> $kw: --derived --from Alignment.Checkpoint::Readiness
> --intent the designer's readiness checkpoint re-run from outside,
> --cont as an audit list over an artifact the reviewer did not write

The designer's `Alignment.Checkpoint::Readiness` list, re-run from outside:

- scope and out-of-scope explicit
- current state inspected and cited (and it survived the evidence audit)
- every slice has an observable result and a check; `RED.GREEN.Test.Suite` behaviors named and runnable in this environment
- dependencies and ordering explicit
- no unresolved decision hidden inside an execution step
- risks/deviation triggers cover the failure modes the evidence audit exposed
- the plan is followable without the design chat — the cold-read notes are the verdict on this one

> $kw. end

### 4. Report (in chat)

Lead with the verdict, then findings ranked by severity:

- **Verdict**: `ready` / `ready-with-notes` / `not ready`
- **Findings**: each tied to the artifact section or line, stating the claim, the evidence checked, and the grade or gap — concrete enough that the designer can fix it without re-deriving the review
- **Cold-read friction**: what a context-free executer will stumble on, even where nothing is strictly wrong
- **Evidence coverage**: what was verified vs taken on trust, so the caller knows the report's own grounding

## Boundaries

- report only — do not fix the artifact, do not implement, do not update `Impl.Log`; if asked to fix afterwards, that is a new instruction from the caller
- do not re-litigate the design: the review checks groundedness and executability, not whether the design is good; a genuine design smell may appear as one flagged note, never as a review axis
- read-only toward the repos: no mutating commands, no test-suite runs that write artifacts — running the named test commands to confirm they *collect* is fine; executing the plan is not
- the review's authority is evidence, not opinion: every finding cites what was checked

## Alignment.Mode

- `Interactive` — may ask the caller to resolve genuinely ambiguous claims (e.g. which repo a relative path means) before grading them `unverifiable`
- `Autonomous` — grade with what can be established; ambiguity becomes an explicit finding, never a guess

> $kw: --from Impl.Req --from RED.GREEN.Test.Suite
