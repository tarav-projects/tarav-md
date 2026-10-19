# Attic

<!-- tarav.sessions
7c51c146 = codex:01a15606-58f7-77a0-9600-8d0b0bf63a82 @7c51c146657d59fa35293ab3b44b6be3b0e38654e1dfd05d83fa752a7bd0f4c4
-->

## Cheap conservation

Attic moves material aside from active development while retaining it for
later investigation, extraction of value, recovery, or deliberate removal.
It can remain there indefinitely; conserving material should be cheap.
<!-- tarav.breadcrumb 62506ec3429f -->

## Opaque contents, self-declared metadata

The User explicitly makes Attic contents opaque. Its manifest provides a small
self-declared description of what was stored and why. Mechanical checks can
judge metadata format; they cannot establish whether descriptions, former
locations, completeness, recoverability, or disconnected status are true.
<!-- tarav.breadcrumb bff2e7d95960 -->

The requested maintenance belongs to a real Python workflow with its own Types,
composed into the top-level System Project. It uses Tarav's existing check,
POI, and Action machinery rather than requiring investigation before storage.
<!-- tarav.breadcrumb 07af6d384bb5 -->
<!-- tarav.breadcrumb 88203a08c2a1 -->

## Implemented boundary

The implementation in [tarav.l1.attic](../../../tarav-py/src/tarav/l1/attic/)
provides `AtticWorkflow`, depot and deposit handlers, the manifest model, and
identified metadata checks. The suite lists immediate deposits and reads only
`deposit.json`; it never inspects or requires the existence of the declared
material. Tests in [test_attic.py](../../../tarav-py/tests/test_attic.py)
exercise that boundary, malformed declarations, and duplicate IDs.
[System tests](../../../tarav-py/tests/test_project_system.py) verify an action
opens for a missing manifest, stays open during unavailable discovery, and
closes after metadata repair. These are implementation observations, not proof
of depositor claims. See [request 932](../../../tarav-py/notes/live/932-attic-workflow-impl-req.md)
for checks and outcomes.
<!-- tarav.breadcrumb cb675c1fa781 -->

Agent operations and the version-1 declaration format live in
[tarav-pkg --attic](../../skills/tarav-pkg/references/attic.md).
The current deposit metadata was left untouched: the new checks flag two older
formats for deliberate maintenance rather than silently migrating them.
<!-- tarav.breadcrumb 54e37f690440 -->
