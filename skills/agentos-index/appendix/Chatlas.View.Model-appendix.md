# Chatlas.View.Model — Appendix

> Extends: `Chatlas.View.Model`, `View.Identity`, `Session.Set`, `View.Workflow`, `View.Class`

## Programmatic.View

- `Programmatic.View` is a view whose production is programmatic
- the framework produces it directly — no agent, no staging
- production is deterministic and cheap relative to the session data
- stale freshness triggers automatic re-production

## Agentic.View

- `Agentic.View` is a view whose production requires an external agent
- the framework prepares a production prompt and a `View.Stage`
- an agent produces the artifact; the framework validates and commits the result
- stale freshness signals that production is needed but does not auto-trigger

## View.Context

- `View.Context` is the resolved runtime state the framework provides to a workflow
- it binds a `View.Identity` to everything the workflow needs to operate
- contains: the workflow, the session data, the cache key, and the storage location
- the workflow does not resolve its own context — it receives it
- from the context, a workflow can call back into the framework — including resolving other views

## Context.Resolution

- `Context.Resolution` is the framework step that produces a `View.Context` from a `View.Identity`
- normalizes `Session.Set`, computes `Cache.Key`, resolves `View.Depot`, binds the workflow
- does not eagerly resolve dependencies — produces a lightweight context the workflow operates from
- dependency resolution is on-demand at runtime

## Cache.Key

- `Cache.Key` is a deterministic hash derived from `View.Identity`
- same identity always produces the same key
- computed, never assigned — a pure function of `View.Identity`

## View.Depot

- `View.Depot` is the storage location for a materialized view instance
- derived from `View.Name` and `Cache.Key`
- holds the current materialized version — not a history

## Driving.Prompt

- `Driving.Prompt` is an optional caller-provided prompt that customizes an `Agentic.View` production
- empty by default — most views don't use it
- when present, it is part of `View.Identity` — different prompts produce different views
- stored in the view manifest or artifact for traceability
- prompt discipline is the caller's responsibility — the framework does not normalize prompt text

## View.Freshness

- `View.Freshness` is whether a materialized view is up to date with its inputs
- states: `fresh`, `stale`, `missing`
- checked by comparing fingerprints — input hash at production time vs current inputs
- for `Programmatic.View`, stale triggers automatic re-production
- for `Agentic.View`, stale signals need but does not auto-trigger
- each workflow defines how it fingerprints its inputs

## View.Dependency

- `View.Dependency` is a view that a workflow requires as input to its own production
- a dependency is another view — it has its own `View.Identity`, `View.Depot`, and `View.Freshness`
- declared by the workflow, resolved on demand through `View.Context`
- freshness propagates — if a dependency is stale, the dependent view is stale
- dependency chains are acyclic

## Artifact.Contract

- `Artifact.Contract` is what a view declares it will produce
- names the primary artifact and any required artifacts
- declares the content type
- part of the workflow registration — does not change per invocation
- the framework validates production satisfies the contract before committing

## View.Stage

- `View.Stage` is a temporary working directory where an external agent writes its output
- created by the framework before agent production begins
- isolated from the depot — the agent cannot corrupt a previous materialization
- carries metadata: which view, which parameters, which artifact contract
- only applies to `Agentic.View`

## View.Commit

- `View.Commit` is the framework step that promotes a stage into the depot
- validates that the stage satisfies the `Artifact.Contract`
- records observed dependency fingerprints for `View.Freshness`
- atomically replaces the depot content
- only the framework commits — the agent writes to the stage, never to the depot directly
- for `Programmatic.View`, the framework writes to the depot directly — no staging needed
