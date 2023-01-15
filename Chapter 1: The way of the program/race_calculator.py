"""calculates miles per hour of a 10-km race in 42 min, 42 sec"""

from __future__ import division, print_function

KM_TO_MILES = 10 / 1_61
TOTAL_SEC = (60 * 42) + 42
SEC_PER_MILE = TOTAL_SEC / KM_TO_MILES
MPH = 60 / (SEC_PER_MILE / 60)

print(f"{MPH:.2f}")
