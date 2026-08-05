****

## Chat.Index/Agendix/User.Turn.Index

- [DF] `User.Turn.Index` is the maintained `Chat.Index` projection attached to one qualifying user turn ^c20260803-3u
- [CT] its anchoring user turn marks the end of its evidence scope; the projection may interpret preceding chat context but not later evidence ^c20260803-4u
- [CT] its source horizon is fixed while its extraction remains maintainable: agents may extend, amend, or correct it like any index ^c20260803-5u
- [PR] ordered user-turn projections preserve the evolution of ideas while allowing a separate current-model projection ^c20260803-6u
- [PR] newly captured lines attach preferentially to the index structure visible within their turn-bounded scope ^c20260803-7u

****

## Chat.Index/Agendix/Line.Home

- [DF] `Line.Home` is the canonical `Chat.Index` location assigned to one line by its issuing or capturing agent ^c20260803-8u
- [PR] the active chat is the default line home because its capturing agent holds fresh `User.Attention` and the richest semantic context ^c20260803-9u
- [CT] `Line.Home` is independent from `Known.Origin` and `Support.Set`; origin records occurrence while support records touched authority ^c20260803-10u

****

## Chat.Index/Agendix/Line.Provenance

- [DF] `Line.Provenance` is the independently maintained dossier of observed origins and tracked materializations for one canonical line content ^c20260803-11u
- [DF] `Known.Origin` is the best currently evidenced candidate for where canonical line content first appeared within the searched scope ^c20260803-12u
- [CT] an origin observation may be a user or assistant turn and does not become a `Chat.Support.Set` member merely by being the origin ^c20260803-13u
- [FR] Git evidence may extend line provenance with the first known tracked materialization and write commit when available ^c20260803-14u

****

## Chat.Index/Agendix/Line.Dossier.V5

- [DC] new line-bound anchor records use `chatlas.support-set.v5` while v3 and v4 remain readable ^c20260805-12u
- [DC] the v5 dossier preserves immutable subject, support-member ordering and types, and predecessors while issue context and provenance observations grow monotonically ^c20260805-10u
- [DC] `Known.Origin` is derived from the earliest currently known observation; `Line.Home` is independently recomputed from exact Delta containment ^c20260805-9u

****

## Chat.Index/Agendix/Project.Chat.Reconciliation

- [DC] Project reconciliation reads exact support-chat identities from `009-SUPPORT-CHATS.md` and audits every available Chat.Index in one pass ^c20260805-13u
- [DC] ordinary Project lines seek exact Delta home plus Chat HEAD coverage, while Issue.Block maintenance lines require an exact Delta home and may omit Chat HEAD ^c20260805-11u
- [DC] reconciliation findings remain advisory POIs; cursor advancement is project-local machine state and never writes Project HEAD ^c20260805-14u
