"""memoizes Ackermann function from earlier"""

from __future__ import print_function

known = {(0,0):1, (0,1):2, (1,1):3, (1,2):4, (2,2):7, (2,3):9, (3,3):61, (3,4):125}

def ackermann(mvar, nvar):
    """computes Ackermann function"""
    if (mvar, nvar) in known:
        return known[(mvar, nvar)]
    if mvar == 0:
        return nvar + 1
    if nvar == 0:
        return ackermann(mvar - 1, 1)
    return ackermann(mvar - 1, ackermann(mvar, nvar - 1))

print(ackermann(3, 4))
