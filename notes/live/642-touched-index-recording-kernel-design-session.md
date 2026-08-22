# Touched.Index Recording Kernel - design-session

## Session.Abstract

- **topic** — define `Touched.Index` as a user-scoped, addressable sequence of context-attached records that curate atomic changes to semantic blocks over immutable Chatlas conversations
- **settled frame** — canonical `Index.Record`s live in Bloberia; each record has a producer context, operation, line or block targets, support, and assertions, while blocks and lines remain independently addressable derived objects
- **integration frame** — projects remain ordinary `Product.Surface`s whose prose, skills, documentation, and code may query or depend on the user Index through SKW and POI feedback
- **prior-design input** — preserve still-useful constraints from the Chat/Project lifecycle, Index curation, Tarav2 record/linter, real-time backpropagation, and Bloberia reimplementations without importing their superseded ownership model
- **active concern** — implement the generalized record algebra against the current `LineRecord`, Capture.Manifest, linter, Chatlas context, and SKW realizations without importing the superseded multi-surface model
- **next useful move** — derive the smallest executable schema for context-attached records, operation-aware support projections, and line/block identity, then exercise it against the accumulated usage scenarios

## Design.Index

### Touched.Index.Recording.Model

- [DF] `Touched.Index` is a maintained sequence of context-attached `Index.Record`s that describe atomic changes to semantic blocks over selected `User.Touched` material on immutable `Chat.Surface`s. ^c20260821-169u
- [DC] the canonical Index records live at machine-user scope beside the user-scoped Chatlas evidence they address. ^c20260821-75u
- [CT] honest indexing means faithfully representing what the user touched, not certifying factual truth, currentness, acceptance, or implementation state. ^c20260821-76u
- [DC] the recording kernel owns records, capture, grounding, addressing, citation, Isoline and Isoblock membership, assertions, fidelity checks, projections, and direct reading. ^c20260821-170u
- [RJ] project HEAD, issues, design projects, and workflow-specific organization are not responsibilities of the recording kernel. ^c20260821-78u
- [PR] the Index stays composable by performing only the fundamental work shared by direct readers and more sophisticated consumers. ^c20260821-79u
- [CT] the chats are immutable and append-only source material, while the Index is a maintained `WIP.Surface` that agents continuously amend and prune. ^c20260821-137u

### Index.Record

- [DF] an `Index.Record` is the minimum serialized Index mutation, attached to the `Turn.Context` in which its operation was produced. ^c20260821-171u
- [DC] one complete record carries immutable `Record.Id`, `Record.Context`, `Record.Operation`, addressed targets, `Support.Set`, and opaque assertions. ^c20260821-172u
- [CT] every semantic record targets at least one `Index.Line` or `Index.Block`; when neither object changes, no record is emitted. ^c20260821-173u
- [CT] every semantic record carries a nonempty qualifying `Support.Set` grounding the exact operation it performs. ^c20260821-174u
- [CT] records form a maintained event-like surface rather than an immutable event store; `Bad.Indexing` records may be amended or purged. ^c20260821-175u

### Block.Change

- [DF] a `Block.Change` is the semantic result of one or more related `Index.Record` operations affecting one `Index.Block`. ^c20260821-176u
- [DC] the ordered record sequence serializes the evolution of `Block.Change`s across chats. ^c20260821-177u
- [CT] every `Block.Change` contains at least one line or block operation; a change with neither is a no-op and produces no Index material. ^c20260821-178u
- [CT] one capture act may emit several records that compose one `Block.Change` without making the capture workflow transactional. ^c20260821-179u
- [DC] the current block projection is derived by folding the surviving applicable records rather than accepted as an agent-set state flag. ^c20260821-180u

### Index.Block

- [DF] an `Index.Block` is the minimum self-interpreting semantic unit of `Touched.Index`. ^c20260821-181u
- [DC] a block's content is defined by the `Index.Line`s currently attached to it. ^c20260821-182u
- [CT] an `Index.Line` is interpreted within the semantic frame supplied by its block. ^c20260821-183u
- [PR] `Kernel.Writing` keeps sibling lines as orthogonal and atomic as possible inside that shared semantic frame. ^c20260821-184u
- [DC] `Block.Create` creates an addressable `Block.Id`, initial name, and Isoblock membership; its content arrives through line operations. ^c20260821-185u
- [CT] the block name is the only directly editable block property in the current design. ^c20260821-186u

