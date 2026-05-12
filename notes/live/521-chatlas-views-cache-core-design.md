# Chatlas Views Cache - core-design

## Motivation

Design `Chatlas.Views` as the conceptual model behind cached derived data products for Chatlas session data. The design should keep Chatlas deterministic while allowing both programmatic producers and external agent producers to create reusable derived artifacts.

## Items Index

- Chatlas.Views: in-progress cached derived data products with workflow-owned dependency and freshness semantics
- View.Internal.Workflow: in-progress programmatic view lifecycle handled inside Chatlas
- View.External.Workflow: in-progress externally produced view lifecycle coordinated by Chatlas

## Items

### Chatlas.Views

#### Design.Alignment.Core

`Chatlas.Views` are cached derived data products produced from Chatlas session content and/or other Chatlas views.

Each view declares dependencies with fingerprints. Freshness is computed by comparing the committed dependency fingerprints against current dependency fingerprints, recursively when a dependency is another view.

Freshness diagnostics should explain the dependency tree, not only return a flat status. When a view is stale, diagnostics should identify which dependency or nested dependency made the view stale.

Dependencies are declared by the producer workflow. At first, dependency declarations are static per view type and are resolved from the view query.

#### Design.Open.Space

- Define the exact diagnostic output shape for dependency trees.
- Decide whether dependency freshness should distinguish direct stale dependencies from transitive stale dependencies in the public status labels, or only in diagnostics.
- Decide the manifest schema fields for dependency declarations and observed dependency fingerprints.

#### Usage History

The first motivating view is `agents-summary-zip-transcripts`, an agent-produced summary artifact derived from a Chatlas session and likely from the deterministic `zip-transcript` view. This view should be reusable across future sessions and should report stale when its source session, upstream view, or producer policy changes.

## Notes

- `Chatlas.Views` is a cache registry with workflow hooks, not a general agent runtime.
- Programmatic producers may implement a deterministic internal `produce` hook.
- External or agent-produced views may implement their lifecycle hooks as production guidance: a prompt, skill reference, staging path, expected artifacts, and commit command.
- Consuming a view should not silently trigger external production. Missing or stale views should be reported clearly and may suggest a production command.

### View.Internal.Workflow

#### Design.Alignment.Core

`View.Internal.Workflow` is the workflow class for views that Chatlas can produce programmatically and deterministically from Chatlas-owned data and registered view dependencies.

Internal views do not use staging. When a user queries an internal view, Chatlas checks whether a committed cached view is present and fresh. If it is present and fresh, Chatlas returns a Query Result JSON with sufficient information for reaching the view. If the view is missing or stale, Chatlas may run the view's internal `produce` hook before returning the Query Result JSON, when that view is configured for automatic production. If automatic production is disabled, Chatlas returns a Query Result JSON that reports the missing or stale state.

#### Design.Open.Space

- Define the per-view configuration field for automatic internal production.
- Decide whether stale internal views are replaced in place, versioned, or archived when auto-produced again.

### View.External.Workflow

#### Design.Alignment.Core

`View.External.Workflow` is the workflow class for views whose artifact content is produced outside Chatlas, such as by an agent.

The shared public contract is still: a user asks for a view and receives a Query Result JSON. The difference is whether Chatlas can satisfy the request itself.

External views are not produced by Chatlas. When a user queries an external view and a fresh committed artifact exists, Chatlas returns a Query Result JSON with sufficient information for reaching the view. When the view is missing or stale, Chatlas returns a Query Result JSON that reports production is required and includes predefined production instructions.

The external producer then stages the view through Chatlas. Staging resolves the view query, checks the expected dependency and artifact contract, and returns a staging Query Result JSON. The external producer writes the required artifacts into the staging location and commits through Chatlas. Commit validates the staged artifacts, writes the committed manifest, moves the artifacts into canonical storage, and returns a committed Query Result JSON.

#### Design.Open.Space

- Define the exact status name for external views that require production.
- Define the fields in production-instruction JSON for agent-produced views.
- Decide whether stale external views require a new staging entry or may reuse an existing incomplete staging entry.

## End Log

- 2026-05-11: Created Core.Design artifact and captured initial `Chatlas.Views` alignment around derived data, dependencies, recursive freshness, diagnostics, and producer-declared dependency semantics.
- 2026-05-11: Added `View.Internal.Workflow` and `View.External.Workflow`, plus the Query Result JSON contract and clarified that `produce` is an internal lifecycle hook, not a public command.
