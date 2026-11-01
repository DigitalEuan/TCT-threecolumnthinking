#!/usr/bin/env python3
"""T08 - 100 at 5% compound interest for 3 years (exact rational finance)"""
from fractions import Fraction as F

P, r, n = 100, F(1, 20), 3
A = P * (1 + r) ** n
assert A == F(9261, 80)
interest = A - P
assert interest == F(1261, 80)
# terminating decimal: denominator 80 = 2^4 * 5
assert 80 == 16 * 5
assert 9261 * 125 == 1157625                  # A = 115.7625 exactly
assert 1261 * 10000 == 157625 * 80            # interest = 15.7625 exactly

print(f"AMOUNT={A}")
print("TERMINATING=1")
print(f"INTEREST={interest}")
print(f"AMOUNT_DECIMAL={F(1157625, 10000)}")
print(f"AMOUNT={A}")
