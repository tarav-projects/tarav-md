---
name: agentos-index-trigger
description: "Lightweight always-on detection of Dotted.Names during conversation. Fires the Index.Eval.Loop and reports grounding in footer."
---

# agentos-index-trigger

Lightweight always-on detection of `Dotted.Names` during conversation.

This is an `Alias.Skill` of the `agentos-index` `Skill.Package`.
Full design reference: `agentos-index/references/eval-loop.md`

## Behavior

Watch user messages AND your own reasoning for `Dotted.Names` and fire the `Index.Eval.Loop`:

1. Detect `Dotted.Names` — capitalized words joined by dots, 2+ parts
2. Resolve against `001-ontology.md` — exact or approximate match
3. If resolved → load block fundamentals, ground the conversation
4. If unresolved → park as `Unresolved.Index.Name`
5. Report in footer: `> Index: loaded ... | unresolved: ...`

Detection applies to: user messages, files you read, concepts you encounter while reasoning.

## Detection Rules

- Triggers: `Word.Word(.Word)*`, `Word.Word:target`, `<Word>.Word`, `<Word>.Word:<target>`
- NOT triggers: `e.g.`, `file.txt`, URLs, lowercase dotted, single-part names

## Escalation

- load `agentos-index-resolution` when name matching needs deeper search
- load `agentos-index` when full design context is needed
- suggest `agentos-index-writer` to the user when a concept recurs 3+ times unresolved

## Constraints

- stay minimal — this skill is loaded in every active-index conversation
- do not interrupt conversation flow — detection and grounding happen naturally
- gap detection is passive: park and show in footer, don't prompt unless recurrent
