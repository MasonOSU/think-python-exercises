"""computes greatest common divisor (GCD)"""

from __future__ import print_function

def gcd(num1, num2):
    """returns GCD"""
    if num1 % num2 == 0:
        return num2
    return gcd(num2, num1 % num2)

print(gcd(10, 15))
