# Classification ledger (TCT §14)

Identity: `n = p + s + a + r` → **20 = 12 + 3 + 5 + 0**

## Proved (12) — Python VERIFIED; Lean proved where a lemma exists

1. `U` termwise = matrix–vector product (01 `LINEARITY_MATCH`)
2. output state `(1)|↑⟩|D↑⟩ + (1)|↓⟩|D↓⟩` (01)
3. non-product via cross-minors (01 `ENTANGLED_MINORS`; Lean `entangled_witness_minor`)
4. reduced-state mixing `Tr(ρ_D²) ≠ Tr(ρ_D)²` (01 `ENTANGLED_PURITY`)
5. branch orthogonality (01 `BRANCH_ORTHO`)
6. coherence vanishing (02 `OFFDIAG_ZERO`)
7. Born normalization, two paths (02 `NORMALIZATION`; Lean `born_weight_sum`)
8. two nonzero pointer branches under C1∧C2 (01 `NONZERO_BRANCHES`)
9. C3 contradicted (01 `C3_CONTRADICTED`; Lean `trilemma_from_model`)
10. pure-logic skeleton (05 `PAIRWISE_EQUIVALENCE`; Lean `trilemma_logic`, `pair_exclusion`)
11. GRW arithmetic (03; Lean `grw_macro_tau`, `grw_threshold_rate`)
12. branch counting + total weight (04; Lean `branches_pow10`, `branch_weight_times_count`)

## Sorry (3) — named gaps, development required

- `branch_weight_sum_general` — needs nonzero-powers lemma (`pow_ne_zero` /
  `field_simp`, or core induction).
- `product_state_minors` — needs ring normalization (`ring`, or manual
  `mul_comm`/`mul_assoc` calc).
- `everett_emergence_gap` — **deliberate target**: recovering single outcomes
  from C1∧C2 alone (Deutsch–Wallace emergence). Expected unproven; keeping it
  sorry is the formal record that the many-worlds door still owes an account
  of outcomes and probability.

## Axioms (5) — assumed premises, never sorry theorems

- `linearity_entangles` — the toy model's physical content (re-derived in 01).
- `detector_single_readings_empirical` — detectors show one result.
- `born_rule_empirical` — weights are squared amplitudes.
- `grw_lambda_empirical` — GRW rate λ = 10⁻¹⁶ s⁻¹ per particle.
- `door_realization_principle` — each 2-claim pair is realized by a family
  (Bohm 1952 / GRW 1986 / Everett 1957).

## Refused (0)

`WOULD_BE_GUESS = 0`. Nothing under-specified: all deterministic sub-claims
close exactly over ℚ. The Everett item is a named development target (sorry),
not missing data (refusal).

## Cross-check register (14 written, 1 tautology-class artifact removed)

| Script | Cross-check pairs (disjoint paths) |
|---|---|
| 01 | dict-rewrite vs. matrix; minors vs. purity; Born-sum vs. trace |
| 02 | full-trace vs. direct sum; Σw vs. Tr(ρ̂); explicit off-diag vs. zero-product support |
| 03 | Fraction vs. gcd-reduced ratio; solve vs. cross-multiply |
| 04 | loop vs. shift; accumulation vs. closed form |
| 05 | enumeration vs. binomial; enumeration vs. combinatorial |
| 06 | argmax vs. difference sign; conservation (symmetric + asymmetric) |

Removed: one unreferenced intermediate in script 02 (tautology class).
`c − t = 13 ≥ 2`. ✓
