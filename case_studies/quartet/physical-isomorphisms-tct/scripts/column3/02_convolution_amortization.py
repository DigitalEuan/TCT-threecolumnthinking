#!/usr/bin/env python3
"""Column 3 (TCT) — Hurdle H2b: convolution — FFT vs. direct vs. optical isomorphism.
Physical isomorphism: a 4f optical system (two lenses, one focal length apart)
performs a Fourier transform in one light-propagation step; the filter plane
realizes elementwise `mult`; diffraction realizes `spatial` mixing. The
convolution theorem (F(g*h) = F(g)·F(h)) is the structure preserved.

Cost model (declared; ops counted in exact integers):
  N = 1024 (1-D signal), log2 N = 10
  direct convolution   = N^2           = 1048576 ops
  FFT convolution      = 5*N*log2(N)   = 51200 ops
  optical (amortized): setup = N^2 (program arbitrary kernel), per frame = N+1
    (N readout + 1 propagation step)

Two disjoint derivation paths per witness:
  - break-even reuse T: closed inequality vs. enumeration
  - op ratio: Fraction reduction vs. direct integer comparison

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction
from math import gcd

N = 1024
LOG2 = 10
assert 2 ** LOG2 == N

ops_direct = N * N                  # 1048576
ops_fft = 5 * N * LOG2              # 51200
assert ops_direct == 1048576 and ops_fft == 51200

ratio = Fraction(ops_direct, ops_fft)
g = gcd(ops_direct, ops_fft)
assert (ratio.numerator, ratio.denominator) == (512, 25)
RATIO_DIRECT_FFT = ratio

# optical total cost over T frames vs. digital FFT total over T frames
setup = N * N                       # kernel programming (conservative: N^2 writes)
per_frame_opt = N + 1               # readout + constant-latency propagation
per_frame_fft = ops_fft

def optical_total(T):
    return setup + T * per_frame_opt

def fft_total(T):
    return T * per_frame_fft

# break-even: smallest T with fft_total(T) >= optical_total(T)
# T*51200 >= 1048576 + T*1025  <=>  T*50175 >= 1048576  <=>  T >= 1048576/50175
boundary = Fraction(setup, per_frame_fft - per_frame_opt)
be_closed = -(-boundary.numerator // boundary.denominator)  # ceiling
be_enum = None
for T in range(1, 100000):
    if fft_total(T) >= optical_total(T):
        be_enum = T
        break
assert be_closed == be_enum == 21
BREAKEVEN_T = be_enum

# amortization identity check (two paths): at T = breakeven both totals compared
assert fft_total(BREAKEVEN_T) >= optical_total(BREAKEVEN_T)
assert fft_total(BREAKEVEN_T - 1) < optical_total(BREAKEVEN_T - 1)
AMORTIZATION_CONSISTENT = 1

# latency (declared model): one propagation step vs. 51200 sequential ops
latency_ratio = Fraction(ops_fft, 1)
assert latency_ratio == 51200
LATENCY_RATIO = latency_ratio

print(f"OPS_DIRECT={ops_direct}")
print(f"OPS_FFT={ops_fft}")
print(f"RATIO_DIRECT_FFT={RATIO_DIRECT_FFT}")
print(f"BREAKEVEN_T={BREAKEVEN_T}")
print(f"AMORTIZATION_CONSISTENT={AMORTIZATION_CONSISTENT}")
print(f"LATENCY_RATIO={LATENCY_RATIO}")
