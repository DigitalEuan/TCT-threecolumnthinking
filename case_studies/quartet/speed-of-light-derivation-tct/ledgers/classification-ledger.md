# Classification ledger (TCT §14)

Identity: `n = p + s + a + r` → **22 = 11 + 3 + 7 + 1**

## Proved (11) — Python VERIFIED (6/6, isolated subprocesses)

1. definitional chain exact (light-year 9,460,730,472,580,800 m; ns = 149896229/5000000 cm) (01)
2. SI number is definition, not derivation (`DEFINITIONAL=1`) (01)
3. exact relative differences of WK/Fizeau/Foucault vs. modern value (02)
4. era agreement < 1/20 (02)
5. wave scheme: dict ≡ matrix-list at all t ≤ 20 (03)
6. wave cone: support bound + edge speed exactly 1/step; SUPPORT_T20 = 19 (03)
7. Clifford: Pauli-label rules ≡ GF(2) symplectic propagation (04)
8. Clifford cone: growth ≤ 1 site/layer per side (04)
9. LR bound v = 2Ja = 1 at J = 1/2, tight; dominates both observed cones (05)
10. 1/α from α: floor 137 by two paths (06)
11. uncertainty inversion + exact width of 1/α interval (06)

Lean proved (5): `light_year_m`, `ns_cm`, `wk_diff`, `wk_within_era`, `alpha_floor`.

## Sorry (3) — named gaps, development required

- `lr_bound_nonneg` — needs positivity (`mul_nonneg`, Mathlib) or manual cases.
- `inv_alpha_interval_general` — needs `field_simp` + order reasoning.
- `alpha_from_premises` — **deliberate target, expected unproven**: the
  parameter-free derivation of α. This sorry is the study's formal boundary;
  it is the one theorem everyone wants and nobody has.

## Axioms (7) — named premises

- `si_definition_c` — c = 299,792,458 m/s exactly (definitional).
- `maxwell_em_wave_speed` — EM waves at 1/√(μ₀ε₀).
- `historical_determinations_empirical` — WK/Fizeau/Foucault values.
- `ignatowski_premises` — relativity+homogeneity+isotropy+causality ⇒ κ ≥ 0.
- `lieb_robinson_theorem` — signal bound v = 2Ja.
- `alpha_empirical` — α measured (CODATA 2018).
- `wave_scheme_represents_wave` — integer scheme discretizes the wave equation.

## Refused (1)

- "c's numeric value (equivalently α) is derivable computationally from theory
  alone" — **`WOULD_BE_GUESS`**. No licensed derivation path; the numerology
  lineage (Eddington-class and modern preprints) fits measured values with
  free parameters and lacks independent parameter-free predictions. Script 06
  stamps `ALPHA_FROM_THEORY=0`, `REFUSAL_REGISTERED=1`. Additional
  refusal-class dispositions (circular modern formula, digital-physics value
  claims) in docs/05.

## Cross-check register (14 written; 1 dead artifact removed; 13 live)

| Script | Cross-check pairs (disjoint derivation paths) |
|---|---|
| 01 | light-year direct vs. digit-wise product; ns via Fraction vs. manual gcd |
| 02 | rel. diff via Fraction vs. manual gcd (×3); ppm via integer division |
| 03 | dict evolution vs. wide-list matrix evolution (all t ≤ 20); cone via enumeration vs. edge-advance counting |
| 04 | Pauli-label gate rules vs. GF(2) symplectic matrices (all layers); cone via support bounds vs. per-side growth |
| 05 | closed formula vs. interaction-range sum; bound via Fraction vs. cross-multiplied integers |
| 06 | floor via integer division vs. inequalities; interval via reciprocals vs. direction check |

Removed: one inert draft block in script 03 (tautology class). `c − t = 13 ≥ 2`. ✓
