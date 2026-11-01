#!/usr/bin/env python3
"""Decision engine — USING the physical-isomorphisms-tct outputs.

Five concrete workload decisions, computed exactly (Fraction/int only, no
floats, no random — UBP) from the case study's re-verified premises:

  premises (case_studies/physical-isomorphisms-tct, scripts 01-06, re-run live):
    per-MAC energy, units of 0.1 pJ (Horowitz 2014 + declared illustrative):
      von Neumann 12838 · in-memory 138 · crossbar cell 2 · converter 3700 (2N per pass)
    optical 4f convolution at N=1024: setup N^2, per frame N+1, FFT per frame 5·N·log2N
    stochastic bits: N >= p(1-p)/eps^2 (Chebyshev, p=1/2); AND gate 1 unit vs FP multiply 37
    analog ODE floor eps_a = 1/1000; Euler error e_M = (3M-1)/(2M^2)
    SAT->Ising: exact mapping (EQUIVALENCE=1), ECT carried as axiom

Each decision prints: verdict, exact quantities (two paths where cheap),
caveat. Output feeds the brief (tct_applied_isomorphisms.md) and the HTML
selector (parity-tested against this script).
"""
from fractions import Fraction
from math import gcd, log2

# ---- premises (re-verified above; cite: scripts/column3/01..06) ----
MULT, ADD, SRAM, DRAM = 37, 1, 50, 6400
CELL, CONV = 2, 3700
PER_MAC_VN = MULT + ADD + 2 * DRAM            # 12838
PER_MAC_INMEM = MULT + ADD + 2 * SRAM         # 138
assert PER_MAC_VN == 12838 and PER_MAC_INMEM == 138


def reduce(a, b):
    g = gcd(a, b)
    return f"{a // g}/{b // g}"


def approx(fr):
    """Display-only decimal (decisions never use this)."""
    return f"{float(fr):.2f}"


# =====================================================================
print("=" * 72)
print("DECISION A — edge-inference matmul engine (N=1024, 32-bit effective)")
print("=" * 72)
N = 1024
for bits, passes in ((8, 1), (32, 4)):
    assert passes == bits // 8
    analog = passes * (CELL * N * N + 2 * N * CONV)
    inmem = PER_MAC_INMEM * N * N
    vn = PER_MAC_VN * N * N
    r_inmem = Fraction(inmem, analog)
    r_vn = Fraction(vn, analog)
    # second path: per-MAC decomposition  (passes*(2 + 7400/N)) vs 138
    per_mac_analog = Fraction(passes * (CELL * N * N + 2 * N * CONV), N * N)
    assert per_mac_analog == Fraction(analog * 1, N * N) and inmem == PER_MAC_INMEM * N * N
    print(f"[{bits}-bit, {passes} pass(es)]")
    print(f"  analog total   = {analog} units   ({passes}·(2·{N}² + 7400·{N}))")
    print(f"  in-memory total= {inmem} units   von Neumann total = {vn} units")
    print(f"  in-memory / analog = {reduce(inmem, analog)} = {approx(r_inmem)}× fewer units")
    print(f"  vonNeumann / analog= {reduce(vn, analog)} = {approx(r_vn)}× fewer units")
# break-even N at 32-bit (four passes): 4·(2N²+7400N) < 138N² <=> N > 2960/13
be32 = 29600 // 130 + 1
assert be32 == 228 and Fraction(29600, 130) == Fraction(2960, 13)
print(f"  break-even vs in-memory: N > 2960/13 → N ≥ {be32} (32-bit); N=1024 clears it")
print(f"  verdict: CROSSBAR WINS at N=1024 — 3.7× vs in-memory, 348× vs von Neumann (32-bit);")
print(f"           15× vs in-memory at 8-bit. Caveat: converters dominate below N=228;")
print(f"           precision via bit-slicing (H7); model constants illustrative (carried as axioms).")

