"""text-provided code for import"""

from __future__ import print_function, division

import math
import turtle

def square(tdraw, length):
    """turtles square with sides of given length
    returns Turtle to starting position and location"""
    for _ in range(4):
        tdraw.fd(length)
        tdraw.lt(90)

def polyline(tdraw, num, length, angle):
    """turtles num line segments"""
    for _ in range(num):
        tdraw.fd(length)
        tdraw.lt(angle)

def polygon(tdraw, num, length):
    """turtles polygon with num sides."""
    angle = 360.0 / num
    polyline(tdraw, num, length, angle)

def arc(tdraw, radius, angle):
    """turtles arc with given radius and angle"""
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    num = int(arc_length / 4) + 3
    step_length = arc_length / num
    step_angle = float(angle) / num

    # reduce linear approximation error
    tdraw.lt(step_angle / 2)
    polyline(tdraw, num, step_length, step_angle)
    tdraw.rt(step_angle / 2)

def circle(tdraw, radius):
    """turtles circle with given radius"""
    arc(tdraw, radius, 360)

# checks if running as script
# runs test code if so
# doesn't if imported
if __name__ == "__main__":
    draw = turtle.Turtle()

    # turtles circle centered on origin
    RADIUS = 100
    draw.pu()
    draw.fd(RADIUS)
    draw.lt(90)
    draw.pd()
    circle(draw, RADIUS)

    # waits for user to close window
    turtle.mainloop()
