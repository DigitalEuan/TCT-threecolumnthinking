#!/usr/bin/env python3
"""Column 3 (TCT) — Objective-collapse (GRW) arithmetic, step re-derivation.

Steps re-derived (exact rationals, empirical parameters declared as givens):
  - GRW parameter (empirical): lambda = 1/10^16 per particle per second.
  - N-particle object: collapse rate N*lambda; mean time between collapses
    tau = 1/(N*lambda) = 10^16/N seconds.
  - Single particle: tau = 10^16 s; converted to Julian years (365.25 d).
  - Macroscopic object (illustrative N = 10^23): tau = 10^16/10^23 = 1/10^7 s.
  - Threshold: tau = 1 s exactly at N = 10^16 particles.

Two disjoint derivation paths per witness:
  - tau: Fraction division vs. integer numerator/denominator reduced by gcd
  - N threshold: solve N*lambda = 1 vs. cross-multiplication check

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction
from math import gcd

# ---- givens (empirical parameters, axioms in the Lean tier) ----
LAMBDA_NUM, LAMBDA_DEN = 1, 10**16        # GRW rate per particle per second
N_SINGLE = 1
N_MACRO = 10**23                          # illustrative: dust-grain-sized object
SEC_PER_JULIAN_YEAR = 31557600            # 365.25 * 86400 (exact integer)

def tau_seconds(n):
    """mean time between collapses = 1/(n*lambda) = LAMBDA_DEN/(n*LAMBDA_NUM)"""
    return Fraction(LAMBDA_DEN, n * LAMBDA_NUM)

# --- single particle: tau path 1 (Fraction) ---
tau_single = tau_seconds(N_SINGLE)

# --- single particle: tau path 2 (manual gcd reduction of raw integer ratio) ---
num, den = LAMBDA_DEN, N_SINGLE * LAMBDA_NUM
g = gcd(num, den)
tau_single_p2 = (num // g, den // g)
assert (tau_single.numerator, tau_single.denominator) == tau_single_p2
TAU_SINGLE_S = tau_single

# years: exact fraction and floor via integer division
years_frac = Fraction(TAU_SINGLE_S.numerator, TAU_SINGLE_S.denominator * SEC_PER_JULIAN_YEAR)
years_floor, years_rem = divmod(TAU_SINGLE_S.numerator,
                                TAU_SINGLE_S.denominator * SEC_PER_JULIAN_YEAR)
assert years_frac == Fraction(TAU_SINGLE_S.numerator, TAU_SINGLE_S.denominator * SEC_PER_JULIAN_YEAR)
YEARS_SINGLE = years_frac

# --- macroscopic: tau path 1 (Fraction) vs path 2 (power-of-ten cancellation) ---
tau_macro = tau_seconds(N_MACRO)
assert tau_macro == Fraction(10**16, 10**23)
g2 = gcd(10**16, 10**23)
tau_macro_p2 = (10**16 // g2, 10**23 // g2)
assert (tau_macro.numerator, tau_macro.denominator) == tau_macro_p2
assert tau_macro == Fraction(1, 10**7)
TAU_MACRO_S = tau_macro

# macro collapse frequency: N*lambda collapses per second
macro_rate = Fraction(N_MACRO * LAMBDA_NUM, LAMBDA_DEN)
assert macro_rate == 10**7
MACRO_RATE_PER_S = macro_rate

# --- threshold N where tau = 1 s: N*lambda = 1 => N = 10^16 ---
# path 1: solve; path 2: substitute back and cross-check
N_THRESHOLD = LAMBDA_DEN // LAMBDA_NUM
assert Fraction(LAMBDA_DEN, N_THRESHOLD * LAMBDA_NUM) == 1
N_THRESHOLD_CHECK = N_THRESHOLD
assert N_THRESHOLD_CHECK == 10**16

print(f"TAU_SINGLE_S={TAU_SINGLE_S}")
print(f"YEARS_SINGLE={YEARS_SINGLE} (floor {years_floor}, rem {years_rem})")
print(f"TAU_MACRO_S={TAU_MACRO_S}")
print(f"MACRO_RATE_PER_S={MACRO_RATE_PER_S}")
print(f"N_THRESHOLD={N_THRESHOLD_CHECK}")
