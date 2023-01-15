"""stack diagram with print functions"""

from __future__ import print_function

def bfunc(zvar):
    """outputs cfunc total, afunc product"""
    print("cfunc zvar called to bfunc, squared from afunc", zvar)
    prod = afunc(zvar, zvar)
    print("prod from afunc:", "\n     ",
          "zvar (9 + 1) * zvar (9) ->", prod)
    return prod

def afunc(xvar, yvar):
    """outputs cfunc total, duplicate plus one"""
    print("xvar called as zvar (9) from bfunc ->", xvar)
    xvar = xvar + 1
    print("xvar called as zvar + 1 ->", xvar)
    return xvar * yvar

def cfunc(xvar, yvar, zvar):
    """sums total of xvar, yvar, zvar and squares afunc product."""
    print("totaling...")
    total = xvar + yvar + zvar
    print("cfunc total: ", "\n     ",
          "xvar (reassigned to 1), ->", xvar, "\n     ",
          "yvar (xvar + 1 + 3 in function call) ->", yvar, "\n     ",
          "zvar (original xvar + original yvar) ->", zvar, "\n     ",
          "total ->", total)
    square = bfunc(total) ** 2
    print("square from cfunc:", "\n     ",
          "90 squared ->", square)
    return square

XVAR = 1
print("xvar reassignment to 1 ->", XVAR)
YVAR = XVAR + 1
print("yvar reassignment to 2->", YVAR)
print("final output ->", cfunc(XVAR, YVAR + 3, XVAR + YVAR))
