# Development.Model

## Design.Target.Model

- `Design.Target.Model` is the current explicit design model of a system
- not a frozen spec — the current best understanding of the target
- does not live only in the index — the index is a map of the model and holds part of its content
- other surfaces hold design data too: `Index.Appendix`, skills, etc.
- the index is still the entry point for building the design model because it links out to the other surfaces
- `Design.Target.Model` is a distributed model, with the index as the discovery layer

****

## Current.Implementation

- `Current.Implementation` is the current realized state of a system
- may live in code, CLI, skills, data, notes, or any combination depending on the project type

****

## Progress.Gradient

- `Progress.Gradient` is the current best direction of movement between `Current.Implementation` and `Design.Target.Model`
- the project is never finished — working is moving in the direction of the gradient
- being unfinished is acceptable when a credible gradient exists
- related to but distinct from `Placement.Balance` (spatial equilibrium across surfaces) — `Progress.Gradient` is directional/temporal

****

## Design.Implementation.CoEvolution

- `Design.Implementation.CoEvolution` is the development dynamic where design understanding and implementation reshape each other
- progress means co-developing `Design.Target.Model` and `Current.Implementation`
- neither side is frozen — implementation reveals design gaps, design reshapes implementation direction
