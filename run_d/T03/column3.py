#!/usr/bin/env python3
"""T03 - What is gravity? (witness triple under g=49/5)"""
from fractions import Fraction as F

g = F(49, 5)
t, v, h = F(5, 7), 7, F(5, 2)                 # the witness triple
# three kinematic relations simultaneously (paper 6.10):
r1 = (h == g * t * t / 2)
r2 = (v == g * t)
r3 = (v * v == 2 * g * h)
r4 = (h == v * t / 2)
assert r1 and r2 and r3 and r4
assert sum([r1, r2, r3, r4]) == 4

print("WITNESS_OK=1")
print(f"T={t}")
print(f"V={v}")
print(f"H={h}")
print("RELATIONS=4")
print("WITNESS_TRIPLE_OK=1")
