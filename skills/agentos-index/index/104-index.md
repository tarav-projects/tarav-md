## Project.File.Index

- `Project.File.Index` is the file-level routing section of the `Index.Router`
- describes the project's file system at folder level, with individual files listed only when fundamental
- one sentence description per entry — token budget is tight, this is always-loaded context
- gives agents a structural map of where to look — not a complete listing, but the important entry points

****

## Index.Activation

- `Index.Activation` is the process of bootstrapping the `Index.Runtime` for a session
- handled by `agentos-index-activate` — a dedicated bootstrap skill
- loads the full index into context, then activates operating behavior
- activation is opt-in — triggered by `AGENTS.md` or manual invocation
- operational detail: `references/runtime.md`

****

## Unresolved.Index.Name

- `Unresolved.Index.Name` is an unknown `Dotted.Name` that the agent cannot resolve against the index
- parked in the session — available for later resolution if more context emerges
- if the same name recurs 3+ times, suggest capture to the user
- gap detection is passive — don't interrupt conversation flow

****

## BuiltIn.Namespace

- `BuiltIn.Namespace` is an `Explicit.Namespace` that every Agentos project is expected to have
- it's an interface — can be empty, populated as the project evolves
- examples: `Project.Surfaces`

****

## Project.Index.Skill

- `Project.Index.Skill` is the `<project>-index` skill that holds the public index
- the canonical public surface for the index — other skills assume it exists
- contains `index/`, `appendix/`, and `references/`

****

## Concept.Cite

- `Concept.Cite` is the inline citation notation for referencing related concepts: `[Concept.X, Concept.Y]`
- used when the relationship is relevant but doesn't come up naturally in the writing
- goes inline — next to the line it relates to, like academic paper citations
