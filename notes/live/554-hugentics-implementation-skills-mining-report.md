# Hugentics Implementation Skills - mining report

## Purpose

This report collects source-mined improvement topics for:

- `hugentics-impl-designer`
- `hugentics-impl-executer`
- `hugentics-codebase-cleaner`

It is a proposal input, not accepted design. The linked design session walks through the report and makes design decisions about each part.

## Current Direction

The three skills already form a coherent phase chain:

```txt
cleanup candidate selection
-> implementation design
-> implementation execution
```

The highest-value improvement is strengthening the contracts between phases:

- what makes a cleanup candidate worth pursuing
- what makes an `Impl.Req` ready for execution
- what the executer must verify before editing
- what evidence proves each slice and the full implementation succeeded
- what happens when reality invalidates the plan

## Immediate Consistency Issue

`hugentics-codebase-cleaner` says the executer owns per-slice commits. This contradicts the executer's current git checkpoint contract:

- commit all worktree changes found before implementation
- divide that checkpoint into coherent commits when rational boundaries are clear
- make no commits and suggest no commits after implementation begins

## Shared Improvement Topics

### Executable.Feedback.Loop

Every `Impl.Req` should identify the narrowest reliable feedback loop before execution begins.

Possible signals:

- focused test
- CLI invocation
- generated artifact comparison
- type check
- linter
- manual inspection with explicit criteria

Potential design move:

- the designer specifies feedback loops
- the executer confirms they are available and establishes the baseline before editing when feasible
- the executer records pre-existing failures or unavailable checks

### Impl.Req.Readiness

An explicit readiness contract could require:

- scope and out-of-scope boundaries are explicit
- current state was inspected and cited
- the first observable endpoint is identified
- every slice has a concrete observable result and check
- dependencies and ordering constraints are explicit
- known risks and deviation triggers are stated
- no unresolved design decision is hidden inside an execution step
- the plan is understandable without chat context

### Impl.Req.Reader.Test

A substantial `Impl.Req` could be tested from a fresh-agent perspective.

The reader should be able to:

- explain the goal
- identify the first action
- identify forbidden scope
- identify verification commands or checks
- recognize when execution must stop or deviate

This could begin as a lightweight designer self-check rather than a mandatory delegated-agent workflow.

### Slice.Dependency.Semantics

Slices currently have ordering, but dependencies are mostly implicit.

Potential fields:

- blocked by
- enables
- independent work
- human-gated decision
- external dependency

Explicit dependency semantics help detect plans that call horizontal phases vertical slices.

### Verification.Ladder

Verification could operate at three levels:

1. baseline: prove the signal works before editing
2. per-slice: prove the current observable result
3. completion: prove original intent, integration behavior, and cleanup state

### Deviation.Taxonomy

The current reversible/non-reversible distinction is useful but broad.

Potential deviation classes:

- implementation detail differs while intent remains unchanged
- planned file or module does not exist or has moved
- dependency assumption is false
- acceptance signal cannot be produced
- requested scope conflicts with current architecture
- discovered work expands scope
- original design intent is no longer implementable

Each class could map to continue, amend the `Impl.Req`, or stop.

### Impl.Req.State.Model

`Impl.Abstract.status` could use canonical states and transitions.

Candidate states:

- designing
- ready-for-execution
- executing
- blocked
- implemented
- partially-implemented
- superseded

The state model should remain lightweight and avoid machine-readable bureaucracy.

## Impl Designer Topics

### Canonical.Impl.Req.Template

The existing example is useful but too light to establish the complete artifact contract.

A reusable template could include:

- scope
- source context
- current-state evidence
- target behavior
- constraints and out-of-scope
- dependencies
- ordered vertical slices
- feedback loop per slice
- risks
- deviation triggers
- acceptance signals
- unresolved questions
- status and log

The detailed template belongs in `references/`, not the workflow master.

### Current.State.Evidence

The designer should inspect actual implementation surfaces before designing the path. Evidence should cite files, commands, artifacts, or observed behavior.

### Decisions.And.Assumptions

Accepted decisions and assumptions should be distinguished.

- accepted decisions should not be casually reopened during execution
- assumptions should carry a validation action or deviation trigger

### Vertical.Slice.Quality

The first slice should be a tracer bullet that proves the deepest relevant integration path early.

Avoid horizontal phases such as:

- create all models
- update all services
- add all tests

Prefer one narrow observable behavior through all relevant layers.

### Readiness.Review

Before handoff, the designer could review the artifact against the agreed readiness contract.

## Impl Executer Topics

### Pre.Checkpoint.Readiness

The executer should confirm that the `Impl.Req` is executable before creating the git checkpoint. The checkpoint remains immediately before the first implementation edit.

### Baseline.Verification

Run planned verification signals before editing when feasible and record:

- passing baseline
- known pre-existing failures
- unavailable verification
- environmental blockers

### Slice.Entry.Exit

Potential slice entry checks:

- prerequisites are satisfied
- relevant files were reread
- feedback loop is available

Potential slice exit checks:

