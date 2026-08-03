****

## Addressing.Sigil.Vocabulary/Appendix

- [DC] members enumerate inline, one line per sigil — diverging from the `Line.Type.Vocabulary` per-member-block precedent: a sigil's whole semantics fits one line ^c20260712-46u
- [PR] `^`'s one-register-per-space rule documents the full sigil budget on index surfaces — collision-proofing; `Anchory.System` owns the chat register, skw labels the file register ^c20260712-89u
- [DF] `::` mirrors Julia type ascription; its type reading subsumes the retired "applied to a target" phrasing: `Maintenance.System::Agentos` is the `Maintenance.System` instance identified by `Agentos` ^c20260712-61u
- [DF] `:` mirrors the universal `path:line` convention; `::` longest-matches over `:`, so parsing is unambiguous ^c20260712-63u
- [PR] `#` and `:` are the two file-internal addressers — `#` by heading region (stable), `:` by line number (volatile); prefer regions for durable names ^c20260712-88u
- [CT] a `<...>` variable is resolved only where the context calls for it — the skw `--from` context binds it through `Skw.Pkg.Dependency`; a documentation or example context communicates it unresolved ^c20260724-41u

****
