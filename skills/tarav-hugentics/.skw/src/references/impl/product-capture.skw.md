> $kw: ^implementation-product-capture-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-authority-contract
> --loading-dep SKILL.skw.md^driver-index-literacy

# Implementation.Product.Capture.Workflow.Module

> $kw: --dev-from references/index-context-assembly.skw.md
> $kw: --from Impl.Req --from Index.Line --from Index.Presumption --from Kernel.Writing --from Line.Type --from Open.Inference --from Skw.Annotation --from Touched.Authority
> --note [DC] Implementation capture is a selective transactional companion to each verified slice: only landed product editions backpropagate, and zero annotations remains valid. ^d20260816-50u

This internal module composes `Real.Time.Capture` with mutating implementation workflows. It makes capture a transactional companion to each implementation slice while preserving the central restraint: good `Kernel.Writing`, not annotation volume.

It is not a public route and is not an extra implementation phase. `Implementation.Design.Workflow.Module`, `Implementation.Execute.Workflow.Module`, and `Implementation.Develop.Workflow.Module` load it as shared behavior.

## Surface Model

- An **`Index.Native.Surface`** already hosts `Index.Line` anatomy directly. `Impl.Index` and `Impl.Log` are native implementation surfaces; Project Index and Chat Index files are other examples. Do not wrap their lines in `Skw.Annotation`.
- An ordinary **`Product.Surface`** hosts qualifying typed `Index.Line`s inside `Skw.Annotation` blocks. This applies to code, tests, configuration, documentation, and other Skillware-annotatable products.
- A product annotation is part of the product edition it explains. It is not an external receipt and does not introduce a new captured-edition subject.
- The same `Index.HEAD.Backpropagation` used by other Hugentic capture targets applies to exact grounded lines landed on either kind of surface.

## Capture Bar

Capture only a direct, maintenance-relevant fact, decision, constraint, issue, or presumption that helps a later maintainer understand why the product is shaped as it is.

Every captured line must:

- use the correct `Line.Type`;
- say one fundamental thing directly;
- carry qualifying support when it asserts `Touched.Authority`;
- attach at the coarsest `Skw.Annotation` point whose scope honestly fits, unless its host is an `Index.Native.Surface`;
- describe the verified product edition rather than intended work.

Zero product annotations is a valid result. Ordinary implementation detail remains ordinary product content. Never invent support, duplicate self-evident code, annotate every touched file by rule, or turn a plan into a claim that the product already implements it.

The implementation invocation authorizes faithful product annotation within scope. It does not authorize a new semantic claim beyond the implementation. When the agent makes a consequential `Open.Inference`, surface it in chat and record it as a typed `Index.Presumption` in `Impl.Log`; never fabricate `Touched.Authority`.

## Slice Transaction

For every vertical slice, preserve this order.

### 1. Slice.Open.Capture

Before product edits, capture the plan grounding that actually constrains the slice into `Impl.Index`:

- resolve only the current-chat messages and touched Index blocks selected as support;
- write typed, supported lines directly on this `Index.Native.Surface`;
- distinguish authority from presumption;
- leave unrelated design-chat material out.

This records why the slice is being attempted. It does not assert that the product state already exists.

### 2. Product.Landing.Capture

As the product edition lands, add or update only qualifying product lines on the product itself:

- use `Skw.Annotation` on ordinary `Product.Surface`s;
- use native Index-line anatomy on an `Index.Native.Surface`;
- keep the annotation and the product behavior in the same slice edition;
- anchor final wording only after the product line and its scope are stable.

### 3. Slice.Close.Capture

After the slice checks pass and its diff is reviewed:

1. compare the verified product edition, `Impl.Index`, and landed annotations;
2. add any missed maintenance-relevant line and remove or correct any unsupported one;
3. record consequential unresolved inference in `Impl.Log` as presumption;
4. assemble one `Capture.Manifest` for the exact verified editions and selected grounding;
5. preview it, then land it through the complete Anchory, source, `LineRecord`, and Chat.Index pipeline;
6. require its final audit and report retryable head-only or failed placement gaps.

Backpropagation is batched only after the slice's actual product edition is verified. Intended but unimplemented plan material must not masquerade as landed product state. A failed slice may update `Impl.Index` or `Impl.Log`, but it must not backpropagate a product claim that never landed.

Mark the slice complete only after this close audit and backpropagation attempt.

## Final Product.Surface Audit

Before closing the `Impl.Req`, audit all changed product surfaces once more:

- every surviving product annotation still matches the final product;
- every authoritative line has qualifying support and resolves;
- no important direct constraint or issue was lost between slices;
- no plan-only or obsolete line remains presented as landed state;
- every final grounded edition was included in a successful or explicitly reported backpropagation attempt.

An empty audit is valid. The audit exists to catch important omissions and drift, not to increase annotation count.

## Operational Boundary

Use the current conversation already loaded in agent context for understanding. Ask Chatlas2 only to resolve selected message references for the one capture manifest. Let `tarav index capture` derive and apply the line dossiers, source patches, records, and Chat.Index plan; do not reconstruct the whole transcript or hand-author those intermediate artifacts.

The primary product landing remains successful if chronological Delta placement is unavailable. `Chat.Index.HEAD` still receives the exact landed line when possible, and any gap is reported for later reconciliation rather than repaired by invented chronology.
