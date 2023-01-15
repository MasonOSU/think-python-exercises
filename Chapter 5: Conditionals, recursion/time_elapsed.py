"""reads current time, converts to time of day in days, hours, minutes, seconds since epoch"""

import time

total_days = time.time() / (3600 * 24)
rem_days = total_days % 365
hours = (rem_days * 24) % 24
minutes = (hours * 60) % 60
seconds = (minutes * 60) % 60

print(str(int(total_days)) + " days, "
      + str(int(hours)) + " hours, "
      + str(int(minutes)) + " min, "
      + str(int(seconds)) + " sec since epoch UTC")
