# agentos-index --type

Use this module when the caller wants line typing understood, read, or proposed: classifying `Kernel.Line`s with the `Line.Type.Vocabulary`.

This module is `Workflow.Neutral`: it is a cited surface explaining how to make and read proper index line typing. It runs no workflow and mutates no file — typing lands on the index only through the `--edit` path and its gates.

Authority lives in the index: `Line.Type`, `Line.Type.Vocabulary`, and the `Line.Type:*` blocks in `agentos-pkg/design/` own the concepts. This file is operating guidance over them.

## Syntax

- a typed line carries a leading bracketed code: `- [CT] the anchor token stays small`
- the type is read first and primes the line; the tail stays free for `Inline.Grounding` anchors
- the definition first line of a block is explicitly typed `[DF]`
- untyped lines are mechanically detectable (no leading bracket) — pre-fence legacy, worked down by calibration passes

## The Vocabulary

Eight starting types, sorted by their verb on the `Design.Space`. One-line reminders — the `Line.Type:XX` blocks are the authority:

| verb | type | act |
|---|---|---|
| define | `DF` | fixes what a name means |
| collapse | `DC` | pins a `Design.Variable` to a value |
| collapse | `CT` | bounds a variable to a subset without picking |
| collapse | `RJ` | excludes a considered alternative |
| orient | `PR` | generative orientation across variables |
| open | `FR` | explicitly declares a variable agent-owned |
| witness | `EX` | illustrates another line's claim with a concrete case |
| cite | `GR` | accounts what an anchored evidence neighborhood grounds, anchor trailing |

The vocabulary is soft and extensible (`Concept.Hardness`) — but extension is an index edit, not a call this module makes.

## Reading Typed Lines

The type tells the agent how to obey the line:

- `[CT]` bounds your choices; `[DC]` fixes one; `[RJ]` forbids re-proposing the excluded alternative
- `[PR]` orients decisions and breaks ties across variables
- `[FR]` grants explicit freedom — decide yourself, coherently, provisionally
- `[DF]` and `[EX]` inform: they fix vocabulary and witness claims, they do not bind action

Reading a typed block is loading a small constraint system: derive what you are bound by and what you are free in from the types, not from prose interpretation.

## Proposing Types

When drafting or reviewing a line's type:

- every type creates a validation point: the line must perform its act — a `[CT]` must exclude something, a `[DC]` must pin something, an `[EX]` must illustrate a specific claim
- a typed line that performs nothing is mistyped filler; check the validation point in the relevant `Line.Type:XX` block before proposing
- a `[PR]` scoped to a single variable is a `[CT]`
- type proposals on index content are index edits — `Edit.Trigger.Gated`, `Content.Verbatim.Gated`; propose, never self-write

## The Fence And The Residue

- the vocabulary is the fence of the index: index content is what the vocabulary can express
- a line that can take no type is not a classification failure — it is content that belongs elsewhere (appendix example, reference file, chat, agendix)
- calibration: type existing blocks and collect the residue — each untypeable line is a discussion: out of the index, or extend the vocabulary
- report residue explicitly; never force a type to make a line fit

## Semantic Lints

Typed lines make these agent-checkable — report them when noticed, route fixes through `--edit`:

- two `[DC]` lines pinning the same variable to different values
- `[CT]` constraints whose intersection is empty, or a `[CT]` silently violated by a later `[DC]`
- a `[RJ]`-rejected alternative later reintroduced without a new touch
- a `[FR]` freedom later constrained without retiring the declaration
- an `[EX]` inconsistent with the claims it illustrates
- a block whose first line is not a `[DF]`
