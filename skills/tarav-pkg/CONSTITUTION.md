# Tarav Constitution

<!-- tarav.sessions
4720b13e = codex:01a02f8b-8c36-7123-ba70-1a217b776e28 @4720b13eeb5dc61cad2d999b24f45a78d9dcd776c77e0be98b68822e30fdb604
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

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

## Preamble

This document is the Constitution of Tarav.

It states the fundamental principles and boundaries of the Tarav system. Any surface claiming to be part of Tarav must comply with this Constitution.
<!-- tarav.breadcrumb c3bd772ca1caa09098602fc5400e3ca2c81ec7a65c003f7c5f43643f55180318 -->

The Constitution is intentionally general, incomplete, and amendable. It does not contain all Tarav design truth or require a single implementation.
<!-- tarav.breadcrumb ecd16660e190d6eb883bb1044daaa3183a253af95914bb564128d27d36d8c63f -->

When a Tarav design conflicts with the Constitution, the conflict must be surfaced. It can be resolved by changing the design, amending the Constitution, or changing both.
<!-- tarav.breadcrumb 1c3656d5961752d205250f0c823213bc177298c4132964a575f331384a0b85a8 -->

## Purpose

Tarav is an external `Agents.Harness` intended to enhance collaboration between Users and Agents. It provides tools and workflows addressing recurring problems in that collaboration.

Concretely, Tarav is an extensible Python library. Its capabilities can be integrated into a wider system and composed into specialized harnesses for particular Projects.
<!-- tarav.breadcrumb 529226730418253fa70e0ad7f7848c36fe93624bf9e70953a35589c2f415cebf -->

Capture, including recording `User.Touched.Data`, annotation primitives, contextualization, checks, and workflow coordination are concrete capabilities through which Tarav supports collaboration. They can evolve while remaining consistent with this purpose.
<!-- tarav.breadcrumb 3d347443ec3ebb3baa08748724a7b83545615148fdfef743d54c8bb5e9fed8be -->
<!-- tarav.breadcrumb f8a6d1c8c52ca8392f8e5d4604d47cfce44b41e4d47aea6aec9bf99dab8ea6c2 -->

[NOTE We need to expand this to add the harnessing part. ]

## Projects

A `Project` is a fundamental Tarav concept. Tarav's capabilities can be selected, extended, and combined to build a harness for a particular Project.
<!-- tarav.breadcrumb 8178981fa7712ff82167273de791c67fb8dd23ab3a6511cf8b97e949bc1d515a -->

## Agent Harness Boundary

An Agent is a harness around an LLM. Tarav is an `Agents.Harness`: a harness around Agents that supports collaboration between those Agents and Users.
<!-- tarav.breadcrumb e1afd7dc093487ec9d7abfecd323930932d304a3810c88280838112967dcaa4e -->

Tarav may provide mechanisms for launching or operating Agents, but agent execution is not its defining responsibility.
<!-- tarav.breadcrumb 7353b15ca16e0e94caf7a7309e4140a92d2af91874ec3f6b0b848df9a15df065 -->

Tarav supports the contextualization of agent reasoning; it does not prescribe the internal reasoning of an Agent.
<!-- tarav.breadcrumb e0644e75d73d3511237f0bd16b628b57ee456abe24b39de95db93cd7bd473bf2 -->

## Mechanical and Agentic Work

Tarav must use deliberately simple, bounded code to perform work that can be specified reliably and to provide data, context, and signals to flexible Agents.

Tarav should mechanize as much of the common case as practical without encoding complex or brittle solutions merely to avoid Agent involvement.
<!-- tarav.breadcrumb 193b02b6c8d2d32b7f592b1d8e9424b19fa1b932d5872971ab9f2c0ab3475a13 -->

Ambiguous, interpretive, open-ended, and long-tail work should be routed to Agents.

Agent fallback is an intended part of Tarav architecture, not a failure of mechanical automation.
<!-- tarav.breadcrumb 49fa142669d14c2dea84aac8c3706f4cfa638ad2a2ad346934769e23a7b5118f -->

## User Context

Tarav is biased toward enriching agent context with `User.Touched.Data`. It must help agents work as fully contextualized on the user as possible.

This grounding does not claim that `User.Touched.Data` is authoritative or correct. Tarav does not prescribe how an agent reasons from that context.
<!-- tarav.breadcrumb e638ee17754d955e99a46c63655d1d32e4f07b4523f70cb41fd365476805b87e -->

## Natural Workflows and Extensibility

Tarav must fit `User.Natural.Workflows` rather than require users to adopt one prescribed Tarav workflow.

