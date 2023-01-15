"""calculates nested list sums"""

from __future__ import print_function

def nested_sum(lst):
    """computes sum of all elements in nested list"""
    total = 0
    for ele in enumerate(lst):
        for ele in ele[1]:
            total += ele
    return total

print("nested sum:", nested_sum([[1, 2], [3], [4, 5, 6]]))
