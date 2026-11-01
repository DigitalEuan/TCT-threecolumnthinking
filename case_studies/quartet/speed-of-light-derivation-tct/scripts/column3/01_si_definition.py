#!/usr/bin/env python3
"""Column 3 (TCT) — Boundary B1: the SI value of c is DEFINED, not derived.
Since the 1983/2019 SI, c = 299,792,458 m/s exactly: the meter is *defined*
from c. A computation that outputs this number is doing unit bookkeeping.

This script computes the definitional chain exactly (so the triviality is
itself witnessed, not asserted): light-second, light-year, nanosecond-scale
distances, all as exact integers/rationals, each by two disjoint paths.

Verdict key DEFINITIONAL=1: these identities are consequences of a
*definition*, not a physical derivation. The physical derivations live in
scripts 02-05; the boundary lives in script 06.

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction
from math import gcd

C_SI = 299792458            # m/s, exact by definition (SI)
SEC_PER_JULIAN_YEAR = 31557600   # 365.25 * 86400, exact

# 1 light-second in meters (definitional identity, path 1: direct)
light_second_m = C_SI * 1
assert light_second_m == 299792458

# light-year in meters: c * seconds/year — two paths: direct vs. expanded product
ly_p1 = C_SI * SEC_PER_JULIAN_YEAR
ly_p2 = sum(C_SI * (31557600 // 10**k % 10) * 10**k for k in range(8))  # digit-wise
assert ly_p1 == ly_p2
LIGHT_YEAR_M = ly_p1

# nanosecond in centimeters: c * 1e-9 s = 0.299792458 m = 29.9792458 cm
ns_m = Fraction(C_SI, 10**9)
ns_cm = ns_m * 100
# two paths: Fraction vs. manual gcd reduction of the raw integer ratio
num, den = C_SI * 100, 10**9
g = gcd(num, den)
ns_cm_p2 = (num // g, den // g)
assert (ns_cm.numerator, ns_cm.denominator) == ns_cm_p2
NS_CM = ns_cm

# meter in light-seconds: 1/299792458 exactly
m_in_lightseconds = Fraction(1, C_SI)
assert m_in_lightseconds.numerator == 1 and m_in_lightseconds.denominator == C_SI

# every identity above follows from the DEFINITION alone: no empirical input
DEFINITIONAL = 1

print(f"LIGHT_SECOND_M={light_second_m}")
print(f"LIGHT_YEAR_M={LIGHT_YEAR_M}")
print(f"NS_CM={NS_CM}")
print(f"M_IN_LIGHTSECONDS={m_in_lightseconds}")
print(f"DEFINITIONAL={DEFINITIONAL}")
