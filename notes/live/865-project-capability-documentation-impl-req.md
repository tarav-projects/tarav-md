# 865 — Project capability documentation — Impl.Req

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

## Impl.Abstract

Knowledge.Surface: wiki. Alignment.Mode: Interactive. Status: Ready. Phase: Develop.

Update maintained Tarav Markdown documentation and the Hugentics skill's authored SKW source for the Project paths implemented by [Python Impl.Req 866](../../../tarav-py/notes/live/866-project-capability-paths-impl-req.md): `project.docs.wiki`, `project.models`, and `project.checks`.
<!-- tarav.breadcrumb cf661731d7b38a2c9c8a5992b39d77852c4559888f4763e4dff6683334f5db05 -->

## Design narrative

The User selected semantic paths for Project documentation, models, and checks. `docs` groups documentation, `models` remains a bound capability, and `checks` is a shared provider namespace. Compiled skill Markdown is a product; its `.skw/src` JSON output is authoritative and must be recompiled after edits.
<!-- tarav.breadcrumb 8a59581656342beec2cf8b1db817afb685b290622ed5d34597a7822b4b353eca -->

## Impl.Req.Wiki

Product: `tarav-md`. Wiki root: `notes/wiki/`; topical `projects.md` and daily `2026-10-07.md`. Supporting session: `codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8`. Capture status: pending.

## Execution.Plan

1. Update the Hugentics skill's authored source references and compile its product.
2. Update the Projects Wiki topical note and daily narrative with exact User-Turn Breadcrumbs.
3. Validate skill compilation and scope, then make separate documentation and Wiki commits.

## Impl.Log

- Design: inspected skill package instructions and found two maintained Hugentics references using the former `Project.from_path(path).wiki()` call.
