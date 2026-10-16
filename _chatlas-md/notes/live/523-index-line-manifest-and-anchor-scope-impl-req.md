# Index.Line.Manifest And Anchor Scope — Impl.Req

> Historical implementation record. The current line-manifest implementation is Index-owned and exposed through the canonical `agentos index` namespace; use the maintained Chatlas command reference for current syntax.

## Impl.Abstract

- Status: implemented and independently verified.
- Scope: add a volatile, derived `Index.Line.Manifest`; make Chatlas resolve many
  line dossiers and their relationship turns in one process; add general
  anchor-scoped Index linter selection and stable line-subject metadata; update
  maintained CLI/skill guidance.
- Authority boundary: Index Markdown and Chat surfaces remain authoritative.
  `<chatlas-root>/workspace/` is an ignored `Volatile.Surface`; a manifest is an
  inspectable observation and never a new support, gate, or provenance relationship.
- Out of scope: durable audit history, manifest-to-manifest diffing, automatic
  semantic relevance judgment, migration of non-line Anchory records, and changes
  to Index content.

## Impl.Index

### Current.State

- `agentos index linter` can scope by file path but cannot select lines by
  `Anchory.Anchor`. Chatlas-powered checks therefore resolve the whole configured
  depot even when the caller needs a few lines.
- Linter POIs expose a target location, while anchor identity appears only in
  check-specific evidence when a producer happened to add it. There is no stable
  location-to-`Index.Line` subject registry in the structured result.
- `agentos chatlas anchory resolve` resolves one anchor per process. Repeated calls
  repeatedly initialize depot/session resolution and make a batch audit an N+1
  shell workflow.
- Chatlas has no line-centered derived artifact that presents the observed Index
  line, dossier namespaces, resolved relationship turns, and attachment standing
  together.
- `<chatlas-root>/.gitignore` does not yet declare `/workspace/`.

### Benchmark.Baseline

- A Luna agent repeated the `c20260809-171u`…`182u` audit with 27 Agentos CLI
  invocations in approximately 48.6 seconds.
- The full linter took 16.8 seconds; the ostensibly focused approval/verbatim run
  took 25.7 seconds because `--scope` still executes Chatlas checks over the whole
  depot.
- Twelve generic resolutions took 2.1 seconds and twelve detailed Chatlas
  resolutions took 3.7 seconds, excluding the human/agent joining work.

### Selection.Model

- Anchor selection is a general projection of the parser-backed Index floor, not
  an audit-specific mode.
- A repeated `--anchor` selector normalizes optional leading `^`, selects every
  `KernelLine` carrying any requested anchor, and fails closed when a requested
  anchor is absent from the configured floor.
- `LinterState.parsed_kernel_lines()` applies the selector, so core and injected
  checks using the public parser feed avoid unrelated line work. Structural checks
  may still inspect the complete floor.
- Structured linter output publishes an `Index.Line` subject registry keyed by
  path and line, with all anchors on each subject. POI targets join to it through
  their existing path/line coordinates; findings are not duplicated.

### Index.Line.Manifest

- Schema: `chatlas.index-line-manifest.v1`.
- One schema handles one or many selected lines. A line entry contains its observed
  source coordinate, exact statement/type/body, source fingerprint, and one entry
  per attached anchor.
- Each anchor entry contains the dossier schema, record fingerprint, attachment
  assertion and computed standing, and the selected relationship namespaces.
- Relationship namespaces remain independent: support members, semantic/tokenized
  gates, and provenance references are never flattened.
- Resolved turns live once in a top-level registry keyed by
  `<session>:<turn-id>`; line relationships point to those keys. This avoids copying
  the same turn for every supported line while terminal rendering may expand it.
- Detail levels are `reference`, `turn`, and `context`; context takes a caller-set
  radius. Relationship namespaces are caller-selectable. Stable ordering and an
  optional line limit make batch output bounded and reproducible.
- Building always validates complete `Normal.Turn.Ref` assertions. Support members
  additionally retain `User.Turn.Purity`; gate turns may be user or assistant turns.
- `show` prints the derived manifest as text or JSON without writing it.
  `materialize` writes JSON under
  `<chatlas-root>/workspace/index-line-manifests/` and prints the resulting path.
- Materialization ensures `/workspace/` is ignored. The generated file declares
  itself volatile and carries input fingerprints so consumers can detect stale
  observations.

### Batch.Resolution

- One batch assembler shares an `AnchoryDepot`, session-index cache, loaded session
  models, and turn indexes across every selected line and relationship.
- The existing single-anchor API remains a focused projection; the new line
  manifest is the general batch inspection surface rather than a shell loop over
  single-anchor commands.

### Output.And.Errors

- Missing anchors, invalid dossiers, failed turn assertions, and unsafe/out-of-depot
  scopes fail closed.
