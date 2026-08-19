# Hugentics --impl System Pass - impl-req

## Impl.Abstract

- **Status:** Implemented and verified. Build clean; `skw check` carries only pre-existing advisory drift.
- **Scope:** One pass over the `--impl` subsystem of `tarav-hugentics`. Fix the routing defect that hides the shared practices and preferences from the designer, remove the module naming that caused it, and land the design principles this session produced into the modules that now reach every mutating implementation workflow.
- **Governing principle:** a design constraint the designer never loads is a constraint the plan can contradict. The two `general-*` modules carry design stances, not only execution mechanics, so they belong to the whole namespace.
- **Targets:** `tarav-md/skills/tarav-hugentics/.skw/src/` — this skill is Skillware, so all edits are to `.skw.md` sources and reach the runnable surface only through `agentos skw build`.
- **Out of scope:** The `Convergent.Justification` concept block in `tarav-pkg` (a `Verbatim.User.Gated` surface needing user approval); splitting the two knowledge modules by phase; `capture.md` and the Index namespace.
- **Acceptance:** `--impl --design` loads practices and preferences. No module name asserts a phase binding it does not have. The readiness checkpoint tests convergent justification, and `review.md` inherits it without its own edit. `agentos skw check` is clean or its findings are accounted for.

## Impl.Index

### Routing.Defect

- [IS] `general-practices.md` and `general-preferences.md` are loaded by `execute.md` alone, so `--impl --design` never sees them.
- [CT] both files carry design stances rather than execution mechanics: `No.Legacy.Allowed`, composition over inheritance, dependency justification, and testing durable public behavior are all decisions the plan commits to.
- [DC] the defect lets the `Impl.Req` and the executer contradict each other — a plan may specify a compatibility shim its executer is instructed not to build.
- [DC] `review.md` re-runs the designer's `Alignment.Checkpoint::Readiness` from outside, so a gap in the designer's list silently becomes a gap in review.
- [DC] `develop.md` makes it visible: one agent loads the preferences after it has already written the artifact they govern.
- [DF] the root cause is the module identity — `Implementation.Execution.*` asserts a phase binding that was then encoded in the routing row's `when`.

### Convergent.Justification

- [DF] convergent justification is the property that a design element has several independent reasons to exist; it is evidence the design is carved at a joint.
- [CT] an element with exactly one reason is fragile: weaken that reason and it becomes ceremony.
- [DC] the reasons must be independent — each still standing if the others were removed — or the test degrades into post-hoc defence of whatever exists.
- [DC] it belongs in `Alignment.Checkpoint::Readiness` because it is a design-time test applied when choosing between candidates, and `review.md` inherits it from there.

### Implementation.Principles

- [DC] verification cost is a design axis: prefer a candidate whose claims something cheap can check over one that must be trusted.
- [DC] `Producer.Aids.Checker` applies to implementation design — shape the output so the check stays trivial rather than making the checker clever.
- [DC] a defect found by hand owes the suite a test, because a wrong system with a green suite means the test is missing.
- [DC] documentation points at the implementation rather than describing it, since a description is a stored copy of a computable fact with nothing asserting it still holds.

## Impl.Log

- Index.Presumption: the two `general-*` modules are **not** split by phase. Some content ("read the target files first", "run the immediate feedback loop") applies only at execute, but a few lines of phase-irrelevant context are far cheaper than a third module, and nothing in either file is wrong at design time.
- Index.Presumption: `Convergent.Justification` lands in `general-preferences.skw.md` as plain content rather than a `--derived --from` block, because no `tarav-pkg` concept block exists to derive from yet. Landing that block is a gated act deferred to the user.
- Tarav1 alignment: `Producer.Aids.Checker`, `Constraint.Steering`, and `Accountable.Assertion` already exist in `tarav-pkg/design/106-design.md`. The principles added here cite them by name in the existing `harvest.md` style rather than restating them.
- Skillware: `references/*.md` are compiled surfaces. All edits go to `.skw/src/**.skw.md`, then `agentos skw build --skill <path>`, then `agentos skw check`.

## Execution.Plan

### Slice 1 — Routing fix
`^route-implementation-design` gains both `--load` lines; `design.skw.md`'s "Always load" sentence names them.
**Check:** the compiled `SKILL.md` design row lists four loads; `design.md` names practices and preferences.

### Slice 2 — Module rename
Drop `Execution` from both module identities and the routing row's address and `when`.
**Check:** no `Implementation.Execution.*` string survives anywhere in `src/` or the compiled tree.

### Slice 3 — Convergent.Justification
Add the principle to `general-preferences.skw.md` and one line to `Alignment.Checkpoint::Readiness` in `design.skw.md`.
**Check:** `poi`-free build; the readiness list carries the test; `review.md` is untouched and inherits it.

### Slice 4 — Implementation principles
Add verification cost, `Producer.Aids.Checker`, and the point-don't-describe rule to `general-preferences.skw.md`; add the defect-owes-a-test rule to `general-practices.skw.md`.
**Check:** each new block either derives from a real concept or is plain content; no invented `--from`.

### Slice 5 — Build and check
`agentos skw build`, then `agentos skw check`.
**Check:** build succeeds, lock updates, check findings are clean or accounted for in `Impl.Log`.

## Slice Status

| # | Slice | Status | Check |
|---|---|---|---|
| 1 | Routing fix | done | the design row loads four surfaces; `design.md` names both modules |
| 2 | Module rename | done | no `Implementation.Execution.*` survives in src or the compiled tree |
| 3 | Convergent.Justification | done | in the preferences module and in the readiness list |
| 4 | Implementation principles | done | verification cost, `Producer.Aids.Checker`, point-don't-describe, defect-owes-a-test |
| 5 | Build and check | done | 32 files, 5 built, 0 refused; my three findings resolved |

## Verification

Compiled `SKILL.md` after the pass:

```text
| Implementation.Design.Workflow.Module | design.md · product-capture.md
                                        · general-practices.md · general-preferences.md |
| Implementation.Practices.Knowledge.Module  | references/impl/general-practices.md  |
| Implementation.Preferences.Knowledge.Module| references/impl/general-preferences.md |
```

`references/impl/design.md:43` now carries the readiness test, and `review.md` was not edited —
it re-runs the designer's list from outside, so it inherited the check. **One edit, two
workflows**, which is the principle passing on itself.

Three POIs were raised by this pass and all three are resolved:

```text
Dependency.Undeclared   design.md mentions No.Legacy.Allowed   → --cite No.Legacy.Allowed
Dependency.Undeclared   preferences mentions Impl.Req          → --cite Impl.Req
Context.Assembly.Bypass --from Producer.Aids.Checker           → --dev-from index-context-assembly
```

The fourth, `Dependency.Uncited`, appeared while fixing the third — a `--cite` whose target was
not visible in the compiled body. Naming `Producer.Aids.Checker` in the line itself resolved it,
which is the linter enforcing *point, do not describe* on the very edit that added that rule.

Five `Derived.Stale` advisories remain and are **pre-existing**, confirmed by their evidence:

```text
alignment-session.md ×2   Alignment.Loop, Design.Variable, QA.Space, …
impl/design.md    6ba9b9e   Alignment.Loop, Alignment.Loop::How      (^how-loop)
impl/design.md    200b870   Impl.Req, RED.GREEN.Test.Suite, Vertical.Slice
impl/example.md           upstream concept drift
```

All are upstream `tarav-pkg` concepts that moved since those bodies were written. None is the
readiness block this pass edited — that one re-blessed on its body change, exactly as the lock
model specifies.
