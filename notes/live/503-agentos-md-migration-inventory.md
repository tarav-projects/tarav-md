# Agentos-md Migration Inventory

Inventory and initial classification for migrating the Agentos markdown surface into `agentos-md`.

## Scope

Migration objective:

- make `agentos-md` the markdown implementation of the Agentos project
- treat `agentos-md` as the home for `Design.Target.Model:Agentos`
- keep `agentos-py` focused on the Python CLI/backend implementation surface
- migrate first, redesign after the old design surface is present

## Source Inventory

Current migrated source markdown/design-bearing surface:

- `AGENTS.md`
- `README.md`
- `notes/index/`: 10 markdown files
- `notes/live/`: 21 active live-note files
- `notes/live/archived/`: 34 archived live-note files
- `skills/`: 33 active markdown skill/reference files
- `_DEPRECATED/`: 27 deprecated markdown skill files

## Migrated Index Surface

The first migration pass copied all files from:

- source: `agentos-py/notes/index/*.md`
- destination: `agentos-md/notes/live/migrated-agentos-index/`

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
- the folder was moved under `notes/live/` after the first promotion pass so legacy evidence does not remain inside the active index root

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

- `004-Agentos.Project.md` -> promoted into `notes/index/105-Agentos.Project.md`
- `006-Session.Model.md`
- `007-Chatlas.Standard.Model.Contract.md`

Legacy but useful:

- `000-index.md`
- `001-chat-session-interface.md`
- `002-Tara.Integration.Ontology.md`
- `003-Agentos.Mission.md` -> promoted into `notes/index/107-Agentos.Mission.md`
- `005-Agentos.Skills.md` -> promoted into `notes/index/106-Agentos.Skills.md`

Needs consolidation:

- `006-Session.Model.md`
- `007-Chatlas.Standard.Model.Contract.md`

Promoted but may need later detail review:

- `003-Agentos.Mission.md`
- `005-Agentos.Skills.md`

Implementation-specific or status-like material that may belong outside the final index:

- `DOING.md`
- `consolidation-score.md`

## Follow-Up Migration Passes

Next likely sources:

- active `agentos-py/notes/live/*.md`
- archived `agentos-py/notes/live/archived/*.md`
- deprecated index-note skills under `agentos-py/_DEPRECATED/`
- root `AGENTS.md` and `README.md`

Expected handling:

- durable design truth promotes into `agentos-md/notes/index/`
- implementation/development workflow guidance becomes `Agentos.Dev.Notes`
- live design artifacts can remain in `notes/live/` or be summarized
- obsolete or status-only material can be kept as migration evidence but should not become final design truth

## End Log

- 2026-05-04: Created initial migration inventory and copied `agentos-py/notes/index/*.md` into `agentos-md`.
- 2026-05-04: Copied active skills from `agentos-py/skills/` into `agentos-md/skills/` with exact path preservation.
- 2026-05-04: Promoted `Agentos.Project`, `Agentos.Skills`, and `Agentos.Mission` into active index notes; moved legacy migrated index evidence to `notes/live/migrated-agentos-index/`.
