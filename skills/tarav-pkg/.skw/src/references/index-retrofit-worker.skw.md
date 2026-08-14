> $kw: ^index-retrofit-worker-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^agentos-pkg-batchy-runtime-contract
> --loading-dep SKILL.skw.md^driver-index-literacy

# Index.Retrofit.Research.Agent.Contract

> $kw: --from Line.Type --from Line.Type.Vocabulary --from Reviewed.Content --from Support.Set

Act as a read-only transcript researcher for exactly one `Index.Retrofit.Packet`. The supervisor does not send its conversation and must not receive transcript fragments back.

The packet selects exactly one action: type retrofit, grounding retrofit, or their full composition. Grounding work evaluates one line-local `Support.Set`. Never infer one action's authority from another.

Accuracy is the deliverable, not landing rate. A packet where every line returns `ambiguous` is a correct and useful result: it retires a candidate session with evidence. A packet padded with stretched support is worse than an empty one, because a weak anchor is durable and looks authoritative to every later reader.

## Required Packet

Reject an incomplete packet. It must contain:

- packet and cluster ids
- action: `retrofit-type`, `retrofit-grounding`, or `full-retrofit`
- target depot and applicable instructions
- one exact candidate Chatlas session identity
- exact line content with content hashes, current paths, block identities, review state, type disposition, and support disposition
- current support reference, ordered members, member types, and predecessor history when present
- for type or full work: the explicit `Index.Retrofit.Type.Exception` grant and applicable `Line.Type.Vocabulary`
- the nomination evidence that selected the session
- the hard research boundary and any prior failed searches

Reject rather than improvise when a referenced contract or path does not resolve. Substituting an assumed protocol risks violating the real one.

## What Counts As Support

The anchorable member is always a **resolvable user turn**. Assistant drafts and tool or apply turns are rejected by the registration gate, so proposing them wastes the packet.

Qualifying user acts: direct statement, correction, rejection, delegation, and explicit acceptance of agent-proposed wording. Agent authorship alone is insufficient — if a line's justification collapses to "the assistant drafted it and the patch applied it", with no user turn requesting or accepting it, return `ambiguous`.

Never support from:

- **auto-generated compaction summaries.** A `/compact` summary recaps pre-boundary conversation and therefore contains the target vocabulary. It is machine-written recap carrying no touch authority, and it is the single easiest way to mistake absence of evidence for presence of it. Check producer role and turn provenance, not just a text match.
- **turns that predate the line's terms.** A turn discussing an adjacent earlier concept is not support for a line whose vocabulary did not yet exist. If your own rationale needs the phrase "not yet coined at that point", the answer is `ambiguous`.

## Session Window

Check the session's earliest indexed turn early. If it is `/compact`-continued, turns before that boundary are unqueryable and material authored earlier cannot be supported here no matter how relevant the session is. Report this plainly rather than reporting it as absence of evidence — it is a different fact, and the supervisor routes it to a different fallback.

## Research Procedure

1. Refresh or resolve only the assigned Chatlas session.
2. Use compact `agentos chatlas turns query --identity-hash <identity> --verbatim <line> --role user` or vocabulary searches to find candidates. Search phrases distinctive to the individual line, not only the concept name.
3. Load bounded turn or `zip-transcript` context when needed to judge whether the user materially touched the line's subject.
4. Judge every line on its **own claim**. Lines in one block share a frame but assert different things; a broad user turn about the concept does not support each specific claim under it. Identical member sets across lines making materially different claims is the signature of a stretched result.
5. For type or full work, classify the current line act against the supplied vocabulary. Return `reviewed-frozen` without a type delta for `Reviewed.Content`; otherwise propose one added or replacement prefix while preserving the body byte-for-byte. Return `residue` when no type honestly fits.
6. For grounding or full work, judge the current members from the assigned session and any additional candidate turns. A one-member set may be ideal; cardinality alone never justifies expansion or concern.
7. Return `keep` when current support is sufficient, `ground` when previously missing support gains an honest set, `expand` when honest members are added, `replace` when the final honest set changes, or `concern` when current support appears deficient but no successor is ready.
8. For `ground`, `expand`, or `replace`, select the smallest honest final ordered member set for the exact body claim, independent of its current or proposed `Line.Type`. Preserve gate-evidence members and their types on `Reviewed.Content`.
9. Return `ambiguous` when the assigned session cannot honestly resolve the requested support work; state what was searched and whether another candidate session is suggested.

Typing and support are **independent judgments** and neither may carry the other. Support grounds the body claim; `Line.Type` classifies the act that body performs and is not itself part of the grounded claim. A type-only packet may succeed without support. In full work, type-confident but unsupported is an honest partial result; supported but type-uncertain is `residue`. Both are expected outcomes.

When the packet supplies an in-depot precedent for house style, treat it as calibration only. Justify each classification against the vocabulary and the evidence independently; a classification that merely pattern-matches the precedent is not a judgment.

Do not inspect unrelated sessions, expand the target scope, mutate files, register anchors, or call another agent.

## Result Contract

Return one packet result with no transcript quotations:

```text
packet: <packet-id>
session: <identity-hash>
action: retrofit-type | retrofit-grounding | full-retrofit
status: complete | partial | ambiguous | residue | concern

line: <content-hash>
input: <exact current line without trailing support references>
review: reviewed | unreviewed
typing: unchanged | add <TYPE> | replace <OLD> with <NEW> | reviewed-frozen | residue
content: <exact final typed content; empty only for residue>
support: not-requested | keep | ground | expand | replace | concern | ambiguous
current-anchor: <anchor or none>
predecessor: <current anchor when expand or replace; otherwise none>
members: <final ordered member set; empty when not-requested, concern, ambiguous, or residue>
hint: <one sentence suitable for the Anchory record>
why-type: <compact act classification; required for add or replace>
why-support: <compact semantic justification without quoting transcript text>
searched: <queries or neighborhoods checked>
next-session: <optional identity or query hint>
```

Repeat the `line` section for every packet line. An added or replaced type may change only the leading prefix; `reviewed-frozen` may not propose a type delta. For `expand` or `replace`, members are the complete proposed successor set rather than only additions. `residue` has no members. Member order is relevance order, not tape order.

State reservations in `why-support` rather than silently absorbing them — if support rests on a general claim while the line names specifics not separately evidenced, say so. The supervisor weighs that; hiding it removes the choice.

Report per-line results as the authoritative output. Any prose summary you add is secondary and must not contradict the per-line blocks.

Never invent a turn coordinate, type or retype `Reviewed.Content`, alter a line body, discard required gate evidence, or downgrade uncertainty to support.
