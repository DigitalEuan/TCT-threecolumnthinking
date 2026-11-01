#!/usr/bin/env python3
"""Column 3 (TCT) — Class O: the Euler-Mascheroni constant gamma — computable
to any precision, rigorously bounded, and FAMOUSLY NOT closed-form.

Definition (first principles): gamma = lim_{n->inf} (H_n - ln n)
  = sum_{k>=1} t_k,  t_k = 1/k - ln(1 + 1/k).

Exact bounds (no floats):
  - ln(1+1/k) by Mercator alternating partial sums (odd #terms overestimates,
    even underestimates) -> t_k bracketed by exact rationals
  - t_k <= 1/(2k^2)  (from ln(1+x) >= x - x^2/2) -> tail < 1/(2N)
  - coarse independent path: integral-rectangle sandwich on ln n
    (sum_{k=2}^n 1/k < ln n < sum_{k=1}^{n-1} 1/k)

Anchor: gamma ~ 0.5772156649 (10 decimals). Status stamp: irrationality is
an OPEN problem (Erdos prize); no closed form is known — the deliberate
boundary of this study (Lean: gamma_rational_target, sorry).

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

ANCHOR = Fraction(5772156649, 10**10)          # gamma to 10 decimals

def ln2_bracket(m):
    """bracket ln 2 by the binary series sum 1/(j*2^j): tail <= 1/((m+1)*2^m)."""
    S = sum((Fraction(1, j * 2**j) for j in range(1, m + 1)), Fraction(0))
    return S, S + Fraction(1, (m + 1) * 2**m)

def ln1p_inv(k, m):
    """bracket ln(1+1/k) by Mercator partial sums with m terms (exact)."""
    L = sum((Fraction((-1)**(j+1), j * k**j) for j in range(1, m + 1)), Fraction(0))
    # m odd -> L over-estimates; m even -> L under-estimates
    if m % 2 == 1:
        U, Lo = L, L - Fraction(1, (m + 1) * k**(m + 1))
    else:
        U, Lo = L + Fraction(1, (m + 1) * k**(m + 1)), L
    return Lo, U

# --- path A: t-series (k = 1 via binary ln 2; k >= 2 via Mercator) ---
N, M = 200, 8
lower = Fraction(0)
upper = Fraction(0)
ln2_lo, ln2_hi = ln2_bracket(60)
for k in range(1, N + 1):
    if k == 1:
        ln_lo, ln_hi = ln2_lo, ln2_hi
    else:
        ln_lo, ln_hi = ln1p_inv(k, M)
    lower += Fraction(1, k) - ln_hi
    upper += Fraction(1, k) - ln_lo
tail_bound = Fraction(1, 2 * N)                # sum_{k>N} t_k < sum 1/(2k^2) < 1/(2N)
gamma_A = (lower, upper + tail_bound)

# --- path B (coarse, independent): integral-rectangle sandwich on ln n ---
n = 150
H_n = sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))
L_ln = sum((Fraction(1, k) for k in range(2, n + 1)), Fraction(0))     # < ln n
U_ln = sum((Fraction(1, k) for k in range(1, n)), Fraction(0))         # > ln n
gamma_B = (H_n - U_ln, H_n - L_ln)

# --- witnesses ---
assert gamma_A[0] <= ANCHOR <= gamma_A[1]
assert gamma_B[0] <= ANCHOR <= gamma_B[1]
GAMMA_CONTAINED = 1
GAMMA_CONTAINED_COARSE = 1

# the two constructions must overlap
assert gamma_A[0] <= gamma_B[1] and gamma_B[0] <= gamma_A[1]
PATHS_OVERLAP = 1

# width shrinks like 1/(2N): at N = 200 the strict interval is below 1/100
width = gamma_A[1] - gamma_A[0]
assert width < Fraction(1, 100)
WIDTH_OK = 1

# --- the open boundary, stamped ---
GAMMA_IRRATIONALITY = "UNKNOWN"    # open problem (Erdos prize); no closed form
OPEN_PROBLEM = 1
assert GAMMA_IRRATIONALITY == "UNKNOWN" and OPEN_PROBLEM == 1

print(f"GAMMA_CONTAINED={GAMMA_CONTAINED}")
print(f"GAMMA_CONTAINED_COARSE={GAMMA_CONTAINED_COARSE}")
print(f"PATHS_OVERLAP={PATHS_OVERLAP}")
print(f"WIDTH_OK={WIDTH_OK}")
print(f"GAMMA_IRRATIONALITY={GAMMA_IRRATIONALITY}")
print(f"OPEN_PROBLEM={OPEN_PROBLEM}")
print(f"GAMMA_DIGITS10={(gamma_A[0].numerator * 10**10) // gamma_A[0].denominator}")
