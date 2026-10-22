# Projects

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Core and specialized integrations

### Explicit capability paths — 2026-10-07

The User chose `project.docs.wiki.daily(date)`, `project.models.ls()`, and `project.checks.run()` as the Project API shape. Top-level Project members should generally state concrete object meaning; shared or abstract capability operations should sit under semantic paths. `docs` groups documentation, `models` is a bound capability in its own right, and `checks` comes from the common CheckProvider contract.
<!-- tarav.breadcrumb 2c873fc0f395 -->
<!-- tarav.breadcrumb fea17d25ee0a -->

The first implementation exposes `project.docs.wiki`, `project.models`, and `project.checks`; `checks.suite()` builds the runnable suite and `checks.run()` executes it. Named Model listing reads the Project marker, while `get()` and `main()` still require the disconnected Models backend. This access-path change does not itself restore Model resolution. See [Impl.Req 866](../../../tarav-py/notes/live/866-project-capability-paths-impl-req.md).
<!-- tarav.breadcrumb dc892a154968 -->


The design separates a workflow's minimal functionality from specialized
integrations. Loading Models for another consumer should not bring along
Project-specific functionality; the same concern applies to the Project core.
The proposed organization places Model operations under `models/` and the
Project–Model integration under `project/models/`, with `ProjectModels`
connecting the two domains.
<!-- tarav.breadcrumb 493b9e2dc3cb -->
<!-- tarav.breadcrumb df69e6de9598 -->

## Explicit project capabilities

The minimal and more featured Project types should be provided now, not
deferred until a later consumer appears. A caller chooses the interface with
`<ProjectClass>.from_path(path)`. This split also establishes the mechanism
for other systems to subtype Projects. The discussed names are `TaravProject`
for the minimal base and `Project` for Tarav's more opinionated variant.
<!-- tarav.breadcrumb eb0cdcf6ee1c -->

Project integration can be exposed through `project.models()` or through a
specialized `ProjectModels(project)` interface. Whether it belongs directly
on a Project class depends on that class's intended capabilities; Models need
not be part of every project's minimal contract. The precise accessor return
shape remains an implementation choice, not settled here.
<!-- tarav.breadcrumb b2c41014c434 -->

## Project-local types

A project can implement its own Project subtype in its folder, attaching
project-specific operations and configuration. Tarav supplies common types;
individual projects specialize the suitable base. This is a concrete intended
usage of Project subtyping, not a request for one universal Project class to
accumulate every subsystem's functionality.
<!-- tarav.breadcrumb 07505d50a873 -->

These sections capture design intent; they do not claim the subtype split or
integration extraction has been implemented.

## First implementation of the split

The user selected Wiki-backed Develop for this design.
<!-- tarav.breadcrumb ed0aa0197d7f -->

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
<!-- tarav.breadcrumb 9613d530e936 -->
<!-- tarav.breadcrumb 8ff60071e1c6 -->

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
<!-- tarav.breadcrumb 82d59f20c620 -->

The discussion entered implementation Design in
[824](../../../tarav-py/notes/live/824-project-local-python-harness-impl-req.md).
Its package layout and bootstrap mechanics remain implementation proposals;
this capture does not claim they have been implemented.
<!-- tarav.breadcrumb 5f9589358437 -->

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
<!-- tarav.breadcrumb 8a2e200a8fed -->

## Explicit Tarav process launching

[826](../../../tarav-py/notes/live/826-tarav-process-launching-impl-req.md)
is implemented. The [Python runner](../../../tarav-py/src/tarav/l1/python_env/runner.py)
defines `RunnerConfiguration`, an abstract `RunnerConfigurator`, and the
current-environment specialization. The [shared execution engine](../../../tarav-py/src/tarav/l1/python_env/core.py)
runs only the file, source, stdin, and arguments supplied by its caller. The
general `tarav run` adapter selects current or Project configuration; it does
not import a runtime factory, inject a Project, or make Record loading switch
environments.
<!-- tarav.breadcrumb f3f3f542857f -->
<!-- tarav.breadcrumb ad3faf722f82 -->

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
<!-- tarav.breadcrumb acc3077a2618 -->

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
<!-- tarav.breadcrumb 252778bad09c -->

The Agent first proposed a separate object for the library and then a separate
Harness object attached to a Project. The User considered renaming, since a
Project should keep overlaying the folder-rooted project of an agent tool, and
then settled it differently: Tarav does not model the Python library. A
library is Python's concern, which is where code lives and how it is imported.
A Tarav Project is an object inside a Python library, and one library can
hold several Project objects. The Agent withdrew both proposals. "Harness"
remains an ordinary word for what a Project gives its place.
<!-- tarav.breadcrumb e50d8ac558fb -->
<!-- tarav.breadcrumb 0ad29e402d83 -->

What a harness means in a place, in the User's terms: running the project
checks there runs the checks proper to that place, as a test suite would; and
the place's `AGENTS.md` and skills tell agents how to use the code made for
that place. A consumer place inherits checks, types and commands from the
library it imports, and every Project keeps its own point of extension for
code that belongs to no library.
<!-- tarav.breadcrumb e3bf2f581ca3 -->

