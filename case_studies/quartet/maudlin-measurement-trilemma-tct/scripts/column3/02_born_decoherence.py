#!/usr/bin/env python3
"""Column 3 (TCT) — Born-rule and decoherence bookkeeping over Q (step re-derivation).

Steps re-derived: the post-measurement state's squared amplitudes give weights
1/2, 1/2; the detector's reduced state is diagonal (pointer states are
orthogonal, so off-diagonal coherences vanish); the reduced state is mixed
(purity 1/2), which is exactly the "both readings present, neither definite"
content of (C1 and C2) — while each branch considered alone is pure.

Two disjoint derivation paths per witness:
  - reduced detector matrix: trace of the full 6x6 density matrix vs. direct
    sum over the electron index
  - normalization: sum of squared amplitudes vs. trace of the reduced matrix
  - coherence vanishing: explicit off-diagonal sum vs. branch-disjoint support test

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

# givens (illustrative, carried exactly): post-measurement state
# basis index e*3+d; amplitudes: (e=0,d=1) -> 1  [up + detector reads up],
# (e=1,d=2) -> 1 [down + detector reads down]
psi = {(0, 1): 1, (1, 2): 1}
E, D = 2, 3

# full density matrix rho[(e,d),(e',d')] = psi psi^T (integer outer product)
def rho_full(a, b):
    return psi.get(a, 0) * psi.get(b, 0)

# Path 1: reduced detector matrix by tracing out the electron from rho_full
rhoD_p1 = [[sum(rho_full((e, d), (e, dp)) for e in range(E)) for dp in range(D)] for d in range(D)]

# Path 2: reduced detector matrix directly as sum_e psi(e,d) psi(e,dp)
rhoD_p2 = [[sum(psi.get((e, d), 0) * psi.get((e, dp), 0) for e in range(E)) for dp in range(D)] for d in range(D)]

assert rhoD_p1 == rhoD_p2
REDUCED_AGREE = 1

norm2 = sum(c * c for c in psi.values())
rho_hat = [[Fraction(rhoD_p1[i][j], norm2) for j in range(D)] for i in range(D)]

# normalization cross-check: sum of squared amplitudes vs. trace of reduced matrix
norm_path1 = sum(Fraction(c * c, norm2) for c in psi.values())
norm_path2 = sum(rho_hat[i][i] for i in range(D))
assert norm_path1 == norm_path2 == 1
NORMALIZATION = norm_path1

# coherence vanishing: off-diagonal entries of rho_hat
# path 1: explicit evaluation
offdiag = sum(abs(rho_hat[i][j]) for i in range(D) for j in range(D) if i != j)
# path 2: branch-disjoint support — the two branches never share a detector index,
# so every off-diagonal summand has a zero factor
support_products_zero = all(
    psi.get((e, i), 0) * psi.get((e, j), 0) == 0
    for e in range(E) for i in range(D) for j in range(D) if i != j
)
assert offdiag == 0 and support_products_zero
OFFDIAG_ZERO = 1

# purity of reduced state: Tr(rho_hat^2); pure iff = 1
purity = sum(rho_hat[i][j] * rho_hat[j][i] for i in range(D) for j in range(D))
assert purity == Fraction(1, 2)
PURITY = purity

# each branch alone is pure (single basis ket): weight 1/2 each
branch_weights = sorted((Fraction(c * c, norm2) for c in psi.values()))
assert branch_weights == [Fraction(1, 2), Fraction(1, 2)]
BRANCH_WEIGHTS = "1/2,1/2"

print(f"REDUCED_AGREE={REDUCED_AGREE}")
print(f"NORMALIZATION={NORMALIZATION}")
print(f"OFFDIAG_ZERO={OFFDIAG_ZERO}")
print(f"PURITY={PURITY}")
print(f"BRANCH_WEIGHTS={BRANCH_WEIGHTS}")
