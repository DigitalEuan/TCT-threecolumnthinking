#!/usr/bin/env python3
"""Programmatic visual + content check of the two deliverable PDFs."""
import re
import subprocess
import sys


def pages_text(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf],
            capture_output=True, text=True).stdout).group(1))
    return n, {p: subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), pdf, "-"],
               capture_output=True, text=True).stdout for p in range(1, n + 1)}


def check(pdf, renderdir, expect_pages, checks, glyphs, bad_strings):
    fails = []
    subprocess.run(["bash", "-c",
        f"rm -rf {renderdir} && mkdir -p {renderdir} && "
        f"pdftoppm -r 60 -jpeg -jpegopt quality=60 {pdf} {renderdir}/page"], check=True)
    import glob
    from PIL import Image
    imgs = sorted(glob.glob(f"{renderdir}/page-*.jpg"))
    if len(imgs) != expect_pages:
        fails.append(f"page count {len(imgs)} != expected {expect_pages}")
    for img in imgs:
        im = Image.open(img).convert("L")
        h = im.histogram()
        if 1 - h[255] / sum(h) < 0.01:
            fails.append(f"nearly blank page: {img}")
    n, pages = pages_text(pdf)
    full = "\n".join(pages.values())
    for bad in bad_strings:
        if bad in full:
            fails.append(f"leaked artifact: {bad!r}")
    for g in glyphs:
        if g not in full:
            fails.append(f"math glyph missing: {g}")
    for label, needle in checks:
        if needle not in full:
            fails.append(f"missing {label}: {needle[:60]}")
    print(f"{pdf}: {n} pages, {len(imgs)} rendered, "
          f"{'ALL CHECKS PASSED' if not fails else 'FAILURES:'}")
    for f in fails:
        print("  -", f)
    return 1 if fails else 0


def main():
    rc = 0
    rc |= check(
        "/home/z/my-project/download/tct_paper.pdf", "/tmp/render_paper",
        expect_pages=16,
        checks=[
            ("Run D section", "5.4 Run D"),
            ("case studies section", "5.6 External case studies"),
            ("battery totals", "105"),
            ("battery build", "12/12"),
            ("quartet totals", "49+12+25+2"),
            ("quartet Lean totals", "30/12/25"),
            ("maudlin row", "10/3/5"),
            ("platform A", "dola.com"),
            ("platform quartet", "aistudio.xiaomimimo.com"),
            ("kernel catch", "729"),
            ("observation 6.12", "6.12 The Python tier transfers"),
            ("reference 5", "[5] External case-study quartet"),
            ("section 7 quartet gap", "scale by the external case studies"),
            ("conclusion transfer", "from experiment to"),
            ("artifacts regeneration", "regeneration"),
            ("regenerated ref", "Regenerated and"),
            ("xor refinement", "closed-literal XOR"),
            ("T10 accounting", "accounting refinement"),
        ],
        glyphs=["𝔽", "ℤ", "π", "¢", "∆", "ℚ"],
        bad_strings=["TODO", "XXX", "待补充", "【", "____", "|---", "## ", "undefined", "NaN"],
    )
    rc |= check(
        "/home/z/my-project/download/tct_case_studies.pdf", "/tmp/render_cs",
        expect_pages=5,
        checks=[
            ("scope", "Scope and provenance"),
            ("famous", "famous-constants-tct"),
            ("speed of light", "speed-of-light-derivation-tct"),
            ("isomorphisms", "physical-isomorphisms-tct"),
            ("maudlin", "maudlin-measurement-trilemma-tct"),
            ("audit section", "Independent audit"),
            ("audit table", "byte-identical"),
            ("finding 1", "transfers perfectly"),
            ("finding 2", "do not compile as shipped"),
            ("finding 3", "all four projects build"),
            ("totals", "88 claims = 49 proved + 12 sorry + 25 axioms + 2"),
            ("maudlin ledger", "10 proved, 3 sorry, 5 axioms"),
            ("reproduction", "Reproduction"),
            ("gf2", "GF(2)"),
        ],
        glyphs=["π", "¢", "γ", "ζ", "α"],
        bad_strings=["TODO", "XXX", "待补充", "【", "____", "|---", "## ", "undefined", "NaN"],
    )
    return rc


if __name__ == "__main__":
    sys.exit(main())
