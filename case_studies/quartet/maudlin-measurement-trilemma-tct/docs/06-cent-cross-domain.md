# 06 — cent cross-domain mode (£ → ¢ → ∆)

The trilemma is hard *as stated* only because quantum theory is the domain.
Compiled to the 22-primitive ¢ vocabulary (TCT §12), the same structure
realizes in a fluidic/mechanical domain where it is trivial to see. Status of
the mapping: **conjectural** — each analogy is recorded as a sorry-class item
in the cent ledger, not asserted.

## £ — Abstract Intent

Goal: understand what "a measurement with a single outcome" demands of a
dynamics. Operation to compile: *a continuous quantity reaching a decision
device that must latch exactly one of several branches.*

## ¢ — Intermediate representation

Decomposition of the quantum measurement interaction (post-optimization v2,
`cent/decomp_v2.json` — 6 primitives):

| Primitive | Class | Role in the measurement interaction |
|---|---|---|
| `state_space` | composite | the composite system (electron ⊗ detector) and its amplitude field |
| `sum` | atomic | superposition: amplitudes of alternatives add |
| `mult` | atomic | Born weighting: branch weight = amplitude squared / norm |
| `eq` | composite | orthogonality of pointer states: branches are disjoint |
| `sat` | atomic | saturation: an outcome register accepts exactly one value |
| `hysteresis` | atomic | the record latches: the outcome does not un-happen |

Cost: v1 (12 primitives) → v2 (6 primitives) after one optimization
iteration, all witnesses preserved (docs/07).

## ∆ — Physical substrates: two isomorphisms

**∆1 — Fluidic fork + latch (script 06, `scripts/column3/06_cent_fluidic_latch.py`).**
Input flow 1 meets a symmetric fork: branch flows 1/2 and 1/2 (that is `sum` +
`mult`). A latch downstream must select exactly one outflow (`sat` +
`hysteresis`). With the symmetric flows alone, the latch finds a **tie**
(`1/2 − 1/2 = 0`) and selects nothing: *linear symmetric dynamics + complete
state (flows only) ⇒ no single outcome.* Adding one extra variable —
asymmetry ε = 1/1000 (declared illustrative) — the latch selects branch A
deterministically. The extra variable is exactly what a
complete-state-only description lacks: **the Bohmian door, in fluidic dress.**

**∆2 — Mechanical double-well (conjectural, verbal).** A ball in a symmetric
double well with no noise stays in superposition-like indifference at the
unstable midpoint; any asymmetry (extra variable) or noise (collapse-like
perturbation) sends it to one well (`hysteresis`). Many-worlds corresponds to
taking both wells as equally real outcomes; collapse corresponds to a random
kick; Bohm corresponds to a tiny fixed initial offset.

**Inverse mapping (∆ → £).** In every domain, the same three-way trade
resolves: give the decision device an extra variable (Bohm), give the
dynamics an irreversible stochastic term (collapse), or accept that both
branches are outcomes (many-worlds). The structure "three doors" is not
specific to quantum theory — what is domain-specific is *which* trade the
physics makes cheap.

## Cent ledger

| Analogy | License | Status |
|---|---|---|
| superposition = flow split (`sum`, `mult`) | physical analogy (conservation of flow vs. unit norm) | conjectural — sorry-class |
| orthogonality = disjoint pipe support (`eq`) | structural | conjectural — sorry-class |
| outcome = latch (`sat`, `hysteresis`) | structural | conjectural — sorry-class |
| tie without extra variable = outcomelessness | re-derived exactly in script 06 (ℚ arithmetic) | verified within the analogy |
| ε-asymmetry = hidden variable | structural | conjectural — sorry-class |

The script's arithmetic (flow conservation, tie, tie-breaking) is exactly
verified; the *identification* with quantum structure is the conjectural part.
Per TCT §12: an unlicensed analogy is recorded as `sorry`/gap, not asserted.
