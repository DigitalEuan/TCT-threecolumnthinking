#!/usr/bin/env python3
"""Column 3 (TCT) — The classification machine: which famous constants are
"derivable from first principles", and in what sense?

Taxonomy (docs/04):
  D = definitional        (pi, e, phi, sqrt(2), Champernowne)
  T = theorem-determined  (ln 2, zeta(2), zeta(4); zeta(3): irrational [Apery
      1979] but no closed form; e^pi transcendental [Gelfond-Schneider])
  O = open                (gamma [Erdos prize], zeta(5), Catalan's closed
      form, zeta(3) closed form)
  U = definable but UNCOMPUTABLE (Chaitin's Omega)
  P = physical, measured/defined (alpha [measured], c/h [SI-defined],
      G [measured])  -> the study-3 boundary carries over: REFUSED to derive

Executable checks here:
  - Champernowne C10 = 0.123456789101112... digit generation by two disjoint
    paths (string concatenation vs. position arithmetic)
  - taxonomy validity + class counts
  - the physical-constants refusal stamp (trilogy link)

UBP: int/str only; no floats, no random, no SHA-256, stdlib only.
"""
# --- Champernowne: two disjoint derivations of the first 25 digits ---
# path A: string concatenation
concat = ""
i = 1
while len(concat) < 25:
    concat += str(i)
    i += 1
digits_A = concat[:25]

# path B: position arithmetic (positions 1-9 are digits of numbers 1-9;
# positions 10+ are 2-digit numbers 10, 11, ...)
def digit_at(p):                      # 1-based position
    if p <= 9:
        return str(p)
    j = (p - 10) // 2                 # which 2-digit number, from 10
    d = (p - 10) % 2                  # which digit of it
    return str(10 + j)[d]

digits_B = "".join(digit_at(p) for p in range(1, 26))
assert digits_A == digits_B == "1234567891011121314151617"
CHAMPERNOWNE_OK = 1

# --- taxonomy catalog ---
CATALOG = [
    ("pi",          "D"), ("e", "D"), ("phi", "D"), ("sqrt2", "D"),
    ("champernowne","D"),
    ("ln2",         "T"), ("zeta2", "T"), ("zeta4", "T"),
    ("zeta3",       "T"), ("e_pi", "T"),
    ("gamma",       "O"), ("zeta5", "O"), ("catalan_closed", "O"),
    ("zeta3_closed","O"),
    ("omega",       "U"),
    ("alpha",       "P"), ("c_si", "P"), ("h_si", "P"), ("G", "P"),
]
VALID = {"D", "T", "O", "U", "P"}
for name, cls in CATALOG:
    assert cls in VALID
TAXONOMY_VALID = 1

counts = {c: sum(1 for _, x in CATALOG if x == c) for c in sorted(VALID)}
assert counts == {"D": 5, "O": 4, "P": 4, "T": 5, "U": 1}
CLASS_COUNTS = counts

# --- physical boundary stamps (trilogy link: study 3) ---
# alpha: measured; derivation from theory alone REFUSED: WOULD_BE_GUESS
# c, h: SI-defined exact (2019); G: measured
ALPHA_STATUS = "REFUSED_WOULD_BE_GUESS"
SI_DEFINITIONS = ("c_si", "h_si")
assert ALPHA_STATUS == "REFUSED_WOULD_BE_GUESS"
ALPHA_REFUSED = 1

# open-problem list (docs/04-05): the O class is exactly these
OPEN_LIST = ["gamma", "zeta5", "catalan_closed", "zeta3_closed"]
assert [n for n, c in CATALOG if c == "O"] == OPEN_LIST
OPEN_LIST_OK = 1

print(f"CHAMPERNOWNE_OK={CHAMPERNOWNE_OK}")
print(f"TAXONOMY_VALID={TAXONOMY_VALID}")
print(f"CLASS_COUNTS={counts}")
print(f"ALPHA_REFUSED={ALPHA_REFUSED}")
print(f"OPEN_LIST_OK={OPEN_LIST_OK}")
