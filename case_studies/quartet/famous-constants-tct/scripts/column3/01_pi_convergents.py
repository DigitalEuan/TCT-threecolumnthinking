#!/usr/bin/env python3
"""Column 3 (TCT) — Class D/T: pi from first principles, three independent ways.
All three derive rigorous RATIONAL INTERVALS for pi (UBP: no floats; the
irrational value is carried by convergents + alternating-series error bounds):

  A. Machin (1706):  pi = 16*arctan(1/5) - 4*arctan(1/239)
  B. Euler:          pi  = 4*(arctan(1/2) + arctan(1/3))
  C. BBP (1995):     pi = sum_k [4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)]/16^k

arctan(1/x) = sum_k (-1)^k / ((2k+1) x^(2k+1)) — alternating, decreasing,
so |error| <= first omitted term (exact rational bound).
BBP tail: |tail| <= sum_{k>N} 4/((8k+1) 16^k) < 4/((8N+7) * 15 * 16^N).

Witnesses: the three intervals mutually overlap, all contain the anchor
3.1415926535897 (13 decimals), and widths fall below 10^-25.

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

ANCHOR = Fraction(31415926535897, 10**13)      # pi to 13 decimals (known digits)
WIDTH_TARGET = Fraction(1, 10**25)

def arctan_inv(x, n):
    """S = sum_{k<n} (-1)^k/((2k+1)x^(2k+1)); bound = 1/((2n+1)x^(2n+1))."""
    S = Fraction(0)
    for k in range(n):
        term = Fraction(1, (2*k + 1) * x**(2*k + 1))
        S += term if k % 2 == 0 else -term
    bound = Fraction(1, (2*n + 1) * x**(2*n + 1))
    return S, bound

# --- A. Machin ---
s5, b5 = arctan_inv(5, 40)
s239, b239 = arctan_inv(239, 20)
mid_A = 16*s5 - 4*s239
eps_A = 16*b5 + 4*b239
A = (mid_A - eps_A, mid_A + eps_A)

# --- B. Euler: pi = 4*(arctan(1/2) + arctan(1/3)) ---
s2, b2 = arctan_inv(2, 90)
s3, b3 = arctan_inv(3, 60)
mid_B = 4*(s2 + s3)
eps_B = 4*(b2 + b3)
B = (mid_B - eps_B, mid_B + eps_B)

# --- C. BBP ---
def bbp(n):
    S = Fraction(0)
    for k in range(n):
        S += (Fraction(4, 8*k+1) - Fraction(2, 8*k+4)
              - Fraction(1, 8*k+5) - Fraction(1, 8*k+6)) * Fraction(1, 16**k)
    tail = Fraction(4, (8*n + 7) * 15 * 16**n)
    return S, tail

mid_C, eps_C = bbp(35)
C = (mid_C - eps_C, mid_C + eps_C)

# --- witnesses ---
def overlaps(I, J):
    return I[0] <= J[1] and J[0] <= I[1]

assert overlaps(A, B) and overlaps(B, C) and overlaps(A, C)
INTERVALS_OVERLAP = 1

# digit-block check: both endpoints of every interval share pi's known
# leading digits (truncation anchors cannot sit inside intervals this tight)
def floor_digits(x, d):
    return (x.numerator * 10**d) // x.denominator

KNOWN_13 = 31415926535897           # floor(pi * 10^13)
for I in (A, B, C):
    assert floor_digits(I[0], 13) == floor_digits(I[1], 13) == KNOWN_13
PI_ANCHOR = 1

widths = [I[1] - I[0] for I in (A, B, C)]
assert all(w < WIDTH_TARGET for w in widths)
WIDTH_OK = 1

# cross-check: all three midpoints agree to better than 2*max width (consistency)
for I, J in ((A, B), (B, C), (A, C)):
    mid_i = (I[0] + I[1]) / 2
    mid_j = (J[0] + J[1]) / 2
    assert abs(mid_i - mid_j) <= (I[1] - I[0]) + (J[1] - J[0])
MIDPOINTS_CONSISTENT = 1

print(f"INTERVALS_OVERLAP={INTERVALS_OVERLAP}")
print(f"PI_ANCHOR={PI_ANCHOR}")
print(f"WIDTH_OK={WIDTH_OK}")
print(f"MIDPOINTS_CONSISTENT={MIDPOINTS_CONSISTENT}")
print(f"PI_DIGITS13={(A[0].numerator * 10**13) // A[0].denominator}")
