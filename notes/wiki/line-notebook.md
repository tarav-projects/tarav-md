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

The proposed default layout has a Project root with two typed branches:
Discussion and Model. Discussion stores and indexes conversation and reasoning;
its content carries no obligation to implement it or align another surface
with it. Model aims to represent the Project's current design and can carry
alignment and maintenance obligations. Model here is a typed Block within
the notebook.
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
design. Whether Archive is nested beneath Discussion remains open for use
to inform. Candidate sources include the old Diagram stores, Archive.Attic
repositories, and historical Markdown indexes and their Git histories.
<!-- tarav.breadcrumb c954c91f710c -->

Start by selecting the most recent suitable recovered state. “Current archive”
means the selected archive snapshot, not a claim of present applicability.
Git can record changes after import. General historical reconstruction belongs
to the separate [Lineage design](lineage.md); the first notebook/import should
not require a Block-specific version system.
<!-- tarav.breadcrumb 74db021699d7 -->
<!-- tarav.breadcrumb 3bf8feada293 -->

These sections capture agreed design and proposed implementation scope. They
do not claim that Notebook storage, Project partitions, or recovery imports
have been implemented by this Wiki capture.
