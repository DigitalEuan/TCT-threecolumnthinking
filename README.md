# Three Column Thinking — Skill Study: Packaged Repository

This repository packages the complete record of the `three-column-thinking`
(TCT) skill evaluation: the comparative study paper (Runs A–D), the four
independent external case studies with their full audit, the regenerated Run D
artifact bundle, the evaluated skill itself, and every driver script needed to
re-verify the results.

## Contents

```
paper/                     The study paper (16 pp PDF + markdown source)
case_studies/              The four external case studies (the "quartet")
  tct_case_studies.pdf     The recorded case studies + audit (5 pp)
  quartet/                 The four study repositories EXACTLY as shipped:
                           famous-constants-tct, speed-of-light-derivation-tct,
                           physical-isomorphisms-tct, maudlin-measurement-trilemma-tct
                           (produced on aistudio.xiaomimimo.com)
  audit/                   Live audit logs: scripts byte-diff (16/16 identical),
                           Tier-1 re-runs (24/24), 14/14 expected-value spot
                           checks, ledger scans, cent-cost verification, and the
                           three-phase Lean build audit
  repaired/                The minimal-repair Lean copies that compile on pure
                           core 4.35 (Nat/Rat + native_decide + Lake 5 lakefile)
run_d/                     The Run D battery bundle (REGENERATED — see its
                           REGENERATION_NOTES.md): T01–T12 with column3.py,
                           spec.json, built-since Lean projects, decomp pairs;
                           plus RUN_D_SUMMARY.md, optimization_loop.md, results.log
                           (12/12 + 31/31 spot checks), lean_tier.log (12/12 built,
                           56/9/25), and lean_probe/ (15 live environment probes)
skill/SKILL.md             The skill as evaluated in Runs A-D (14 sections), verbatim
skill/SKILL_v3.md          Post-study v3 (probe-first §8 + lean_probe.py, Lake-5
                           scaffold, Reading block, coverage map) — closes the
                           paper's four remaining gaps; verified live
skill/v3_verification.log  Live evidence: v3 scaffold builds as shipped on Lake
                           5.0.0; lean_probe 13/13 baseline agreement
applied/                   USING the outputs: physical-isomorphisms crossovers
  tct_applied_isomorphisms.pdf/.md  the application brief — five workload decisions
                               computed exactly from the study's premises, each with
                               its crossover location and inherited caveat (7 pp)
  tct_substrate_selector.html  the instrument: a self-contained static decision page
                               (exact-integer JS engine, guardrail refusals built in),
                               parity-tested 45/45 against the Python engine
  logs/ + figures/           re-verification, decision and parity evidence
scripts/                   All regeneration/audit driver scripts + paper stylesheet
```

## Headline results

- **Run D** (paper §5.4): 12 questions / 8 domains, classification identity
  105 = 66+9+28+2, Tier 1 12/12 verified with 31/31 spot checks, Tier 2 12/12
  `lake build` (56 proved / 9 sorry / 25 axioms), both refusals machine-checked.
- **The quartet** (paper §5.6, case_studies/): 88 = 49+12+25+2 claims across
  four independent studies; Python tiers reproduce exactly under audit; Lean
  tiers fail to compile as shipped for three documented reasons and compile
  after the named repairs — "proved, not compiled" is endemic.
- **Two kernel catches during regeneration** (honest record): the pure-core
  kernel refuted a wrong cross-multiplied T10 lemma (fixed), and the probes
  refined one paper claim (closed-literal Nat XOR does decide).

## Re-verify (Python 3 stdlib only; Lean optional)

```bash
# Run D Tier 1:
for t in run_d/T??; do python3 <skill-dir>/scripts/verify_column3.py $t/column3.py; done
# Quartet Tier 1:
for d in case_studies/quartet/*/; do (cd $d && for f in scripts/column3/0*.py; \
  do python3 scripts/verify_column3.py $f; done); done
# Lean tiers (lean/lake 4.35 on PATH; run_d projects carry the Lake 5 workaround):
cd run_d/T01/lean_tct && lake build
```

The bundled §13 scripts (`verify_column3.py`, `scaffold_lean_project.py`,
`lean_ledger.py`, `cent_cost.py`) are inside each quartet repository (byte-
identical to the skill's §13) and also embedded in `skill/SKILL.md`.

## Provenance note

The original Run D payload was lost to an environment recycle; `run_d/` is a
regeneration, re-executed live on 2026-11-01 (Lean 4.35.0 / Lake 5.0.0), with
per-test Lean inventories locked to the paper's battery table and every
documented value re-derived. See `run_d/REGENERATION_NOTES.md`.
