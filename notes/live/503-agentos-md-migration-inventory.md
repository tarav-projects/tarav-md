# Agentos-md Migration Inventory

Inventory and initial classification for migrating the Agentos markdown surface into `agentos-md`.

## Scope

Migration objective:

- make `agentos-md` the markdown implementation of the Agentos project
- treat `agentos-md` as the home for `Design.Target.Model:Agentos`
- keep `agentos` focused on the Python CLI/backend implementation surface
- migrate first, redesign after the old design surface is present

## Source Inventory

Current `agentos` markdown/design-bearing surface:

- `AGENTS.md`
- `README.md`
- `notes/index/`: 10 markdown files
- `notes/live/`: 21 active live-note files
- `notes/live/archived/`: 34 archived live-note files
- `skills/`: 33 active markdown skill/reference files
- `_DEPRECATED/`: 27 deprecated markdown skill files

## Migrated Index Surface

The first migration pass copied all files from:

- source: `agentos/notes/index/*.md`
- destination: `agentos-md/notes/index/migrated-agentos-index/`

Files copied:

- `000-index.md`
- `001-chat-session-interface.md`
- `002-Tara.Integration.Ontology.md`
- `003-Agentos.Mission.md`
- `004-Agentos.Project.md`
- `005-Agentos.Skills.md`
- `006-Session.Model.md`
- `007-Chatlas.Standard.Model.Contract.md`
- `DOING.md`
- `consolidation-score.md`

Numbering rule:

- original filenames and numeric handles were preserved
- no renumbering was performed
- the migrated folder is a transitional holding surface, not the final consolidated index structure

## Migrated Skill Surface

The second migration pass copied all active skill files from:

- source: `agentos-py/skills/`
- destination: `agentos-md/skills/`

Copy result:

- 43 files copied
- directory structure and filenames preserved
- source and destination trees match exactly at copy time

Initial classification:

- active public Agentos skills: copied for later redesign/consolidation
- active artifact/design/session skills: copied as current behavior surfaces
- skill references and agent configs: copied as supporting md-surface material
- Python packaging/runtime ownership is deferred to a later implementation pass

## Initial Classification

Already stable enough to use as migration input:

- `004-Agentos.Project.md`
- `006-Session.Model.md`
- `007-Chatlas.Standard.Model.Contract.md`

Legacy but useful:

- `000-index.md`
- `001-chat-session-interface.md`
- `002-Tara.Integration.Ontology.md`
- `003-Agentos.Mission.md`
- `005-Agentos.Skills.md`

Needs consolidation:

- `003-Agentos.Mission.md`
- `005-Agentos.Skills.md`
- `006-Session.Model.md`
- `007-Chatlas.Standard.Model.Contract.md`

Implementation-specific or status-like material that may belong outside the final index:

- `DOING.md`
- `consolidation-score.md`

## Follow-Up Migration Passes

Next likely sources:

- active `agentos/notes/live/*.md`
- archived `agentos/notes/live/archived/*.md`
- deprecated index-note skills under `agentos/_DEPRECATED/`
- root `AGENTS.md` and `README.md`

Expected handling:

- durable design truth promotes into `agentos-md/notes/index/`
- implementation/development workflow guidance becomes `Agentos.Dev.Notes`
- live design artifacts can remain in `notes/live/` or be summarized
- obsolete or status-only material can be kept as migration evidence but should not become final design truth

## End Log

- 2026-05-04: Created initial migration inventory and copied `agentos/notes/index/*.md` into `agentos-md`.
- 2026-05-04: Copied active skills from `agentos-py/skills/` into `agentos-md/skills/` with exact path preservation.