- observable result exists
- planned check completed
- diff scope inspected
- `Impl.Log` updated

### Final.Acceptance.Review

Completion could explicitly verify:

- all acceptance signals
- original user intent
- no stale legacy surfaces
- implementation diff scope
- known failures and remaining risk

### Git.Checkpoint.Boundary

Preserve the current contract:

- commit all existing changes before implementation
- split them into coherent commits when rational boundaries are clear
- use one checkpoint commit when boundaries are ambiguous
- make and suggest no commits after implementation begins

## Codebase Cleaner Topics

### Cleanup.Candidate.Selection

A candidate scoring model could consider:

- demonstrated maintenance friction
- repeated knowledge or boundary leakage
- blast radius
- verification strength
- confidence in behavior preservation
- expected simplification
- architectural fit

### Cleanup.Evidence

A cleanup candidate should cite concrete evidence such as:

- repeated logic across specific callers
- confusing navigation path
- shallow pass-through abstraction
- inability to test through a meaningful interface
- dead or bypassed layer
- repeated bug-prone rule

### Deletion.Test

Potential heuristic:

- if deleting an abstraction spreads its complexity across callers, it may earn its place
- if deleting it makes complexity disappear, it may be unnecessary

This should remain one tool rather than the cleaner's entire architectural vocabulary.

### Cleanup.Classes

Candidate classes could include:

- remove dead state
- centralize repeated knowledge
- simplify local control flow
- deepen a module
- remove a bypassed abstraction
- improve agent navigability
- tighten an ownership boundary

### No.Cleanup.Justified

Explicit reasons to stop without changing code could include:

- insufficient verification
- cleanup value too low
- change requires architecture redesign
- apparent duplication represents intentionally different concepts
- change exceeds requested scope

## Trigger And Packaging Topics

### Skill.Description.Triggering

Per the local custom recommendation, `hugentics-impl-designer` and `hugentics-impl-executer` should gain explicit `USE WHEN` clauses. The cleaner already follows this pattern.

### Progressive.Disclosure

Potential designer references:

- `impl-req-template.md`
- `impl-req-readiness.md`
- `vertical-slice-design.md`

Potential executer references:

- `execution-readiness.md`
- `verification-and-deviation.md`
- `git-checkpoint.md`

### Lightweight.Validation

A deterministic structural validator could eventually check:

- required `Impl.Req` sections
- every slice has observable, check, and status fields
- no placeholder text remains
- canonical status values are used

It should validate structure, not judge design quality.

## Avoid

- heavy identifier systems such as `REQ-001`, `TASK-001`, and `RISK-001` everywhere
- exact line-number requirements that become stale quickly
- treating all work as parallelizable or machine-deterministic
- generic code-smell catalogs embedded directly into the cleaner
- mandatory tests for every cleanup or bug fix
- mandatory rollback instructions per slice when the initial git checkpoint already provides the rollback floor
- roleplay, forced output theater, and arbitrary formatting constraints
- turning `Impl.Req` into a specification so large that it delays implementation feedback

## Proposed Upgrade Order

1. Correct the cleaner's stale per-slice commit statement.
2. Define the shared `Impl.Req` readiness and verification contract.
3. Upgrade the designer with template, evidence, dependencies, and readiness review.
4. Upgrade the executer with baseline verification, slice entry/exit checks, and final acceptance review.
5. Upgrade the cleaner with evidence-based candidate selection and cleanup classes.
6. Add lightweight behavioral test prompts for the three-skill chain.

## Sources Mined

### Local Agentos Sources

- `skills/hugentics-impl-designer/`
- `skills/hugentics-impl-executer/`
- `skills/hugentics-codebase-cleaner/`
- `skills/agentos-hugentics/references/alignment-session.md`
- `skills/agentos-pkg/index/102-index.md`
- `skills/agentos-pkg/appendix/Impl.Req-appendix.md`
- `skills/agentos-pkg/appendix/Development.Principles-appendix.md`
- `skills/agentos-skills-ingenier/references/source-registry.md`
- `skills/agentos-skills-ingenier/references/mining-rubric.md`
- `skills/agentos-skills-ingenier/references/custom-recommendations/`

### External Mirrors

- Matt Pocock skills: `diagnose`, `tdd`, `to-issues`, `to-prd`, `improve-codebase-architecture`, `grill-with-docs`
- Anthropic skills: `doc-coauthoring`, `skill-creator`, `webapp-testing`
- Awesome Copilot skills: implementation-plan, refactor-plan, refactor, and review/refactor workflows
- Fabric patterns: `review_code`, `review_design`, `create_coding_feature`, `summarize_git_diff`, `create_git_diff_commit`

## Source Assessment

- **adopt:** feedback loops, tracer-bullet slices, explicit dependencies, readiness checks, reader perspective, evidence-backed candidate selection
- **adapt:** state models, reader testing, deletion test, structural validation, plan templates
- **avoid:** rigid machine-readable bureaucracy, generic code-smell catalogs, roleplay-heavy prompting, arbitrary output constraints
