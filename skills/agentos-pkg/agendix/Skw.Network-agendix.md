****

## Skw.Network/Agendix/Dependency.Sync

- [DF] `Dependency.Sync` is the bidirectional CPU check between a surface's declared dependencies and its addressable-name mentions — two surfaces kept in sync, modulo blessings ^c20260716-13u
- [DC] a declaration is normative intent and part of the generation contract: "this surface MUST depend on these" — an agent regenerating the surface reads the dependency list as instructions, not metadata about the text ^c20260716-13u ^c20260716-14u
- [DC] mentions are the artifact's actual references — mechanically extractable via `Dotted.Notation` ^c20260716-14u
- [DC] forward check: a resolving mention without a declaration or blessing is a POI — undeclared dependency; declare it, or remove/bless the mention ^c20260716-12u ^c20260716-14u
- [DC] reverse check: a declaration never mentioned is a POI — unhonored dependency; the text fails its contract, or the declaration is stale and should be removed ^c20260716-13u ^c20260716-14u
- [RJ] auto-derived implicit mention-edges as a substitute for declarations — with one surface there is nothing to sync against; the redundancy of intent vs artifact is the value ^c20260716-13u
- [DC] the agent resolves each POI; the resolution edits whichever surface was wrong — that is the sync ^c20260716-14u
- [PR] the reverse direction catches generation failure, not just drift: a surface that silently ignored part of its brief ^c20260716-13u

****

## Skw.Network/Agendix/Structural.Vs.Touched

- [DF] the `Skw.Network` splits into two dependency kinds — structural and touched — distinguished by what authorizes each ^c20260721-11u
- [DC] a structural dep is a derivation edge, "this surface derived from that surface": self-authorizing and evident, needing no grounding because the derivation is re-runnable proof — the axis of architecture and surface reuse ^c20260721-11u ^c20260721-12u
- [DC] a touched dep links to a touched surface — an index line/block or a user turn — carrying the user's decision: it needs `Annotation.Authority` and is gated — the axis of surface grounding ^c20260721-11u ^c20260721-12u

****

## Skw.Network/Agendix

- [DC] the index surface may participate in the `Skw.Network`, which is what makes a blessing's documentation dependency mechanically checkable ^c20260802-8u
