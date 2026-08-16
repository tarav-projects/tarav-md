> $kw: ^touched-data-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract

> $kw: --from Agentos.Index.System --from Anchory.System --from Chat.Surface --from Demoted.Index.Line --from Index.Line --from Index.Line.Anchor --from Index.Presumption --from Live.Index.Line --from Open.Inference --from POI.Instance --from Reviewed.Content --from Support.Set --from Touch.Authority.Surface --from Touched.Authority --from Touched.Data --from Touched.Index --from Touched.Support.Network
> --dev-from references/index-context-assembly.skw.md

# Touched.Data.Knowledge.Module

Use this workflow-neutral knowledge module whenever an index operation must decide what carries touch, how an indexed statement is supported, or how much decision weight a line has.

`Touched.Data` is read from provenance through this model, never inferred from a container name alone.

## Authority Flow

The general path is:

```text
qualifying Touch.Authority.Surface edition
  -> first-order Touched.Data
  -> Support.Set
  -> Support.Reference
  -> Index.Line
```

- the system observes qualifying editions of registered authority surfaces, never `User.Touch` directly
- qualification is surface-specific and defeasible; not every change to a containing surface carries touch
- a qualifying user `Chat.Message` is presently the only registered authority-surface realization
- `Chat.Surface` is the containing context, while the attributable qualifying user message is the current authority unit
- factual error, staleness, or contradiction does not by itself erase touch provenance

## Support Network

- `Support.Set` is one line's evidence bundle of exact authority-surface data or durable coordinates
- `Support.Reference` is the abstract edge connecting the line to that set
- `Support.Reference.Metadata` describes the edge but is not the edge
- `Touched.Support.Network` is the global network composed by those line-local sets and references
- `Anchory.System` supplies the stable `Index.Line.Anchor` joining the Index triplet to its Chatlas relationship dossier
- the dossier's `relationships.support` namespace records the line's `Support.Reference` and exact `Chat.Support.Set` members; gates and provenance remain independent relationships
- a changed support interpretation creates a new reference because it creates a new network edge

## Line Standing

- `Live.Index.Line` is present in the current index cut and may condition current reasoning
- `Grounded.Index.Line` has a resolvable nonempty support set and carries `Touched.Authority`
- `Ungrounded.Index.Line` remains live index content but carries only `Index.Presumption`; missing grounding is debt, not a deletion trigger
- `Demoted.Index.Line` is historical and does not condition current reasoning
- review is independent of grounding: `Reviewed.Content` records the approval protocol for wording, not touch authority or factual truth

## Coherence And Decision Weight

- coherent applicable touched data constrains the answer region
- contradictory, ambiguous, stale, or applicability-sensitive evidence requires reasoning rather than mechanical obedience
- a conflict becomes a `POI.Instance`; the POI signals required attention but does not prescribe resolution
- `Open.Inference` evaluates provenance, applicability, currentness, support strength, and consequences
- open inference may select a provisional action without silently rewriting or discarding unresolved touched positions
- changing a gated index surface remains a separate reconciliation act

## Current Realization

The current implementation maps the general model as follows:

| General model | Current realization |
|---|---|
| `Touched.Index` | `Agentos.Index.System` plus its reachable touched-index members |
| `Touch.Authority.Surface` | qualifying user `Chat.Message` on `Chat.Surface` |
| `Support.Set` | exact members in `relationships.support` |
| `Support.Reference` | the support relationship recorded by the line dossier |
| `Index.Line.Anchor` | trailing `Anchory.Anchor` joined to a Chatlas2 line dossier |
| independent line relationships | `relationships.gates` and `relationships.provenance` |
| `Index.Line` | typed or legacy Markdown kernel line |
| chronological touched record | exact lines in `Chat.Index.Delta` files |
| current chat projection | `Chat.Index.HEAD` |
| current Project projection | chapters, appendix, agendix, and `Issue.Block`s |
| line dossier | attachment assertion plus independent support, gate, and provenance namespaces |
| home | oldest evidenced exact Delta containment, derived rather than declared |
| live cut / history | current Project/Chat HEAD files / Chat Deltas and Git history |

`Project.Support.Chats` links a Project Index to the Chat.Index surfaces that may cover it. Exact Delta containment supplies materialization evidence, while grounding members supply support. Missing grounding, ambiguous home selection, or semantic uncertainty remains a reconciliation POI; passive contextual import cannot prove itself.

Do not project current mechanics back into the general model. New authority surfaces or support implementations extend the realization without redefining touch.
