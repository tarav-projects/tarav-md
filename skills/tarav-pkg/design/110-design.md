> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Wayfinder

- [DF] `Agentos.Wayfinder` is the shared Agentos subsystem that resolves portable `Wayfinder.Reference`s into verified reachable resources through composable registry and domain-resolution stages ^c20260729-249u
- [PR] its primary consumers are programs that require deterministic lookup of resources whose concrete locations may change ^c20260729-338u
- [CT] resolution composes `Wayfinder.Registry` lookup with the `Wayfinder.Resolver` stages selected by the reference type ^c20260729-132u
- [CT] successful resolution produces a `Wayfinder.Resolution.Result` only after the target domain verifies that the requested resource is reachable ^c20260729-135u
- [CT] the same canonical reference, resolution context, and registry state produce the same resolution result ^c20260729-152u
- [PR] stable surfaces retain portable references while machine-local concrete locations remain disposable resolution state ^c20260729-348u
- [CT] failed resolution emits a structured `Wayfinder.Resolution.POI` carrying the original reference and resolution trace ^c20260729-101u
- [FR] agents may use `Agentos.Wayfinder` or inspect and discover resources directly; Wayfinder does not constrain agent exploration ^c20260729-307u
- [RJ] `Agentos.Wayfinder` orchestrates domain address systems and resolvers; it does not replace or redefine them ^c20260729-358u

****

## Wayfinder.Reference

- [DF] a `Wayfinder.Reference` is a stable portable pointer declaring a resource that `Agentos.Wayfinder` may resolve ^c20260729-286u
- [DC] the canonical form of a `Wayfinder.Reference` is a versioned JSON object ^c20260729-237u
- [CT] every reference carries a `Wayfinder.Reference.Type` that defines its resolution semantics and selects its composable resolver chain ^c20260729-99u
- [CT] reference identity is independent of the resource's current concrete location ^c20260729-128u
- [FR] domains may expose convenient `Wayfinder.Reference.Sugar` forms such as URLs, block names, and paths ^c20260729-309u
- [CT] every `Wayfinder.Reference.Sugar` form must parse deterministically into the canonical `Wayfinder.Reference` JSON object ^c20260729-96u
- [RJ] a concrete path or locator obtained during resolution is not the identity or authority of the referenced resource ^c20260729-362u

****

## Wayfinder.Registry

- [DF] a `Wayfinder.Registry` is a source of remembered resource registrations consulted by `Agentos.Wayfinder` during resolution ^c20260729-287u
- [CT] each registration associates a `Wayfinder.Reference` or `Wayfinder.Reference.Root` with its last verified concrete location and optional relocation hints ^c20260729-89u
- [PR] registering reusable roots rather than every contained resource limits staleness and enables composable domain resolution ^c20260729-343u
- [CT] a registered concrete location is machine-local operational evidence, not the identity or authority of the referenced resource ^c20260729-62u
- [FR] relocation hints are an open agent-facing collection that may contain structured values or natural-language guidance ^c20260729-316u
- [RJ] relocation hints may guide discovery but do not establish successful resolution without domain verification ^c20260729-369u
- [FR] Wayfinder may compose contextual, project-local, and global registry providers under deterministic precedence ^c20260729-302u

****

## Wayfinder.Resolver

- [DF] a `Wayfinder.Resolver` is one deterministic stage that advances resolution for a declared `Wayfinder.Reference.Type` or resource domain ^c20260729-291u
- [CT] a reference type selects an ordered resolver chain that may compose registry lookup, root resolution, domain addressing, and target verification ^c20260729-61u
- [CT] each resolver stage receives the canonical reference, resolution context, and prior stage result needed by its contract ^c20260729-90u
- [CT] each stage contributes its attempted inputs and outcome to the resolution trace ^c20260729-91u
- [CT] a domain resolver owns the interpretation and verification rules of its resource domain ^c20260729-59u
- [RJ] a `Wayfinder.Resolver` does not make an unverified candidate into a successful resolution ^c20260729-360u

****

## Wayfinder.Resolution

