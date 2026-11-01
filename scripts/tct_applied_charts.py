#!/usr/bin/env python3
"""Crossover charts for the applied-isomorphisms brief.

All values computed exactly (Fraction/int) in this script; floats appear
only as pixel coordinates for matplotlib. Charts follow the charts-skill
matplotlib template (constrained_layout, clean_axis, CB-safe palette,
direct labels / legend outside, no overlap).
"""
import matplotlib
import matplotlib.font_manager as fm
fm.fontManager.addfont('/usr/share/fonts/truetype/chinese/NotoSansSC-Regular.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
import matplotlib.pyplot as plt
from fractions import Fraction

plt.rcParams.update({
    'font.sans-serif': ['Noto Sans SC', 'DejaVu Sans'],
    'axes.unicode_minus': False,
    'figure.facecolor': '#FFFFFF', 'axes.facecolor': '#FFFFFF',
    'axes.edgecolor': '#E5E7EB', 'axes.linewidth': 0.8,
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.grid': False,
    'xtick.major.size': 0, 'ytick.major.size': 0,
    'xtick.labelsize': 9, 'ytick.labelsize': 9,
    'axes.labelsize': 10, 'axes.titlesize': 13, 'axes.titleweight': 'bold',
    'axes.titlepad': 14,
    'legend.frameon': False, 'legend.fontsize': 9,
    'figure.dpi': 200, 'savefig.dpi': 200, 'savefig.facecolor': '#FFFFFF',
})

CB = ['#0077BB', '#33BBEE', '#009988', '#EE7733', '#CC3311', '#EE3377']
G900, G700, G500, G400, G300 = '#111827', '#374151', '#6B7280', '#9CA3AF', '#D1D5DB'
OUT = '/home/z/my-project/download/tct_applied/figures'
import os
os.makedirs(OUT, exist_ok=True)

# ---- premises ----
CELL, CONV, INMEM, VN = 2, 3700, 138, 12838


def clean_axis(ax, grid=True):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if grid:
        ax.yaxis.grid(True, alpha=0.08, color=G300)
        ax.set_axisbelow(True)


# ═════════════════════════════════════════════════════════════════════
# Fig 1 — per-MAC energy vs N: the converter hump and the two break-evens
# ═════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 4.35), constrained_layout=True)
Ns = [8 * 2 ** i for i in range(10)]          # 8 .. 4096
per_mac = lambda passes, N: Fraction(passes * (CELL * N * N + 2 * N * CONV), N * N)

ax.axhline(float(Fraction(VN, 1)), color=G300, lw=1.2, ls=':')
ax.axhline(float(Fraction(INMEM, 1)), color=CB[3], lw=1.2, ls='--')
ax.plot([float(n) for n in Ns], [float(per_mac(1, n)) for n in Ns],
        color=CB[0], lw=2.4, marker='o', ms=4, label='crossbar, 8-bit (1 pass)')
ax.plot([float(n) for n in Ns], [float(per_mac(4, n)) for n in Ns],
        color=CB[1], lw=2.4, marker='s', ms=4, label='crossbar, 32-bit (4 passes)')

for N0, lab, y in ((55, 'N = 55', INMEM), (228, 'N = 228', INMEM)):
    ax.axvline(N0, color=G400, lw=1.0, ls=':')
    ax.annotate(lab, xy=(N0, 700), ha='center', fontsize=9, color=G700,
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=G300, lw=0.6))
ax.set_xscale('log', base=2)
ax.set_yscale('log')
ax.set_xticks([8, 32, 55, 128, 228, 512, 1024, 4096])
ax.set_xticklabels(['8', '32', '55', '128', '228', '512', '1024', '4096'])
ax.set_xlabel('matrix dimension N')
ax.set_ylabel('energy per MAC-equivalent (units of 0.1 pJ)')
ax.set_title('Converters dominate until N ≈ 55 (8-bit) / 228 (32-bit) — then the crossbar approaches 2 units per MAC')
ax.text(4100, float(VN), 'von Neumann 12838', fontsize=9, color=G500, va='center', ha='left')
ax.text(4100, float(INMEM), 'in-memory 138', fontsize=9, color=CB[3], va='center', ha='left')
ax.legend(loc='lower left', bbox_to_anchor=(0.02, 0.06))
ax.set_xlim(7, 14000)
clean_axis(ax)
fig.savefig(f'{OUT}/fig1_energy_crossover.png', bbox_inches='tight')
plt.close(fig)

# ═════════════════════════════════════════════════════════════════════
# Fig 2 — total ops vs kernel reuse T: amortization crossover at T = 21
# ═════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 4.35), constrained_layout=True)
SETUP, PFO, PFF = 1024 ** 2, 1025, 51200
Ts = list(range(0, 625, 25))
opt = [SETUP + T * PFO for T in Ts]
fft = [T * PFF for T in Ts]
ax.plot(Ts, fft, color=G500, lw=2.0, ls='--')
ax.plot(Ts, opt, color=CB[0], lw=2.4)
ax.fill_between(Ts, opt, fft, where=[f >= o for f, o in zip(fft, opt)],
                color=CB[0], alpha=0.06)
