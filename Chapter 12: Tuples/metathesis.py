"""finds all metathesis pairs in a dictionary"""

from __future__ import print_function

def metathesis(fin):
    """prints all metathesis pairs"""
    fin = anagrams(fin)
    for key in fin:
        value = fin[key]
        for item in value:
            count = 0
            for ele, char in zip(key, item):
                if ele != char:
                    count += 1
            if count == 2:
                print(''.join(key), item, count)

def anagrams(fin):
    """outputs anagrams in descending order
    sets keys to unsorted tuple duplicates"""
    dvar = setd(fin)
    fin = set_keys(fin)
    avar = {}
    for key in fin:
        newkey = tuple(sorted(key))
        if newkey in dvar:
            avar.setdefault(newkey, [])
            avar[newkey].append(key)
    avar = sorted(avar.items(), key = lambda avar: len(avar[1]), reverse = True)
    dvar = {}
    for (key, value) in avar:
        for item in value:
            dvar.setdefault(tuple(item), value)
    return dvar

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

metathesis("/home/mason/Comp Sci/think python exercises/Chapter 12: Tuples/words.txt")
