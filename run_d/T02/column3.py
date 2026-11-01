#!/usr/bin/env python3
"""T02 - Why do things bounce? (g=49/5, h0=5/2, m=1/2, e=3/4)"""
from fractions import Fraction as F

g, h0, m, e = F(49, 5), F(5, 2), F(1, 2), F(3, 4)
v_in2 = 2 * g * h0
assert v_in2 == 49                            # engineered: v_in = 7 exactly
v_in = 7
v_out = e * v_in
h1 = v_out * v_out / (2 * g)
h2 = e * e * h1
h3 = e * e * h2
assert h1 == F(45, 32) and h2 == F(405, 512) and h3 == F(3645, 8192)
assert h3 == e ** 6 * h0                      # three-bounce closed form
# the kernel-corrected Lean cross-multiplication (Nat):
assert 729 * 5 * 8192 == 3645 * 4096 * 2
assert 729 * 2 * 4096 != 3645 * 512 * 256     # the refuted first attempt

# geometric closure: total distance and total time
total_d = h0 + 2 * h1 / (1 - e * e)
t_drop = v_in / g
assert t_drop == F(5, 7)
total_t = t_drop + 2 * v_out / g / (1 - e)
assert total_d == F(125, 14) and total_t == 5

print(f"V_IN={v_in}")
print(f"H1={h1}")
print(f"H2={h2}")
print(f"H3={h3}")
print(f"TOTAL_DISTANCE={total_d}")
print(f"TOTAL_TIME={total_t}")
print("LEAN_CROSS_OK=1")
print(f"H3_M={h3}")
