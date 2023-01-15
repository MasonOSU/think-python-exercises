"""finds a word from array that returns the same homophone
if the first or second letter is removed"""

from __future__ import print_function

def find_homophones(fin):
    """finds word that makes homophone when first or second letter removed"""
    fin = set_homo(fin)
    for key in fin.items():
        prime_val = key[1][0]
        sec_word1 = key[1][1][0]
        sec_val1 = key[1][1][1]
        sec_word2 = key[1][2][0]
        sec_val2 = key[1][2][1]
        if prime_val == sec_val1 == sec_val2:
            if key != sec_word1 != sec_word2:
                print(key[0], sec_word1, sec_word2)

def set_homo(fin):
    """sets list of potential homophone answers"""
    fin = set_keys(fin)
    dpron = read_dictionary()
    homo = {}
    for key in fin:
        newkey1 = key[1:]
        newkey2 = key[0] + key[2::]
        if newkey1 in dpron and len(newkey1) == 4:
            if newkey2 in dpron and len(newkey2) == 4:
                homo.setdefault(key,
                                [dpron[key], [newkey1, dpron[newkey1]], [newkey2, dpron[newkey2]]])
    return homo

def set_keys(fin):
    """outputs words list as dictionary,
    sets values as pronunciation guides,
    removes words that aren't five characters"""
    word_dict = {}
    dpron = read_dictionary()
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            if word in dpron and len(word) == 5:
                word_dict.setdefault(word, dpron[word])
    return word_dict

def read_dictionary(filename="cmu_dictionary"):
    """reads from a file, builds dictionary mapping each word to string of primary pronunciation
    secondary pronunciations added to dictionary with a parenthetical number at end of keys,
    e.g., key for second pronunciation of 'abdominal' is 'abdominal(2)'
    filename: string
    return: maps from string to pronunciation"""
    dvar = {}
    with open(filename, encoding = "UTF-8") as file:
        for line in file:
            # skip comments
            if line[0] == "#":
                continue
            split_line = line.split()
            word = split_line[0].lower()
            pron = " ".join(split_line[1:])
            dvar[word] = pron
    return dvar

find_homophones("/home/mason/Comp Sci/think python exercises/Chapter 11: Dictionaries/words.txt")
