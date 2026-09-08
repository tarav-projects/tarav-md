# Capture.Note

<!-- tarav.sessions
33afe59c = codex:01a07228-313a-7ab3-b6e0-aedcb5216b3c @33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd
-->

## Intent

`tarav-hugentics --capture --note` is a user-triggered, chat-centric,
session-bounded workflow for preserving what a discussion produced in Markdown
Notes. The target is Notes rather than a canonical Diagram Model, but every
substantive addition remains anchored to exact User Turns.
<!-- tarav.context 33afe59c:864b0f87dd82fb92 -->

## Project.Wiki placement

The default surface is the selected project's `notes/wiki/`. The workflow
performs bounded navigation of existing filenames, headings, links, and nearby
material, then selects or creates a meaningful topical Note. A User may instead
select one explicit target Note.
<!-- tarav.context 33afe59c:2ede6ce59c12922c -->

`notes/wiki/daily/YYYY-MM-DD.md` is active only for an implicit Project.Wiki
capture. It is the primarily Agent-maintained fallback for material without a
justified topical home; an explicit target never also writes a daily entry.
Capturing is the first priority and organization is the second.
<!-- tarav.context 33afe59c:726a46194513e1d4 -->

## Additive history

Capture records what the discussion produced; it does not automatically
reconcile the wiki into one canonical position. Compatible material may be
integrated into an existing section. Brainstorming alternatives, candidate
histories, disagreements, and open tensions remain visible. Existing wording
is amended only when the discussion itself performs that amendment.
<!-- tarav.context 33afe59c:ca8c2be6ce06c080 -->

Any section may acquire an append-friendly edition suffix such as
`## <subject> - v001`. For each capture, the Agent decides whether a compatible
addition belongs in the current edition, semantic evolution deserves another
edition, or an independent branch deserves a different section. There are no
mandatory Session wrappers or generic `Candidates`/`Open tensions` subheadings.
<!-- tarav.context 33afe59c:02bfb6fd53fb2719 -->

## Git closure

A successful capture ends with a recoverable Git checkpoint. An implicit wiki
capture commits the complete current working state under `notes/wiki/`, even
when that includes earlier Note changes. An explicit target commits only that
Note. Neither route includes changes outside its declared surface.
<!-- tarav.context 33afe59c:f4fe73f3f878f979 -->

The invocation authorizes this scoped commit; it is workflow closure rather
than a second approval gate. The Agent first validates references and inspects
the scoped diff. Empty commits are skipped, while blocking validation or Git
failures leave the surface uncommitted and become reported POIs.
<!-- tarav.context 33afe59c:883dd3820d585eaf -->
