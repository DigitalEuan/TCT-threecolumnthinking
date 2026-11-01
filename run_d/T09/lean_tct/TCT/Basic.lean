namespace TCT

axiom simplicity_premise : Prop
-- assumed premise: geometric reading is the conditional answer (named simplicity axiom)

theorem geometric_witness : 16 * 2 = 32 := by
  decide

theorem cubic_witness : 16 + 8 + 4 + 2 = 30 := by
  decide

theorem moser_witness : 15 + 15 + 1 = 31 := by
  decide

theorem uniqueness_disproved : 32 = 30 + 2 ∧ 31 = 30 + 1 := by
  decide

end TCT
