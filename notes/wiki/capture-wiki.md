# Capture.Wiki

<!-- tarav.sessions
33afe59c = codex:01a07228-313a-7ab3-b6e0-aedcb5216b3c @33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd
-->

## Intent

`tarav-hugentics --capture --wiki` is a user-triggered, chat-centric,
session-bounded workflow for preserving what a discussion produced in the
Project.Wiki. The target is the wiki rather than a canonical Diagram Model, but
every substantive addition remains anchored to exact User Turns.
<!-- tarav.context 33afe59c:fd30b0cde0134ccf -->
<!-- tarav.context 33afe59c:83834a6547cd6815 -->

## Two capture views

Every capture updates `notes/wiki/daily/YYYY-MM-DD.md` with an Agent-maintained
narrative of the relevant things that happened. This is the mandatory minimal
capture; it does not attempt to record everything.
<!-- tarav.context 33afe59c:6416966b9f4a72b0 -->

The workflow also performs bounded navigation of the wiki and integrates the
discussion into topical Notes when useful. The daily view answers, “What
relevant things happened today?” while topical Notes answer, “What do we
currently understand about this subject?” The same supported material may
appear in both views.
<!-- tarav.context 33afe59c:19ffe7f63525f2c0 -->

Daily is the fallback because it guarantees retention when no topical home is
justified—not because it is optional. Capturing is mandatory; topical
organization is opportunistic. A `--target` selects a topical Note inside the
wiki without suppressing the daily narrative.
<!-- tarav.context 33afe59c:6416966b9f4a72b0 -->
<!-- tarav.context 33afe59c:83834a6547cd6815 -->

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

A successful capture ends with a recoverable Git checkpoint of the complete
current working state under `notes/wiki/`, even when that includes earlier
Note changes. A topical `--target` does not narrow Git closure. Changes outside
the Project.Wiki remain excluded.
<!-- tarav.context 33afe59c:f4fe73f3f878f979 -->
<!-- tarav.context 33afe59c:83834a6547cd6815 -->

The invocation authorizes this scoped commit; it is workflow closure rather
than a second approval gate. The Agent first validates references and inspects
the scoped diff. Empty commits are skipped, while blocking validation or Git
failures leave the surface uncommitted and become reported POIs.
<!-- tarav.context 33afe59c:883dd3820d585eaf -->
