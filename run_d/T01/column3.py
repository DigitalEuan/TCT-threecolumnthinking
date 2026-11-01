#!/usr/bin/env python3
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
