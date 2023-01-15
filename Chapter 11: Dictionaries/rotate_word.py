"""reads words list, finds all rotate pairs by an integer"""

from __future__ import print_function

def rotate_word(fin, rot):
    """returns rotate pairs from dictionary"""
    fin = set_keys(fin)
    for key in fin:
        rot_word = ""
        for letter in key:
            letter = ord(letter)
            letter += rot
            if letter > 122:
                letter -= 26
            letter = chr(letter)
            rot_word += letter
        if rot_word in fin:
            print(key, rot_word)

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

print(rotate_word("/home/mason/Comp Sci/think python exercises/Chapter 11: Dictionaries/words.txt", 5))
