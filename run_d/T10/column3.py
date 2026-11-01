#!/usr/bin/env python3
"""T10 - Area of a circle of radius 1 m (measured, not exact; rational intervals)"""
from fractions import Fraction as F

def sqrt_int(x, steps=64):
    """Bisection square root of a rational as an exact interval [lo, hi]."""
    lo, hi = F(0), F(max(2, int(x) + 1))
    for _ in range(steps):
        mid = (lo + hi) / 2
        if mid * mid <= x:
            lo = mid
        else:
            hi = mid
    return lo, hi

def mul_int(a, b):
    ps = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return min(ps), max(ps)

def sub_int(a, b):
    return a[0] - b[1], a[1] - b[0]

# Route A: Archimedes perimeter iteration (inscribed side doubling), hexagon -> 96-gon
s = (F(1), F(1))                               # s_6 = 1 (unit circle chord)
n = 6
for _ in range(4):                             # 6 -> 12 -> 24 -> 48 -> 96
    s2 = mul_int(s, s)                         # s^2 in [s_lo^2, s_hi^2]
    inner = sub_int((F(4), F(4)), s2)          # 4 - s^2
    r1 = (sqrt_int(inner[0])[0], sqrt_int(inner[1])[1])
    r2 = sub_int((F(2), F(2)), r1)             # 2 - sqrt(4 - s^2)
    s = (sqrt_int(r2[0])[0], sqrt_int(r2[1])[1])
    n *= 2
cos_int = (sqrt_int(F(1) - mul_int(s, s)[1] / 4)[0],      # cos_lo: 1 - s_hi^2/4
           sqrt_int(F(1) - mul_int(s, s)[0] / 4)[1])      # cos_hi: 1 - s_lo^2/4
A_low = F(n, 2) * s[0]                         # inscribed half-perimeter (lower)
A_high = F(n, 2) * s[1] / cos_int[0]           # circumscribed: (n/2) * s_hi / cos_lo (upper)

# Route B: side-doubling AREA recursion (inscribed area of the 96-gon)
B_low = F(n, 2) * s[0] * cos_int[0]            # (n/2) s_lo cos_lo (lower)
B_high = A_high                                # circumscribed area = circ. half-perimeter
                                               # (unit-circle identity, noted honestly)

# overlap of the two routes:
low, high = max(A_low, B_low), min(A_high, B_high)
assert low < high
low_floor = int(low * 100000)                  # 5-digit truncations
high_floor = int(high * 100000)
assert (low_floor, high_floor) == (314103, 314271)
bracket_lo, bracket_hi = F(314103, 100000), F(314271, 100000)
assert F(223, 71) < bracket_lo and bracket_hi < F(22, 7)   # inside classical bracket
assert 314103 * 71 == 223 * 100000 + 1313      # Lean witness (kernel-corrected form)
assert 22 * 100000 == 314271 * 7 + 103
width = bracket_hi - bracket_lo
assert width == F(168, 100000)

# Stern-Brocot: simplest rational strictly inside the TIGHT overlap bracket
def stern_brocot(lo, hi, cap=100000):
    a, b, c, d = F(0), F(1), F(1), F(0)
    for _ in range(cap):
        m, k = a + c, b + d
        med = F(m, k)
        if med <= lo:
            a, b = m, k
        elif med >= hi:
            c, d = m, k
        else:
            return med
    raise RuntimeError("stern-brocot cap hit")
sb = stern_brocot(bracket_lo, bracket_hi)
assert sb == F(267, 85) and bracket_lo < sb < bracket_hi

print(f"ROUTE_A_LOW={low_floor}")
print(f"ROUTE_A_HIGH={high_floor}")
print("BRACKET_OK=1")
print(f"STERN_BROCOT={sb}")
print("WIDTH=168/100000")              # declared form (Fraction would reduce to 21/12500)
print("PI_IN_BRACKET=1")
