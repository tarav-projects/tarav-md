# Drift.POI — Appendix

****

## Drift.POI/Appendix

- the economics: the CPU stands watch continuously and agents deploy on alarm rather than on schedule — staling and contradiction become both more visible and cheaper to police ^20260711-7
- the verification gradient: test suites (CPU, behavioral verdicts) → skw checker (CPU, POIs over declared semantic dependencies) → ambient agentic sweeps (global non-contradiction with index and chat); each cheap layer triggers the costlier one ^20260711-7
- annotations give the checker what tests structurally cannot see: semantic design/impl drift ^20260711-7
- reporting weighs provenance (`Touched.Authority`): a POI on grounded content is the loud alarm; a POI on the agent's own untouched notes is quiet maintenance ^20260711-7
- implementation follow-up: the shipped checker's `derived-stale` is verdict-flavored naming for what is a POI — rename when the annotated backend lands ^20260711-7
- the [DF] is deliberately narrow (dependency-change POIs only); other checker outputs remain findings — generalize under evidence ^20260711-7
