"""draws turtle pies"""

from __future__ import division, print_function
import turtle
import math

# def draw_pie(tdraw, num, radius):

# def polypie(tdraw, num, radius):

def tri(tdraw, radius):
    """draws isosceles triangle"""
    atop =

    tdraw.fd(radius)
    tdraw.lt(45)
    tdraw.fd(50)
    tdraw.lt(45)
    tdraw.fd(radius)


if __name__ == "__main__":
    draw = turtle.Turtle()

    # draw polypies with various number of sides
    # size = 40
    # draw_pie(draw, 5, size)
    # draw_pie(draw, 6, size)
    # draw_pie(draw, 7, size)
    # draw_pie(draw, 8, size)

    tri(draw, 100)

    draw.hideturtle()
    turtle.mainloop()




# def finish(tris, angle, length):
#     """finishes outer boundaries of turtle pies"""
#     base_angle = 90 - (angle / 2)
#     outer_length = math.sin(math.radians(angle / 2.0)) * length * 2
#     turtle.lt(angle)
#     turtle.fd(length)
#     turtle.rt(180 - base_angle)
#     for _ in range(tris):
#         turtle.fd(outer_length)
#         turtle.rt(angle)
#
# def outline(tris, angle, length):
#     """draws inner outline of all turtle pies"""
#     origin = turtle.pos()
#     for _ in range(tris):
#         turtle.lt(angle)
#         turtle.fd(length)
#         turtle.goto(origin)
#
# def move(xcor, tris):
#     """moves to area on graph"""
#     turtle.pu()
#     turtle.goto(xcor, 200)
#     turtle.pd()
#     turtle_pies(tris)
#
# move(0, 5)
# move(150, 6)
# move(300, 7)
