# POI.Linter.Knowledge.Module

How a `POI.Linter` run actually behaves. The concepts live in the index — `POI.Linter`,
`POI.System`, `POI.Check`, `POI.Class`, `POI.Instance`, `POI.Explain` in `design/107-design.md`,
and `Index.Linter` in `design/104-design.md`. This module is the operational layer beneath them:
what a run does, what its output means, and what it deliberately refuses to tell you.

`Index.Linter` is the reference realization and every example here is drawn from it. The shape
generalizes: any `POI.Linter` over any `Floor.Model` runs the same loop.

Canonical call:

```text
tarav index linter --project <root>
```

## What A Run Is

One run resolves its context once, selects a set of checks, executes them in registry order,
and returns one report. There is no incremental mode and no cache — a run is cheap because the
corpus loads in about a tenth of a second, and the expensive part is per-record archive reads,
which is what narrowing avoids.

```text
context     surfaces read, records loaded, standings computed  (resolved once)
selection   which checks run, given lane, selectors, and narrowing
execution   registry order; each check returns findings, never mutates
report      findings + blocked + blessed + one verdict per check
```

Checks fill the context as they go. `LintContext` starts empty and the structural tier is what
populates it, which is why registry order is load order and why a check that reads something
another check produces must be registered *after* it.

## Tiers And The Short Circuit

Two tiers, and the difference is not severity — it is whether later checks can mean anything.

- `structural` — the surface could not be read, or a record would not load. If a structural
  check produces anything, the run **stops there**. Later findings over an unparseable surface
  are noise, not signal.
- `reportable` — an ordinary finding that accumulates.

The structural tier is therefore never deselectable. `--check line-typed` still runs it, because
honouring that flag literally would run one check against an empty corpus and call the index
clean — which is the exact failure the whole selection mechanism exists to avoid.

## Three-Valued Verdicts

Every assertion returns one of three things, per check *and* per subject:

```text
passed     checked, and it holds
failed     checked, and it does not
blocked    could not check
```

`blocked` is the load-bearing one. Two-valued checking cannot distinguish "verified fine" from
"never looked", so it reports *clean* for an index nothing examined. The report counts the two
separately and prints them separately:

- `clean` — no failures. Says nothing about how much was checked.
- `verified` — no failures **and** nothing blocked.

A report with zero failures and eighteen blocked checks is a completely different epistemic
position from one with zero failures and everything checked. Read `verified`, not `clean`.

There is deliberately no `severity` field. Ranking what a finding *means* is the agent's work,
and a severity column is the route by which semantics gets smuggled back into the signal.

## What A Finding Carries

A finding names a computation and reports the values it compared. That is all.

```text
poi_class   the POI.Class identity, e.g. Index.Linter/Support.Unresolved
subject     what was examined
operands    the values the check compared
status      passed | failed | blocked
surface     where, when the finding is surface-bound
source      file:line of the check body -- computed, never written down
```

It carries **no prose reading of what it means** and **no prescribed remedy**. The reason is
that agents double-check from first principles, and they can only do that from operands rather
than from a sentence about the operands. A description would also be a stored copy of a
computable fact with nothing asserting it still holds — so the check body *is* the description,
and `source` points at it.

A finding's `identity` — the id used for blessing — hashes class, subject, and surface only.
Operands are excluded on purpose: values drift without the finding becoming a different
finding, and including them would evaporate a blessing the moment the thing it accepted moved
slightly.

## The Catalog

Growing the linter means adding a row to `CHECK_REGISTRY`, not adding a command. Thirty-four
rows today; `--list-checks` prints the live catalog and is the only trustworthy enumeration.

Each row carries:

- `name`, `tier`, and the check function
- `default_on` — a check may ship off when it is expensive or situational
- `resolutions` — the one field that is *not* derivable from the body. The code computes that
  something fired; it never computes what may legitimately be done about it. These are
  alternatives to choose between case by case, not a prescription.
- `gate` — an optional precondition the check cannot supply for itself
- `dev` / `replaces` — the dev lane, below

`record_scoped` is **read off the body**, not declared in the row: a check declares its scope by
iterating `selected_records()` or calling `is_selected()`, and the catalog storing that fact a
second time would be a copy with nothing keeping the two honest. The same applies to
`poi_classes`, derived from the literals the check names, and `source`.

## Selection

```text
--check <name>      run only this check; repeatable
--skip <name>       skip this check; repeatable
--label <cite>      narrow to one line by public citation; repeatable
--record-id <id>    narrow to one record edition; repeatable
--lane dev          run the dev lane
```

Narrowing by `--label`/`--record-id` produces a **targeted run**: only record-scoped checks
execute. A corpus check has no per-record answer to give, so asking it about one record and
discarding the rest would mean running the whole linter to throw most of it away.

Narrowing changes what is *examined*, never what is *known*. Records, labels, traces, and
standings stay whole — a check that must consult a record's trace siblings is not asking about
the selection, and narrowing the context would make a targeted run quietly answer a different
question than a full one.