### Index.Capture

- [DF] `Index.Capture` is the operation that emits grounded `Index.Record`s from one producer `Record.Context` onto `Index.Primary.Surface`. ^c20260821-187u
- [DC] capture expresses one or more `Block.Change`s through a small vocabulary of line and block operations. ^c20260821-188u
- [CT] a `Line.Capture` operation must derive both its exact wording and block assignment from the producer `Agent.Context`. ^c20260821-189u
- [CT] self-chat and external-chat capture are derived from context and support relationships rather than selected as distinct workflow modes. ^c20260821-190u
- [CT] capture may also maintain an `Index.Secondary.Surface`, but secondary materialization is not required for the canonical record to exist. ^c20260821-167u

### Index.Capture.Profile

- [DF] an `Index.Capture.Profile` selects which touched material qualifies for capture into one Index. ^c20260821-80u
- [DC] `Line.Type` currently supplies the default capture vocabulary and therefore acts as part of the capture prompt. ^c20260821-81u
- [FR] applications and activated workflows may extend the capture profile or maintain additional Indexes without changing the recording kernel. ^c20260821-82u

### Index.Line

- [DF] an `Index.Line` is the minimum addressable and capturable Index unit; its exact wording is interpreted through its `Index.Block`. ^c20260821-191u
- [DC] every line is attached to a block by grounded record operations; an unscoped line is `Bad.Indexing`. ^c20260821-192u
- [CT] line wording performs one typed `Kernel.Writing` act and aims to remain orthogonal to sibling lines. ^c20260821-193u
- [DC] the line label is its public citation, `Line.Id` identifies the exact wording object, and `Isoline.Id` identifies its asserted semantic-equivalence class. ^c20260821-194u
- [CT] project relevance is not intrinsic to an `Index.Line`; several projects or consumers may use the same line independently. ^c20260821-87u

### Turn.Context

- [DF] `Turn.Context` is Chatlas's addressed reconstruction of contextual state at one turn horizon from the chat Normal Model. ^c20260821-195u
- [DC] one chat identity and horizon turn address the context without copying its material into the Index record. ^c20260821-196u
- [CT] a `Turn.Context` exposes distinct `Agent.Context` and `Visible.Context` projections rather than treating chat prefix and agent input as identical. ^c20260821-197u

### Agent.Context

- [DF] `Agent.Context` is the reconstructable material supplied to the agent at one `Turn.Context`, including applicable chat, loaded Index blocks, files, tool results, instructions, and summaries. ^c20260821-198u
- [RJ] internal attention, hidden reasoning, and other unreconstructable model state are not `Agent.Context`. ^c20260821-199u
- [CT] compaction and private runtime inputs mean `Agent.Context` need not equal or contain the whole `Visible.Context`. ^c20260821-200u

### Visible.Context

- [DF] `Visible.Context` is the portion of a `Chat.Surface` visible at one turn horizon and serves as a proxy for `User.Context`. ^c20260821-201u
- [CT] `Visible.Context` supports assertions about what was visible in the conversation, not claims about everything the user knew. ^c20260821-202u
- [CT] user-visible history may exceed compacted `Agent.Context`, while agent-only inputs may exceed `Visible.Context`; neither projection generally contains the other. ^c20260821-203u

### Record.Context

- [DF] `Record.Context` is the producer `Turn.Context` to which one `Index.Record` is chronologically attached. ^c20260821-204u
- [DC] record attachment identifies where the Index operation was generated rather than where its supporting touched material originated. ^c20260821-205u
- [CT] the record operation, payload, and target assignments must be auditable from its producer `Agent.Context`. ^c20260821-206u
- [CT] an external source used by a record must enter the producer `Agent.Context` through a reconstructable addressed read or projection. ^c20260821-207u
- [CT] touched authority remains in `Support.Set`; `Record.Context` supplies production provenance and derivation bounds. ^c20260821-208u

### Support.Set

- [DF] a `Support.Set` is the set of touched conversational neighborhoods attached to one `Index.Record` and grounding the exact operation that record performs. ^c20260821-209u
- [RJ] support is not recruited to certify a pre-existing conclusion; the addressed `User.Touched` material is what the record indexes through its operation. ^c20260821-210u
- [DC] one `Support.Set` may span many turns and chats while preserving the exact address and validation hash of every referenced message. ^c20260821-97u
- [CT] every support neighborhood belongs to a source chat's `Visible.Context`, but it need not belong to the writing chat's `Visible.Context`. ^c20260821-211u
- [CT] record support grounds only the operation-defined relationship; it does not automatically support every property of the record's targets. ^c20260821-212u
- [CT] a capture instruction or landing approval is a gate assertion rather than substitute substantive support. ^c20260821-213u

