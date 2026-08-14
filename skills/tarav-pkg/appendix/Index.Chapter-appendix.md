****

## Index.Chapter/Appendix

- `000-INDEX.md` routes every chapter; the appendix is the Index's depth layer, reached by naming (`Appendix.Discovery`), not routed as a chapter
- a concept may carry its chapter as an optional `Dotted.Name` prefix (`Impl.Concept.A`)

****

## Index.Chapter/Flat.File.Design

- semantic file names create placement friction — every new concept requires deciding which file it belongs to
- placement friction slows writing and creates false groupings that age poorly
- flat anonymous chapter files eliminate the decision: append to the last file, done
- the router (`000-INDEX.md`) absorbs the cost — one place to update, loaded with the index per the `Package.Driver`
- organizing is a separate concern handled by `Block.Path` and `Explicit.Namespace` — a concept can belong to multiple namespaces without moving between files
- splitting an overfull file is deferred to maintenance — not a writing concern

