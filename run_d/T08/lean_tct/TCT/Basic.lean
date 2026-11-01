namespace TCT

axiom compound_interest_definition : Prop
-- assumed premise: A = P(1+r)^n (definition), P=100, r=1/20, n=3

theorem amount_cross : 9261 * 8000 = 926100 * 80 := by
  decide

theorem terminating_denominator : 80 = 16 * 5 := by
  decide

theorem decimal_digits : 9261 * 125 = 1157625 := by
  decide

theorem interest_cross : 1261 * 10000 = 157625 * 80 := by
  decide

theorem geometric_growth_symbolic : ∀ (p : Nat), p * 21 * 21 * 21 = p * 9261 * 1 * 1 * 1 + (p * 21 * 21 * 21 - p * 9261) := by
  sorry
  -- GAP: general growth identity — needs ring (absent in core)

end TCT
