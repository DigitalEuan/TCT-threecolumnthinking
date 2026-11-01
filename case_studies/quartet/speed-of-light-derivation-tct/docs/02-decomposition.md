# 02 — Decomposition: 22 atomic claims, classified

Classification identity (TCT §14 condition 1): `n = p + s + a + r` →
**22 = 11 + 3 + 7 + 1**. The single refused claim is the naive heart of the
question — refusing it is a result, not a failure.

## Givens (declared; empirical where marked)

- c_SI = 299,792,458 m/s (**definitional**, BIPM SI); Julian year = 31,557,600 s.
- Historical determinations (**empirical**): WK 1856 = 310,740,000;
  Fizeau 1849 = 313,300,000; Foucault 1862 = 298,000,000 (m/s).
- α = 72973525693/10^13 ± 11 last-digits (**empirical**, CODATA 2018).
- Scheme parameters: wave grid Δx = Δt = 1; Clifford circuit L = 8,
  6 layers, Y start at site 3; LR couplings J ∈ {1/2, 3/4}, a = 1.

## Proved (11) — Python VERIFIED; Lean proved where a lemma exists

| # | Claim | Witness |
|---|---|---|
| 1 | definitional chain: light-second/Year/ns distances exact | 01 `LIGHT_YEAR_M=9460730472580800`, `NS_CM`; Lean `light_year_m`, `ns_cm` |
| 2 | the SI number is definition, not derivation (`DEFINITIONAL=1`) | 01 |
| 3 | exact relative differences of the three determinations | 02 `REL_DIFF_*`; Lean `wk_diff` |
| 4 | era agreement at < 1/20 (5%) | 02 `ERAS_AGREE=1`; Lean `wk_within_era` |
| 5 | wave scheme: dict path ≡ matrix path at all t ≤ 20 | 03 `PATHS_AGREE=1` |
| 6 | wave cone: support bound \|x\| ≤ t; edge speed exactly 1/step | 03 `CONE_BOUND=1`, `EDGE_SPEED=1`, `SUPPORT_T20=19` |
| 7 | Clifford: label rules ≡ GF(2) symplectic propagation at all layers | 04 `PATHS_AGREE=1` |
| 8 | Clifford cone: support growth ≤ 1 site/layer each side | 04 `CONE_BOUND=1`, `SUPPORT_LE_LAYER=1` |
| 9 | LR bound: v = 2Ja = 1 (J = 1/2), tight; ≥ observed cone speeds | 05 `V_LR=1`, `BOUND_TIGHT=1`, `FRAMEWORKS_MATCH=1` |
| 10 | 1/α from α: floor 137 by two paths; c = 1/α in atomic units | 06 `INV_ALPHA_FLOOR=137` |
| 11 | exact uncertainty inversion and width of the 1/α interval | 06 `INTERVAL_OK=1`, `WIDTH` |

## Sorry (3) — named gaps, development required

| # | Claim | Gap |
|---|---|---|
| 12 | `lr_bound_nonneg` — symbolic nonnegativity of 2Ja | positivity (`mul_nonneg`, Mathlib) |
| 13 | `inv_alpha_interval_general` — interval inversion for all bounds | `field_simp` + order reasoning |
| 14 | `alpha_from_premises` — **deliberate target, expected unproven**: parameter-free derivation of α | the open problem itself (Eddington-lineage programs); the formal boundary of the study |

## Axioms (7) — named premises

| # | Name | Premise |
|---|---|---|
| 15 | `si_definition_c` | c = 299,792,458 m/s exactly (definitional) |
| 16 | `maxwell_em_wave_speed` | EM waves at 1/√(μ₀ε₀) (Maxwell 1865) |
| 17 | `historical_determinations_empirical` | WK/Fizeau/Foucault values measured |
| 18 | `ignatowski_premises` | relativity+homogeneity+isotropy+causality ⇒ invariant speed exists |
| 19 | `lieb_robinson_theorem` | signal bound v = 2Ja for lattice Hamiltonians |
| 20 | `alpha_empirical` | α measured (CODATA 2018) |
| 21 | `wave_scheme_represents_wave` | the integer scheme faithfully discretizes the wave equation |

## Refused (1)

| # | Claim | Refusal |
|---|---|---|
| 22 | "c's numeric value (equivalently α) is derivable computationally from theory alone" | **`WOULD_BE_GUESS`** — no exact derivation path exists; any claimed one lacks a licensed derivation and is numerology-class until it predicts independent constants parameter-free. (Script 06 stamps `ALPHA_FROM_THEORY=0`, `REFUSAL_REGISTERED=1`.) |

## The four conditions (§14) — report

1. **Classification identity.** 22 = 11 + 3 + 7 + 1. ✓
2. **Independent cross-checks.** 14 cross-checks across the six scripts
   (Fraction vs. gcd; dict vs. matrix; label-rules vs. symplectic GF(2);
   closed formula vs. interaction sum; division vs. cross-multiplied
   inequalities). 1 tautology-class artifact removed in pre-verification
   cleanup (an inert comment-block in script 03's draft); `c − t = 13 ≥ 2`. ✓
3. **Optimization-loop acceptance.** ¢ pipeline 10 → 7 primitives, witnesses
   preserved (2 cone keys re-verified), accepted; second proposal (drop
   `spatial`) rejected — the cone-support witness would lose its meaning. ✓
4. **Named ledger.** 3 sorry with exact gaps (incl. the deliberate boundary);
   7 named axioms; 1 refusal with named reason. `WOULD_BE_GUESS` appears
   exactly once — as the study's conclusion about the naive claim. ✓
