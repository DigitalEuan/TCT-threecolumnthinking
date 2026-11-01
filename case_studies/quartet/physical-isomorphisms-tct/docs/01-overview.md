# 01 — Overview: physical functions as isomorphisms into computational systems

## The question

Can physical functions be mapped as isomorphisms onto computational systems in
ways that produce **measurable improvement**? And which computational hurdles
can be overcome — or worked around — by doing so?

Short answer: **yes, in five measurable ways, under five preconditions — and
no, not the one way everyone secretly hopes for.** Physical isomorphisms buy
constant factors, latency, amortization, sampling quality, and continuous
time. They do not buy complexity classes.

## What "isomorphism" means here

A map `φ` from a physical state space to a computational state space that
preserves the *structure that does the work*:

```
φ(x ∘ y) = φ(x) ★ φ(y)
```

where `∘` is a physical interaction and `★` the computational operation it
stands for. Examples (all licensed engineering practice, see docs/06):

| Physical `∘` | Computational `★` | Primitives |
|---|---|---|
| currents meeting at a wire node (Kirchhoff) | addition of products | `sum`, `mult` |
| light through a lens pair (4f system) | Fourier transform | `spatial`, `mult` |
| a noisy bit source | Bernoulli sampling | `rate` |
| an RC op-amp integrator | ODE integration step | `accum`, `state_space` |
| a spin glass relaxing | gradient-free minimization | `state_space`, `sat`, `hysteresis` |

The map is an isomorphism *only with respect to the preserved structure* —
that qualifier is where all the engineering lives (noise, precision, I/O).

## The five measurable gains (each computed exactly in this study)

1. **Constant factors — energy per operation.** Physics performs arithmetic
   for free: a crossbar wire sums currents in the same instant regardless of
   fan-in. Model: 6419× energy per MAC-equivalent vs. von-Neumann digital,
   69× vs. in-memory digital (`scripts/column3/01`).
2. **Latency — physical time replaces sequential time.** A Fourier transform
   by diffraction takes one propagation step, not 51200 ops (`scripts/column3/02`).
   An analog computer integrates an ODE in continuous time: 1500 digital Euler
   steps vs. 1 physical evolution at a 1/1000 error floor (`scripts/column3/04`).
3. **Amortization — the asymptotic-by-reuse game.** A physical setup cost
   (kernel programming: N² writes) is paid once; per-use cost is ~O(1).
   Break-even is exact and honest: T ≥ 21 reuses for the optical filter
   (`scripts/column3/02`).
4. **Sampling quality — true randomness is free.** Physical noise *is* a
   Bernoulli sampler; streams estimate values with exact binomial tails, and a
   stream multiplier is one AND gate (`scripts/column3/03`).
5. **Structure exploitation — NP-hard landscapes, heuristically.** Ising
   machines map combinatorial objectives to physical energy and let physics
   search. Honest status: heuristic; **no proven asymptotic speedup**
   (`scripts/column3/06`, docs/05).

## The five preconditions for a real gain

1. **Structure match** — the workload's dominant operation must be one the
   physics does natively (`sum`, `mult`, `grad`, `state_space`…).
2. **Reuse / amortization** — setup cost must be spread over enough uses
   (T ≥ 21 in our optical model).
3. **Precision sufficiency** — analog delivers ~6–10 bits; if the task needs
   32-bit, converter passes multiply cost (break-even shifts 55 → 228).
4. **I/O discipline** — conversions (DAC/ADC) must not eat the compute saved;
   they dominate at small N.
5. **Complexity honesty** — an isomorphism is a change of substrate, not of
   complexity class (extended Church-Turing, carried as an axiom); the quantum
   case is genuinely open and is *not* claimed here.

## What physical isomorphisms cannot do (docs/05)

- Turn NP-hard into P (structure-preserving maps preserve hardness;
  SAT→Ising keeps the exponential search; our mapping is exact and its cost
  — cubic terms needing gadgets — is computed, not hidden).
- Beat the noise/precision floor without paying (drift, calibration,
  reproducibility).
- Remove the cost of getting data in and results out.
- Serve irregular control flow; digital logic is unbeaten there.

## Why this is a TCT/cent study

The question is the cent_compiler's home terrain (TCT §12): compile the
intent (solve a computational problem) into the 22-primitive `¢` vocabulary,
realize it across the eight physical domains `∆`, solve where it is cheap,
map back. The full £ → ¢ → ∆ run is docs/06; the license ledger (37 licensed,
3 conjectural analogies) is `scripts/column3/05` and `ledgers/`.
