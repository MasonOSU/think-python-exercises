"""returns True if letters in word appear in alphabetical order
counts words"""

from __future__ import print_function

def is_abc(fin):
    """prints words that are abecedarian"""
    count = 0
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            if compare(word) is True:
                count += 1
                print(word)
    print(count, "abecedarian words")

def compare(string):
    """checks if string is abecedarian"""
    old_char = 0
    new_char = 1
    for _ in string:
        if string[old_char] <= string[new_char]:
            old_char += 1
            new_char += 1
            if new_char == len(string):
                return True
    return False

is_abc("/home/mason/Comp Sci/think python exercises/Chapter 9: Case study: word play/words.txt")
