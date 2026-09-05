# 780 — Reading Club first slice — Impl.Req

Status: Ready for execution

## Impl.Abstract

Implement the first bounded `Tarav.Reading.Club` product slice:

- establish the independent Git-backed data surface at
  `~/Documents/tarav/reading-club/`;
- add a read-only `tarav reading-club` CLI for simple project discovery and
  navigation;
- add the Agent-operated `tarav-hugentics --reading-club [DOCUMENT]` skill
  module; and
- move the annotated 2025 metabolic-coordination transcript and its active
  study note from the PhD workspace into the first Reading Project, updating
  PhD links without changing the paper content or losing annotations.

The first CLI slice owns logistics, not reading interpretation or cursor
automation. Project selection remains a human/Agent judgment aided by ordinary
metadata; no fingerprinting, canonical-library behavior, or formal document
equivalence enters this implementation.

## Impl.Req.Diagram

- **namespace:** User.Touched.Chatlas.Index / `1c99092c-ba46-4006-adc3-9ada50c00abd`
- **model:** Tarav / `b7b78eab-e5c2-4610-9bf5-1b704a106f34`
- **collection:** 780.Impl.Req / `e3368ae9-46fd-499a-975a-b72b6b66adfb`
- **collection type:** Impl.Req.Collection
- **draft:** `9bad2c4b-6800-4c49-a5ce-fdbb9c36c621` / `/Users/pereiro/Documents/tarav/diagram/drafts/9bad2c4b-6800-4c49-a5ce-fdbb9c36c621.json`
- **authorization gate:** `9ac7f976-a660-4dd1-8ddc-45f85c4a995d`

The Collection hosts supported User-Touched requirements. The live note owns
execution coordination and does not substitute for the Draft.

## Execution.Plan

### Slice 1 — Reading Club data model and navigation CLI

- add a focused `tarav.reading_club` domain using the common Tarav data root;
- define a small project manifest used only as Agent-maintained logistical
  metadata;
- expose `tarav reading-club list`, `find`, and `show`, including JSON output
  and an explicit root override for isolated use and testing;
- keep the CLI read-only and tolerate no hidden document-identity inference;
- observable: the CLI discovers and resolves Reading Projects from one Club;
- check: focused command/domain tests plus CLI help;
- status: not started.

### Slice 2 — First durable Reading Project

- initialize `~/Documents/tarav/reading-club/` as an independent Git repository;
- add concise Club and project guidance plus the first project manifest;
- move the annotated 2025 paper transcript and its study note into that project;
- update PhD navigation surfaces to point to the Reading Club copy while
  preserving `md-library` as the canonical provider transcript;
- observable: `tarav reading-club list/show/find` locates the paper project and
  the PhD has no dead links to the moved surfaces;
- check: file comparison/history inspection, CLI acceptance, and PhD link scan;
- status: not started.

### Slice 3 — Hugentics Reading Club workflow

- expose and route `tarav-hugentics --reading-club [DOCUMENT]`;
- document project discovery/resume, source constancy, the
  `Present → Read → Discuss → Capture → Advance` loop, explicit navigation
  commands, and the distinction between CLI logistics and Agent judgment;
- observable: cold skill reading identifies one complete, usable workflow;
- check: Skill Markdown validation, command-surface inspection, and diff check;
- status: not started.

### Slice 4 — Integration and final audit

- reinstall the editable CLI and run focused plus architectural tests;
- verify the new data repository, Tarav code, skill surface, and PhD references;
- close `780.Impl.Req`, reconcile the final Draft, and apply it once;
- observable: the first Reading Project is navigable and the implementation
  remains aligned with the landed Reading Club Model;
- check: final CLI smoke tests, repository status review, Draft check/apply;
- status: not started.

Risks: turning logistical metadata into document identity; making the CLI own
Agent interpretation; losing inline annotations during the move; leaving PhD
links stale; or accidentally mixing the independent Reading Club Git history
with Tarav implementation repositories.

Deviation triggers: the existing transcript and study note cannot be moved
without losing content; the CLI architecture requires a cross-domain import;
or the landed Reading Club design conflicts with the proposed filesystem
surface.

Acceptance signals:

- `~/Documents/tarav/reading-club/` is an independent, clean Git repository;
- the first project contains the existing annotated transcript and study note;
- all three CLI navigation commands work in text and JSON modes;
- the Hugentics skill routes `--reading-club` to a complete Agent workflow;
- relevant tests pass and unrelated pre-existing work is preserved;
- the Impl.Req Collection is closed and its Draft has one retained receipt.

## Impl.Log

- Alignment.Mode is Autonomous from the explicit `--AUTO` selector.
- The implementation chooses a small per-project `project.json` as logistical
  metadata, not as a content fingerprint, canonical identity, or equivalence
  registry.
- The CLI is deliberately read-only in this slice; Agents perform creation,
  transcript migration, annotation, and Reading.Session interpretation.
- The current PhD copy is already an annotated working transcript, so moving it
  preserves the accumulated reading surface rather than recopying from
  `md-library`.
- No deviations or blockers at design completion.