Tarav must be flexible and designed for extension so users, agents, and implementations can adapt it to their natural collaboration patterns.
<!-- tarav.breadcrumb c0c3c12db0f297a54b9ad3c6b935e336c76afca422a5c259e8e517924fb18203 -->

Extensions may introduce different mechanisms and workflows, but any surface claiming to be part of Tarav remains bound by this Constitution.

## Session Goals

Tarav-supported user-agent sessions may pursue both the user’s immediate objective and the capture and enrichment of `User.Touched.Data`.

The user controls the foreground workflow. Tarav must not stop or redirect product development to require Diagram enrichment.
<!-- tarav.breadcrumb 177f4e2677c5641242c25d3be452d17e3fcc94504547f18115a44a446c82ec61 -->

When the user chooses development, the session develops. Enrichment may occur organically without obstructing that work. When the user chooses capture, curation, or enrichment, the session pursues that work directly.

Tarav must provide primitives that make collecting, annotating, and curating `User.Touched.Data` cheap and organic within `User.Natural.Workflows`.
<!-- tarav.breadcrumb bfab21d025fbc7b3e931481d55d4dc2724ff0de970bdf862af660216f38b7a66 -->

Completeness measures may guide enrichment and surface opportunities, but they must not gate work or impose a globally complete Diagram.

## Mutation and Validation

Tarav must be evolvable and migration-friendly. Its code, schemas, and data are amendable. For product surfaces, committed Git history together with retained work conversations is sufficient change evidence by default. Additional documentation or tracking may be added when useful, but exhaustive change explanations must not become a prerequisite for evolution.
<!-- tarav.breadcrumb 823eddb6a42fcfd861b7cc40f927e3acceb464e5ad0abb352f64081fd140fbb7 -->
<!-- tarav.breadcrumb a1e213b405af0b0a19869ff724d548e9ead51ca70cdd9d9f80125a84563fb5da -->

The nonblocking validation commitment for capturing user data is stated in Capture First below.

Users, agents, and other consumers are the primary mutators of Tarav state.

Validation independently judges the resulting state. Its responsibility is to surface POIs together with the context needed to understand them.
<!-- tarav.breadcrumb 1fc63f86c71e12bac98fd2e0e96394fcf68fbd93a74990655430f2a75f843ee7 -->
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]

Tarav must provide primitives that allow and aid consumer responses to POIs, but the action taken remains the consumer’s choice.
<!-- tarav.breadcrumb c56142ed2217c467ff8363f6a06c8cb7f8629e43a24b1eea15c0c48ed9473d20 -->
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]

Misalignment and POIs are expected Tarav states, not system failures. Their presence may demonstrate that validation is working as designed.
<!-- tarav.breadcrumb 00b72fd32bcd44303e2bbe4e1b3719ee46d0a4d94b4090c917a84afc5875c55e -->
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]

Tarav must allow users, agents, and consumers to modify and explore its state without first resolving existing POIs.
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]

After mutation, Tarav must evaluate and score the current state and surface the problems it finds.
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]

Tarav does not force a workflow or require POIs to be resolved before work continues. Consumers decide whether, when, and how to act on them.
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]

[NOTE
    I mean, here I think we should talk about tarav as a harness.
    And that one of the main feature of a tarav harness is that it provides checks.
    So, the system is built so the agent can evaluate the state of the current project.
    I do not know what Constitution material is here. to discuss...
]

## POI System
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]

Tarav uses POIs to surface suspicious states that may require user or agent attention. A POI is a signal, not a verdict, and does not make the system broken.

Tarav should detect suspicious states mechanically wherever practical and surface them with enough context for flexible agent or user judgment.

POIs may originate from Assertion scoring or from any other Tarav system. A POI does not need to be represented as a Diagram Annotation.
<!-- tarav.breadcrumb 20f80db606bd728c54a898aff47a53dba7c409e21750902a6d3687b28a75a042 -->

Users, agents, and other consumers decide how to interpret and respond to POIs.

## Capture First

Tarav prioritizes recording `User.Touched.Data`. When data may contain or preserve `User.Touched.Data`, capture must occur before concerns about completeness, formatting, annotation quality, or other POIs are resolved.
<!-- tarav.breadcrumb 88630183a7afa89e6f254cf9b10173c4823282a34abd90f03ad4a8e19243f838 -->

Tarav capture must favor recoverable overcapture over irrecoverable failure to record touched data.
<!-- tarav.breadcrumb 627d3007ee2b0b33ef31495e2075348f72cb037332fbb9dd7444046af5659be6 -->

