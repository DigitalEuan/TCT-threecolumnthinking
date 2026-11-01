#!/usr/bin/env python3
"""Column 3 (TCT) — Boundary B2: the physical identification c_EM = c_light.
Maxwell (1861-65): the speed of transverse EM waves is 1/sqrt(mu0*eps0), and
the ratio of electromagnetic to electrostatic charge units (Weber-Kohlrausch
1856) numerically equals the measured speed of light -> light IS EM waves.

Historical determinations (empirical givens; see docs/08):
  v_WK      = 310,740,000 m/s  (Weber-Kohlrausch 1856, EM/ESU unit ratio)
  v_Fizeau  = 313,300,000 m/s  (Fizeau 1849, toothed wheel)
  v_Foucault= 298,000,000 m/s  (Foucault 1862, rotating mirror)
  c_SI      = 299,792,458  m/s  (defined value, for retrospective comparison)

Exact results: relative differences as reduced Fractions (two paths: Fraction
vs. manual gcd), era-agreement at the 5% level (= 1/20), and ppm-scale
magnitudes via exact integer division.

This is what a *computational* derivation of c could mean before the SI fix:
compute the EM value from electrical measurements, compare with optical.
The comparison is the derivation; the numbers were empirical.

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction
from math import gcd

V_WK, V_FIZEAU, V_FOUC = 310740000, 313300000, 298000000   # empirical givens
C_SI = 299792458                                            # defined value

def rel_diff(v, c):
    return Fraction(abs(v - c), c)

def rel_diff_checked(v, c):
    num, den = abs(v - c), c
    g = gcd(num, den)
    return (num // g, den // g)

results = {}
for name, v in (("WK", V_WK), ("FIZEAU", V_FIZEAU), ("FOUCAULT", V_FOUC)):
    r1 = rel_diff(v, C_SI)
    r2 = rel_diff_checked(v, C_SI)
    assert (r1.numerator, r1.denominator) == r2
    results[name] = r1

REL_DIFF_WK = results["WK"]             # 5473771/149896229 (after reduction)
REL_DIFF_FIZEAU = results["FIZEAU"]
REL_DIFF_FOUCAULT = results["FOUCAULT"]

# absolute differences, exact integers (Lean witnesses)
diff_wk = abs(V_WK - C_SI)
diff_fizeau = abs(V_FIZEAU - C_SI)
diff_fouc = abs(V_FOUC - C_SI)
assert diff_wk == 10947542 and diff_fizeau == 13507542 and diff_fouc == 1792458

# era agreement: all three determinations within 1/20 (5%) of the modern value
max_rel = max(results.values())
assert max_rel < Fraction(1, 20)
ERAS_AGREE = 1

# ppm magnitudes via exact integer division (floor of v*1e6 / c)
def ppm_floor(v, c):
    return abs(v - c) * 10**6 // c
PPM_WK = ppm_floor(V_WK, C_SI)
PPM_FIZEAU = ppm_floor(V_FIZEAU, C_SI)
PPM_FOUC = ppm_floor(V_FOUC, C_SI)
assert PPM_WK == 36517 and PPM_FIZEAU == 45056 and PPM_FOUC == 5978

print(f"REL_DIFF_WK={REL_DIFF_WK}")
print(f"REL_DIFF_FIZEAU={REL_DIFF_FIZEAU}")
print(f"REL_DIFF_FOUCAULT={REL_DIFF_FOUCAULT}")
print(f"PPM_WK={PPM_WK}")
print(f"PPM_FIZEAU={PPM_FIZEAU}")
print(f"PPM_FOUC={PPM_FOUC}")
print(f"ERAS_AGREE={ERAS_AGREE}")
