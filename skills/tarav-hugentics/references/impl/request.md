# Implementation Request

The live-note Impl.Req is the durable design-to-execution handoff and the
Agent's main coordination artifact. It stays outside the backend's own
surfaces.

## Location

Name new implementation-request live notes
`<number>-<descriptive-name>-impl-req.md` under the product's notes/live/.
Follow its numbering convention; preserve existing filenames on resume.
When one design changes several repositories, write one request per owning
repository, each in its own notes/live/, cross-referenced and executed in
dependency order; each repository keeps its own evidence commits.

## Contents

- Impl.Abstract: requested result, scope, explicit non-goals and status.
- Knowledge.Surface: the context backend, currently `wiki`.
- Design narrative: requested behavior, rationale, relevant current behavior,
  decisions, constraints, informative alternatives, and open questions, with
  supporting Breadcrumbs beside the passages they contextualize.
- The backend's own section, such as Impl.Req.Wiki.
- Execution.Plan: the core data shape and ordered vertical slices, each with
  its work kind, observable result, check, and status.
- Impl.Log: decisions, changes, checks, commits, blockers, and capture
  outcomes.

## Evidence

Do not invent evidence or turn an agent plan into user-approved design.
Record user decisions, implementation observations, and proposals distinctly.
Do not copy the whole plan into the backend.

The Impl.Req must be sufficiently self-contained for another agent in another
session to understand and implement the request. Backend links remain useful
for broader context and detail, but must not replace the explanation of what
is requested and why. Carry the necessary bounded narrative and evidence in
the note itself; neither copy the entire discussion nor require its
reconstruction.

During Design, attach exact supporting Chatlas User Turns as Breadcrumbs in
the live note, even when the same turns also support backend passages. Apply
the shared Inlined Capture workflow to that Markdown surface; the Impl.Req is
an authorized Design output, not an implementation edit. Log evidence gaps
rather than fabricate support. On later execution, preserve the original
sessions and turns; a new session's invocation does not replace design
evidence. Add later clarifications and observations distinctly.

