"""text-provided function"""

from __future__ import print_function
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def draw(length, steps):
    """draws beginning of Koch curve"""
    if steps == 0:
        return
    angle = 50
    turtle.forward(length * steps)
    turtle.left(angle)
    draw(length, steps - 1)
    turtle.right(2 * angle)
    draw(length, steps - 1)
    turtle.left(angle)
    turtle.bk(length * steps)

draw(10, 3)

screen.exitonclick()
