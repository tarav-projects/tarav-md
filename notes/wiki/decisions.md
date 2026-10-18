# Decisions

What we currently understand about Decisions: the recorded interventions that
users and agents make in a Tarav system. The discussion arose while
redesigning g70203 on Tarav; its project-side record is
`g70203-project/g70203-md/notes/wiki/attention-and-decisions.md`. The design
sections below preserve that discussion; the implementation snapshot is
separate.

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
64298cbc = claude-code:9da4cef5-68b7-4d17-8a06-1351ca51e82f @64298cbc8db2e7aa971e0828653c07bcb483cfed40931fdf87d5abe7ce1c60b3
-->

## Decisions must never be permanent

A system that asks the user to decide fails if a decision becomes permanent:
if the user made a mistake, the problem never comes back. Detection is
separated from decision. Every recorded decision is re-evaluated, at
different priorities: a decided problem returns after about a month for a
second opinion, and each reapproval extends the interval (say three months)
up to a maximum of about a year.
<!-- tarav.breadcrumb df6407488f78 -->

## Blessing is one kind of Decision

A blessing is the decision that suppresses a POI. Decisions are broader: the
interventions we make to modify the system, which we collect and keep
continuously asserting. Some decisions are only reported: an opportunity to
encapsulate an action and capture it as a decision so it can be traced. Such a
decision captures its own context, for example Git commits and the diffs they
produce. Like the blessing implementation, a decision is assertable and can be
hooked into automatic scoring.
<!-- tarav.breadcrumb 3db06a8d811b -->

```text
Decision: an intervention in the system, recorded and asserted over time
├── Blessing: suppresses (defers) a still-detected POI
├── Order: changes the data; its consequences are public
└── Reported action: captured for tracing (context, commits, diffs)
```

## Orders and blessings are asymmetric

An order's consequences live in the data itself, which is public and used by
everyone else, so a wrong order has a greater chance of being discovered. A
blessing instead recognizes a live POI and suppresses it. A decision that
modified the data and caused a POI does not suppress that POI. Decisions with
no live POI linked to them need their own priority policy, to be worked out
later.
<!-- tarav.breadcrumb faf4c55e9cf4 -->

Decisions are typed. Because the harness is Python code, each situation can
have its own type, handled differently by the scheduling system; if some
decisions show up too early and do not matter, more workflows can modify the
order. The present work defines the main scaffolding: the main decision
vectors.
<!-- tarav.breadcrumb 2cbd2b6de9da -->

## Decisions are not scores

Scoring is the automatic, agent-evaluated path that assigns a number to each
assertion. User intervention is treated like agent output: the user can be
wrong, as an agent generating tokens can. Users are not scoring at the moment;
a scoring system with users as judges is a different conversation.
<!-- tarav.breadcrumb abe1fbe07190 -->

The system that orders reassessment and spends resources (user attention,
agent tokens) may still give user decisions more authority than agent
decisions. That split should be quantitative.
<!-- tarav.breadcrumb 07d6fc4825d8 -->

## Agent suggestions, not yet decided

- Keep the base Decision almost empty, like the base POI; scheduling behaviour
  lives in subtypes.
- Record the decider (user or agent) on every Decision, as an input to the
  attention policy's authority weighting.
- A reported action could wrap the existing commit-evidence record rather
  than define a new one.
- Orders could still keep who decided and on what evidence, so a wrong order
  is traceable when its data is later found wrong.

## First implementation slice

Request 854 established `Decision` as the common attributed, Assertable
record. `BlessingRecord` inherits it without changing its Type identity or
stored schema: the retained `actor` is exposed as a `decider` accessor. `Order`
and `ReportedAction` retain subjects and optional tracked-POI identities.
Their generic main Assertion identifies the account, but no assessment case or
attention schedule is prescribed yet. This implements the type relationship,
not the broader claim that every Decision is already re-evaluated over time.
See `tarav-py/src/tarav/l1/decisions/`,
`tarav-py/src/tarav/l1/blessings/store.py`, and the tests in
`tarav-py/tests/decisions/`.
<!-- tarav.breadcrumb 811f8c971a05 -->
<!-- tarav.breadcrumb 76922a6e4635 -->

<!-- tarav.sessions
5a029cbf = claude-code:8c55cc60-f28a-439f-a6a0-0521567e600e @5a029cbf49a299c9709013b8ccb3fc517b2fb56fed373d3da819b6ea842afa2f
-->

## Only designed types in the core — 2026-10-03

Order and Reported action were discussed as hypothetical kinds of decision and
were never explicitly designed, so they do not belong yet in a workflow as core
as Decisions. They are to be deleted; nothing is implemented without a clear
need or design, and other Decision types can be defined later.
<!-- tarav.breadcrumb 664a8d75e709 -->
<!-- tarav.breadcrumb c2a672f617de -->

A Decision is a point in the ontology saying that the object exists. It is not
forced to have storage, and the Decisions workflow does not handle storage.
Where Decisions are kept is still to be designed and may depend on the workflow
or the project. One store for all the Decisions of a project, linked to the
Project workflow, is the first arrangement worth establishing; others can
follow.
<!-- tarav.breadcrumb ad60977b9d32 -->
<!-- tarav.breadcrumb d8976147f1ac -->

Implemented in request 856: both types are removed, `Decision` prescribes no
concrete subtype, and `DecisionStore` holds only the types its caller
registers. The earlier paragraphs describing the two types are history. See
[856](../../../tarav-py/notes/live/856-remove-order-and-reported-action-impl-req.md).

## The Project's Decision store — request 857

Each Project has a storage solution for its Decisions, and everything that is
a subtype of Decision has this place. Workflows may keep theirs elsewhere, but
what is tracked as the Project's decisions is what is put in this store.
<!-- tarav.breadcrumb 02351e02102a -->

Blessings attached to a Project go there by default. The types differ and the
location is shared; a general filter by Type, subtypes included, serves them
all.
<!-- tarav.breadcrumb c1f0261c96fb -->

Implementation: `Project.decisions()` opens `ProjectDecisions`
(`tarav-py/src/tarav/l2/project/decisions.py`) over `.tarav/decisions/`, one
append-only file per Record. `snapshot(decision_type=...)` selects a Type and
its subtypes through the registered Record types; an unregistered type is a
finding. `blessings()` returns a `BlessingStore` over the same directory, so
standing is computed as before. `DecisionStore` is gone from the Decisions
workflow, which owns no storage, and `Project.poi_board()` reads this store.
Existing blessing stores were not migrated. See
[857](../../../tarav-py/notes/live/857-project-decision-store-impl-req.md).
