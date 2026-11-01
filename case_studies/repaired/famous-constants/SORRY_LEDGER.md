# Development-required ledger — tct_constants

- lemmas total: 9
- proved (sorry-free): **6**
- `sorry` (development required): **3**
- axioms: **7**
- definitions: 2

## sorry lemmas

- `zeta2_tail_symbolic` : `∀ (N : ℕ), 0 < N → (1:ℚ)/(N+1) < 1/N`
  - gap: requires linarith/order reasoning over ℚ (Mathlib) or manual cross-multiplication; general shape of the tail sandwich verified concretely in scripts/column3/03_zeta2_basel.py
- `gamma_rational_target` : `∀ (g : ℚ), g = 5772156649 / 10^10`
  - gap: DELIBERATE TARGET, EXPECTED UNPROVEN: gamma has no known closed form and its irrationality is itself an OPEN problem (Erdos prize). Any proof would show gamma rational — believed false. This sorry marks the class-O boundary: constants definable and computable to any precision yet not closed-form-derivable
- `alpha_physical_target` : `∀ (a : ℚ), a = 72973525693 / 10^13`
  - gap: DELIBERATE TARGET, EXPECTED UNPROVEN (trilogy link to speed-of-light-derivation-tct): no accepted parameter-free derivation of the fine-structure constant. Numerology-class claims are registered REFUSED: WOULD_BE_GUESS in the ledgers

## axioms (assumed)

- `pi_definition` : `Prop` — definitional: pi is the circle ratio (equivalently, twice the smallest positive zero of cosine)
- `e_definition` : `Prop` — definitional: e = lim_{n->inf} (1 + 1/n)^n = sum 1/k!
- `analysis_convergence_premises` : `Prop` — analytic premises (provable in analysis/Mathlib, not carried in pure core): alternating-series error bounds, telescoping and integral tail bounds
- `euler_basel_identity` : `Prop` — Euler 1735: comparing coefficients in the sine product gives sum 1/n^2 = pi^2/6 (and pi^4/90 for n^4)
- `apery_theorem` : `Prop` — Apéry 1979: zeta(3) is irrational (theorem; no closed form known)
- `gelfond_schneider` : `Prop` — Gelfond-Schneider theorem: e^pi is transcendental (theorem; assumed)
- `physical_constants_empirical` : `Prop` — empirical/definitional: alpha is measured (CODATA 2018); c and h are SI-defined (2019); G is measured. No accepted parameter-free derivation exists for any of them

## To verify

```bash
cd lean/tct_constants && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
