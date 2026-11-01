#!/usr/bin/env python3
"""Column 3 (TCT) — Hurdle H2: quadratic linear algebra vs. analog crossbar.
Physical isomorphism: Kirchhoff's current law performs a dot product —
conductance × voltage = current, currents sum at a wire node (primitive `sum`),
transconductance realizes `mult`. One physical step = one matrix-vector product.

Cost model (declared illustrative; empirical parameters as givens):
  units = 0.1 pJ  (Horowitz, ISSCC 2014, 45nm-class figures):
    32b FP multiply = 37 units (3.7 pJ)      32b add = 1 unit (0.1 pJ)
    32b SRAM read   = 50 units (5 pJ)        32b DRAM read = 6400 units (640 pJ)
  declared illustrative:
    crossbar cell compute = 2 units; DAC/ADC conversion = 3700 units each (370 pJ)

Baselines for an N x N matrix-vector product:
  digital, von Neumann:  N^2 * (mult + add + 2*DRAM) = N^2 * 12838
  digital, in-memory:    N^2 * (mult + add + 2*SRAM) = N^2 * 138
  analog crossbar:       N^2 * cell + 2N * conv      = 2N^2 + 7400N

Two disjoint derivation paths per witness:
  - break-even N: closed inequality (cross-multiplication) vs. enumeration
  - energy ratios: Fraction division vs. manual gcd reduction

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction
from math import gcd

# ---- givens ----
MULT, ADD, SRAM, DRAM = 37, 1, 50, 6400        # empirical (Horowitz 2014)
CELL, CONV = 2, 3700                            # illustrative (crossbar model)

per_mac_vn = MULT + ADD + 2 * DRAM              # 12838
per_mac_inmem = MULT + ADD + 2 * SRAM           # 138
assert per_mac_vn == 12838 and per_mac_inmem == 138

def analog_cost(N, passes=1):
    return passes * (CELL * N * N + 2 * N * CONV)

def digital_vn_cost(N):
    return per_mac_vn * N * N

def digital_inmem_cost(N):
    return per_mac_inmem * N * N

# --- energy ratios (asymptotic, per MAC-equivalent) ---
ratio_vn = Fraction(per_mac_vn, CELL)                 # 6419
ratio_inmem = Fraction(per_mac_inmem, CELL)           # 69
g = gcd(per_mac_vn, CELL)
assert (ratio_vn.numerator, ratio_vn.denominator) == (per_mac_vn // g, CELL // g)
assert ratio_vn == 6419 and ratio_inmem == 69
RATIO_VN = ratio_vn
RATIO_INMEM = ratio_inmem

# --- break-even N vs in-memory digital, 8-bit conversion path ---
# path 1: closed inequality analog < inmem  <=>  2N^2 + 7400N < 138N^2
#         <=>  7400N < 136N^2  <=>  7400 < 136N  <=>  N > 925/17
boundary = Fraction(7400, 136)
assert boundary == Fraction(925, 17)
be_closed = boundary.numerator // boundary.denominator + 1   # ceil for strict >
# path 2: enumeration
be_enum = None
for N in range(1, 2000):
    if analog_cost(N) < digital_inmem_cost(N):
        be_enum = N
        break
assert be_closed == be_enum == 55
BREAKEVEN_N = be_enum

# --- break-even N at 32-bit effective precision (8-bit converters: 4 passes) ---
passes = 32 // 8
assert passes == 4
# 4*(2N^2 + 7400N) < 138N^2  <=>  29600N < 130N^2  <=>  N > 2960/13 = 227.69...
boundary32 = Fraction(29600, 130)
assert boundary32 == Fraction(2960, 13)
be32_closed = boundary32.numerator // boundary32.denominator + 1
be32_enum = None
for N in range(1, 5000):
    if analog_cost(N, passes) < digital_inmem_cost(N):
        be32_enum = N
        break
assert be32_closed == be32_enum == 228
BREAKEVEN_N_32BIT = be32_enum

# --- latency model (declared): N^2 sequential MACs vs 1 physical step + 2N conversions ---
N_LAT = 256
latency_ratio = Fraction(N_LAT * N_LAT, 2 * N_LAT + 1)
assert latency_ratio == Fraction(65536, 513)
LATENCY_RATIO_N256 = latency_ratio

print(f"PER_MAC_VN={per_mac_vn}")
print(f"PER_MAC_INMEM={per_mac_inmem}")
print(f"RATIO_VN={RATIO_VN}")
print(f"RATIO_INMEM={RATIO_INMEM}")
print(f"BREAKEVEN_N={BREAKEVEN_N}")
print(f"BREAKEVEN_N_32BIT={BREAKEVEN_N_32BIT}")
print(f"LATENCY_RATIO_N256={LATENCY_RATIO_N256}")
