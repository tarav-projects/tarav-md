# Program runtime design capture

<!-- tarav.sessions
ec6cf584 = codex:01a1563b-2992-7c62-8a38-05c1cc75b1fe @ec6cf5849bb6c4e66f011b015415da94eeb1a17634872aa4fb9e25d8e065ab53
-->

## Impl.Abstract

Knowledge.Surface: wiki. Status: complete. Capture the agreed Program design and
its measured implementation. Programs are trusted Project classes. A State
produces checks reused by the StateAction that reaches it; fresh arrival tokens
contextualize maintenance checks and allowed progress. The base class owns
storage and execution; concrete Python defines States/Actions/connections.
<!-- tarav.breadcrumb 1e6f93b5221b -->
<!-- tarav.breadcrumb 8537deb41cfe -->
<!-- tarav.breadcrumb 8fa50724a9ff -->

The User requests request-and-execute. Project Monitor redesign is deferred.
<!-- tarav.breadcrumb 2135f2423acc -->

## Impl.Req.Wiki

Product request: ../../../tarav-py/notes/live/955-project-program-runtime-impl-req.md.
Wiki destinations: notes/wiki/programs.md and daily/2026-10-23.md. Preserve older
design as history and distinguish execution observations from User decisions.

## Execution.Plan

- [x] Append supported design and implementation references to the Wiki.
- [x] Submit/audit Notes and close scoped evidence commit.

## Impl.Log

- Read Project guidance and existing programs.md. Product and Wiki keep their
  independent Git histories; no legacy Iterante material is changed.
- Captured the accepted refinement in programs.md and the new daily/2026-10-23.md.
  Preserved earlier dated proposals. Both Notes carry User-Turn Breadcrumbs;
  submission and refreshed-position audits passed. Product request 955 and the
  operating guide describe measured mechanics separately from User decisions.
