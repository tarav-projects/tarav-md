# agentos-skillware --dev (adoption)

Use this module to bring an existing hand-owned skill under Skillware management. Adoption is per-file and incremental — a skill can stay partially managed indefinitely.

## The Playbook

1. **Inventory.** Read the whole skill — every module, in full. Adoption without a full read produces a decorative graph.
2. **Parity contract.** Decide what the compiled surfaces must equal. For a pure adoption: each compiled file equals the current hand file byte-for-byte (compile normalization: blank-run collapse and trim). State any intended deltas up front — they are the only acceptable diffs.
3. **Graph extraction.** Identify the real span-level relations (`references/author.md`): which sections restate an index block, digest another module's section, or duplicate a span verbatim. Everything else is a root.
4. **Author srcs.** Per adopted file, create the mirrored `.skw.md`: passthrough for roots (verbatim content), recipes for the identified relations with the current content as the derived body. Create `.skw/skw.json` if `Dotted.Name` deps exist. Delete hand files being superseded by compiled ones *before* building.
5. **Build and verify.** `agentos skw build`, then `check` (expect all-ok), then the mechanical parity diff:

   ```
   diff <compiled-file> <original-file>
   ```

   Empty diffs (modulo stated deltas) close the adoption.
6. **Record.** Note the landed graph — roots, derived recipes, copies — wherever the work is being tracked.

## Judgment Calls

- **prefer parity over improvement**: adopt first, improve later — a content change hiding inside an adoption is invisible in review
- **weak derivations are fine**: when a section's original wording must survive, keep it as the derived body and state the weaker rule in the intent
- **duplicate heading titles** within a source file collide as regions — first match wins; restructure headings if that is wrong
- **nothing earns a recipe** is a valid outcome for a module — passthrough roots are the common case, not a failure
