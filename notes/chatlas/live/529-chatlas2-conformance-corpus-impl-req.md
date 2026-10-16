# Chatlas2 Conformance Corpus - impl-req

## Impl.Abstract

- **scope:** implement a self-contained Chatlas2 conformance corpus, add one consolidated all-feature script, and ingress the four historical `User.Script.Invariant` scripts with best-effort anonymized copies of their 21 accepted provider sessions' retained artifacts
- **status:** implemented and verified
- **source:** Chatlas2 design session 527, first vertical slice 528, and the explicit implementation request ^c20260815-29u
- **target:** `tarav-py`; historical source material is read from the identical deprecated snapshots under the current and former umbrella repositories
- **out of scope:** perfect or formally complete anonymization; reversible anonymization; portable corpus export/import beyond the included archive; a Claude Chatlas2 normalizer; requiring every provider to expose unsupported native actions; treating normalized output as stored authority
- **acceptance:** the corpus keeps versioned scripts, append-only capture records, and content-addressed anonymized provider artifacts; ingresses all 21 historical accepted sessions without a runtime dependency on the live Chatlas archive; and evaluates the current Codex normalizer against the exact user-message invariant

## Impl.Agendix

- **touched (authorization):** implement the corpus system and ingress the current scripts ^c20260815-29u
- **touched (artifact policy):** include provider artifacts in the known corpus; anonymization is best-effort and operates on text without provider or raw-model knowledge ^c20260815-30u
- **touched (registration workflow):** source recognition, anonymization, specimen-preservation comparison, inspection, and registration run only when an operator intentionally adds a test artifact; the workflow must be documented rather than automated in the background ^c20260815-31u
- **touched (model):** Chatlas2 is a shallow chronological event tape with `User.Event`, `Agent.Event`, `Unresolved.Event`, `Chat.Message`, and conservative `Agent.Loaded.Context`; raw artifacts remain the inspection authority (`527-chatlas2-normal-model-redesign-design-session.md`)
- **touched (implementation):** Chatlas2 already has Codex structural recognition, multi-artifact assembly, inspectable JSON, and one-way dependency enforcement (`528-chatlas2-codex-vertical-slice-impl-req.md`)
- **hard evidence:** both historical corpus directories are byte-identical at commit `2d9a86a4a59d5e4bf2d9b9e4299db058866891f2`; all 21 accepted session IDs resolve from the current Chatlas index with their recorded identity hashes; the 10 Codex captures currently reproduce every canonical user message exactly and in order
- **touched (index):** `Raw.Archive`, `Chatlas.Session.Index`, `Normalization.Pipeline::Chatlas.Session.Model`, `Session.Event.Tape`, `RED.GREEN.Test.Suite`, and `Test.At.Boundaries`
- **structural:** historical script text and accepted-session metadata are ingress sources, not runtime dependencies; the active corpus must be complete inside `tarav-py`
- **open space:** the concrete corpus schema and consolidated-script wording are provisional v1 test surfaces and may evolve without changing the Normal Model

## Impl.Index

### Chatlas2.Conformance.Corpus

- a corpus is a set of immutable capture snapshots grouped by `script_id`, provider, and Chatlas-assigned `Raw.Model.Version`
- repeated runs of one script accumulate; no capture is selected as the canonical run
- exact source transcript bytes remain owned by current Chatlas; the corpus stores best-effort anonymized, losslessly compressed copies of every relevant retained artifact
- each capture pins both the source artifact digest and the included anonymized artifact digest and byte size
- records contain no absolute path; ordinary corpus verification materializes only the included artifacts, while an optional provenance check may resolve the source session through current Chatlas
- a capture identifier is derived from canonical capture content; exact re-ingress is idempotent, while changed raw content produces another append-only snapshot
- malformed records, conflicting duplicate identifiers, missing sessions, identity drift, and missing artifact digests fail visibly

### Chatlas2.Text.Anonymizer

- the anonymizer is a provider-neutral streaming text transformation; it neither parses provider records nor consults `Raw.Model.Version`
- deterministic text substitutions cover home-directory prefixes, emails, UUID/session-shaped identifiers, and obvious credential-shaped values while preserving line order and textual container syntax
- repeated sensitive values map consistently within the corpus so identifiers and references remain joinable
- anonymization is explicitly best-effort: it reports its replacement counts and residual warnings but makes no completeness or secrecy proof
- an outer ingress workflow may run raw-model recognition and normalization before and after anonymization as specimen-preservation checks where compatible implementations exist; the anonymizer itself never performs or depends on those checks
- a transformation that changes recognized `Raw.Model.Version`, canonical user messages, chronology, event classes, or annotation topology for a supported capture is rejected from ingress
- the anonymizer has its own small version recorded in every archived-artifact manifest; changing it creates new content-addressed artifacts rather than rewriting existing blobs

### Chatlas2.Corpus.Ingress

