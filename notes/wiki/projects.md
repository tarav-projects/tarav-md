# Projects

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Core and specialized integrations

The design separates a workflow's minimal functionality from specialized
integrations. Loading Models for another consumer should not bring along
Project-specific functionality; the same concern applies to the Project core.
The proposed organization places Model operations under `models/` and the
Project–Model integration under `project/models/`, with `ProjectModels`
connecting the two domains.
<!-- tarav.breadcrumb 493b9e2dc3cb33dd9e36e190c1971aa9b660f059a0985fb9f1c837e899520df9 -->
<!-- tarav.breadcrumb df69e6de95987540f5119ad8412bfba99f47ab1bdcd036aa89e95d0d861c8e5c -->

## Explicit project capabilities

The minimal and more featured Project types should be provided now, not
deferred until a later consumer appears. A caller chooses the interface with
`<ProjectClass>.from_path(path)`. This split also establishes the mechanism
for other systems to subtype Projects. The discussed names are `TaravProject`
for the minimal base and `Project` for Tarav's more opinionated variant.
<!-- tarav.breadcrumb eb0cdcf6ee1c59b21b580f1e60ed81a105dddfdf705426c0a31030065d720723 -->

Project integration can be exposed through `project.models()` or through a
specialized `ProjectModels(project)` interface. Whether it belongs directly
on a Project class depends on that class's intended capabilities; Models need
not be part of every project's minimal contract. The precise accessor return
shape remains an implementation choice, not settled here.
<!-- tarav.breadcrumb b2c41014c434a5915ee5d00db3523296d7587599e2a2aa12a2c1ce5118510271 -->

## Project-local types

A project can implement its own Project subtype in its folder, attaching
project-specific operations and configuration. Tarav supplies common types;
individual projects specialize the suitable base. This is a concrete intended
usage of Project subtyping, not a request for one universal Project class to
accumulate every subsystem's functionality.
<!-- tarav.breadcrumb 07505d50a873473c1b5c6e1166dc329ae49053a973d5c1feba39375caf0db83a -->

These sections capture design intent; they do not claim the subtype split or
integration extraction has been implemented.

## First implementation of the split

The user selected Wiki-backed Develop for this design.
<!-- tarav.breadcrumb ed0aa0197d7f84736fddf5e3497d6b904beaaa51d8c62847f4535f3f08f223c3 -->

The implementation now separates
[TaravProject](../../../tarav-py/src/tarav/project/base.py) from the featured
[Project](../../../tarav-py/src/tarav/project/__init__.py).
`Project.from_path(path).models().main()` resolves the existing main Model;
`Project.from_path(path).wiki()` returns the conventional Wiki folder.
Minimal callers can explicitly use `ProjectModels(project)` or
`ProjectWiki(project).open()`. The integrations declare child workflows under
Project; generic Model and Wiki no longer expose `from_project()`.

Explicit subtype discovery preserves project identity and leaves the marker
file untouched. A retained Type tag is reprojected in memory to the selected
class, while generic Record loading keeps exact Type checks. The
[Project tests](../../../tarav-py/tests/test_project_entity.py) exercise local
subtypes and lazy imports; [Model tests](../../../tarav-py/tests/test_models.py)
exercise default resolution and missing configuration without creation.
See the [implementation note](../../../tarav-py/notes/live/818-project-capability-tiers-impl-req.md)
for verification results and remaining boundaries.

## Named Model associations

The user requested selection of Models other than main and approved named
associations with `project.models().ls()` and `get(name)` alongside `main()`.
<!-- tarav.breadcrumb 9613d530e936ba89236f1a82191f35c82396503231e621254c6989a92082f69e -->
<!-- tarav.breadcrumb 8ff60071e1c6e4608d0da63e0c4e7cc636f34fc9d149de44ca7e34f218b3e11d -->

The [integration](../../../tarav-py/src/tarav/project/models/__init__.py)
reads `diagram.models` as a name-to-Model-Ship mapping in project.json.
`ls()` returns sorted names without resolving storage; `get(name)` resolves
the selected association and raises KeyError for an absent name.
`diagram.main_model` remains independent: no migration or implicit alias is
required. Users can edit the mapping directly; this slice adds no write API.
[Tests](../../../tarav-py/tests/test_models.py) cover shared aliases, live
marker edits, invalid mappings, missing names, and unchanged retained data.

## Project-local Python harness

The user proposed that a Project's `.tarav` folder host a Python virtual
environment at `<project-root>/.tarav/env` by default. Managed using uv, it
would contain Tarav and a project-specific Python package. That package would
define a default `MyProject(TaravProject)` class for the project's node,
giving the project a place for executable specialization.
<!-- tarav.breadcrumb 82d59f20c6207a475a83c907cc45648c90bf0e29825e1ea48193d2e4d362a34c -->

The discussion entered implementation Design in
[824](../../../tarav-py/notes/live/824-project-local-python-harness-impl-req.md).
Its package layout and bootstrap mechanics remain implementation proposals;
this capture does not claim they have been implemented.
<!-- tarav.breadcrumb 5f9589358437a88df624b5aac9a2e04a444e564ead5c252f6bd4ac55687caf5c -->

## Project-local harness implementation — 824

<!-- tarav.sessions
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

The user invoked Execute for 824. The implemented
[ProjectHarness](../../../tarav-py/src/tarav/l2/project/harness.py) provides
read-only inspection, explicit scaffolding and uv sync into `.tarav/env`.
Its generated editable package defines a concrete Project Type with a stable
TypeShip separate from the marker's project_id. Launch metadata and the explicit
local Tarav checkout/wheel dependency live in `.tarav/pyproject.toml`; the lock
is retained and env is ignored. Adopting an existing base/untyped marker is
explicit; reruns preserve edited source and identities. The
[launcher](../../../tarav-py/src/tarav/l3/project/harness.py) starts the local
interpreter, binds the trusted Project Type, dynamically loads its marker, and
runs code/files with `project` and `runtime` available. The CLI exposes
`tarav project harness inspect|scaffold|sync|run`. The
[tests](../../../tarav-py/tests/test_project_harness.py) cover neutral discovery,
adoption, failure preservation, literal arguments, and real uv installation
with editable Project behavior. This completes the earlier design's first slice;
the maintained [usage guide](../../../tarav-py/README.md#optional-project-local-python-harness)
shows concrete commands.
<!-- tarav.breadcrumb 8a2e200a8fed357e223b7f119293f83ac0a399bdb21fcb29253e48ed5fdb32eb -->
