# POI visibility, navigation, and blessings

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
1ae20f8c = codex:01a0ff32-0ec2-7b72-8850-fa795135f3c9 @1ae20f8c8159f12d2402ea702cf49c876ec46a72f71ce12423ae1dbdf2a91871
64298cbc = claude-code:9da4cef5-68b7-4d17-8a06-1351ca51e82f @64298cbc8db2e7aa971e0828653c07bcb483cfed40931fdf87d5abe7ce1c60b3
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## Current design direction — 2026-10-09

This note is a history: its sections were written as the design moved, and
several describe mechanisms the design has since left. The User asked that
the Wiki state the current design and not only append to it.
<!-- tarav.breadcrumb 5a3d45aa9a03 -->

Where the design stands (updated 2026-10-11):

- A POI is a flag between detecting and working: what a check returns. It
  is momentary and owns nothing; nothing stores a POI that was printed.
- The model has three levels and no optional parts. A `POI` has a Type and a
  message. A `SituationPOI` adds a situation, an object describing what was
  found; each line of POIs decides what goes into it, and the Type plus the
  situation is the identity. A specialization adds fields of its own Type.
  There is no subject and no evidence at the base.
- A consumer decides what happens to a POI. Printing is how a person looks
  at checks directly. The Project status escalates: what its checks raise
  becomes actions. A running step keeps the POIs of its tests as the reason
  it could not close. Actions are the unit of work.
- What integrates several workflows, such as blessing or asking how an
  action stands, is modeled on the Project. The status reads only actions.
- An actionable POI spins one action. That run is the persistent thing that
  was called a tracked POI. Its identity comes from its Type and its POI.
- An action is registered under a Project. Three pieces stay apart:
  `project.checks` only runs checks, `project.actions` only handles the
  registered actions, and the Project composes them. The Project hands the
  suite that ran to its actions; each Action Type decides what the results
  mean for it. A container Project asks each child to do the same for
  itself. A run that no Project hands over is momentary.
- A suite is a detector. It is a class with an identity; it does not contain
  checks but the code that runs them, because the checks cannot be listed
  beforehand; and it holds the results of its one run. It can run whole or
  filtered. An action keeps the suites above the check that raised its POI,
  and closes as gone when the nearest of them that ran no longer reports it.
- `tarav status --project` runs the composition and is the command to repeat.
  It leaves slow suites out, such as a Project's tests; `--all` runs
  everything. `tarav check` only runs the checks.
- Every closing leaves a typed record, and that Type decides whether the POI
  raised again reopens the action. A Blessing is one such record: the action
  is closed although the situation still exists.
- Status is three axes: the situation (present, absent, check failed), the
  action, the closing.
- Tarav commands print a readable summary by default and the full result
  with `--json`, from one model.
- Guidance about what to do belongs to the action and its skill.

The last three sections of this note, "A POI is an event; what follows it is
an action", "Suites, closing records and the blessing as a closing" and "The
suite is the Project's own set of checks", hold the discussion. What that makes of the earlier sections:

| Section | Standing |
| --- | --- |
| Detection, navigation, situation identity, atomic types, reported POIs | Current. |
| Recorded blessings; composable blessings | History. The blessing store and its records were removed by request 896. A Blessing is now the closing record of a POI's action. |
| Revisable blessing attention | Current in purpose, reduced: the attention view reads the Blessing of each action. Counting several independent reviews of one POI is gone, since an action has one current Blessing. |
| Tracked POIs, the board; POI tracking with status axes; record status changes only | History. The tracking code was removed by request 894: the record is now an action in the central registry, and its history is that registry's Git history. |
| Neutral POIs and the producer–reader gap | Current. Request 893 removed the two fields; a Type's descriptive notes appear in the POI's context, and an action's skill says what to do. |
| "What was built from it" (2026-10-09): dismissal, the subject key, clear results | Replaced on 2026-10-11 by blessing, suites and closing records. |
| "Suites" and "What was built" of 2026-10-11 (request 896): a separate suite Type named by the caller, with a target | Replaced the same day by request 897: the suite is the Project's own check suite. The closing records and the Blessing stand. |

## Detection and presentation

### Points of interest, not inherently problems

A POI is a claim that something is of interest. It does not inherently imply
negativity, failure, or a required corrective action. This clarification
broadens the problem-oriented examples elsewhere in this note.
<!-- tarav.breadcrumb 8abe33d8f103 -->

The base POI has two initial specializations: `CheckPOI`, coupled to the bound
Check object that produced it, and `NotificationPOI`, reporting an event or
operation worth making visible without requiring a Check. In Breadcrumb
auditing, a stale position is the first case; appending a location observation
is the second. `NotificationPOI` is the selected name, replacing the tentative
`LogPOI`.
<!-- tarav.breadcrumb 7690a9f80fa8 -->
<!-- tarav.breadcrumb b415403c3774 -->
<!-- tarav.breadcrumb d697c96ab0ef -->

Check code raises only failure POIs by default. That is a checking convention,
not a restriction on POI meaning; positive results can also be points of
interest. The [Checks workflow](checks-workflow.md) owns the Check-coupled
specialization while sharing the general POI base. Notification mechanics
may use lighter context, such as creation and raise locations; their exact
schema remains open.
<!-- tarav.breadcrumb f8f7a8a5028c -->
<!-- tarav.breadcrumb 6a9a8c7a5a33 -->

Detection retains all findings, including blessed ones. Presentation defaults
to all POIs in scope, with compact counts/grouping and bounded pages. Agents
can selectively expand evidence, check code, documentation, or blessing
records. This separates full finding visibility from how much material enters
the agent's context.
<!-- tarav.breadcrumb d4ecde7c9dca -->

POIs are analogous to automatic issues. Their existence does not mean an agent
must address all of them during every task. Users and agents choose which
findings to address for a particular workflow; navigation should protect the
agent's context from being flooded.
<!-- tarav.breadcrumb 1de53d518bed -->

## Minimal navigation

An agent facing a POI needs a route to understand what it checks and where its
documentation lives. The initial navigation primitive can simply point to the
path of the POI class. A richer navigation interface is not a prerequisite for
providing that entry point.
<!-- tarav.breadcrumb 91344e5ea648 -->
<!-- tarav.breadcrumb 2e48db834bb5 -->

## Recorded blessings and permitted resolutions

*As design, overtaken on 2026-10-09: blessing becomes the dismissal close path
of the POI's action. The blessing code still exists beside dismissal.*

### Minimal base and specialization ownership

Keep the shared POI base almost empty for now. Check-coupled semantics belong
on CheckPOI rather than becoming requirements for every point of interest.
NotificationPOI belongs directly to the POI workflow for the moment. The
foundation and Breadcrumb integration are planned in
[request 832](../../../tarav-py/notes/live/832-neutral-pois-checks-and-breadcrumb-audits-impl-req.md).
<!-- tarav.breadcrumb 84bbfb38d647 -->
<!-- tarav.breadcrumb 32cd6269b377 -->

### Neutral foundation implemented

Request 832 implemented the nearly empty `POI`, POI-owned
`NotificationPOI`, and Checks-owned `CheckPOI`. Every `CheckPOI` retains its
bound runtime `Check`; a completed `CheckResult` may therefore contain failure
POIs without confusing validation outcome with execution failure. Breadcrumb
file and commit audits now return one mixed POI stream: unresolved concerns are
CheckPOIs, while successful opt-in position refreshes are NotificationPOIs and
do not fail the audit.
<!-- tarav.breadcrumb 25a3d8ca9b83 -->

POI diagnostic payloads do not occupy the `context` attribute. The normal
`TaravObject.context()` entry point remains callable and exposes diagnostic
details and, for a `CheckPOI`, its exact bound Check through `obj_context`.
<!-- tarav.breadcrumb ce67a9ca6579 -->

The existing SKW `POICheck`/`POIInstance` finding model remains operational and
will migrate separately. Request 832 changes only its import boundary; it does
not reinterpret retained SKW finding Records.
<!-- tarav.breadcrumb 76e537d68e30 -->

A blessing is an agent action accepting the state as valid despite a raised
POI. Blessing actions must be recorded so they can be scored. A blessed POI
remains visible, marked as blessed rather than disappearing from the findings.
<!-- tarav.breadcrumb 8dd9d281d745 -->
<!-- tarav.breadcrumb dbcc606ac63b -->

Not every POI is blessable. Some represent errors whose intended resolution is
fixing the analyzed surface. The blessing system must preserve that distinction.
These are design requirements; this capture does not assert a completed
implementation or settle the blessing Record schema.
<!-- tarav.breadcrumb a97b61b83a06 -->

## Workflow-owned types and composable blessings

