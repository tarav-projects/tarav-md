# Product Mapping guidance and discussion capture

<!-- tarav.sessions
ec6cf584 = codex:01a1563b-2992-7c62-8a38-05c1cc75b1fe @ec6cf5849bb6c4e66f011b015415da94eeb1a17634872aa4fb9e25d8e065ab53
-->

## Impl.Abstract

Knowledge.Surface: wiki. Alignment.Mode: Interactive. Status: completed.
Capture the Product Mapping discussion and implementation outcome. Product
Mapping maintains byte chunks at chosen Git commits; Product Review Tracker
will be a separate consumer. The current request implements mapping and a
historical tarav-py run at ten-commit intervals.
<!-- tarav.breadcrumb 49663466e305 -->

## Impl.Req.Wiki

Wiki owner: tarav-md/notes/wiki. Destinations: product-mapping.md and
daily/2026-10-22.md. Product request:
../../../tarav-py/notes/live/946-product-mapping-impl-req.md.
Preserve the distinction between user design, agent choices and test evidence.

## Execution.Plan

- [x] Capture stable chunk identity, committed byte states, maintainer decisions,
  selected checkpoints and freshness policy in the topical and daily Notes.
- [x] Submit and audit exact User-Turn Breadcrumbs; commit supported capture.

## Impl.Log

- New standalone workflow; no changes to existing Breadcrumb or review semantics.
- Start checkpoint: d74445e9. Product slices: 23141237, 13920481, 0bd9564c.
- Captured product-mapping.md and daily/2026-10-22.md. Exact User Turns support
  the workflow split, byte units, maintainer identity choices, selected checkpoints,
  freshness policy and implementation/historical-run authorization. Implementation
  facts cite the maintained guide, code, tests and historical JSON report.
- The fixed historical exercise completed and independently audited 127 maps
  over 1,257 commits; final historical state: 1,157 files, 4,584 chunks. Final
  implementation catch-up is retained in the workflow registry after the product
  completion commit; no tracked report is repeatedly rewritten to chase HEAD.
