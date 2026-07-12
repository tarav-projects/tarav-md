****

## Skw.Address.Schema/Appendix

- [PR] minting a `Dotted.Name` for an entity that already has a native address causes concept-name explosion — the pressure this schema removes ^20260712-0
- [EX] the four motivating usage cases: a bare concept, ontological nesting, a file as ontology entity, a region inside a file ^20260712-0
- [RJ] form-dependent semantics ("concept blocks vs address blocks") — blocks are blocks under any name form ^20260712-0
- [RJ] a closed vocabulary of file-space root tokens — common sense governs roots; `<...>` variables are self-describing ^20260712-0
- [DC] bare-mention resolution: a bare `Bla/Blo` is ontology-space by default; a `Locator.Name` match wins when it exists ^20260712-2
- [DC] when both an ontology block `Bla/Blo` and a locator block `@Bla/Blo` exist, surface both candidates and confirm (`Fuzzy.Dotted.Name`); no fixed precedence ^20260712-2
- [RJ] scheme prefixes (`project:`, `skill:`, `index:`) — replaced by `@` + common-sense roots; `:` states line position, making schemes unparseable ^20260712-2
