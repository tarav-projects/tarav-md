# AGENTS.md

## Purpose

`agentos-md` is the markdown implementation of the Agentos project.

It owns `Md.Surface:Agentos.Stack`, including the durable index notes, live notes, skills, and markdown coordination surfaces used to define and operate the Agentos agentic framework.

## Surface Rules

- `notes/index/` is the active `Design.Target.Model:Agentos` surface.
- Use `notes/index/001-ontology.md` for registered concept names and concept lookup.
- Do not treat closed live design sessions as active authority; use them as provenance only.
- Do not turn `AGENTS.md` into a progress tracker or design log.
- Durable design truth belongs in `notes/index/`.
- Development instructions and local workflow reminders can live here when they help agents work safely.
