****

## Agentos.Index.System/Agendix/Project.Current.Model

- [DF] `Project.Current.Model` is the present-facing projection maintained by a `Project.Index` ^c20260803-15u
- [CT] complete historical reasoning belongs in supporting `Chat.Index` tapes; the Project Index need not retain stale material solely for provenance ^c20260803-16u
- [PR] a fresh Project Index structure separates the current model, unresolved frontier, current resolution rationale, and mechanical support map ^c20260803-17u
- [DC] `Resolution.Head` retains contradiction lines and decision lines while they support the current Project model ^c20260803-18u

****

## Agentos.Index.System/Agendix/Project.Chat.Integration

- [DF] `Project.Chat.Integration` is the maintained relationship connecting Project Index lines to canonical homes in the Project Support Chat Set ^c20260803-19u
- [CT] either index may advance first; Project-to-Chat completeness is an eventual reconciliation assertion rather than a development constraint ^c20260803-20u
- [CT] a Project-only line is valid intermediate state whose missing Chat home emits a reconciliation `POI.Instance`, not an error ^c20260803-21u
- [DC] `Project.Support.Chats` is the explicit session-routing layer between the Project Index and supporting Chat Indexes and transcripts ^c20260803-22u
- [DF] `Project.Support.Chats` is the project-scoped union of support chats exposed by every `Touched.Index` surface in that project ^c20260803-43u
- [DC] each Markdown Index folder surface owns its local `Project.Support.Chats` shard ^c20260803-44u
- [DC] the first materialized projection covers Markdown Index depots only and stores each local shard at `<index-depot>/009-SUPPORT-CHATS.md` ^c20260803-45u
- [CT] `Skw.Touched.Index`, `Chat.Index`, and future `Touched.Index` surfaces remain inside the conceptual closure of `Project.Support.Chats`; their materialized projections are deferred until the Markdown Index projection stabilizes ^c20260803-46u
- [PR] reconciliation agents inspect unreconciled turn-index tails by default, produce live findings, and route review-worthy material into the Project Agendix ^c20260803-23u

****

## Agentos.Index.System/Agendix/Project.Index.Redesign.Rollout

- [DF] `Project.Index.Redesign.Rollout` is the staged transition from Chat Index redesign through compatibility integration to eventual Project Index redesign ^c20260803-24u
- [DC] the expensive Project Index redesign happens last, after an intermediate phase integrates the redesigned Chat Index with the existing Project Index ^c20260803-25u
