# Attic semantics and agent operating guidance

Knowledge.Surface: wiki

<!-- tarav.sessions
7c51c146 = codex:01a15606-58f7-77a0-9600-8d0b0bf63a82 @7c51c146657d59fa35293ab3b44b6be3b0e38654e1dfd05d83fa752a7bd0f4c4
-->

## Impl.Abstract

Refresh the Attic skill module to describe opaque conservation, self-declared
manifests, the real Python workflow, and lightweight System Project checks.
Status: complete, verified and captured after the core of
[the Python request](../../../tarav-py/notes/live/932-attic-workflow-impl-req.md).
<!-- tarav.breadcrumb a1c755be87fa -->

## Design narrative

The Attic cheaply moves material out of active development while preserving it
for later investigation, value extraction, recovery, or deliberate removal.
It does not require Archive registration or interpretation before conservation.
<!-- tarav.breadcrumb 08e587797286 -->

The User explicitly makes contents opaque and manifests self-declared. Checks
validate format, not whether depositor claims are true. Preserve the existing
no-live-dependency, copy-out recovery, and explicit deletion authorization rules.
Refresh the obsolete Diagram application progression. Explain the Python
workflow and metadata-only checks, including that old formats produce findings
without blocking preservation or investigation. Do not add a migration, payload
inventory, automatic cleanup, or new Artifact-reference guarantees.
<!-- tarav.breadcrumb c1ff323334b3 -->

Current authority: `.tarav/skillware/skills/tarav-pkg/src/references/attic.skw.json`
compiles to `skills/tarav-pkg/references/attic.md`. Read its depot AGENTS.md;
edit the source and rebuild. Keep its existing linked legacy-skill-mine
reading declaration. Data shape: the documented version-1 manifest remains
the small JSON contract; arbitrary supplemental hints remain possible.

## Impl.Req.Wiki

Wiki owner/root: `tarav-md/notes/wiki/`. Relevant nearby notes:
`record-archive.md`, `projects.md`. Capture the requested semantics in `attic.md`
and append today's `daily/2026-10-19.md`. Supporting exact User Turns:
`7e5cab371f946325`, `952e05cea4612df7`; capture pending.

## Execution.Plan

1. **Feature — refreshed guidance.** Revise the authoritative Attic source and
   rebuild the skill. Document workflow discovery, self-declared metadata,
   agent deposit/recovery steps, and System maintenance without payload reads.
   Observable: agents can operate the implemented workflow from its skill.
   Verify SKW build/check and that generated text matches the implementation.
   Status: verified; build and check returned zero findings.
2. **Capture and closure.** Submit and audit inlined evidence on implemented
   documentation, capture supported discussion in daily and topical Wiki notes,
   and commit the declared scope. Status: captured and audited; Git closure follows.

No unresolved User decision is required. Extra hints stay optional, historical
manifests stay untouched, and the depot's physical AGENTS.md is not a new
source of schema truth. Product changes belong to the Python companion.

## Impl.Log

- Start checkpoint: `1d085d57b61b3d9100279e2c6d9ac1a9e9aeaeff`;
  pre-existing external deletion preserved with unknown-session evidence.
- User authorized creation and execution of both requests through Hugentics.
- Cold-reloaded the request and executed after the Python core passed its
  focused tests. Replaced the obsolete Diagram application progression with
  explicit optional recovery/registration, documented opaque payloads and
  self-declared format, and added the implemented workflow and System suite.
- SKW skill build and check both returned zero findings. Source text was
  captured through a temporary Markdown working projection, stored back in
  `.skw.json`, and rebuilt. The temporary projection was removed before final
  product-position refresh; generated-document Breadcrumb audit then passed.
- Installed skill location resolves to this maintained product; no separate
  deployment was needed. No deposit manifests or material were changed.
- Captured supported discussion into `notes/wiki/attic.md` and appended
  `notes/wiki/daily/2026-10-19.md`; the broader wiki was not reconciled.
- Inlined audits passed: five Breadcrumbs in the skill module, three in this
  request, six in the topical Wiki note, and twenty total in today's daily
  note (prior discussion preserved). Source text/product match after compilation.
- Python slice commit: `9f333d1b2db4601a720496a4360c5410b11dba5b`.
- No pending evidence or product gap remains in this documentation scope.
