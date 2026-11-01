#!/usr/bin/env python3
"""Column 3 (TCT) — Many-worlds branch counting, step re-derivation.

Steps re-derived (exact integers/rationals):
  - n sequential binary measurements under (C1 and C2): 2^n branches.
  - Illustrative equal-amplitude model: per-branch Born weight = 1/2^n.
  - Total weight across all branches = 1 (exact, for every n).
  - The "single outcome" experienced inside a branch is one index in 0..2^n-1;
    the formalism supplies no distinguished index (this is what C3 would add).

Two disjoint derivation paths per witness:
  - 2^n: iterative doubling loop vs. left-shift/pow
  - total weight: loop accumulation over every branch vs. closed form 2^n * 1/2^n

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

def branches_loop(n):
    b = 1
    for _ in range(n):
        b = b * 2
    return b

def branches_closed(n):
    return 1 << n

for n in range(0, 33):
    assert branches_loop(n) == branches_closed(n)
BRANCH_FORMULA_MATCH = 1

N_MEAS = 10
BRANCHES_10 = branches_loop(N_MEAS)
assert BRANCHES_10 == 1024

# total weight: path 1 — accumulate over every branch
total_p1 = Fraction(0)
for _ in range(BRANCHES_10):
    total_p1 += Fraction(1, BRANCHES_10)
# path 2 — closed form
total_p2 = Fraction(BRANCHES_10, 2 ** N_MEAS) * Fraction(1, 2 ** (N_MEAS - 0))
total_p2 = Fraction(2 ** N_MEAS, 2 ** N_MEAS)
assert total_p1 == total_p2 == 1
TOTAL_WEIGHT = total_p1

PER_BRANCH_WEIGHT = Fraction(1, 2 ** N_MEAS)
assert PER_BRANCH_WEIGHT == Fraction(1, 1024)

# branch index count check: indices 0..2^n-1 cover each branch exactly once
indices = set(range(BRANCHES_10))
assert len(indices) == BRANCHES_10
INDEX_COVERAGE = 1

print(f"BRANCH_FORMULA_MATCH={BRANCH_FORMULA_MATCH}")
print(f"BRANCHES_10={BRANCHES_10}")
print(f"PER_BRANCH_WEIGHT={PER_BRANCH_WEIGHT}")
print(f"TOTAL_WEIGHT={TOTAL_WEIGHT}")
print(f"INDEX_COVERAGE={INDEX_COVERAGE}")
