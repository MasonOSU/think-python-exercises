"""approximates square root"""

from __future__ import division, print_function
import math

def mysqrt(num):
    """Returns estimate of square root."""
    epsilon = 0.00001
    value = 6.00000
    while True:
        est = (value + (num / value)) / 2.0
        if abs(est - value) < epsilon:
            return est
        value = est

def test_square_root():
    """prints table of results."""
    print(" num  mysqrt(num)    math.sqrt(num)  difference")
    print(" ---  -----------    --------------  ----------")
    for num in range(1, 10):
        print(f"{num: 0.1f}",
              f"{mysqrt(num): 0.11f}",
              f"{math.sqrt(num): 0.11f}",
              " ", f"{mysqrt(num) - math.sqrt(num)}")

test_square_root()
