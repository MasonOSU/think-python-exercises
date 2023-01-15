"""finds child's age when it's been palindromic to mother's age six times and can be twice more"""

from __future__ import print_function

def find_age():
    """finds child's age where age with parent is palindromic six times
    and will be twice more"""
    gap = find_gap()
    instances = 0
    for child in range(0, 100):
        parent = child + gap
        child = str(child)
        child = child.zfill(2)
        parent = str(parent)
        if child[::-1] == parent:
            instances += 1
            if instances == 6:
                print("child's age is " + child)

def find_gap():
    """finds child's gap where age with parent is palindromic eight times"""
    gap = 14
    instances = 0
    while gap < 40:
        for child in range(1, 100):
            parent = child + gap
            child = str(child)
            parent = str(parent)
            child = child.zfill(2)
            if child[::-1] == parent:
                instances += 1
                if instances == 8:
                    return gap
        gap += 1

find_age()
