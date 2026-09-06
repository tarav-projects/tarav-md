# 780 — Reading Club first slice — Impl.Req

Status: Completed

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
- status: completed.

### Slice 2 — First durable Reading Project

- initialize `~/Documents/tarav/reading-club/` as an independent Git repository;
- add concise Club and project guidance plus the first project manifest;
- move the annotated 2025 paper transcript and its study note into that project;
- update PhD navigation surfaces to point to the Reading Club copy while
  preserving `md-library` as the canonical provider transcript;
- observable: `tarav reading-club list/show/find` locates the paper project and
  the PhD has no dead links to the moved surfaces;
- check: file comparison/history inspection, CLI acceptance, and PhD link scan;
- status: completed.

### Slice 3 — Hugentics Reading Club workflow

- expose and route `tarav-hugentics --reading-club [DOCUMENT]`;
- document project discovery/resume, source constancy, the
  `Present → Read → Discuss → Capture → Advance` loop, explicit navigation
  commands, and the distinction between CLI logistics and Agent judgment;
- observable: cold skill reading identifies one complete, usable workflow;
- check: Skill Markdown validation, command-surface inspection, and diff check;
- status: completed.

### Slice 4 — Integration and final audit

- reinstall the editable CLI and run focused plus architectural tests;
- verify the new data repository, Tarav code, skill surface, and PhD references;
- close `780.Impl.Req`, reconcile the final Draft, and apply it once;
- observable: the first Reading Project is navigable and the implementation
  remains aligned with the landed Reading Club Model;
- check: final CLI smoke tests, repository status review, Draft check/apply;
- status: completed.

Risks: turning logistical metadata into document identity; making the CLI own
Agent interpretation; losing inline annotations during the move; leaving PhD
links stale; or accidentally mixing the independent Reading Club Git history
with Tarav implementation repositories.

Deviation triggers: the existing transcript and study note cannot be moved
without losing content; the CLI architecture requires a cross-domain import;
or the landed Reading Club design conflicts with the proposed filesystem
surface.

Acceptance signals:

- `~/Documents/tarav/reading-club/` is an independent Git repository with a
  recoverable initialization checkpoint and a reviewable implementation diff;
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
- Slice 1 added the read-only `tarav.reading_club` domain and registered
  `list`, `find`, and exact `show` commands. Three focused tests, Ruff, and
  `git diff --check` pass.
- Exact Product.Surface production-context annotations are not yet
  representable through the current external-surface primitives; the Git
  checkpoint, diff, Impl.Req, and Draft retain the available coordination and
  capture context as a retryable POI.
- Slice 2 initialized the independent Reading Club repository and moved the
  transcript and study note into its first project. The transcript SHA-256 is
  unchanged (`08f67c334eb67c6de346e1ec40a43f6ad05033d88c4661ccd0c6819543432b63`);
  all 11 transcript and 14 note annotations remain present. PhD navigation
  links now target the Reading Project, and live CLI discovery succeeds.
- The initial “clean repository” acceptance wording conflicted with Execute's
  requirement to leave post-checkpoint changes uncommitted for User review. It
  was corrected to require an independent repository, initialization
  checkpoint, and reviewable implementation diff.
- Slice 3 added and cold-read the routed Reading Club module. It defines
  project resolution, fixed-source boundaries, the natural reading loop, all
  settled runtime commands, and selective capture while leaving equivalence,
  chunking, and interpretation Agent-operated. The skill validator and diff
  check pass.
- The requested public spelling `--reading-club` supersedes the earlier
  proposed `--reading` spelling. The Draft now appends this decision as a new
  edition of the existing Reading.Session command Line rather than creating a
  competing lineage.
- The first Reading Project is an initialized Tarav project associated with
  dedicated Diagram Model `f22e2bb0-5f30-426b-a206-776d4c299bad`.
- The installed editable CLI passes live `list`, `find`, and `show` acceptance.
  The complete `tarav-py` suite passes: 1,556 tests in 59.41 seconds; full Ruff
  validation and diff checks also pass.
- Concurrent work in `tarav-py` created checkpoint `22a9ab3` and included the
  Reading Club code while beginning an unrelated assertion-scoring task. Its
  untracked `src/tarav/scoring/` work was preserved and excluded from this
  implementation's handling.
- Final skill validation, annotation-retention checks, PhD dead-link scan,
  project Model resolution, and repository diff audits pass.
- Closed `780.Impl.Req` and applied its Draft once. Diagram receipt commit:
  `ac1dcec92d9e917610786d308050b1fdc663dcd8`.
- Final Draft POIs include four expected Archive-grounding notices and seven
  unasserted semantic records from this request. The broader Model also reports
  16 Collection-hosted staleness notices and pre-existing missing-Type and
  closed-collection findings; no authorization, schema, support-resolution, or
  command-lineage failure remains.
