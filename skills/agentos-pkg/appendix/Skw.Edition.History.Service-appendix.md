# Skw.Edition.History.Service - Appendix

****

## Skw.Edition.History.Service/Skw.Edition

- [DF] `Skw.Edition` is a Git-observed change to one managed file, identified by its repository, path at the change, and commit. ^c20260725-129u
- [DC] Git supplies the edition identity and commit time; Chatlas does not decide whether the edition occurred. ^c20260725-99u
- [CT] an edition records historical change, orthogonal to `Touched.Authority`; an associated chat session may or may not support the file's content. ^c20260725-59u
****

## Skw.Edition.History.Service/Skw.Edition.Session

- [DF] `Skw.Edition.Session` is the association between a `Skw.Edition` and a `Chat.Surface` whose agent work contributed to that file edition. ^c20260725-128u
- [CT] the association expresses contribution, not sole authorship or `Touched.Authority`. ^c20260725-88u
- [PR] Chatlas supplies the session identity, timing, and evidence used to establish the association. ^c20260725-150u
****

## Skw.Edition.History.Service/Skw.Edition.History

- [DF] `Skw.Edition.History` is the accumulated, queryable set of `Skw.Edition.Session` associations for one managed file. ^c20260725-127u
- [PR] it is maintained incrementally and can be reconciled against full Git file history and the Chatlas corpus. ^c20260725-161u
- [CT] it is historical provenance, not a statement of current authority over the file. ^c20260725-75u
****

## Skw.Edition.History.Service/Skw.Edition.Session.Support

- [DF] embedded Chat.Support.Set warranting the claim that a session contributed to an edition. ^c20260725-143u
- [DC] reuse the Chatlas support-set record shape directly; no Anchory allocation or indirection is required. ^c20260725-111u
- [CT] the support set has at least one member, every member resolves, and it includes the associated session. ^c20260725-93u
- [RJ] candidate-discovery signals and search heuristics belong to the maintainer workflow, not the persisted history. ^c20260725-170u
- [PR] the maintainer inspects transcript fragments before recording an association. ^c20260725-163u
****
