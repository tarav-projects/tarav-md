# Concept Discovery

`Concept.Discovery` is the subject prior-art move of a `What.Design.Session`: before inventing concepts, find what the owning index already says about the subject and its neighbors.

It is run during `Design.Session.Setup` and again whenever the session opens a **new subject block**. Its job is to keep design grounded in existing `Named.Concepts` instead of reinventing or silently contradicting them.

This reference leans on `[Cited.Duplication, Inline.Relatedness, Natural.Placement, Grounding.DRIFT]` from `agentos-pkg/design/`. The origin owns authority.

## Distinction — subject prior-art vs the process floor

Two different things load at session start; do not conflate them:

- **Process floor (Axis 1)** — the design *workflow* concepts: `Kernel.Writing`, `Design.Block`, `Natural.Placement`, etc. Loaded once via the Minimal Runtime / `writing-craft.md`. Concept-agnostic; true for every session.
- **Subject prior-art (Axis 2, this file)** — the existing index concepts about *this specific subject*. Discovered fresh per session and per new subject block.

`Concept.Discovery` is only the second. The first is already covered by the Minimal Runtime.

## When To Run

- inside `Design.Session.Setup`, once the subject is known
- again each time a new subject block is opened mid-session
- skip re-running for a subject already discovered this session

## Procedure

1. **Locate the owning index.** Identify which project owns the subject's concepts. Use the target project's `AGENTS.md` routing, then its `skills/agentos-pkg/design/` and `appendix/` (or the project's own index surfaces). Load `agentos-index` if the ownership or structure is unclear.

2. **Build probes.** Derive search terms from the subject:
   - the exact concept name and its `Dotted.Name` tokens
   - likely synonyms and user-facing phrasing
   - named neighbor concepts the subject couples to

3. **Search.** Prefer a few high-signal probes over broad noisy recall:

   ```sh
   rg -n "Subject.Name|token|neighbor" <project>/skills/agentos-pkg/design <project>/skills/agentos-pkg/appendix
   ```

   Failed search is not proof the concept is absent — widen probes once, then report.

4. **Classify each hit:**
   - **exists** — a block already defines this concept. Do not create a parallel block. Revise it, or mark `Grounding.DRIFT` if current work contradicts it.
   - **neighbor** — a related block the new work couples to. Cite it via `Inline.Relatedness` / `Cited.Duplication`; do not duplicate its content uncited.
   - **none** — no match. A new block is justified, but record the adjacent vocabulary found so the new block aligns with existing naming.

5. **Load relevant hits as `Cited.Duplication`** into the working context, so the design is written against what exists, not from memory.

6. **Surface to the user** before designing further (see Output Shape).

## Output Shape

A short report, not a dump:

```txt
Concept.Discovery — <subject>
- exists: [Concept.Name] — already defined; propose revise / DRIFT
- neighbors: [Concept.A], [Concept.B] — will cite
- new: no existing block; adjacent vocabulary: <terms>
Proposed anchors: [Concept.Name], [Concept.A]
```

Then ask the framing question: revise an existing block, branch a new one, or cite-and-extend?

## Boundaries

- `Concept.Discovery` finds prior art; it does not decide stable index wording or write the index.
- It does not replace the Minimal Runtime — that floor still loads regardless.
- Absence of hits is a reportable result, not a license to assume novelty.
