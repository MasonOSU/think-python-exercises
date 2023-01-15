"""lists_6_2.py words.txt as list items using append, then without append"""

from __future__ import print_function

def words_append(fin):
    """lists_6_2.py all words of text file as list items using append
    more steps to execute than an idiom. calls sppend module each time"""
    lst = []
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.split()
            for char in word:
                lst.append(char)
    return lst

def words_idiom(fin):
    """lists_6_2.py all words of text file as list items without append
    less steps to execute than append. doesn't call the module repeatedly"""
    lst = []
    with open(fin, encoding = "UTF-8") as file:
        for word in file:
            word = word.split()
            lst += word
    return lst

print(words_append("/home/mason/Comp Sci/think python exercises/Chapter 10: Lists/words.txt"))
print(words_idiom("/home/mason/Comp Sci/think python exercises/Chapter 10: Lists/words.txt"))