Where the code of a Project class sits is a packaging choice. A library may
keep its development harness in the same code base, under a namespace such as
`.dev`, or in a separate one; Tarav should not care. Tarav needs to know how
to find the Project object that harnesses a folder, and the reading paths that
contextualise agents must document it. A consumer should have no use for the
development Project of the library it imports, even when that Project ships in
the same package.
<!-- tarav.breadcrumb b1001fbf8888 -->

A Project class defined by a library is a control point: a place that subtypes
it runs the checks the library defined. md-library's depots are the first
intended case.
<!-- tarav.breadcrumb ccbea9715ce5 -->

### Root Project over child Projects

A development folder can be a small graph of Projects: a root Project whose
checks are those of the Projects below it, with an implementation Project and
a documentation Project as children, sharing one Python environment at the
root. The User described this for md-library and confirmed that it is general:
`taravangian-project` has the same layout and should get it as well.
<!-- tarav.breadcrumb fdb73a4817b7 -->
<!-- tarav.breadcrumb 1da500bbadea -->

The Agent noted two points that are not decided: the root and documentation
Project classes are candidates for Tarav to provide, and a root should list
its children explicitly, since a root folder can contain a link to a place
that is not its child.
<!-- tarav.breadcrumb 0fb779cdfebd -->

## Root Projects implemented — 861 and 862

The User asked for the requests to be executed.
<!-- tarav.breadcrumb ac6f8afbd532 -->

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
<!-- tarav.breadcrumb 5c7aa1327a1f -->

[Impl.Req 882](../../../tarav-py/notes/live/882-global-project-index-impl-req.md)
adds a machine-local index keyed by each marker's `project_id`. Explicit
Project operations observe the marker on a best-effort basis. Global listing
validates remembered locations and retains missing paths; an explicit root scan
can find a moved Project again. Two live locations with one ID are shown as
ambiguous. The marker remains the identity authority, and moving a Project
cannot be detected until a command observes its new location or an explicit
scan reaches it.
<!-- tarav.breadcrumb 74f760c81059 -->

[862](../../../tarav-py/notes/live/862-taravangian-as-a-project-tree-impl-req.md)
added general development types
([dev.py](../../../tarav-py/src/tarav/l2/project/dev.py)):
`PythonPackageProject`, whose check is the test suite, and `DocsProject`,
whose checks are each skill's own checks and wiki Notes with unsubmitted
markers. `taravangian-project` now runs as a root over `tarav-py` and
`tarav-md`. md-library uses the same mechanism for its development root and
its depots.

## A Project bootstraps from its project.json — 909

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

The Projects of this workspace were of Tarav's generic Types. The User
said that is not right: each Project must be of a unique Type, which may
extend those but not be them.
<!-- tarav.breadcrumb c4bc55018a56 -->

Every Tarav Project has a code base, at least its harness; whether it shares
a code base with the rest of the system is an organization decision. A
Project configures where its harness and its environment are.
<!-- tarav.breadcrumb 33f2d601ffbf -->

A child's Type is defined in its own Project's package, not in the root's.
<!-- tarav.breadcrumb e5884f4c3794 -->

Asked why Project Types were listed in the environment's manifest and not
in the marker, the User answered that there is no reason to split it: the
marker is configuration, loading a Project is a bootstrapping act, and
explicit configuration and paths are fine. The launcher needs an
environment and a path to the Project Type, loaded from a package installed
in that environment with ordinary uv.
<!-- tarav.breadcrumb 8d7b29746dea -->
<!-- tarav.breadcrumb 4d4193686e7b -->
<!-- tarav.breadcrumb 6a5c4ee3fb68 -->

`"class": "agentos.project"` is legacy and goes; a pydantic model describes
the marker and a check checks it. The marker being the whole Record was
split: `project.json` is the Project Record with the Project workflow's own
configuration, `harness` included, and `config.json` is where other
workflows add theirs. The Record's type tag and `harness.type` are both
kept. No legacy handling.
<!-- tarav.breadcrumb c9e06af35770 -->
<!-- tarav.breadcrumb 862942cfadef -->
<!-- tarav.breadcrumb de508aaaa6fa -->
<!-- tarav.breadcrumb d71c4c0a3fe7 -->

Built as request
[909](../../../tarav-py/notes/live/909-project-bootstrap-from-project-json-impl-req.md).
`project.json` has `harness: {environment, type}`; the launcher imports
`harness.type` from that environment and loads the Record with it. The
manifest's `projects` list and the `harness.project` ancestor indirection
are gone. `config.json` sections (`agents`, `skills`, `diagram`) are owned
and validated by their workflows, and `ProjectFilesCheck` reports what does
not fit. The root is now a Git repository tracking an allowlist; its
Projects are `Taravangian.TaravangianRootProject` (a package of the root),
`Taravangian.TaravPyProject` (`tarav.l2.dev.project`) and
`Taravangian.TaravMdProject` (a package of tarav-md). Only this workspace's
Projects were migrated: by the User's choice, the other workspaces wait for
a later pass and do not load until then.

