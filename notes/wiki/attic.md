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

## Project-local Attics

The User wants Projects to declare their own Attic folder so retired material
can stay beside the Project. The default is `<project>/_ATTIC`; a configured
folder is an alternative location for the same conservation workflow. Project
checks include the local Attic's metadata checks. The general Tarav Attic remains
available independently. Retired Projects inside a deposit are historical
material, not active child Projects.
<!-- tarav.breadcrumb 7bd28e7af9ba -->
<!-- tarav.breadcrumb 374b2d1a57ee -->

The featured `Project.attic()` now selects `_ATTIC` or `attic.path` from
`.tarav/config.json`. It returns the existing Attic handler without provisioning.
The integration lives in `tarav.l2.project.attic`; focused tests in
`tarav-py/tests/test_project_attic.py` cover selection, invalid config, child
aggregation and resolution action closure. These are implementation observations;
see [request 944](../../../tarav-py/notes/live/944-project-attic-impl-req.md).

The umbrella's former `_DEPRECATED` tree was conserved intact in its local
`_ATTIC/deposits/20261022T174331Z-retired-projects/material/`, preserving nine
retired trees and their repository internals. Deposit UUID:
`78570498-efeb-44de-b785-5c38d82bf1d8`. The operator compared hashes and sizes for
12,633 files before and after the move; that verification is separate from
Attic metadata checks.
<!-- tarav.breadcrumb 56595ea00bc8 -->
