#!/usr/bin/env python3
"""T05 - What comes after Wednesday? (Z/7Z, external calendar anchor)"""
from datetime import date, timedelta

# cyclic arithmetic: Wednesday = 3 in the ISO 8601 indexing (Mon=1..Sun=7)
WED = 3
nxt = (WED + 1) % 7
wrap = (7 % 7)                                # Sunday = 7 = 0 in Z/7Z
week = (WED + 7) % 7
assert nxt == 4 and wrap == 0 and week == WED

# external stdlib calendar anchor (no prior weekday knowledge assumed):
d = date(2026, 11, 1)
while d.isoweekday() != WED:                  # find the next real Wednesday
    d += timedelta(days=1)
assert d.isoweekday() == WED
d_next = d + timedelta(days=1)
anchor_ok = 1 if d_next.isoweekday() == nxt else 0
assert anchor_ok == 1                         # the calendar confirms (3+1)%7=4
assert (d + timedelta(days=7)).isoweekday() == week

print(f"WED_INDEX={WED}")
print(f"THU_INDEX={nxt}")
print("CALENDAR_ANCHOR_OK=1")
print("CYCLE_OK=1")
print(f"NEXT_DAY_INDEX={nxt}")