## Every Project under ~/projects on its own harness — 910

The User asked to migrate every other Project, with a configuration like
Taravangian's, starting with a read-only check of all of `~/projects`.
<!-- tarav.breadcrumb 725505541fb3 -->

All Projects under `~/projects` become Tarav Projects shaped like
Taravangian: Types are, by default, in each Project's own harness, so the
children's classes leave the roots' packages; roots become Git repositories
that conservatively track only obvious files; archival Projects are left
alone; the migration is committed in every repository.
<!-- tarav.breadcrumb b56f54d65216 -->

Built as request
[910](../../../tarav-py/notes/live/910-migrate-projects-to-own-harnesses-impl-req.md):
72 Projects in 25 roots and singles. Children of scaffolded roots got
`.tarav/harness/` packages installed by their root's environment; library
roots (md-library, tankefactory) and product environments (telar, g70203)
kept their Types where their owners put them, with `harness` in
project.json. Every Project loads as its Type, and no root raises a
project-files POI. md-library still uses the removed Blessing store, a
separate break.

## The Tarav System Project — 911

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

The User wanted a default Project for the whole machine: every Project
under it without their knowing, a formal way to work on all of them as the
migration of 910 did, starting minimal — information about the Projects, a
list of active ones, basic operations, and checks of its own over them.
<!-- tarav.breadcrumb 049dcb222b2e -->

It is a Project with a repository, skills and documentation, the top of the
user's Tarav system, `TaravSystemProject`, at `~/Documents/tarav/system/`,
created by `tarav init --system`; its active list is manual. Installing
Tarav itself is parked.
<!-- tarav.breadcrumb 7a21fb2eb659 -->
<!-- tarav.breadcrumb 107dd4dec759 -->

A longer discussion considered making it the owner of all workflows and
splitting a Project's roles (library, harness). The User settled it simply:
a Project means a place, as in Claude or Codex; nothing new, just a new
Project at `~/Documents/tarav/system/`.
<!-- tarav.breadcrumb 56d5c72b4b54 -->
<!-- tarav.breadcrumb bc528a2f9cf9 -->

Built as request
[911](../../../tarav-py/notes/live/911-tarav-system-project-impl-req.md):
`TaravSystemProject` (`tarav.l2.project.system`) with its `active` list and
one check per active Project that loads it through its own harness;
`tarav init --system` creates the folder, its own Type, its environment and
its repository. This machine's System Project exists, with one active
Project to start with.


## Project Git hooks — 915

A Project whose root is a Git repository selects Tarav Git hook handlers in
the `git` section of its config; the hooks call the `tarav` CLI, never block
Git, and the Project's checks keep them installed. The first handler is
tarav-change; see [tarav-change](tarav-change.md).
<!-- tarav.breadcrumb 7d4382f74921 -->

## Project-owned integration managers — 940

<!-- tarav.sessions
ec6cf584 = codex:01a1563b-2992-7c62-8a38-05c1cc75b1fe @ec6cf5849bb6c4e66f011b015415da94eeb1a17634872aa4fb9e25d8e065ab53
-->

The User chose ActionManager, ChecksManager, SkwManager and RecordsManager
as integration objects belonging to a Project Class. They separate Project
integration from workflow primitives' core functionality. Other Project Classes
can inherit and extend those managers and their integrations.
<!-- tarav.breadcrumb 781c59f439d7 -->
<!-- tarav.breadcrumb 83d7890c83e8 -->

The User clarified that loops belong to managers too: a loop is one integration
among the capabilities the managers connect. There is no separate Project-loop
layer. Actions and POIs remain general concepts; the current check-related
Situation Chain is a useful particular integration to refine now.
<!-- tarav.breadcrumb 647f2b5ae451 -->
<!-- tarav.breadcrumb 7e72a946b863 -->

The User invoked Develop to create the managers and move existing Project
integration into them.
<!-- tarav.breadcrumb dc17e41766f3 -->

[940](../../../tarav-py/notes/live/940-project-integration-managers-impl-req.md)
implements class-selected `Actions`, `Checks`, `Skw` and `Records`, exposed
through `project.actions`, `project.checks`, `project.skw` and `project.records`.
The [ActionManager](../../../tarav-py/src/tarav/l1/project/actions.py) owns the
existing status loop; Project.status delegates to it and child loops enter
through their own action managers. Checks remain independently runnable.
RecordsManager keeps the existing class/object Record API and selects registry
access for integrations. The base SkwManager binds Documents; its featured
specialization handles skill-depot discovery and checks formerly held by
DocsProject. [Manager tests](../../../tarav-py/tests/test_project_managers.py)
exercise overrides of all four managers, custom action storage, direct checks,
child loops and SKW binding. These are implementation facts, not additional
User decisions or a new universal hook protocol.
