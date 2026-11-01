# 03 — The three-column contract

The three columns describe the **identical logical steps**. Domain: ℤ / ℚ
(and declared GF(2) sites in script 04). UBP: `int`/`Fraction` only; XOR only
over declared 𝔽₂ symplectic sites; no floats, no random, no SHA-256.

**Givens.** c_SI = 299,792,458 m/s (definitional); WK/Fizeau/Foucault values
(empirical); α = 72973525693/10^13 ± 11 (empirical); wave grid Δx = Δt = 1;
Clifford circuit L = 8, 6 layers; J ∈ {1/2, 3/4}, a = 1.

| Step | Plain English | Mathematics | Python (this step) | Lean |
|---|---|---|---|---|
| 1 | the definition of the meter through c | 1 m = 1/299792458 light-second | 01: `M_IN_LIGHTSECONDS` | `si_definition_c` (axiom) |
| 2 | the light-year, from the definition alone | 299792458 · 31557600 = 9460730472580800 | 01: `LIGHT_YEAR_M` | `light_year_m` (proved) |
| 3 | the nanosecond in centimeters | 299792458·100/10⁹ = 149896229/5000000 | 01: `NS_CM` | `ns_cm` (proved) |
| 4 | the verdict on steps 1–3 | bookkeeping: no empirical input | 01: `DEFINITIONAL=1` | — |
| 5 | the Weber–Kohlrausch difference from the modern value | 310740000 − 299792458 = 10947542 | 02: `diff_wk` | `wk_diff` (proved) |
| 6 | the exact relative differences | 5473771/149896229 etc. (reduced, two paths) | 02: `REL_DIFF_*` | — |
| 7 | the era agreement of all three determinations | max rel. diff < 1/20 | 02: `ERAS_AGREE=1` | `wk_within_era` (proved) |
| 8 | the wave scheme on the integer grid | u_{t+1}(x) = u_t(x+1) + u_t(x−1) − u_{t−1}(x) | 03: `evolve_dict`/`evolve_list` | `wave_scheme_represents_wave` (axiom) |
| 9 | the agreement of the two evolutions | dict ≡ matrix-list at all t ≤ 20 | 03: `PATHS_AGREE=1` | — |
| 10 | the light cone of the scheme | supp ⊆ \|x\| ≤ t; edge +1 cell/step | 03: `CONE_BOUND=1`, `EDGE_SPEED=1` | — |
| 11 | the emergent invariant speed on this grid | v = Δx/Δt = 1 exactly | 03: `SUPPORT_T20=19` | — |
| 12 | the Clifford brickwork circuit | H/S/CNOT on L = 8; Y start at site 3 | 04: circuit | — |
| 13 | the two exact propagations agree | label rules ≡ GF(2) symplectic matrices | 04: `PATHS_AGREE=1` | — |
| 14 | the circuit light cone | growth ≤ 1 site/layer/side | 04: `CONE_BOUND=1` | — |
| 15 | the Lieb–Robinson velocity at J = 1/2, a = 1 | v = 2Ja = 1 (two paths) | 05: `V_LR=1` | `lr_bound_nonneg` (sorry: symbolic) |
| 16 | the bound dominates both observed cones | v_LR ≥ 1 = observed; tight | 05: `BOUND_TIGHT=1`, `FRAMEWORKS_MATCH=1` | — |
| 17 | the dimensionless value of c in atomic units | c = 1/α = 10¹³/72973525693 | 06: `INV_ALPHA` | `alpha_codata` (def) |
| 18 | the floor of 1/α by two paths | 137·72973525693 ≤ 10¹³ < 138·72973525693 | 06: `INV_ALPHA_FLOOR=137` | `alpha_floor` (proved) |
| 19 | the uncertainty interval of 1/α | [1/(α+δ), 1/(α−δ)], width exact | 06: `INTERVAL_OK=1`, `WIDTH` | `inv_alpha_interval_general` (sorry: symbolic) |
| 20 | the boundary verdict: α given vs. α derived | from α: exact; from theory: none | 06: `ALPHA_FROM_THEORY=0` | `alpha_from_premises` (sorry: deliberate) |
| 21 | the existence of an invariant speed from causality | relativity+homogeneity+isotropy+causality ⇒ κ ≥ 0 | — | `ignatowski_premises` (axiom) |
| 22 | the naive claim, refused | "value derivable from nothing" | 06: `REFUSAL_REGISTERED=1` | — |

**UBP compliance.** `int`/`Fraction` only; XOR confined to declared 𝔽₂ sites
(script 04 symplectic path); no floats, no random, no SHA-256.

**Decomposition.** 22 atomic claims: 11 proved, 3 sorry, 7 axioms, 1 refused
(docs/02).

**Full Column 3 scripts:** `scripts/column3/01…06_*.py`; outputs
`verification/tier1-run.txt`.

**Verification.** Python: **VERIFIED** 6/6, isolated subprocesses (asserts
caught two hand-arithmetic slips in draft constants — corrected to computed
values). **Lean:** 5 proved, 3 sorry (`lr_bound_nonneg`,
`inv_alpha_interval_general`, `alpha_from_premises` — the last is the
deliberate boundary), 7 axioms. `lake build`: not run here; ready at
`lean/tct_lightcone/`.
