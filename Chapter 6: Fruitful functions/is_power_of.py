"""checks if one number is a power of another"""

from __future__ import print_function

def is_power(num1, num2):
    """returns True if num1 a power of num2"""
    if num1 == 1:
        return num2 == 1
    power = 1
    while power < num2:
        power = power * num1
    return power == num2

print(is_power(5, 125))
print(is_power(10, 1000))
print(is_power(4, 1))
print(is_power(1, 2))
