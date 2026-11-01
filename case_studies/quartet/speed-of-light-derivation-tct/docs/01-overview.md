# 01 — Overview: deriving the speed of light computationally

## The question, and why it fights back

"How can the speed of light be derived computationally?" looks like one
question. It is at least four, and they have different answers:

| # | Question | Answer |
|---|---|---|
| B1 | Can a computation produce the number 299,792,458? | Yes — trivially. It is **defined** (SI). Bookkeeping, not derivation. |
| B2 | Can a computation derive that light's speed is an *electromagnetic* speed? | Yes — historically done: c = 1/√(μ₀ε₀) vs. optical determinations (Weber–Kohlrausch 1856). Empirical inputs required. |
| B3 | Can a computation derive that an **invariant maximum speed exists** — a light cone? | Yes — three independent ways, exactly enumerable: discrete wave dynamics, Clifford circuit dynamics, Lieb–Robinson bounds. |
| B4 | Can a computation derive the **dimensionless value** (α, hence c in natural units) from nothing? | **No — open problem.** Named refusal: `WOULD_BE_GUESS` for any claim otherwise. |

The payoff of facing the boundaries one at a time: the question's naive form
("derive the number") dissolves, and what remains is sharp —
**computation derives the *structure* (an invariant speed, a light cone, an
EM identification); measurement supplies exactly one dimensionless number.**

## B1 — The number is a definition

Since 1983 (and 2019 SI revisions), c = 299,792,458 m/s **exactly**: the meter
is *defined* as the distance light travels in 1/299,792,458 s. Any script
printing that number is unfolding a definition. Script 01 computes the whole
definitional chain exactly (light-second, light-year = 9,460,730,472,580,800 m,
nanosecond = 149896229/5000000 cm) and stamps it `DEFINITIONAL=1`.

## B2 — The historical derivation: c from electromagnetism

Maxwell (1861–65) showed transverse EM waves propagate at 1/√(μ₀ε₀), and the
Weber–Kohlrausch ratio of EM to electrostatic charge units (1856) numerically
matched the measured speed of light — the inference that light *is* EM waves.
This is the genuine "computational derivation" of c in the 19th-century sense:
**compute from electrical measurements, compare with optical ones.** Script 02
does the comparison exactly:

- Weber–Kohlrausch 1856: 310,740,000 m/s → 36,517 ppm off the modern value
- Fizeau 1849: 313,300,000 m/s → 45,056 ppm
- Foucault 1862: 298,000,000 m/s → 5,978 ppm

All three agree with the modern value at the ~5% level of their era
(`ERAS_AGREE=1`, exact fractions). Note the shape: the derivation needed
*measured* constants — it never produced the value from nothing.

## B3 — The structural derivations: light cones from computation

Three independent computational frameworks derive that a maximum signal speed
**exists**, and compute it exactly:

1. **Discrete wave equation (script 03).** The exact integer scheme
   `u_{t+1}(x) = u_t(x+1) + u_t(x−1) − u_{t−1}(x)` has characteristics that
   move exactly one cell per step: an invariant speed = Δx/Δt **emerges from
   the dynamics**, enumerable to t = 20 with the support edge advancing
   exactly 1/step (`EDGE_SPEED=1`, `CONE_BOUND=1`).
2. **Clifford circuit dynamics (script 04).** In an exact GF(2) brickwork
   circuit, Pauli operators spread at most one site per layer — a light cone
   in a purely discrete, finite system, verified by two disjoint
   implementations (label rules vs. symplectic matrices), `PATHS_AGREE=1`.
3. **Lieb–Robinson bounds (script 05).** For a lattice Hamiltonian with
   nearest-neighbor coupling J, signal velocity is rigorously bounded by
   v = 2Ja — an *effective* speed of light computed from a microscopic model.
   At J = 1/2, a = 1: v = 1, exactly the cone speed of both simulations
   (`FRAMEWORKS_MATCH=1`, `BOUND_TIGHT=1`).

Plus the analytic existence route: von Ignatowski (1910) showed that
relativity + homogeneity + isotropy + **causality** force the coordinate law
to contain an invariant speed (κ ≥ 0). Existence is derivable; value is not.

## B4 — The value boundary

In natural units c's value is one dimensionless number: c = 1/α in atomic
units. Script 06 computes this exactly from measured α (CODATA 2018):
1/α = 137.0359... (floor 137, exact uncertainty interval). But that is
bookkeeping *given α* — and **α itself is measured, not derived**. No accepted
parameter-free derivation exists; the long lineage of claimed derivations
(Eddington's 1/137 numerology; modern "purely mathematical" preprints) is
exactly the class this study's taxonomy refuses:

> `REFUSED: WOULD_BE_GUESS — any claimed derivation of α (or of c's
> dimensionless value) without empirical input.`

Formal record: the Lean tier carries `alpha_from_premises` as a **deliberate
`sorry`** — the one theorem this study wants but cannot have. Everything else
in the ledger is proved or honestly axiomatic.

## The answer in one paragraph

The speed of light is derivable computationally in three senses — as the EM
wave speed 1/√(μ₀ε₀) from electrical measurements (B2), as the light-cone
speed Δx/Δt of any faithful discrete dynamics (B3a), and as the rigorous
signal bound 2Ja of lattice Hamiltonians (B3b) — and its existence as an
invariant speed follows from symmetry and causality alone (Ignatowski). Its
*dimensionless value* is not derivable by any known computation (B4): one
measured number (α) enters at the bottom, and the SI value on top is a
definition. The question "derive c computationally" is thus answerable
*structurally* in full and *numerically* not at all — and knowing which is
which is the whole study.
