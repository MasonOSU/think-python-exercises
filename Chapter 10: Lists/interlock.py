"""compiles words from list made by interlocking two other words"""

from __future__ import(print_function)
from bisect import bisect_left

def interlock(fin):
    """finds interlocking pairs in two or three words"""
    steps = int(input("print words of _ pairs (2 or 3): "))
    if steps > 3 or steps < 2:
        raise ValueError
    lst = build_lst(fin)
    for ele in lst:
        if steps < 3:
            inter1 = bisect_left(lst, ele[::steps])
            inter2 = bisect_left(lst, ele[1:][::steps])
            if inter1 != len(lst) and lst[inter1] == ele[::steps]:
                if inter2 != len(lst) and lst[inter2] == ele[1:][::steps]:
                    print(ele, lst[inter1], lst[inter2])
        inter1 = bisect_left(lst, ele[::steps])
        inter2 = bisect_left(lst, ele[1:][::steps])
        inter3 = bisect_left(lst, ele[2:][::steps])
        if inter1 != len(lst) and lst[inter1] == ele[::steps]:
            if inter2 != len(lst) and lst[inter2] == ele[1:][::steps]:
                if inter3 != len(lst) and lst[inter3] == ele[2:][::steps]:
                    print(ele, lst[inter1], lst[inter2], lst[inter3])

def build_lst(fin):
    """builds, cleans list"""
    lst = []
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            word = word.split()
            lst += word
    return lst

interlock("/home/mason/Comp Sci/think python exercises/Chapter 10: Lists/words.txt")
