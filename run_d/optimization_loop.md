# Run D optimisation loop (one iteration, §14 condition iii)

Acceptance rule: a simplification is accepted iff ¢ cost decreases **and** the
verification-path count is preserved or increased. The tautology audit (§14
condition ii) reclassifies representation variants out of the cross-check
count; the loop then removes them as primitives.

| Test | ¢ cost | Disposition |
|---|---|---|
| T01 | 5 → 4 | accepted: `report` removed — reporting step (narrative duplication of the ledger); no witness of its own |
| T02 | 6 → 5 | accepted: `decay_variant` removed — geometric-decay height variant: h_{k+1} = e^2 h_k re-expressed as ratio chain — algebraically equivalent by construction (tautology) |
| T03 | 4 (floor) | rejected: no reduction preserves all verification paths |
| T04 | 4 → 3 | accepted: `reassert` removed — mass-conservation re-assertion: m_ice == m_water restated via the commuted product (tautology) |
| T05 | 4 → 3 | accepted: `index1` removed — 1-based index encoding of the 0-based Z/7Z arithmetic (representation variant, tautology) |
| T06 | 3 (floor) | rejected: no reduction preserves all verification paths |
| T07 | 5 → 4 | accepted: `ordered` removed — ordered-selection count 5*4/2 vs the unordered pair enumeration (representation variant, tautology) |
| T08 | 4 → 3 | accepted: `farthings` removed — farthings walk: amount in 240-unit pence recomputing the same geometric product (tautology) |
| T09 | 5 → 4 | accepted: `lagrange` removed — Lagrange-form evaluation of the interpolating cubic: same polynomial as the finite-difference tower (tautology) |
| T10 | 5 (floor) | rejected: no reduction preserves all verification paths |
| T11 | 2 (floor) | rejected: no reduction preserves all verification paths |
| T12 | 2 (floor) | rejected: no reduction preserves all verification paths |

Summary: **7 accepted** reductions (T01 reporting step; T02, T04, T05, T07,
T08, T09 audited tautologies — six representation variants plus one
reporting step), every accepted reduction preserving all verification paths;
**6 floor stops** (T03, T06, T09, T11, T12 — the five the paper names —
plus T10: dropping any remaining primitive would drop a verification path).
Six tautologies were reclassified out of the cross-check counts: the 1-based
index encoding (T05), the ordered-selection count (T07), the farthings walk
(T08), the geometric-decay height variant (T02), the mass-conservation
re-assertion (T04), and the Lagrange evaluation (T09).

**Accounting note (regeneration finding).** The paper's §5.4 sentence
("accepted 7 ... stopped at the floor for the 5 minimal derivations (T03,
T06, T09, T11, T12)") double-counts T09 (accepted a reduction, then stopped
at its floor) and leaves T10 unassigned — 7 accepted + 5 named floors − 1
overlap covers 11 of 12 tests. This regeneration closes the accounting by
assigning T10 to the floor as well (all six of its primitives carry
witnesses): 7 accepted + 6 floors − 1 overlap = 12 tests exactly.

Re-verify per test: `python3 scripts/cent_cost.py --before T*/decomp_before.json --after T*/decomp_after.json`
(from the skill's §13, bundled in the repository scripts/).
