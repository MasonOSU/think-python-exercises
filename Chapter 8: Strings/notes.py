"""text exercises"""

from __future__ import print_function

def backward(string):
    """returns string backwards, one letter per line"""
    index = -1
    while index > -len(string) - 1:
        letter = string[index]
        print(letter)
        index -= 1

def mod_list(prefixes, suffix):
    """modifies list to correct misspellings"""
    for letter in prefixes:
        if letter in ("O", "Q"):
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)

def find(string, char, index):
    """returns index location of letter in word
    modified with start parameter
    returns -1 if letter not after start index"""
    while index < len(string):
        if string[index] == char:
            return index
        index += 1
    return -1

def count(string, char):
    """counts instances of letter in word"""
    index = 0
    total = 0
    for ele in string:
        find(string, char, index)
        if ele == char:
            total += 1
    return total

print("backward")
backward("test")
print("")

print("mod_list")
mod_list("JKLMNOPQ", "ack")
print("")

print("find")
print(find("a test string", "t", 0))
print("")

print("count")
print(count("a test string", "t"))
print("")