Validation must not block the capture of user data. Tarav considers this data highly valuable. When a capture path fails, the system must provide a simpler fallback, including retaining raw data for later processing. Capture comes first; validation and organization can follow.
<!-- tarav.breadcrumb 45e1f418f101790abbfb35b62e2fd9991404bfb10721038722c1d7730baa3ffa -->
<!-- tarav.breadcrumb 96e54d858b65c779aecb5b43613a2899828d73f6e4b2215e4cd6a2126ca02ea6 -->

Once data enters Tarav, it may be curated, annotated, amended, enriched, and scored over time.

Tarav is not a general repository for Agent-generated summaries or content. Agent-generated data is not archived merely because it was generated; it may be archived when touched, deliberately selected, or captured as a safety margin against losing touched data.

## Logistical Extensions

Tarav must support integration with databases, query systems, and other logistical extensions that improve performance and access over Tarav data.

Tarav data remains authoritative. Logistical extensions may index, cache, query, or project that data, but they do not displace its authority.
<!-- tarav.breadcrumb 287596d1a3ecbe19f14e508a80cb18d2d594d64f6b4c8678c54ef0767918deca -->

## Collaboration Loop
[NOTE
    Too specific for the constitution.
    Consider delete/move.
]

Tarav is organized around a continuous collaboration loop:

```text
user-agent collaboration
          ↓ captures
       Touched.Data
          ↓ recorded by
      Tarav.Archive
          ↓ structured by
      Tarav.Diagram
          ↓ selected through
     Contextualization
          ↓ enriches
  user-agent collaboration
```

## Tarav.Archive
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

The main responsibility of `Tarav.Archive` is to record `User.Touched.Data`.
<!-- tarav.breadcrumb a8662815421ff220bf881440afa0b8a726260f646294a6adcd16f7938ed60ddf -->

`Tarav.Archive` registers `Archive.Artifact`s and retains `Archive.Record`s about them.

An `Archive.Artifact` is the actual data identified by the Archive. An Artifact may be retained by the Archive, located elsewhere, or temporarily unavailable.

An `Archive.Record` is retained data associated with one Artifact. Records may preserve Archive bureaucracy, identity information, current and historical locations, observations, descriptions, fingerprints, and other hints about that Artifact.

`Tarav.Archive` records Artifacts and Records without regard to their origin, purpose, or meaning. Tarav must use the Archive to record `User.Touched.Data`; the Archive itself does not recognize or distinguish that data from anything else it records.
<!-- tarav.breadcrumb 73beb42996d3ff5b4c93858bd2399a8ffe0d87586cc64083db8a59c7f2cfc09f -->

The Archive does not interpret the internal semantic structure of Artifacts. Consumers construct organization and meaning from Archive Artifacts and Records.

Archive Records do not need to agree. The Archive preserves attributed claims and observations without endorsing their correctness or meaning.

Archive Artifacts are immutable signal. A changed Artifact is another Artifact. Archive Records describing an Artifact are amendable: locations, annotations, fingerprints, and other information may evolve while the Record continues to describe the same Artifact.
<!-- tarav.breadcrumb 843ff542a6dbc6ebac52c58206b048260dc7881dfb79ba5ed083bda2bb4a3f03 -->
<!-- tarav.breadcrumb 1278026470b5faaa1f1edea517f6639a2c1490b33ff3900deba2d72a431f673c -->

The Archive provides typed references whose contracts consumers must be able to inspect. A reference to an amendable Record follows its declared contract. The Archive must never silently provide a different Artifact in place of the identified Artifact. If it offers a substitute or another representation, it must make the substitution and its relationship to the requested Artifact explicit.
<!-- tarav.breadcrumb 461b2a55511f5881b7f2623e37e9b8e64b9b68f2cb8f76856f9914218b004ce2 -->
<!-- tarav.breadcrumb cd281677c0ea0f5ad80ae29d1ff3de5fe2c94d3251b2748f0cd193f6f469a0f1 -->

The Archive must help consumers locate Artifacts. When an Artifact is unavailable, the Archive must expose its retained location history, fingerprints, External Descriptors, and other available hints.

Archive Record coverage may be progressive and demand-driven. Tarav must permit Records to be enriched over time and must not require complete Record coverage as a precondition for capture, reference, or use.

Archive Records must favor representations cheap enough to retain broadly. Records have greater retention priority than the Artifacts they describe. When preservation tradeoffs are unavoidable, the Archive should discard an Artifact before its associated Records, while strongly prioritizing preservation of `User.Touched.Data`.

