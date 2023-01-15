"""cleans word list and prints words more than 20 characters"""

from __future__ import print_function

def over20(word_list):
    """prints words more than 20 characters"""
    with open(word_list, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            if len(word) > 20:
                print(word)

over20("/home/mason/Comp Sci/think python exercises/Chapter 9: Case study: word play/words.txt")
