# Projects

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Core and specialized integrations

### Explicit capability paths — 2026-10-07

The User chose `project.docs.wiki.daily(date)`, `project.models.ls()`, and `project.checks.run()` as the Project API shape. Top-level Project members should generally state concrete object meaning; shared or abstract capability operations should sit under semantic paths. `docs` groups documentation, `models` is a bound capability in its own right, and `checks` comes from the common CheckProvider contract.
<!-- tarav.breadcrumb 2c873fc0f3954687f59e594feb44d03d18dc258e6b2fd6ccb75704617ef5fe22 -->
<!-- tarav.breadcrumb fea17d25ee0a6e8ffa9d4bfac35933a21d26ba8e3765d4ae949c2218b0d15f37 -->

The first implementation exposes `project.docs.wiki`, `project.models`, and `project.checks`; `checks.suite()` builds the runnable suite and `checks.run()` executes it. Named Model listing reads the Project marker, while `get()` and `main()` still require the disconnected Models backend. This access-path change does not itself restore Model resolution. See [Impl.Req 866](../../../tarav-py/notes/live/866-project-capability-paths-impl-req.md).
<!-- tarav.breadcrumb dc892a154968a26462eba71f8d1fd2bb89117143e3b34f244064785f8d12367c -->


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

## Explicit Tarav process launching

[826](../../../tarav-py/notes/live/826-tarav-process-launching-impl-req.md)
is implemented. The [Python runner](../../../tarav-py/src/tarav/l1/python_env/runner.py)
defines `RunnerConfiguration`, an abstract `RunnerConfigurator`, and the
current-environment specialization. The [shared execution engine](../../../tarav-py/src/tarav/l1/python_env/core.py)
runs only the file, source, stdin, and arguments supplied by its caller. The
general `tarav run` adapter selects current or Project configuration; it does
not import a runtime factory, inject a Project, or make Record loading switch
environments.
<!-- tarav.breadcrumb f3f3f542857f0f4f04e57958c3ee60671a410f95015a66de382430c1a9e21080 -->
<!-- tarav.breadcrumb ad3faf722f82cbcb0f16c855411052e395d9b457685cb1957648fcfb16cfd842 -->

Project markers can declare relative `harness.manifest` and
`harness.environment` paths; absence selects the generated `.tarav` defaults.
The [Project launch projection](../../../tarav-py/src/tarav/l2/project/runner.py)
reads only those common marker fields before launching and does not resolve the
marker's concrete Project Type. Paths must remain inside the Project root,
inspection is read-only, and sync targets exactly the selected manifest and
environment. Concrete Project loading remains an explicit operation performed
inside an environment that has the product Type installed. The
[tests](../../../tarav-py/tests/test_project_harness.py) cover an unknown
concrete Type in the bootstrap runtime, declared product paths, generated
harness behavior, and a real isolated uv environment.
<!-- tarav.breadcrumb acc3077a26189a46980b2820716297f4a47ccab541dc063ae3503a2ebdfb5f62 -->

## Places, libraries and Project classes

<!-- tarav.sessions
5a029cbf = claude-code:8c55cc60-f28a-439f-a6a0-0521567e600e @5a029cbf49a299c9709013b8ccb3fc517b2fb56fed373d3da819b6ea842afa2f
-->

This section records a design discussion held while organising md-library. It
does not claim any implementation.

The User laid out what Tarav must be able to express: Tarav as a library,
the harness used to develop Tarav, md-library as a library, the harness used
to develop md-library, and the harness of each depot where md-library's
pipeline runs. All of that work is done by humans and agents together, so each
place of work wants a harness.
<!-- tarav.breadcrumb 252778bad09c130896801e2b0b49aadac28f339fab7ef29d2b3d6c43798dde29 -->

The Agent first proposed a separate object for the library and then a separate
Harness object attached to a Project. The User considered renaming, since a
Project should keep overlaying the folder-rooted project of an agent tool, and
then settled it differently: Tarav does not model the Python library. A
library is Python's concern, which is where code lives and how it is imported.
A Tarav Project is an object inside a Python library, and one library can
hold several Project objects. The Agent withdrew both proposals. "Harness"
remains an ordinary word for what a Project gives its place.
<!-- tarav.breadcrumb e50d8ac558fb44089651cc68cd507503c5f19eb61e8d0375e9881ce8176fbc38 -->
<!-- tarav.breadcrumb 0ad29e402d83b93a916f80d9cae3fe5beb01ceb8d0d1da6e7cfaa4aafab8f9b2 -->

