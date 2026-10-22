# Project Attic guidance

<!-- tarav.sessions
96bd11c6 = codex:01a16464-7389-73a0-bebe-0189d9c953c3 @96bd11c6715ef7012dd7ebf6f826d3e465aae80853b9ba89380eb6614772f9f3
-->

## Impl.Abstract

Document Project-local Attics, their `_ATTIC` default, configurable location and
Project check integration. Preserve the same opaque conservation semantics as
the general Attic. Status: complete.
<!-- tarav.breadcrumb 6bff37869ee9 -->

Knowledge.Surface: wiki. Alignment.Mode: Interactive.

## Design

The User wants Projects to declare their own Attic folder for convenience.
Default to `_ATTIC`, allow a Project workflow configuration override, and run
Attic metadata checks with Project checks. Retired Projects in that folder are
historical contents, not active children. General and local Attics conserve
material under the same deposit convention.
<!-- tarav.breadcrumb 0dca3dfa0634 -->
<!-- tarav.breadcrumb b1e57fd0f879 -->

Implementation contract and adoption plan are in Python request
[944](../../../tarav-py/notes/live/944-project-attic-impl-req.md).
Use authoritative SKW sources for package guidance; rebuild generated products.
Do not change the Constitution or repair unrelated old deposits.

## Impl.Req.Wiki

Wiki: `notes/wiki/attic.md`, `notes/wiki/daily/2026-10-22.md`.
Exact supporting User Turns are declared above. Capture pending.

## Execution.Plan

1. Documentation feature: extend Attic operator guidance with Project discovery,
   configuration, checks and local deposit examples after Python behavior passes.
   Produce/compile source, then check the skill and resulting guidance.
2. Capture: add bounded topical and daily Wiki passages; submit and audit all
   changed surfaces and commit scoped changes. Verify links and Breadcrumbs.

## Impl.Log

- Start checkpoint: `b35d0ab`; Python and root checkpoints recorded in request 944.
- No unresolved user decisions. Python behavior is a dependency of documentation.
- Documented default selection, config, checks, status ownership and the shared
  deposit convention in the authoritative Attic SKW source; skill build passes.
  Generated operator guidance was rebuilt. JSON source uses an external
  Breadcrumb, so registration did not write into its content.
- Topical capture: `notes/wiki/attic.md`, Project-local Attics.
  Daily capture: `notes/wiki/daily/2026-10-22.md`, Project-local Attics.
  Both submitted and audited with zero findings across the bounded capture pass.
- Python request 944 records 103 passing focused tests, editable installation,
  live local metadata verification, and the intact local Attic adoption.
- Documentation/capture slice committed as `ee565ae`; commit evidence audit
  passes. Final skill checks pass; all 19 implemented/capture surfaces pass
  Breadcrumb audits. Completion updates record the broad-check outcome.
- Root full verification completed 1,343 checks with zero Attic findings. One
  Git-hook test failed in that full run and passed on focused rerun with all
  feature tests (12 passed). Existing broad Project findings remain explicit
  in Python request 944; the full run is not represented as green.
