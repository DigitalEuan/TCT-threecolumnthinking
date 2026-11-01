#!/usr/bin/env python3
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
