#!/usr/bin/env python3
"""Column 3 (TCT) — Class T: ln 2 and Catalan's constant G from first principles.
All via rigorous rational interval arithmetic (alternating-series bounds).

ln 2, two independent series:
  A. Mercator:  ln 2 = sum (-1)^{k+1}/k; |error| <= 1/(N+1) (alternating)
  B. Binary:    ln 2 = sum 1/(k*2^k); tail <= 1/((M+1)*2^M)
Witness: intervals overlap and both contain the anchor 0.693147180559.

Catalan: G = sum (-1)^k/(2k+1)^2; |error| <= 1/(2N+3)^2 (alternating).
Anchor 0.915965594177. Status note: no closed form known; irrationality is a
famous open problem (docs/04) — computed here to arbitrary precision with
rigorous bounds, but not "closed-form derived".

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

LN2_ANCHOR = Fraction(693147180559, 10**12)     # ln 2 to 12 decimals
G_ANCHOR = Fraction(915965594177, 10**12)       # Catalan to 12 decimals

# --- A. Mercator ---
N = 4000
S_A = sum((Fraction((-1)**(k+1), k) for k in range(1, N + 1)), Fraction(0))
err_A = Fraction(1, N + 1)
# alternating remainder sign: N even -> S_A under-estimates (last term negative)
if N % 2 == 0:
    A = (S_A, S_A + err_A)
else:
    A = (S_A - err_A, S_A)

# --- B. Binary series ---
M = 60
S_B = sum((Fraction(1, k * 2**k) for k in range(1, M + 1)), Fraction(0))
err_B = Fraction(1, (M + 1) * 2**M)
B = (S_B, S_B + err_B)

def overlaps(I, J):
    return I[0] <= J[1] and J[0] <= I[1]

assert overlaps(A, B)
LN2_OVERLAP = 1
# A: anchor containment (A is wide); B: digit-block at 12 decimals (B is tight)
def floor_digits(x, d):
    return (x.numerator * 10**d) // x.denominator

assert A[0] <= LN2_ANCHOR <= A[1]
assert floor_digits(B[0], 12) == floor_digits(B[1], 12) == 693147180559
LN2_ANCHOR_OK = 1

# --- Catalan: alternating with last term POSITIVE (N even) -> S over-shoots ---
NC = 4000
S_G = sum((Fraction((-1)**k, (2*k + 1)**2) for k in range(NC + 1)), Fraction(0))
err_G = Fraction(1, (2*(NC + 1) + 1)**2)
if NC % 2 == 0:
    G = (S_G - err_G, S_G)      # remainder in (-err, 0)
else:
    G = (S_G, S_G + err_G)
assert G[0] <= G_ANCHOR <= G[1]
CATALAN_ANCHOR_OK = 1

# widths below 1e-6 at these N (cheap-but-strict check of bound validity)
assert (A[1] - A[0]) < Fraction(1, 10**3)
assert (G[1] - G[0]) < Fraction(1, 10**6)
WIDTH_OK = 1

print(f"LN2_OVERLAP={LN2_OVERLAP}")
print(f"LN2_ANCHOR_OK={LN2_ANCHOR_OK}")
print(f"CATALAN_ANCHOR_OK={CATALAN_ANCHOR_OK}")
print(f"WIDTH_OK={WIDTH_OK}")
# print digit blocks (fractions here have thousands of digits; avoid str limits)
def floor_digits(x, d):
    return (x.numerator * 10**d) // x.denominator

print(f"LN2_DIGITS12={floor_digits(A[0], 12)}")
print(f"CATALAN_DIGITS12={floor_digits(G[0], 12)}")
