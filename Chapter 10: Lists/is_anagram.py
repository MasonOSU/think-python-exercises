"""outputs if anagram"""

from __future__ import print_function

def is_anagram(str1, str2):
    """determines if two strings are anagrams"""
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    str1 = list(str1)
    str2 = list(str2)
    str1.sort()
    str2.sort()
    return str1 == str2

print("is_anagram:", is_anagram("act", "cat"))
print("is_anagram:", is_anagram("punishment", "nine thumps"))
print("is_anagram:", is_anagram("this is", "not an anagram"))
