# Development-required ledger — tct_maudlin

- lemmas total: 13
- proved (sorry-free): **10**
- `sorry` (development required): **3**
- axioms: **5**
- definitions: 3

## sorry lemmas

- `branch_weight_sum_general` : `∀ (n : ℕ), (2^n : ℚ) * (1 / 2^n) = 1`
  - gap: requires a nonzero-powers lemma (2^n ≠ 0, Mathlib pow_ne_zero/field_simp) or a core-level induction on Nat.pow; target: derive the general total-weight identity checked concretely by scripts/column3/04_branch_counting.py
- `product_state_minors` : `∀ (a b c d x y u v : ℚ), a = x * u → b = x * v → c = y * u → d = y * v → a * d = b * c`
  - gap: requires ring-style normalization (Mathlib ring) or a manual calc over mul_comm/mul_assoc/mul_left_comm; this is the symbolic form of the minor test in scripts/column3/01_trilemma_core.py
- `everett_emergence_gap` : `∀ (C3 : Prop), C3`
  - gap: DELIBERATE TARGET, EXPECTED UNPROVEN: recovering single outcomes (C3) from C1∧C2 alone (the Everett emergence-of-outcome step). Requires a decision-theoretic or self-locating argument (Deutsch-Wallace) that this framework does not contain; keeping it sorry is the formal record that the many-worlds door still owes an account of outcomes/probability

## axioms (assumed)

- `linearity_entangles` : `∀ (C1 C2 C3 : Prop), C1 ∧ C2 → C3 → False` — physical content of the entangled-detector toy model (re-derived in scripts/column3/01_trilemma_core.py): completeness + linear evolution yields a detector superposition with two macroscopic readings, incompatible with a single outcome
- `detector_single_readings_empirical` : `Prop` — empirical premise of C3: detectors show one result (Bell 1990, 'outcomes')
- `born_rule_empirical` : `Prop` — empirical: outcome weights are squared amplitudes
- `grw_lambda_empirical` : `Prop` — empirical parameter: GRW rate lambda = 10^-16 s^-1 per particle (Ghirardi-Rimini-Weber 1986)
- `door_realization_principle` : `Prop` — philosophical: each 2-claim pair is realized by an interpretation family (Bohm 1952 / GRW 1986 / Everett 1957)

## To verify

```bash
cd lean/tct_maudlin && lake build
```
0 sorry = fully described; each sorry above is exactly what remains.
