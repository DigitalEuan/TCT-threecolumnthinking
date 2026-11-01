#!/usr/bin/env python3
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
