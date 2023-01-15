"""finds semordnilap pairs"""

from __future__ import print_function
from bisect import bisect_left

def reverse_pairs(fin):
    """lists_6_2.py semordnilap pairs"""
    lst = build_list(fin)
    for ele in lst:
        rev = bisect_left(lst, ele)
        if rev != len(lst) and lst[rev] == ele[::-1]:
            del lst[rev]
        semo = bisect_left(lst, ele[::-1])
        if semo != len(lst) and lst[semo] == ele[::-1]:
            del lst[semo]
            print(ele, ele[::-1])

def build_list(fin):
    """cleans, builds list without calling append"""
    lst = []
    with open(fin, encoding = "UTF_8") as file:
        for line in file:
            line = line.strip()
            line = line.split()
            lst += line
    return lst

reverse_pairs("/home/mason/Comp Sci/think python exercises/Chapter 10: Lists/words.txt")
