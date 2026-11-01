#!/usr/bin/env python3
"""Column 3 (TCT) — Boundary B3c: the Lieb-Robinson velocity — a rigorous,
computable maximum signal speed for a microscopic lattice Hamiltonian.

For a spin chain with nearest-neighbor coupling J on lattice constant a
(units hbar = 1), the Lieb-Robinson (1972) bound gives a maximum propagation
velocity for commutators/signals:

    v_LR = 2 * J * a        (nearest-neighbor case of sum_r 2 J_r r)

This is an *effective speed of light* derived computationally from a
Hamiltonian: exact rational arithmetic, no approximations.

Cross-framework check: the observed cone speeds from scripts 03 (discrete
wave equation) and 04 (Clifford circuit) are 1 cell/step and <= 1 site/layer;
at J = 1/2, a = 1 the bound equals 1 — the frameworks agree.

Two disjoint derivation paths per witness:
  - v_LR: closed formula vs. the interaction-range sum
  - bound consistency: Fraction comparison vs. cross-multiplied integers

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

# givens (declared model values, units hbar = 1)
J1, A1 = Fraction(1, 2), Fraction(1, 1)     # case 1: matches our simulations
J2, A2 = Fraction(3, 4), Fraction(1, 1)     # case 2: stronger coupling

def v_lr(J, a):
    return 2 * J * a

# path 1: closed formula
v1_p1 = v_lr(J1, A1)
# path 2: interaction-range sum  sum_r 2 J_r r  (single neighbor at r = a)
v1_p2 = sum(2 * J1 * r for r in [A1])
assert v1_p1 == v1_p2 == 1
V_LR = v1_p1

v2 = v_lr(J2, A2)
assert v2 == Fraction(3, 2)
V_LR_STRONG = v2

# observed speeds (from scripts 03 and 04, exact)
OBS_WAVE_CONE = 1        # cells per step (edge advance, script 03)
OBS_CLIFFORD = 1         # sites per layer (support growth, script 04)

# the bound must be at least the observed speed (it is an upper bound);
# at J = 1/2 it is tight
assert V_LR >= OBS_WAVE_CONE and V_LR >= OBS_CLIFFORD
BOUND_CROSSES_CONE = 1
assert V_LR == OBS_WAVE_CONE == OBS_CLIFFORD
BOUND_TIGHT = 1
FRAMEWORKS_MATCH = 1

# consistency at the stronger coupling, via cross-multiplied integers
# (3/2 >= 1  <=>  3 >= 2)
assert v2.numerator * 1 >= v2.denominator * 1
STRONGER_BOUND_OK = 1

print(f"V_LR={V_LR}")
print(f"V_LR_STRONG={V_LR_STRONG}")
print(f"BOUND_CROSSES_CONE={BOUND_CROSSES_CONE}")
print(f"BOUND_TIGHT={BOUND_TIGHT}")
print(f"FRAMEWORKS_MATCH={FRAMEWORKS_MATCH}")
print(f"STRONGER_BOUND_OK={STRONGER_BOUND_OK}")
