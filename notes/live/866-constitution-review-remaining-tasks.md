# Constitution review — remaining work and extracted notes

Status: discussion backlog, not approved amendments or an implementation request.
Date: 2026-10-18.

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

This live note preserves the remaining review tasks and editorial notes removed
from the Constitution, as requested by the User.
<!-- tarav.breadcrumb 2b08e3f9d71b -->

## Context

This note continues the Constitution review in Codex session
`01a1176b-f14c-7fd0-a97c-b22279c3f8c8` (Chatlas identity
`473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f`).
The Constitution is an operational alignment tool: audits surface mismatches;
resolving them may change a product or the Constitution. Audits do not choose.
The maintained [Constitution](../../skills/tarav-pkg/CONSTITUTION.md) is compiled
from [SKW source](../../skills/tarav-pkg/.skw/src/CONSTITUTION.skw.json).
Removing editorial notes does not resolve their open questions or change the
remaining constitutional commitments.

## Remaining tasks

1. **Apply the agreed contextualization amendment (original task 10).**
   The User accepted: “Tarav must provide extensible capabilities for discovering,
   selecting, and presenting context to users and agents, with navigable paths to
   available supporting material.” The current Constitution still ties this to
   Diagram Records. Apply the accepted wording in a separate amendment and ground
   it in the acceptance turn. Generation Context was explicitly removed; do not
   restore it as part of this task.

2. **Review the Collaboration Loop section.** The extracted note questions its
   specificity. The current linear sequence passes through Archive and Diagram;
   consider whether it should remain a constitutional commitment or become a
   workflow illustration. No replacement or deletion has been agreed.

3. **Finish reviewing Archive capabilities (original tasks 6–7).** The broader
   idea is evidence collection, progressive digestion into cheaper representations,
   and maintainable references, including DOI-like indirection and chains of
   representatives. Typed reference contracts, change detection, immutable
   Artifacts, mutable Records, and explicit substitution have already been amended.
   Preserve those decisions. The placement of remaining detailed Archive rules
   and the larger progressive-digestion design still need discussion; neither
   implementation nor wholesale relocation has been authorized.

4. **General SKW Markdown block boundary rule (task 13).** The User wants no block
   spanning multiple level-0 or level-1 (`#` or `##`) sections; smaller blocks are
   allowed. The Constitution's 18 blocks already fit. General authoring guidance
   and validation remain to implement. This is a SKW modeling rule, not a
   constitutional requirement.

5. **Specialized SKW document Types (task 14).** Captured as an open idea in the
   [Skillware wiki](../wiki/skillware.md#specialized-document-types--idea-for-later-design):
   a skill document could distinguish description and metadata from instruction
   blocks. Exact Types and enforcement remain open; no implementation requested.

6. **System Project location (task 16).** The User's earlier note proposed
   `~/Documents/tarav/` instead of `~/Documents/tarav/system/`. The last discussion
   asked whether this Project should coordinate the whole data depot while child
   stores retain independent storage and Git histories. That question is unanswered.
   Inspect `tarav-py/src/tarav/l3/project/system.py` and current project/harness
   behavior before proposing a migration. Do not infer a single repository.

7. **Derived Chatlas Markdown view for Obsidian (task 17).** The original root
   `050-TODOS.md` requests a maintained Markdown view of chat sessions. Treat it
   as derived output over retained Chatlas evidence. Selection, layout, refresh,
   and integration with Obsidian have not been designed. Recheck ongoing Chatlas
   work before planning it; this note is not authorization to implement it.

## Already addressed — do not reopen from stale notes

- Purpose now describes an external collaboration harness and an extensible
  Python library; Projects are fundamental.
- Original Constitution discussions were recovered and Breadcrumbs added.
- The Constitution and skill entry point were split into section blocks.
- Validation's nonblocking commitment is specific to user-data capture, with
  simpler/raw-data fallbacks.
- Evolvability and migration friendliness are explicit; committed Git history
  plus retained work conversations suffice by default.
- Diagram now provides expressive, navigable, queryable relationships;
  specialized workflows own their grounding requirements.
- Checks are a capability; detailed POI mechanics and mandatory scoring were
  removed. Generation provenance was removed from the Constitution.
- `tarav-pkg --constitution --audit --project <path>` reports misalignments in chat.
- Short Breadcrumb labels were tracked separately in product request 918 and
  subsequently implemented by another session; do not treat that as pending here.

## Original notes extracted verbatim

These preserve the User's wording before cleanup. Some are stale or partly
resolved; the status above distinguishes that from genuinely remaining work.

### Source block: `introduction`

```text
[TODOS
- This constitution is TOO diagram heavy. Its fine, but we most revisit it.
- We should go back and find the chats where we discussed the constitution.
And add breadcrumbs
- The skw file of the constitution is a single block
- lets at least split it by sections
    - I mean, for avoiding this to happend on another files
    - we might introduce a minimal block granularity on markdown files
    - for instance, we can not have blocks encaptuling more than on l0 and l1 header sections
]
```

### Source block: `purpose`

```text
[NOTE We need to expand this to add the harnessing part. ]
```

### Source block: `collaboration-loop`

```text
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]
```

### Source block: `tarav-archive`

```text
[NOTE
    This have happended to not be the case.
    It is an aim... but it is not still there.
    Again, what we are planing for Tarav is a set of workflows that provides an expectrum of capabilities.
    The archive system will just be an evidence recolector system.
    It will encaptulate that deam of tarav of progreive digestion.
    We have the raw data, and we extract liter representation of it, so we can conserve it longer and cheaper.
    WHICH, in turns, makes its references more stable.
    I mean, we try to make the references robut not by forcing and dealing aroung immutability.
    But with maintainable and recoverable systems.
    For instance, the DOI system.
    We issue an id, and the archive now have the freedom of maintaning the deeper links...
    Including substitutes or a chain of representatives.
    This way we can scale as necessary the detail chain.

    Also, this is too specific for a CONSTITUTION.
    Propuse move out.
]
```

### Source block: `contextualization`

```text
[NOTE
    Better generality, but we most revisit.
]
```
