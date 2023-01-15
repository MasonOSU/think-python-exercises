"""takes word, string. returns True if word contains only letters in string"""

from __future__ import print_function

def uses_only(fin, string):
    """prints words from a file if they contain letters from a given string"""
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            if has_all(word, string) is True:
                print(word)

def has_all(word, string):
    """checks if all letters in word without duplicates"""
    word = remove_extra(word)
    count = 0
    for char in string:
        if char in word:
            count += 1
        if count == len(word):
            return True
    return False

def remove_extra(word):
    """removes duplicates from string"""
    word = sorted(word)
    new_word = ""
    for char in word:
        if char in word:
            if char not in new_word:
                new_word += char
    return new_word

uses_only("/home/mason/Comp Sci/think python exercises/Chapter 9: Case study: word play/words.txt", "acefhlo")
