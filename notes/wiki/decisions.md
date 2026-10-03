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
<!-- tarav.breadcrumb df6407488f7898ed3afffdfad645eaa0d41b72a8c9ce69965b6af0f0b8790734 -->

## Blessing is one kind of Decision

A blessing is the decision that suppresses a POI. Decisions are broader: the
interventions we make to modify the system, which we collect and keep
continuously asserting. Some decisions are only reported: an opportunity to
encapsulate an action and capture it as a decision so it can be traced. Such a
decision captures its own context, for example Git commits and the diffs they
produce. Like the blessing implementation, a decision is assertable and can be
hooked into automatic scoring.
<!-- tarav.breadcrumb 3db06a8d811b205e62d1de8e5920a8d344dfa1b5b755efb2f8eb95b75a2c447b -->

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
<!-- tarav.breadcrumb faf4c55e9cf4c30f51a898d0d87353b1d903542f1db4c1d4286e8b9cedef3fe6 -->

Decisions are typed. Because the harness is Python code, each situation can
have its own type, handled differently by the scheduling system; if some
decisions show up too early and do not matter, more workflows can modify the
order. The present work defines the main scaffolding: the main decision
vectors.
<!-- tarav.breadcrumb 2cbd2b6de9da249f512bb928f0ea3a34dc7797d311be799107fa5d8bf649c9be -->

## Decisions are not scores

Scoring is the automatic, agent-evaluated path that assigns a number to each
assertion. User intervention is treated like agent output: the user can be
wrong, as an agent generating tokens can. Users are not scoring at the moment;
a scoring system with users as judges is a different conversation.
<!-- tarav.breadcrumb abe1fbe071902a8f5157441381ef3cd7a20402b7c8effbe3c855e03b8c6435e0 -->

The system that orders reassessment and spends resources (user attention,
agent tokens) may still give user decisions more authority than agent
decisions. That split should be quantitative.
<!-- tarav.breadcrumb 07d6fc4825d8f3d46ae57ee4d3aec1c01f353f70106fc3535277db75244bfc42 -->

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
<!-- tarav.breadcrumb 811f8c971a059772c3d3e8f66d45841c393ee5c39f29a4daec25b00abff2aa03 -->
<!-- tarav.breadcrumb 76922a6e4635f4259582009a60a23f8fd0bdaabc78e6142fb62da22eb731f43f -->

<!-- tarav.sessions
5a029cbf = claude-code:8c55cc60-f28a-439f-a6a0-0521567e600e @5a029cbf49a299c9709013b8ccb3fc517b2fb56fed373d3da819b6ea842afa2f
-->

## Only designed types in the core — 2026-10-03

Order and Reported action were discussed as hypothetical kinds of decision and
were never explicitly designed, so they do not belong yet in a workflow as core
as Decisions. They are to be deleted; nothing is implemented without a clear
need or design, and other Decision types can be defined later.
<!-- tarav.breadcrumb 664a8d75e709b365314195f2a394c1f55ea8846932a17947c0a64b7094260fe6 -->
<!-- tarav.breadcrumb c2a672f617ded053ddab709735d8efaeacea7b1fdef75c6957ec0b2fd74f587d -->

A Decision is a point in the ontology saying that the object exists. It is not
forced to have storage, and the Decisions workflow does not handle storage.
Where Decisions are kept is still to be designed and may depend on the workflow
or the project. One store for all the Decisions of a project, linked to the
Project workflow, is the first arrangement worth establishing; others can
follow.
<!-- tarav.breadcrumb ad60977b9d32c9d2398fafae6430ea5fc822f31c2fd83c82c3c3b62f46a150a2 -->
<!-- tarav.breadcrumb d8976147f1ace06e6093b1049f4f1a351f9167a4ca3d96ce329fa6ae07dc301d -->

Implemented in request 856: both types are removed, `Decision` prescribes no
concrete subtype, and `DecisionStore` holds only the types its caller
registers. The earlier paragraphs describing the two types are history. See
[856](../../../tarav-py/notes/live/856-remove-order-and-reported-action-impl-req.md).
