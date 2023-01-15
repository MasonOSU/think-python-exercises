"""print statements for stack diagram of recursion function"""

def recurse(current, base):
    """counts down current while adding current value to base until current is zero
    reaches maximum excursion depth if current less than zero"""
    if current == 0:
        print("current: " + str(current) + " | base: " + str(base))
    else:
        print("current: " + str(current) + " | base: " + str(base))
        recurse(current - 1, current + base)

recurse(3, 0)
