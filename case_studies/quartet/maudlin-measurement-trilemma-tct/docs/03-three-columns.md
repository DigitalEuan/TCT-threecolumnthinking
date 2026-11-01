# 03 — The three-column contract

The three columns describe the **identical logical steps**, not three different
answers. Domain: ℚ / ℤ throughout (unnormalized integer amplitudes; Born
weights as exact fractions). UBP: Column 3 uses `fractions.Fraction`/`int`
only — no floats, no rounding, no random, no SHA-256, stdlib only.

**Givens.** Electron prepared with amplitudes 1 up + 1 down (weights 1/2, 1/2);
detector with ready state `|D0⟩` and pointer states `|D↑⟩`, `|D↓⟩`;
illustrative `N = 10^23`, `λ = 10^−16 s^−1`, `ε = 1/1000`.

| Step | Plain English | Mathematics | Python (this step) | Lean |
|---|---|---|---|---|
| 1 | the input state of electron and detector, ready | ψ_in = (1)\|↑⟩\|D0⟩ + (1)\|↓⟩\|D0⟩ | 01: `psi_in` dict | given |
| 2 | the measurement interaction on basis states | U(\|↑⟩\|D0⟩) = \|↑⟩\|D↑⟩; U(\|↓⟩\|D0⟩) = \|↓⟩\|D↓⟩ | 01: `apply_U_dict` | given |
| 3 | the application of U to the input, taken termwise | U(ψ_in) = (1)\|↑⟩\|D↑⟩ + (1)\|↓⟩\|D↓⟩ | 01: path A (dict rewrite) | axiom `linearity_entangles` (physical reading) |
| 4 | the same application as a matrix product over the six basis indices | U·vec = (0,1,0,0,0,1)^T | 01: path B (6×6 matrix) | — |
| 5 | the equality of the two applications | outA = outB | 01: `assert`, `LINEARITY_MATCH=1` | — |
| 6 | the amplitude matrix of the output, of shape 2 by 3 | Amp = [[0,1,0],[0,0,1]] | 01: `Amp` | — |
| 7 | the failure of every product-state cross-minor to vanish | ∃ e,f,d,d′: Amp[e][d]·Amp[f][d′] ≠ Amp[e][d′]·Amp[f][d] | 01: `ENTANGLED_MINORS=1` | `entangled_witness_minor` (proved); `product_state_minors` (sorry: symbolic form) |
| 8 | the mixing of the reduced detector state | Tr(ρ_D²) = 2 ≠ 4 = Tr(ρ_D)² | 01: `ENTANGLED_PURITY=1` | — |
| 9 | the agreement of the two reductions of the detector state | ρ_D from tracing ρ_full = Σ_e ψ(e,d)ψ(e,d′) | 02: `REDUCED_AGREE=1` | — |
| 10 | the orthogonality of the two reading branches | ⟨D↑\|D↓⟩ = 0 | 01: `BRANCH_ORTHO=1` | — |
| 11 | the vanishing of all detector coherences | ρ̂_D = diag(0, 1/2, 1/2) | 02: `OFFDIAG_ZERO=1`, `PURITY=1/2` | — |
| 12 | the normalization of the Born weights, two ways | 1/2 + 1/2 = 1 = Tr(ρ̂_D) | 02: `NORMALIZATION=1`; 01: `BORN_SUM=1` | `born_weight_sum` (proved) |
| 13 | the count of nonzero pointer branches under C1 and C2 | \|supp(pointer)\| = 2 | 01: `NONZERO_BRANCHES=2` | — |
| 14 | the requirement of C3 on that count | C3 ⟹ count = 1; 2 ≠ 1 ⟹ ¬(C1 ∧ C2 ∧ C3) | 01: `C3_CONTRADICTED=1` | `trilemma_from_model` (proved from `linearity_entangles`) |
| 15 | the pure-logic skeleton of the trilemma | (C1 ∧ C3 → ¬C2) → ¬(C1 ∧ C2 ∧ C3) | 05: `PAIRWISE_EQUIVALENCE=1` | `trilemma_logic`, `pair_exclusion` (proved) |
| 16 | the enumeration of the eight valuations of the claims | 8 valuations; 7 admissible; 1 excluded | 05: `ADMISSIBLE=7` | — |
| 17 | the count of doors, of exactly two kept claims | C(3,2) = 3 | 05: `DOORS=3` | `door_count := 3` (def) |
| 18 | the GRW collapse time of one particle, in seconds and years | τ = 10^16 s = 12500000000000/39447 yr | 03: `TAU_SINGLE_S`, `YEARS_SINGLE` | `grw_threshold_rate` (proved) |
| 19 | the GRW collapse time of a macro object of 10^23 particles | τ = 10^16/10^23 = 1/10^7 s | 03: `TAU_MACRO_S=1/10000000` | `grw_macro_tau` (proved) |
| 20 | the count of branches after ten binary measurements | 2^10 = 1024 branches of weight 1/1024 | 04: `BRANCHES_10=1024` | `branches_pow10` (proved) |
| 21 | the total weight across all branches | 1024 · (1/1024) = 1 | 04: `TOTAL_WEIGHT=1` | `branch_weight_times_count` (proved); general: `branch_weight_sum_general` (sorry) |
| 22 | the fluidic fork of equal flows, and its tie | 1/2 − 1/2 = 0 ⟹ latch selects nothing | 06: `TIE_NO_OUTCOME=1`, `fluidic_tie` | `fluidic_tie` (proved) |
| 23 | the tie broken by an extra variable ε = 1/1000 | (1/2+ε) − (1/2−ε) = 2ε > 0 ⟹ latch selects A | 06: `ASYMMETRY_OUTCOME=1` | — (analogy, conjectural; docs/06) |

**UBP compliance.** Column 3: `Fraction`/`int` only; no floats, no rounding,
no random, no SHA-256; no XOR sites declared or used; stdlib only.

**Decomposition.** 20 atomic claims: 12 proved, 3 sorry, 5 axioms, 0 refused
(docs/02). Steps 22–23 are the cent cross-domain witness, classified as
conjectural analogy (sorry-class in the cent ledger).

**Full Column 3 scripts:** `scripts/column3/01…06_*.py` (one per module;
each is self-contained and prints `KEY=VALUE`).

**Verification.** Python: **VERIFIED** — 6/6 scripts, isolated subprocess,
exit 0 (`verification/VERIFICATION_REPORT.md`).
**Lean:** 10 proved, 3 sorry, 5 axioms. sorry gaps: `branch_weight_sum_general`
(nonzero-powers lemma), `product_state_minors` (ring normalization),
`everett_emergence_gap` (deliberate: Deutsch–Wallace emergence step).
`lake build`: not run (no toolchain here); project ready at
`lean/tct_maudlin/`.
