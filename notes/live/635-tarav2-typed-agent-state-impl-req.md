# Tarav2 Typed.Agent.State - impl-req

## Impl.Abstract

- **Status:** Implemented and verified. 167 tests green; `ruff` clean; the depot runs 29 checks over 49 records with 0 errors and 1 blocked. Continues `634-tarav2-no-agent-state-impl-req.md`, whose governing principle this reframes: the axis is not presence/absence of agent state but **verification cost**.
- **Scope:** Turn the linter from a defect reporter into an estimator. Assertions return three-valued verdicts with a named evaluator; unknowns become loud instead of silent; findings carry operands and a source pointer instead of prose; the check's own code becomes its documentation; the report distinguishes clean-because-checked from clean-because-uncheckable.
- **Governing principle:** an `Agent.State.Variable` is expensive to validate, so the design should minimise them and pay deliberately for the fundamental ones. A `Typed.Agent.State` carries assertions that are cheap to validate; the implemented assertions belong to the type; the linter is the tooling that reacts to them.
- **Targets:** `tarav2/tarav2-py/src/tarav2/`, its tests, the `tarav2-md` depot, and both `AGENTS.md` files.
- **Out of scope:** Agent-tier and user-tier evaluators as running systems — the `evaluator` field is declared and only `code` is implemented. Never-fired check tracking. Concentration heuristics beyond grouping.
- **Acceptance:** No check silently reports unknown as clean. No `Finding` carries a prose description of its own computation. `poi explain` points at the implementation. Reading an entry shows its verdict vector.

## Impl.Index

### Typed.Agent.State

- [CT] an `Agent.State` is dangerous because it is not easy to verify in general, so the design question is how costly verification is.
- [DF] an `Untyped.Agent.State` is expensive to validate and is avoided; a `Typed.Agent.State` carries assertions that are cheap to validate.
- [DC] the implemented assertions belong to the type of the state, which is what tooling such as the linter reacts to.
- [CT] the index line is the paradigm case: `Line.Type` is the discriminator, and scope, label, support and surface presence are its cheap assertions.
- [DC] the principle drives the design and not only the checking, so a design candidate carrying `Agent.State.Variable`s should be changed rather than merely instrumented.
- [DF] a variable is not fundamental when something in the world **computes** it cheaply; determinacy was never the test.
- [CT] the `Touched.Index` is a collection of `Agent.State.Variable`s, and the system around it exists to validate them.

### State.Estimation

- [DF] a state is minimally a `value + err/unknown` pair, and using it without estimating that pair is an antipattern.
- [DC] the assertions are the estimator: they test fundamentals of the state, so a state failing many systematic assertions is probably a `Bad.State` — or the system drifted.
- [DC] a verdict carries its evaluator, because `ok` from cheap code and `ok` from an agent are different amounts of trust.
- [IS] reporting `unknown` as clean is the antipattern applied to the estimator itself; four checks currently degrade to silence when the archive or git is absent.

### Dumb.Code

- [CT] `DUMB.CODE.IS.BETTER`: the linter saves the agent computable operations and never does the semantic work.
- [DC] rules may overdetect and produce false positives, because an agent is on the other side; that is acceptable by design.
- [DC] agent search is expensive because finding one error requires semantically re-verifying everything as good, and it still loses long-range interactions.
- [DF] the check catalog is a `Fishing.Net`: cheap tests run over all items, converting expensive semantic attention into cheap mechanical attention.
- [DC] the growth rule is TDD's: a bad index with a clean linter means the check is missing, chiselling out one revealed constraint at a time.
- [CT] the catalog inherits TDD's growth rule and explicitly not its verdict semantics, because a finding is ambiguous between bad state and drift.

### Signal.Not.Semantics

- [CT] the linter communicates no semantic value; agents double-check from first principles and that is their job.
- [DF] a finding is a standardized typed signal of a well-declared computation: the check, the subject, the verdict, and the operands compared.
- [DC] prose describing what a check computed is a summary standing in for the evidence, so findings carry operands rather than a sentence.

### Documentation.Is.The.Code

- [CT] a check's prose description is itself `Untyped.Agent.State`: a stored copy of a computable fact with nothing asserting it still holds.
- [DC] point the agent at the check's implementation — for understanding a check, the agent reads the code.
- [DC] do not describe the object; describe how to explore the system and tell the agent where to look.
- [DC] the docstring says why the constraint exists, the body says what is computed, and nothing says what is computed twice.
- [DC] `resolutions` survive because what answers are legitimate is not derivable from the body; the crafted surface shrinks to exactly what execution cannot hold true.
- [CT] readability of a check body is a contract rather than a style preference, which is a third independent argument for dumb code.

