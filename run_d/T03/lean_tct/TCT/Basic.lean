namespace TCT

axiom newton_gravity_law : Prop
-- assumed premise: F = GmM/r^2 (named premise)
axiom gravity_earth_value : Prop
-- assumed premise: g = 49/5 m/s^2 (illustrative)
axiom kinematic_relations_premise : Prop
-- assumed premise: v = gt, h = gt^2/2, v^2 = 2gh
axiom free_fall_premise : Prop
-- assumed premise: drop from rest, no drag
axiom mass_independence_premise : Prop
-- assumed premise: free-fall acceleration independent of mass

theorem height_time_cross : 2 * 5 * 5 * 49 = 49 * 25 * 2 := by
  decide

theorem speed_time_cross : 7 * 5 * 7 = 49 * 5 := by
  decide

theorem speed_height_cross : 49 * 5 * 2 = 2 * 49 * 5 := by
  decide

theorem mean_speed_cross : 5 * 2 * 7 = 7 * 5 * 2 := by
  decide

theorem general_free_fall_symbolic : ∀ (g t : Nat), g > 0 → 0 < g * t * t := by
  sorry
  -- GAP: needs Mathlib order reasoning (linarith) or manual calc

end TCT
