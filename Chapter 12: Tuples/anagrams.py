"""reads word list from file, prints anagram word sets as lists_6_2.py
prints anagram lists_6_2.py in descending order
outputs 'bingos' - i.e., eight-letter sets forming the most words"""

from __future__ import print_function

def bingo(fin):
    """outputs winning eight-letter set, full anagrams list"""
    fin = anagrams(fin)
    winner = {}
    for (_, value) in fin:
        if len(value[0]) == 8:
            winner.setdefault(tuple(value), len(value))
    winner = sorted(winner.items(), key = lambda winner: winner[1], reverse = True)
    letters = sorted(winner[0][0][0])
    print("winning letters are", letters)
    print("\n" + "anagrams sorted by descending")
    for (_, value) in fin:
        print(value)

def anagrams(fin):
    """outputs anagrams in descending order"""
    dvar = setd(fin)
    fin = set_keys(fin)
    final = {}
    for key in fin:
        newkey = tuple(sorted(key))
        if newkey in dvar:
            final.setdefault(newkey, [])
            final[newkey].append(key)
    final = sorted(final.items(), key = lambda final: len(final[1]), reverse = True)
    return final

def setd(fin):
    """sets keys as sorted by descending frequency"""
    fin = set_keys(fin)
    dvar = {}
    for key in fin:
        key = tuple(sorted(key))
        dvar[key] = dvar.get(key, 0) + 1
    dvar = sorted(dvar.items(), key = lambda dvar: dvar[1], reverse = True)
    dvar = {key: value for key, value in dvar if value > 1}
    return dvar

def set_keys(fin):
    """outputs words list as dictionary"""
    word_dict = {}
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            word_dict[word] = word_dict.get(word, None)
    return word_dict

bingo("/home/mason/Comp Sci/think python exercises/Chapter 12: Tuples/words.txt")
