# Git Grounding

`git-grounding` is the git-guided `Chat.Grounding` module: target one `Chat.Grounding.Target.Block`, use git history to find likely chat evidence, then discuss candidate grounding lines with the user until approved.

This module is for one-session grounding. It does not stop at `Chat.Grounding.Request`; it continues through `Chat.Grounding.Candidate.Review` and writes accepted grounding only after explicit user approval.

## Execution Mode

Run `git-grounding` inline in the caller conversation by default.

- candidate review is a human/agent discussion, so a separate mining agent cannot finish the workflow alone.
- a helper agent may gather read-only evidence, but the caller owns the review turn, approval, and file write.
- do not write stable index or appendix files until the user approves the exact candidate grounding line.

## Input

Required: one target block name or an unambiguous block reference.

If the caller gives a loose topic, first resolve it to a `Chat.Grounding.Target.Block`:

- find an existing `Kernel.Block:Index` or `Kernel.Block:Appendix`;
- if no block exists, stop and say grounding needs a block first;
- if the evidence belongs to a subtopic, propose creating or selecting a narrower block.

## Procedure

1. **Resolve the target block.**
   - locate the owning project/repository;
   - read the block, current `### grounding`, appendix/history if relevant, and line range;
   - identify user-language phrases, aliases, related concepts, and existing `*HEAD*` rows.

2. **Walk git history newest-first.**
   - use `git log -L <start>,<end>:<path>` when a stable line range exists;
   - collect commit hashes, commit dates, diff hunks, changed phrases, and nearby concept names;
   - treat git as a hint generator, not as grounding evidence by itself.

3. **Query Chatlas from git hints.**
   - prefer queries using changed concept names, distinctive phrases, renamed files, and the commit time window;
   - use `--active-after`, `--message-contains`, `--user-contains`, provider/project filters, and short high-signal probes;
   - do not treat a failed query as absence of grounding; widen once, then report.

4. **Inspect candidate chat neighborhoods.**
   - read `--view transcript` when assistant context is needed;
   - prioritize user turns under `Grounding.Hugentic.Authority`;
   - use assistant turns only as context unless the user accepts, corrects toward, or acts on them;
   - label unaccepted assistant-only evidence `ASSISTANT`.

5. **Choose the resolution shape.**
   - use a point ref when the landing turn itself is enough;
   - use a range ref when grounding depends on proposal, correction, discussion, or convergence;
   - use the shortest readable identity-hash prefix that resolves unambiguously;
   - follow `Chat.Grounding.Ref.Resolution`: the ref is a landing point, not a claim that one turn contains all evidence.

6. **Run one grounding review turn.**
   - expose one candidate at a time unless the user asks for a batch;
   - include the evidence, analysis, role, resolution shape, and candidate grounding line;
   - answer feedback by revising the candidate line, ref, role, or analysis;
   - wait for explicit approval before writing.

7. **Write approved grounding.**
   - insert or update the target block's `### grounding` section;
   - write only the approved candidate line;
   - place historical/superseded grounding in appendix history, not compressed index grounding;
   - run `Chat.Grounding.Head.Audit` when the new line appears to supersede existing heads or the block changed fundamentally.

8. **Report.**
   - print the target block, approved line count, files changed, and any deferred audit/history work.

## Grounding Review Turn

Use this shape for each candidate:

```md
### Evidence N
Ref: @short-hash-time[..time]
Role: *HEAD* | history | DRIFT | reject
Resolution: point | range | session/context

Evidence:
[short relevant excerpt or paraphrase]

Analysis:
- why this supports the current block shape
- whether nearby context contradicts it
- whether this should remain active or become history
- whether the evidence is user-grounded or must be labeled ASSISTANT

Candidate grounding line:
- *HEAD* @ref — evidence note written exactly as it would appear in `### grounding`
```

The candidate line is the review object. The user edits that line like a kernel block line: propose, feedback, revise, approve, then write.

## Candidate Line Rules

- explain the support relation, not merely a transcript summary.
- cite a `Chat.Ref` that lands a future reader near the relevant evidence neighborhood.
- use `*HEAD*` only when the evidence directly supports the current factual shape of the block.
- use history only when the evidence is retained for provenance but no longer supports the current block as written.
- use `DRIFT:` only when accepted active evidence indicates the block needs alignment discussion.
- add `ASSISTANT` when the cited support is assistant-authored and not explicitly accepted by the user.

## Commands

Resolve a block line range:

```sh
rg -n "^## <Block.Name>$|^\\*\\*\\*\\*$" <index-dir>
```

Walk block history:

```sh
git -C <repo> log --date=iso-strict --format='%H%x09%ad%x09%s' \
  -L <start>,<end>:<path>
```

Query likely sessions:

```sh
agentos chatlas query --message-contains "<phrase>" \
  --active-after "<iso>" --sort newest --limit 20
```

Read candidate evidence:

```sh
agentos chatlas views inline --ref "@<hash>-<time>..<time>" \
  --view transcript --format json
```

Validate a short ref before proposing it:

```sh
agentos chatlas views inline --ref "@<short-hash>-<time>" \
  --view transcript --format json >/tmp/chat-grounding-ref.json
```

## Boundaries

- do not create a grounding target for a loose topic; create or select a block first.
- do not use git commits as grounding evidence; git only points to likely chats.
- do not promote a `Chat.Grounding.Request` automatically; review the chat itself.
- do not write a candidate line without explicit user approval.
- do not collapse several candidates into one review turn unless the user asks for batching.
