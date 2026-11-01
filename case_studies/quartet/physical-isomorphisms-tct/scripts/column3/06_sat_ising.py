#!/usr/bin/env python3
"""Column 3 (TCT) — Hurdle H3: combinatorial optimization — SAT -> Ising mapping, exact.
Physical isomorphism: an Ising machine (spin glass, photonic network, annealer)
realizes E = -sum J_ij s_i s_j - sum h_i s_i as physical energy; ground state =
optimizer (primitives `state_space`, `sat`, `hysteresis`).

Exact check on a fixed instance (no randomness): 3 variables, 2 clauses
  C1 = (x1 OR (NOT x2) OR x3)
  C2 = ((NOT x1) OR x2 OR x3)
Two disjoint derivation paths over all 8 assignments:
  - path A: direct Boolean clause evaluation
  - path B: multilinear energy polynomial  E = sum_c prod_{l in c} (1 - l),
    expanded and evaluated as an exact integer polynomial dict
Claim checked: assignment satisfies both clauses  <=>  E(assignment) = 0.
Also: the expansion contains cubic monomials — a quadratic-only Ising form
needs auxiliary spins (the honest mapping cost; see docs/05-guardrails.md).

UBP: int only; no floats, no random, no SHA-256, stdlib only.
"""

# literals as (var_index, is_negated); var_index in {0,1,2}
CLAUSES = [
    [(0, False), (1, True), (2, False)],   # C1 = x1 | ~x2 | x3
    [(0, True), (1, False), (2, False)],   # C2 = ~x1 | x2 | x3
]

def lit_value(lit, assign):
    x = assign[lit[0]]
    return (1 - x) if lit[1] else x          # 1 = literal true

# path A: Boolean satisfaction
def satisfies(assign):
    return all(any(lit_value(l, assign) for l in c) for c in CLAUSES)

# path B: energy polynomial E = sum_c prod_l (1 - l_value), as multilinear dict
# monomial key = sorted tuple of var indices (with multiplicity-free products);
# evaluation at an assignment from the dict, compared against path A.
def poly_mul(p, q):
    out = {}
    for ka, va in p.items():
        for kb, vb in q.items():
            # merge exponents: x_i * x_i = x_i for {0,1} variables? NO — keep
            # honest polynomial arithmetic over the x variables: exponent sums.
            key = tuple(sorted(ka + kb))
            out[key] = out.get(key, 0) + va * vb
    # reduce x^2 = x (valid on boolean assignments, the only evaluations used)
    reduced = {}
    for key, v in out.items():
        rkey = tuple(sorted(set(key)))
        reduced[rkey] = reduced.get(rkey, 0) + v
    return {k: v for k, v in reduced.items() if v != 0}

def poly_eval(p, assign):
    return sum(v * _monomial(k, assign) for k, v in p.items())

def _monomial(key, assign):
    m = 1
    for i in key:
        m *= assign[i]
    return m

energy_poly = {}
for c in CLAUSES:
    factor = {(): 1}
    for l in c:
        # (1 - l_value):  positive literal: 1 - x_i ;  negated literal: x_i
        lin = {(): 1, (l[0],): -1} if not l[1] else {(l[0],): 1}
        factor = poly_mul(factor, lin)
    for k, v in factor.items():
        energy_poly[k] = energy_poly.get(k, 0) + v
energy_poly = {k: v for k, v in energy_poly.items() if v != 0}

# equivalence over all 8 assignments
equivalence = True
sat_count = 0
energies = []
for bits in range(8):
    assign = ((bits >> 0) & 1, (bits >> 1) & 1, (bits >> 2) & 1)
    e_bool = 0 if satisfies(assign) else 1
    e_poly = poly_eval(energy_poly, assign)
    equivalence = equivalence and (e_bool == e_poly)
    energies.append(e_poly)
    if satisfies(assign):
        sat_count += 1
assert equivalence
EQUIVALENCE = 1

SAT_COUNT = sat_count
assert SAT_COUNT == 6                       # C1 fails only at (0,1,0); C2 only at (1,0,0)

E_MIN = min(energies)
assert E_MIN == 0

# polynomial degree: cubic monomials present => quadratic Ising needs gadgets
max_deg = max(len(k) for k in energy_poly)
CUBIC_TERMS_PRESENT = 1 if max_deg == 3 else 0
assert CUBIC_TERMS_PRESENT == 1

TERMS_EXPANDED = len(energy_poly)
# mapping cost sanity: 2 clauses x 8 monomial slots (before like-term merging)
MAPPING_SLOTS = 2 * 8
assert TERMS_EXPANDED <= MAPPING_SLOTS

print(f"EQUIVALENCE={EQUIVALENCE}")
print(f"SAT_COUNT={SAT_COUNT}")
print(f"E_MIN={E_MIN}")
print(f"CUBIC_TERMS_PRESENT={CUBIC_TERMS_PRESENT}")
print(f"TERMS_EXPANDED={TERMS_EXPANDED}")
print(f"MAPPING_SLOTS={MAPPING_SLOTS}")
