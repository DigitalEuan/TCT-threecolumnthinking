namespace TCT

axiom calendar_convention : Prop
-- assumed premise: days indexed Wed=3 in Z/7Z (ISO convention)

theorem wednesday_successor : (3 + 1) % 7 = 4 := by
  decide

theorem cyclic_wrap : (6 + 1) % 7 = 0 := by
  decide

theorem seven_day_cycle : (3 + 7) % 7 = 3 := by
  decide

theorem succ_mod_law : ∀ n : Int, (n + 1) % 7 = (n % 7 + 1) % 7 := by
  omega

end TCT
