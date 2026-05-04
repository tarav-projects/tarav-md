# Agentos.Project.Doctor Checks - design-session

## Purpose

Collect candidate checks for enriching `Agentos.Project.Doctor`.

This is not an implementation plan yet. Each item is open until discussed, shaped, and either accepted, changed, split, or dropped.

The goal is to identify check families across Agentos subsystems so later work can decide which checks belong in `Doctor.CLI`, `Doctor.Skill`, or mixed doctor workflows.

## Status

- Session state: open
- Implementation state: not started
- Default posture: collect candidates first, design each item later

## Items

- Project.Identity.Checks: [open]
- Surface.Presence.Checks: [open]
- Md.Surface.Checks: [open]
- Agentos.Index.Notes.Checks: [open]
- Index.Note.Style.Checks: [open]
- Ontology.Registry.Checks: [open]
- Dotted.Notation.Checks: [open]
- File.Numbering.Protocol.Checks: [open]
- Reserved.Notes.Checks: [open]
- TODOS.Note.Checks: [open]
- Live.Scripts.Checks: [open]
- Agentos.Dev.Notes.Checks: [open]
- Agentos.Skills.Checks: [open]
- Usage.Skill.Checks: [open]
- Project.CLI.Checks: [open]
- Maintenance.System.Checks: [open]
- Doctor.CLI.Output.Checks: [open]
- Doctor.Skill.Report.Checks: [open]
- Doctor.Check.Schema.Checks: [open]
- Canonical.Reference.Implementation.Checks: [open]
- Migration.Legacy.Surface.Checks: [open]
- Authority.Drift.Checks: [open]
- Artifact.Surface.Checks: [open]
- Design.Session.Artifact.Checks: [open]
- Live.Note.Artifact.Checks: [open]
- Chatlas.Surface.Checks: [open]
- Mission.Surface.Checks: [open]
- External.Integration.Surface.Checks: [open]

## Candidate Notes

### Project.Identity.Checks

Candidate checks:

- `.agentos/project.json` exists when a target claims to be an `Agentos.Project`
- `.agentos/project.json` parses as JSON
- `.agentos/config.json` is not treated as the project identity marker
- commands resolve the intended project root
- component repos such as `agentos-md` and `agentos-py` are classified clearly as project roots or implementation components

Likely layer:

- deterministic identity checks in `Doctor.CLI`
- adoption interpretation in `Doctor.Skill`

### Surface.Presence.Checks

Candidate checks:

- detect `AGENTS.md`
- detect `.agentos/`
- detect `notes/index/`
- detect `notes/live/`
- detect `skills/`
- detect `dev/live/`
- report observed surfaces without assuming every surface is required

Likely layer:

- deterministic surface inventory in `Doctor.CLI`
- adoption interpretation in `Doctor.Skill`

### Md.Surface.Checks

Candidate checks:

- active markdown surfaces use current registered names such as `Md.Surface:Agentos.Stack`
- markdown implementation surfaces are distinguishable from concrete implementation surfaces
- `AGENTS.md` remains local guidance, not the design SSOT
- markdown surfaces route to `notes/index/` for durable design truth when applicable

Likely layer:

- deterministic stale-name search in `Doctor.CLI`
- semantic authority judgment in `Doctor.Skill`

### Agentos.Index.Notes.Checks

Candidate checks:

- `notes/index/000-index.md` exists when `notes/index/` exists
- `000-index.md` routes durable concept notes, not progress artifacts
- index notes are concept-centered or clearly marked as stubs
- live design sessions are not active authority after promotion
- external durable design truth is promoted or referenced from the index

Likely layer:

- file existence and routing inventory in `Doctor.CLI`
- note-quality and authority judgment in `Doctor.Skill`

### Index.Note.Style.Checks

Candidate checks:

- stable index notes have explicit title and concept name
- sections are block-structured
- notes include definitions, boundaries, rules, or related concepts where useful
- low-friction drafts are not falsely treated as complete notes
- stubs meet `Stub.Convention` minimums

Likely layer:

- mostly `Doctor.Skill`
- possible deterministic heading/section checks later

### Ontology.Registry.Checks

Candidate checks:

- `notes/index/ontology.md` exists when index notes use dotted concepts
- registry entries are small concept blocks
- important index concepts have registry entries
- registry stays low-resolution and does not become deep concept development
- registry points to fuller notes when they exist

