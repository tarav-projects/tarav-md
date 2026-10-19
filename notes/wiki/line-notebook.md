# Line Notebook

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## Workflow and Project integration

The agreed design separates the [Lines primitives](lines-workflow.md) from
Line Notebook, a workflow providing the central persistent home for Blocks
and Lines. Notebook owns storage, capture, retrieval, and organization; Lines
supplies the recursive typed contexts. Notebook is intended to play a role
analogous to Chatlas's home for chats.
<!-- tarav.breadcrumb 0114b579847d -->
<!-- tarav.breadcrumb 538cfa114882 -->

A participating Project gets a notebook partition rooted in a Project Block.
Its Project Type can provide a default layout of typed Blocks and extend that
layout for its own work. The Project integrates checks, POIs, and actions;
it is an integration surface for the notebook's behavior. Exact class and
accessor names remain implementation choices.
<!-- tarav.breadcrumb 8f5d0282be58 -->
<!-- tarav.breadcrumb 5faef8e3fddb -->

## Default discussion and current model

The default layout has a Project root with three typed sibling branches:
Discussion, Model, and Archive. Discussion stores conversation and reasoning;
its content carries no obligation to implement it or align another surface
with it. Model aims to represent the Project's current design and can carry
alignment and maintenance obligations. Model here is a typed Block within
the notebook.
<!-- tarav.breadcrumb 18a9929cf7d1 -->
<!-- tarav.breadcrumb 215d0f2ea689 -->

Lines explain a Block's intended reading; its Type supplies code for assertions,
checks, and other operational behavior. Possible protections include a
read-only root or an explicit acceptance step for edits. These are capabilities
to design for particular Types, not a universal approval requirement for
capture.
<!-- tarav.breadcrumb 2048adc9463e -->
<!-- tarav.breadcrumb 7fed2ad6797e -->

## First use: recover a design archive

The first intended use is an Archive Block containing recovered legacy
design discussions. Its Lines establish the historical context inherited by
the recovered Blocks; inclusion does not claim that the material is current
design. The first implementation places Archive beside Discussion and Model;
the arrangement can evolve through later design and use. Candidate sources
include the old Diagram stores, Archive.Attic
repositories, and historical Markdown indexes and their Git histories.
<!-- tarav.breadcrumb c954c91f710c -->
<!-- tarav.breadcrumb b484181f85e1 -->

Start by selecting the most recent suitable recovered state. “Current archive”
means the selected archive snapshot, not a claim of present applicability.
Git can record changes after import. General historical reconstruction belongs
to the separate [Lineage design](lineage.md); the first notebook/import should
not require a Block-specific version system.
<!-- tarav.breadcrumb 74db021699d7 -->
<!-- tarav.breadcrumb 3bf8feada293 -->

## Implemented first use — request 931

[Request 931](../../../tarav-py/notes/live/931-line-notebook-impl-req.md) implements
the bounded storage, Project layout, and first import. The Python
[Notebook](../../../tarav-py/src/tarav/l1/notebook/__init__.py) uses the
Notebook Workflow partition of the existing Record Registry. Each Line or
Block is one JSON Record keyed by Ship. The
[Project binding](../../../tarav-py/src/tarav/l2/project/notebook.py) selects a
ProjectBlock; explicit create() seeds its explanatory Lines and three typed
sibling Blocks once. Existing layouts and edits are loaded without regeneration.
<!-- tarav.breadcrumb 0a93a5eb1c22 -->
<!-- tarav.breadcrumb 89bee5b1a16a -->

Run Python through Tarav and initialize the current runtime before using the
default store. A minimal example from the umbrella Project is:

```python
from pathlib import Path
from tarav.l3.runtime import get_runtime
from tarav.l2.project import Project

get_runtime()
project = Project.from_path(Path("/Users/pereiro/projects/taravangian-project"))
book = project.notebook()
root = book.root
archive = book.archive
for item in archive.contents:
    print(type(item).__name__, item.id)
```

Notebook.save(obj) writes one Record. Notebook.save_tree(block) writes its
contained tree. Notebook.load(ship) resolves the connected context with shared
object identity. Notebook.commit(message) explicitly records changes in Git.
The [storage and layout tests](../../../tarav-py/tests/test_project_notebook.py)
and [storage tests](../../../tarav-py/tests/test_notebook.py) verify reload,
identity continuity, mixed contents, and preservation of edits. This first
implementation adds no alignment engine, editing protections, move operations,
or general Lineage API.
<!-- tarav.breadcrumb a158c6f2a488 -->
<!-- tarav.breadcrumb c1476bc6d5e0 -->

The [bounded recovery script](../../../tarav-py/scripts/import_legacy_notebook.py)
imported 1,581 legacy Lines, 269 legacy Blocks, and nine former Model groupings
as ordinary Blocks. It selected the latest explicit editions in the two
retained Diagram stores and preserved text and Ships. Former labels became
ordinary Lines. The live Tarav root Project's notebook now has 2,149 Records
including explanatory and label Lines. Original namespace, ship, annotation,
and richer edition data were copied alongside the conversion; the 38 former
Collection records remain there as raw source.
<!-- tarav.breadcrumb 5f3ab7cb0427 -->
<!-- tarav.breadcrumb b246defca8b1 -->

The local partition is
`~/Documents/tarav/records/92338514-6f87-4dad-8a41-3148020f90d4`.
Its import report is
`imports/ee7c5865-2209-516f-8be2-361eea2d8f18/report.json`.
The data commit is `a14e4955`. Reopening the Project root verified all 1,581
legacy texts and Block links, all 1,859 selected source hashes, and reachability
of all 2,149 Records. The
[recovery tests](../../../tarav-py/tests/test_notebook_recovery.py) cover
latest-edition selection, source retention, fresh-process execution, and
refusal to overwrite a later notebook edit. Older Markdown indexes, Git
histories, and unfinished Drafts were not part of this selected first import.
<!-- tarav.breadcrumb 49908ac5c359 -->
<!-- tarav.breadcrumb 6d8bb0536f55 -->
