"""estimates pi with Ramanujan formula using an infinite series"""

from __future__ import division, print_function
import math

def estimate_pi():
    """computes Ramanujan formula"""
    def factorial(num):
        products = range(1, num)
        output = 1
        while output <= num:
            if num > 0:
                for ele in products:
                    output *= (ele + 1)
                return output
        if num == 0:
            output = 1
            return output
        return "error, must be zero or greater"

    def summation():
        total = 0
        lst_results = []
        seq = 0
        result = ((factorial(4 * seq)) / (factorial(seq) ** 4)) \
                 * ((1103 + (26390 * seq)) / (396 ** (4 * seq)))
        lst_results.append(result)
        while result > 1e-15:
            seq += 1
            result = ((factorial(4 * seq)) / (factorial(seq) ** 4)) \
                     * ((1103 + (26390 * seq)) / (396 ** (4 * seq)))
            lst_results.append(result)
        for num in enumerate(lst_results):
            total += num[1]
            return 1.0 / (((2.0 * (2.0 ** 0.5)) / 9801.0) * total)

    summation()

    print ("est:  " + str(summation()) + "\n"
           "calc: " + str(math.pi))

estimate_pi()