ax.annotate('FFT total: T × 51200', xy=(600, 600 * PFF), xytext=(452, 600 * PFF),
            fontsize=9, color=G700, va='center',
            arrowprops=dict(arrowstyle='-', color=G400, lw=0.8))
ax.annotate('optical total: 1048576 + T × 1025', xy=(600, SETUP + 600 * PFO),
            xytext=(352, SETUP + 600 * PFO + 2.2e6), fontsize=9, color=CB[0],
            va='center', arrowprops=dict(arrowstyle='-', color=CB[0], lw=0.8))
ax.axvline(21, color=CB[3], lw=1.2, ls=':')
ax.annotate('crossover T* = 21\n(1048576 / 50175)', xy=(21, 2.6e7), ha='left',
            xytext=(52, 2.55e7), fontsize=9, color=CB[3],
            arrowprops=dict(arrowstyle='->', color=CB[3], lw=0.9))
ax.annotate('at T = 600: 18.5× fewer ops\n(49.95× per frame)', xy=(600, 1.0e7),
            ha='right', xytext=(560, 1.15e7), fontsize=9, color=G700,
            arrowprops=dict(arrowstyle='->', color=G400, lw=0.8))
ax.set_xlabel('frames between kernel rewrites T')
ax.set_ylabel('total operations (N = 1024)')
ax.set_title('Optical 4f convolution wins only beyond T = 21 reuses — static kernels, not adapted ones')
clean_axis(ax)
fig.savefig(f'{OUT}/fig2_convolution_amortization.png', bbox_inches='tight')
plt.close(fig)

# ═════════════════════════════════════════════════════════════════════
# Fig 3 — Euler error vs M against the analog floor
# ═════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 3.98), constrained_layout=True)
Ms = sorted(set([1, 2, 3, 5, 8, 12, 20, 30, 50, 80, 125, 200, 320, 500, 800,
                 1250, 1500, 2000, 3200, 5000, 8000, 12500, 20000, 32000,
                 50000, 80000, 125000, 200000, 320000, 500000, 800000, 1500000]))
err = [float(Fraction(3 * M - 1, 2 * M * M)) for M in Ms]
ax.plot(Ms, err, color=CB[0], lw=2.4)
ax.axhline(1e-3, color=CB[3], lw=1.4, ls='--')
ax.text(1.15, 1.25e-3, 'analog floor 1/1000 (declared)', fontsize=9, color=CB[3], va='bottom')
ax.axvline(1500, color=CB[3], lw=1.0, ls=':')
ax.annotate('digital meets the floor at M = 1500\n(1500 steps : 1 analog evolution)',
            xy=(1500, 3.5e-4), xytext=(8000, 1.6e-3), fontsize=9, color=G700,
            arrowprops=dict(arrowstyle='->', color=G400, lw=0.8))
ax.annotate('1/1,000,000 accuracy: floor unreachable —\ndigital only, M = 1,500,000',
            xy=(1500000, 1e-6), xytext=(52000, 4e-7), fontsize=9, color=G700,
            arrowprops=dict(arrowstyle='->', color=G400, lw=0.8))
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Euler steps M')
ax.set_ylabel('integration error (3M−1) / 2M²')
ax.set_title('Continuous time is a bounded-accuracy win: the isomorphism switches off below the analog floor')
clean_axis(ax)
fig.savefig(f'{OUT}/fig3_euler_error.png', bbox_inches='tight')
plt.close(fig)

# ═════════════════════════════════════════════════════════════════════
# Fig 4 — noise bits vs error tolerance (bar, log y) with the multiply tax
# ═════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9, 3.95), constrained_layout=True)
labels = ['ε = 1/10', 'ε = 1/100', 'ε = 1/1000']
bits = [25, 2500, 250000]                     # p(1-p)/eps^2 at p=1/2 (exact)
bars = ax.bar(labels, bits, width=0.52, color=[CB[1], CB[0], G400],
              zorder=3, edgecolor='white', linewidth=0.5)
for b, v in zip(bars, bits):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() * 1.18, f'{v:,} bits',
            ha='center', va='bottom', fontsize=10, color=G900, fontweight='bold')
ax.set_yscale('log')
ax.set_ylim(10, 3.2e6)
ax.set_ylabel('noise bits per estimate (Chebyshev N ≥ p(1−p)/ε²)')
ax.set_title('The Bernoulli source is free; the arithmetic is not — 1% costs 2500 bits, 67.6× a 37-unit multiply')
ax.text(0.5, -0.16, 'stochastic multiply at ε = 1/100: 2500 AND-units vs one 37-unit FP multiply → 2500/37 = 67.57×',
        transform=ax.transAxes, ha='center', fontsize=9, color=G500)
clean_axis(ax)
fig.savefig(f'{OUT}/fig4_sampling_bits.png', bbox_inches='tight')
plt.close(fig)

print("saved 4 figures to", OUT)
