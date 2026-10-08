# Search workflow

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

## Design

`SearchWorkflow` provides one front for search engines from different workflows. An engine is a `SearchEngine` capability with a bound `obj.search` namespace. It decides whether it accepts each typed `SearchQuery`; several engines may accept the same query. The workflow's registry records available engines by name, without assigning query types exclusively to one engine.
<!-- tarav.breadcrumb 738489efaf77187b617645c49d0546d5a333c674189621b636c6c3bfd4589203 -->
<!-- tarav.breadcrumb 5f5b0c8f47055841c4b7036886a05ca978fed70a41f67c8f30f7901beb1321f9 -->
<!-- tarav.breadcrumb 6d538062639a62e88f4555970841444ec8a58cc613c72a0872559bb2b450af45 -->

The incremental operation yields individual hits. A query can select engines and cap the total hit count; a cap of one returns on the first hit. Dispatch follows registration order and preserves each hit's engine provenance. `run()` collects the same stream. Declining a query differs from accepting it and finding no hits; an accepted engine failure remains visible. A query is a TaravObject, but searching does not imply storing it.
<!-- tarav.breadcrumb d32df61bdfc3a546805fdfd8b5fd9c46b8c0a5af197848b103e194f10aa6cee8 -->
<!-- tarav.breadcrumb a3fd350d0b0d36432bd12a336fb496805a343c7caee4cda9363d0403dedd56ee -->

## First implementation

`tarav.l1.search` defines `SearchQuery`, `SearchEngine`, `SearchStream`, `SearchHit`, `SearchResult`, and the registry-backed `SearchService`. The installed runtime owns one service per composition and registers `SearchWorkflow`. Domain-specific search adapters are separate work; [Impl.Req 871](../../../tarav-py/notes/live/871-incremental-search-workflow-impl-req.md) records checks and boundaries. See the [source](../../../tarav-py/src/tarav/l1/search/__init__.py) and [tests](../../../tarav-py/tests/search/test_search_workflow.py).
<!-- tarav.breadcrumb 0e31b3fb34f26cfb53bd505a7dfe19beaf7ad1ee80006ded20fc94e9de5eaf6a -->