What a harness means in a place, in the User's terms: running the project
checks there runs the checks proper to that place, as a test suite would; and
the place's `AGENTS.md` and skills tell agents how to use the code made for
that place. A consumer place inherits checks, types and commands from the
library it imports, and every Project keeps its own point of extension for
code that belongs to no library.
<!-- tarav.breadcrumb e3bf2f581ca3645eb824edec4b2cb1d277590697ca1c343c2291b39347e1b4da -->

Where the code of a Project class sits is a packaging choice. A library may
keep its development harness in the same code base, under a namespace such as
`.dev`, or in a separate one; Tarav should not care. Tarav needs to know how
to find the Project object that harnesses a folder, and the reading paths that
contextualise agents must document it. A consumer should have no use for the
development Project of the library it imports, even when that Project ships in
the same package.
<!-- tarav.breadcrumb b1001fbf8888025558d4d3b18013f4fae1eac33c1ebd42e62e1dea6a6d5047c4 -->

A Project class defined by a library is a control point: a place that subtypes
it runs the checks the library defined. md-library's depots are the first
intended case.
<!-- tarav.breadcrumb ccbea9715ce5d7c9d028640fb3b46207643ac013d51ff6c2e8ede7f3c9052b76 -->

### Root Project over child Projects

A development folder can be a small graph of Projects: a root Project whose
checks are those of the Projects below it, with an implementation Project and
a documentation Project as children, sharing one Python environment at the
root. The User described this for md-library and confirmed that it is general:
`taravangian-project` has the same layout and should get it as well.
<!-- tarav.breadcrumb fdb73a4817b7df816c9c06ff3f2967fab8110a02ba401ba0e5caf21ce3fc96ac -->
<!-- tarav.breadcrumb 1da500bbadea187155b25c88918ecb2277a3399dfd0183e7677cb0bd0ed57b33 -->

The Agent noted two points that are not decided: the root and documentation
Project classes are candidates for Tarav to provide, and a root should list
its children explicitly, since a root folder can contain a link to a place
that is not its child.
<!-- tarav.breadcrumb 0fb779cdfebd47ed43cb307c7a322614aa6309d7a36465cc0bfb82e4bc69abc6 -->

## Root Projects implemented — 861 and 862

The User asked for the requests to be executed.
<!-- tarav.breadcrumb ac6f8afbd532d5561e2b91098c5695b61902a728110f00a0a0b90bc38a781feb -->

[861](../../../tarav-py/notes/live/861-root-project-and-shared-harness-impl-req.md)
added three things:

- `RootProject` ([root.py](../../../tarav-py/src/tarav/l2/project/root.py),
  `Tarav.Project.Root`), whose `checks()` are those of the children its marker
  lists.
- Child markers that use an ancestor's harness (`harness.project`).
- A harness manifest that lists several trusted Project Types (`projects`),
  started through `tarav.l3.project.launch`.

A child with its own environment is reported as one result per POI type with
its count.

## Global Project index — 882

<!-- tarav.sessions
1ecb7d18 = codex:01a11db9-9ffe-7390-a38b-7b12d4b07714 @1ecb7d185a8f713f39ddd88e8dd5b622aff55d59ec635ba0824227061124aac5
-->

The User wants a holistic enumeration of Projects, including ones whose folders
have moved. Project commands and `tarav run --project` should notify Tarav of a
Project's existence, and `tarav project list --global` should identify it by a
stable ID.
<!-- tarav.breadcrumb 5c7aa1327a1f60520c059bfd1994e133d8a582d247d2fba5c6b32b03b18968e6 -->

[Impl.Req 882](../../../tarav-py/notes/live/882-global-project-index-impl-req.md)
adds a machine-local index keyed by each marker's `project_id`. Explicit
Project operations observe the marker on a best-effort basis. Global listing
validates remembered locations and retains missing paths; an explicit root scan
can find a moved Project again. Two live locations with one ID are shown as
ambiguous. The marker remains the identity authority, and moving a Project
cannot be detected until a command observes its new location or an explicit
scan reaches it.
<!-- tarav.breadcrumb 74f760c810597c184fdc636f22b16b2bf292bca1b19ba83a2434165fa918091c -->

[862](../../../tarav-py/notes/live/862-taravangian-as-a-project-tree-impl-req.md)
added general development types
([dev.py](../../../tarav-py/src/tarav/l2/project/dev.py)):
`PythonPackageProject`, whose check is the test suite, and `DocsProject`,
whose checks are each skill's own checks and wiki Notes with unsubmitted
markers. `taravangian-project` now runs as a root over `tarav-py` and
`tarav-md`. md-library uses the same mechanism for its development root and
its depots.
