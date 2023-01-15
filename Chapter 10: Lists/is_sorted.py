"""tests if list is sorted"""

from __future__ import print_function

def is_sorted(lst):
    """determines if list is sorted"""
    lst2 = lst[:]
    lst2.sort()
    return lst == lst2

print("is_sorted:", is_sorted([1, 2, 2]))
print("is_sorted:", is_sorted(["b", "a"]))
