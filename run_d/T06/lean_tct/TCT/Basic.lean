namespace TCT

theorem successor_route : 1 + 1 = 2 := by
  rfl

theorem decide_route : 1 + 1 = 2 := by
  decide

theorem xor_site_value : (1 + 1) % 2 = 0 := by
  decide

theorem mod7_value : (1 + 1) % 7 = 2 := by
  decide

theorem xor_site_bool : Bool.xor true true = false := by
  decide

end TCT
