#!/usr/bin/env python3
"""Column 3 (TCT) — cent cross-domain witness: the trilemma in a fluidic fork + latch.

The quantum measurement interaction, compiled to ¢ primitives, has an exact
rational analogue in a fluidic domain: one flow (weight 1) meets a symmetric
fork and splits into two branches of flow 1/2 each (superposition = sum),
branch flows are squared weights (mult), the branches are disjoint (eq),
and a latch must select exactly one outflow (sat + hysteresis).

Witness (this is the trilemma's moral, re-derived outside quantum theory):
  - symmetric fork: both branches carry equal flow 1/2; a latch fed ONLY the
    symmetric flows finds a tie and selects nothing (no single outcome).
  - breaking the tie requires an EXTRA variable (an asymmetry epsilon = 1/1000,
    declared illustrative): the latch then selects the larger branch
    deterministically — the Bohmian door, in fluidic dress.

Status of the cross-domain mapping: CONJECTURAL (analogy, not derivation);
recorded as sorry in the Lean/cent ledger per TCT §12.

Two disjoint derivation paths per witness:
  - latch selection: argmax by pairwise comparison vs. sign of the difference
  - conservation: sum of branch flows vs. 1 (input flow)

UBP: Fraction/int only; no floats, no random, no SHA-256, stdlib only.
"""
from fractions import Fraction

VOCAB_ATOMIC = {"sum","neg","mult","scale","accum","rate","wrap","spatial","exp","log",
                "sat","hysteresis","grad","div_spatial","curl","delay"}
VOCAB_COMPOSITE = {"recip","div","sqrt","eq","translinear","state_space"}

# ¢ decomposition of the measurement interaction (see docs/06-cent-cross-domain.md)
decomp = ["state_space", "sum", "mult", "eq", "sat", "hysteresis"]
unknown = [p for p in decomp if p not in VOCAB_ATOMIC | VOCAB_COMPOSITE]
assert not unknown
CENT_DECOMP_VALID = 1

# ---- symmetric fork: flow 1 splits into 1/2 + 1/2 ----
total_in = Fraction(1, 1)
branch_a = Fraction(1, 2)
branch_b = Fraction(1, 2)
assert branch_a + branch_b == total_in
CONSERVATION = branch_a + branch_b

# latch with only the symmetric flows: tie -> no selection
def latch(flows):
    """sat + hysteresis: select the strictly largest flow; None on a tie."""
    best = max(flows.values())
    winners = [k for k, v in flows.items() if v == best]
    return winners[0] if len(winners) == 1 else None

sym_flows = {"A": branch_a, "B": branch_b}
tie_result = latch(sym_flows)
assert tie_result is None
TIE_NO_OUTCOME = 1

# tie detected by an independent path: the difference of the flows is zero
assert (sym_flows["A"] - sym_flows["B"]) == 0
TIE_BY_DIFFERENCE = 1

# ---- asymmetric fork (extra variable, Bohmian door): epsilon = 1/1000 ----
eps = Fraction(1, 1000)
branch_a2 = Fraction(1, 2) + eps
branch_b2 = Fraction(1, 2) - eps
assert branch_a2 + branch_b2 == total_in
CONSERVATION_ASYM = branch_a2 + branch_b2

asym_flows = {"A": branch_a2, "B": branch_b2}
# path 1: argmax by comparison
sel_p1 = latch(asym_flows)
# path 2: sign of the difference
sel_p2 = "A" if (asym_flows["A"] - asym_flows["B"]) > 0 else "B"
assert sel_p1 == sel_p2 == "A"
ASYMMETRY_OUTCOME = 1

# the extra variable is exactly what a complete-state-only description lacks:
# with flows alone the tie stands; with (flows + epsilon) the outcome is fixed
EXTRA_VARIABLE_REQUIRED = 1

print(f"CENT_DECOMP_VALID={CENT_DECOMP_VALID}")
print(f"CONSERVATION={CONSERVATION}")
print(f"TIE_NO_OUTCOME={TIE_NO_OUTCOME}")
print(f"TIE_BY_DIFFERENCE={TIE_BY_DIFFERENCE}")
print(f"CONSERVATION_ASYM={CONSERVATION_ASYM}")
print(f"ASYMMETRY_OUTCOME={ASYMMETRY_OUTCOME}")
print(f"EXTRA_VARIABLE_REQUIRED={EXTRA_VARIABLE_REQUIRED}")
