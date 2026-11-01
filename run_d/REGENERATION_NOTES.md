# REGENERATION NOTES — provenance of this bundle

## What happened

Run D was originally executed on 2026-11-01 (dola.com's AI system) with the
updated 14-section skill; its results are documented in the companion paper
(§5.4). The original artifact payload (including the per-question
`payload.md` three-column answers and the original `column3.py` sources) was
lost to an environment recycle, twice. This bundle was regenerated on
2026-11-01 from the paper's documented results and re-verified live in a
fresh environment (Lean 4.35.0, Lake 5.0.0).

## What is regenerated vs live

- **Regenerated from documentation** (faithful to the paper's numbers, but
  new code): the 12 `spec.json` files (lemma statements, sorry/axiom
  inventory — per-test counts locked to the paper's battery table,
  56/9/25 total); the 12 `column3.py` scripts (re-deriving every documented
  exact value); the decomp pairs and `optimization_loop.md` (from the
  documented loop outcome: 7 accepted, 5 floors, 6 tautologies).
- **Live-executed in this run**: all 12 column3 scripts (Tier 1), all 12
  Lean scaffolds + builds (Tier 2), the 31 spot checks, the 15 environment
  probes, and the loop cost re-computation. Every log in this directory is
  from this run.
- **Not recoverable**: the original per-question `payload.md` files (the
  full §6-format three-column answers) and the original column3.py sources.
  The paper's §5.4/§6.8–6.11 carry the analytical content.

## Fidelity checks (all passed in this run)

- Classification identity, Python tier: per-test n=p+s+a+r sums to
  105 = 66+9+28+2 (paper's totals).
- Lean tier: 12/12 build OK; ledger totals exactly 56 proved / 9 sorry /
  25 axioms; per-test counts match the battery table exactly.
- Tier 1: 12/12 VERIFIED in isolated subprocesses; 31/31 spot checks,
  including every value the paper names (h₃ = 3645/8192 m, 125/14 m, 5 s,
  t/v/h = 5/7, 7, 5/2, 2750/2997, 9261/80, 32/30/31 witnesses, 267/85,
  bracket 314103–314271×10⁻⁵, both refusals).
- Probes: 14/15 AGREE with the paper's documented findings; 1 boundary
  refinement recorded honestly (p12: closed-literal Nat XOR decides fine on
  this build; variable-based xor goals do not).

## Two kernel catches in this regeneration (same class as the original)

1. T10's lower-bound lemma was first written `314103 * 71 = 223 * 100000 +
   813` — the pure-core kernel refuted it (the correct identity has +1313;
   314103·71 = 22,301,313). Fixed and rebuilt. The original run's
   analogous catch was the bounce lemma (729·2·4096 = 3645·512·256 →
   729·5·8192 = 3645·4096·2).
2. The as-shipped scaffold lakefile still fails under Lake 5.0 (probe p15);
   all 12 projects here carry the named workaround
   (`globs := #[.one `TCT.Basic]`), as in the original run.
