# 05 — Guardrails: what physical isomorphisms cannot do

The study's value depends on keeping its negative results as loud as its
positive ones.

## G1 — Complexity classes do not move

A structure-preserving map from a computational problem to a physical system
does not change the problem's complexity class — it changes the *cost model's
constants* and which operations are cheap. The extended Church-Turing thesis
(any physical system can be simulated efficiently by a digital computer) is
carried as an axiom (`physical_church_turing`); under it:

- NP-hard stays NP-hard: the SAT→Ising map (script 06) is exact and preserves
  the search space — 8 assignments of the toy instance map to 8 energy
  evaluations; for n variables it is 2ⁿ either way.
- "The physics searches in parallel" is real but bounded: massive constant
  parallelism ≠ asymptotic escape. Reported annealer/Ising speedups over
  optimized classical baselines remain **contested and instance-dependent** —
  this study claims none.

**The open exception: quantum.** If BQP ⊄ BPP, quantum substrates would
change classes for some problems (factoring, simulation). That is *unknown*;
no claim about it appears in any ledger here. The honest position: the
isomorphism framework measures classical physical speedups exactly and
carries the quantum case as open.

## G2 — Noise and precision floors

Analog computes at 6–10 effective bits with drift, temperature dependence,
and device variation. Floors are floors: below them, no isomorphism helps;
at them, digital refinement passes are the workaround (and cost exactly —
break-even 55 → 228 at 32-bit, script 01). Physical systems also drift after
calibration, so reproducibility is a recurring maintenance cost — the one
"cost" our integer models deliberately exclude and this text explicitly
restates.

## G3 — I/O and conversion overhead

Nothing is free at the boundary: DAC/ADC conversions dominate small-N
workloads (the break-even N = 55 exists *because* of 7400N conversion terms).
Data must still get in and results must still get out; for streaming workloads
this is amortized, for one-shot problems it can eat the whole win.

## G4 — Irregular logic and control flow

Branchy, exact, high-precision, or irregular workloads (databases, compilers,
cryptography's exact arithmetic) are digital's home turf. Physical
isomorphisms match *structure*: dense linear algebra, dynamics, sampling,
physical fields. Outside that envelope the mapping is contrived and the
measurement would be `WOULD_BE_GUESS` — refused without a cost model.

## G5 — Setup, programmability, and build cost

Physical solvers are special-purpose (H8). Below the amortization break-even
(T = 21 in our optical model), general-purpose digital wins outright. Any
"speedup" claim that does not state its reuse count is incomplete by
construction.

## How this study handles over-claiming

| Tempting claim | Disposition |
|---|---|
| "Analog AI is 1000× faster" | `WOULD_BE_GUESS` unless a cost model + accuracy target is declared |
| "Ising machines solve NP-hard problems" | rephrased: heuristics with parallel search; no class claim (06 `EQUIVALENCE` shows only mapping exactness) |
| "Optics makes convolution O(1)" | verified only with amortization: T ≥ 21 and per-frame readout terms (02) |
| "Quantum computers break complexity" | not claimed; carried as open in `physical_church_turing`'s note |
| 8-bit analog vs 64-bit digital comparison | `DIFFERENT_SCALES` unless conversion is modeled (01 models it as 4 passes) |