The first migration pass should define POIs in the workflows producing them,
subtyping the common POI base while preserving existing detection mechanics.
Blessing semantics belong to a separate workflow with a BlessablePOI base,
rather than becoming requirements for every POI.
<!-- tarav.breadcrumb 9448bf2344fe -->

A concrete workflow-owned POI may inherit both CheckPOI and BlessablePOI.
The accepted example is StaleGenerationPOI(CheckPOI, BlessablePOI), owned by
SKW: checking and blessing capabilities compose without changing its owner.
This establishes a modeling pattern, not universal permission to bless every
check outcome. [Request 833](../../../tarav-py/notes/live/833-workflow-owned-pois-and-blessings-impl-req.md)
plans the follow-up migration after 832.
<!-- tarav.breadcrumb 172e9cb5c362 -->
<!-- tarav.breadcrumb 3040b3d79f5a -->

### Workflow migration implemented

[Request 833](../../../tarav-py/notes/live/833-workflow-owned-pois-and-blessings-impl-req.md)
implemented the migration. POI now supplies neutral, identified, notification,
and collection foundations. References, Navigation, Skills, SKW, Breadcrumbs,
Archive, and provisional Diagram reporting use workflow-owned concrete POIs;
the old kernel occurrence marker and parallel POI check/occurrence types were
removed.
<!-- tarav.breadcrumb 6f11b15dfaa3 -->

Blessings are now an independent workflow. `BlessablePOI` is the capability:
a concrete POI is blessable only when its class inherits it. The implementation
does not retain an occurrence-level boolean or an old generic occurrence model.
Check-owned behavior composes with blessability through multiple inheritance,
while the concrete workflow remains the semantic owner.
<!-- tarav.breadcrumb 6d32637f2a47 -->

Typed notifications now have shared delivery. They warn once by default or are
captured explicitly without duplicate delivery. Archive uses this path for a
skipped suspicious remote while preserving its ordinary artifact return value.
<!-- tarav.breadcrumb 5791a5f84456 -->

### 2026-10-01 — Situation is the identity input

The next design replaces the separate identity/state model described above.
An identified POI is identified by its concrete class Ship and an explicit
caller-supplied `situation`. Blessings are one application of that identity,
not its definition. There is no second POI state under the same identity.
Producers decide which inputs distinguish situations; prefer a concern
resurfacing for reblessing over accidentally treating a new concern as blessed.
<!-- tarav.breadcrumb 6b9ffe48e00b -->
<!-- tarav.breadcrumb c31b79dbad09 -->

A producer can represent recurring equivalent situations or intentionally
fresh occurrences. The situation must be a LiteRecord: dictionary-shaped data
whose accepted values have controlled serialization. Supported native values,
such as dates and Tarav Types, need not be manually converted by callers.
Unsupported objects are not accepted merely because they can be stringified.
<!-- tarav.breadcrumb a3381fa6a0ac -->
<!-- tarav.breadcrumb 06d3860c914c -->
<!-- tarav.breadcrumb 367513415a77 -->

[Request 834](../../../tarav-py/notes/live/834-situation-poi-identity-and-lite-records-impl-req.md)
carries the implementation plan. This section records the new design, not a
claim that the current implementation already follows it.

### Situation identity implemented

Request 834 implemented `LiteRecord` as the controlled, deterministic value
contract for caller-declared situations. `IdentifiedPOI` now derives identity
from its concrete class Ship and explicit situation; evidence and presentation
remain outside identity, while producers include revision inputs when a changed
surface must produce a new situation.
<!-- tarav.breadcrumb 1025bc0dd537 -->

Repeated emissions of one situation remain distinct report occurrences. A
collector addresses them by the stable situation identity plus a zero-based,
evaluation-local emission index. The index is navigation data and does not
participate in identity or blessing.
<!-- tarav.breadcrumb 849ab6b37feb -->

Blessings now retain and validate the situation identity directly, with only
`blessed` and `unblessed` standing. CLI inspection exposes occurrence indexes,
and the implementation is documented and verified in Request 834.
<!-- tarav.breadcrumb 8110cf98d019 -->

## Revisable blessing attention

Detection remains authoritative about whether a POI still exists. A blessing
accepts that exact situation for now, without erasing it. An attention view
can defer a still-detected, reviewed POI, show when its next review is due,
and always let an agent inspect or force review of deferred entries. A POI
that no longer appears in the current evaluation has no attention schedule.
<!-- tarav.breadcrumb def8b47d7f1b -->
<!-- tarav.breadcrumb ebad637d2356 -->

Request [849](../../../tarav-py/notes/live/849-blessing-attention-and-reassessment-impl-req.md)
implemented a separate pageable `attention_report` over a current collector,
BlessingStore, and ScoringRepository. Its pilot policy defers a first or weakly
assessed blessing briefly. A sufficiently sampled favorable *relative* score
can extend that interval, and only separately scored reviews by distinct
actors with explicitly disjoint source groups extend it further, within a cap.
Score, coverage, review count, and due time remain separate signals; none is a
truth verdict. The existing full POI report and binary standing remain intact.
The product commit is `e419920`; 63 focused and 155 configured Python tests
passed.
<!-- tarav.breadcrumb d2354eb4a3b6 -->
<!-- tarav.breadcrumb 751d3074eb14 -->

## Tracked POIs, the board, and attention

From the g70203 redesign discussion; see also [Decisions](decisions.md).

"Attention" names the workflow, or workflows, that rank and sort POIs. Many
words mean nearly the same thing with different nuances; naming will settle
with time.
<!-- tarav.breadcrumb 55af6d704dae -->

The engine produces POIs, events we record. Recorded POIs are like GitHub
issues: explicit, and they need resolving — closed, ignored, and so on. Some
are not under agent control (a check ran and failed); others are introduced by
the agent. A board, like GitHub's, lets agents and any workflow see and filter
POIs, for example the unresolved POIs of their own workflow. Blessings and
other decisions attach to recorded POIs. A system that generates POIs and
prompts the agent to resolve them is already a driving force; with evaluation
and automatic scoring it starts to run by itself, as md-library begins to.
<!-- tarav.breadcrumb cb2ffc8a73a7 -->

Not every POI is recorded; that is the workflow implementer's choice. Some are
just notifications, for instance in the command line, and still use the POI
system for contextualization, Diagram integration, and knowing which checker
produced them. "Issue" was a candidate name for the recorded ones but
suggests something wrong. The agent proposed **tracked POI** (tracking as a
property, not a new noun) and the User chose it.
<!-- tarav.breadcrumb 0ebb27abb363 -->
<!-- tarav.breadcrumb aba381da3ffc -->

POIs are typed and can express any axes we need. `CheckPOI` forces a companion
Check class, so it is clear which check failed; `NotificationPOI` is raised
text. Both share the common POI features, and more types will come as new
functionality is discovered. Being tracked is a separate axis from these
types.
<!-- tarav.breadcrumb 8b3336827f9f -->

### First tracking and board slice

Request 854 added optional `TrackedPOI` records at a caller-selected root.
An identified POI is tracked by its situation identity; completed evaluations
of its exact declared scope can update detection and history. Absence from an
incomplete run or another scope changes nothing. The pageable board filters by
workflow, type, detection, disposition, and subject. It may join Blessings and
other Decisions, but a Blessing never changes detection: a still-detected POI
remains visible. The initial disposition view distinguishes blessed from
unreviewed; broader attention policy is later work. See
`tarav-py/src/tarav/l1/poi/tracking.py`, `tarav-py/src/tarav/l2/poi/board.py`,
and `tarav-py/tests/decisions/`.
<!-- tarav.breadcrumb 2bb73a07d0cb -->
<!-- tarav.breadcrumb b124ef563fb1 -->

## Reported POIs and their context — 2026-10-08

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

While reviewing the bootstrap POIs, the full record of a POI was only reachable by writing a script. The User took this as evidence that any presentation of data must give the agent a clear way to escalate to full context, because an agent should not act on limited context, and that guards may be added later. The expansion should be central instead of implemented by each surface, and the connection should itself be checkable, so that its absence is a POI.
<!-- tarav.breadcrumb 2693f678cb96 -->
<!-- tarav.breadcrumb d67600570d36 -->

The POI life cycle is: a POI is shown with its identifier and a short message, and the agent is told explicitly that before doing anything with any POI it must open its context, and how. That instruction is stated once per output, with the command, placeholders, an example and a pointer to help. Arguments are explicit key/value. The view is named for a POI that has been presented, not just "poi". The POIs currently reported on Tarav are not repaired; they are the test bench.
<!-- tarav.breadcrumb e56c308512a6 -->
<!-- tarav.breadcrumb 978b9c97f5aa -->
<!-- tarav.breadcrumb 9a060f83b08b -->

