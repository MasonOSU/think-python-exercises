"""stack diagram (print statements) for circle"""

from __future__ import print_function, division
from turtle import Turtle, Screen
import math

turtle = Turtle()
screen = Screen()

def circle(radius):
    """draws circle with given radius"""
    print("2. arc call")
    arc(radius, 360)

def arc(radius, angle):
    """Draws arc with given radius and angle
    print statements are stack diagram"""
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    steps = int(arc_length / 4) + 3
    step_length = arc_length / steps
    step_angle = float(angle) / steps
    turtle.lt(step_angle/2)
    print("3. step_angle calc")
    polyline(steps, step_length, step_angle)
    turtle.rt(step_angle / 2)

def polyline(steps, length, angle):
    """draws line segments"""
    print("4. polyline for loop")
    for _ in range(steps):
        turtle.fd(length)
        turtle.lt(angle)

if __name__ == '__main__':
    # draws circle centered on origin
    # checks if script or import
    print("1. first call")
    RADIUS = 100
    turtle.pu()
    turtle.fd(RADIUS)
    turtle.lt(90)
    turtle.pd()
    circle(RADIUS)

    screen.exitonclick()