### Evidence.Neighborhood

- [DF] an `Evidence.Neighborhood` is one declared conversational reading unit inside a `Support.Set`, combining grounding user turns with the contextual agent turns needed to interpret them. ^c20260821-100u
- [CT] grounding user turns carry `User.Touch`; contextual agent turns provide referents or reasoning context without independently acquiring touched authority. ^c20260821-101u
- [PR] the capturer records the minimum sufficient neighborhood so later tools can render useful evidence without repeating the semantic reconstruction. ^c20260821-102u
- [FR] readers may search around a declared neighborhood when interpretation remains unclear, while expanded context stays exploratory until the `Support.Set` is amended. ^c20260821-103u

### Index.Support.Projection

- [DF] `Index.Support.Projection` derives content, placement, and aggregate support from the semantics of grounded record operations. ^c20260821-214u
- [DC] `Line.Support` is the union of `Line.Capture` and `Support.Add` support targeting that exact `Line.Id`. ^c20260821-215u
- [DC] `Isoline.Support` is the union of `Line.Support` across the equivalent lines in one `Index.Isoline`. ^c20260821-216u
- [DC] `Block.Support` is the union of `Isoline.Support` for the lines attached to one `Index.Block`. ^c20260821-217u
- [CT] `Line.Reblock` support grounds the placement change and does not automatically strengthen support for the line wording. ^c20260821-218u
- [CT] support aggregation deduplicates identical evidence neighborhoods while the contributing records preserve when and where each contribution occurred. ^c20260821-219u

### Index.Isoline

- [DF] an `Index.Isoline` groups exact `Index.Line`s asserted to be semantically equivalent. ^c20260821-220u
- [DC] changed wording remains in one Isoline only when semantic equivalence holds; a semantic change uses another Isoline. ^c20260821-221u
- [DC] `Support.Add` targets an exact `Line.Id`, forcing the agent to identify the precise wording being supported. ^c20260821-222u
- [CT] retaining an Isoline during `Line.Reblock` asserts that the placement change preserves the line semantics. ^c20260821-223u
- [CT] changing both block placement and Isoline membership is a distinct semantic reinterpretation operation. ^c20260821-224u
- [CT] an Isoline accumulates a collection of addressed member contexts rather than merging them into one synthetic context. ^c20260821-225u

### Index.Isoblock

- [DF] an `Index.Isoblock` groups block records or editions asserted to preserve one semantic frame. ^c20260821-226u
- [CT] a name-only `Block.Rename` remains in one Isoblock when the block frame stays semantically equivalent. ^c20260821-227u
- [CT] a genuine block reframing uses another Isoblock rather than presenting the change as a rename. ^c20260821-228u

### Index.Record.Operation

- [DF] an `Index.Record.Operation` is a small kernel verb describing the exact line or block mutation performed by one record. ^c20260821-229u
- [DC] `Block.Create` creates `Block.Id`, initial name, and Isoblock membership; the block content remains derived from attached lines. ^c20260821-230u
- [DC] `Block.Rename` changes the name of an exact block without directly editing its line-defined content. ^c20260821-231u
- [DC] `Line.Capture` creates an exact line wording, assigns its block and Isoline, and grounds those choices from the producer context and record support. ^c20260821-232u
- [DC] `Support.Add` contributes another support neighborhood to an exact existing line without creating a wording edition. ^c20260821-233u
- [DC] `Line.Reblock` records a later grounded placement decision without rewriting the line's earlier capture record or context. ^c20260821-234u
- [FR] additional record verbs enter the kernel only when usage scenarios demonstrate a fundamental mutation that the current set cannot express. ^c20260821-235u

### Index.Record.Assertion

