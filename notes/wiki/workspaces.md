# Workspaces

<!-- tarav.sessions
f5845518 = claude-code:4ee3b84e-14fa-4aa9-9c6f-8d139954fe18 @f5845518e808c6cf0496f867fc656fdad9063980a184f7c3f15c54adf8fcb31f
-->

## Purpose

A basic self-improvement system for Tarav needs isolated working copies. The
first idea was Git worktrees tied to a project, kept outside the project under
the Tarav folder in Documents, where Agents can work.
<!-- tarav.breadcrumb b656598a2a8f6296dedff3e93c35c07fa749ced448961cbf58224646f39368b8 -->

Because a project can be an umbrella over several repositories, the unit
became the workspace: a folder holding worktrees and any other data, with a
description of the initial condition that created it. Complexity moves up to
the Agent and is paid at merge-back, where new Breadcrumb locations and any
migration are handled. Workspaces stay for a while after merging as a
reference and are removed later, as garbage collection.
<!-- tarav.breadcrumb f0b1d8503c7cceab291e1f981e42b0c70d3bbb55dc9ceb903afb53aff8f560d4 -->

## Git as a caller interface

Tarav does not duplicate Git. It models the minimum its workflows need and
calls the user's `git` as configured, without touching configuration.
<!-- tarav.breadcrumb c6d507b810ebc4b6c6de3b00c674aa572ea4d3203a45f209f47957947763c935 -->

## Manifest

A workspace is described by a JSON manifest, a proper Tarav object, that
states its initial configuration precisely and gives its tree layout. It can
be used to reset the workspace or clone it into another one. Its primitives
are copied documents, symlinks, repository worktrees, and new documents. A
copy without a repository behind it records its hash.
<!-- tarav.breadcrumb bd5cd9d7b28b3c931e86a399402e33bada9815e8d3502ed8ece6b16852535401 -->

The manifest says how a reset creates the workspace. A second file describes
the last reset, with the hashes and other initial conditions found, including
the hash of a symlinked file as plain information. This is a minimal
provenance infrastructure.
<!-- tarav.breadcrumb c26659cc8fdb7e6853b606b7e3d3bd0bda0894018f8ca1f3d0d0c36e4f370dab -->

A small vocabulary of states allows basic filtering. The system should not be
more complex than this.
<!-- tarav.breadcrumb 3d4dfde012f95b3086ed5347a83a8216cab010ab026118d41bba3c8ab25dba66 -->

## Worktrees and checks

Workspaces must work with real Git worktrees, defined precisely in the
manifest, so a project or a set of projects can be worked on independently.
Checks verify, for example, that the worktrees exist.
<!-- tarav.breadcrumb 7466621250849572385894898c2a62d8911f78248c74ed20d91f4716a5b59d4a -->

## Stable references are a goal, not a prison

The August rule that nothing stable may reference a workspace path is not how
Tarav works now. Stable-to-stable references are a goal. A reference into a
workspace is allowed and raises a reminder POI to link it properly when done.
Tarav must breathe and stay open and must not add too much friction.
<!-- tarav.breadcrumb 379da50079738d2ccd27406b93d53e45b41ba46c8af34813881263439a402585 -->

## Location and Project integration

Workspaces move to the Tarav folder in Documents. The workspace workflow has
its own way to visit and list workspaces. Projects get an easy way to create
workspaces and to know those created under their link; this is only an
interface between two independent workflows, for organization.
<!-- tarav.breadcrumb 304bba1b3bd9d412a0ff14857bfd6eb7a8eadb85115ed471cd6179f44771d3f6 -->
<!-- tarav.breadcrumb 37e34538cb7e9895d8d75a48a59a29505470420fcd1fccf8e59dbebb1feb20af -->

Design request: `tarav-py/notes/live/852-workspace-manifest-worktrees-and-project-integration-impl-req.md`.
The Agent recommended local clones over worktrees; the User chose worktrees
with checks.
<!-- tarav.breadcrumb b35e1d90b7c8b16f0002e6559094e8cc83388655452d8e57cf34a594450670cd -->

## First implementation

At the User's request, 852 implemented this workspace model in the Python
library. The workspace manifest identifies one Workspace and pins each Git
entry to an exact commit; a clone receives a fresh identity and branch. The
setup record retains observations, while seed files retain the initial bytes
needed to reset copied and new documents. `Project.workspaces()` is a view onto
the independent depot, not a field in the Project marker. See
`tarav-py/notes/live/852-workspace-manifest-worktrees-and-project-integration-impl-req.md`
for the execution record and tests.
<!-- tarav.breadcrumb 9259ac8a3a0c897e71906ec5888c9c21cbb491fb710536f8ccef096a3b70db3f -->
