---
name: agentos-index-resolution
description: "Resolve approximate or unknown Dotted.Names against the Agentos Index using whole-block content and chat context."
---

# agentos-index-resolution

Resolve approximate or unknown names against the Agentos Index.

This is an `Alias.Skill` of the `agentos-index` `Skill.Package`.
Full design reference: `agentos-index/references/gating.md` (Index.Name.Resolution section)

## When To Use

- called by the `Index.Eval.Loop` when a name needs resolution beyond simple registry lookup
- called manually by the user: "resolve `Some.Name`"
- called when near-duplicates or approximate names are detected

## MVP Behavior (fully agentic)

1. Read `000-index.md` and `001-ontology.md` as entry points
2. Follow your instincts from there — scan blocks, read notes as needed
3. Use the **whole block** for matching, not just the `findability:` field
4. Use the **whole chat context** for discovery — the `Dotted.Name` is the trigger, but resolution uses surrounding conversation and common sense
5. `findability:` is a performance hint — extra info to help search, not the only input
6. Return: resolved canonical name OR unresolved

## Resolution Rules

- when a name doesn't exactly match the registry → search for close equivalents
- matching is semantic (meaning-based), not just string similarity
- if a likely match exists → ground using the canonical name
- if no match → treat as potential new concept (feeds into `Gap.Detection`)
- near-duplicates: surface as a warning in the footer, don't interrupt flow

## Future Evolution

- may call CLI (`agentos index find ...`) for deterministic search
- may use embedding-based semantic similarity
- the skill boundary protects the interface — internals can evolve freely
