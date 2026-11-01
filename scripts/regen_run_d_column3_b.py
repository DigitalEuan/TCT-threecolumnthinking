#!/usr/bin/env python3
"""Regenerate Run D Column-3 scripts, part B (T07-T12)."""
import os

OUT = "/home/z/my-project/tct_run_d"

SCRIPTS = {}

SCRIPTS["T07"] = '''#!/usr/bin/env python3
"""T07 - How many ways to choose 2 toppings from 5? (combinatorics)"""
from fractions import Fraction as F

n, k = 5, 2
fact = [1, 1, 2, 6, 24, 120]                  # 0!..5! (core Lean has no Nat.factorial)

formula = fact[n] // (fact[k] * fact[n - k])   # 5!/(2!3!)
enum = sum(n - i for i in range(1, n))        # pairs by first element: 4+3+2+1
pascal = fact[4] // (fact[1] * fact[3]) + fact[4] // (fact[2] * fact[2])  # C(4,1)+C(4,2)
complement = fact[n] // (fact[n - k] * fact[k])  # C(5,3) = C(5,2)
ordered = n * (n - 1) // 2                    # ordered/2: representation variant (audited out)
assert formula == enum == pascal == complement == ordered == 10

print(f"FORMULA={formula}")
print(f"ENUM={enum}")
print(f"PASCAL={pascal}")
print(f"COMPLEMENT={complement}")
print(f"ANSWER={formula}")
'''

SCRIPTS["T08"] = '''#!/usr/bin/env python3
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
'''

SCRIPTS["T09"] = '''#!/usr/bin/env python3
"""T09 - What comes next: 2, 4, 8, 16, ...? (refusal: UNDERDETERMINED)"""
from fractions import Fraction as F

givens = [2, 4, 8, 16]

# witness 1: geometric (ratio 2)
geo = [2 ** i for i in range(1, 6)]
assert geo[:4] == givens and geo[4] == 32

# witness 2: interpolating cubic via the finite-difference tower
seq = list(givens)
tower = [seq]
while len(tower[-1]) > 1:
    tower.append([b - a for a, b in zip(tower[-1], tower[-1][1:])])
assert tower[1] == [2, 4, 8] and tower[2] == [2, 4] and tower[3] == [2]
d3, d2, d1 = 2, tower[2][-1] + 2, tower[1][-1] + tower[2][-1] + 2
assert (d2, d1) == (6, 14)
cubic_next = givens[-1] + d1
assert cubic_next == 16 + 14 == 30            # = 16+8+4+2 (the Lean witness)

# witness 3: Moser's circle-region sequence R(n) = C(n,4)+C(n,2)+1
def C(a, b):
    num = den = 1
    for i in range(b):
        num *= a - i; den *= i + 1
    return num // den
moser = [C(k, 4) + C(k, 2) + 1 for k in range(1, 7)]
assert moser[1:5] == givens and moser[5] == 31  # R(2)..R(5) match; next R(6)=31

# the three licensed continuations disagree -> uniqueness disproved
witnesses = [32, 30, 31]
assert len(set(witnesses)) == 3
assert 32 == 30 + 2 and 31 == 30 + 1
REFUSED = "UNDERDETERMINED"                    # conventional 32 only under named simplicity axiom

print(f"GEOMETRIC={geo[4]}")
print(f"CUBIC={cubic_next}")
print(f"MOSER={moser[4]}")
print("DISAGREE=1")
print(f"REFUSAL={REFUSED}")
'''

SCRIPTS["T10"] = '''#!/usr/bin/env python3
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
'''

SCRIPTS["T11"] = '''#!/usr/bin/env python3
"""T11 - A light is off; the switch is flipped 17 times (F2 at declared XOR site)"""

FLIPS = 17
# declared reading: each flip toggles the state (switch convention)
# state = 0 XOR (FLIPS mod 2)  -- parity arithmetic in F2:
parity = FLIPS % 2
assert parity == 1
final_state = (0 + FLIPS) % 2
assert final_state == 1                        # ON (odd number of toggles)
even_check = (0 + 16) % 2
assert even_check == 0                         # 16 flips would return OFF
# the general parity law (Lean: omega): (n+2) % 2 = n % 2
for n in range(-6, 24):
    assert (n + 2) % 2 == n % 2

print(f"FLIPS={FLIPS}")
print(f"PARITY={parity}")
print(f"FINAL_STATE={final_state}")
print(f"EVEN_CHECK={even_check}")
print(f"ANSWER_STATE={final_state}")
'''

SCRIPTS["T12"] = '''#!/usr/bin/env python3
"""T12 - Given V=12 V, I=5 A, R=4 Ohm, what is the power? (refusal: INCONSISTENT_GIVENS)"""

V, I, R = 12, 5, 4
# the three licensed readings of "the power":
ohm_lhs, ohm_rhs = V, I * R                    # V = IR ?
P_vi = V * I                                   # P = VI
P_i2r = I * I * R                              # P = I^2 R
P_v2r = V * V // R if V * V % R == 0 else V * V / R  # P = V^2/R
assert (ohm_lhs, ohm_rhs) == (12, 20)
assert ohm_lhs != ohm_rhs                      # Ohm's law already violated
assert (P_vi, P_i2r, P_v2r) == (60, 100, 36)
assert P_vi != P_i2r and P_vi != P_v2r and P_i2r != P_v2r
# every pair of readings disagrees -> the givens are jointly inconsistent
REFUSED = "INCONSISTENT_GIVENS"

print(f"OHM_V={ohm_lhs}")
print(f"OHM_IR={ohm_rhs}")
print(f"P_VI={P_vi}")
print(f"P_I2R={P_i2r}")
print(f"P_V2R={P_v2r}")
print(f"REFUSAL={REFUSED}")
'''


def main():
    for name, src in SCRIPTS.items():
        d = os.path.join(OUT, name)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "column3.py"), "w", encoding="utf-8") as f:
            f.write(src)
        print(f"wrote {d}/column3.py")


if __name__ == "__main__":
    main()
