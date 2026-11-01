#!/usr/bin/env python3
"""T07 - How many ways to choose 2 toppings from 5? (combinatorics)"""
from fractions import Fraction as F

n, k = 5, 2
fact = [1, 1, 2, 6, 24, 120]                  # 0!..5! (core Lean has no Nat.factorial)

formula = fact[n] // (fact[k] * fact[n - k])   # 5!/(2!3!)
enum = sum(n - i for i in range(1, n))        # pairs by first element: 4+3+2+1
pascal = fact[4] // (fact[1] * fact[3]) + fact[4] // (fact[2] * fact[2])  # C(4,1)+C(4,2)
complement = fact[n] // (fact[n - k] * fact[k])  # C(5,3) = C(5,2)
ordered = n * (n - 1) // 2                    # ordered/2: representation variant (audited out)
assert formula == enum == pascal == complement == ordered == 10

print(f"FORMULA={formula}")
print(f"ENUM={enum}")
print(f"PASCAL={pascal}")
print(f"COMPLEMENT={complement}")
print(f"ANSWER={formula}")
