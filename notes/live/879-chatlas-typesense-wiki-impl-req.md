# Chatlas Typesense integration Wiki capture

<!-- tarav.sessions
0d8af26c = codex:01a168fe-92d6-7410-a7f7-7c15cf921b95 @0d8af26c5b8dff7be764aac420b13df80bb530919d551881ae7d1afcc2400744
-->

## Impl.Abstract

Knowledge.Surface: wiki. Status: captured; live POC pending. Develop / Autonomous. Capture the
accepted thin Typesense product integration, Studio-only engine deployment and
machine-neutral CLI. Search only the stored Normal Model files.
<!-- tarav.breadcrumb d060cb46f991 -->
<!-- tarav.breadcrumb 9037b18bee8d -->
<!-- tarav.breadcrumb 7f62af6c8e4b -->

## Design

The product owns embedding generation and retrieval. Tarav exports text,
available metadata and exact source references, and exposes status/sync/search.
The global router selects the Studio independently of the adapter. Implementation
and evidence: ../../../tarav-py/notes/live/957-chatlas-typesense-normal-model-search-impl-req.md.
<!-- tarav.breadcrumb 81893ba5cfb8 -->

## Impl.Req.Wiki

Owner/root: tarav-md/notes/wiki. Context: chatlas-normal-model.md and cli-routing.md.
Destinations: chatlas-typesense.md and daily/2026-10-23.md. Reuse the declared
session and exact User Turns, submit and audit each changed surface.

## Execution.Plan

- [x] Documentation: capture scope, ownership and observed implementation facts,
  distinguish deployment readiness from a live verified service; scoped evidence
  commit and Project checks. No whole-Wiki reconciliation.

## Impl.Log

- Markdown start checkpoint a26b3f91. Exact supporting User Turns resolved.
- Concurrent checkpoint d90be81 absorbed this request as external work; preserved.
  Capturing only Typesense discussion and measured implementation facts; live
  deployment remains explicitly pending the operator's Ansible check/apply.
- Added the required live Kernel.Writing POC to the topical Note: completion
  needs actual Typesense results, dates and exact source verification. Wiki
  Breadcrumb submissions/audits passed, including the later POC User Turn.
  The daily capture was conserved by the concurrent Program Wiki commit a936ba6.
  Isolated tests: 668 passed; current shared Typesense/routing/architecture
  verification: 94 passed. No live engine result is claimed yet.
- Wiki capture commit 862683d0 and its Breadcrumb audit passed, and the Markdown
  source was pushed to GitHub successfully. The actual operator apply and live
  Kernel.Writing test remain open in Python request 957, to be captured when
  measured. Daily capture was included in the prior concurrent Wiki commit.