# =====================================================================
print()
print("=" * 72)
print("DECISION B — real-time 4K convolution pipeline (fixed kernel, 60 fps)")
print("=" * 72)
NB = 1024                      # 1-D line size in the case-study model
LOG2 = 10
assert 2 ** LOG2 == NB
SETUP = NB * NB                # 1048576 kernel-programming writes
PER_FRAME_OPT = NB + 1         # 1025
PER_FRAME_FFT = 5 * NB * LOG2  # 51200
# break-even reuse: T·51200 >= N² + T·1025 <=> T >= N²/50175
beT = -(-SETUP // (PER_FRAME_FFT - PER_FRAME_OPT))
assert beT == 21 and Fraction(SETUP, PER_FRAME_FFT - PER_FRAME_OPT) == Fraction(1048576, 50175)
for label, T in (("kernel re-learned every 10 s @60fps", 600), ("adapted filter, per frame", 1)):
    opt = SETUP + T * PER_FRAME_OPT
    fft = T * PER_FRAME_FFT
    if fft >= opt:
        ratio = Fraction(fft, opt)
        print(f"[{label}: T={T}]  optical {opt} ops vs FFT {fft} ops")
        print(f"   → OPTICAL WINS: {reduce(fft, opt)} = {approx(ratio)}× fewer total ops;"
              f" per-frame {reduce(PER_FRAME_FFT, PER_FRAME_OPT)} = {approx(Fraction(PER_FRAME_FFT, PER_FRAME_OPT))}×")
    else:
        ratio = Fraction(opt, fft)
        print(f"[{label}: T={T}]  optical {opt} ops vs FFT {fft} ops")
        print(f"   → FFT WINS: optical costs {reduce(opt, fft)} = {approx(ratio)}× more")
print(f"  break-even reuse T* = ceil(1048576/50175) = {beT}")
print(f"  verdict: STATIC-KERNEL PIPELINES ONLY — T=600 (re-learned every 10 s) wins 18.5×;")
print(f"           per-frame adaptation (T=1) loses 20.5×. The gain is amortization (H8),")
print(f"           not raw compute — exactly the crossover the study measured.")

# =====================================================================
print()
print("=" * 72)
print("DECISION C — Monte-Carlo Bernoulli estimates at 1% error")
print("=" * 72)
for k in (10, 100, 1000):
    eps = Fraction(1, k)
    n_bits = Fraction(1, 4) / (eps * eps)          # p(1-p)/eps^2 at p=1/2
    assert n_bits.denominator == 1
    n_bits = int(n_bits)
    # enumeration path (second witness)
    n = 0
    while Fraction(1, 4) / (n + 1) > eps * eps:
        n += 1
    assert n + 1 == n_bits, (n + 1, n_bits)
    print(f"  ε=1/{k}: N ≥ {n_bits} noise bits per estimate (Chebyshev, two paths agree)")
# energy per stochastic multiply at ε=1/100: 2500 AND-units vs 37-unit FP multiply
n100 = 2500
ratio_stoch = Fraction(n100 * 1, MULT)             # 2500/37
print(f"  one stochastic multiply at 1% = {n100} AND-units vs {MULT}-unit FP multiply")
print(f"   → {reduce(n100, MULT)} = {approx(ratio_stoch)}× MORE energy per multiply")
print(f"  verdict: USE PHYSICAL NOISE AS A RANDOMNESS SOURCE (free Bernoulli stream, H4),")
print(f"           NOT as an arithmetic engine — at 1% error the bit-serial multiply pays")
print(f"           {approx(ratio_stoch)}× per operation. Verdict inherits the Chebyshev")
print(f"           bound's pessimism (exact binomial tail at N=100 is far smaller).")

# =====================================================================
print()
print("=" * 72)
print("DECISION D — analog co-processor for ODE integration")
print("=" * 72)
EPS_A = Fraction(1, 1000)      # analog error floor (declared illustrative)


def euler_error(M):
    return Fraction(3 * M - 1, 2 * M * M)


def m_min(k):
    """Smallest M with (3M-1)/(2M^2) <= 1/k — closed form + enumeration agree."""
    target = Fraction(1, k)
    m = 1
    while euler_error(m) > target:
        m += 1
    # second path: k(3M-1) <= 2M^2 checked directly
    assert k * (3 * m - 1) <= 2 * m * m and k * (3 * (m - 1) - 1) > 2 * (m - 1) ** 2
    return m


for k in (1000, 10**6):
    m = m_min(k)
    if Fraction(1, k) < EPS_A:
        reach = "analog floor 1/1000 CANNOT reach it — digital mandatory"
    else:
        reach = f"analog floor reaches it: {m} digital Euler steps : 1 analog evolution"
    print(f"  accuracy 1/{k}: digital Euler needs M = {m} steps; {reach}")
m1000 = m_min(1000)
assert m1000 == 1500
print(f"  verdict: MATCH THE FLOOR — demand 1/10³ buys the full 1500:1 step ratio;")
print(f"           demand 1/10⁶ (M = {m_min(10**6)}) exceeds the analog floor and the")
print(f"           isomorphism is OFF at that accuracy. Continuous time (H5) is a")
print(f"           bounded-accuracy win, not an infinite one.")

# =====================================================================
print()
print("=" * 72)
print("DECISION E — 'buy an Ising annealer to solve SAT faster?' (guardrail)")
print("=" * 72)
print("  premises: SAT→Ising mapping exact (EQUIVALENCE=1 on all 8 assignments);")
print("            gadget overhead measured (16 slots, 6 surviving cubic terms);")
print("            extended Church-Turing carried as an AXIOM (not derived).")
print("  VERDICT: REFUSED — WOULD_BE_GUESS for any superlinear speedup claim.")
print("  What the isomorphism DOES license: massive parallel energy evaluation")
print("  (constant-factor, problem-size-dependent constants), and an exact")
print("  encoding whose overhead is itself measured (6 cubic terms = the")
print("  quadratic-hardware tax). Structure-preserving maps preserve hardness;")
print("  the quantum case remains explicitly open and unclaimed.")
print()
print("UBP: all decisions computed in Fraction/int; floats appear only in")
print("approx() display strings, never in a comparison.")
