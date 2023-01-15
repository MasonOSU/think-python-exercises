"""is_palinrome optimized in one line"""

from __future__ import print_function

def is_palindrome(string):
    """determines if string is palindrome"""
    if string == string[::-1]:
        return True
    return False

print(is_palindrome("bob"))