Implemented in `tarav-py` commit `4289796`. `tarav check --project` retains what it reported under `~/.tarav/check-reports/`, and every report with POIs opens with the instruction and an example. `tarav context --id <poi-id> --view reported-poi` lists `poi-type`, `raised-by`, `finding`, `read-first` and `may-do`. A POI Type declares `read_first` and `may_do`; the seven bootstrap POI types do, as the worked example. Two checks run where the POI base Type is developed: a reminder for each POI Type without guidance (48 today, left in place) and a round trip from the advertised example to the view. The view name, the retention place and the omission of an earlier-actions entry were agent choices. [Impl.Req 876](../../../tarav-py/notes/live/876-context-command-and-reported-poi-impl-req.md) has the detail.
<!-- tarav.breadcrumb 9fa116eb350f -->

## Atomic POI types — 2026-10-08

Reading a reported POI through the context command, the User met a `code` field and asked what it was for. A search of the POI design sessions found no User turn asking for it: it came from the index linter of May 2026 as a rule label and was carried into the neutral POI base by request 832 without discussion. The User asked for it to be eliminated.
<!-- tarav.breadcrumb 26fb5d73cc1c -->
<!-- tarav.breadcrumb a91da531e00a -->

The decision: POIs are atomic. Each POI type describes one situation and there is no further degeneracy inside a type; the field was an inherited linter habit duplicating the type system.
<!-- tarav.breadcrumb c7aba3389e08 -->

A family parent that is never raised may remain so related cases can be selected together, because in Tarav the typing system expresses semantics. The base type loses the argument, every multi-case type is split into one class per case, checks stop copying the code into the situation, and reports group by type instead of code.
<!-- tarav.breadcrumb 0281a7a663e9 -->

[Impl.Req 877](../../../tarav-py/notes/live/877-atomic-poi-types-impl-req.md) implemented it in `tarav-py` commit `9559db7`: fourteen families became 88 case types, and `tarav check` lost `--by code` and `--code`. Three older finding classes that subclass the bare `POI` (`BreadcrumbFinding`, `ReferenceFinding`, the Diagram `Finding`) still carry a code and are a follow-up. Guidance reminders rose from 48 to 93 on the Taravangian root because each atomic type without guidance is now reported separately.
<!-- tarav.breadcrumb fe5f488b2279 -->

## Shared presentation and further POI integration — 2026-10-08

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

The User accepted a common presentation path: a POI Type supplies one POI's meaning, selection fixes the page before rendering, and a named renderer lays out that page and tells the agent how to open full context. Surfaces select a renderer by name; the default and JSON-lines presentations support line, record, and context levels. The connection from a displayed identifier to context is itself checked.
<!-- tarav.breadcrumb 943d1c7cf40b -->
<!-- tarav.breadcrumb a73e6a566f61 -->

[Impl.Req 879](../../../tarav-py/notes/live/879-one-poi-system-and-rendering-impl-req.md) integrates `tarav check`, Skillware POI reports, and Breadcrumb audit output with that renderer contract. Breadcrumb and Reference resolution now use atomic identified POI families. A displayed identified POI is retained so its advertised `tarav context` path can open the reported occurrence. Chatlas query matches and low-level record observations were renamed as plain data, rather than treated as POIs. The Diagram's coded `Finding` remains: Capture Receipt records retain its `code` shape, so its conversion needs a separate typed-case and data-migration pass.
<!-- tarav.breadcrumb 4278a7af9829 -->
<!-- tarav.breadcrumb 99eded3fcfc8 -->

## POI tracking: records with status axes — 2026-10-08

*Overtaken on 2026-10-09 and removed from the code by request 894: the
tracking record became an action. This section is history.*

This section replaces the mechanics of "Tracked POIs, the board, and attention"
above. That earlier text stays as the history of the first design.

The User decided that tracking is a capability and that every check POI is
tracked by default, because a check POI is defined by its situation. The
trackable class has a setting that can disable a particular instance. POI
tracking is its own workflow; the User does not love the name and kept it for
now.
<!-- tarav.breadcrumb 816354d3714c -->

The check run is where tracking integrates. A run starts from the beginning,
so it gives the tracking system a new data point. It has to register the
positive sign, a POI was raised, and the negative sign: the owning check
finished and did not raise it, "the check passed". The User rejected the word
"board" for this: it is a record system that tracks the state of POIs.
<!-- tarav.breadcrumb 5fe3457a6a93 -->

Status is a vector, not one value. "Passed" is one status on one axis and does
not prevent closing a POI or saying more about it. The store is a database of
every POI ever tracked, like the issues of a GitHub repository: records stay,
can be referenced, and can be discussed indefinitely.
<!-- tarav.breadcrumb d9ad9ba94552 -->

Blessing is one of the axes. Workflows can add their own, several axes may
speak about related things, and that overlap is accepted on purpose. The aim
is a system flexible enough to express everything, to be formalized and
simplified later. The earlier tracking code was inspiration only and could be
redesigned from the ground up.
<!-- tarav.breadcrumb b5049e5e5d6a -->
<!-- tarav.breadcrumb 75e6fd8732d1 -->

### Implemented

[Impl.Req 883](../../../tarav-py/notes/live/883-poi-tracking-workflow-impl-req.md)
built this in `tarav-py`, commit `0d524e2`.

- `tarav.l1.poi_tracking` owns the workflow. `TrackablePOI` is the capability;
  `CheckPOI` extends it. One `TrackRecord` per POI identity is kept in a
  `TrackRecordStore`, and nothing deletes a record.
- A record holds the POI snapshot, the owning check with its identity, and
  `axes`. Each axis entry has its Type, owner workflow, value, the time since
  it holds, and its own history of changes with what made each one. The
  tracker stores and filters axes and does not interpret them. A workflow
  adds one by subtyping `TrackAxis`.
- `Check.identity` says which check this is across runs. A `SituationCheck`
  derives it from its Type and situation; a plain `Check` returns nothing
  unless it declares one.
- `CheckRun.track(into=tracker)` turns each `CheckResult` into one data point.
  A raised POI is `active`. A record whose owning check completed without
  raising it is `passed`. A check that did not complete, did not run, or has
  no identity gives no evidence, and the record reads `not-evaluated`.
- The blessing axis lives in `tarav.l2.blessings.tracking` and reads the
  unchanged blessing store. A read shows the current blessing without writing;
  the next observation puts the change into the axis history.
- A Project's records live in `.tarav/poi-tracking/`. `tarav check --project`
  writes them and `--tracking skip` leaves them alone. `tarav poi tracking list
  --project --axis observation=passed` filters, and `tarav context --id
  <poi-id> --view tracked-poi` opens one record.
- Tests: `tests/test_poi_tracking.py`, 10 tests; the suite passed 232 tests in
  the shared worktree and 222 on the exact commit tree, and Ruff passed.
<!-- tarav.breadcrumb 48116b703134 -->

### What the first real run showed

Two runs of `tarav check --project` on the root wrote 149 records for 151
reported POIs. Only 14 of them belong to a check that states an identity
(`Tarav.SKW.Check.ContextFreshness`). The other 135 come from four checks
without one, so they can never read `passed`; when one stops being raised it
will read `not-evaluated`. Giving those checks an identity is follow-up work.

### Agent choices and open questions

These were chosen by the agent, not decided by the User.

- The per-instance switch works only for a POI Type that lists `TrackablePOI`
  in `settings_include`, because the settings capability includes a parent's
  settings only explicitly.
- The record stores the last-active and last-evaluated times, so every check
  run rewrites every evaluated record. In a Project under Git that leaves the
  tree modified after each check.
- The store is inside the Project, and a child Project checked through its
  root is tracked in the root's store.
- The machine-local check-report cache stays. It holds what a surface last
  showed; the tracking store is durable Project state.

Left for later: a manual disposition axis, a discussion thread on a record,
links between records, a scoring axis, notifications when axes disagree, and
retirement rules.

### Record status changes only — 2026-10-08

The User rejected the rewrite on every run. Repeating a check whose POIs did
not change must not touch the store: tracking records changes of state, not a
refreshed timestamp, and it is append-only. A record keeps the moment each
change was detected; the latest entry is the last change, not the latest run.
<!-- tarav.breadcrumb 13aaea0e57f1 -->

The User also asked to keep it simple, with zero smartness in the code and no
event system. The tracker builds one explicit object per POI describing its
current tracking situation, the status it assigns, in the same way a check
declares a situation for POI identity. It hashes that object and compares the
hash with the last recorded one. Equal hashes write nothing; a different hash
appends one entry. The hashed object is stored beside its hash, so what was
hashed stays explicit.
<!-- tarav.breadcrumb d43f415e15e1 -->

