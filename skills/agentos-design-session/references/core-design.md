# Core.Design Artifact

`*-core-design.md` is the conceptual design layer of a `Design.Session`.

It stages a scoped fragment of `Design.Target.Model`: the named concepts, meanings, behaviors, relationships, open questions, and settled judgments produced through the session.

## Filename

Use:

```txt
NNN-short-topic-core-design.md
```

Store it in `notes/live/` using `agentos-live-note-base` numbering guidance.

## Structure

```md
# [Short Title] - core-design

## Motivation

## Items Index

- Item.Name: [status] short description

## Items

### Item.Name

#### Usage History

## Notes

## End Log
```

## Item States

Use the same lightweight item states as design-session work:

- `fresh` — just added, no discussion yet
- `in-progress` — some discussion has happened
- `converging` — likely ready to close soon
- `closed` — sufficient for this session, user-gated
- `reopened` — user explicitly reopened a previously closed item

`closed` means sufficient for the session. It does not mean the concept is globally finished or frozen.

## Item Scope

Items are the selected conceptual focus set for this session. They are not a registry of every relevant concept in the ontology.

An item may be new design material, an old concept being revisited, a refinement of an existing index concept, a relationship, a boundary, a behavior, or an unresolved question.

The item section should be self-contained enough to understand the design work done in this session without replaying the chat or chasing every referenced index note. References are allowed, but the session's actual contribution should live in the item section itself or elsewhere in the same `Core.Design` file.

## Writing Guidance

Write concept material here, not task execution detail.

Good `Core.Design` material includes:

- named concepts
- meanings and boundaries
- behavior descriptions
- relationships between concepts
- user-settled design judgments
- important open questions
- taste, tradeoffs, and rationale when they shape the design

Distinguish settled material from open material:

- `Design.Alignment.Core` is material explicitly settled with the user.
- `Design.Open.Space` is material that remains unsettled, implicit, deferred, or agent-assumed.

The agent may propose candidate material. Only the user can settle material into `Design.Alignment.Core`.

Use `#### Usage History` when it helps explain why a concept exists, how it was used in the session, or why a naming/behavior choice matters. Usage history adds motivation and context; it is not part of the concept's primary definition.

## Boundaries

Do not put concrete implementation steps here. Put task objectives, validation, and boundaries in `TODO.Design`; put implementation handoff, vertical slices, ordered work when useful, and acceptance signals in `Impl.Req`.

Do not turn the file into a transcript. Capture the durable concept shape and the current settled/open state.