Consumers may register Artifacts as `External.Descriptors` of other Artifacts. An External Descriptors Record contains attributed references to other Artifacts declared to be useful descriptions, representations, or recovery hints for its target Artifact.

The Archive preserves External Descriptor references without endorsing their correctness or meaning. Each External Descriptor remains an ordinary Artifact with its own identity, locations, Records, and possible External Descriptors.

The Archive does not provide a general semantic relationship graph. Relationships beyond its bounded External Descriptor references, and the assessment of those relationships, belong to consumers such as `Tarav.Diagram`.

`Tarav.Archive` makes no commitment to downstream readers about Record formatting or which context a Record contains. Its responsibility is preservation, not presentation; readers are responsible for interpreting what it preserves.
<!-- tarav.breadcrumb 779ab9387f69646209a0326e62b35e45a784bdfc7b8cfe1283228487a7facef7 -->

## Tarav.Diagram
[NOTE
    The Diagram is not the emergent graph langugage we emmbeded on Tarav.
    Its core functionality is querable expressivity.
    We can express semantics in a way that is querable.

    Now, the User.Touched part now is just a further semantic we can express.
    Not only on the Diagram, but will be also in the code part.

    Too specific for the constitution.
    Consider delete/move.
]

`Tarav.Diagram` is a consumer of `Tarav.Archive`. It indexes, parses, links, and annotates archived data to make that data useful for contextualizing collaborative user-agent sessions.

Every semantic `Diagram.Record` must link to archived data, directly or through the support contract of its containing Ship. A Diagram Annotation may also link that archived data to external data or surfaces.

`Tarav.Diagram` never modifies Archive Records or registered Artifacts; its interpretations do not alter the Archive data they consume.
<!-- tarav.breadcrumb e9995bf3d85fad3ce8e4680f9899fd9a64f1ad60ffee6d4be9584cbb2dbc41fd -->

`Tarav.Diagram` is responsible for storing its own data. Diagram storage is separate from `Tarav.Archive`, and the Diagram does not register its own data in the Archive.
<!-- tarav.breadcrumb 9435aa124cd3e1d2735192e6f2ba1c83808afc3c613f7aa30395a62dd77527d6 -->

Diagram data, including annotations, may itself become `Touched.Data` and may be recorded by `Tarav.Archive` as new archived data. When recorded, the Archive treats it like any other data.

A semantic record claiming to represent `User.Touched.Data` must be supportable solely by the union of all `User.Touched.Data` linked to it.
<!-- tarav.breadcrumb 11a5b26566f984d655ad9ebc8e90cc76477b9eb8f1d1a61bf117d632cef6a225 -->

A semantic record claiming to contextualize user intention must link directly to its supporting `User.Touched.Data`.
<!-- tarav.breadcrumb e635d80185142f0aa29ce125cd989ef6f1f675cf39e0823522c4108b50927c55 -->

Links between such annotations and their supporting data should remain as close as practical. These constraints make no claim about annotations of other kinds of data.

Tarav must provide one main `Tarav.Diagram`. Other Diagrams may also exist.
<!-- tarav.breadcrumb 2daa27eae8528625a489f4467fc7443f9152542db463a239f117f450d26fe5e9 -->

Every `Tarav.Diagram.Record` must remain supportable by and representative of the archived data it links.

`Tarav.Diagram` is a live surface. A main responsibility of the Diagram is to prune or amend ill-annotated Records and to continuously improve and enrich its annotations.
<!-- tarav.breadcrumb 79ab8a05a8bc7070a0ae36d0d3a1d1eff8ab52454a66403fde5f03322a809806 -->

`Tarav.Diagram` does not resolve contradictions between valid Records or determine which interpretation prevails. Contradictory archived data may be correctly represented by contradictory Diagram Records.
<!-- tarav.breadcrumb 13e12a75897faf44d188e2ff54f6fcdea5a5fb3bf7ea6e4d9d8a55c21b463172 -->

Consumers of `Tarav.Diagram` are responsible for deciding how to use and interpret its Records.

A Diagram Record’s full claim and evidentiary basis may depend on linked external data; `Tarav.Archive` need not contain the entire evidentiary basis.

Tarav systems must be designed under the assumption that data necessary to support Diagram records will be archived. When required data is absent, deleted, or unreachable, validation must surface the affected Assertions and records as POIs.

Assertion links must make the consequences of Archive retention and deletion decisions inspectable.

Diagram construction may require expensive curation, interpretation, and computation. The Constitution does not require rebuilding a Diagram to be practical, deterministic, or operationally available.
<!-- tarav.breadcrumb 783b0c1d53e5f4b0e0ce59399c0a48f671dcd0766a92323fc607ed1cca63cff3 -->

