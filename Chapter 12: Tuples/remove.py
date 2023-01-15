"""outputs longest valid English word if letters removed piecemeal from end or middle"""

from __future__ import print_function

memo = {}

def build(fin):
    orig = set_keys(fin)
    fin = child(fin)
    def reduce(str):
        if str not in orig or len(str) <= 1:
            return None
        front, back = str[1:], str[:-1]
        half = len(str) // 2
        mid = str[0:(half - 1)] + str[half:]
        mid2 = str[0:half] + str[(half + 1):]
        set = [front, back, mid]
        for item in set:
            if item in orig:
                print(str, item)
                return reduce(item)
            if item not in orig:
                if len(str) % 2 == 0:
                    if mid2 in orig:
                        print(str, item)
                        return reduce(mid2)

    reduce("oology")

def child(fin):
    fin = set_keys(fin)
    child = {}
    for key in fin:
        front, back = key[1:], key[:-1]
        halve = len(key) // 2
        mid = key[0:(halve - 1)] + key[halve:]
        mid2 = key[0:halve] + key[(halve + 1):]
        if len(key) % 2 == 0:
            if mid2 in fin:
                child.setdefault((key, mid2))
        set = [front, back, mid]
        for item in set:
            if item in fin:
                child.setdefault((key, item))
    return child

def set_keys(fin):
    """outputs words list as dictionary"""
    fin = fin
    nfin = {}
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            nfin[word] = nfin.get(word, None)
    return nfin

build("/home/mason/Comp Sci/think python exercises/Chapter 12: Tuples/words.txt")

# def test(fin):
#     fin = set_keys(fin)
#
#     def reduce(str):
#         if str not in fin or len(str) <= 1:
#             return None
#         front, back = str[1:], str[:-1]
#         half = len(str) // 2
#         mid = str[0:(half - 1)] + str[half:]
#         mid2 = str[0:half] + str[(half + 1):]
#         set = [front, back, mid]
#         for item in set:
#             if item in fin:
#                 memo[item] = None
#                 # t.setdefault(item)
#                 return reduce(item)
#             if len(str) % 2 == 0:
#                 if mid2 in fin:
#                     memo[item] = None
#                     # t.setdefault(mid2)
#                     return reduce(mid2)
#
#     for key in fin:
#         reduce(key)
#
# test("/home/mason/Comp Sci/think python exercises/Chapter 12: Tuples/words.txt")
# print(memo, len (memo))
