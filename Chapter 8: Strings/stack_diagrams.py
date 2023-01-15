"""text-given functions to determine lowercase characters in strings"""

def any_lowercase1(string):
    """incorrectly returns False if any uppercase"""
    for char in string:
        return char.islower()

def any_lowercase2(string):
    """incorrectly returns True for all uppercase
    ignore pylint error, intentional"""
    for char in string:
        return 'char'.islower()

def any_lowercase3(string):
    """correctly assigns lowercase character iteration to flag"""
    flag = 0
    for char in string:
        flag = char.islower()
    return flag

def any_lowercase4(string):
    """correctly assigns flag, checks lowercase characters"""
    flag = False
    for char in string:
        flag = flag or char.islower()
    return flag

def any_lowercase5(string):
    """incorrectly returns False for all if any character uppercase"""
    for char in string:
        if not char.islower():
            return False
    return True

print("func1, correct:", any_lowercase1("banana"))
print("func1, wrong:  ", any_lowercase1("Banana"))
print("func1, correct:", any_lowercase1("BANANA"))

print("func2, correct:", any_lowercase2("banana"))
print("func2, correct:", any_lowercase2("Banana"))
print("func2, wrong   ", any_lowercase2("BANANA"))

print("func3, correct:", any_lowercase3("banana"))
print("func3, correct:", any_lowercase3("Banana"))
print("func3, correct:", any_lowercase3("BANANA"))

print("func4, correct:", any_lowercase4("banana"))
print("func4, correct:", any_lowercase4("Banana"))
print("func4, correct:", any_lowercase4("BANANA"))

print("func5, correct:", any_lowercase5("banana"))
print("func5, correct:", any_lowercase5("Banana"))
print("func5, correct:", any_lowercase5("BANANA"))
