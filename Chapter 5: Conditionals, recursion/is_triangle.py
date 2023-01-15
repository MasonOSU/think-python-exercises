"""determines if three integers can form triangle from given lengths"""

from __future__ import print_function

def is_triangle(len1, len2, len3):
    """determines if triangle"""
    if (len1 + len2 < len3) \
            or (len3 + len1 < len2) \
            or (len2 + len3 < len1):
        return "no"
    return "yes"

def test():
    """input for is_triangle."""
    len1, len2, len3 = (int(x) for x in (input("submit len1, len2, len3: ").split(",")))
    print(is_triangle(len1, len2, len3))

test()