Likely layer:

- deterministic entry discovery in `Doctor.CLI`
- concept importance judgment in `Doctor.Skill`

### Dotted.Notation.Checks

Candidate checks:

- dotted concept names are registered when stable
- parameterized notation uses `Concept.Name:Target`
- colon parameters are not treated as new concepts by default
- stale dotted names are detected
- approximate or old names are mapped to registered names during discussion

Likely layer:

- deterministic dotted-name extraction in `Doctor.CLI`
- semantic classification in `Doctor.Skill`

### File.Numbering.Protocol.Checks

Candidate checks:

- active numbered files use three-digit prefixes
- active numeric prefixes are unique in the relevant surface
- project-wide collisions are detected where required
- reserved files stay in `000-099`
- index notes use `100-499`
- live notes and live scripts use `500-999`
- allocator behavior is append-only and does not gap-fill

Likely layer:

- deterministic checks in `Doctor.CLI`
- migration-context interpretation in `Doctor.Skill`

### Reserved.Notes.Checks

Candidate checks:

- `notes/index/000-index.md` exists for active index surfaces
- `notes/live/010.TODOS.md` exists for active live-note surfaces
- reserved notes keep their fixed roles
- reserved ranges are not used casually by ordinary files

Likely layer:

- deterministic `Doctor.CLI`
- adoption-context warnings in `Doctor.Skill`

### TODOS.Note.Checks

Candidate checks:

- `notes/live/010.TODOS.md` exists when `TODOS.Note` is adopted
- TODO note remains lightweight
- TODO note does not become a full project-management surface
- TODO items point to durable artifacts when follow-up needs deeper work

Likely layer:

- existence in `Doctor.CLI`
- content-scope judgment in `Doctor.Skill`

### Live.Scripts.Checks

Candidate checks:

- `dev/live/` scripts use correct numbering range
- live scripts can be runnable, partial, or fake
- stable reusable commands are promoted toward `Project.CLI`
- script-shaped target surfaces do not become hidden design authority

Likely layer:

- deterministic file inventory in `Doctor.CLI`
- promotion/authority judgment in `Doctor.Skill`

### Agentos.Dev.Notes.Checks

Candidate checks:

- internal development guidance is separated from external usage guidance
- `AGENTS.md` routes development behavior without becoming design SSOT
- future `notes/dev/` surfaces, if present, stay internal-development oriented
- repeated durable design truth in dev notes is promoted to `Agentos.Index.Notes`

Likely layer:

- mostly `Doctor.Skill`

### Agentos.Skills.Checks

Candidate checks:

- skill folders have `SKILL.md`
- skill frontmatter has name and description
- skill descriptions are trigger-useful and not overly broad
- usage skills derive durable concepts from `notes/index/`
- skill references do not define unregistered durable concepts
- imported skill depots are synced when relevant

Likely layer:

- deterministic inventory and import status in `Doctor.CLI`
- semantic trigger and authority judgment in `Doctor.Skill`

### Usage.Skill.Checks

Candidate checks:

- `<project>-usage` exists when a public usage surface is expected
- usage skill explains how to use the project, not how to develop it
- usage skill routes to deeper references when needed
- usage skill derives durable design truth from index notes

Likely layer:

- deterministic presence checks in `Doctor.CLI`
- boundary judgment in `Doctor.Skill`

### Project.CLI.Checks

Candidate checks:

- project CLI exists when declared
- CLI help is available
- deterministic commands used by skills are available
- `agentos doctor ...` exists for `Project.CLI:Agentos`
- CLI commands remain independently useful, not only skill internals

Likely layer:

- deterministic command checks in `Doctor.CLI`
- usefulness and surface-boundary judgment in `Doctor.Skill`

### Maintenance.System.Checks

Candidate checks:

- maintenance model is diagnosis-first
- doctor findings do not auto-fix
- subsystem checks are discoverable
- issue-report or TODO follow-up is explicit, not automatic
- project-specific maintenance conventions are documented when they exist

Likely layer:

- mostly `Doctor.Skill`

### Doctor.CLI.Output.Checks

Candidate checks:

