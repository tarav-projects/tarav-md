# Search workflow

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

## Design

`SearchWorkflow` provides one front for search engines from different workflows. An engine is a `SearchEngine` capability with a bound `obj.search` namespace. It decides whether it accepts each typed `SearchQuery`; several engines may accept the same query. The workflow's registry records available engines by name, without assigning query types exclusively to one engine.
<!-- tarav.breadcrumb 738489efaf77 -->
<!-- tarav.breadcrumb 5f5b0c8f4705 -->
<!-- tarav.breadcrumb 6d538062639a -->

The incremental operation yields individual hits. A query can select engines and cap the total hit count; a cap of one returns on the first hit. Dispatch follows registration order and preserves each hit's engine provenance. `run()` collects the same stream. Declining a query differs from accepting it and finding no hits; an accepted engine failure remains visible. A query is a TaravObject, but searching does not imply storing it.
<!-- tarav.breadcrumb d32df61bdfc3 -->
<!-- tarav.breadcrumb a3fd350d0b0d -->

## First implementation

`tarav.l1.search` defines `SearchQuery`, `SearchEngine`, `SearchStream`, `SearchHit`, `SearchResult`, and the registry-backed `SearchService`. The installed runtime owns one service per composition and registers `SearchWorkflow`. Domain-specific search adapters are separate work; [Impl.Req 871](../../../tarav-py/notes/live/871-incremental-search-workflow-impl-req.md) records checks and boundaries. See the [source](../../../tarav-py/src/tarav/l1/search/__init__.py) and [tests](../../../tarav-py/tests/search/test_search_workflow.py).
<!-- tarav.breadcrumb 0e31b3fb34f2 -->