## Impl.Log

- Index.Presumption: `Check.title` is deleted rather than kept for display. It is a prose restatement of the body, and `poi explain` printing `file:line` plus the docstring's *why* is strictly more useful and cannot drift.
- Index.Presumption: `source` is computed from `check.run.__code__`, never stored. A stored pointer would be the same defect one level up.
- Index.Presumption: `evaluator` ships declared with only `Evaluator.CODE` produced. Naming the axis now costs nothing and prevents `ok` meaning two different things later; implementing agent-tier evaluation is out of scope.
- **Tarav1 alignment (mid-run correction).** The three-valued verdict already exists in tarav1: `tarav.index._linter_models` carries `CheckStatus = passed | failed | blocked` and a `GateResult{allowed, reason, blocked_by}` that declares why a check could not run, and `tarav.index.linter` reports `blocked_count` in its summary. I had invented `Status{ok, err, unknown}` before checking. Adopted tarav1's vocabulary verbatim and its per-check `GateResult` shape.
- Tarav1 alignment: `LinterFinding.details` and `POIDiagnostic.evidence` are already structured operand dicts — the operands idea is tarav1's too. The tarav2 delta is only that the prose `message` is *removed* rather than carried alongside, which is traceable to `Signal.Not.Semantics`.
- Tarav1 divergence, named: tarav1's `LinterFinding` carries `severity: error | warning`. Tarav2 has no severity — ranking what a finding means is the agent's work, and severity is the route by which semantics would be smuggled back into the signal. Traceable to `Signal.Not.Semantics`.
- Tarav1 divergence, named: tarav2 lets a **single subject** be blocked, not only a whole check. The err/unknown pair belongs to the state, not only to the checker, which is the `State.Estimation` model change. Both mechanisms ship: a per-check `gate` for whole-check preconditions (no git), per-finding `blocked` for per-subject ones (one session missing).
- Parked, from tarav1: `poi_catalog.py` discovers POI classes from `poi/` chapters in the depot, so tarav1's POI-class documentation is addressable index content rather than a Python tuple. That is closer to *do not describe the object* than tarav2's `resolutions` tuple. Not adopted now — it buys cross-package POI registration tarav2 does not need — but it is the better long-run shape.
- Index.Presumption: `review-covers-support` is added as a *separate* dumb check rather than tightening `verify_gate`. Overdetecting additively is the cheaper shape and leaves the gate's contract stable.
- Deferred: never-fired check tracking (a check that never fired has unknown status). It needs run-persistent state and was not asked for; the argument stands in `Dumb.Code` if it is wanted later.
- Deferred: concentration heuristics. The report groups by subject and by check, which is what makes Bad.State versus drift *readable*; ranking it is semantic work and belongs to the agent.

## Execution.Plan

### Slice 1 — Verdict types
`Status{ok,err,unknown}` and `Evaluator{code,agent,user}` in a `verdict` module; `Finding` gains `status`, `evaluator`, `operands`, and drops `detail`.
**Check:** a finding round-trips its operands; `identity` is unchanged by operand content so blessings survive.

### Slice 2 — Operands everywhere
Rewrite every `Finding(...)` site to emit compared values, not sentences.
**Check:** no finding constructor takes a prose string; `line-drift` emits `surface` and `record` operands.

### Slice 3 — Loud unknowns
The four degradations emit `Status.UNKNOWN` findings: archive absent, gate unverifiable, git absent, blessing unverifiable.
**Check:** a project with no archive reports unknowns and is not `clean`; an err and an unknown are never conflated.

### Slice 4 — The check is its own documentation
Delete `Check.title`; compute `Check.source` from the function; strip the *what* line from every check docstring; `poi explain` prints source location, why, and resolutions.
**Check:** `poi explain <check>` names `linter.py:<line>`; no check carries a prose title.

### Slice 5 — Report as estimate
`LintReport` separates errors from unknowns, counts per-check status, and groups findings by subject.
**Check:** the summary distinguishes `27 clean` from `9 clean, 18 unknown`.

### Slice 6 — Verdict vector on the entry
`tarav2 index record` and `index resolve` show each entry's verdicts.
**Check:** resolving a line prints its measurement alongside its value.

