"""prints words from a file without the letter e, computes percentage"""

from __future__ import print_function, division

def gadsby(string):
    """prints words from a file without the letter e"""
    count = 0
    with open(string, encoding = "UTF-8") as file:
        for word in file:
            word = word.strip()
            if has_no_e(word) is False:
                print(word)
                count += 1
    compute_pct(string)

def compute_pct(string):
    """computes percentage of words with no e"""
    no_count, all_count = 0, 0
    with open(string, encoding = "UTF-8") as file:
        for word in file:
            if has_no_e(word) is False:
                no_count += 1
            all_count += 1
        pct = (no_count / all_count) * 100
        print("percent with no e:" + f"{pct: .2f}" + "%")

def has_no_e(string):
    """returns True if letter e found in word"""
    string = string.lower()
    return "e" in string

gadsby("/home/mason/Comp Sci/think python exercises/Chapter 9: Case study: word play/words.txt")
