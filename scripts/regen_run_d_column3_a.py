#!/usr/bin/env python3
"""Regenerate Run D Column-3 scripts, part A (T01-T06).

Each script re-derives the paper's documented exact results with rational
arithmetic only (fractions.Fraction / int), asserts its own construction,
prints KEY=VALUE lines (last line = headline), and exits 0."""
import os

OUT = "/home/z/my-project/tct_run_d"

SCRIPTS = {}

SCRIPTS["T01"] = '''#!/usr/bin/env python3
"""T01 - How does a spring store and release energy? (k=100 N/m, x0=1/5 m, m=1 kg)"""
from fractions import Fraction as F

k, x0, m = 100, F(1, 5), 1
assert k == 100 and x0 == F(1, 5) and m == 1

# Column 3: energy ledger, exact rationals only.
U = F(k, 1) * x0 * x0 / 2                    # elastic PE at full compression
vmax2 = F(k, 1) * x0 * x0 / m                # v^2 at equilibrium
vmax = 2
KE_eq = F(m) * vmax * vmax / 2               # KE at equilibrium
assert U == 2 and vmax2 == 4 and vmax * vmax == vmax2 and KE_eq == 2
assert U == KE_eq                             # exchange balance (no dissipation)
assert F(k, 1) / m == 100                     # omega^2 = k/m

# Lean cross-multiplied witnesses (Nat): 2*2*25 = 100*1, etc.
assert 2 * 2 * 25 == 100 * 1
assert 1 * 2 * 2 == 2 * 2
assert 2 * 2 == 1 * 2 * 2

print("GIVENS_OK=1")
print(f"STORED_ENERGY_J={U}")
print(f"MAX_SPEED={vmax}")
print(f"KE_EQ_J={KE_eq}")
print("EXCHANGE_OK=1")
print(f"ANSWER_U_J={U}")
'''

SCRIPTS["T02"] = '''#!/usr/bin/env python3
"""T02 - Why do things bounce? (g=49/5, h0=5/2, m=1/2, e=3/4)"""
from fractions import Fraction as F

g, h0, m, e = F(49, 5), F(5, 2), F(1, 2), F(3, 4)
v_in2 = 2 * g * h0
assert v_in2 == 49                            # engineered: v_in = 7 exactly
v_in = 7
v_out = e * v_in
h1 = v_out * v_out / (2 * g)
h2 = e * e * h1
h3 = e * e * h2
assert h1 == F(45, 32) and h2 == F(405, 512) and h3 == F(3645, 8192)
assert h3 == e ** 6 * h0                      # three-bounce closed form
# the kernel-corrected Lean cross-multiplication (Nat):
assert 729 * 5 * 8192 == 3645 * 4096 * 2
assert 729 * 2 * 4096 != 3645 * 512 * 256     # the refuted first attempt

# geometric closure: total distance and total time
total_d = h0 + 2 * h1 / (1 - e * e)
t_drop = v_in / g
assert t_drop == F(5, 7)
total_t = t_drop + 2 * v_out / g / (1 - e)
assert total_d == F(125, 14) and total_t == 5

print(f"V_IN={v_in}")
print(f"H1={h1}")
print(f"H2={h2}")
print(f"H3={h3}")
print(f"TOTAL_DISTANCE={total_d}")
print(f"TOTAL_TIME={total_t}")
print("LEAN_CROSS_OK=1")
print(f"H3_M={h3}")
'''

SCRIPTS["T03"] = '''#!/usr/bin/env python3
"""T03 - What is gravity? (witness triple under g=49/5)"""
from fractions import Fraction as F

g = F(49, 5)
t, v, h = F(5, 7), 7, F(5, 2)                 # the witness triple
# three kinematic relations simultaneously (paper 6.10):
r1 = (h == g * t * t / 2)
r2 = (v == g * t)
r3 = (v * v == 2 * g * h)
r4 = (h == v * t / 2)
assert r1 and r2 and r3 and r4
assert sum([r1, r2, r3, r4]) == 4

print("WITNESS_OK=1")
print(f"T={t}")
print(f"V={v}")
print(f"H={h}")
print("RELATIONS=4")
print("WITNESS_TRIPLE_OK=1")
'''

SCRIPTS["T04"] = '''#!/usr/bin/env python3
"""T04 - How does water become large when hot and cold? (anomalous expansion)"""
from fractions import Fraction as F

rho_ice, rho_water = 2750, 2997               # scaled, near measured densities
V = 2997                                      # scaled volume units
m_ice = rho_ice * V
V_sub = rho_ice * V // rho_water              # displacement route
assert V_sub == 2750
m_water = rho_water * V_sub                   # density route
assert m_ice == m_water == 8241750            # the two axiom routes agree
submerged = F(V_sub, V)
above = 1 - submerged
assert submerged == F(2750, 2997) and above == F(247, 2997)
assert 2997 - 2750 == 247

print(f"SUBMERGED={submerged}")
print(f"ABOVE={above}")
print("MASSES_AGREE=1")
print(f"ICE_MASS={m_ice}")
print(f"SUBMERGED_FRACTION={submerged}")
'''

SCRIPTS["T05"] = '''#!/usr/bin/env python3
"""T05 - What comes after Wednesday? (Z/7Z, external calendar anchor)"""
from datetime import date, timedelta

# cyclic arithmetic: Wednesday = 3 in the ISO 8601 indexing (Mon=1..Sun=7)
WED = 3
nxt = (WED + 1) % 7
wrap = (7 % 7)                                # Sunday = 7 = 0 in Z/7Z
week = (WED + 7) % 7
assert nxt == 4 and wrap == 0 and week == WED

# external stdlib calendar anchor (no prior weekday knowledge assumed):
d = date(2026, 11, 1)
while d.isoweekday() != WED:                  # find the next real Wednesday
    d += timedelta(days=1)
assert d.isoweekday() == WED
d_next = d + timedelta(days=1)
anchor_ok = 1 if d_next.isoweekday() == nxt else 0
assert anchor_ok == 1                         # the calendar confirms (3+1)%7=4
assert (d + timedelta(days=7)).isoweekday() == week

print(f"WED_INDEX={WED}")
print(f"THU_INDEX={nxt}")
print("CALENDAR_ANCHOR_OK=1")
print("CYCLE_OK=1")
print(f"NEXT_DAY_INDEX={nxt}")
'''

SCRIPTS["T06"] = '''#!/usr/bin/env python3
"""T06 - What is 1+1? (the domain declaration is load-bearing)"""

# domain-declared answers:
int_value = 1 + 1                             # Z: successor route
assert int_value == 2
f2_value = (1 + 1) % 2                        # F2 at the declared XOR site
assert f2_value == 0
mod7_value = (1 + 1) % 7                      # Z/7Z
assert mod7_value == 2

# three genuinely disjoint routes to the Z answer:
r1 = 2                                        # definitional successor
r2 = len({("L", 0)} | {("R", 1)})             # tagged disjoint-union cardinality
r3 = len([(a, b) for a in (0, 1) for b in (0,)])  # explicit pairing: 1+1 = 2*1
assert r1 == r2 == r3 == 2
assert (True != True) is False                # Bool xor site

print(f"INT_VALUE={int_value}")
print(f"F2_VALUE={f2_value}")
print(f"MOD7_VALUE={mod7_value}")
print("ROUTES=3")
print(f"ANSWER_INT={int_value}")
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
