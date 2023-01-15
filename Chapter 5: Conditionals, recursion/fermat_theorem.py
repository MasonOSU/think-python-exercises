"""checks Fermat's theorem"""

from __future__ import print_function

def check_fermat(pos1, pos2, pos3, exp):
    """Fermat's theorem states no three positive integers satisfy
    equation a^n + b^n = c^n for any int greater than 2"""
    theorem = (pos1 ** exp) + (pos2 ** exp)
    if exp > 2 and (theorem == (pos3 ** exp)):
        return "Fermat's wrong"
    return "doesn't work"

def fermat():
    """inputs values for check_fermat"""
    pos1, pos2, pos3, exp = \
        (int(x) for x in input("enter three positive integers, exponent").split(","))
    print(check_fermat(pos1, pos2, pos3, exp))

fermat()
