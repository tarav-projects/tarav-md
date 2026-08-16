# Chatlas2 Delta Update — Impl.Req

## Impl.Abstract

- **Status:** implemented and verified
- **Scope:** make `tarav chatlas2 --update <command>` perform one reliable, incremental Provider.Home → Raw.Archive → Session.Index refresh before the selected Chatlas2 command, then let existing cache validation rebuild stale Normal Models transparently.
- **Source:** the user requested a Chatlas2-targeted redesign that reuses proven Chatlas update mechanics without inheriting the old read-side escalation complexity. ^d20260816-43u
- **Out of scope:** replacing Provider.Home adapters, changing Raw.Archive layout, redesigning Session.Index schema, porting Chatlas1 trust tiers, updating Chatlas1 read commands, adding an automatic background updater, or making Normal Model construction incremental.
- **Acceptance:** an unarchived supported session becomes queryable through one Chatlas2 command carrying `--update`; exact-session reads use exact-session scan scope; broad reads use only Chatlas2-supported providers; update failure prevents the requested command; ordinary commands remain read-only and cache-transparent.

## Impl.Index

### Design.Index.Block::Chatlas2.Update.Preflight

- [DF] `Chatlas2.Update.Preflight` is an explicit CLI boundary: update the retained source material once, then execute the requested command once.
- [DC] `--update` is a boolean top-level Chatlas2 option, used as `tarav chatlas2 --update ...`; it does not expose Chatlas1's direct/index/recent/full satisfaction ladder.
- [CT] The update mutates only Raw.Archive and Session.Index. It never writes a Normal Model directly; the canonical Chatlas2 provider remains responsible for cache freshness and reconstruction.
- [CT] The preflight fails closed: when update fails, the selected command does not run and stale output is not presented as freshly updated.
- [PR] Keep the update result off stdout so every existing JSON-producing command preserves its output contract; progress may use stderr.

### Design.Index.Block::Chatlas2.Update.Scope

- [DF] Update scope is derived only from structural CLI selectors, never message text or other content predicates.
- [DC] A native `--session-id` produces one exact-session delta scan over the explicitly selected provider or the two Chatlas2-supported providers.
- [DC] A known `--identity-hash` resolves through Session.Index to the native session and provider before scanning; an unknown identity falls back to the supported provider scope so newly discoverable material is not excluded by stale metadata.
- [DC] A command without an exact selector performs one cached delta scan over its selected provider set, defaulting to Codex and Claude Code.
- [RJ] Do not retry progressively until a non-empty read appears. Empty is a valid result and update policy must not depend on consumer result shape.

### Design.Index.Block::Reuse.Boundary

- [CT] Reuse the existing Provider.Home adapters, archive copier, derivation signatures, scoped scanner, and Session.Index writer behind `chatlas_update()`.
- [CT] Reimplement Chatlas2's orchestration in the Chatlas2 namespace rather than importing the Chatlas1 CLI helper, whose tier ladder and satisfaction predicates are coupled to Chatlas1 commands.
- [CT] Preserve the dependency direction: Chatlas2 may depend on Chatlas mechanics; Chatlas must not depend on Chatlas2.
- [FR] This slice can later replace shared archive mechanics behind the same Chatlas2 preflight without changing consumer command semantics.

## Impl.Agendix

### Touched.Support

- User execution and product-shape authority: ^d20260816-43u
- `Raw.Archive`, `Chatlas.Session.Index`, `Chatlas.Update.Pipeline`, `Scan.Scope`, and `Provider.Home.Adapter` in `skills/tarav-chatlas-pkg/design/100-design.md`.

### Structural.Dependencies

- `tarav.chatlas.core.chatlas_update` — current reusable archive/index update composition.
- `tarav.chatlas.delta_scan` — scoped discover → compare → archive → index mechanics.
- `tarav.chatlas2.normal_model` and `tarav.chatlas2.cache` — existing transparent stale-cache reconstruction after retained artifacts change.
- `tarav.chatlas2.commands` — CLI composition point that can bracket every leaf handler once.

## Execution.Plan

### Vertical.Slice.1 — Chatlas2 update request and scope

- **Status:** completed
- Add one focused Chatlas2 update module with an immutable request/scope and one-pass execution over `chatlas_update()`.
- RED: tests prove exact session scope, provider-bounded broad scope, known identity resolution, unknown identity fallback, and single invocation.
- GREEN: implement only the structural scope derivation and reusable update call.
- **Check:** `uv run pytest tests/chatlas2/test_update.py -q`.
- **Deviation trigger:** existing shared update mechanics cannot ingest a fresh Codex or Claude artifact without invoking old Normal Model materialization as result authority.

### Vertical.Slice.2 — Top-level CLI preflight

- **Status:** completed
- Add `--update` to `tarav chatlas2`, route every leaf through one Chatlas2 dispatcher, and preserve leaf behavior when the option is absent.
- RED: a CLI boundary test proves update occurs before the selected handler, update failure prevents the handler, and JSON stdout contains only the selected command result.
- GREEN: replace leaf ownership of the root handler with a leaf-operation slot consumed by the dispatcher.
- **Check:** focused Chatlas2 update and CLI tests.
- **Deviation trigger:** argparse cannot preserve the existing command grammar without command-specific wrappers or root-CLI coupling.

### Vertical.Slice.3 — Freshness acceptance and maintained guidance

- **Status:** completed
- Add an isolated provider-home E2E proving a bare Chatlas2 read misses an unarchived session and the same read with top-level `--update` ingests, indexes, normalizes, and returns it.
- Update `tarav-py/AGENTS.md` and `ARCHITECTURE.md` with the actual Chatlas2 update/cache boundary.
- Run focused tests, all Chatlas2 tests, architecture tests, and Ruff on changed Python files.
- Validate the installed editable CLI help and one live exact-session update/read.
- **Check:** implementation-driving suite plus Chatlas2 and architecture regression suites.
- **Deviation trigger:** cache fingerprints do not recognize the archive mutation produced by the shared delta scanner.

## Impl.Log

- 2026-08-16 — Autonomous design selected a one-pass preflight instead of copying Chatlas1's result-driven escalation ladder. Empty query results remain semantically valid, so update completeness cannot be inferred from read cardinality. ^d20260816-43u
- 2026-08-16 — Execution completed without design deviations. The isolated freshness acceptance proved bare-read absence followed by one-pass archive, index, cache reconstruction, and Chat.Message return; 106 Chatlas2 and architecture tests passed, focused Ruff passed, and the installed CLI completed a live exact-session update/read.
