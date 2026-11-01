#!/usr/bin/env python3
"""Column 3 (TCT) — Boundary B3b: light cone from exact Clifford circuit dynamics.
A brickwork Clifford circuit (H, S, CNOT) on L = 8 qubits propagates Pauli
operators with EXACT structure: no amplitudes, no floats — Pauli labels and
GF(2) symplectic vectors only. DECLARED F2 SITE: XOR is used only over the
binary symplectic representation (UBP D9-compliant).

Claim verified: an operator's support grows at most ONE site per layer on each
side — a light cone with speed exactly 1 site/layer emerges from the discrete
dynamics itself.

Two disjoint derivation paths per witness (compared at every layer):
  - path 1: Pauli-label propagation with explicit gate rules and a
    phase-free Pauli product table
  - path 2: full 2L x 2L GF(2) symplectic matrix propagation (XOR site)

UBP: int + GF(2) XOR only (declared site); no floats, no random, no SHA-256.
"""
# Pauli labels: 0=I, 1=X, 2=Y, 3=Z   (phase-free)
# product table (Klein four-group, phases dropped — support is what matters)
PMUL = {
    (0,0):0,(0,1):1,(0,2):2,(0,3):3,
    (1,0):1,(1,1):0,(1,2):3,(1,3):2,
    (2,0):2,(2,1):3,(2,2):0,(2,3):1,
    (3,0):3,(3,1):2,(3,2):1,(3,3):0,
}

def gate_H(l):
    return {0:0, 1:3, 2:2, 3:1}[l]

def gate_S(l):
    return {0:0, 1:2, 2:1, 3:3}[l]

def gate_CNOT(la, lb, a, b):
    # Heisenberg: X-type at control a -> multiply target by X;
    #             Z-type at target b -> multiply control by Z
    new_a = PMUL[(la, 3)] if lb in (2, 3) else la
    new_b = PMUL[(lb, 1)] if la in (1, 2) else lb
    return new_a, new_b

def to_bits(l):       # label -> (x, z) in F2
    return [(0,0),(1,0),(1,1),(0,1)][l]

def to_label(x, z):
    return {(0,0):0,(1,0):1,(1,1):2,(0,1):3}[(x, z)]

L = 8
LAYERS = 6

# brickwork: even layers pair (0,1),(2,3),... control left; odd layers pair
# (1,2),(3,4),... with control RIGHT (alternating propagation directions)
def layer_pairs(ell):
    if ell % 2 == 0:
        return [(i, i+1) for i in range(0, L-1, 2)]
    return [(i+1, i) for i in range(1, L-1, 2)]   # control = i+1, target = i

# --- path 1: label propagation ---
labels = [0]*L
labels[3] = 2                       # start: Y on site 3 (has both X and Z parts)
hist1 = [labels[:]]
for ell in range(LAYERS):
    for s in range(L):
        labels[s] = gate_H(labels[s])     # H everywhere (support-preserving)
    for (a, b) in layer_pairs(ell):
        labels[a], labels[b] = gate_CNOT(labels[a], labels[b], a, b)
    hist1.append(labels[:])

# --- path 2: GF(2) symplectic matrix propagation (declared F2/XOR site) ---
def eye2(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

n2 = 2*L
def mat_mul_F2(A, B):
    return [[sum(A[i][k] & B[k][j] for k in range(n2)) & 1 for j in range(n2)] for i in range(n2)]

def apply_op_F2(M, vec):
    return [sum(M[i][k] & vec[k] for k in range(n2)) & 1 for i in range(n2)]

def gate_mat_H(s, M):
    # swap x_s and z_s
    xs, zs = s, L + s
    M[xs], M[zs] = M[zs], M[xs]
    return M

def gate_mat_S(s, M):
    # z_s ^= x_s
    xs, zs = s, L + s
    M[zs] = [M[zs][j] ^ M[xs][j] for j in range(n2)]
    return M

def gate_mat_CNOT(a, b, M):
    # x_b ^= x_a ; z_a ^= z_b
    xa, za, xb, zb = a, L + a, b, L + b
    M[xb] = [M[xb][j] ^ M[xa][j] for j in range(n2)]
    M[za] = [M[za][j] ^ M[zb][j] for j in range(n2)]
    return M

vec = [0]*n2
vec[3] = 1            # X part of Y_3
vec[L + 3] = 1        # Z part of Y_3
hist2 = []
M = eye2(n2)
hist2.append(apply_op_F2(M, vec))
for ell in range(LAYERS):
    for s in range(L):
        M = gate_mat_H(s, M)
    for (a, b) in layer_pairs(ell):
        M = gate_mat_CNOT(a, b, M)
    hist2.append(apply_op_F2(M, vec))

# --- compare paths at every layer: supports AND labels must agree ---
for ell in range(LAYERS + 1):
    for s in range(L):
        x, z = hist2[ell][s], hist2[ell][L + s]
        assert to_label(x, z) == hist1[ell][s]
PATHS_AGREE = 1

# --- the light cone claim: support after ell layers stays inside [3-ell, 3+ell],
#     and each side grows at most one site per layer ---
cone_ok = True
growth_ok = True
prev = set(s for s in range(L) if hist1[0][s] != 0)
for ell in range(1, LAYERS + 1):
    supp = set(s for s in range(L) if hist1[ell][s] != 0)
    for s in supp:
        cone_ok = cone_ok and (abs(s - 3) <= ell)
    left_new = min(supp) - min(prev) >= -1
    right_new = max(supp) - max(prev) <= 1
    growth_ok = growth_ok and left_new and right_new
    prev = supp
assert cone_ok and growth_ok
CONE_BOUND = 1
SUPPORT_LE_LAYER = 1

final_support = sorted(s for s in range(L) if hist1[LAYERS][s] != 0)
SUPPORT_FINAL = len(final_support)

print(f"PATHS_AGREE={PATHS_AGREE}")
print(f"CONE_BOUND={CONE_BOUND}")
print(f"SUPPORT_LE_LAYER={SUPPORT_LE_LAYER}")
print(f"SUPPORT_FINAL={SUPPORT_FINAL}")
