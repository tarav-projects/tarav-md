# Agent-generated data minimization

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## A general design constraint

Tarav uses mechanically obtained facts wherever possible, especially data
from established systems such as the operating system and Git. Otherwise,
absence is preferable to filling the gap with agent-generated content. This
is a general design constraint, not merely a preference about hints.
<!-- tarav.breadcrumb 1260a59e2ce29a2a7d3365ee9a055a04e5137ef4e9a494936e6b984d12c04461 -->
<!-- tarav.breadcrumb 27af841a96151d3986588dde9a965811c89706b69fc478b113af63155d5b16c2 -->

Agent-generated claims are used only when necessary for an explicitly defined
purpose and must be treated with care. Their production, provenance,
evaluation, and retention must be controlled by the workflow. The amount of
agent-generated data must remain deliberate and bounded: every such field or
artifact needs a reason to exist. Agent generation is not the default way to
populate missing information. The design must actually follow this constraint,
not merely state it.
<!-- tarav.breadcrumb 212ece818b0df25aed08600e59c02befa630a8ced3048a0f9ddc7d18b80fcfd1 -->
<!-- tarav.breadcrumb d2b519d2660fc3e893067a682d9e300ce5b745ea018fd4658e2a5fcaad278063 -->

## Harnessed generation is the goal

The antipattern is unharnessed generation, not generation itself. Generated
material should provide a way to score it and sufficient evidence to explain
it; otherwise it can reflect an agent's unavailable production context.
Tarav's goal is to harness and benefit from agent generation. The required
infrastructure is still being built, so this clarification states the intended
direction rather than claiming that the full generation harness exists.
<!-- tarav.breadcrumb 67339248fe017949575c26d31a1733c28f8dc6781955e1e52b8218c871ffd114 -->

## Agent consumption does not imply agent authorship

[Reference hints](references.md) are for agents to consume; that does not mean
agents should generate them. Prefer mechanically extracted information. A
generated summary stored as an ordinary descriptive field is an antipattern,
not a default use of the opaque hint payload.
<!-- tarav.breadcrumb c4a13f2d72746e0c64b865cc1f3183a5f296e35769a3dd9a436fc5e5dfc42d57 -->
<!-- tarav.breadcrumb b5de393f73643e0a9615e0d2dba6568ec3ee8885fc886591f3e11979838e1852 -->

Defining and controlling agent-generated data belongs to the Tarav harness
framework. The discussion used “agentic variables” for this concern; their
precise vocabulary and contracts remain to be developed.
<!-- tarav.breadcrumb a09f4f927f690c510f96b92f875f6b38e08ccf6a041302fcea072c35aa3f42cc -->
