# External annotations and discovery

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Claims about arbitrary subjects

Agents and users should be able to attach typed annotation Records to anything.
Each annotation type owns its semantics: a claim may concern one subject's
property or express a directional relationship, among other possibilities.
Annotations accumulate claims and links about their subjects.
<!-- tarav.breadcrumb 14af973a0f41 -->

The annotator is external. The subject need not know about its annotations;
interpretations can accumulate without modifying the thing being interpreted.
The claim belongs to the annotator.
<!-- tarav.breadcrumb 0651b376b16b -->
<!-- tarav.breadcrumb c43347d39e14 -->

## Capture and annotation are soft distinctions

Capture is mostly about representing existing material faithfully, through
such operations as copying, extracting, transcribing, or summarizing.
Annotation is mostly about adding semantics about something: an attributed
property, interpretation, relationship, or evaluation. These are orienting
definitions, not strict categories whose corner cases need to be settled.
<!-- tarav.breadcrumb 8729b6856271 -->

## What do we have about this file?

After loading a file, an agent should be able to query Tarav for what it has
about that file. The response is a list of candidates, similar to search;
the agent can expand results or query differently. External annotations are
one way to accumulate the material and relationships that make this useful.
<!-- tarav.breadcrumb 0ffac4ff00f0 -->

## General subject references

The current restriction of annotation arguments to Diagram Ships, editions,
and annotations was identified as a problem. The proposed direction is a
reference-resolution workflow where other workflows register their reference
types, allowing consumers to resolve them through a common entry point.
Common types and reusable mechanics should support general annotation subjects;
see [References](references.md).
<!-- tarav.breadcrumb 796b2ef1b97c -->
<!-- tarav.breadcrumb ef438f3afd20 -->
