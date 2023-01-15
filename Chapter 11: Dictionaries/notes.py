"""notes"""

from __future__ import print_function

def histogram(string):
    """creates dictionary with get method"""
    dvar = {}
    for char in string:
        dvar[char] = dvar.get(char, 0) + 1
    print(dvar)

histogram("brontosaurus")
