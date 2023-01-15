"""computes middle of list"""

from __future__ import print_function

def middle(lst):
    """returns all but first, last elements of list"""
    return lst[1:-1]

print("middle input:", middle([1, 2, 3, 4]))
