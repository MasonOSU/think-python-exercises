"""turtles flowers with refactoring"""

from __future__ import division, print_function
import turtle
from polygon import arc

def petal(tdraw, radius, angle):
    """turtles petal using two arcs"""
    for _ in range(2):
        arc(tdraw, radius, angle)
        tdraw.lt(180 - angle)

def flower(tdraw, steps, radius, angle):
    """turtles flower with number of petals"""
    for _ in range(steps):
        petal(tdraw, radius, angle)
        tdraw.lt(360.0 / steps)

def move(tdraw, length):
    """moves Turtle forward (length) units without leaving trail, leaves pen down"""
    tdraw.pu()
    tdraw.fd(length)
    tdraw.pd()



if __name__ == "__main__":
    draw = turtle.Turtle()

    # draws three flowers from book
    move(draw, -200)
    flower(draw, 7, 60.0, 60.0)

    move(draw, 200)
    flower(draw, 10, 40.0, 80.0)

    move(draw, 200)
    flower(draw, 20, 140.0, 20.0)

    draw.hideturtle()
    turtle.mainloop()
