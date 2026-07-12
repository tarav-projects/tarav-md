****

## Addressing.Sigil.Vocabulary/Appendix

- [DC] members enumerate inline, one line per sigil — diverging from the `Line.Type.Vocabulary` per-member-block precedent: a sigil's whole semantics fits one line ^20260712-1
- [PR] `^`'s one-register-per-space rule documents the full sigil budget on index surfaces — collision-proofing; `Anchory.System` owns the chat register, skw labels the file register ^20260712-1 ^20260712-10
- [DF] `::` mirrors Julia type ascription; its type reading subsumes the retired "applied to a target" phrasing: `Maintenance.System::Agentos` is the `Maintenance.System` instance identified by `Agentos` ^20260712-1
- [DF] `:` mirrors the universal `path:line` convention; `::` longest-matches over `:`, so parsing is unambiguous ^20260712-1
- [PR] `#` and `:` are the two file-internal addressers — `#` by heading region (stable), `:` by line number (volatile); prefer regions for durable names ^20260712-1

****
