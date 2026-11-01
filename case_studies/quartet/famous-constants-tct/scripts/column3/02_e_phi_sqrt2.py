#!/usr/bin/env python3
"""Column 3 (TCT) — Class D: e, phi, sqrt(2) from first principles.

e   = sum 1/k!, with exact tail bound R_n < (n+2)/((n+1)*(n+1)!).
    Two paths: direct factorial sum vs. term recurrence t_{k+1} = t_k/(k+1).
phi = [1;1,1,1,...] continued fraction: convergents F_{n+1}/F_n.
    Exact identities verified: Cassini F_{n+1}^2 - F_n F_{n+2} = (-1)^n and
    the quadratic residual F_{n+1}^2 - F_{n+1}F_n - F_n^2 = (-1)^n (phi^2=phi+1).
sqrt(2): two paths — integer isqrt bounds vs. Pell convergents p'=p+2q, q'=p+q
    with exact certificate p^2 - 2q^2 = +/-1.

Anchors (known leading digits, exact rational floors): e ~ 2.718281828459,
phi ~ 1.618033988749, sqrt(2) ~ 1.414213562373.

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction
from math import isqrt

# ---------- e ----------
N = 60
# path 1: direct factorial sum
fact = 1
S_p1 = Fraction(0)
for k in range(N + 1):
    if k > 0:
        fact *= k
    S_p1 += Fraction(1, fact)

# path 2: recurrence
t = Fraction(1)
S_p2 = t
for k in range(1, N + 1):
    t = t / k
    S_p2 += t
assert S_p1 == S_p2

# tail bound: R_N < (N+2)/((N+1)*(N+1)!)
fact_np1 = 1
for k in range(1, N + 2):
    fact_np1 *= k
e_bound = Fraction(N + 2, (N + 1) * fact_np1)
e_lo, e_hi = S_p1, S_p1 + e_bound

# digit-block check at 12 decimals (interval is far tighter than 1e-12)
def floor_digits(x, d):
    return (x.numerator * 10**d) // x.denominator

assert floor_digits(e_lo, 12) == floor_digits(e_hi, 12) == 2718281828459
E_OK = 1

# ---------- phi ----------
fib = [0, 1]
for _ in range(2, 40):
    fib.append(fib[-1] + fib[-2])

cassini_ok = True
quadratic_ok = True
for n in range(1, 30):
    Fnm1, Fn, Fnp1, Fnp2 = fib[n-1], fib[n], fib[n+1], fib[n+2]
    cassini_ok = cassini_ok and (Fnp1**2 - Fn*Fnp2 == (-1)**n)
    quadratic_ok = quadratic_ok and (Fnp1**2 - Fnp1*Fn - Fn**2 == (-1)**n)
assert cassini_ok and quadratic_ok
CASSINI_OK = 1
PHI_RESIDUAL_OK = 1

# phi: digit-block check at 12 decimals from convergent bracket p/q +/- 1/q^2
p, q = fib[36], fib[35]
phi_lo, phi_hi = Fraction(p, q) - Fraction(1, q*q), Fraction(p, q) + Fraction(1, q*q)
assert floor_digits(phi_lo, 12) == floor_digits(phi_hi, 12) == 1618033988749
PHI_OK = 1

# ---------- sqrt(2) ----------
# path 1: isqrt bounds at 12 decimals
scaled = 2 * 10**24
r = isqrt(scaled)
sq_lo, sq_hi = Fraction(r, 10**12), Fraction(r + 1, 10**12)
assert r*r <= scaled < (r+1)*(r+1)

# path 2: Pell convergents
pp, qq = 3, 2
pell_ok = (abs(pp*pp - 2*qq*qq) == 1)   # 3^2 - 2*2^2 = +1; sign alternates
convergents = [(pp, qq)]
for _ in range(12):
    pp, qq = pp + 2*qq, pp + qq
    convergents.append((pp, qq))
    pell_ok = pell_ok and abs(pp*pp - 2*qq*qq) == 1
assert pell_ok
PELL_OK = 1

p2, q2 = convergents[-1]
pell_lo = Fraction(p2, q2) - Fraction(1, q2*q2)
pell_hi = Fraction(p2, q2) + Fraction(1, q2*q2)
SQRT2_ANCHOR = Fraction(1414213562373, 10**12)  # sqrt(2) to 12 decimals
assert sq_lo <= SQRT2_ANCHOR <= sq_hi
assert pell_lo <= SQRT2_ANCHOR <= pell_hi
SQRT2_OK = 1

print(f"E_OK={E_OK}")
print(f"CASSINI_OK={CASSINI_OK}")
print(f"PHI_RESIDUAL_OK={PHI_RESIDUAL_OK}")
print(f"PHI_OK={PHI_OK}")
print(f"PELL_OK={PELL_OK}")
print(f"SQRT2_OK={SQRT2_OK}")
print(f"E_DIGITS12={(e_lo.numerator * 10**12) // e_lo.denominator}")
