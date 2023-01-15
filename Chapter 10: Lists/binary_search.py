"""searches for word in list with bisect module"""

from __future__ import print_function
from bisect import bisect_left

def bisect_search(fin, word):
    """searches with bisect module"""
    lst = []
    with open(fin, encoding = "UTF-8") as file:
        for line in file:
            line = line.split()
            lst += line
        lst = sorted(lst)
        where = bisect_left(lst, word)
        if where != len(lst) and lst[where] == word:
            return where
        return None

print(bisect_search("/home/mason/Comp Sci/think python exercises/Chapter 10: Lists/words.txt", "foxfire"))
