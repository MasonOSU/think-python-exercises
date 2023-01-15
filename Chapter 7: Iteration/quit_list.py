"""iteratively calls function until user enters 'done'"""

from __future__ import print_function
from ast import literal_eval

def eval_loop():
    """prints, builds list
    outputs final element when finished"""
    lst = []
    expression = str(input("enter an expression: "))
    while expression != "done":
        lst.append(literal_eval(expression))
        print(lst)
        expression = str(input("enter an expression: "))
    print(lst[-1])

eval_loop()
