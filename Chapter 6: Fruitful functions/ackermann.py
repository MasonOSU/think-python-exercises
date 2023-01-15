"""recursion with base case for Ackermann function"""

from __future__ import print_function

def ack(mvar, nvar):
    """computes Ackermann function"""
    if mvar == 0:
        return nvar + 1
    if nvar == 0:
        return ack(mvar - 1, 1)
    return ack(mvar - 1, ack(mvar, nvar - 1))

print(ack(3, 4))