- [DF] an `Index.Record.Assertion` is an opaque object retained on an Index record for machinery that understands its meaning. ^c20260821-108u
- [DC] the recording kernel preserves assertions losslessly without defining a general assertion format or scoring semantic assertions. ^c20260821-109u
- [DC] the rendered `Line.Type` is surface sugar for a typed assertion retained on the record. ^c20260821-110u
- [DF] an Index gate is a mechanically evaluated assertion whose token and addressed turns let the linter verify the protocol event. ^c20260821-111u
- [CT] known mechanical assertions may be linted now while semantic assertion machinery remains deferred. ^c20260821-112u
- [CT] a record's `Support.Set` grounds its operation independently from the evidence or evaluation mechanics of opaque assertions. ^c20260821-236u
- [FR] contextual justification of line wording, block assignment, Isoline membership, and external-source inclusion may later become mechanically evaluated assertions. ^c20260821-237u

### Bad.Indexing

- [DF] `Bad.Indexing` is a fidelity POI raised when Index material fails to index qualifying touched data honestly through the recording kernel's invariants. ^c20260821-114u
- [EX] missing grounding, unrelated support, mistyping, missing block attachment, invalid grouping, duplication, and incorrect extraction are forms of `Bad.Indexing`. ^c20260821-115u
- [CT] the Index is a `WIP.Surface`, so problematic states may exist temporarily while remaining visible as POIs. ^c20260821-116u
- [FR] a `Bad.Indexing` POI prescribes attention rather than a remedy; maintenance may ground, amend, regroup, replace, or remove the material. ^c20260821-117u
- [DC] corrupted Index material is eventually amended or purged rather than preserved as semantic history. ^c20260821-118u
- [CT] an operation unsupported by its own `Record.Context` or `Support.Set` is `Bad.Indexing`, even when a later context could support the same resulting projection. ^c20260821-238u
- [CT] legitimate semantic evolution preserves the earlier grounded record and emits a later record; correction may prune an earlier record that was never honestly grounded. ^c20260821-239u

### Index.Consumer

- [DF] an `Index.Consumer` reads addressed records, blocks, lines, Isolines, Isoblocks, support, and assertions for one purpose without changing the recording kernel's semantics. ^c20260821-240u
- [DC] agents may consume the Index directly; optional tooling improves navigation, synthesis, and maintenance without making the base Index unusable. ^c20260821-120u
- [DC] a renderer may assemble record history, current block projections, Isoline members, declared support neighborhoods, assertions, and linter verdicts as derived inspection material. ^c20260821-241u
- [CT] a renderer or semantic engine creates no new authority merely by reorganizing Index records. ^c20260821-122u

### Index.Primary.Surface

- [DF] `Index.Primary.Surface` is the canonical collection of complete `Index.Record`s stored in the user-scoped Bloberia depot. ^c20260821-242u
- [DC] the records are the maintained source of Index identity, operations, context, support, assertions, and derived line and block state. ^c20260821-243u
- [RJ] no Chat, Markdown, project, or other parallel Index surface is required by the current model. ^c20260821-150u
- [CT] because records and their components are addressable, consumers can cite an Index object and follow it to the touched material in its `Support.Set`. ^c20260821-151u

### Index.Secondary.Surface

- [DF] an `Index.Secondary.Surface` is a noncanonical surface that claims to render or materialize Index objects or projections from canonical `Index.Record`s. ^c20260821-244u
- [DC] every rendered line on an `Index.Secondary.Surface` must resolve to the records from which its exact wording and current relationships are projected. ^c20260821-245u
- [CT] a secondary line without a canonical record must be captured into the Index or surfaced as a reconciliation POI. ^c20260821-154u
- [CT] stale or divergent secondary material raises a POI against its canonical record rather than becoming another source of Index authority. ^c20260821-155u
- [CT] ordinary derived project prose is not an `Index.Secondary.Surface` unless it claims to render or materialize `Index.Line`s. ^c20260821-156u

### Project.Index.Grounding

- [DF] `Project.Index.Grounding` is the use of Index queries to discover user-scoped material relevant to the project surfaces an agent is maintaining. ^c20260821-157u
- [DC] the project's current model is expressed through normal prose, skills, documentation, code, and other maintained product surfaces rather than an Index-shaped HEAD. ^c20260821-124u
- [DC] SKW annotations ground project surfaces to addressed Index records, blocks, lines, Isolines, or Isoblocks and may raise drift POIs when those dependencies change. ^c20260821-246u
- [DC] agents may query the Index for newly touched material related to the product surfaces they are maintaining. ^c20260821-126u
- [CT] project association is derived from consumer relationships and conversational context rather than stored as an intrinsic line property. ^c20260821-127u
- [DC] collaboration and cross-machine portability are explicitly deferred while the implementation targets one user on one computer. ^c20260821-128u

