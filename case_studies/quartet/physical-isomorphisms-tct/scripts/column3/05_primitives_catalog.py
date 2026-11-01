#!/usr/bin/env python3
"""Column 3 (TCT) — cent catalog: the 22-primitive vocabulary x 8 physical domains.
Each row: (primitive, domain, license) — 'licensed' = established engineering
practice in that domain (axiom-class); 'conjectural' = plausible mapping, not
established (sorry-class, per TCT §12).

Checks (this is the license condition of §12 made executable):
  - every primitive named is in the 22-word vocabulary
  - every primitive used is realizable in >= 2 domains
  - license counts are reported (licensed vs conjectural)

UBP: int only; no floats, no random, no SHA-256, stdlib only.
"""
ATOMIC = {"sum","neg","mult","scale","accum","rate","wrap","spatial","exp","log",
          "sat","hysteresis","grad","div_spatial","curl","delay"}
COMPOSITE = {"recip","div","sqrt","eq","translinear","state_space"}
VOCAB = ATOMIC | COMPOSITE

DOMAINS = {"electrical","mechanical","fluidic","thermal","optical","digital",
           "spintronic","biochemical"}

CATALOG = [
    # (primitive, domain, license) — the study's cross-domain isomorphism table
    ("sum",         "electrical",  "licensed"),     # Kirchhoff: currents sum at a node
    ("sum",         "fluidic",     "licensed"),     # flows merge at a junction
    ("sum",         "digital",     "licensed"),     # adder tree
    ("mult",        "electrical",  "licensed"),     # translinear loop / Gilbert cell
    ("mult",        "mechanical",  "licensed"),     # gear / differential
    ("mult",        "digital",     "licensed"),     # multiplier array
    ("mult",        "spintronic",  "conjectural"),  # torque-product mapping
    ("rate",        "electrical",  "licensed"),     # VCO: voltage -> frequency
    ("rate",        "spintronic",  "licensed"),     # spin-torque oscillator
    ("rate",        "digital",     "licensed"),     # clock divider
    ("sat",         "electrical",  "licensed"),     # amplifier limiter
    ("sat",         "mechanical",  "licensed"),     # clutch / hard stop
    ("sat",         "digital",     "licensed"),     # clamp / saturation logic
    ("hysteresis",  "electrical",  "licensed"),     # Schmitt trigger / latch
    ("hysteresis",  "mechanical",  "licensed"),     # snap-action mechanism
    ("hysteresis",  "spintronic",  "licensed"),     # magnetic hysteresis
    ("hysteresis",  "biochemical", "licensed"),     # bistable genetic switch
    ("spatial",     "optical",     "licensed"),     # beam propagation field
    ("spatial",     "fluidic",     "licensed"),     # channel pressure field
    ("spatial",     "digital",     "licensed"),     # memory array addressing
    ("exp",         "electrical",  "licensed"),     # diode I-V / subthreshold
    ("exp",         "thermal",     "licensed"),     # Arrhenius rate
    ("exp",         "biochemical", "licensed"),     # rate laws
    ("log",         "electrical",  "licensed"),     # log amplifier
    ("log",         "biochemical", "licensed"),     # pH scale
    ("log",         "digital",     "conjectural"),  # LUT approximation
    ("delay",       "electrical",  "licensed"),     # transmission line
    ("delay",       "fluidic",     "licensed"),     # pipe transport delay
    ("delay",       "digital",     "licensed"),     # pipeline register
    ("state_space", "electrical",  "licensed"),     # analog computer
    ("state_space", "mechanical",  "licensed"),     # spring-mass network
    ("state_space", "fluidic",     "licensed"),     # lumped-circuit fluid analogy
    ("state_space", "thermal",     "licensed"),     # RC thermal network
    ("state_space", "optical",     "conjectural"),  # cavity-mode state space
    ("state_space", "digital",     "licensed"),     # numerical simulator
    ("eq",          "digital",     "licensed"),     # comparator
    ("eq",          "electrical",  "licensed"),     # Wheatstone bridge null
    ("accum",       "electrical",  "licensed"),     # integrating capacitor
    ("accum",       "mechanical",  "licensed"),     # odometer gear train
    ("accum",       "digital",     "licensed"),     # accumulator register
]

# vocabulary validity
for p, d, lic in CATALOG:
    assert p in VOCAB, f"unknown primitive {p}"
    assert d in DOMAINS, f"unknown domain {d}"
    assert lic in ("licensed", "conjectural")
VOCAB_VALID = 1

# coverage: each primitive used has >= 2 domain realizations (license condition)
from collections import defaultdict
domains_by_prim = defaultdict(set)
for p, d, lic in CATALOG:
    domains_by_prim[p].add(d)
counts = {p: len(ds) for p, ds in domains_by_prim.items()}
min_domains = min(counts.values())
assert min_domains >= 2
MIN_DOMAINS = min_domains

PRIMITIVES_USED = len(domains_by_prim)
assert PRIMITIVES_USED == 12

REALIZATIONS_TOTAL = len(CATALOG)
LICENSED = sum(1 for _, _, l in CATALOG if l == "licensed")
CONJECTURAL = sum(1 for _, _, l in CATALOG if l == "conjectural")
assert LICENSED + CONJECTURAL == REALIZATIONS_TOTAL
assert CONJECTURAL == 3

print(f"VOCAB_VALID={VOCAB_VALID}")
print(f"PRIMITIVES_USED={PRIMITIVES_USED}")
print(f"REALIZATIONS_TOTAL={REALIZATIONS_TOTAL}")
print(f"LICENSED={LICENSED}")
print(f"CONJECTURAL={CONJECTURAL}")
print(f"MIN_DOMAINS={MIN_DOMAINS}")
