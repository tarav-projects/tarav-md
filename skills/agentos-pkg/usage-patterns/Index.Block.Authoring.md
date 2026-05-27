# Usage Pattern: Index.Block.Authoring

## Situation

The user proposes a concept and wants an index block. Or a discussion converges and the user says "make this into a kernel-block." The agent produces a complete proposal for user approval.

## Expected Behavior Path

1. The agent must be literate about the index system and `Kernel.Block:Index` conventions before proposing. If not already in context, load `agentos-index` and the relevant index references.
2. Check the routing table (`000-index.md`) for existing concepts that may overlap with the proposed one.
3. If overlap exists, show the related concepts to the user — not just "there's overlap" but what the existing concepts say. The user decides whether to merge, complement, cite, or create new.
4. If new, draft the block in `Kernel.Block:Index` dash-list format.
5. Present a complete proposal for approval:
    - Block content
    - Related existing concepts (with brief description of how they relate)
    - Target index page and placement rationale
    - Router update entry
6. The user approves or redirects. Writing happens after approval through normal index writing.

## Key Signals

- "propose an index block"
- "make this into a kernel-block"
- "write the blocks"
- Concept name in `Dotted.Notation`
- Discussion converges on a nameable idea

## Observed Friction (from test runs and sessions)

- **Agents skip the routing table check** — they propose a new block without checking what already exists. This leads to redundant or overlapping concepts.
- **Agents use prose format instead of dash-list** — the `Kernel.Block:Index` format is dash-list, not paragraphs with subsections. The agent must know the format before proposing.
- **Agents hallucinate related concepts** — instead of citing real existing concepts from the index, they invent plausible-sounding concept names. The agent must cite only concepts it actually found.
- **Agents assume the target index** — the target index page should be part of the proposal with a rationale, not an assumption.

## Related Patterns

- `Package.Skill.Bootstrap` — index blocks are often authored during or after a bootstrap
- `Package.Skill.Driver.Refinement` — driver improvements may surface new concepts that need blocks

## Source Sessions

- `019e5b0f` — Provider.Instance concept refinement
- `019e4c30` — multiple blocks during linter design
- `258b002c` — PaperSON blocks during design session
- `ac16fc98` — kernel blocks in external project context

## Existing Test

- `agentos-pkg/testing/agentos-pkg-driver-guidance-locality-01.md` — overlap trap test for this pattern
