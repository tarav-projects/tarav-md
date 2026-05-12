# Chatlas Views Cache - design-summary

## Summary

Design Chatlas `views` as a generic derived-artifact cache and registry. Chatlas owns storage, staging, commit, lookup, and freshness reporting, while each view type implements its own workflow hooks and freshness semantics.

## Accepted Decisions

1. Store derived artifacts under Chatlas-owned `views/` storage, not project-local `notes/live/`, so cached view artifacts can be reused across projects and future sessions.
2. Use the committed storage shape `~/Documents/chatlas/views/<view-name>/<cache-key>/manifest.json` plus view-owned artifact files, starting with `artifact.md` for markdown outputs.
3. Name the agent-produced compressed transcript view `agents-summary-zip-transcripts` to distinguish it from Chatlas' deterministic `zip-transcript` export view.
4. Treat each view as a full workflow with standard hooks; generic `chatlas views` commands must not hardcode per-view behavior except through workflow registration.
5. Let views share primitives such as session resolution, manifest I/O, staging directory creation, artifact hashing, and atomic commit, while keeping view-specific source, cache-key, artifact, and freshness logic inside the view workflow.
6. Use a staging flow: `views stage` creates a view-specific work folder and draft metadata; producers write artifacts there; `views commit` validates and moves the result into the canonical cache path.
7. Freshness is view-owned. For `agents-summary-zip-transcripts`, freshness should include at least the source session/content fingerprint plus producer workflow or compression-policy version, not only a generic session hash.
8. Keep Chatlas deterministic at first. Chatlas provides the cache and lifecycle interface; external agents or tools produce the artifact contents and then register them through the views surface.

## Execution Plan

1. Add a Chatlas views module with generic storage primitives for view roots, staging roots, manifest read/write, artifact metadata, and committed entry lookup.
2. Define a static workflow registry such as `CHATLAS_VIEW_WORKFLOWS = {"agents-summary-zip-transcripts": ...}`.
3. Define the workflow interface: resolve source, compute current fingerprint, compute cache key, create draft manifest, validate artifacts, compute freshness, build committed manifest, and project list/status rows.
4. Implement the `agents-summary-zip-transcripts` workflow as the first view type, using Chatlas session resolution and the current `zip-transcript` export content as its source dependency.
5. Add CLI commands under `agentos chatlas views`: `list`, `status`, `stage`, `commit`, `path`, and `get`.
6. Update `agentos-session-zip-transcript` so it stages through `agentos chatlas views`, writes the artifact into the staging folder, commits it, and returns the committed manifest.
7. Add tests for missing/fresh/stale/invalid/orphaned states, stage/commit behavior, collision prevention, and view-specific workflow dispatch.

## Deferred Items

- Automatic `ensure` generation is deferred because it would imply Chatlas invoking an LLM agent; keep production outside deterministic Chatlas commands for now.
- Dynamic third-party view plugins are deferred; start with a static in-repo registry.
- Caching deterministic Chatlas export views such as `zip-transcript` itself is deferred; the first target is the agent-produced `agents-summary-zip-transcripts` view.
- Cross-machine synchronization policy for cached derived views is deferred.

## Relevant Files Or Surfaces

- `agentos-py/src/agentos/chatlas/`
- `agentos-py/tests/test_chatlas_commands.py`
- `agentos-md/skills/agentos-session-zip-transcript/SKILL.md`
- `agentos-md/skills/agentos-session-zip-transcript/references/subagent-workflow.md`
- Chatlas dataset root: `~/Documents/chatlas`

## Open Questions

- What exact schema version fields should view workflows use for producer/compression policy versions?
- Should committed view manifests store artifact paths as dataset-relative paths only, or include absolute paths for convenience?
- Should `views commit` support `--replace`, or should stale replacement require an explicit delete or archive step?

## End Log

- 2026-05-11: Created summary from converged design discussion on Chatlas-owned view caching and per-view workflow hooks.
