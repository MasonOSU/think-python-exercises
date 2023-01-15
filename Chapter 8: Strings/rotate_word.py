"""rotates words for Caesar cypher"""

from __future__ import print_function

def rotate_word(string, rot):
    """encrypts a string given a number of rotations"""
    string = string.lower()
    new_string = ""
    for char in string:
        dig_char = ord(char) + rot
        if dig_char > 122:
            dig_char -= 26
        rot_char = chr(dig_char)
        new_string += rot_char
    new_string = new_string.replace("-", " ")
    return new_string

print("how do you make a hot dog stand?", rotate_word("Fgrny vgf punve", 13))
print("what do you hold without touching?", rotate_word("N pbairefngvba", 13))
