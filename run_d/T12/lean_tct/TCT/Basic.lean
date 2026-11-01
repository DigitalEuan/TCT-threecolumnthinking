namespace TCT

axiom ohms_law_premise : Prop
-- assumed premise: V = IR and P = VI = I^2 R = V^2/R (definitions under test)

theorem ohm_violation : 12 ≠ 5 * 4 := by
  decide

theorem power_vi_vs_i2r : 60 ≠ 100 := by
  decide

theorem power_vi_vs_v2r : 60 ≠ 36 := by
  decide

theorem power_i2r_vs_v2r : 100 ≠ 36 := by
  decide

end TCT