- ingress is an explicit, occasional operator workflow used only to add a new test artifact; no daemon, hook, archive scan, or ordinary test run discovers and registers captures automatically
- the documented loop is: select a closed source session → collect every retained transcript artifact → recognize the source when possible → prepare best-effort anonymized candidates → inspect the candidates and replacement report → compare source/candidate recognition and supported normalization structure → explicitly register the accepted candidate
- preparation is non-mutating with respect to the committed corpus; registration is a separate explicit action that writes content-addressed blobs and appends capture records
- failure of source/candidate recognition agreement prevents labeling the candidate as a specimen of that `Raw.Model.Version`; it is not treated as an anonymization-quality verdict
- ordinary corpus verification and conformance tests consume only committed corpus artifacts and never rerun anonymization or contact the originating archive
- `tests/chatlas2/conformance/README.md` is the operator runbook and documents commands, inspection points, acceptance checks, recovery, and how to add another capture for an existing script/version cell

### Chatlas2.Conformance.Script

- each script has a stable id and revision, exact ordered user messages, provider-neutral operator directions, declared feature targets, and capture-validity requirements
- operator directions are never canonical user messages
- the new `chatlas2-conformance.v1` script exercises ordinary exchange, deterministic tool call/result, dependency on earlier user and tool data, interrupted generation, rollback with alternate continuation, manual compaction, post-compaction recall, and final summary
- native actions are capability evidence: a capture is accepted only when its raw artifact proves every action claimed for that capture
- the four historical scripts remain separate legacy scenarios because they provide already-captured focused evidence for tools, reasoning, rollback/fork, and compaction

### Chatlas2.Capture.Record.V1

- required identity: schema, capture id, script id/revision, provider, hashed native-session and Chatlas-identity references, acceptance status, and captured date
- each artifact member records role, `sha256:<hex>` identity, byte size, and recognized `raw_model_version` or null
- each included artifact additionally records source digest, anonymized digest, compression, anonymizer version, and best-effort replacement summary
- feature evidence is an explicit set attached to the capture; it does not infer provider capabilities from the script alone
- the v1 committed registry contains accepted captures only; rejected preparations remain outside the corpus and are never registered
- registry order is append order; meaning never depends on line position

### Chatlas2.Conformance.Check

- corpus integrity checks are provider-neutral and run even when no Chatlas2 normalizer supports the capture
- corpus integrity reconstructs every included anonymized artifact byte-for-byte, verifies its digest, and never requires access to the originating Chatlas archive
- normalization checks dispatch only after raw-model recognition and report unsupported captures explicitly rather than silently counting them as passing
- current Codex checks assert chronology, raw source resolution, exact ordered user `Chat.Message`s, resolved annotation membership, and conservative event classes
- agent wording, agent-message count, reasoning count, tool count, and context completeness are not cross-provider invariants
- union and retention mechanics continue to use derived same-session artifact cases; repeated independent sessions measure cross-run and cross-provider generalization instead

### Storage.Layout

```text
tests/chatlas2/conformance/
├── README.md
├── captures.jsonl
├── artifacts/
│   └── sha256/
│       └── ab/<anonymized-digest>.raw.gz
├── scripts/
│   ├── chatlas2-conformance.v1.md
│   └── legacy/
│       ├── imaginary-calendar-compact.md
│       ├── knights-knaves.md
│       ├── knights-knaves-restore.md
│       └── primes-utility.md
└── specifications/
    ├── chatlas2-conformance.v1.json
    └── legacy-*.json
```

- package mechanics live under `src/tarav/chatlas2/`; test data and expectations live under `tests/chatlas2/conformance/`
- the CLI accepts an explicit corpus path so installed code never assumes the source checkout layout
- artifact paths are derived from anonymized content digests; no provider, session, username, or source path is encoded in a stored filename

## Execution.Plan

### Slice 1 - Establish the corpus and capture contracts

- add RED tests for strict script/capture loading, canonical identifiers, idempotent append, conflicting duplicate rejection, generic text anonymization, compression round trips, and artifact-digest verification
- implement focused corpus models, model-agnostic text anonymization, content-addressed artifact storage, and Chatlas-backed ingress under `tarav.chatlas2`
- expose explicit `chatlas2 corpus ingest` preparation/registration actions plus read-only `list|verify`, all with an explicit `--corpus` root and exact session selector where applicable
- observable: a closed archived session becomes one path-free, content-pinned capture record plus reconstructable anonymized artifacts, and ordinary verification succeeds with the source archive unavailable
- check: focused unit and CLI tests; Ruff; no reverse dependency from current Chatlas
- risk: accidentally pinning only the current primary artifact; collect the selected row plus every archived transcript artifact using the same retention boundary as the Chatlas2 assembler
- risk: coupling anonymization to current provider structure; tests pass opaque text fixtures through the same anonymizer and prohibit provider/raw-version imports in that module
- risk: hiding judgment behind an automatic pipeline; ingress defaults to preparation only and requires an explicit registration action after operator inspection
- status: complete