Agent reading of the 883 code, not yet decided or built: the rewrite comes
from the `last_active_at` and `last_evaluated_at` times, which would go; the
per-axis histories would become one list of entries per record; the POI copy
in a record would be refreshed only when an entry is appended, so a changed
count in a message alone changes nothing. Blessing stays an axis inside the
situation, so a new blessing enters the record at the next check run.
## Diagram POIs and retained Drafts

The Diagram now raises atomic identified POIs. Its 81 concrete cases sit under twelve
family Types and the shared `Tarav.Diagram.POI` parent. Each case's Type and path
define identity; the message and evidence explain the current observation.
The family Types are grouping points and cannot be raised. Capture Receipts and
Diagram command JSON retain `pois` with `type`, `path`, and `message` per row.
Commands use the shared POI renderer and retain displayed POIs for Context.
<!-- tarav.breadcrumb 067092b81400 -->
<!-- tarav.breadcrumb 2666bd852678 -->
<!-- tarav.breadcrumb 434a6263ff78 -->

Draft schema 2 holds those typed receipt rows. The explicit
`tarav diagram draft migrate --to 2` operation maps version-1 rows; the reader
does not translate them. Before migration, 53 Drafts held 13,347 coded rows in
50 receipts. A dated sibling backup was made, the migration reported no unmapped
rows, and all 53 Drafts and 13,347 rehydrated POIs loaded afterward. See
[Impl.Req 881](../../../tarav-py/notes/live/881-diagram-poi-atomic-types-impl-req.md).
<!-- tarav.breadcrumb 7999d9e48b0d -->

## Check report filtering and batch Breadcrumb audits

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

`tarav check --type NAME` selects POIs whose Type is `NAME` or descends from
it. The report states how many POIs matched out of the full run; filtering
changes presentation, while tracking, retention, and the command's exit status
still reflect the entire run. `--check` remains a report filter by exact Check
Type name. Group pagination applies after selection.
<!-- tarav.breadcrumb 6bf9b64281e5 -->

`tarav breadcrumbs audit chatlas-context` accepts repeated `--surface` paths
or `--files-from` with one path per line. The command audits each selected file,
returns a result for each, and can refresh uniquely located stale positions in
one pass. A missing file is reported beside successful files. The manifest
mechanic does not choose which User Turns are relevant to a surface; that
judgment remains with the agent. See [Impl.Req 884](../../../tarav-py/notes/live/884-check-poi-filter-and-breadcrumb-batch-audit-impl-req.md).
<!-- tarav.breadcrumb 94da2d7f8b1f -->

## Diagram POI completion

Request 881's follow-up covered the twelve Diagram POI families through their
emitting methods. The separate `tarav diagram render` content command now
retains its typed POIs and displays them through the shared POI renderer. Its
`--renderer` still selects Diagram content; `--poi-renderer` and `--level`
select POI presentation. The command's JSON output retains typed POI rows.
The retained Draft migration remained intact: 53 version-2 Drafts and 13,347
typed receipt POIs, with no coded rows. [Impl.Req 881](../../../tarav-py/notes/live/881-diagram-poi-atomic-types-impl-req.md)
records the verification and the existing Project and Skillware POIs that are
outside its repair scope.
<!-- tarav.breadcrumb 256e980bf25b -->

## Neutral POIs and the producer–reader gap — 2026-10-09

An open design discussion; nothing here is implemented. The full thread is in
[Operator Context, Directives and Harnessed Actions](operator-context.md).

The User looked for first-principle arguments for the current POI design,
compared with Python's exception system.
<!-- tarav.breadcrumb 0def7e3aa8e7 -->

A POI connects above all to the code and the situation that produced it. It
narrows the gap between producer and reader, making the producer's intention
clear so the reader can judge. The producer cannot know the reader's goal and
the design does not pretend to.
<!-- tarav.breadcrumb c2b80891fb46 -->

Directions the User set:

- A general `.throw()` on POIs, raising the POI as an exception that carries
  the whole POI. Today only `CheckPOI.error()` does this
  (`tarav-py/src/tarav/l1/checks/__init__.py`), through `POIError`.
<!-- tarav.breadcrumb 2e42c09421a1 -->
<!-- tarav.breadcrumb f1457b7d3440 -->
- POI wording is descriptive, not imperative (`Workflow.Neutral`). "What to
  do" belongs to the skill that contextualizes the agent, not to the POI.
<!-- tarav.breadcrumb 19846c92b781 -->
<!-- tarav.breadcrumb 09c8c5868c09 -->
- `may_do` moves out of the POI. It was first to become part of the context;
  later in the day its home became the POI's action and that action's skill.
  The POI is concerned with the triggered check and the situation. Precedent is another
  contextualization workflow, and a skill can prime the agent on what to look
  for, even with its own typed Context view.
<!-- tarav.breadcrumb 0f6799fa762b -->
- Candidates, not decided: a typed Message that models guidance instead of
  the POI; typed subjects beside the situation, so precedent on similar
  subjects can be found.
<!-- tarav.breadcrumb 330361530e4c -->
<!-- tarav.breadcrumb 5c5fefb93f65 -->
- Weak situations are found by maintenance while processing POIs.
<!-- tarav.breadcrumb d749600056e2 -->

The User was unsure what it means for a check to have no identity, and whether
some POIs are ill-typed and should be CheckPOIs. In code a Check's `identity`
says which check this is across runs; `Check` returns `None` and
`SituationCheck` derives it from its Type and situation. Agent reading, not
decided: the identity-less checks are debt to convert explicitly, not a
meaning to preserve.
<!-- tarav.breadcrumb 89514a83ccf7 -->

Agent's comparison with exceptions, as discussed: both let the class be the
kind and carry no severity; POIs differ in that they do not interrupt, outlive
the process and therefore need an identity kept apart from description, have
an attributed acceptance, and make absence meaningful only when the check ran
completely.

Request 889 built the first of these directions on 2026-10-09: every POI has
`throw()`, which raises `POIError` carrying the POI
(`tarav-py/src/tarav/l1/poi/primitives.py`). `CheckPOI.error()` was removed in
its favour, so the `.error()` named in [Checks workflow](checks-workflow.md)
is the earlier name.
<!-- tarav.breadcrumb 3d95d861eb7d -->

## A POI is an event; what follows it is an action — 2026-10-09

A later turn of the same day's discussion. It replaces the idea, held for a
few minutes, that a POI declares its own resolutions, and it changes what a
tracked POI is. Nothing here is implemented. The Actions it builds on are in
[Operator Context, Directives and Harnessed Actions](operator-context.md).

### What a blessing means

Reviewing the first Actions example, the User asked what blessing a POI such
as "this file has a TODO" means: that it is done, that it is not really a
TODO, that it is recorded elsewhere? A blessing answers a specific question,
and the types should carry that semantic.
<!-- tarav.breadcrumb 264fa41857a6 -->

The same POI can be blessed by different kinds of blessing. What makes
something a blessing is that the POI's claim is attenuated or dismissed; its
original nature is an overrule of the check. It is not the only relationship
one can have with a POI: a POI may be annotated, or may ask for something to
be provided.
<!-- tarav.breadcrumb 302d002af40f -->

The general frame is that a POI can be resolved, in several typed ways:
because the situation was changed, because something the POI asks for was
done, or because it was dismissed, which is the softest. Dismissal has grades,
from no justification to a reason that must score well. The word "blessing"
may not survive.
<!-- tarav.breadcrumb 4475d3796fed -->

### The POI is only the event

Too much responsibility was being put on the POI. A POI is the event that a
situation happened and was raised. It can have consequences: it can activate
an action. A blessing is a way to finish that action.
<!-- tarav.breadcrumb 6c8218183755 -->

What used to be a tracked POI is not a POI: it is an action triggered when the
POI is first raised, closed automatically when a later check no longer raises
it. An action can have more than one close path, as a program has; dismissal
is one. The design starts from scratch and need not keep earlier names. The
guidance about what to do lives with the action and its skill, not in the POI.
<!-- tarav.breadcrumb 58bd0fd530f8 -->

One action per POI, for simplicity. Other workflows may hook their own,
independent actions from outside when a kind of POI is raised, and an action
may close when another closes, as a chain.
<!-- tarav.breadcrumb a2447cd89c1e -->

The name for now is an actionable POI: a POI that also spins an action.
Everything stays typed: situation, check, check POI, action. What is
happening in a Project is asked as "which actions are active?". Closing is
done by a loop that belongs to the Actions workflow: it asks each running
action whether one of its close paths is met, and closes it if so. That is
simpler than hooking into the checks.
<!-- tarav.breadcrumb 2e49cb0920a5 -->

