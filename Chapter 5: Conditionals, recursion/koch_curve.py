"""draws snowflake outline with Koch curve function"""

from __future__ import print_function
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def snowflake(tdraw, length):
    """draws outline of snowflake"""
    for _ in range(3):
        koch(turtle, length)
        tdraw.rt(120)

def koch(tdraw, length):
    """draws Koch curve
    size determines turns, complexity
    higher size is smaller snowflake"""
    if length < 10:
        tdraw.fd(length)
        return
    size = length / 3
    koch(tdraw, size)
    tdraw.lt(60)
    koch(tdraw, size)
    tdraw.rt(120)
    koch(tdraw, size)
    tdraw.lt(60)
    koch(tdraw, size)

if __name__ == "__main__":
    turtle.pu()
    turtle.goto(-150, 90)
    turtle.pd()
    snowflake(turtle, 300)

    screen.exitonclick()
