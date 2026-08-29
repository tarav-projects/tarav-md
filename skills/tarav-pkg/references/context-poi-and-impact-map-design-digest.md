# Context, POIs, and Product-Surface Impact

## Status

- This is an unapproved WIP design digest.
- It preserves discussion material for later review, capture, amendment, or rejection.
- It is not constitutional material, landed Diagram content, or approved Tarav design truth.
- The discussion recorded here took place in Chatlas session
  `01a02f8b-8c36-7123-ba70-1a217b776e28`.
- Future capture should recover the exact supporting User turns from that session
  rather than treating this summary as their replacement.

## Harness.Context.And.POI.Services

- Tarav's main services to Agents are context and POIs.
- Context gives an Agent the relevant user-grounded material needed to understand
  a situation.
- A POI tells the Agent that something about the current situation may deserve
  attention.
- Context alleviates the uncertainty exposed by a POI; it does not dictate a
  conclusion.
- Tarav supplies context and signals while users and Agents retain responsibility
  for reasoning and action.
- A POI is evidence that validation is operating, not evidence that Tarav is
  broken.

```text
suspicious state
      ↓ surfaces
     POI
      ↓ accompanied by
   Context
      ↓ interpreted by
User / Agent
```

## Production.Context

- `Production.Context` is the Model material demonstrably loaded into the chat
  context that produced a Product.Surface or one of its editions or fragments.
- A Model edition that merely existed at production time is not
  `Production.Context` unless its material was supplied to the producing Agent.
- Presence in `Production.Context` is observable provenance; it does not prove
  that the Agent relied on that material internally.
- Chatlas provides the producing chat's causal tape and context horizon.
- Git provides editions and changes to Product.Surfaces.
- Together, Git and Chatlas can help narrow which chats produced which changes
  and what context those producing Agents received.
- The mapping between a chat and an exact Product.Surface change may itself be
  incomplete or uncertain and may need annotations, assertions, and POIs.

```text
Product.Surface edition or fragment
              ↓ trace through Git and chat activity
       producing Chat.Context
              ↓ inspect through Chatlas
        Production.Context
```

## Review.Context

- A Product.Surface may be reviewed later without being modified.
- The review chat's loaded Model material forms its `Review.Context`.
- A modern review can establish that an unchanged Surface was inspected with
  newer context than the context available during production.
- Production and review histories remain independently inspectable.
- A review does not rewrite the historical `Production.Context`.

## Product.Surface.Annotations

- SKW is a fundamental tool for attaching annotations to Product.Surfaces.
- SKW provides addressable Product.Surface attachment points and may point from
  those surfaces into Diagram material.
- The Diagram owns the semantic annotation, its evidence, assertions, scores,
  and relationships; SKW embeds or renders the Product.Surface-side pointer.
- A Product.Surface annotation may identify an entire Model as relevant.
- A more selective annotation may identify the Lines or Blocks considered
  fundamental to that Surface or fragment.
- Selective annotations can provide future Agents with focused context while
  retaining escalation paths to the wider Model and its supporting data.

```text
Product.Surface fragment
          ↕ SKW attachment
Diagram context/dependency annotation
          ↓
Model / Block / Line ships
          ↓
Chatlas support and Archive evidence
```

## Context.Model.Views

- Later work may benefit from the Model material used during production, the
  material currently present in Model HEAD, or both.
- A historical view helps an Agent understand why a Surface was produced in its
  present form.
- A current view helps an Agent apply the project's present understanding.
- A change-aware view lets an Agent compare production context with current
  context.
- Tarav should preserve these options and provide sufficient context; it should
  not hardcode the semantic choice of which view an Agent must use.

## Impact.Map

- Product.Surface annotations progressively form an impact map across Tarav
  surfaces.
- A Surface may declare that a Model, Block ship, or Line ship is fundamental to
  understanding or maintaining it.
- Diagram material may participate in the same map: a Block that cites or
  depends on another Block ship may require attention when that dependency
  changes.
- A change to declared fundamental material surfaces a POI against dependent
  surfaces.
- The POI asks whether anything should be reconsidered; it does not claim that a
  dependent Surface is wrong or prescribe an update.
- Impact-map coverage may remain incomplete and grow organically over time.
- Agents perform semantic impact analysis. Tarav maintains declared hints,
  detects observable change, supplies context, and raises POIs.

```text
Model Line or Block ship changes
               ↓
declared dependent Product/Diagram surfaces
               ↓
POI: should these surfaces be revisited?
               ↓
Agent receives dependency change and context
```

## Producer.And.Reviewer.Audit

- Tarav can audit whether the Agent that produced or reviewed a Surface had the
  expected Model material loaded.