Agent proposals, not decided: keep the close path visible wherever runs are
listed, so a dismissal never looks like a fix; a dismissed POI that is still
raised does not reopen its run while its situation is unchanged; a situation
that returns after it was gone opens a new run; other workflows' extra
actions come from an explicit list consulted when a run opens, and
dependencies between actions are checks that read run states, so no event
system is needed.

### What was built from it — 2026-10-09

The User asked for the requests to be prepared and executed.
<!-- tarav.breadcrumb 1bf2b756ce75 -->

- [892](../../../tarav-py/notes/live/892-actionable-pois-and-resolution-action-impl-req.md):
  exits on Step actions; the POI resolution action; `Check.subject_key`,
  `Check.clear()` and `ClearPOI`. The instance of a POI's action is derived
  from the POI's identity, and reopening shows in the registry's Git history.
- [893](../../../tarav-py/notes/live/893-elementary-pois-guidance-to-context-impl-req.md):
  `POI.context_notes`; the guidance check is gone, which took the root
  Project from about 190 reported POIs to 54.
- [894](../../../tarav-py/notes/live/894-project-pois-on-actions-impl-req.md):
  `CheckPOI` is actionable; `tarav check --project --actions write|skip`;
  `tarav action list --project`; `tarav context --id <poi id> --view poi-action`;
  tracking removed. On the root Project 52 actions opened, and after the
  agents file was compiled from its source the action of its drift POI closed
  as `gone` with the signal printed.
- [895](../../../tarav-py/notes/live/895-dismissal-replaces-blessings-impl-req.md),
  first part: `DismissablePOI`; dismissal refused where the Type does not
  allow it; a dismissed finding counts as settled.

Agent choices made while building, not decided by the User: a check's stable
key is called `subject_key`, because checks already use an attribute named
`subject`; the caller passes the completed checks to the Actions workflow, and
no clear POI is synthesized for every check; in a whole run a check Type that
can name neither a subject nor an identity closes its absent actions; no real
check declares a subject key yet; the blessing code was not removed.

## Suites, closing records and the blessing as a closing — 2026-10-11

Request 895 had put dismissal beside the blessing code without removing it.
The User asked for blessings to be reimplemented with the new primitives.
<!-- tarav.breadcrumb 38b7ff3ffc79 -->

### A blessing is a closing

An action is running, and a blessing is one way of closing it. It is not
different in kind from other closings: the action defines how it can be
closed. The POI can still appear; a blessed action is a suppressed one. The
blessing is a record that can carry a reason and evidence, so it can be
scored, and that is why it hooks into the assertion system. A Blessing is a
type of closing constructor for a POI action.
<!-- tarav.breadcrumb 08bd98d692d7 -->

The agent had proposed a second action to score a blessing and withdrew it.
The User stated the boundary: the scoring system is independent and assigns
scores to declared assertions; scores attach to assertions; the Blessing,
like any object, declares assertions. The chain Situation, SituationCheck,
SituationPOI, SituationAction, SituationBlessing is one particular
implementation, and others can come later. The word Blessing stays, defined
mechanically: the action is closed even though the situation still exists.
<!-- tarav.breadcrumb f018ec000856 -->

Closing an action produces a record of some Type; it is not a plain status.
An action can close automatically and can have several closing paths. It
can be reopened, and that can depend on how it was closed. Status is a
vector with several axes.
<!-- tarav.breadcrumb fc2cc01410bf -->

### Suites

The agent had added, without approval, a per-check "subject key" to tell
"the check looked again and found nothing" from "the check did not look".
The User asked what it was, and replaced it with a suite: a suite targets
checks run on targets and has a hardcoded UUID; its meaning is "if you run
me, you are testing the same thing"; a situation has disappeared when the
suite no longer detects it.
<!-- tarav.breadcrumb 0472474d74fd -->
<!-- tarav.breadcrumb 61a31fbac267 -->

A suite can be very general, for instance one Projects suite: if it did not
produce the POI, the action is closed. No finer scoping is needed, and the
semantics are clear.
<!-- tarav.breadcrumb b8b8780f3eb2 -->

A check does not carry a suite. The caller specifies it, and attaches it
where documentation needs it. The suite is like the operating system: it
knows all the actions that belong to it, and after a run it closes those the
results allow. Identity is apart: the suite is who manages the action.
<!-- tarav.breadcrumb 8e1841997a89 -->
<!-- tarav.breadcrumb 9d82b4a307c3 -->

### What was built — 2026-10-11

Request 896 in `tarav-py` (commit `7f74882`), with the extension's request
005 (`4cd36d5`):

- `tarav.l1.actions`: `Closing` records, `Exit.closing`, `axes(run)`.
  `tarav.l1.actions.suites.Suite` with `settle()`; `ProjectsSuite` and
  `SkillwareSuite`. `tarav check --project` settles the Projects suite.
- `tarav.l1.actions.blessing`: `Blessing`, `BlessingInput` and the test of
  that exit, in the Blessings workflow. `POIResolutionAction` has the paths
  `gone` (by the suite) and `blessed` (by an operator).
- Removed: the blessing store, its two record Types and its Skillware
  commands, `ProjectDecisions.blessings()`, the subject key, clear results,
  and the matching by check identity.
- On the root Project, the 51 open actions were taken over by the Projects
  suite. Tests: 259 passed in the shared worktree, 247 on a clean export.

Agent choices in that work, not User decisions:

- The managing suite is a Type of its own, `Tarav.Actions.Suite`. A
  `CheckSuite` already existed in the checks workflow; it only composes
  checks and was left as it is.
- A check that did not complete leaves the actions it raised as they are,
  and a run that is not the whole suite closes nothing.
- A Blessing holds when its situation goes away and returns; the situation
  axis records the absence.
- A Blessing is Assertable and no longer a Decision.
- The Blessing Types are defined beside the Actions code, because defining
  them in the Blessings package made the two packages import each other.

Known limits:

- An action has one manager and one target. A Project's checks include those
  of its skill packages and of its child Projects, so those POIs' actions are
  managed by the Projects suite on the root; a Skillware run, or a run on a
  child alone, leaves them as they are.
- Removing a check from a suite closes its actions as gone: "no longer
  detected" is not always "fixed".

## The suite is the Project's own set of checks — 2026-10-11

Request 896 gave an action one manager and one target: the Project a
command started from. The root's run therefore owned the POIs of its
children, and a run on a child alone closed nothing.
<!-- tarav.breadcrumb 28cc66d7a46f -->

A check must belong to something, because otherwise nothing can say whether
it is no longer happening. The model is suite/check. If others want those
checks managed, for instance container Projects, it is done from the suites.
For now suites are attached only to Projects. Checks and POIs can be built
from many objects; the suite is about what a Project records as an action,
and a momentary check whose only footprint is printing needs none of it. The
suite is an organization of a Project's action system, not something
fundamental to POIs and checks. The question it answers: who can tell me
whether this check disappeared?
<!-- tarav.breadcrumb 40adf7563ff6 -->

The suite is something a Project has, identified from its Project, like
`<project>.suite`. It represents a set of checks. A check removed from the
code is no longer in the suite, which is not very different from a check
that is no longer triggered: the suite is where the current set of active
checks is defined.
<!-- tarav.breadcrumb 1969c2379641 -->

