"""solves the birthday problem"""

from __future__ import print_function
import random

def same_bday():
    """computes probability of 23 people having same birthday"""
    timer = 0
    count = 0
    while timer < 100:
        timer += 1
        lst = [random.randint(1, 365) for _ in range(23)]
        lst.sort()
        new_lst = []
        for ele in lst:
            if ele not in new_lst:
                new_lst.append(ele)
        new_lst.sort()
        if lst == new_lst:
            count += 1
    result = (count / 100.0) * 100

    return f"{result: .0f}" + "%" + " share the same birthday"

print(same_bday())
