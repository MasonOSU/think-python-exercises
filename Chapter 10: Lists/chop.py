"""computes middle of list but returns None"""

from __future__ import print_function

lst = [1, 2, 3, 4]

def chop(array):
    """removes first, last elements of list while returning None"""
    array.remove(lst[0])
    array.remove(lst[-1])

chop(lst)
print(lst)
