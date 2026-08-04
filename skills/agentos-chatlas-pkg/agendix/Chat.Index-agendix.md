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