### Slice 2 - Add the script model and ingress historical evidence

- add the consolidated `chatlas2-conformance.v1` human-readable script plus its machine-readable exact user messages, operator actions, features, and validity rules
- copy the four historical Markdown scripts into the active corpus and translate their canonical inputs and feature expectations into strict specifications
- ingress the 21 accepted historical captures through the implemented path; preserve recorded provider, source identity, and capture date in provenance while committing anonymized artifacts and corpus-safe identities
- document the complete interactive ingress loop in the corpus README and use that same loop for the historical batch rather than introducing a one-off importer
- observable: corpus listing reports five scripts, 21 accepted historical captures, 11 Claude captures, 10 Codex captures, and included artifacts covering every retained transcript source plus raw-version recognition for every supported Codex artifact
- check: historical source/session counts, identity hashes, script messages, source digests, anonymized digests, and archive round trips match; no active test reads either deprecated repository or the live Chatlas archive
- risk: treating the diagnostic Claude `knights-knaves` run as accepted; preserve its historical exclusion
- status: complete

### Slice 3 - Run conformance from the ingressed corpus

- add a corpus check that verifies the included archive and registry first, then dispatches recognized materialized captures through compatible Chatlas2 normalizers
- assert the exact ordered user-message invariant and the current minimal Normal Model promises; summarize passed, failed, and unsupported captures separately
- retain the existing synthetic same-session union/dedup tests and connect them in documentation as derived mechanical tests rather than independent semantic captures
- update `AGENTS.md`, `ARCHITECTURE.md`, and architecture tests if the public command or dependency map changes
- observable: all 21 captures verify hermetically from included artifacts; all 10 Codex captures pass the exact user-message conformance check; 11 Claude captures report unsupported normalization until a Claude versioner/normalizer exists
- check: focused Chatlas2 tests, relevant current-Chatlas archive/index regressions, Ruff, Skillware, installed CLI, and live corpus summary
- deviation trigger: stop if a historical accepted session cannot be resolved or its current identity disagrees with the recorded registry; do not silently omit it
- status: complete

## Impl.Log

- **2026-08-15 — execution gate:** interactive execution of Impl.Req 529 authorized ^c20260815-32u
- **2026-08-15 — executable audit:** all targeted Chatlas2 surfaces and checks exist; all 21 source sessions resolve to 21 unique retained transcript artifacts totaling 1,717,725 uncompressed bytes, so the included archive is practical without changing scope
- **2026-08-15 — design evidence:** located `User.Script.Invariant.Test` in both deprecated umbrella snapshots; directories are byte-identical and last changed together
- **2026-08-15 — corpus availability:** all 21 accepted sessions resolve in the current Chatlas index with exact recorded identities
- **2026-08-15 — current-model probe:** all 10 Codex sessions pass exact ordered canonical user messages through Chatlas2; this establishes a GREEN target that must first be reproduced as a RED corpus test
- **2026-08-15 — artifact policy:** the corpus will include best-effort anonymized provider artifacts in a content-addressed archive; anonymization is generic text processing and intentionally independent from provider schemas and raw-model recognition ^c20260815-30u
- **2026-08-15 — registration boundary:** anonymization and source/candidate preservation checks belong only to explicit artifact ingress; committed-corpus tests are hermetic and registration remains operator-reviewed rather than automatic ^c20260815-31u
- **2026-08-15 — checkpoint:** the mandatory pre-edit checkpoint was recorded at commit `a200515`; the corpus implementation remains uncommitted after that boundary
- **2026-08-15 — slice 1:** added strict script/capture contracts, a provider-independent opaque-text anonymizer, content-addressed deterministic-gzip storage, registry self-authentication, and separate `corpus ingest prepare|register` commands; focused RED/GREEN unit and CLI tests passed
- **2026-08-15 — slice 2:** preserved the four legacy scripts, added the consolidated v1 script and five strict specifications, prepared and reviewed all 21 historical captures, then explicitly registered 10 Codex and 11 Claude artifacts; the included anonymous corpus is 532 KiB compressed and emitted no anonymizer residual warnings
- **2026-08-15 — specimen preservation:** all 10 Codex artifacts remained `codex.rollout.v1`, preserved structural normalization topology after anonymization, and reproduced their exact canonical user messages; Claude artifacts were retained with null Raw.Model.Version pending a future Versioner/Normalizer
- **2026-08-15 — slice 3:** added hermetic `corpus verify|check`, local artifact reconstruction, recognition/dispatch, exact-message and event/reference invariants, installed CLI coverage, architecture guards, and the interactive operator runbook
- **2026-08-15 — verification:** corpus integrity reports 21 captures and 21 artifacts; conformance reports 10 passed, 11 explicitly unsupported, and 0 failed; Ruff passed; Skillware found no new code-surface POIs (only unrelated pre-existing edition-history advisories); the installed CLI was refreshed; the complete repository suite passed 1,921 tests
- no blockers
