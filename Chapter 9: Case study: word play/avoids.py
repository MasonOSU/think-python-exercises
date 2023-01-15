"""filters words with none of five specific letters
finds the combination that excludes the least words"""

from __future__ import print_function

def avoids(fin):
    """prints words from a file without five letters"""
    string = input(str("enter five letters: ")).split(" ", 5)
    string = ''.join(string)
    if len(string) != 5:
        string = input(str("enter five letters: ")).split(" ", 5)
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            if has_none(word, string) is False:
                print(word)

def has_none(word, string):
    """checks if any letters in words"""
    for char in string:
        if char in word:
            return True
    return False

avoids("/home/mason/Comp Sci/think python exercises/Chapter 9: Case study: word play/words.txt")