### Index.Implementation.Kernel

- [DF] `Index.Implementation.Kernel` is the minimal executable machinery that records, resolves, evaluates, and projects the user-scoped Index primitives. ^c20260821-129u
- [DC] one user-side Bloberia depot stores every complete Index record as consumer-owned opaque cargo keyed by immutable record identity. ^c20260821-130u
- [CT] public labels remain mutable selectors and therefore cannot be storage identity. ^c20260821-131u
- [DC] exact chat identity, horizon turns, context-import addresses, message coordinates, and validation hashes keep record production and support mechanically auditable without copying Chatlas content into the Index. ^c20260821-247u
- [PR] any standing or verdict that machinery can derive from records, assertions, Chatlas, or product-surface presence is computed rather than accepted as an agent-set flag. ^c20260821-133u
- [DC] linter evaluation distinguishes passed, failed, and blocked so unavailable evidence is never reported as clean. ^c20260821-134u
- [CT] POI-driven reconciliation tolerates temporary cross-surface incoherence without imposing one transactional authoring workflow. ^c20260821-135u
- [DF] the Index linter checks canonical records, derived projections, and declared secondary surfaces against structural and grounding invariants, then surfaces conformance failures as POIs. ^c20260821-248u
- [PR] linter findings guide agent maintenance without prescribing whether a problem is amended, recaptured, regrouped, or removed. ^c20260821-161u
- [CT] the linter can verify nonempty support, exact addresses, chronology, target existence, operation shape, context inclusion, duplicate operations, and no-ops without claiming semantic truth. ^c20260821-249u

### Usage.Scenario

- [DF] a `Usage.Scenario` is a grounded simulation used to stress the record model through a given state, operation, emitted records, expected projection, and expected POIs. ^c20260822-0u
- [DC] the Design.Session accumulates self-chat capture, external capture, support addition, block evolution, line reblocking, and Bad.Indexing correction as its initial scenario suite. ^c20260822-1u

### Usage.Scenario::Self.Chat.Capture

- [DF] `Usage.Scenario::Self.Chat.Capture` exercises a record whose producer context and support neighborhoods belong to the same chat. ^c20260822-2u
- [EX] a `Line.Capture` attached to Chat A derives its wording and block from `Agent.Context(A)` and grounds its operation in neighborhoods from `Visible.Context(A)`. ^c20260822-3u
- [CT] self-chat validation checks that support is within the applicable chat horizon without making same-chat placement a universal capture requirement. ^c20260822-4u

### Usage.Scenario::External.Chat.Capture

- [DF] `Usage.Scenario::External.Chat.Capture` exercises a record produced in one chat from touched material originating in another chat. ^c20260822-5u
- [EX] a `Line.Capture` attached to Chat B may carry support from `Visible.Context(A)` when an addressed read of Chat A entered `Agent.Context(B)`. ^c20260822-6u
- [CT] the record cites Chat A directly as substantive support; a quotation copied into Chat B does not replace the original source address. ^c20260822-7u
- [CT] Chat B records the indexing act, Chat A retains touched-source provenance, and any Chat B capture instruction remains a separate gate assertion. ^c20260822-8u
- [CT] if Chat A enters the agent context only after the Chat B horizon, the later inspection requires a later record and cannot retroactively justify the earlier one. ^c20260822-9u

### Usage.Scenario::Support.Add

- [DF] `Usage.Scenario::Support.Add` exercises explicit growth of the support accumulated around an exact line. ^c20260821-250u
- [EX] a later `Support.Add` record targets `Line.Id`, attaches to its own producer context, and carries the newly indexed evidence neighborhood in its record support. ^c20260821-251u
- [CT] the operation changes `Line.Support` without creating another wording edition or silently assigning support to every Isoline member. ^c20260821-252u

### Usage.Scenario::Block.Evolution

- [DF] `Usage.Scenario::Block.Evolution` exercises creation and name evolution of a line-defined semantic block. ^c20260821-253u
- [EX] `Block.Create` assigns `Block.Id`, initial name, and Isoblock membership, while accompanying line operations establish its content. ^c20260821-254u
- [EX] a later `Block.Rename` changes the exact block name without rewriting its attached lines. ^c20260821-255u
- [CT] retaining the Isoblock across a rename asserts an equivalent semantic frame; a genuine reframing creates or selects another Isoblock. ^c20260821-256u

