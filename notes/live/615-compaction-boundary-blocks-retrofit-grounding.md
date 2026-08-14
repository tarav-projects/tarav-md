# 615 — Compaction Boundary Blocks Retrofit Grounding

Status: open issue, mitigation available, no fix attempted.
Discovered during the `tarav-pkg` Index.Retrofit campaign (`notes/live/611-agentos-pkg-grounding-campaign.md`), passes 2 and 4.

## The Issue

A `/compact`-continued Chatlas session can only ground material that was authored **after** its compaction boundary. Turns before the boundary are not indexed, so they are unreachable by `agentos chatlas turns query` and therefore unusable as `Support.Set` members.

This is invisible at nomination time. Every cheap nomination signal — phrase queries, git dates, anchor neighbourhood, even *verified prior grounding in the same session* — can point confidently at a session whose relevant turns are on the wrong side of its own boundary.

## Evidence

Session `4f7b47fffe9e` (claude-code), during the retrofit campaign:

- **Pass 2 — succeeded.** Packet `P3b`, the `Line.Type` vocabulary family. 25/28 lines landed. The 3 failures (`Line.Type.Vocabulary`'s first three lines) failed *specifically* because that content predated the boundary.
- **Pass 4 — total failure.** Packet `P4`, the `Index.Edit.*` family. **30/30 ambiguous.** Target committed in `6ba0aa1` on 2026-07-05; the session's earliest indexed turn is its own compaction summary at 2026-07-07T17:23Z.

Same session, same worker model, same contract, same depot — one pass 89% successful, the next 0%. The only variable was which side of the boundary the material sat on.

## Why It Is Easy To Get Wrong

The failure mode is not "no evidence found". It is **evidence that looks real but is not user-authored**.

An auto-generated compaction summary recaps the pre-boundary conversation. It therefore *contains the target vocabulary* — often the exact concept names being searched for. A phrase query hits it. A careless worker reads those hits as support and proposes anchors over what is actually machine-written recap text.

Both affected packets avoided this because the workers checked producer role and turn provenance rather than trusting a text match. That should not be left to worker diligence.

## Impact On Retrofit

- **Nomination signals do not detect it.** `--user-contains` matches summary text. Git dates say when content was committed, not whether the authoring turns survived compaction.
- **Proven authorship does not transfer.** A session that grounded 25 lines in one pass is not thereby a good candidate for another cluster. Authority is per-boundary, not per-session.
- **Cost is a full packet.** Detection currently happens only after a worker has loaded and searched the transcript — roughly 6–10 minutes and a full worker context per wasted dispatch.
- **Silent scope loss.** Material authored before a boundary and never re-discussed afterward may be unreachable in *every* candidate session, making some lines permanently ungroundable for reasons unrelated to whether the user touched them.

## Mitigation (in use)

Cheap pre-dispatch check. Compare the session's earliest indexed turn against the target's authoring window:

```sh
agentos chatlas turns query --identity-hash <session> --sort oldest --limit 1 --json
```

If the earliest indexed turn postdates the target's introduction commit, **do not dispatch** — the packet cannot succeed. Go to the fallback session first.

Applied successfully after the `P4` failure: fallback `9d194db7f404` was checked before dispatch (earliest indexed turn 2026-06-26, running to 2026-07-10) and confirmed to span the 2026-07-05 authoring commit.

Cost of the check: one query, a few seconds. Cost of skipping it: an entire wasted packet.

## Secondary Rule

Text inside an auto-generated compaction summary is **never** support. It is machine-written recap, not a `User.Turn`, and carries no `Touch.Authority`. Worker packets in this campaign now state this explicitly.

## Open Questions

Not investigated — parked here rather than guessed at:

1. **Can Chatlas recover pre-boundary turns?** The raw provider artifact may still hold them even though the session model does not index them. If recoverable, this issue mostly dissolves.
2. **Should the boundary be queryable as session metadata?** A `compaction_boundary_at` field on the session index row would let a supervisor filter candidates mechanically instead of probing with an oldest-turn query.
3. **Should the retrofit survey pass do this automatically?** The check is cheap enough to run for every nominated session during survey, turning a per-dispatch discipline into a structural guarantee.
4. **How much of the corpus is affected?** Unknown. If `/compact` continuation is common in this dataset, the reachable grounding surface is meaningfully smaller than the ungrounded-line count suggests.

## Related

- `notes/live/611-agentos-pkg-grounding-campaign.md` — campaign report; the `Grounding.Log` entries for passes 2 and 4 carry the primary evidence
- `tarav-pkg` `references/index-retrofit.md` — supervisor contract (survey pass, session nomination)
- `tarav-pkg` `references/index-retrofit-worker.md` — worker contract (support requirements)
- separate but adjacent finding from the same campaign: some index vocabulary appears in **zero** user turns corpus-wide and may be agent-authored, which is a different reason for unreachable grounding than this one
