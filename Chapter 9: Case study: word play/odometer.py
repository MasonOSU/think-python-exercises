"""“finds six-digit integers that are palindromic for last four digits,
then palindromic for last five digits when one is added"""

from __future__ import print_function, division

def palindromic():
    """computes list of four-digit, five-digit palindromes"""
    for num in range(100001, 1000000):
        five_set = str(num % 100000)
        five_set = five_set.zfill(5)
        if five_set == five_set[::-1]:
            four_set = num - 1
            four_set = str(four_set % 10000)
            four_set = four_set.zfill(4)
            if four_set == four_set[::-1]:
                print(num - 1)

palindromic()