### Usage.Scenario::Line.Reblock

- [DF] `Usage.Scenario::Line.Reblock` exercises a later grounded change to the block placement of an exact existing line. ^c20260821-257u
- [EX] a `Line.Reblock` record attached to a future context targets the exact line and destination block while leaving its earlier capture record unchanged. ^c20260821-258u
- [CT] retaining the Isoline asserts semantic equivalence across the move; changing Isoline membership represents a distinct semantic reinterpretation. ^c20260821-259u
- [CT] the reblock record requires support for the placement operation and cannot borrow justification from a prior context that supported only the earlier placement. ^c20260821-260u

### Usage.Scenario::Bad.Indexing.Correction

- [DF] `Usage.Scenario::Bad.Indexing.Correction` distinguishes curation of an invalid record from grounded evolution of a previously valid interpretation. ^c20260821-261u
- [EX] an original block placement unsupported by its own context may be amended or purged as Bad.Indexing. ^c20260821-262u
- [EX] an original placement supported by its context remains historical evidence when a later discussion emits a grounded reblock record. ^c20260821-263u
- [CT] both paths may yield the same current block projection, but only semantic evolution preserves the earlier record as legitimate indexed history. ^c20260821-264u

## Session.Notes

### Prior designs retained

- `607-chat-project-index-redesign-design-req.md` contributes the canonical Chat attachment, causal conversation horizon, orthogonality of home/support/provenance/project use, and eventual POI-driven reconciliation.
- `626-index-narrative-identity-design-req.md` contributes the core direction that chat history is what gets indexed under a semantic and the mechanical stress test that semantic identity must survive lexical change; the separate `Index.Narrative` object is not retained because `Index.Isoline` groups semantically equivalent exact lines.
- `629-index-curation-model-design-session.md` contributes `Bad.Indexing`, fidelity/completeness as maintained WIP concerns, and removal of corrupt interpretations; its Index-owned HEAD/Tail and multi-surface semantic ownership are not retained.
- `632` through `635` contribute complete addressable records, immutable record and lineage identities, surface-neutral attachment addresses, no agent-set standing flags, gates as checkable claims, three-valued verdicts, and dumb POI checks that never pretend to evaluate meaning.
- `628-hugentics-real-time-chat-index-backpropagation-impl-req.md` contributes exact current-chat references, chronological addressing, idempotent capture, and recoverable reconciliation gaps; its `Other.HEADs -> Chat.Index.HEAD` direction is superseded by canonical records plus optional secondary surfaces.
- `641-bloberia-record-store-impl-req.md` contributes the one user-side depot, opaque consumer-owned records, immutable-id sharding, scan-based public-label lookup, Git-backed recovery, and strict test isolation from the live corpus.

### Current implementation gaps

- `LineRecord` is the only canonical record shape today; the new model requires a general `Index.Record` envelope and operation payloads for both line and block mutations.
- `LineRecord.scope` currently names a Project block or SKW annotation point; the new model requires addressable `Index.Block`, `Index.Line`, Isoline, and Isoblock targets while treating project/product occurrences as consumer relationships.
- `PlacementRef` models one surface coordinate; the new model requires producer `Record.Context` backed by Chatlas `Turn.Context`, `Agent.Context`, and `Visible.Context` projections.
- current Chatlas context data does not yet expose a first-class reconstructable assertion that an external chat read entered one producer `Agent.Context`.
- `LineRecord.support` is stored as a flat tuple of qualifying user messages; the new record-owned `Support.Set` requires declared `Evidence.Neighborhood`s and operation-aware derived support.
- support updates currently rewrite the line record's support tuple; the new model emits `Support.Add` records targeting exact `Line.Id`.
- `Equivalence` and predecessor chaining are privileged schema fields today; the new model replaces trace terminology with Isoline and Isoblock membership while retaining optional relationship detail as opaque assertions.
- review and landing gates are dedicated record links today; the new model treats them as known mechanical assertions under the common assertion carrier.
- `Line.Type` currently lives inside the rendered line object; `Line.Capture` records must retain its assertion form while preserving `[TYPE]` as convenient surface syntax.
- current HEAD/Tail, agent/user standing, Chat.Index backpropagation, and HEAD-surface discovery belong to the superseded integrated model and must not remain responsibilities of the reduced recording kernel.
- current capture can only create or update line records from a Markdown or SKW source line; the new model must create general records directly, including block creation, rename, support addition, and reblock operations.
- current `record-placed` evaluation requires records to appear on another discovered surface; the new model instead checks canonical record integrity and only checks placement when a declared secondary surface exists.
- current SKW discovery treats annotated product lines as distributed Index materializations; the new model needs dependencies from ordinary product surfaces into the user Index without forcing those products to become secondary Index surfaces.
- current capture profiles, chapter policies, Issue.Block semantics, and semantic assertion scoring remain useful experiments or consumers rather than required kernel machinery.
- `Capture.Manifest` can ground explicit live-Markdown heading targets, but its mandatory Chat.Index projection and the general linter's placement model encode parallel surfaces that the new design no longer requires.