A check that crashed is a result of the test, so the test is present. Some
checks are always created and run ("AGENTS.md is present"); others are not
explicitly defined and can occur once and never again ("a TODO on this
line"), and those are the ones that can be missing from the suite. The two
kinds are not tracked differently; they emerge. We run a suite, we have the
results, and we resolve the status of checks and actions.
<!-- tarav.breadcrumb 1282cfa031a1 -->

The existing `project.checks.suite()` is the suite: the place where actions
go to resolve the current status of checks. The status must be clear when a
check failed.
<!-- tarav.breadcrumb 1aa8af12a056 -->

### Command output

Decided in the same session: Tarav commands render their output by default
and `--json` dumps it. Rendering is only how the data is presented; there is
one model for both, the command decides what to present, and the readable
form is usually summarized while the JSON can hold all the details.
<!-- tarav.breadcrumb b3902e470b94 -->
<!-- tarav.breadcrumb d03bc412dc84 -->

### What was built — 2026-10-11

Request 897 in `tarav-py` (commit `d1398c7`), with the extension's request
006 (`8dd2ddf`):

- `CheckSuite` takes an `owner`; a run keeps the owner of each result
  (`CheckRun.groups()`). `TaravProject.suite` is the Project's suite, and the
  root nests each child's own suite.
- `POIActions.resolve(check_run)` resolves each Project's actions from its
  own results. `Tarav.Actions.Suite`, `ProjectsSuite` and `SkillwareSuite`
  are removed; `tarav skw skills check` records no action.
- The situation axis has `check failed`.
- `tarav action` and `tarav operator-context` print a summary by default and
  the full result with `--json`.
- On this workspace the root's run reported 3 Projects and moved the 51 open
  actions to `tarav-md`, the Project whose suite produces them; a run on
  `tarav-md` alone then reported the same 51. Tests: 263 passed in the
  shared worktree, 251 on a clean export.

Agent choices in that work, not User decisions:

- The owner is a plain description on the suite; the checks code gives it no
  meaning. A nested suite without an owner belongs to the suite around it.
- An action found under another Project is moved to the Project whose suite
  produces its POI, in the normal run.
- A failed check is matched to its actions by its Type, since a check such
  as the TODO one has no stable instance between runs.
- A child that runs in its own environment is one check of the root; its
  actions are resolved by the child's own run.

Known limits:

- A Project removed from its container, or a check moved to another
  Project, leaves actions that no run resolves until the POI is produced
  again.
- No real action has been closed by a child-alone run or blessed yet; both
  are covered by tests only.

## The Project composes its checks and its actions — 2026-10-11

After request 897 the User restated the model to align on it. The Project is
the object the actions are attached to. Open actions are like open issues:
typed, persistent across sessions, registered under a Project. An object
such as a check or a POI is distinct from what is done with it. They doubted
that the suite is needed as a concept: what is needed is that the machinery
of the actions can tell whether a situation is happening now, and that
something knows how to run the checks again in an equivalent context.
<!-- tarav.breadcrumb b4a6a430ea9e -->

The agent's reading of the code as it stood: the Project was bypassed. The
check code carried the Project's identity (an owner on suites, groups in a
run) so that one function of the Actions code could do everything, and the
command was the only place where checks and actions met.

### What was decided

Registering actions is something about the Project, and that is what makes
the integration of checks, results and actions necessary. Objects may hold
builders of other objects; another layer integrates them with larger
systems. The Project runs a loop that gives the check results to every
registered action, and each action does what it needs: ignore them, close
itself, or change its status.
<!-- tarav.breadcrumb 5aca0b1ff7ec -->

Builders on objects are a modeling pattern to use when it fits, not a rule,
and redundant paths are allowed.
<!-- tarav.breadcrumb a4bf8b63cc62 -->

`project.suite` is eliminated; a cache of a run, if ever needed, would go
inside `project.checks`.
<!-- tarav.breadcrumb 91bbe122cb71 -->

`project.checks` holds the checks of a Project, may run those of its
subprojects, and only runs checks. Its results are passed to the action
workflow to update any action and to start any action.
<!-- tarav.breadcrumb 6f5689988db9 -->

The separation comes first and the ergonomics later, but one command is
needed that an agent can run repeatedly. For now it is
`tarav project status`.
<!-- tarav.breadcrumb 17dbcbbda492 -->
<!-- tarav.breadcrumb e2dfe5d0b2e5 -->

### What was built — 2026-10-11

Request 898 in `tarav-py`
(`notes/live/898-the-project-composes-checks-and-actions-impl-req.md`).
Names and details are the agent's.

- Check code no longer carries a Project: `CheckSuite` has no owner and
  `CheckRun` no groups. `CheckRun.report` takes a neutral `label` function
  and `clean()` means no finding (`tarav.l1.checks`).
- `Action.on_checks(run, update)` is what an Action Type does with a run of
  its Project's checks; the base ignores it. `POIResolutionAction` holds the
  POI rules, among them leaving an action whose check failed
  (`tarav.l1.actions`, `tarav.l1.actions.pois`).
- `ProjectActions`, reached as `project.actions`: `start` registers the
  action of each POI not registered under the Project, `refresh` hands the
  results to every registered action, `update` does both and records them
  (`tarav.l1.actions.project`).
- `project.status()` runs the Project's own checks, hands the results to its
  actions, and asks each member Project to do the same
  (`tarav.l1.project.base`, `status.py`; `RootProject.members()`).
- `tarav project status --project` runs it; `tarav check --project` lost
  `--actions` and only reports the checks (`tarav.l3.check`).
- The exit taker `suite` is now `project`.

Evidence: `tests/test_actions_workflow.py`, `tests/test_project_tree.py`
(a real root with two children). On this workspace
`tarav project status --project .` reported 51 actions raised in 3 Projects
with nothing opened or closed, and the same for `tarav-md` alone, so the
existing actions were taken over unchanged.

Left open: a child in its own Python environment is still one check of the
root, so the root's status does not update that child's actions; the loop
visits closed actions too and may need a limit with a long history.

## Suites are detectors that hold their run — 2026-10-12

The User tried `tarav project status` and it took very long: the check of
the test suite ran the whole pytest suite of `tarav-py`, about a minute,
every time.
<!-- tarav.breadcrumb 9fa54892b789 -->

One POI per failing test is good. The problem is convenience: agents call
the status constantly as the mechanical feedback about the Project, so it
cannot be slow. Agents can focus on a subset; the full suite does not have
to run all the time.
<!-- tarav.breadcrumb d39dd02efe3e -->

The difficulty was the closing rule. An action closed as gone when its POI
was not in the results, so running only some checks would close the actions
of everything left out. The agent proposed that a check result say which
situations it covered.

### What was decided

That cannot work in general: the situations that disappeared cannot be
listed. So the suite returns, as a compartment: it is known which suites ran
completely, actions know which suites they belong to, and those that need to
detect a missing POI look at complete suite runs. Suites are recursive and
subsets of them can be run.
<!-- tarav.breadcrumb a2d6f52fb3ac -->

A suite has an identity, not a path, so moving it costs no migration. It can
be run partially or completely, for instance filtered by check Type.
<!-- tarav.breadcrumb be4f10f4c120 -->

All the data lives on the suite, the run results included. Every suite is a
class, as every check is, and it contains the method that runs the checks.
<!-- tarav.breadcrumb 41e84333a885 -->

One suite instance holds one run, or it is reset. A check only returns its
result and does not care what is done with it. Fewer object Types is fine
when clarity does not suffer. No history of runs.
<!-- tarav.breadcrumb 3e3295032c2e -->

A correction the User asked to state explicitly, of a mistake made earlier:
a suite does not contain checks. The checks cannot be enumerated, because
many depend on situations and situations cannot be enumerated. What a suite
contains is code that runs the checks, and which ones run can change from
run to run.
<!-- tarav.breadcrumb e0b74aa8c339 -->

The closing rule, in the User's words: the signal is gone when the detector
is not detecting it any more.
<!-- tarav.breadcrumb 46e4aa9e7f16 -->

For the tests: one bound suite per test file; any default to start with, as
long as a flag runs everything; no selection inside pytest yet, only a
filter on the whole pytest suite; a `PyTestSuite` base type. No legacy code:
old data is deleted or migrated. The User chose to delete the existing
action records and let them reopen.
<!-- tarav.breadcrumb 3f05fb67b33b -->
<!-- tarav.breadcrumb 800b1f9c8e34 -->

### What was built — 2026-10-12

Request 899 in `tarav-py`
(`notes/live/899-suites-are-detectors-that-hold-their-run-impl-req.md`).
Names and details are the agent's.

- `CheckSuite` took over the run and `CheckRun` is gone: `produce()` is the
  code that yields checks, nested suites or ready results; `run(select=)`
  runs it whole or filtered and returns the suite with its results, summary
  and report. A subclass, or an instance with a `key`, has an `identity`; a
  plain grouping has none and counts as part of the suite above it
  (`tarav.l1.checks`).
- A suite is `exhausted` when its own code ran to its end with nothing
  refused, and `conclusive_for` a Type of check when its own checks of that
  Type also completed. A nested suite with an identity answers for itself.
- An action keeps the identified suites above its check in `event.suites`.
  When its POI is not raised, the nearest of them that is in the run
  decides, and the suite handed over does when none is: conclusive, the
  action closes as gone; otherwise it stays, with the situation
  `check failed` or `not run` (`tarav.l1.actions.pois`).
- `PyTestSuite` runs pytest once and yields one `PyTestFileSuite` per test
  file; it is not routine. `TestSuiteCheck` is gone
  (`tarav.l2.project.dev`).
- Both commands leave non-routine suites out and say which; `--all` runs
  everything (`tarav.l3.check`).

One refinement came from the tests, not from the discussion. With the rule
as first written, one check that failed kept every action under the same
suite. The agent kept the earlier precision: a suite answers per Type of
check, so a failed check only holds the actions its own Type raised.

Evidence: `tests/test_checks_workflow.py`, `tests/test_actions_workflow.py`
(a detector that did not run, a suite no longer yielded, the routine run),
`tests/test_project_dev.py` (pytest once, a suite per file). On this
workspace the 52 old action records were deleted; the routine status took
about 4 seconds, where the previous one took over a minute, and opened 51
actions; `--all` ran 394 checks in 1 minute 38 and changed nothing.

