"""draws ASCII grid through refactoring"""

from __future__ import division, print_function

def do_twice(func):
    """repeats function twice"""
    func()
    func()

def do_four(func):
    """repeats function four times"""
    do_twice(func)
    do_twice(func)

def one_four_one(func, gfunc, hfunc):
    """outputs function once, four times, once again"""
    func()
    do_four(gfunc)
    hfunc()

def print_plus():
    """prints + symbol for beam
    corner for grid"""
    print('+', end=' ')

def print_dash():
    """prints - symbol for row"""
    print('-', end=' ')

def print_bar():
    """prints | symbol for post"""
    print('|', end=' ')

def print_space():
    """sets space between posts in grid"""
    print(' ', end=' ')

def print_end():
    """sets new line after row"""
    print()

def nothing():
    """does nothing
    placeholder function if only two inputs required for one_four_one"""

def print1beam():
    """prints one beam"""
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    """prints one post"""
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    """prints four beams, sets new line"""
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    """prints four posts, sets new line"""
    one_four_one(print_bar, print1post, print_end)

def print_row():
    """prints row"""
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    """prints full ASCII grid"""
    one_four_one(print4beams, print_row, nothing)

print_grid()
