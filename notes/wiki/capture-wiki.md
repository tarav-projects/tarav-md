# Capture.Wiki

<!-- tarav.sessions
33afe59c = codex:01a07228-313a-7ab3-b6e0-aedcb5216b3c @33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd
-->

## Intent

`tarav-hugentics --capture --wiki` is a user-triggered, chat-centric,
session-bounded workflow for preserving what a discussion produced in the
Project.Wiki. The target is the wiki rather than a canonical Diagram Model, but
every substantive addition remains anchored to exact User Turns.
<!-- tarav.breadcrumb e1d96de799c4 -->
<!-- tarav.breadcrumb 66bf6fbd981b -->

## Two capture views

Every capture updates `notes/wiki/daily/YYYY-MM-DD.md` with an Agent-maintained
narrative of the relevant things that happened. This is the mandatory minimal
capture; it does not attempt to record everything.
<!-- tarav.breadcrumb 72eb2c0af12b -->

The workflow also performs bounded navigation of the wiki and integrates the
discussion into topical Notes when useful. The daily view answers, “What
relevant things happened today?” while topical Notes answer, “What do we
currently understand about this subject?” The same supported material may
appear in both views.
<!-- tarav.breadcrumb fa6c6db0ab88 -->

Daily is the fallback because it guarantees retention when no topical home is
justified—not because it is optional. Capturing is mandatory; topical
organization is opportunistic. A `--target` selects a topical Note inside the
wiki without suppressing the daily narrative.
<!-- tarav.breadcrumb 4bf6a9b7a7aa -->
<!-- tarav.breadcrumb ba298c791e8d -->

## Additive history

Capture records what the discussion produced; it does not automatically
reconcile the wiki into one canonical position. Compatible material may be
integrated into an existing section. Brainstorming alternatives, candidate
histories, disagreements, and open tensions remain visible. Existing wording
is amended only when the discussion itself performs that amendment.
<!-- tarav.breadcrumb 4b5a1b625bf1 -->

Any section may acquire an append-friendly edition suffix such as
`## <subject> - v001`. For each capture, the Agent decides whether a compatible
addition belongs in the current edition, semantic evolution deserves another
edition, or an independent branch deserves a different section. There are no
mandatory Session wrappers or generic `Candidates`/`Open tensions` subheadings.
<!-- tarav.breadcrumb ccf757e0b9f6 -->

## Git closure

A successful capture ends with a recoverable Git checkpoint of the complete
current working state under `notes/wiki/`, even when that includes earlier
Note changes. A topical `--target` does not narrow Git closure. Changes outside
the Project.Wiki remain excluded.
<!-- tarav.breadcrumb b38f4695518c -->
<!-- tarav.breadcrumb 1a346f5baeb7 -->

The invocation authorizes this scoped commit; it is workflow closure rather
than a second approval gate. The Agent first validates references and inspects
the scoped diff. Empty commits are skipped, while blocking validation or Git
failures leave the surface uncommitted and become reported POIs.
<!-- tarav.breadcrumb 38af8c66bccf -->
