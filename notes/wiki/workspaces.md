# Workspaces

<!-- tarav.sessions
f5845518 = claude-code:4ee3b84e-14fa-4aa9-9c6f-8d139954fe18 @f5845518e808c6cf0496f867fc656fdad9063980a184f7c3f15c54adf8fcb31f
-->

## Purpose

A basic self-improvement system for Tarav needs isolated working copies. The
first idea was Git worktrees tied to a project, kept outside the project under
the Tarav folder in Documents, where Agents can work.
<!-- tarav.breadcrumb b656598a2a8f -->

Because a project can be an umbrella over several repositories, the unit
became the workspace: a folder holding worktrees and any other data, with a
description of the initial condition that created it. Complexity moves up to
the Agent and is paid at merge-back, where new Breadcrumb locations and any
migration are handled. Workspaces stay for a while after merging as a
reference and are removed later, as garbage collection.
<!-- tarav.breadcrumb f0b1d8503c7c -->

## Git as a caller interface

Tarav does not duplicate Git. It models the minimum its workflows need and
calls the user's `git` as configured, without touching configuration.
<!-- tarav.breadcrumb c6d507b810eb -->

## Manifest

A workspace is described by a JSON manifest, a proper Tarav object, that
states its initial configuration precisely and gives its tree layout. It can
be used to reset the workspace or clone it into another one. Its primitives
are copied documents, symlinks, repository worktrees, and new documents. A
copy without a repository behind it records its hash.
<!-- tarav.breadcrumb bd5cd9d7b28b -->

The manifest says how a reset creates the workspace. A second file describes
the last reset, with the hashes and other initial conditions found, including
the hash of a symlinked file as plain information. This is a minimal
provenance infrastructure.
<!-- tarav.breadcrumb c26659cc8fdb -->

A small vocabulary of states allows basic filtering. The system should not be
more complex than this.
<!-- tarav.breadcrumb 3d4dfde012f9 -->

## Worktrees and checks

Workspaces must work with real Git worktrees, defined precisely in the
manifest, so a project or a set of projects can be worked on independently.
Checks verify, for example, that the worktrees exist.
<!-- tarav.breadcrumb 746662125084 -->

## Stable references are a goal, not a prison

The August rule that nothing stable may reference a workspace path is not how
Tarav works now. Stable-to-stable references are a goal. A reference into a
workspace is allowed and raises a reminder POI to link it properly when done.
Tarav must breathe and stay open and must not add too much friction.
<!-- tarav.breadcrumb 379da5007973 -->

## Location and Project integration

Workspaces move to the Tarav folder in Documents. The workspace workflow has
its own way to visit and list workspaces. Projects get an easy way to create
workspaces and to know those created under their link; this is only an
interface between two independent workflows, for organization.
<!-- tarav.breadcrumb 304bba1b3bd9 -->
<!-- tarav.breadcrumb 37e34538cb7e -->

Design request: `tarav-py/notes/live/852-workspace-manifest-worktrees-and-project-integration-impl-req.md`.
The Agent recommended local clones over worktrees; the User chose worktrees
with checks.
<!-- tarav.breadcrumb b35e1d90b7c8 -->

## First implementation

At the User's request, 852 implemented this workspace model in the Python
library. The workspace manifest identifies one Workspace and pins each Git
entry to an exact commit; a clone receives a fresh identity and branch. The
setup record retains observations, while seed files retain the initial bytes
needed to reset copied and new documents. `Project.workspaces()` is a view onto
the independent depot, not a field in the Project marker. See
`tarav-py/notes/live/852-workspace-manifest-worktrees-and-project-integration-impl-req.md`
for the execution record and tests.
<!-- tarav.breadcrumb 9259ac8a3a0c -->