If an annotation process introduces additional data, that data must ultimately be recorded by `Tarav.Archive` and linked as support. Otherwise, the affected Record must be amended or pruned.
<!-- tarav.breadcrumb e2658dc0569dbe5d0a60cda38ef0fa613defca8a81e13affafc9fd21ab258c8c -->

`Tarav.Diagram` does not constrain what may be asked or asserted about archived data. It must be extensible so that anything can be asked against that data and annotated.
<!-- tarav.breadcrumb ad61cfb21e4968c439837a7c1c336133fa8075690bd3d2a46442157f25f1b1bf -->

`Diagram.Ship` establishes a semantic entity and retains its editions. `Diagram.Annotation` is a separate typed claim about a Ship, edition, transition, relation, external surface, or other subject; an Annotation may retain its own claim lineage, but it does not establish the entity it discusses.

Typed `Diagram.Records` and `Semantic.Assertions` form Tarav’s general model for expressing and assessing semantic structure. Every semantic Record carries Assertions, including an implicit assertion that it correctly represents its linked archived data, and may carry additional Assertions about structure or other assessable properties.

Every assertion must be subject to evaluation and scoring against the subject of its claim. Tarav must provide `Assertion.Scoring.Systems` and primitives for assessing assertions.

Every semantic `Diagram.Record` is associated with a score vector containing the score of each of its Assertions.

Tarav must provide tooling for computing and maintaining those score vectors.

`Tarav.Diagram` permits unlimited inquiry. It must not remain silent about unassessable annotations.
<!-- tarav.breadcrumb 3d81df184ecbbab87e223a5789f5a735798392526a6c12f0750906e26a218328 -->

Missing, unresolvable, or unassessable Assertion scores must surface POIs. A semantic Record without resolvable scores for its Assertions is `UnAsserted`.

A low-scoring Assertion must also surface a POI, but its Record remains `Asserted`: the score records a falsy or weak assessment.
<!-- tarav.breadcrumb 24a96634a5dcdc7dcb96c1fef28bd5c636ee80e7f57f643a1bf001e344b054a5 -->

Records with missing or low scores are natural targets for Diagram curation, amendment, and enrichment.

When contextualizing a semantic Record, Tarav must include its available score vector. Consumers decide how to interpret and act on those scores.
<!-- tarav.breadcrumb 1bc9d3fd7f296e943832e382440c45e11a416467f0075c76ef4fdfd8ff014b33 -->

## Contextualization
[NOTE
    Better generality, but we most revisit.
]

Tarav must provide extensible tooling and systems for selecting and presenting `Tarav.Diagram` content to collaborative user-agent sessions.

Context may begin with compact Ship editions or Annotations, but Tarav must preserve a navigable path from each contextualized Record to its linked supporting data.

Agents and other consumers must be able to expand that path on demand and inspect progressively deeper supporting context.
<!-- tarav.breadcrumb a6d682f872eac4a529ed73606f58d3a4e1b434504b916d6ed4265546c1fb96ce -->

## Generation Context
[NOTE
    This is about skw.
    Again, I do not know if CONSTITUTION material
]

Tarav must provide tooling for annotating a generated `Product.Surface` with the archived data supplied as context for its generation.
<!-- tarav.breadcrumb bbde65f7cc886bb2965e983c1fbbd72ba17c4df09c91e58f266322e78ba5dc1f -->

A generation-context Annotation may link archived `User.Touched.Data` to an external `Product.Surface`. Its provenance claims are `Annotation.Assertions` and must be scored like other Assertions.
<!-- tarav.breadcrumb 6d09fc56ada5ccfacb07121532d3c83f7a8d5d48e6bab9d13bda66bf275dcc03 -->

Generation context must distinguish data presented to the agent from claims about what influenced the agent’s internal reasoning. Tarav makes contextual provenance inspectable without prescribing or claiming knowledge of that reasoning.

## Reference Contracts

Tarav references are typed. Their Types declare the contract under which data is identified and resolved. Some contracts permit maintenance such as schema changes; others commit to exact bytes.

References must never silently deliver data that violates their declared contract. They must provide a way to check for changes relevant to that contract. Hashes and retained hints can support these checks.
<!-- tarav.breadcrumb 2c09edaf5ab91cf0585b8b3c6bbb91ec3229a29fd2c9bb4ea6e813864ea6ee93 -->
<!-- tarav.breadcrumb 4b3b5219ff55a4d27d6d33512a5acf13dd318761f8462456a74a39aae995b0fd -->
