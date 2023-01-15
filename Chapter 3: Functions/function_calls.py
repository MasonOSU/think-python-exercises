"""function calls to limit redundant code"""

from __future__ import print_function

def do_twice(function):
    """text-given function to repeat function call twice using parameter"""
    function()
    function()

def print_spam():
    """text-given function to print string"""
    print("text example:", "spam")

do_twice(print_spam)

def print_twice(arg):
    """text-given function testing do_twice_mod"""
    print("modified example at first iteration:", arg)
    print("modified example at second iteration:", arg)

def do_twice_mod(function, val):
    """calls function twice, passing value as argument"""
    function(val)
    function(val)

do_twice_mod(print_twice, "spam two")

def do_four(function, val):
    """calls print_twice four times using two statements"""
    do_twice_mod(function, val)
    do_twice_mod(function, val)

do_four(print_twice, "spam three")
