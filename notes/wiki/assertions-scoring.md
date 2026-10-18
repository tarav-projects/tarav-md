# Assertions and scoring

<!-- tarav.sessions
1ae20f8c = codex:01a0ff32-0ec2-7b72-8850-fa795135f3c9 @1ae20f8c8159f12d2402ea702cf49c876ec46a72f71ce12423ae1dbdf2a91871
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Assertable objects and closed cases

An Assertable object can expose several labeled, identified Assertions through
`.assertions`. A label is a durable route to an Assertion, while list order is
only presentation. Each Assertion identifies an exact subject and can produce
more than one typed assessment case for different scoring questions.
<!-- tarav.breadcrumb cd25ccfe7f85 -->
<!-- tarav.breadcrumb e5b08612e1ea -->

A case is a closed scoring packet: it retains an Assertion reference, a question,
and the material presented to the scorer. Case payloads are owned by their
producer and consumer; Tarav does not impose one universal evidence schema.
The scorer judges only the supplied packet. A producer may report that a case
Type is unsupported or that a supported case lacks enough material; those are
different conditions. Scoring results remain separate from Assertion identity.
<!-- tarav.breadcrumb 85c84972b987 -->

Request [846](../../../tarav-py/notes/live/846-assertable-assessment-cases-impl-req.md)
implemented this foundation in `tarav.l2.scoring.assertions`. Its Line-owned
example produces grounding and support-inventory cases from an exact Line
edition and its rendered Support.Set. The runtime registers their Record Types;
the existing Line Assertion identity and ranking adapter were preserved.
`tests/scoring/test_assessment_cases.py` exercises label lookup, closed snapshots,
distinct case payloads, failure modes, and Record round-trips; 47 focused
scoring and architecture tests passed in `tarav-py` commit `230b98a`.

## Pairwise tribunals

A ranking case names its tribunal Type. The tribunal owns its population,
comparison question, instructions, and optional admission check. The common
ranker compares only two cases from the same tribunal, using their retained
presentations and no external research. It accepts A, B, tie, or abstain and
retains the exact prompt, judge, outcome, and rationale for inspection.
<!-- tarav.breadcrumb 4bf188231e01 -->
<!-- tarav.breadcrumb 6630cabff2d5 -->

The first derived measure is relative win/tie support among judged pairs,
accompanied by comparison and opponent counts, abstentions, and population
coverage. One case has no relative score. Sparse or weak support may become
scoring-owned POIs, but a low rank does not establish that an Assertion is
false. Request [848](../../../tarav-py/notes/live/848-pairwise-tribunal-scoring-mvp-impl-req.md)
implemented this path in `tarav.l2.scoring.tribunals` and the existing
ScoringRepository. Two different tribunal Types and case payloads use the same
ranker in its tests; 61 focused tests passed at product commit `bd5be10`.
<!-- tarav.breadcrumb f323afe8896d -->

## Blessing Assertions

A blessing is an attributed judgment that a still-detected POI situation can
stand for now. Its stable `main` Assertion concerns acceptance of that exact
blessing and situation; optional `grounds` exposes offered support as another
question. Both can produce closed cases, while a blessing with no support can
still be recorded and assessed as a weak case. A changed POI situation does not
inherit the prior Assertion. Scoring stays with the scorer; a blessing's
`score_vector()` navigates named results by Assertion identity and distinguishes
unassessed, unscored, and scored. No score suppresses detection.
<!-- tarav.breadcrumb cd9386fa5bdf -->
<!-- tarav.breadcrumb 23a585aa187d -->

Request [847](../../../tarav-py/notes/live/847-blessing-assertions-and-score-view-impl-req.md)
implemented this in `tarav.l1.blessings` and `tarav.l2.blessings`, with the
shared Assertable capability in `tarav.l1.scoring`. The latter keeps the direct
`BlessingRecord : Assertable` relationship within Tarav's import direction.
The configured Python suite passed 154 tests in product commit `8c1fd6a`.
Attention scheduling remains request 849.
<!-- tarav.breadcrumb b65b4a93c1db -->

