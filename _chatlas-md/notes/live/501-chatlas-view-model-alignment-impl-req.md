# Chatlas View Model Alignment - impl-req

## Impl.Abstract

- **scope:** Align the Chatlas view system codebase with the `Chatlas.View.Model` index design — rename concepts, lift the single-session constraint, add `Driving.Prompt`, make dependencies declarative. Full refactor; no legacy slop.
- **status:** complete
- **source:** `Chatlas.View.Model` design session (`agentos-chatlas-md/notes/live/500-chatlas-view-model-design-session.md`), public index (`105-index.md`), appendix (`Chatlas.View.Model-appendix.md`), alignment report from design-to-code audit

## Impl.Index

### Naming.Alignment

- the design settled on specific names that the code must adopt
- `slot` → `depot` everywhere: `slot_path` → `depot_path`, `resolve_chatlas_view_slot_path` → `resolve_chatlas_view_depot_path`, `_VIEWS_ROOT` stays
- `kind` field values: `"internal"` → `"programmatic"`, `"external"` → `"agentic"`
- the `kind` field itself can stay — it carries `View.Class` semantics as a string tag
- apply globally — grep for old names, kill every occurrence, no aliases or compat shims

### Session.Set.Support

- the design says `Session.Set` is a normalized, deduplicated, sorted array of `identity_hash` strings
- the context dataclass already holds `parameters: list` and `source_rows: list` — the architecture supports N sessions
- the bottleneck is `_context_from_selector()` which calls `select_one_chatlas_index_row()`
- introduce `_context_from_session_set()` that accepts a list of index rows, normalizes them into a `Session.Set`, and builds context
- normalization: extract `identity_hash` from each row, deduplicate, sort lexicographically
- `_context_from_selector()` becomes a convenience that resolves one row and delegates to `_context_from_session_set()`
- add a multi-session CLI path: view commands should accept query results, not just single-session selectors
- existing single-session workflows remain valid — they operate on a `Session.Set` of size 1

### Driving.Prompt.Integration

- `Driving.Prompt` is an optional string, empty by default, part of `View.Identity`
- add `driving_prompt: str` to `ChatlasViewContext` (default `""`)
- include `driving_prompt` in cache key computation when non-empty — different prompts produce different views
- pass through to `build_produce_prompt()` and `prepare_agent_production()` for agentic views
- CLI: add `--prompt` flag to view commands that support agentic views
- programmatic views ignore it — it's present in identity but doesn't affect their production

### Dependency.Declaration

- current code hardcodes dependency checks inside each workflow's `current_status()` — e.g., `ZipTranscriptAgentSummaryWorkflow` manually resolves `zip-transcript` internally
- the design says dependencies should be declared and resolved on-demand through context
- add a `dependencies` declaration to the workflow protocol: a tuple of `(dependency_view_name, ...)` or similar
- the framework can then automate freshness propagation — if any declared dependency is stale, the view is stale
- workflows still resolve dependency data on demand through the context at runtime, but the dependency graph is inspectable
- keep the existing fingerprint-based freshness — just make the dependency wiring explicit instead of buried in each workflow

### View.Workflow.Protocol.Cleanup

- the current protocol has methods that only apply to one class: `produce()` is only for programmatic, `prepare_agent_production()` is only for agentic
- the design says both classes share a common surface (status, contract, name, dependencies) and differ only in production
- keep single protocol for now — the cost of dead methods is lower than the cost of a type hierarchy at this stage
- remove `production_instructions()` if unused or redundant with `build_produce_prompt()`

### Storage.Path.Structure

- rename filesystem paths to match: `{view-name}/{cache-key}/` is the depot (was "slot")
- staging at `_staging/{stage-id}/` is fine — matches design
- manifest structure stays — it already records dependencies and fingerprints

## Execution.Plan

### Slice 1 — Naming rename: slot → depot, internal → programmatic, external → agentic

