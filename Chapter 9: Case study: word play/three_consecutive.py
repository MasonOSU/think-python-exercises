""" identifies word with three consecutive letter pairs"""

from __future__ import print_function

def three_doubles(fin):
    """prints words with three consecutive letter pairs"""
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            if check(word) is True:
                print(word)

def check(word, pairs = 0):
    if pairs == 3:
        return True
    if len(word) <= 1 and pairs < 3:
        return False
    if word[0] == word[1]:
        pairs += 1
        return check(word[2:], pairs)
    if word[0] != word[1]:
        pairs = 0
    return check(word[1:], pairs)

three_doubles("/home/mason/Comp Sci/think python exercises/Chapter 9: Case study: word play/words.txt")