### Open implementation questions

- Choose the physical envelope and payload representation for `Index.Record` while keeping the kernel operation vocabulary small and extensible.
- Define how `Turn.Context` reconstructs agent inputs, visible chat, compaction, tool results, loaded files, and addressed external-chat reads from the Chatlas Normal Model.
- Define the smallest address vocabulary for record, block, line, Isoline, Isoblock, context horizon, evidence neighborhood, and secondary occurrence.
- Decide the exact operation that represents reblocking with changed Isoline membership rather than conflating semantic reinterpretation with equivalence-preserving `Line.Reblock`.
- Decide whether Isoblock groups immutable block editions, block identities, or both through a derived projection while only block names are directly editable.
- Define operation-aware support projection and determine which relationship assertions become mechanically lintable first.
- Decide how capture creates canonical records directly while optionally maintaining source prose as an `Index.Secondary.Surface`.
- Define the first direct-reader, record-history renderer, and Usage.Scenario runner before generalizing capture profiles or assertion schemas.
- Reconcile existing Chat.Index HEAD/Delta data and the 3,974-record Bloberia corpus through conservation-first migration rather than treating current projections as canonical placement.

### Explicitly deferred

- Cross-machine portability, collaboration, and export of user-scoped support.
- A general schema, type hierarchy, or scoring engine for semantic assertions.
- A universal project workflow, HEAD document format, Issue lifecycle, or Design.Project organization.
- Multiple capture profiles beyond preserving the extension point and the current `Line.Type` default.

## Session.Log

- **2026-08-21** — opened as a new Design.Session after the discussion deliberately reduced `Touched.Index` from an integrated project/current-design system to a user-scoped recording kernel with optional consumers.
- Gap-completed the current design against the latest Chat/Project lifecycle, narrative/curation, Tarav2 record/linter, real-time backpropagation, and Bloberia implementation generations; retained compatible constraints and named conflicting mechanics as implementation gaps.
- Captured 62 typed lines across 13 blocks through one current-session `Capture.Manifest`; 62 anchors and records were created, Chat.Index backpropagation completed, and the final exact-item audit reported no gaps.
- Bounded validation ran 20 applicable checks over the 62 new records: 19 passed and `record-placed` failed for all 62 because the linter does not discover the Design.Session surface; retained as an implementation POI rather than blessed or hidden.
- **2026-08-21** — revised the model after evaluation against the simpler mechanics: made Bloberia records the only primary Index surface, introduced optional `Index.Secondary.Surface`s, replaced turn attachment with horizon-addressed `Line.Context`, tightened trace membership to semantic equivalence, and named project use as `Project.Index.Grounding` through SKW.
- Captured 33 grounded revision lines in four bounded passes; every exact audit passed. The linter passed 19 of 20 checks and raised `Record.Unplaced` for every revision record because it still requires a separate discovered placement, directly witnessing the superseded multi-surface assumption.
- **2026-08-21** — generalized the kernel from line-attached records to context-attached `Index.Record`s, made block changes and block semantics explicit, introduced Agent/Visible/Record context, renamed trace to Isoline, added Isoblock and operation-aware record support, and accumulated grounded Usage.Scenarios for model stress testing.
- Captured 106 grounded revision lines across 29 blocks through one manifest; all source lines and records were present on the idempotent verification preview with no ungrounded Design.Index lines.
- Bounded validation examined the 106 revision records: 19 of 20 checks passed, while `record-placed` raised the already-modeled `Record.Unplaced` POI for every record because the current linter still requires a separate discovered surface.
