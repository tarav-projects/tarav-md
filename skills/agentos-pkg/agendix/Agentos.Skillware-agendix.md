****

## Agentos.Skillware/Agendix

- [DC] skw is the umbrella: the command, config, and build home all take the `skw` name — `agentos skillware` → `agentos skw`, `.skillware/` → `.skw/`, `skillware.json` → `skw.json`; sources are already `*.skw.md`, so `skillware` was the lone legacy token ^c20260720-8u
- [DC] the `.skw/` build home is recursive and git-tracked: a project root carries one and each package carries one — same shape, one level apart; `.agentos/` keeps only project identity + runtime (marker, profile, state, tapes), the tracked skw source lives in `.skw/` ^c20260720-9u
- [PR] project scope and package scope solve the same problem at different reach — one for any surface, one for a particular surface — so they mirror: one `skw.json` schema (`depots` / `surfaces` / `exclude` / `projects`) read at both levels, package extending project via cascade; absence of config = discover every `.skw/` and check all ^c20260720-9u
- [DC] `agentos skw check` runs project-wide by default (discovery), `--skill <path>` narrows to one node; project scope is the `Skw.Network` checked whole — a rename in one package that breaks a pointer in another is caught even when nobody re-checks the second (the `dangling-dependency` POI, now firing across the graph) ^c20260720-8u

****

## Agentos.Skillware/Agendix/Skw.Package

- [DC] candidate concept `Skw.Package`: the folder that owns a `.skw/` build home — the recursive unit of skw management (project root + each skill); it declares dependencies and produces tracked output ^c20260720-10u
- [DC] the general naming ladder, `Skill.*` becoming the skills-backend instances (same move as `Kernel.Line` → `Index.Line`): `Skw.Package` ⊃ `Package.Skill`; `Skw.Build.Surface` ⊃ `Skill.Build.Surface` (the `.skw/`); `Skw.Runnable.Surface` ⊃ `Skill.Runnable.Surface` (the output); `Skw.Module` ⊃ `Skill.Module` (the per-source unit) ^c20260720-10u
- [CT] `Skw.Package` is the folder grain, not the file grain — a package contains modules, so the folder unit is a package while `Skw.Module`/`Skill.Module` stays the per-source `*.skw.md` → output unit inside it ^c20260720-10u
