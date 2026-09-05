# 779 — Inlined Capture audit

Status: Completed

## Impl.Abstract

Add `tarav-hugentics --capture --inline --audit <surface>` as a read-only,
Agent-operated audit of the lightweight references already embedded in one
Product.Surface.

The audit has generic questions but no universal surface parser: the Agent uses
the selected surface's native tools and conventions, resolves declared Chatlas
targets exactly, and reports POIs without editing the surface. The first
documented specialization remains Markdown.

## Impl.Req.Diagram

- **namespace:** User.Touched.Chatlas.Index / `1c99092c-ba46-4006-adc3-9ada50c00abd`
- **model:** Tarav / `b7b78eab-e5c2-4610-9bf5-1b704a106f34`
- **collection:** 779.Impl.Req / `f4de218f-11ec-4c33-8fd3-2737e7f71c43`
- **collection type:** Impl.Req.Collection
- **draft:** `51fe8b7c-7cba-442b-a7b4-00e0298bc0f4` / `/Users/pereiro/Documents/tarav/diagram/drafts/51fe8b7c-7cba-442b-a7b4-00e0298bc0f4.json`
- **authorization gate:** `901b18fc-07c6-453f-835e-5c1de3bf74e1`

The Collection hosts supported User-Touched requirements. The live note owns
the execution plan and implementation log.

## Execution.Plan

### Slice 1 — Public route and audit contract

- expose the composed `--capture --inline --audit <surface>` route in the
  Hugentics command surface
- specify the generic audit questions, read-only boundary, surface-native
  inspection, exact Chatlas resolution, and POI report
- keep semantic attachment judgment Agent-operated
- observable: the skill routes the composed flags to a complete audit workflow
- check: skill validation and cold reading of the documented command
- status: completed

### Slice 2 — Real-surface acceptance

- exercise the documented workflow against the PhD Constitution without
  modifying it
- observable: declarations and references are inventoried and resolved, with
  attachment concerns reported separately from mechanical resolution
- check: exact Chatlas batch resolution succeeds for the selected surface
- status: completed

Risks: accidentally turning audit into mutation; coupling `tarav.surfaces` to
Inlined.Capture policy; over-specifying one attachment model for every surface;
or silently treating a resolvable reference as semantically correct.

Deviation triggers: the existing surface or Chatlas tooling cannot support a
bounded read-only audit, or the Markdown convention cannot be inspected
without new mechanical code.

Acceptance signals:

- the public skill documents the composed route and its precedence;
- audit never updates the selected Product.Surface;
- generic audit semantics remain separate from surface-specific conventions;
- unresolved aliases, malformed declarations/references, zero or multiple
  Chatlas matches, and suspicious attachments are reported as POIs;
- a real annotated PhD surface can be audited with current tooling.

## Impl.Log

- Direct-input Execute was selected from the User's explicit implementation
  request.
- The implementation intentionally changes skill surfaces only. No universal
  parser, registry, manifest attachment, or multi-surface orchestrator is in
  scope.
- Workflow checkpoint: `f99ced8`.
- Updated `skills/tarav-hugentics/SKILL.md` with the composed public route,
  flag precedence, read-only standing, and focused routing.
- Extended `references/inline-capture.md` with separate capture and audit
  routes, a generic audit contract, an Agent-operated workflow, Markdown
  acceptance rules, and explicit POI conditions.
- The audit performs no Chatlas update, Diagram mutation, retained report, or
  Product.Surface edit. `tarav.surfaces` remains a domain-neutral optional
  source of syntax facts and spans.
- Skill validation passed and `git diff --check` is clean.
- Live acceptance against the PhD `THESIS-CONSTITUTION.md`: Markdown
  specialization, one session declaration, 17 references to 11 distinct Turn
  prefixes, all resolving exactly to User Turns; no malformed, missing,
  ambiguous, wrong-side, fenced-example, orphaned, or structurally suspicious
  reference was found.
- Product.Surface production context is preserved through the checkpoint,
  current diff, Impl.Req, and rooted Draft support; no separate external
  Product.Surface Annotation primitive was applied.
- Draft checking retains expected unasserted, Archive-grounding, and
  Collection-hosted Model-staleness POIs. The initial producer-order POI was
  corrected before closing.
- Closed `779.Impl.Req` and applied the Draft once. Diagram receipt commit:
  `94e990080f5bbc7b737dc6e8b449667d2e8efb80`.
