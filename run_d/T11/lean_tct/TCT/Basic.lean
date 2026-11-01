namespace TCT

axiom switch_toggles_premise : Prop
-- assumed premise: each flip toggles the state (declared reading)

theorem flip_count_parity : 17 % 2 = 1 := by
  decide

theorem toggle_law_sample : (1 + 1) % 2 = 0 := by
  decide

theorem state_after_two : (0 + 2) % 2 = 0 := by
  decide

theorem even_flips_return : (0 + 16) % 2 = 0 := by
  decide

theorem parity_law : ∀ n : Int, (n + 2) % 2 = n % 2 := by
  omega

theorem final_state : (0 + 17) % 2 = 1 := by
  decide

theorem xor_site_declared : 17 % 2 = 1 ∧ (0 + 17) % 2 = 1 := by
  decide

end TCT
