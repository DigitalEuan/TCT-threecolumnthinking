#!/usr/bin/env python3
"""Column 3 (TCT) — Boundary B4: the value boundary — alpha, and the refusal.
In dimensionless terms the speed of light is not 299,792,458 (that is unit
bookkeeping, script 01) but c = 1/alpha in atomic units: one dimensionless
number, MEASURED (fine-structure constant, CODATA).

Given alpha, everything about c's value is computable (bookkeeping again —
computed exactly below). Deriving alpha itself from theory/computation is an
OPEN problem; every known claim of a closed derivation is numerology-class
(Eddington lineage) and is registered as WOULD_BE_GUESS by this study's
refusal taxonomy.

Givens (empirical, CODATA 2018): alpha = 7.2973525693(11) x 10^-3,
i.e. alpha = 72973525693/10^13 with uncertainty +/-11 in the last digits.

Two disjoint derivation paths per witness:
  - floor(1/alpha): exact integer division vs. cross-multiplied inequalities
  - interval endpoints: Fraction reciprocals vs. inequality-direction check

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

ALPHA_NUM, ALPHA_DEN = 72973525693, 10**13    # empirical (CODATA 2018)
UNC = 11                                        # +/- in last digits

alpha = Fraction(ALPHA_NUM, ALPHA_DEN)
alpha_lo = Fraction(ALPHA_NUM - UNC, ALPHA_DEN)
alpha_hi = Fraction(ALPHA_NUM + UNC, ALPHA_DEN)
assert alpha_lo < alpha < alpha_hi

# 1/alpha in atomic units: c's dimensionless value
inv_alpha = Fraction(ALPHA_DEN, ALPHA_NUM)

# floor(1/alpha): two paths
floor_p1 = inv_alpha.numerator // inv_alpha.denominator
floor_p2 = 137 if (137 * ALPHA_NUM <= ALPHA_DEN < 138 * ALPHA_NUM) else -1
assert floor_p1 == floor_p2 == 137
INV_ALPHA_FLOOR = floor_p1

# uncertainty interval for 1/alpha (reciprocal reverses inequalities)
inv_lo = Fraction(ALPHA_DEN, ALPHA_NUM + UNC)     # 1/alpha_hi
inv_hi = Fraction(ALPHA_DEN, ALPHA_NUM - UNC)     # 1/alpha_lo
# direction check by cross-multiplication (independent path)
assert inv_lo * alpha_hi <= 1 and inv_hi * alpha_lo >= 1
assert inv_lo <= inv_alpha <= inv_hi
INTERVAL_OK = 1

width = inv_hi - inv_lo
assert width == Fraction(ALPHA_DEN * 2 * UNC, (ALPHA_NUM - UNC) * (ALPHA_NUM + UNC))
WIDTH = width

# --- the boundary, stated as this study's verdict ---
# given alpha: derivable exactly (above).  alpha from theory: OPEN.
DERIVATION_FROM_ALPHA = 1
ALPHA_FROM_THEORY = 0
# REFUSED: WOULD_BE_GUESS — any claimed parameter-free derivation of alpha
# (or of c's dimensionless value) that is not in the ledger as proved.
REFUSAL_REGISTERED = 1
assert ALPHA_FROM_THEORY == 0 and REFUSAL_REGISTERED == 1

print(f"INV_ALPHA={inv_alpha}")
print(f"INV_ALPHA_FLOOR={INV_ALPHA_FLOOR}")
print(f"WIDTH={WIDTH}")
print(f"INTERVAL_OK={INTERVAL_OK}")
print(f"DERIVATION_FROM_ALPHA={DERIVATION_FROM_ALPHA}")
print(f"ALPHA_FROM_THEORY={ALPHA_FROM_THEORY}")
print(f"REFUSAL_REGISTERED={REFUSAL_REGISTERED}")