- Missing or outdated expected context may surface a POI that the Surface was
  likely produced or reviewed with insufficient context.
- This remains a signal rather than a verdict about Surface correctness.
- A later review performed with modern context may address the operational
  concern without modifying the Surface.

## Blessing

- The former Tarav design called an explicit acceptance of one POI in its
  current situation a `Poi.Bless` act.
- A Blessing is a candidate Diagram Annotation in the new system.
- A Blessing targets one POI situation, not the POI class, another occurrence,
  or future changed situations.
- The Blessing's producing Chatlas context provides its `Review.Context`.
- If the Surface, dependency, or other material situation changes, the prior
  Blessing may become stale and the concern may return.
- The old `Bless.Session.Audit` candidate already described locating the
  blessing chat and checking whether required context was loaded before the
  blessing moment.
- A Blessing should remain auditable and visible rather than erasing history.
- `Reviewed.Content` remains distinct: it records explicit user approval of
  materially equivalent wording, while a Blessing accepts one POI situation.
- These recovered concepts are legacy evidence until they pass the new design
  and capture process.

## Minimal.Common.POI.Engine

- Tarav needs one small POI runtime that every subsystem can use.
- The runtime is analogous to pytest's collection, execution, and reporting
  machinery, while each domain owns its checks and input model.
- The minimum execution shape is:

```text
Domain Floor.Model
        ↓
registered POI.Check classes
        ↓
passed / failed / blocked
        ↓
stable POI.Instances
        ↓
shared report
```

- A `POI.Check` is executable code that detects one or more suspicious states.
- A `POI.Instance` is one concrete occurrence with stable identity and evidence.
- Every instance points to the exact Check class in the codebase that defines
  its detection mechanics.
- Every instance also points to the exact subject location where the suspicious
  state was found.
- The minimal engine does not require SKW or Diagram documentation.
- Diagram annotations may later enrich Check classes and code surfaces without
  becoming a dependency of POI execution.
- The common runtime owns selection, ordering, execution status, instance
  identity, and reporting.
- Domains retain their Floor.Models, Check classes, and domain semantics.
- Checks report state; they do not mutate the checked system or force a
  resolution workflow.

## Old.Index.Migration

- The disconnected Tarav Attic contains substantial indexed design material,
  including old Blocks, Lines, support sets, approval evidence, and POI/Blessing
  concepts.
- This material must not be bulk-copied as current truth or silently discarded.
- A candidate `tarav-pkg --migrate-old-index` skill should guide deliberate
  migration into the new Diagram.
- Migration should discover old identities, wording, support, and review
  evidence; resolve original User.Touched support through Chatlas; inspect
  continuity and current placement; and land accepted material through the
  ordinary current capture workflow.
- The Attic is migration evidence, not a runtime dependency of the new Diagram.
- New annotations must ultimately ground themselves in original
  User.Touched.Data rather than depending on legacy summaries.
- Missing or ambiguous support should surface POIs and must not be replaced with
  invented grounding.
- Migration receipts should preserve useful legacy identity and source mappings
  for audit.

```text
Old indexed Blocks and Lines
          ↓ discover
legacy wording, identities, support, review evidence
          ↓ resolve and inspect
current Chatlas and Archive grounding
          ↓ review
ordinary Capture.Manifest
          ↓ land
new Diagram annotations
```

## Usage.History.Product.Surface.Contextualized.Continuation

- An Agent begins work on a registered Product.Surface or fragment.
- Tarav locates known chats that produced or reviewed the relevant Surface
  editions.
- Tarav exposes the `Production.Context` and later `Review.Context`s that can be
  recovered from those chats.
- Tarav supplies relevant historical and/or current Model material according to
  the needs of the current collaboration.
- The Agent can expand from compact Model material to Diagram support, Chatlas
  context, and archived evidence.
- Missing expected context, stale Blessings, changed fundamental dependencies,
  and unresolved provenance surface as POIs.
- Tarav does not decide whether the Surface is correct or what action must be
  taken.
- The Agent uses the supplied context to make an informed decision and may
  modify the Surface, bless the current situation, enrich its annotations, or
  leave it unchanged.

## Open.Design.Questions

- How should Tarav associate exact Git changes and fragments with producing or
  reviewing chats when the evidence is ambiguous?
- How is expected Model context declared for production and review audits?
- What minimal Diagram Annotation types represent Product.Surface context,
  declared fundamental dependencies, and Blessings?
- Which historical and current Context.Model views should contextualization
  offer by default?
- What exact change makes a Blessing stale?
- How should direct impact findings be expanded across longer dependency paths
  without turning simple code into a semantic reasoning engine?
- How should old indexed support references be resolved and migrated in safe,
  reviewable batches?
