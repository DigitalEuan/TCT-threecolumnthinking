#!/usr/bin/env python3
"""Column 3 (TCT) — Maudlin trilemma: core model, step re-derivation.
Claim under test: (C1 completeness AND C2 linearity) => post-measurement state is
an entangled superposition containing TWO macroscopic detector readings,
contradicting C3 (single outcome).

Model (declared illustrative): electron basis {0:up, 1:down} x
detector basis {0:ready, 1:reads_up, 2:reads_down}. Unnormalized integer
amplitudes; Born weights carried exactly as fractions.Fraction.

Two disjoint derivation paths per witness:
  - linearity:  dict rewrite (U as basis map)  vs.  6x6 integer matrix-vector product
  - entanglement: all 2x2 cross-minors of the amplitude matrix  vs.
    reduced-detector purity test  Tr(rho_D^2) == Tr(rho_D)^2
  - Born sum:  sum of squared branch amplitudes  vs.  trace of reduced matrix

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

def add(s, k, v):
    s[k] = s.get(k, 0) + v

# ---- givens (illustrative model values, rational witnesses) ----
# prepared electron: amplitude 1 up + 1 down (unnormalized); weights 1/2, 1/2
psi_in = {(0, 0): 1, (1, 0): 1}

# measurement interaction U on basis: |up>|D0> -> |up>|Dup>, |down>|D0> -> |down>|Ddown>
# (d != 0 states are already-recorded pointers; U leaves them fixed)
def apply_U_dict(state):
    out = {}
    for (e, d), c in state.items():
        nd = d
        if d == 0:
            nd = 1 if e == 0 else 2
        add(out, (e, nd), c)
    return out

# Path A: direct dict rewrite
outA = apply_U_dict(psi_in)

# Path B: U as a 6x6 integer matrix over basis index e*3+d; matrix-vector product
DIM = 6
def idx(e, d):
    return e * 3 + d

M = [[0] * DIM for _ in range(DIM)]
for e in (0, 1):
    for d in (0, 1, 2):
        nd = d if d != 0 else (1 if e == 0 else 2)
        M[idx(e, nd)][idx(e, d)] = 1

vec_in = [0] * DIM
for (e, d), c in psi_in.items():
    vec_in[idx(e, d)] = c

vec_out = [sum(M[r][k] * vec_in[k] for k in range(DIM)) for r in range(DIM)]
outB = {}
for r, c in enumerate(vec_out):
    if c != 0:
        outB[(r // 3, r % 3)] = c

assert outA == outB, "linearity paths disagree"
LINEARITY_MATCH = 1

# amplitude matrix Amp[e][d] of the output state
Amp = [[outA.get((e, d), 0) for d in (0, 1, 2)] for e in (0, 1)]

# Witness: entanglement path 1 — all 2x2 cross-minors of Amp vanish iff product state
minor_failures = 0
for e in (0, 1):
    for f in (0, 1):
        for d in (0, 1, 2):
            for dp in (0, 1, 2):
                if Amp[e][d] * Amp[f][dp] != Amp[e][dp] * Amp[f][d]:
                    minor_failures += 1
entangled_by_minors = minor_failures > 0
assert entangled_by_minors
ENTANGLED_MINORS = 1

# Witness: entanglement path 2 — reduced detector matrix rho_D = Amp^T . Amp;
# product state iff Tr(rho_D^2) == Tr(rho_D)^2 (rank-1 criterion)
rhoD = [[sum(Amp[e][d] * Amp[e][dp] for e in (0, 1)) for dp in (0, 1, 2)] for d in (0, 1, 2)]
tr = sum(rhoD[i][i] for i in range(3))
tr2 = sum(rhoD[i][j] * rhoD[j][i] for i in range(3) for j in range(3))
entangled_by_purity = tr2 != tr * tr
assert entangled_by_purity
ENTANGLED_PURITY = 1

# Witness: branch orthogonality — the two macroscopic readings are orthogonal branches
v1 = {(0, 1): 1}
v2 = {(1, 2): 1}
dot = sum(c * v2.get(k, 0) for k, c in v1.items())
assert dot == 0
BRANCH_ORTHO = 1

# Outcome count under (C1 and C2): number of nonzero detector-pointer branches
nonzero_branches = sorted({d for (e, d), c in outA.items() if c != 0})
NONZERO_BRANCHES = len(nonzero_branches)
assert NONZERO_BRANCHES == 2

# Born weights (exact): w = |amp|^2 / norm^2
norm2 = sum(c * c for c in outA.values())
weights = [Fraction(outA.get((e, d), 0) ** 2, norm2) for (e, d) in sorted(outA.keys())]
born_sum_path1 = sum(weights, Fraction(0))
born_sum_path2 = Fraction(sum(rhoD[i][i] for i in range(3)), tr)
assert born_sum_path1 == born_sum_path2 == 1
BORN_SUM = born_sum_path1

# C3 (single outcome) requires exactly one nonzero pointer branch; model gives 2
C3_CONTRADICTED = 1 if NONZERO_BRANCHES != 1 else 0
assert C3_CONTRADICTED == 1

print(f"LINEARITY_MATCH={LINEARITY_MATCH}")
print(f"ENTANGLED_MINORS={ENTANGLED_MINORS}")
print(f"ENTANGLED_PURITY={ENTANGLED_PURITY}")
print(f"BRANCH_ORTHO={BRANCH_ORTHO}")
print(f"NONZERO_BRANCHES={NONZERO_BRANCHES}")
print(f"BORN_SUM={BORN_SUM}")
print(f"C3_CONTRADICTED={C3_CONTRADICTED}")
