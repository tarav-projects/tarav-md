# Tarav.Diagram

This document describes the current candidate design of `Tarav.Diagram`.
It is subordinate to the Tarav Constitution and remains amendable.

## Data Train

Tarav progressively interprets captured user-agent collaboration through
one integrated data train:

```text
Chat.Raw.Artifact
      ──normalize──▶ Chatlas.Normal.Model
      ──annotate───▶ Diagram.Annotations
      ──select─────▶ Context.Model
      ──supply─────▶ user-agent collaboration
```

Evidence inspection and audit travel in the opposite direction:

```text
Context.Model
      ──expand─────▶ Diagram.Annotations
      ──resolve────▶ Chatlas.Normal.Model
      ──verify─────▶ Chat.Raw.Artifact
```

Meaning accumulates toward the `Context.Model`; evidentiary authority
accumulates toward the `Chat.Raw.Artifact`.

## Progressive Interpretation

`Chat.Raw.Artifact` preserves provider-native evidence. It retains the
greatest source detail while making the fewest Tarav interpretations.

`Chatlas.Normal.Model` turns provider-specific chats into a shared causal
tape of sessions, events, turns, content, and context horizons.

`Diagram.Annotations` extract supported semantic structure from that tape.
Each Annotation identifies its producer, its selected support, and the
assertions by which its claim can be assessed.

`Context.Model` selects and organizes relevant Diagram material for a
particular collaboration. It is a contextual projection, not a new
authority surface.

The supplied context enriches further user-agent collaboration, which
captures more touched chat data and continues the loop.

## Responsibility Boundaries

The data train is layered so no component must carry all of Tarav's
complexity:

- `Tarav.Archive` preserves Artifacts without understanding chats.
- Chatlas understands chats without constructing Diagram ontology.
- `Tarav.Diagram` constructs supported semantic structure without parsing
  provider-native artifacts.
- Contextualization selects useful structure without becoming its
  authority.

Capture therefore precedes interpretation. Higher layers remain
inspectable through lower layers, derived layers can evolve without
rewriting their evidence, and faults in normalization, annotation, or
selection can be surfaced independently.

## Chatlas Foundation

Chatlas is an integral part of Tarav and the native chat-evidence model of
the main `Tarav.Diagram`.

Chatlas captures selected provider-native material into a Git-tracked raw
repository suitable for registration by `Tarav.Archive`. It then derives
the normalized causal tape used by the Diagram.

Diagram support and producer coordinates use Chatlas references rather
than direct references into provider-native Artifacts. A Chatlas reference
must remain able to resolve its normalized subject and expose the Archive
references supporting it.

Conceptually:

```text
Diagram.Annotation
      ↓ Support.Set / Producer
Chatlas.Reference
      ↓ normalized subject and provenance
Chatlas.Normal.Model
      ↓ source evidence
Archive.Reference
      ↓
Chat.Raw.Artifact
```

For every member of an Annotation's `Support.Set`, the referenced content
must have been present in the Annotation's producing chat context before
the producing turn. This is assessed by resolving the support content and
inspecting the producer's preceding chat horizon; it does not require a
separate materialization record.

## Monolithic Library

Tarav is one monolithic library. Archive, Chatlas, Diagram, and
Contextualization are responsibility and data boundaries rather than
separate packages or services.

Diagram Records are retained as typed data and instantiated by the Tarav
library as runtime objects. The retained data stores irreducible
instance-specific facts. Type-level rules and reliably recoverable values
may be supplied or derived by code. Data is duplicated only when a
material robustness benefit justifies it.

A minimal Annotation data shape is:

```json
{
  "type": "<Annotation.Type>",
  "producer": "<Chatlas.Reference>",
  "support": ["<Chatlas.Reference>"],
  "data": {}
}
```

The Annotation's own address is supplied by its Git-based Diagram storage
context and need not be duplicated inside its retained data.
