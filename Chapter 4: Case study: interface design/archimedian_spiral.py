"""Archimedean spiral based on general approximation formula"""

from __future__ import division, print_function
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def draw_spiral(length, steps):
    """draws Archimedean spiral"""
    start_dist = .1
    turn_dist = .0002
    angle = 0.0
    for _ in range(steps):
        turtle.fd(length)
        d_angle = 1 / (start_dist + turn_dist * angle)
        turtle.lt(d_angle)
        angle += d_angle

draw_spiral(3, 1000)

screen.exitonclick()
