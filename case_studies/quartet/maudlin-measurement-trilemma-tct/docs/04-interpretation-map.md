# 04 — Interpretation map: what each door costs

The trilemma's payoff: ask not "which interpretation is true?" but "what does
each interpretation pay?" Every one of them pays. The disagreement is over
which price is the most reasonable.

## The three doors (from the truth table)

Source of truth: `scripts/column3/05_doors_truth_table.py` —
the doors are exactly the three valuations of (C1, C2, C3) with two claims
kept and one sacrificed.

### Door 1 — Many-worlds (Everett 1957) — keeps C1, C2; sacrifices C3

- **Mechanism.** No collapse, no hidden variables, no special role for
  measurement. The universal wavefunction just evolves linearly. A detector
  interacting with a superposed electron genuinely enters a superposition of
  readings; decoherence makes the branches effectively independent.
- **What is reinterpreted.** The single outcome you experience is one branch's
  record. Everettians (Deutsch 1999; Wallace 2012) argue this is not a loss:
  each observer sees one result within their branch, and the Born rule can be
  recovered by decision theory.
- **What is owed.** Critics (e.g. Maudlin; Albert; Kent) argue the theory owes
  an account of *probability* — in a deterministic branching multiverse, in
  what sense do weights 1/2 and 1/2 mean anything? — and of why branch
  weights, not branch counts, govern experience. Formal record in this study:
  Lean `everett_emergence_gap` (sorry, deliberate).
- **Price.** A strange view of outcomes: they are all real.

### Door 2 — Objective collapse (GRW 1986; Diósi 1989; Penrose 1996) — keeps C1, C3; sacrifices C2

- **Mechanism.** The wavefunction is complete and outcomes single; the price
  is in the dynamics. GRW: each particle undergoes a spontaneous localization
  at rate `λ ≈ 10^−16 s^−1` (empirical parameter, Lean `grw_lambda_empirical`);
  a macro object of `N` particles experiences the amplified rate `N·λ`.
- **Exact arithmetic (script 03).** Mean time between collapses:
  `τ = 1/(Nλ) = 10^16/N` seconds.
  - single particle: `τ = 10^16 s ≈ 3.17 × 10^8 years` (exact:
    `12500000000000/39447` years);
  - macro object, illustrative `N = 10^23`: `τ = 10^−7 s` — collapse is
    effectively instantaneous, so large objects are always found in one place;
  - threshold: `τ = 1 s` exactly at `N = 10^16` particles.
- **Diósi–Penrose variant.** Collapse is not a new stochastic law but gravity:
  a superposition of significantly different mass distributions decays on a
  timescale of order `τ ≈ ħ/E_G`, with `E_G` the gravitational self-energy of
  the difference between the branches. (Parameter carried as an axiom-class
  premise; not computed here.)
- **Price.** A change to the most tested equation in physics: the
  Schrödinger equation is amended (nonlinear, stochastic), and the change must
  be engineered to leave all tested physics intact.

### Door 3 — Bohmian mechanics (Bohm 1952; Bell 1987) — keeps C2, C3; sacrifices C1

- **Mechanism.** Two ingredients: the wavefunction (always linear, always) and
  definite particle positions. ψ guides the particles via the guiding equation;
  the particle configuration is the "hidden variable" that makes one outcome
  actual. The detector's needle has a position; its position is what picks
  which term of the superposition you see.
- **What is preserved.** Exactly the empirical content of quantum mechanics
  (equivariance: |ψ|² statistics for the particle distribution), and a clean
  account of single outcomes.
- **Price.** The wavefunction is not the complete physical state — an added
  ingredient — plus explicit nonlocality (Bell's theorem shows no theory with
  definite outcomes can be local).
- **Tie-breaking, cross-domain (script 06).** The fluidic fork with equal
  flows cannot latch (a tie); an extra variable ε breaks the tie and the latch
  selects deterministically. This is the Bohmian structure in another domain —
  recorded as a conjectural analogy (docs/06).

## Sidesteppers (not doors — relocations of the claims)

### QBism — rejects C1 in a radical way

The wavefunction is not a physical state at all; it encodes an agent's
expectations for their experiences (Caves–Fuchs–Schack 2002; Fuchs–Mermin–Schack
2014). The trilemma dissolves because C1 was never on the table: "completeness"
of an expectation book says nothing about the world. Outcomes are personal,
but the world is not created by observation; the theory is a normative tool
for agents inside the world.

### Relational quantum mechanics (Rovelli 1996) — keeps outcomes, relativizes them

There is no absolute state of the detector: a physical system's state is
relative to another system. The detector has a definite reading *relative to
the observer who interacted with it*, and no fact of the matter about the
distant detector until interaction. The trilemma's C3 survives, but as a
relational fact.

## Cost ledger (summary)

| Family | Sacrificed claim | Pays with | Formal status here |
|---|---|---|---|
| Many-worlds | C3 (single outcomes) | probability + emergence of outcomes | `everett_emergence_gap` (sorry) |
| GRW / Diósi–Penrose | C2 (linearity) | modified dynamics + new parameter(s) | `grw_lambda_empirical` (axiom); script 03 verified |
| Bohm | C1 (completeness) | added ingredient (positions) + nonlocality | script 06 analogy (conjectural) |
| QBism | C1 (physicalist reading) | instrumentalism about ψ | axiom-class, docs |
| RQM | C3 (absolute outcomes) | relational facts only | axiom-class, docs |

The disagreement among physicists and philosophers is about which column of
this table is the least expensive — that is, which claim they are least
willing to give up.
