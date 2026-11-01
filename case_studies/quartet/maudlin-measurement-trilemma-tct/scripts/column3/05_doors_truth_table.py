#!/usr/bin/env python3
"""Column 3 (TCT) — The three-doors truth table, step re-derivation.

Steps re-derived:
  - Model constraint (from script 01): C1 & C2 & C3 cannot hold jointly.
    In classical valuation terms: at most two of the three can be true.
  - The valuations satisfying the constraint: 7 of 8 (all but 111).
  - The three 'doors' are the exactly-two-true valuations:
      C1&C2 (give up C3)  -> many-worlds
      C1&C3 (give up C2)  -> objective collapse (GRW, Diosi-Penrose)
      C2&C3 (give up C1)  -> Bohmian mechanics
  - Sidesteppers (QBism, RQM) reject the *framing* of one claim rather than
    paying inside it: QBism rejects C1's physicalist reading; RQM makes C3
    observer-relative. Both are recorded as semantic relocations, not
    additional doors (axioms/notes in the Lean tier).

Two disjoint derivation paths per witness:
  - admissible valuation count: explicit enumeration vs. binomial count
    C(3,0)+C(3,1)+C(3,2)
  - door count: enumerate exactly-two valuations vs. C(3,2)

UBP: int only; no floats, no random, no SHA-256, stdlib only.
"""
from math import comb

C1, C2, C3 = 0, 1, 2
names = {C1: "completeness", C2: "linearity", C3: "single outcomes"}

def consistent(val):
    # model constraint: not all three
    return not (val[C1] and val[C2] and val[C3])

valuations = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]

admissible = [v for v in valuations if consistent(v)]
inadmissible = [v for v in valuations if not consistent(v)]

# path 1: enumeration count
admissible_p1 = len(admissible)
# path 2: binomial count
admissible_p2 = comb(3, 0) + comb(3, 1) + comb(3, 2)
assert admissible_p1 == admissible_p2 == 7
ADMISSIBLE = admissible_p1

INCONSISTENT_VALUATIONS = len(inadmissible)
assert INCONSISTENT_VALUATIONS == 1 and inadmissible == [(1, 1, 1)]

# doors: exactly two claims kept (one sacrificed)
doors = [v for v in valuations if sum(v) == 2]
assert len(doors) == comb(3, 2) == 3
DOORS = len(doors)

door_map = {
    (1, 1, 0): ("many-worlds (Everett)", "sacrifices C3: single outcomes"),
    (1, 0, 1): ("objective collapse (GRW / Diosi-Penrose)", "sacrifices C2: linear evolution"),
    (0, 1, 1): ("Bohmian mechanics", "sacrifices C1: completeness of the wavefunction"),
}
assert set(doors) == set(door_map)

# each door keeps exactly the two claims the trilemma allows jointly
for v, (family, price) in door_map.items():
    kept = [names[i] for i in range(3) if v[i]]
    dropped = [names[i] for i in range(3) if not v[i]]
    assert len(kept) == 2 and len(dropped) == 1

# pairwise exclusion is equivalent to the joint constraint (classical logic):
# from not(C1&C2&C3): (C1&C3 -> not C2) etc.  Check by enumeration.
for v in valuations:
    if v[C1] and v[C3] and v[C2]:
        assert not consistent(v)
    if v[C1] and v[C2] and v[C3]:
        assert not consistent(v)
    if v[C2] and v[C3] and v[C1]:
        assert not consistent(v)
PAIRWISE_EQUIVALENCE = 1

print(f"ADMISSIBLE={ADMISSIBLE}")
print(f"INCONSISTENT_VALUATIONS={INCONSISTENT_VALUATIONS}")
print(f"DOORS={DOORS}")
print(f"PAIRWISE_EQUIVALENCE={PAIRWISE_EQUIVALENCE}")
for v, (family, price) in sorted(door_map.items()):
    print(f"DOOR_{v[0]}{v[1]}{v[2]}={family} ({price})")
