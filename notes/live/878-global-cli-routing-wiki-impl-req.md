# Global CLI routing Wiki capture

<!-- tarav.sessions
0d8af26c = codex:01a168fe-92d6-7410-a7f7-7c15cf921b95 @0d8af26c5b8dff7be764aac420b13df80bb530919d551881ae7d1afcc2400744
-->

## Impl.Abstract

Knowledge.Surface: wiki. Status: complete. Capture the accepted global CLI router
discussion and implementation outcome. The User authorized designing and
executing an implementation request. Run profiles, the SSH subsystem and vector
storage are deferred; routing can invoke SSH directly for now.
<!-- tarav.breadcrumb 19919df157b2 -->
<!-- tarav.breadcrumb a06ce4fb41ad -->

## Design

The router maps selected commands to external invocations with argument
passthrough and always announces the actual command, including SSH. Python
request [956](../../../tarav-py/notes/live/956-global-cli-command-router-impl-req.md)
owns code design and validation. This request owns only supporting Markdown.
<!-- tarav.breadcrumb 0f0ff3ca384d -->

## Impl.Req.Wiki

Owner/root: tarav-md/notes/wiki. Context read: live-help.md. Destinations:
cli-routing.md and daily/2026-10-23.md. Use the declared exact session once,
submit Breadcrumbs and audit; do not invent evidence or rewrite adjacent topics.

## Execution.Plan

- [x] Documentation: create a topical router note and append the mandatory daily
  narrative, distinguishing User choices from implementation decisions and
  measured results. Verify links, submit/audit changed notes, run Project checks
  and close a scoped Wiki evidence commit after Python verification.

## Impl.Log

- Start checkpoint retained in /tmp/cli-router-start-md-result.json. Worktree
  was clean. Python implementation precedes behavior capture.
- Start checkpoint 459cfa51. Read the supporting exact User Turns through
  Chatlas Query; reused one refresh and the declared session throughout.
- Created cli-routing.md and appended daily/2026-10-23.md with the bounded
  discussion. Five new Breadcrumbs in each Note were submitted and audited
  with zero POIs; request surface also audits clean. Implementation claims link
  to inspected Python code/tests and its live-note execution evidence.
- Python verification: 88 focused checks passed; real installed CLI routed a
  read-only printf call through SSH to the Studio, preserving argument values.
  Wiki diff whitespace check passed. Full Project status is running.
- Wiki request checkpoint 07ee644e and scoped Wiki capture commit 5bf22c01
  completed with zero commit-audit POIs. Python feature commit 1faaccad is also
  committed and audited. Both requests' surface audits resolve all attachments.
- Full root status --all completed all 1,350 checks, including 69 pytest file
  checks with zero test POIs. No skipped or incomplete suites. The 67 existing
  maintenance findings caused exit 1; no new or reopened action was produced.
  Detailed result is retained at /tmp/cli-router-root-status.json and in Python
  request 956's log. No unresolved implementation or Wiki capture gap remains.
