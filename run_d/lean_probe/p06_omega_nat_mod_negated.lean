example (n : Nat) (h : ¬(n % 2 = 1)) : ¬((n + 1) % 2 = 1) := by omega