### Slice 7 — Rephrase chain and support coverage
`ReviewStanding` distinguishes review reached through renames only from review reached through a rephrase; add `review-covers-support`.
**Check:** a rename chain reports `via_trace`; a chain containing a rephrase is distinguishable.

### Slice 8 — Rename and capture
`No.Agent.State` → `Typed.Agent.State` as a trace rename; skw annotations for the new groundings; depot blocks; both `AGENTS.md` files lose their check descriptions in favour of pointers.
**Check:** depot lints clean; no `AGENTS.md` restates what a check computes.

## Slice Status

| # | Slice | Status | Check |
|---|---|---|---|
| 1 | Verdict types | done | tarav1's `passed/failed/blocked` plus the `evaluator` axis |
| 2 | Operands everywhere | done | no finding constructor takes prose; drift emits both sides |
| 3 | Loud unknowns | done | absent archive and absent git both report, neither is clean |
| 4 | Check documents itself | done | `title` deleted; `source` computed from `run.__code__` |
| 5 | Report as estimate | done | `clean` and `verified` are separate claims |
| 6 | Verdict vector on the entry | done | `index resolve` prints signals beside the value |
| 7 | Rephrase chain, support coverage | done | `review-via-rephrase` carries `evaluator=agent` |
| 8 | Rename and capture | done | 5 records rescoped; 17 lines captured; 49 total |

## Verification

The report stopped conflating *unchecked* with *fine*:

```text
before   clean — 32 record(s), 32 surface line(s), 27 check(s)
after    29 check(s): 28 passed, 0 failed, 1 blocked   0 error(s), 0 unverifiable
         Unverifiable — checked nothing, which is not the same as clean
           coverage-converges: the project index is not tracked by git
```

Same depot, same state. The first line was a claim the system was not entitled to make.

`poi explain` points at the code instead of restating it:

```text
landing-evidenced
  computes  linter.py:784   ← read it; the body is the specification
  why       Presence says what is; the gate says what licensed it.
  resolutions (choose case by case; none is prescribed):
    - record the landing gate for the approval turn that licensed it
    - take the line off the HEAD.Surface until it is approved
    - narrow the HEAD.Surface declaration, if this surface is not current design
```

Three of the new tests are the ones that would have caught the old design:
`test_clean_and_verified_are_different_claims`, `test_an_unverifiable_gate_is_blocked_not_silent`,
and `test_the_docstring_is_not_a_restatement_of_the_name`.

```text
tarav2 index linter    29 checks, 49 records, 0 errors, 1 blocked
pytest                 167 passed        ruff  All checks passed
```


## Convergent.Justification Addendum

After landing `Convergent.Justification` into `tarav-pkg`, the principle was run back over this
implementation. Seven elements failed it — each surviving on one reason, or none:

```text
placement / PlacementRef / with_placement   0 reasons  re-exported, never constructed or read
Line.hash / edition_hash / statement_hash   0 reasons  consumed only by the test that tested it
SurfaceLine.src                             0 reasons  assigned at construction, never read
render_line + four tarav1 hash re-exports   0 reasons  dead port surface
Line.at                                     1 weak     serialized, preserved by amend, never read
Check.default_on                            1 dead     no check set False; the branch never varied
BAR_CHECKS                                  1          one line of `poi explain` output
```

All are deleted. `identity.py` shrinks to the one thing tarav2 actually needs from tarav1 —
`split_statement` — which is the module's real reason: naming the port boundary in one place.

Two further items from the same audit:

- `Evaluator.AGENT` / `.USER` are now marked **provisional in the code**. They were shipped on
  one reason and defended in a note; the principle says name that at the site, not in prose
  somewhere else.
- `_check_support_resolves` mixed its constraint with a session cache. The cache moved behind
  `_SessionCache`, matching the shape `_check_coverage_converges` already had — the constraint
  is the body, the plumbing has a name.

**The growth rule was tested rather than assumed.** The `633` defect class — `IndexStore.put`
routing to a root no reader scans — was re-injected:

```python
target = IndexRoot(path=self.project_index_dir / "None", tier=tier)
```
```text
34 failed, 136 passed
```

The constraint is guarded. It is guarded by the tier-geography tests added later, not by a test
written for the defect, so the row exists without the discipline that should have produced it.

Records migrate to `tarav2.index-line-record.v3`: `links.placement` and `line.at` are gone.

```text
pytest   169 passed        ruff  All checks passed
depot    29 checks, 49 records, 0 errors, 1 blocked
```
