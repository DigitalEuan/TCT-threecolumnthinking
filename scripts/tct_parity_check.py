#!/usr/bin/env python3
"""Parity test: the HTML selector's JS engine vs the Python decision engine.

Extracts the ENGINE-START..ENGINE-END block from the delivered HTML, runs it
under Node on 45 parameter sets spanning all five panels, recomputes each
case in Python from the same premises, and compares every field exactly.
Writes tct_applied/parity.log.
"""
import json
import math
import subprocess
import sys

HTML = "/home/z/my-project/download/tct_substrate_selector.html"
LOG = "/home/z/my-project/download/tct_applied/parity.log"

CASES = (
    [("A", N, bits) for N, bits in [
        (16, 8), (55, 8), (56, 8), (100, 16), (111, 16), (228, 32), (229, 32),
        (512, 8), (512, 32), (1024, 8), (1024, 16), (1024, 32), (2048, 32),
        (4096, 8), (4096, 32), (8, 8), (8, 32), (1, 8), (128, 8), (128, 16),
        (128, 32), (55, 32), (228, 8)]] +
    [("B", T, None) for T in [1, 2, 10, 20, 21, 22, 100, 600]] +
    [("C", k, None) for k in [10, 50, 100, 500, 1000]] +
    [("D", k, None) for k in [1, 37, 100, 1000, 10000, 1000000]] +
    [("E", claim, None) for claim in ["speedup", "parallel", "encoding"]]
)


# ── Python reference (same premises as scripts/tct_applied_decisions.py) ──
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a or 1


def reduce(a, b):
    g = gcd(a, b)
    return [a // g, b // g]


PER_MAC_VN, PER_MAC_INMEM, CELL, CONV = 12838, 138, 2, 3700
FFT, SETUP, PFO = 51200, 1048576, 1025


def ref_A(N, bits):
    N = max(1, int(N)); passes = max(1, int(bits) // 8)
    analog = passes * (CELL * N * N + 2 * N * CONV)
    inmem = PER_MAC_INMEM * N * N
    vn = PER_MAC_VN * N * N
    denom = 138 - 2 * passes
    beN = (2 * CONV * passes) // denom + 1 if denom > 0 else None
    return dict(N=N, passes=passes, analog=analog, inmem=inmem, vn=vn,
                ratioInmem=reduce(inmem, analog), ratioVn=reduce(vn, analog),
                breakEven=beN, verdict="CROSSBAR" if analog < inmem else "DIGITAL")


def ref_B(T):
    T = max(1, int(T))
    opt = SETUP + T * PFO
    fft = T * FFT
    beT = -(-SETUP // (FFT - PFO))
    wins = opt <= fft
    return dict(T=T, opt=opt, fft=fft, breakEven=beT,
                ratioTotal=reduce(fft, opt) if wins else reduce(opt, fft),
                ratioFrame=reduce(FFT, PFO),
                verdict="OPTICAL" if wins else "FFT")


def ref_C(k):
    k = max(1, int(k))
    bits = -(-k * k // 4)
    return dict(k=k, bits=bits, tax=reduce(bits, 37), verdict="SOURCE_NOT_ENGINE")


def ref_D(k):
    k = max(1, int(k))
    M = 1
    while not (k * (3 * M - 1) <= 2 * M * M):
        M += 1
    admissible = k <= 1000
    return dict(k=k, M=M, admissible=admissible,
                verdict="ANALOG" if admissible else "DIGITAL_ONLY")


def ref_E(claim):
    if claim == "speedup":
        return dict(verdict="REFUSED", reason="WOULD_BE_GUESS")
    if claim == "parallel":
        return dict(verdict="GRANTED_WITH_CAVEAT", reason="constant-factor only")
    return dict(verdict="GRANTED", reason="exact encoding")


REF = {"A": ref_A, "B": ref_B, "C": ref_C, "D": ref_D, "E": ref_E}


def main():
    html = open(HTML, encoding="utf-8").read()
    start = html.index("/*ENGINE-START*/")
    end = html.index("/*ENGINE-END*/")
    engine = html[start:end]

    harness = engine + """
    var cases = %s;
    var out = [];
    cases.forEach(function (c) {
      var id = c[0] + ":" + c[1] + (c[2] === null ? "" : ":" + c[2]);
      var r;
      if (c[0] === "A") r = decideA(c[1], c[2]);
      else if (c[0] === "B") r = decideB(c[1]);
      else if (c[0] === "C") r = decideC(c[1]);
      else if (c[0] === "D") r = decideD(c[1]);
      else r = decideE(c[1]);
      out.push({ id: id, panel: c[0], result: r });
    });
    console.log(JSON.stringify(out));
    """ % json.dumps([list(c[:2]) + [c[2]] for c in CASES])

    proc = subprocess.run(["node", "-e", harness], capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        print("NODE FAILED:", proc.stderr[:2000])
        return 2
    js_results = {r["id"]: r["result"] for r in json.loads(proc.stdout)}

    lines = ["# Parity test — HTML JS engine vs Python decision engine",
             f"# cases: {len(CASES)} (A:23 B:8 C:5 D:6 E:3)   date: 2026-11-01", ""]
    mismatches = 0
    for panel, a, b in CASES:
        cid = f"{panel}:{a}" + (f":{b}" if b is not None else "")
        py = REF[panel](*([a, b] if panel == "A" else [a]))
        js = js_results[cid]
        diffs = []
        for k, v in py.items():
            jsv = js.get(k)
            if isinstance(v, bool) or isinstance(jsv, bool):
                if bool(jsv) != bool(v):
                    diffs.append(f"{k}: js={jsv} py={v}")
            elif isinstance(v, list):
                if [int(x) for x in jsv] != [int(x) for x in v]:
                    diffs.append(f"{k}: js={jsv} py={v}")
            else:
                if jsv != v:
                    diffs.append(f"{k}: js={jsv} py={v}")
        if diffs:
            mismatches += 1
            lines.append(f"MISMATCH {cid}: " + "; ".join(diffs))
        else:
            key = py.get("verdict")
            extra = {kk: py[kk] for kk in ("analog", "opt", "bits", "M") if kk in py}
            lines.append(f"OK   {cid:14} verdict={key} {extra if extra else ''}")
    lines.append("")
    lines.append(f"RESULT: {len(CASES) - mismatches}/{len(CASES)} cases match exactly"
                 + (f" — {mismatches} MISMATCHES" if mismatches else " — PARITY CONFIRMED"))
    report = "\n".join(lines)
    open(LOG, "w").write(report + "\n")
    print(report[-400:])
    return 1 if mismatches else 0


if __name__ == "__main__":
    sys.exit(main())
