"""takes word, string and returns True if the word uses all required letters at least once"""

from __future__ import print_function

def uses_all(fin, string):
    """prints words from a file if they contain all letters from a given string"""
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            if has_all(word, string) is True:
                print(word)

def has_all(word, string):
    """checks if all letters in word without duplicates"""
    count = 0
    for char in string:
        if char in word:
            count += 1
        if count == len(string):
            return True
    return False

uses_all("/home/mason/Comp Sci/think python exercises/Chapter 9: Case study: word play/words.txt", "aeiou")