Left open: what the routine run should include is to be learned by use; a
child Project in its own Python environment still runs everything as one
check of the root.

## The POI is a flag; the Project integrates — 2026-10-12

### The output of the two commands

The User called the output of `tarav status` a mess: it was the check report
with one line about actions at the end. It was rebuilt to be about actions:
what is open and where, what the run changed, and one line about the checks.
`tarav check` got the same cleanup and stays about POIs.
<!-- tarav.breadcrumb e4b64af6526d -->
<!-- tarav.breadcrumb a75d6353f044 -->

### From the hint to the fundamentals

The status hint named a POI and a view. The User wanted the interface more
action centric: POI actions are one type of action, what the status lists
are open actions, and an id should find the object, whichever it is.
<!-- tarav.breadcrumb 8ad448316be1 -->

The agent proposed that the view belongs to the action. The User corrected
it: the context workflow is independent and receives a contextualizer, such
as a view; the status only promotes how the agent can go further. They then
asked for fundamentals: should every POI that has an impact on the status
produce an action, or not all of them.
<!-- tarav.breadcrumb 96e03083d4a4 -->

The consumer of the POIs matters. A linter can use the POI system without
hooking into the Project's status, and there the POI may only be printed.
The Project status is closely integrated with the Project's checks and
actions, and its checks escalate to actions by design.
<!-- tarav.breadcrumb 4a452a887203 -->

The User then doubted printing as a path of its own: what is the point of a
POI if not to demand action, and should all execution not go through
actions, which are how agents are harnessed on specific steps.
<!-- tarav.breadcrumb ab54d1503b89 -->

### What was settled

A POI is a flag, a notification. It can be escalated by starting an action.
Actions can also start without a POI. Actions are the unit of work in Tarav.
An action needs a place to be registered and a way to end, which a bare POI
does not have. Printing is only how a person looks at checks directly.
<!-- tarav.breadcrumb ef906be9ee81 -->

The User asked whether POIs are needed at all. The agent's answer, which the
User accepted: the POI is the interface between detecting and working. It
gives the action its identity; it keeps detection apart from work, so a
check can run by itself; and inside a step it is the reason the step could
not close. The store of reported POIs must go, at least for now: make a
simple system first and test what is really needed. A POI is momentary and
owns nothing.
<!-- tarav.breadcrumb c19dfd88b6d2 -->

`POI.throw()` stays, as conceptually clean. A Type can still declare
capabilities: the caller triggers one, but an object says what it can do.
<!-- tarav.breadcrumb 27ad4e6ea1be -->

Complex things such as blessing and filtering are modeled only at the level
of a Project or a similar system, because they integrate several workflows
and primitives. Objects may hold parts of the integration, but it is managed
by something larger and well defined: the Project, for now.
<!-- tarav.breadcrumb 58ee3f906763 -->

### What was built — 2026-10-12

Request 900 in `tarav-py`
(`notes/live/900-the-poi-is-a-flag-the-project-integrates-impl-req.md`).
Names and details are the agent's.

- Removed: `tarav.l1.poi.reporting` (the store of reported POIs, its view
  and resolver, the hint POI listings printed), the round-trip contract
  check, the `context` render level, the blessing attention report, the
  blessing and standing in POI listings and `tarav skw skills
  --blessing-status`, and `POIActions`, the reader of actions that belonged
  to no Project.
- `IdentifiedPOI.describe()` gives everything known about one POI as plain
  data. An action keeps it in `event.source`, so what a POI's Type says is
  read from the action (`tarav.l1.poi.primitives`, `tarav.l1.actions.pois`).
- An action contributes its own Context and its Action Type adds what is
  specific to it. `ActionResolver` finds an action by its id or by its POI's
  id, so `tarav context --id <id>` opens it without a view
  (`tarav.l1.actions`, `views.py`).
- `project.actions` answers `of(poi)`, `standing(poi)` and `blessing(poi)`
  (`tarav.l1.actions.project`).
- `tarav status` is settled when every check that ran completed and no
  action is open; its change lines carry action ids (`tarav.l3.status`).

Two corrections to the agent's audit. The notification helpers it called
unused are how `emit_notification` delivers, so they stay. The capability
markers `ActionablePOI` and `BlessablePOI` stay where they are, as
declarations.

