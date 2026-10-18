# TaravRecords — candidate workflow design

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

## Records, Registry, and Archive

`TaravRecords` is the proposed workflow name. Its scope includes reusable primitives for storing Records and the basic functions for discovering and navigating stored Records. Tarav may provide standard locations, while individual workflows may use the same primitives in their own repositories.
<!-- tarav.breadcrumb e95282afbd3b -->
<!-- tarav.breadcrumb fefcdeb218ad -->

An Archive has Artifact identity, descriptive Records, long-term preservation, and DOI-like responsibilities. A Registry is concerned with storing Records; Archive may use a Registry for its Records. Registry storage policy may be append-only or may expose a changing current edition. The shared primitives should support both cases.
<!-- tarav.breadcrumb f996ce152a66 -->
<!-- tarav.breadcrumb 20844742cef8 -->

An Entity view can be projected over retained Records rather than requiring a second Entity repository. Across Tarav, storage solutions should hook into a discoverable graph through their own traversal mechanisms, which may use JSON registries, classes, or other structures. The graph need not register every Record separately in one central list.
<!-- tarav.breadcrumb ce2360b94b79 -->
<!-- tarav.breadcrumb 212c25487a6f -->

## Implementation boundary under discussion

[Impl.Req 864](../../../tarav-py/notes/live/864-tarav-records-workflow-impl-req.md) proposes starting with a source-contribution contract and navigation over existing unlike stores, then deciding separately whether and how the current Record Archive becomes a standard RecordRegistry. This is an Agent proposal awaiting alignment, not a User decision.

## First implementation — 2026-10-07

The User chose to establish the general workflow organization and extract common or easily migrated primitives first. Workflows may keep custom storage; further alignment is deferred. This resolves the first implementation boundary above without deciding a full Record Archive migration.
<!-- tarav.breadcrumb ec932b2789cb -->

In `tarav-py`, `tarav.l1.records` now names the `TaravRecords` workflow. Its service mounts workflow-owned `RecordProvider` sources into one navigable root and derives Entity occurrences by scanning contributed sources on demand. A standard `RecordRegistry` stores typed Records in Workflow Ship partitions with insert, replace, current working-file, committed-head, and exact-commit references. Archive and Scoring expose their existing layouts through the same navigation contract; Archive also uses the shared typed write and Git initialization primitives. The Record Archive layout and Artifact responsibilities have not been migrated. See [Impl.Req 864](../../../tarav-py/notes/live/864-tarav-records-workflow-impl-req.md) for the implementation log and checks.
<!-- tarav.breadcrumb 1355e25a5e59 -->
