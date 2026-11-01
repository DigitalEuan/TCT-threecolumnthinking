# 06 — cent_compiler run: £ → ¢ → ∆ (TCT §12)

## £ — Abstract Intent

Compile *"derive a constant from first principles"* into primitives. The
compiled shape is always the same and is what the six scripts execute:
**a term generator (`recip`/`mult`), an accumulator (`sum`), and an error
certificate (`sat`, `eq`) that turns a limit into a rational interval.**

## ¢ — Intermediate representation (v2, post-optimization)

| Primitive | Role in constant derivation |
|---|---|
| `sum` | the series accumulation (Mercator, factorial, BBP, t-series…) |
| `recip` | term generation: 1/k!, 1/k², 1/(2k+1)² — the series' atoms |
| `mult` | term scaling (16^−k, x^(2k+1) denominators, tail factors) |
| `sat` | bounding: alternating/telescoping/integral certificates clamp the error |
| `eq` | identity checks: Cassini, Pell, digit-block matching, interval overlap |
| `rate` | the convergence rate — what makes the certificate shrink (and what every speed record for π digits chases) |

Cost: v1 (9 primitives) → v2 (6), witnesses preserved (docs/07).

## ∆ — Physical substrates: where the constants *live*

The cross-domain question for constants is not "how to compute" but "why
these numbers appear in physics" — each constant is an invariant that some
physical symmetry charges rent for:

| Constant | Physical realization | License |
|---|---|---|
| π | rotations & waves: pendulum periods, diffraction rings, LC circuits | licensed (periods of circular motion) |
| e | growth & decay: RC discharge, radioactive decay, compound processes | licensed (the eigenfunction of d/dt) |
| φ | Fibonacci phyllotaxis; continued-fraction "most irrational" (KAM stability!) | licensed for phyllotaxis; the KAM link is structural |
| √2 | equipartition ratios; square geometries | licensed |
| ζ(2) | random-walk return statistics; black-body energy (Planck sums!) | licensed (Boltzmann/Planck sums) |
| ζ(3) | Feynman diagram values (periods of algebraic varieties) | conjectural-as-explanation (research-level) |
| γ | entropy/statistical-mechanics asymptotics | conjectural-as-explanation |
| α | coupling strength of EM | **physical; refusal carried** (trilogy) |

### Inverse mapping (∆ → £)

Physics hands back *why the constants are worth deriving* — they are the
exchange rates of symmetry. The derivation direction remains the £ pipeline
above: definitions/theorems + certificates. The one constant that resists
both directions is the one that was never mathematical: α stays measured.

## License ledger (§12)

| Analogy | License | Status |
|---|---|---|
| π ↔ rotation/wave periods | physical law | licensed |
| e ↔ d/dt eigenfunction (decay/growth) | physical law | licensed |
| ζ(2) ↔ Planck/Boltzmann sums | physical law | licensed |
| φ ↔ phyllotaxis / KAM | observed / structural | licensed (phyllotaxis), structural (KAM) |
| ζ(3), γ ↔ physics "explanations" | research-level | **conjectural** — recorded, not asserted |
| α ↔ derivable from math | none | **REFUSED: WOULD_BE_GUESS** |
