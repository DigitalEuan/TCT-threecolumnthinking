#!/usr/bin/env python3
"""T09 - What comes next: 2, 4, 8, 16, ...? (refusal: UNDERDETERMINED)"""
from fractions import Fraction as F

givens = [2, 4, 8, 16]

# witness 1: geometric (ratio 2)
geo = [2 ** i for i in range(1, 6)]
assert geo[:4] == givens and geo[4] == 32

# witness 2: interpolating cubic via the finite-difference tower
seq = list(givens)
tower = [seq]
while len(tower[-1]) > 1:
    tower.append([b - a for a, b in zip(tower[-1], tower[-1][1:])])
assert tower[1] == [2, 4, 8] and tower[2] == [2, 4] and tower[3] == [2]
d3, d2, d1 = 2, tower[2][-1] + 2, tower[1][-1] + tower[2][-1] + 2
assert (d2, d1) == (6, 14)
cubic_next = givens[-1] + d1
assert cubic_next == 16 + 14 == 30            # = 16+8+4+2 (the Lean witness)

# witness 3: Moser's circle-region sequence R(n) = C(n,4)+C(n,2)+1
def C(a, b):
    num = den = 1
    for i in range(b):
        num *= a - i; den *= i + 1
    return num // den
moser = [C(k, 4) + C(k, 2) + 1 for k in range(1, 7)]
assert moser[1:5] == givens and moser[5] == 31  # R(2)..R(5) match; next R(6)=31

# the three licensed continuations disagree -> uniqueness disproved
witnesses = [32, 30, 31]
assert len(set(witnesses)) == 3
assert 32 == 30 + 2 and 31 == 30 + 1
REFUSED = "UNDERDETERMINED"                    # conventional 32 only under named simplicity axiom

print(f"GEOMETRIC={geo[4]}")
print(f"CUBIC={cubic_next}")
print(f"MOSER={moser[4]}")
print("DISAGREE=1")
print(f"REFUSAL={REFUSED}")
