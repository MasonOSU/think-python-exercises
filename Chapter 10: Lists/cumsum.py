"""iterates list, returns cumulative sum to that point"""

from __future__ import print_function

def cumsum(lst):
    """adds newest iteration with itself and most recent iteration cumulatively"""
    cumlist = []
    new = 0
    for ele in lst:
        ele += new
        new = ele
        cumlist.append(ele)
    return cumlist

print(cumsum([1, 2, 3]))