Evidence: `tests/cli/test_context_command.py` (an action found by its id and
by its POI's id; a POI describes itself and stores nothing),
`tests/test_actions_workflow.py`, `tests/test_poi_primitives.py`. On this
workspace the action records were deleted and reopened, 51 again; the 250
files of `~/.tarav/check-reports/` were deleted; `tarav context --id
4e3b5daa-6888` opened an action with its `poi-type`, `raised-by` and
`notes` entries.

Left open: where the policy "this POI escalates" should live; an inbox for
occurrences; forcing agents' work through actions, which belongs to the
harness and not to the POI or check code.

## A SituationPOI has only its situation — 2026-10-12

### How it came up

The Project status did not see a drift the agent had caused in the
`tarav-pkg` skill: the checks that detect it ran only in the skill command.
Once the skill package's suite ran all of them, fixing the drift made 28
actions close and 28 open, although two things had changed. The cause is
that the Skillware POIs keep the state of the package's files inside their
situation.
<!-- tarav.breadcrumb bc8fdf05c47a -->

The agent proposed a POI in three parts: subject, state, evidence. The User
did not recognise that as the POI model and asked for the current one from
first principles.
<!-- tarav.breadcrumb ed168feb8792 -->

The agent's second account described one line of POIs as if it were the
model. The User asked to tell a particular implementation line from a
general principle, and for a tree of the lines.
<!-- tarav.breadcrumb e7f83c686260 -->

The tree showed that only three things are in the base classes. A situation
that includes state, a check bound to a snapshot, and blessable Types are
all choices of the Skillware line.

### What was decided

`IdentifiedPOI` is renamed `SituationPOI`. It only prescribes that the
situation is a `LiteRecord`. More can be modeled inside a situation, but the
fundamental philosophy does not care: an object describing the situation
goes there, with no structure common to all POIs.
<!-- tarav.breadcrumb e5dc12440f3a -->

`subject` and `evidence` should not be in the base model without clear
fundamentals.
<!-- tarav.breadcrumb 0c2476864fd3 -->

At the level of a `SituationPOI` only the situation is required, plus what
comes from the base above it, the message. Specializations add other
fields: POIs are subtypes, and the whole expressivity of the Python type
system is available. What is wanted is a clear and simple model without
ambiguities.
<!-- tarav.breadcrumb 51e4ba75b9c4 -->

The User asked whether `subject`, `evidence` and `coordinate` had been well
defined. They had not: the only written statement was that evidence does not
create a second identity axis; the other two had no definition, and a check
POI filled `subject` and `evidence` with a copy of its `details`.
<!-- tarav.breadcrumb a23c159baf29 -->

On blessing the User noted that it does more than close an action: it can
also suppress a POI from showing, and that they had no clear way to model
it. The agent's reading, not yet confirmed: the Blessing is one fact, an
accepted situation, with two readers in the same consumer, the action that
stays closed and the presentation that does not list it as open.

### What was built — 2026-10-12

Request 901 in `tarav-py`
(`notes/live/901-a-situation-poi-has-only-its-situation-impl-req.md`).

- `POI(message)`; `SituationPOI(message, situation)`; nothing else at the
  base (`tarav.l1.poi.primitives`). `CheckPOI` keeps `check`, `details` and
  `failure` and copies nothing (`tarav.l1.checks`).
- Lines where the old fields repeated the situation or the details dropped
  them: Skillware, tribunal scores, Workspaces, Skillware generation.
- Lines with real data declare it as a field: `error` on the records
  provider error, `entry` on a skills status POI, `hints` on a reference
  resolution POI, `positions` on an ambiguous Breadcrumb position, `project`
  and `closed` on an action closed.
- The Diagram line keeps a field named `evidence`, declared by that line:
  its callers are in files other agents are changing.

Evidence: `tests/test_poi_primitives.py` (a situation POI has a Type, a
message and a situation and nothing else; a specialization's field is not
part of the identity). On this workspace the action records were deleted
and reopened: 58 actions with the same ids as before, so identities did not
change.

Left open, by decision: what the Skillware line puts in its situation, and
with it the actions that end and restart on any edit of a package; how to
model that a blessing also hides a POI.


## Product drift declares its own situation — 2026-10-13

The User opened one product drift action and asked what its situation held.
It held the place of the finding and the content hash of every file of the
package, 51 of them. The snapshot was there so that an acceptance could not
keep applying after later edits; the findings did not say what they depended
on, so the whole package was taken.
<!-- tarav.breadcrumb 0d80243481d8 -->
<!-- tarav.breadcrumb d80645c7fef3 -->

The User stated what a situation is here: a blessing targets a situation;
the situation is the declared state, the state that is blessed and that the
POI represents. Product drift is a simple POI: the compiled file differs
from what compiling produces.
<!-- tarav.breadcrumb 3611c15085d7 -->

The agent had proposed to keep the state on the blessing instead; that was
withdrawn. The state belongs in the situation; the fault of the snapshot is
its scope.

Three fields are sufficient: the product, the hash of the file on disk, and
the hash of the text the source produces.
<!-- tarav.breadcrumb e4eb4c9078c5 -->

A heuristic from the User for defining a situation: see what the check
actually uses.
<!-- tarav.breadcrumb 1c6b3ff96b44 -->

### What was built — 2026-10-13

Request 902 in `tarav-py`
(`notes/live/902-product-drift-declares-its-own-situation-impl-req.md`),
for this Type only.
<!-- tarav.breadcrumb 8a2598323da9 -->

- The drift finding of `Document.lint()` carries the product, the two
  hashes and a count of the difference (`tarav.l1.skw.document`).
- `SkwPOI.from_finding()` holds the general Skillware line, still the place
  plus the package snapshot. `ProductDrift` overrides it with the three
  fields, a message that names the file, and notes saying that either side
  may be the newer one (`tarav.l2.skw.pois`).
- The product is named by its full path: a package can be checked without a
  Project, and the identity must be the same either way.

Evidence: `tests/test_skw_poi.py` (an edit of another file of the package
keeps the identity; an edit of the compiled file changes it; equal texts
raise nothing). On this workspace the old action closed as gone and one
opened with the new situation; a second run changed nothing.

Left open: every other Skillware Type keeps the package snapshot. The drift
found in `tarav-hugentics/references/inline-capture.md` was left as it is,
by instruction: text of request 885 that exists only in the compiled file.
<!-- tarav.breadcrumb dc4dac6dbe02 -->

## A Skillware finding names its POI Type — 2026-10-13

The User saw two names on one status row, `Tarav.SKW.POI.UnreachableBlock`
and `unreachable-block`, and asked what the lowercase one was.
<!-- tarav.breadcrumb 8f1642ab7184 -->

It was the vocabulary of the Skillware analysis. The analysis lived in layer
1 and the POI Types in layer 2, so the analysis named a finding with a
string and a table translated it. The User called this stupid and asked for
it to be eliminated.
<!-- tarav.breadcrumb 933fec644d5f -->

The agent proposed six points and the User started the implementation with
them: the Types move beside the analysis; a finding holds the class; the
table and the strings go; each Type's message is a literal sentence;
command output shows the Type name; the Agents file check loses its table.
<!-- tarav.breadcrumb ba81267b2892 -->

### What was built — 2026-10-13

Request 903 in `tarav-py`
(`notes/live/903-a-skillware-finding-names-its-poi-type-impl-req.md`).

- `tarav.l1.skw.pois` holds `SkwPOI`, the atomic Types and `Finding(poi,
  **data)`. Each Type states one literal `statement`; a message is the
  statement, the place and the detail.
- The analysis reports Types (`l1/skw/document.py`, `loading.py`,
  `skills.py`; `l2/skw/skills.py`, `publication.py`). The checks in
  `tarav.l2.skw` select and compare by Type.
- `tarav skw document lint` and the loading context print `type` where they
  printed `kind` or `code`.
- Three Types nothing reported were deleted; four were added for strings
  that had no Type.

Evidence: `tests/test_skw_poi.py` (a finding refuses a string and the
family Type; each Type has its own statement; a package's POIs and a
document's lint carry no kind). On this workspace the open Skillware
actions kept their identities and show the new sentences.

The Agents file check had twelve Types of its own that mirrored the
Skillware ones. The User chose to delete them: the check raises the
Skillware Types themselves. The User asked for the same in the Breadcrumb
audit, since the Type is already there and a second string is not needed: a
concern of that audit now holds its POI Type and the table of strings is
gone.
<!-- tarav.breadcrumb 324a85a78dab -->

Left open: resolving a Breadcrumb and auditing one each have a Type for a
missing and for an ambiguous position; the audit still chooses its Type
from the resolution's.

## Actions keep a Git log — 2026-10-14

### How it came up

An `OutputChanged` action that a migration had caused raised a question
about the action model: an action stays after it closes, so how it closed
must be recorded, and what happened must be traceable later.
<!-- tarav.breadcrumb f41e812b9a27 -->

The User weighed two ways to run checks: on a commit, which records
provenance, or on the working folder, which is decoupled from Git history.
Neither is wrong; rerunning checks is always possible. Git is the store:
no snapshots or diffs are kept.
<!-- tarav.breadcrumb eedf47ab5d6d -->

### What was decided

Good to have, not a requirement. The checks see by themselves whether they
ran on a committed state, at the level of the whole repository; actions
record the best commit data they have, and agents are advised to keep the
repositories clean.
<!-- tarav.breadcrumb f2304a557757 -->

Check suites declare the repositories their checks read; the maintainers
are responsible for that declaration. An action logs the Git state at every
status change, and the first clean state since the last change, per
repository.
<!-- tarav.breadcrumb 5f9a03857341 -->
<!-- tarav.breadcrumb 0fd97abbcd47 -->

### What was built — 2026-10-14

Request [905](../../../tarav-py/notes/live/905-actions-keep-a-git-log-impl-req.md).
A `CheckSuite` takes `repositories=`; when it runs it records each one's HEAD
and whether it is clean, and every result carries the state of the nearest
declaring suite. A Project's suites declare its root. The log was
`tarav.l1.actions.git` (folded into the tape on 2026-10-15, below): an
action's `git` section holds `opened`, `reopened`, `closed` (with the exit)
and `clean` entries; a blessing reads the repositories when it closes. The
action's context has a `git` entry with the log and advice, and
`tarav status` names the repositories that were not clean.

## Test actions on the live path — 2026-10-14

To test work like the Git log of actions, the User proposed fixture files
under `<project>/.tarav/tests/` whose presence makes a check open test
actions, with different test actions for different workflows.
<!-- tarav.breadcrumb 3b579390908b -->

They are real actions, the folder is kept out of Git when possible, and the
mechanism belongs to Tarav itself; existing test workflows are reused when
they fit. These tests are not always run: they are interactive tests that
involve the User, on the real live path, without touching real actions.
<!-- tarav.breadcrumb bf1c5ca57380 -->
<!-- tarav.breadcrumb b86210a15c1f -->
<!-- tarav.breadcrumb 72039d1b2439 -->

Built as request
[906](../../../tarav-py/notes/live/906-test-actions-on-the-live-path-impl-req.md):
while the folder exists, every Project's checks include
`Tarav.Test.Actions.Fixtures`, which reuses the Actions test workflow's
marker check on its `*.txt` files. The folder ignores itself with a
`.gitignore` of `*`. The scenarios are in `tarav-pkg/references/step-actions.md`,
section "Testing the action loop".

## An action has a tape — 2026-10-15

### How it came up

Testing on the live path, an action had reopened; the last time it closed it
had a closing record. The User asked where that record is now, whether it
is gone or only in Git, and how all this should be interfaced.
<!-- tarav.breadcrumb 5506001bb316 -->

Git is how history is kept and infrastructure must not be duplicated; still,
some knowledge of the history of closing records would be nice, perhaps an
append-only list beside the current record.
<!-- tarav.breadcrumb 925186909234 -->

### What was decided

One log in the action, with different entry Types for different events, the
closings included.
<!-- tarav.breadcrumb dc55363d4cbf -->

The operator's attempts are folded into it and the state is read from it. It
is named `tape`: actions have a tape on which important events are recorded.
<!-- tarav.breadcrumb cf33b8f7a757 -->

### What was built — 2026-10-15

Request [907](../../../tarav-py/notes/live/907-an-action-has-a-tape-impl-req.md).
[`tarav.l1.actions.tape`](../../../tarav-py/src/tarav/l1/actions/tape.py)
defines the entries `Tarav.Actions.Tape.Opened`, `Closed` (exit and closing
record), `Reopened`, `Clean` and `ClosingAttempt`. An action's state, exit,
times and closing are read from its tape; the fields `closing`, `closings`
and `git` are gone, and the Git log of 905 now lives in the status entries
and `Clean` entries. Every registry record was migrated; the reopened action
got back its earlier gone record from the registry history. The context
entry `tape` replaces `closing`, `closings` and `git`, and the extension's
action page shows a Tape section.
<!-- tarav.breadcrumb dd9795f22a85 -->