A run that has narrowed at all is flagged `narrowed`. Any check reasoning about what did *not*
occur must refuse to answer on such a run: most of the corpus is unproduced by construction, so
every absence would look like a defect.

## Gates

A `gate` is a precondition the check cannot supply for itself — the chat archive is absent, the
project is not a git repository, the run was narrowed. When unmet the check reports `blocked`
**once**, with a reason, rather than emitting a blocked finding per subject.

## The Dev Lane

`--lane dev` selects checks marked `dev`. They are ordinary checks on ordinary machinery — same
signature, same findings, same verdict. All `dev` changes is *when they are selected*, and they
exist to make a chain runnable before its evidence can exist (a gate check accepting an agent
turn as the key, so the capture path can be exercised without a real user in the loop).

Two rules keep the lane honest:

- outside the lane a dev check is never selected, **not even by name**. A relaxed check that can
  be summoned into an ordinary run is one that will eventually be summoned by accident.
- inside the lane, each dev check displaces the check it `replaces`, so one constraint reports
  one verdict rather than two contradictory ones.

The report carries the dev check names rather than a boolean, so every caller has to decide what
to do about them. A dev run is a verdict about the machinery, not about the project.

## POI Class Identity

A `POI.Class` identity is the `Wayfinder.Reference` of its **one managed `$kw` block beside the
emitting code**. Not a catalog file, not a registry table — the block. Duplicate the block and
the identity becomes unresolvable; Wayfinder reports that it resolves more than once.

```text
tarav index explain --poi-class <address>
```

resolves that reference and presents the block. `POI.Explain` resolves and presents
documentation; it never copies or owns it.

This is why a markdown POI catalog chapter is optional and, for executable domains, retired: a
chapter would be a second place the identity lives, and the two would drift.

## Blessing An Instance

A blessing is the one thing allowed to stop a checker, so it is the last place an unevidenced
agent value could survive. What licenses it is not an approval token but the same thing that
licenses every other index line: **a free `Index.Line` plus a `User.Touched` support set**.

```text
tarav index bless --poi-id <id> --type DC --body "<why>" --session <s> --support <m>...
tarav index blessings [--poi-id <id>]
```

```text
poi        the POI instance this accepts
line       the agent's one-line explanation -- free, hosted by no surface
support    the user turns the agent claims license that explanation
```

Three consequences worth holding:

- **No validity flag.** Whether a blessing silences its POI is *derived* — `grounded`,
  `ungrounded`, `unresolved`, or `untouched` — and only `grounded` silences. An agent cannot
  write down that its own blessing is good.
- **No scope.** The explanation is a free line. Freeness is a property of the *host*, not a
  field on the line, so there is no scope to leave empty and no `ScopeKind` naming a POI. The
  blessing depot is simply never offered a placement check.
- **The hatch excludes itself.** A blessing cannot silence a blessing finding — that would
  answer the grounding requirement with another unevidenced claim.

Blessing is per instance. It never blesses the class, another instance, or a future occurrence,
and a blessed instance is reported as `blessed` rather than disappearing.

The support set is **not** a proof of relevance. Nothing mechanical can establish that these
turns license this application; that is the `Semantic.Assertion` the record exists to make
auditable later, and it is true of every support set in the system.

`Poi.Unlock.Token` and `Poi.Bless.Question` (`design/107-design.md`) are a future *gate* layered
on the act. They are not built, and they do not replace the support set that licenses the claim.

## Reading A Report

```text
by_class     grouped by check   -- a concentration reads as the system having drifted
by_subject   grouped by state   -- a concentration reads as one Bad.State
```

The linter groups and stops. Which of the two readings applies is semantic, and that is the
agent's work.

Counts move for two different reasons and conflating them is the common error: a count can fall
because the data was migrated, or because a check was removed or narrowed. Under
`Current.Model.Only` a checker recognizes no superseded model, so the count of non-conformant
items *is* the migration's progress measure — which only holds while the check itself is stable.

## Boundary

- a check never mutates anything; it returns findings
- a POI signals attention and prescribes no remedy
- the bar a retained line must reach is **typed** and **`User.Touched` grounded**; a line below
  the bar is work not yet done, not an error to reject
- the index is a `WIP.Surface`, so divergence is a signal to work and the linter never says
  which side is right
- rules may **overdetect** on purpose. A false positive is code successfully handing something
  up the ladder; asking an agent to find the error instead costs a semantic evaluation of
  everything, because establishing that something is fine is as expensive as finding it broken
- corpus counts prove execution, not correctness — each `POI.Class` still needs its own
  semantic review

## When To Load This Module

- interpreting a linter run, a POI instance, or a `blocked` verdict
- adding or modifying a check, or deciding which tier and gate it needs
- deciding whether to bless an instance, and what support the claim rests on
- reading corpus counts as a migration progress measure
