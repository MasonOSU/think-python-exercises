"""right-aligns text"""

from __future__ import print_function

def right_justify(string):
    """adjusts last character of string to column 70"""
    spaces = " "
    rt_side = 70 - len(string)
    new_string = str((spaces * rt_side) + string)
    print(new_string)

right_justify("test")
right_justify("test again")