- `agentos doctor ...` output is machine-readable or consistently structured
- CLI returns check-like statuses when deterministic checks are added
- CLI output distinguishes target, scope, evidence, and status
- missing optional subsystems are `skip` or `info`, not false failures

Likely layer:

- deterministic meta-checks in `Doctor.CLI`
- report-usability judgment in `Doctor.Skill`

### Doctor.Skill.Report.Checks

Candidate checks:

- report includes target and mode
- report distinguishes findings, passed checks, skipped checks
- findings include check, surface, evidence, why it matters, and suggested next step
- report does not fix or imply fixes were applied
- report distinguishes declared, observed, and expected adoption

Likely layer:

- skill self-check or review check

### Doctor.Check.Schema.Checks

Candidate checks:

- decide whether `Doctor.Check` needs a shared JSON schema
- define allowed statuses
- define required evidence fields
- define severity versus status if they remain separate
- decide whether CLI and skill share the same schema

Likely layer:

- design item first
- later CLI/schema validation

### Canonical.Reference.Implementation.Checks

Candidate checks:

- canonical reference implementations are not treated as authority above the md surface
- implementation examples are compared against `Md.Surface`
- drift from canonical implementation is reported only when the md surface supports the concern

Likely layer:

- mostly `Doctor.Skill`

### Migration.Legacy.Surface.Checks

Candidate checks:

- migrated legacy notes are not inside active `notes/index/`
- legacy surfaces are clearly marked as evidence
- promoted legacy material has active index destinations
- unresolved migrated surfaces have TODOs or design items
- stale paths from old repo layout are detected

Likely layer:

- deterministic path/search checks in `Doctor.CLI`
- promotion-state judgment in `Doctor.Skill`

### Authority.Drift.Checks

Candidate checks:

- `AGENTS.md` is not a progress tracker or design log
- skills do not define durable concepts absent from index
- live notes are not used as active authority after promotion
- design summaries are provenance unless explicitly active
- index remains the durable design SSOT

Likely layer:

- deterministic stale-string search in `Doctor.CLI`
- semantic drift judgment in `Doctor.Skill`

### Artifact.Surface.Checks

Candidate checks:

- design-summary, design-session, impl-req, and issue-report artifacts follow their skill-defined formats
- artifact status is clear
- artifacts are not incorrectly routed as active index authority
- issue reports remain problem descriptions, not speculative implementation plans

Likely layer:

- format checks can become `Doctor.CLI`
- artifact-role judgment in `Doctor.Skill`

### Design.Session.Artifact.Checks

Candidate checks:

- closed design sessions are not edited as active design surfaces
- open sessions have item states
- session status can be summarized from the artifact
- closed sessions are promoted into index notes or linked as provenance

Likely layer:

- deterministic artifact-state checks later
- promotion judgment in `Doctor.Skill`

### Live.Note.Artifact.Checks

Candidate checks:

- live notes use `500-999` range except reserved notes
- live notes are not treated as durable SSOT unless promoted
- live-note drafts are classified as drafts or migration artifacts
- live notes with durable signal have TODOs or index-promotion paths

Likely layer:

- deterministic numbering checks in `Doctor.CLI`
- promotion judgment in `Doctor.Skill`

### Chatlas.Surface.Checks

Candidate checks:

- Chatlas usage skill matches current CLI surface
- session model notes are classified as active subsystem notes or legacy evidence
- Chatlas-specific source of truth claims do not conflict with Agentos index authority
- provider-specific session data remains separated from provider-neutral model claims

Likely layer:

- subsystem-specific doctor checks later
- likely mixed checks

### Mission.Surface.Checks

Candidate checks:

- mission command exists if `Agentos.Mission` is adopted
- mission files, if present, are coordination anchors and not project-management dumps
- mission surfaces link out to notes/artifacts rather than absorb them
- default mission selection behavior is documented or checked by CLI

Likely layer:

- deterministic command/storage checks in `Doctor.CLI`
- role-boundary judgment in `Doctor.Skill`

### External.Integration.Surface.Checks

Candidate checks:

- external integration declarations are current or clearly legacy
- consumer-side ontology mappings do not pollute core Agentos ontology
- external integration notes point to source systems when still active

Likely layer:

- mostly `Doctor.Skill`

## End Log

- 2026-05-04: Created candidate check design session from current Agentos index, skills, and CLI surfaces. All items intentionally remain open.

