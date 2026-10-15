# Wiki Context Backend

This backend contextualizes implementation requests through the Project.Wiki:
it supplies context to the phases and receives their supported capture. No
Model, Collection, Diagram View, Diagram Draft, authorization Gate, or Model
capture reconciliation is required or created by this backend.

## Reading context

Resolve the product project and its instructions. Resolve documentation
ownership separately when project guidance assigns the Wiki elsewhere.
Use Project.from_path(path).docs.wiki from tarav.l2.project, or an explicitly
selected folder Wiki. For a minimal TaravProject, use
ProjectWiki(project).open() from tarav.l2.project.wiki.
Read relevant Wiki notes and follow evidence links as needed; do not read or
reconcile the entire Wiki. An absent Wiki is not a reason to bootstrap Models.
For read-only review, report missing context without creating anything.

## Request section

Record `Knowledge.Surface: wiki` and an Impl.Req.Wiki section in the live
note: product project, Wiki owner/root, relevant note paths, available
supporting chat references, and capture status.

## Capture and closure

For mutating phases, compose [`../../wiki-capture.md`](../../wiki-capture.md)
for one bounded capture pass at handoff/completion; intermediate agent
coordination stays in the live note. The implementation invocation authorizes
this scoped pass. Reuse its Project.Wiki selection, mandatory daily narrative,
useful topical integration, Chatlas User-Turn grounding, Breadcrumb
submission/audit, and scoped Wiki Git closure. The product and Wiki evidence
commits keep separate declared file scopes.

Capture relevant user decisions and discussion selectively. Implementation
facts must also cite inspected code or test evidence; user authorization is
not proof that code works. Keep unsupported agent interpretation and raw
execution logs in the live note. Preserve alternatives rather than force a
canonical design. Do not regenerate existing Wiki content merely to make it
match the plan.

If Chatlas, Breadcrumb, or Wiki closure mechanics are unavailable, preserve
verified product work and log the precise capture gap for recovery. Do not
fabricate support or claim capture completed. Missing Model artifacts are not
a gap for this backend. Review never runs this mutating capture procedure.
When the gap is Breadcrumb registration, the read-only trace left by Inlined
Capture is the recoverable form of that gap.

The completion report names the Wiki daily and topical destinations and the
scoped Wiki capture commit, if any.

