# Skw.Annotation — Appendix

****

## Skw.Annotation/Appendix

- the declaration is documentation that cannot silently rot — the checker watches its targets; understanding and maintenance are the same feature ^c20260711-4u
- two constraint tiers price differently: the declared tier (fragment vs annotation) is the continuously watched inner loop; the ambient tier (fragment vs the whole index and chat) holds as always via rarer agentic sweeps — annotations watch the hot subset, they do not replace the global obligation ^c20260711-4u
- annotation scope is editorial — the author regulates each annotation's size; granularity policy (block-hash vs line-level deps) is a parked `Experience.Gated.Decision` ^c20260711-4u
- `Natural.Placement` circulates content both ways: notes accrete at annotations (the lowest-friction surface nearest the work); what proves general or touched promotes inward to the index, `Cited.Duplication` back out — the index keeps its value as the bag of all curated touched data ^c20260711-4u

****

## Skw.Annotation/Construct.Grammar

Construct-form depth, absorbed from the retired `Skillware.Construct` block; the operational spec lives in the `agentos-skillware` lang module.

- the sigil pair splits open from belong: `$kw:` opens a construct (or declares a divider); `$kw.` marks everything belonging to the open construct — further flags, value continuations, and the closer ^c20260712-7u
- closure is fully explicit for body-bearing constructs: a bare `end` is invalid; a multi-close line (`end-a end-b`) unwinds the open stack innermost-first; a heading closes nothing — a construct left open at a heading or EOF is a finding ^c20260710-4u ^c20260711-9u
- closure is declared, never positional: beyond owned ends, the registry may grant a command peer-closure — opening it closes its open peers (`when` closes `when`/`then`; a leveled `section` closes sections of level ≥ its own) — and a parent's end closes its open scoped children; every closure still happens at a marked machinery line ^c20260713-0u
- peer-closure is only for vocabularies where the next declaration IS the boundary by construction (rows, sections); body-bearing primitives (`text`, `copy`, `derived`) keep mandatory owned ends — nothing can infer where an arbitrary body stops ^c20260713-0u
- end-free annotation sections are this mechanism, not an exception: a divider is a peer-closing command, so explicit closure survives intact ^c20260713-0u
- no indentation: bodies sit at column 0 — nesting is logical (the parse stack + owned ends), never visual; the body is runnable prose first ^c20260710-4u
- three primitives instantiate the construct anywhere in a src: `text` (a literal, tag optional), `copy`, and `derived` — a generation function whose declaration describes the generated body and whose body is the current output ^c20260710-4u
- structural commands (`router`, `when`, `then`) compose primitives ^c20260710-4u
- arg flags are trait annotations, orthogonal to the command list: a command gives core semantics, annotations layer constraints on the body (`--from` inbound dependency, `--intent` derivation context, `--to` sends the agent to another surface) ^c20260711-0u ^c20260712-7u
- trait semantics are reserved by JSONPath-style paths: `*.key` reserves the key's meaning on every command, `command.key` scopes it to one; validation is registry-driven, and a scoped semantic that generalizes is promoted up the path ^c20260711-0u
- any declaration may carry a `^label` token — identity riding the construct; `label ^x` is the explicit command for a labeled literal (no command-less declarations); owned ends accept either owner, `end-<command>` or `end-^label` ^c20260711-1u ^c20260712-7u
- labels extend the address grammar — `@path^label` (labeled span), `^label` (file-local); a `--from` on a labeled span hashes only that span, so drift is heading-independent and fine-grained ^c20260711-1u ^c20260712-10u
- labels are src-only machinery, stripped at compile — distinct from `Anchory.Anchor`s (global evidence links that survive in the text); renaming a label breaks importers, caught by the dead-link check ^c20260711-1u