- **changes:** rename `slot_path` → `depot_path` in `ChatlasViewContext`, rename `resolve_chatlas_view_slot_path` → `resolve_chatlas_view_depot_path`, rename all `slot` references in core.py. Change `kind` values from `"internal"`/`"external"` to `"programmatic"`/`"agentic"` in all three workflow classes. Update CLI output and command handlers in `commands.py`.
- **path:** `views/core.py` → `commands.py` → `views/__init__.py` → any importers
- **observable:** `agentos chatlas views list` shows `programmatic`/`agentic` kinds. `agentos chatlas views status --view chatlas-session --identity-hash <hash>` works. No `slot` string anywhere in the codebase.
- **check:** `grep -r "slot_path\|\"internal\"\|\"external\"" agentos-chatlas-py/src/` returns zero hits in view code. Existing view artifacts still resolve (depot path structure unchanged on disk).
- **status:** not started

### Slice 2 — Session.Set normalization and multi-session context

- **changes:** add `_normalize_session_set()` that extracts `identity_hash`, deduplicates, sorts. Add `_context_from_session_set()` that accepts `list[dict]` rows, normalizes, builds context. Refactor `_context_from_selector()` to delegate. Update `chatlas_run_produce()` to build context through the new path.
- **path:** `_context_from_selector()` → `_context_from_session_set()` → `_context_from_parameters()` → `ChatlasViewContext`
- **observable:** `_context_from_session_set([row_a, row_b])` produces same context regardless of input order. `_context_from_selector()` still works for single-session commands.
- **check:** unit test: two rows with same `identity_hash` deduplicate to one. Two rows in different order produce same `cache_key`. Existing single-session CLI commands unchanged.
- **status:** not started

### Slice 3 — Driving.Prompt in identity and context

- **changes:** add `driving_prompt: str = ""` to `ChatlasViewContext`. Include in `compute_chatlas_view_cache_key()` when non-empty. Thread through `_context_from_session_set()`. Add `--prompt` CLI flag to `stage`, `produce`, `run-produce` commands.
- **path:** `ChatlasViewContext` → `compute_chatlas_view_cache_key()` → `_context_from_session_set()` → CLI arg parsing → `build_produce_prompt()` / `prepare_agent_production()`
- **observable:** same view + same sessions + different prompt → different cache key → different depot. Empty prompt → same behavior as before.
- **check:** `agentos chatlas views status --view zip-transcript-agent-summary --identity-hash <hash> --prompt "custom"` resolves to a different depot than without `--prompt`. Prompt appears in stage manifest.
- **status:** not started

### Slice 4 — Explicit dependency declaration

- **changes:** add `dependencies: tuple[str, ...]` to the `ChatlasViewWorkflow` protocol (default `()`). Declare dependencies in each workflow: `SessionModelWorkflow.dependencies = ()`, `ZipTranscriptWorkflow.dependencies = ()`, `ZipTranscriptAgentSummaryWorkflow.dependencies = ("zip-transcript",)`. Extract common freshness-propagation logic into a framework helper that uses the declared list. Simplify `current_status()` in each workflow.
- **path:** protocol definition → workflow classes → `current_status()` → framework helper
- **observable:** `agentos chatlas views list` can show dependency graph. Freshness propagation works the same as before but driven by declaration.
- **check:** existing freshness behavior unchanged. Adding a new workflow with declared dependencies gets automatic staleness propagation.
- **status:** not started

### Slice 5 — Cleanup dead methods and legacy references

- **changes:** audit `production_instructions()` — if redundant with `build_produce_prompt()`, remove from protocol and implementations. Remove hardcoded absolute path `_ZIP_TRANSCRIPT_AGENT_SUMMARY_REFERENCE`. Clean any remaining `slot` references, old naming, or dead code discovered during slices 1-4. Grep the full `agentos-chatlas-py` tree for stale references.
- **path:** full codebase scan
- **observable:** no dead methods in protocol, no hardcoded paths, no stale naming
- **check:** `grep -r "slot\|_ZIP_TRANSCRIPT_AGENT_SUMMARY_REFERENCE\|production_instructions" agentos-chatlas-py/src/` returns only valid hits
- **status:** not started

## Impl.Log

- 2026-05-20: Impl.Req created from Chatlas.View.Model design session and codebase alignment audit. All gaps documented. Five vertical slices designed to incrementally align the codebase.
- 2026-05-20: All 5 slices implemented. Naming aligned (slot→depot, internal→programmatic, external→agentic). Session.Set normalization added. Driving.Prompt threaded through identity, context, CLI, manifests. Dependencies declared on protocol and used generically. Hardcoded absolute path replaced with runtime resolution. Zero legacy references remain. Smoke test passed.
