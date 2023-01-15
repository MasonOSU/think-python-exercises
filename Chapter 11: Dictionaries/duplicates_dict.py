"""checks if duplicates"""

from __future__ import print_function

def has_duplicates(lst):
    """determines if duplicates are in a list"""
    dvar = {}
    for ele in lst:
        dvar[ele] = dvar.get(ele, 0) + 1
        if dvar[ele] > 1:
            return True
    return False

print("has_duplicates:", has_duplicates([1, 2, 3, 4, 2]))