- Limits never silently alter relationship meaning. A line limit records requested,
  emitted, and omitted counts in the manifest summary.
- Terminal JSON and materialized JSON are projections of the same assembled model.

## Execution.Plan

1. **Parser-backed anchor selection and linter subjects**
   - RED: tests prove repeated `--anchor` is unavailable, unrelated line checks run,
     and structured output lacks a joinable subject registry.
   - GREEN: add the shared line-anchor helpers, linter config/CLI selector,
     fail-closed matching, selected parser feed, subject registry, and tests.
   - Check: focused `agentos-py` linter tests, Ruff, then package tests.

2. **Batch manifest assembler**
   - RED: tests specify one/many-line selection, relationship separation, turn
     deduplication, purity, attachment standing, detail/radius behavior, limits,
     and invalid input failures.
   - GREEN: implement the line manifest model using parser-backed Index lines and
     shared Chatlas/Anchory/session caches.
   - Check: focused unit tests and a real 12-anchor JSON build.

3. **Terminal and volatile workspace surfaces**
   - RED: e2e tests specify `show` text/JSON, `materialize` path output, deterministic
     manifest content, and `/workspace/` ignore behavior.
   - GREEN: register CLI surfaces, render text, materialize atomically, and update
     the operator Chatlas `.gitignore`.
   - Check: CLI e2e/output tests and `git check-ignore` on the real workspace path.

4. **Maintained guidance**
   - Update affected AGENTS files, Chatlas command reference/Skillware source, and
     Hugentics check/link guidance. Rebuild generated Skillware targets; retain
     unrelated stale-derived advisories.
   - Check: Skillware build/check and targeted documentation searches.

5. **System verification and benchmark**
   - Run focused and full tests for affected packages, Ruff, compile/diff checks,
     Anchory structural check, and the real anchor-scoped linter.
   - Have a fresh Luna subagent repeat the same semantic audit using the new linter
     selector and manifest; record invocation count, wall time, correctness, and
     comparison with the 48.6-second baseline.

## Acceptance.Signals

- One command produces a complete JSON manifest for the twelve benchmark anchors,
  with one copy of each resolved turn and all relationship namespaces preserved.
- Materialization lands only under ignored `<chatlas-root>/workspace/` and prints a
  readable path.
- Anchor-scoped linter checks return only selected-line standing and are materially
  faster than the previous whole-depot runs.
- Missing requested anchors fail closed.
- The Luna post-run reaches the same correctness judgment with fewer invocations and
  records measured elapsed time.
- Existing full test suites pass; unrelated pre-existing linter/Skillware debt is
  reported separately.

## Impl.Log

- Autonomous develop invocation authorized design and execution.
- Baseline Luna audit: 27 Agentos invocations, approximately 48.6 seconds; all twelve
  benchmark anchors were correct, and the measured friction matched the design above.
- Implemented repeated `--anchor` linter selection with fail-closed matching,
  parser-feed projection, stable `Index.Line` subjects, and explicit reporting of
  depot-wide checks omitted from line scope. The same focused audit dropped from
  26.9 seconds before the depot-check projection to 0.95 seconds after it.
- Implemented the then-current Chatlas-owned line-manifest surface. The real twelve-line
  manifest completed in 0.47 seconds at reference detail and 0.59 seconds at turn
  detail/materialization, resolving one session once, 23 support relationship uses,
  12 token gates, and 12 unique turns.
- Materialized verification artifact:
  `/Users/pereiro/Documents/chatlas/workspace/index-line-manifests/20260810T002225331459Z-cf95dba38a3c.json`.
  `git check-ignore` confirms `/workspace/`; the artifact is not a stable surface.
- Verification: 931 `agentos-py` tests and 476 `agentos-chatlas-py` tests passed;
  changed Chatlas files and changed Index-linter files pass Ruff; Chatlas Anchory
  structural check passes. Whole-package `agentos-py` Ruff retains four unrelated
  findings in concurrent tournament/workspace work. Existing Skillware stale-derived
  advisories were deliberately retained.
- Independent Luna post-run: two CLI invocations completed in 1.242 seconds
  (0.893-second linter plus 0.349-second manifest), a 92.6% command reduction and
  approximately 39.1x speedup / 97.4% elapsed-time reduction from the 27-command,
  48.6-second baseline. It independently confirmed 12 exact subjects, 12 matched
  attachments, 23 pure `User.Turn` support memberships, 12 token gates, 12 unique
  deduplicated turns in one session, and no unrelated depot warnings.

## Impl.Agendix

- User direction: `chatlas/workspace/` is explicitly non-Git-tracked and the
  manifest is a `Volatile.Surface`.
- User direction: integrate the manifest with general anchor-scoped linter work and
  removal of N+1 resolution, without overfitting to one audit style.
- User direction: use Luna subagents before and after implementation to measure the
  benchmark audit's correctness and elapsed time.
