"""inverts dictionary for word list"""

from __future__ import print_function

def invert_dict(dvar):
    """inverts dictionary for word list"""
    dvar = set_keys(dvar)
    inverse = {}
    for (key, value) in dvar.items():
        inverse.setdefault(value, key)
    return inverse

def set_keys(fin):
    """outputs words list as dictionary"""
    word_dict = {}
    count = 1
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            word_dict[word] = word_dict.get(word, 0) + count
            count += 1
    return word_dict

print(invert_dict("/home/mason/Comp Sci/think python exercises/Chapter 11: Dictionaries/words.txt"))
