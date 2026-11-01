#!/usr/bin/env python3
"""Column 3 (TCT) — Hurdle H5: ODE integration — continuous-time physics vs. steppers.
Physical isomorphism: an analog computer (RC op-amp integrator, spring-mass)
evolves dy/dt = f(y,t) in continuous physical time (primitives `state_space`,
`accum`, `rate`); the digital solver pays one sequential step per increment.

Exact problem (rational witnesses throughout): y' = 3 t^2, y(0) = 0, so
y(1) = 1 exactly. Euler with M steps of h = 1/M:
  y_M = sum_{i<M} h * 3 (i h)^2 = (M-1)(2M-1) / (2 M^2)
  error e_M = 1 - y_M = (3M-1) / (2 M^2)          [closed form, verified below]

Analog floor (declared illustrative): a physical integrator holds a fixed
offset error eps_a = 1/1000. The digital solver must take M steps to match
that accuracy.

Two disjoint derivation paths per witness:
  - closed error formula vs. direct Fraction loop for M = 1..20
  - minimum M: enumeration vs. direct substitution at the boundary

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

def euler_y(M):
    h = Fraction(1, M)
    y = Fraction(0)
    for i in range(M):
        t = h * i
        y += h * 3 * t * t
    return y

def error_formula(M):
    return Fraction(3 * M - 1, 2 * M * M)

# --- formula vs. direct loop (two paths), M = 1..20 ---
for M in range(1, 21):
    assert 1 - euler_y(M) == error_formula(M)
FORMULA_MATCH = 1

M10 = 10
e10 = 1 - euler_y(M10)
assert e10 == Fraction(29, 200) == error_formula(M10)
ERROR_M10 = e10

# --- minimum M with e_M <= 1/1000 (analog error floor) ---
EPS_A = Fraction(1, 1000)

# path 1: enumeration
m_enum = None
for M in range(1, 10000):
    if error_formula(M) <= EPS_A:
        m_enum = M
        break
# path 2: direct substitution at the boundary (integer cross-multiplication:
# 1000(3M-1) <= 2M^2)
def boundary_ok(M):
    return 1000 * (3 * M - 1) <= 2 * M * M
assert m_enum == 1500 and boundary_ok(1500) and not boundary_ok(1499)
M_MIN = m_enum

# --- the measured improvement (declared model) ---
# digital sequential integration steps to match the analog error floor: M_MIN
# analog physical steps: 1 (continuous evolution; accuracy set by offset eps_a)
STEP_RATIO = M_MIN                      # 1500 digital steps per 1 analog evolution
assert STEP_RATIO == 1500

print(f"FORMULA_MATCH={FORMULA_MATCH}")
print(f"ERROR_M10={ERROR_M10}")
print(f"ANALOG_ERROR={EPS_A}")
print(f"M_MIN={M_MIN}")
print(f"STEP_RATIO={STEP_RATIO}")