## Workflow roots and particular scoring methods — provisional capture

Assertions and Scoring should have shallow base types. The working assessment
and ranking implementation can subtype them without making its particular
decisions universal. This leaves room for another scoring method beside
Ranking. A score can be a typed, recomputable object derived from retained
evidence; it need not be stored merely to be identifiable in code.
<!-- tarav.breadcrumb 3fce7e286db8 -->
<!-- tarav.breadcrumb 962896660d23 -->

Evidence pending Breadcrumb registration: session
`codex:01a0d86c-9538-7be1-af96-014cd4203d61`, User Turns at
`2026-10-06T14:48:03.492Z` (“we cannot handicap the ... abstract layer”),
`14:57:36.476Z` (“we will have different ... scoring systems”), and
`15:00:02.920Z` (“scorings can be recomputed”). Each timestamp is UTC on
2026-10-06 and identifies one retained raw Chatlas turn; these are recovery
locators, not registered Breadcrumbs.

`RankingWorkflow` is a particular scoring workflow. In this case it can be a
Python subtype of `ScoringWorkflow` as well as its child in the workflow tree,
but that coincidence is not a rule for every workflow relationship. No common
scoring operation needs to be invented while Ranking is the only implemented
method. Ranking compares closed cases within a Tribunal; another scoring
method may organize its own objects differently.
<!-- tarav.breadcrumb 72135afc0080 -->
<!-- tarav.breadcrumb d819385eecef -->

Evidence pending Breadcrumb registration: same session, User Turns at
`2026-10-06T15:31:39.746Z` (“we want them all be scoring workflows”) and
`2026-10-06T15:34:47.306Z` (“we only have one implementation of any scoring
mechanism that is the ranking”).

## Tribunal as a singleton entity — provisional capture

Tribunal belongs to Ranking, not general Scoring. A concrete Tribunal subtype
represents one comparison question and owns its admission, instructions, and
any case-specific requirements. An Assertion may produce different cases for
different Tribunals. The shared ranking machinery should not prescribe a rich
universal case schema simply because one Tribunal needs particular material.
<!-- tarav.breadcrumb 4b4fd4a3f4b7 -->
<!-- tarav.breadcrumb 722dd58e59c6 -->

Evidence pending Breadcrumb registration: same session, User Turns at
`2026-10-06T15:34:47.306Z` (“we will have different ... tribunals”) and
`2026-10-06T15:38:23.044Z` (“we don't want to standardize ... which data a
case needs to bring”).

The class representative `entity(MyTribunal)` and the singleton Tribunal
object `MyTribunal()` are distinct Diagram entities with distinct identities.
The Python class defines the operation; repeated construction yields the same
identified Tribunal instance, whose identity is declared in code. This is the
same deliberate distinction used for Workflow classes and Workflow objects.
Whether the Tribunal object is retained on disk is a separate choice. Current
`tribunal_type_id` fields identify the class and must not silently be treated
as the new object's Ship.
<!-- tarav.breadcrumb cd349bcf2fb3 -->
<!-- tarav.breadcrumb a09487a1ee15 -->

Evidence pending Breadcrumb registration: same session, User Turns at
`2026-10-06T15:41:05.480Z` (“we still have an identify for the class ...
mediated by ... the entity of the class”) and `15:43:12.384Z` (“we are
splitting the identifier ... class ... and instance”). The current field's
meaning is also supported by
`tarav-py/src/tarav/l2/scoring/ranking/tribunals.py` in the current worktree.

Request [863](../../../tarav-py/notes/live/863-assertions-scoring-ranking-score-impl-req.md)
is the implementation handoff. The worktree implementation passed 169 Python
tests but remains uncommitted pending capture closure. The `tarav.context`
references above use read-only Chatlas User-Turn hashes but still await
Breadcrumb submission and audit.
