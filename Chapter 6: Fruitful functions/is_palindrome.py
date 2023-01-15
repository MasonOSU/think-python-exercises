"""checks if word is a palindrome, returns nothing for two letters or less"""

from __future__ import print_function

def first(word):
    """returns first letter"""
    return word[0]

def last(word):
    """returns last letter"""
    return word[-1]

def middle(word):
    """returns middle letters"""
    return word[1:-1]

def is_palindrome(word):
    """returns True if palindrome, False otherwise"""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

if __name__ == "__main__":
    # tests for no output
    print(middle("Am"), middle("I"), middle(""))

    print(is_palindrome('allen'))
    print(is_palindrome('bob'))
    print(is_palindrome('otto'))
    print(is_palindrome('redivider'))
