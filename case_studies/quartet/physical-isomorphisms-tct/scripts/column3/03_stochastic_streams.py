#!/usr/bin/env python3
"""Column 3 (TCT) — Hurdle H4: randomness & sampling — stochastic streams.
Physical isomorphism: a noisy physical bit source IS a Bernoulli sampler;
a stream of N independent bits estimates p as the fraction of 1s, and
multiplication of stream values is a single AND gate (primitive `mult` at
cost ~1 gate) — no multiplier array needed.

Exact results (integers/Fractions only):
  - the binomial tail P(|p_hat - 1/2| >= 1/10) at N = 100, p = 1/2, computed
    exactly (sum of C(100,k)/2^100) by two disjoint paths
  - the Chebyshev bound p(1-p)/(N eps^2) = 1/4 as a rational upper bound
  - stream length required for error <= 1/100 via the exact Chebyshev formula
    N >= p(1-p)/eps^2 = 2500, by closed form and enumeration

Cost honesty: unit-level AND (1 unit) vs. 32b FP multiply (37 units, Horowitz
2014); but a stochastic multiply costs N bit-steps, so the trade is energy per
op vs. precision cost — reported, not hidden.

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction
from math import comb, gcd

P = Fraction(1, 2)
N = 100
EPS = Fraction(1, 10)

# --- exact binomial tail, two disjoint paths ---
# path 1: sum both tails explicitly
tail_p1 = sum(Fraction(comb(N, k), 2 ** N) for k in range(N + 1)
              if abs(Fraction(k, N) - P) >= EPS)
# path 2: 1 minus the central window
tail_p2 = 1 - sum(Fraction(comb(N, k), 2 ** N) for k in range(N + 1)
                  if abs(Fraction(k, N) - P) < EPS)
assert tail_p1 == tail_p2
TAIL_EXACT = tail_p1

# --- Chebyshev bound: Var(p_hat)/eps^2 = p(1-p)/(N eps^2) ---
var = P * (1 - P) / N                       # 1/400
cheb = var / (EPS * EPS)                    # 1/4
assert var == Fraction(1, 400) and cheb == Fraction(1, 4)
CHEBYSHEV = cheb
assert TAIL_EXACT <= CHEBYSHEV
CHEBYSHEV_OK = 1

# --- stream length for error <= 1/100: N >= p(1-p)/eps^2 ---
EPS100 = Fraction(1, 100)
n_closed = (P * (1 - P)) / (EPS100 * EPS100)
assert n_closed == 2500
# enumeration path: smallest N with p(1-p)/N <= eps^2
n_enum = None
for n in range(1, 10000):
    if P * (1 - P) / n <= EPS100 * EPS100:
        n_enum = n
        break
assert n_closed == n_enum == 2500
N_FOR_1PCT = n_enum

# --- gate-cost trade (declared units of 0.1 pJ) ---
MULT32, AND_GATE = 37, 1                    # Horowitz 2014 (mult), illustrative (gate)
gate_ratio = Fraction(MULT32, AND_GATE)
assert gate_ratio == 37
GATE_RATIO = gate_ratio

# stochastic multiply at N=100 bit-steps costs 100 gate-units vs 37 for one
# digital multiply: stochastic wins only when gate-width scaling of the digital
# multiplier (w^2 gates) exceeds the stream length: w^2 > N
crossover_w = None
for w in range(1, 400):
    if w * w > N:
        crossover_w = w
        break
assert crossover_w == 11                     # 11^2 = 121 > 100
CROSSOVER_WIDTH = crossover_w

print(f"TAIL_EXACT={TAIL_EXACT}")
print(f"CHEBYSHEV={CHEBYSHEV}")
print(f"CHEBYSHEV_OK={CHEBYSHEV_OK}")
print(f"N_FOR_1PCT={N_FOR_1PCT}")
print(f"GATE_RATIO={GATE_RATIO}")
print(f"CROSSOVER_WIDTH={CROSSOVER_WIDTH}")
