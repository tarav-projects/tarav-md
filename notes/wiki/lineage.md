# Lineage

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## A general problem of Ship evolution

Evolution and historical states apply to anything with a Ship: a Block, a
Line, the code of a class, or another identified object. The User chose to
approach this as a general History or Lineage workflow, rather than solve
versioning independently inside Notebook or another particular workflow.
Lineage is a working name; its API and concrete Types remain undesigned.
<!-- tarav.breadcrumb 14fd31a35e41 -->
<!-- tarav.breadcrumb 556d9eb1634c -->

## Possible historical representations

Two candidate representations were discussed: Git-backed history addresses
states at different commits, following the object's Ship; an explicitly
stored history retains successive records or data states directly. These
could become different Types implementing the same general capability.
Neither representation is selected as an additional requirement for Notebook.
<!-- tarav.breadcrumb 724d8a696a6c -->

## Recovery scope now

The earlier exploration of explicitly captured historical Block versions is
deferred. First recover a selected, preferably recent archive state and let
ordinary Git commits retain its subsequent evolution. Reconstructing older
states across repositories, folders, and embedded editions can be addressed
through the general history capability later. This keeps the initial
[Line Notebook](line-notebook.md) implementation and archive import bounded.
<!-- tarav.breadcrumb 67565ffdb437 -->
<!-- tarav.breadcrumb 6c22b159dc90 -->
<!-- tarav.breadcrumb e0f508c97fc1 -->
