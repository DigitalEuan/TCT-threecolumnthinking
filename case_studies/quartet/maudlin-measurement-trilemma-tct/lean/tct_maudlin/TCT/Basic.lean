namespace TCT

def lambda_grw : ℚ := 1 / 10^16
def sec_per_julian_year : ℕ := 31557600
def door_count : ℕ := 3

axiom linearity_entangles : ∀ (C1 C2 C3 : Prop), C1 ∧ C2 → C3 → False
-- assumed premise: physical content of the entangled-detector toy model (re-derived in scripts/column3/01_trilemma_core.py): completeness + linear evolution yields a detector superposition with two macroscopic readings, incompatible with a single outcome
axiom detector_single_readings_empirical : Prop
-- assumed premise: empirical premise of C3: detectors show one result (Bell 1990, 'outcomes')
axiom born_rule_empirical : Prop
-- assumed premise: empirical: outcome weights are squared amplitudes
axiom grw_lambda_empirical : Prop
-- assumed premise: empirical parameter: GRW rate lambda = 10^-16 s^-1 per particle (Ghirardi-Rimini-Weber 1986)
axiom door_realization_principle : Prop
-- assumed premise: philosophical: each 2-claim pair is realized by an interpretation family (Bohm 1952 / GRW 1986 / Everett 1957)

theorem trilemma_from_model : ∀ (C1 C2 C3 : Prop), C1 ∧ C2 ∧ C3 → False := by
  intro C1 C2 C3 h; exact linearity_entangles C1 C2 C3 ⟨h.1, h.2.1⟩ h.2.2

theorem trilemma_logic : ∀ (C1 C2 C3 : Prop), (C1 ∧ C3 → ¬C2) → ¬(C1 ∧ C2 ∧ C3) := by
  intro C1 C2 C3 h hc; exact h ⟨hc.1, hc.2.2⟩ hc.2.1

theorem pair_exclusion : ∀ (C1 C2 C3 : Prop), ¬(C1 ∧ C2 ∧ C3) → C1 ∧ C2 → ¬C3 := by
  intro C1 C2 C3 h hc12 hc3; exact h ⟨hc12.1, hc12.2, hc3⟩

theorem born_weight_sum : (1/2 : ℚ) + 1/2 = 1 := by
  decide

theorem branches_pow10 : (2^10 : ℕ) = 1024 := by
  decide

theorem grw_macro_tau : (10^16 : ℚ) / 10^23 = 1 / 10^7 := by
  decide

theorem grw_threshold_rate : (10^16 : ℚ) * (1 / 10^16) = 1 := by
  decide

theorem branch_weight_times_count : 1024 * (1/1024 : ℚ) = 1 := by
  decide

theorem entangled_witness_minor : (1 : ℚ) * 0 - 1 * 1 ≠ 0 := by
  decide

theorem fluidic_tie : (1/2 : ℚ) - 1/2 = 0 := by
  decide

theorem branch_weight_sum_general : ∀ (n : ℕ), (2^n : ℚ) * (1 / 2^n) = 1 := by
  sorry
  -- GAP: requires a nonzero-powers lemma (2^n ≠ 0, Mathlib pow_ne_zero/field_simp) or a core-level induction on Nat.pow; target: derive the general total-weight identity checked concretely by scripts/column3/04_branch_counting.py

theorem product_state_minors : ∀ (a b c d x y u v : ℚ), a = x * u → b = x * v → c = y * u → d = y * v → a * d = b * c := by
  sorry
  -- GAP: requires ring-style normalization (Mathlib ring) or a manual calc over mul_comm/mul_assoc/mul_left_comm; this is the symbolic form of the minor test in scripts/column3/01_trilemma_core.py

theorem everett_emergence_gap : ∀ (C3 : Prop), C3 := by
  sorry
  -- GAP: DELIBERATE TARGET, EXPECTED UNPROVEN: recovering single outcomes (C3) from C1∧C2 alone (the Everett emergence-of-outcome step). Requires a decision-theoretic or self-locating argument (Deutsch-Wallace) that this framework does not contain; keeping it sorry is the formal record that the many-worlds door still owes an account of outcomes/probability

end TCT
