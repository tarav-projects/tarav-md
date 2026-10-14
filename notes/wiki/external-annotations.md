# External annotations and discovery

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Claims about arbitrary subjects

Agents and users should be able to attach typed annotation Records to anything.
Each annotation type owns its semantics: a claim may concern one subject's
property or express a directional relationship, among other possibilities.
Annotations accumulate claims and links about their subjects.
<!-- tarav.breadcrumb 14af973a0f416efe1b6eb8a7f2c58a47c39b8e1ec560fcabc2a9a5ae2c960e0b -->

The annotator is external. The subject need not know about its annotations;
interpretations can accumulate without modifying the thing being interpreted.
The claim belongs to the annotator.
<!-- tarav.breadcrumb 0651b376b16b7fd550117c6f01cf52aeb46347b417c55a963813492560662774 -->
<!-- tarav.breadcrumb c43347d39e14e2a8943cfedd3ae23a0c0a17d4802f101bd954d50dca88d7b1a6 -->

## Capture and annotation are soft distinctions

Capture is mostly about representing existing material faithfully, through
such operations as copying, extracting, transcribing, or summarizing.
Annotation is mostly about adding semantics about something: an attributed
property, interpretation, relationship, or evaluation. These are orienting
definitions, not strict categories whose corner cases need to be settled.
<!-- tarav.breadcrumb 8729b6856271998042b30ff21dfd82ee0ae92873b626dda6892e6d709bb0d2e7 -->

## What do we have about this file?

After loading a file, an agent should be able to query Tarav for what it has
about that file. The response is a list of candidates, similar to search;
the agent can expand results or query differently. External annotations are
one way to accumulate the material and relationships that make this useful.
<!-- tarav.breadcrumb 0ffac4ff00f0f335f054ea3f44c4a49f1acdb55c494e285a9b8432ad958314d8 -->

## General subject references

The current restriction of annotation arguments to Diagram Ships, editions,
and annotations was identified as a problem. The proposed direction is a
reference-resolution workflow where other workflows register their reference
types, allowing consumers to resolve them through a common entry point.
Common types and reusable mechanics should support general annotation subjects;
see [References](references.md).
<!-- tarav.breadcrumb 796b2ef1b97c95257c197ced2add95192b94fa00ca61bc71d57792e508b35989 -->
<!-- tarav.breadcrumb ef438f3afd206ec3c442b01515e148d835fb3370524feb9c9ddd4526acd5687e -->
