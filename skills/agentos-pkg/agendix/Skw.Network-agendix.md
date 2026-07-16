****

## Skw.Network/Agendix/Dependency.Sync

- [DF] `Dependency.Sync` is the bidirectional CPU check between a surface's declared dependencies and its addressable-name mentions — two surfaces kept in sync, modulo blessings ^20260716-13
- [DC] a declaration is normative intent and part of the generation contract: "this surface MUST depend on these" — an agent regenerating the surface reads the dependency list as instructions, not metadata about the text ^20260716-13 ^20260716-14
- [DC] mentions are the artifact's actual references — mechanically extractable via `Dotted.Notation` ^20260716-14
- [DC] forward check: a resolving mention without a declaration or blessing is a POI — undeclared dependency; declare it, or remove/bless the mention ^20260716-12 ^20260716-14
- [DC] reverse check: a declaration never mentioned is a POI — unhonored dependency; the text fails its contract, or the declaration is stale and should be removed ^20260716-13 ^20260716-14
- [RJ] auto-derived implicit mention-edges as a substitute for declarations — with one surface there is nothing to sync against; the redundancy of intent vs artifact is the value ^20260716-13
- [DC] the agent resolves each POI; the resolution edits whichever surface was wrong — that is the sync ^20260716-14
- [PR] the reverse direction catches generation failure, not just drift: a surface that silently ignored part of its brief ^20260716-13
