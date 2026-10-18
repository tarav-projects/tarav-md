# Loading

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

## Configurable discovery

Loading conventions are general mechanics, not a Project-specific feature.
The loading workflow should accept configuration that lets Types supply
additional Record entry paths, such as project.json, alongside the idea of
the loader's existing default entry files. The intended call uses a named
configuration argument, illustrated as `load(path=path, profile=TaravProject)`.
<!-- tarav.breadcrumb 2ee06ba02981 -->
<!-- tarav.breadcrumb d6d493895cd7 -->

The user prefers named arguments generally, allowing at most one positional
argument for the main subject. Loading configuration and existing features
such as expected_type should remain distinct explicit options.
<!-- tarav.breadcrumb 77b0512f51d5 -->

## Opt-in profile interface

LoadingProfile should be an interface Types can implement when they want to
participate in configurable loading. It must not become a required part of
all TaravObjects. The user agreed to keep the profile model simple rather than
infer additional constraints merely because a class supplies configuration.
<!-- tarav.breadcrumb c6a8e7222e7a -->

The [implementation design](../../../tarav-py/notes/live/820-loading-profiles-impl-req.md)
first proposed ordered entry paths as the contract, keeping trusted Type
dispatch and exact expected_type checks separate. Its precedence and directory
semantics became part of the first implementation. The note also
tracks typed Project migration, duplicate-label resolution, and subproject
integration as follow-up slices rather than silently expanding this first one.

## First implementation

The user invoked Wiki-backed Develop for the loading-profile slice.
`tarav.loading.load(path=..., profile=...)` and both `load_object` interfaces
now feed profile entry paths to the same trusted Kernel loader. A profile
changes directory entry selection only: the retained Record still determines
the exact registered Type. Unprofiled loading keeps its original candidate
order and DirectoryRecord guard. TaravProject opts in for
`.tarav/project.json` and `project.json`, with correct root handling for both.
The implementation and verification are recorded in the
[820 note](../../../tarav-py/notes/live/820-loading-profiles-impl-req.md).
<!-- tarav.breadcrumb ceae87674f0a -->