- [DF] a `Wayfinder.Resolution` is one attempt to resolve a canonical `Wayfinder.Reference` through the resolver chain selected by its type ^c20260729-290u
- [CT] successful resolution yields a `Wayfinder.Resolution.Result` containing the canonical reference, verified reachable target, and resolution trace ^c20260729-137u
- [CT] missing, ambiguous, stale, malformed, or unreachable outcomes emit a structured `Wayfinder.Resolution.POI` without hiding the original reference ^c20260729-121u
- [CT] a resolution POI exposes the attempted reference, resolver trace, remembered location, and available relocation hints ^c20260729-63u
- [FR] an agent may use the POI and its hints to discover and verify a relocated resource ^c20260729-308u
- [CT] a verified relocation may update the appropriate `Wayfinder.Registry` registration before retrying the original reference ^c20260729-66u
- [RJ] agent discovery does not establish resolution success until the selected resolver chain verifies the candidate ^c20260729-367u

****

## Wayfinder.Reference.Type

- [DF] a `Wayfinder.Reference.Type` is the stable discriminator that declares the resource domain and resolution semantics of a `Wayfinder.Reference` ^c20260729-285u
- [CT] each type defines the validation rules for its canonical reference data ^c20260729-93u
- [CT] each type selects an ordered `Wayfinder.Resolver` chain and defines what constitutes a verified result ^c20260729-94u
- [FR] Agentos subsystems may add reference types without changing the Wayfinder core model ^c20260729-301u
- [RJ] a reference type does not encode a current concrete location, registry provider, or resolver implementation ^c20260729-363u

****

## Wayfinder.Reference.Root

- [DF] a `Wayfinder.Reference.Root` is a stable registrable identity that anchors relative addressing within one owning resource domain ^c20260729-284u
- [FR] a root may identify an Agentos project, package, index depot, or another domain capable of resolving contained resources ^c20260729-305u
- [CT] a `Wayfinder.Reference` may compose a root identity with an address relative to that root ^c20260729-55u
- [CT] a `Wayfinder.Registry` associates the root identity with its remembered concrete location without changing the root identity ^c20260729-56u
- [PR] one root registration supports resolution of many contained resources and limits duplicated location state ^c20260729-341u
- [RJ] resolving a root does not itself grant engagement, visibility, or authority over the resources it contains ^c20260729-370u

****

## Wayfinder.Reference.Sugar

- [DF] `Wayfinder.Reference.Sugar` is a surface-fitting alternate syntax that parses into a canonical `Wayfinder.Reference` JSON object ^c20260729-281u
- [FR] reference domains may define sugar forms such as URLs, dotted block names, and paths ^c20260729-314u
- [CT] each sugar form has a parsing contract that identifies its `Wayfinder.Reference.Type` and maps its values into canonical reference data ^c20260729-92u
- [CT] the same sugar value and parsing context produce the same canonical reference ^c20260729-153u
- [CT] persisted sugar must either carry every required identity field or resolve omitted fields unambiguously from its parsing context ^c20260729-124u
- [RJ] a sugar form is not a second reference identity or an alternative canonical representation ^c20260729-365u

****

## Wayfinder.Resolution.Result

- [DF] a `Wayfinder.Resolution.Result` is the verified successful output of one `Wayfinder.Resolution` attempt ^c20260729-289u
- [CT] it carries the canonical `Wayfinder.Reference`, concrete reachable target, domain-verification evidence, and resolution trace ^c20260729-109u
- [CT] the result records the resolution context and registry state against which success was established ^c20260729-151u
- [PR] its verified concrete location may refresh the corresponding `Wayfinder.Registry` registration ^c20260729-339u
- [RJ] a resolution result does not modify the identity or canonical data of its reference ^c20260729-364u
- [RJ] a verified result establishes reachability for its resolution attempt, not permanent future reachability ^c20260729-366u

****

## Wayfinder.Reference.Type::Index.Block

- [DF] `Wayfinder.Reference.Type::Index.Block` is the reference type for a `Kernel.Block` contained in a package-owned `Index.Depot` ^c20260729-282u
- [CT] its canonical reference data identifies the owning `Package.Skill` root and the block through `Skw.Address.Schema` ^c20260729-113u
- [CT] its resolver chain first resolves the package root through `Wayfinder.Registry` ^c20260729-117u
- [CT] the resolved package root delegates the remaining address to its Index machinery ^c20260729-150u
- [CT] successful resolution requires the Index machinery to resolve exactly one reachable block ^c20260729-136u
- [PR] the reference remains stable when the package or its Index depot moves ^c20260729-355u
- [RJ] the reference does not encode an absolute path, chapter filename, or package installation layout ^c20260729-371u
