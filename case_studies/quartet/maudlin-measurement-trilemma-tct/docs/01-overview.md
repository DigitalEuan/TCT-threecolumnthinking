# 01 — Overview: Maudlin's trilemma and the three doors

## 1. The measurement problem, sharpened

Left vague, the "measurement problem" is a mood: quantum theory seems
mysterious about observation. Tim Maudlin gave it a sharp form in 1995
("Three Measurement Problems", *Topoi* 14). Three statements — each of which
sounds like plain common sense about quantum mechanics — are logically
incompatible when taken together.

The three claims (the study's givens):

- **C1 — Completeness.** The wavefunction contains everything there is to say
  about a system's physical state; nothing is hidden behind it.
- **C2 — Linearity.** The wavefunction always evolves linearly, per the
  Schrödinger equation, *including during a measurement*.
- **C3 — Single outcomes.** Measurements have outcomes: a detector shows one
  result, not a blur of several.

## 2. The conflict, in one experiment

Prepare an electron in a superposition of spin up and spin down, and let a
detector measure it. Label the detector's ready state `|D0⟩`, and its reading
states `|D↑⟩`, `|D↓⟩`.

1. The input state of electron + detector is
   `(1)|↑⟩|D0⟩ + (1)|↓⟩|D0⟩` (unnormalized; weights 1/2 and 1/2).
2. The measurement interaction acts on the basis states as
   `|↑⟩|D0⟩ ↦ |↑⟩|D↑⟩` and `|↓⟩|D0⟩ ↦ |↓⟩|D↓⟩`.
3. **By C2**, the interaction is linear, so it acts on the superposition as
   the sum of its actions:
   `(1)|↑⟩|D↑⟩ + (1)|↓⟩|D↓⟩`.
4. **By C1**, that superposition is the complete physical state — there is
   nothing else that could pick one term.
5. The two terms carry two distinct macroscopic readings, and the branches are
   orthogonal (`⟨D↑|D↓⟩ = 0`): a detector that is, in the complete-state
   description, *both reading up and reading down*.
6. **C3 says** a detector shows one result. Contradiction.

So at most two of the three claims can be right. Each major family of
interpretations is a choice of what to sacrifice — **three doors out of one
room**.

## 3. The three doors

| Door | Keep | Sacrifice | Family |
|---|---|---|---|
| 1 | C1 + C2 | C3 | Many-worlds (Everett) |
| 2 | C1 + C3 | C2 | Objective collapse (GRW, Diósi–Penrose) |
| 3 | C2 + C3 | C1 | Bohmian mechanics |

**Door 1 — Many-worlds.** The wavefunction is complete and always linear;
there is no special rule for measurement. The detector really does end up in a
superposition, and the apparent single outcome is one branch's experience.
Everettians call this a reinterpretation, not a loss — each observer sees one
result within their branch. Critics answer that the theory then owes an
account of probability (see the Lean ledger: `everett_emergence_gap`).

**Door 2 — Objective collapse.** The wavefunction is complete and outcomes are
single, but the dynamics changes: rarely for one particle, quickly for large
objects, evolution is no longer linear and a collapse really happens. GRW
(1986) makes this a stochastic localization process; the Diósi–Penrose model
ties the collapse rate to gravitational self-energy.

**Door 3 — Bohmian mechanics.** The wavefunction evolves linearly and outcomes
are single, but ψ is not the whole story: particles have definite positions in
addition. The wavefunction guides the particles; their positions supply the
one outcome we see.

## 4. Views that sidestep the frame

- **QBism** (epistemic): the wavefunction is an agent's expectations, not a
  physical state. C1 is rejected in a more radical way — the door marked
  "completeness" is declined because the wavefunction was never claimed to be
  physical in the first place.
- **Relational quantum mechanics** (Rovelli 1996): outcomes are kept, but made
  relative to observers; there is no absolute, observer-independent state of
  the detector.

These are not extra doors in the truth table; they relocate the meaning of a
claim (see `scripts/column3/05_doors_truth_table.py` and docs/04).

## 5. Bell's role

John Bell, in "Against 'Measurement'" (*Physics World*, August 1990), argued
that 'measurement', 'observer', and 'apparatus' have no place in an exact
fundamental theory: they are too vague to say where the dividing line sits.
The trilemma makes Bell's complaint precise — instead of one vague worry,
three exact claims with an explicit incompatibility.

## 6. What the trilemma buys you

Every interpretation pays a price: an added ingredient (Bohm), a change to the
dynamics (collapse), or a strange view of outcomes (many-worlds). The
disagreement is over which price is the most reasonable. Once you see the
structure, the landscape of interpretations stops looking like a pile of
unrelated ideas and becomes a map with three exits.

This repository makes that map checkable: the incompatibility is re-derived
exactly (scripts 01–05), the collapse-door arithmetic is computed exactly
(script 03), the branch accounting of the many-worlds door is computed exactly
(script 04), and the logic of the doors is formalized in Lean
(`lean/tct_maudlin/`).
