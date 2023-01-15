"""checks if duplicates"""

from __future__ import print_function

def has_duplicates(lst):
    """determines if duplicates are in a list."""
    new_lst = []
    new_lst = [new_lst.append(lst) for ele in lst if ele not in new_lst]
    if new_lst != lst:
        return True
    return False

print("has_duplicates:", has_duplicates([1, 2, 3, 4, 2]))
