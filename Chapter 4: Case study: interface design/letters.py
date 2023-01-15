"""manually draws uppercase letters"""

from __future__ import division, print_function
from turtle import Turtle, Screen
import math

print("test")
class Dimensions():
    """sets width, height proportions"""
    def __init__(self):
        self.height = 300
        self.width = self.height * 0.6

    def get_width(self):
        """defines width"""
        return self.width

    def get_height(self):
        """defines height"""
        return self.height

turtle = Turtle()
screen = Screen()
prop = Dimensions()

# unit tests
def test(function):
    """runs function under location, size variable changes"""
    # original
    measure(prop.width, prop.height)
    function(prop.width, prop.height)
    # location test
    move(-(prop.width * 2), prop.height - prop.height)
    measure(prop.width, prop.height)
    function(prop.width, prop.height)
    # size test
    move(-(prop.width * 2), -(prop.height + 10))
    measure(150, 100)
    function(150, 100)
    # location, size test
    move(prop.width - prop.width, -(prop.height + 10))
    measure(70, 250)
    function(70, 250)

def move(xcor, ycor):
    """moves without drawing to coordinate"""
    turtle.pu()
    turtle.goto(xcor, ycor)
    turtle.pd()

def restart(xcor, ycor):
    """moves to original position, rotation"""
    move(xcor, ycor)
    turtle.setheading(0)

def measure(width, height):
    """draws proportions for letter functions"""
    turtle.setheading(0)
    for _ in range(2):
        turtle.fd(width)
        turtle.lt(90)
        turtle.fd(height)
        turtle.setheading(180)

# utilities
def distance(xcor1, xcor2, ycor1, ycor2):
    """computes distance formula for 2 sets of points"""
    dist = (((xcor2 - xcor1) ** 2) + ((ycor2 - ycor1) ** 2)) ** 0.5
    return dist

def midpointx(xcor1, xcor2):
    """computes x-midpoint for set of points"""
    mp_x = (xcor1 + xcor2) / 2
    return mp_x

def midpointy(ycor1, ycor2):
    """computes y-midpoint for set of points"""
    mp_y = (ycor1 + ycor2) / 2
    return mp_y

# structures
def arch(width, height):
    diag_length = distance(0, width / 2, 0, height)
    base_angle = math.asin(height / diag_length) * (180.0 / math.pi)
    top_angle = math.atan((width / 2.0) / height) * (180.0 / math.pi)
    turtle.setheading(base_angle)
    turtle.fd(diag_length)
    turtle.setheading(270 + top_angle)
    turtle.fd(diag_length)

def arc(radius, angle, ext):
    """draws arc with radius, angle"""
    arc_length = 2 * math.pi * radius * (abs(angle) / 360.0)
    steps = int(arc_length / 4) + 3
    step_length = arc_length / steps
    step_angle = float(angle) / steps
    turtle.fd(ext)
    turtle.rt(step_angle / 2.0)
    for _ in range(steps):
        turtle.fd(step_length)
        turtle.rt(step_angle)
    turtle.lt(step_angle / 2.0)
    turtle.fd(ext)

def ellipse(x_radius, y_radius, angle, pos):
    """draws ellipse with 2 radii"""
    startx, starty = turtle.xcor(), turtle.ycor()
    if angle > 180:
        move(startx + (x_radius * math.cos(pos * (math.pi / 180.0))) + x_radius,
             starty + (y_radius * math.sin(pos * (math.pi / 180.0))) + y_radius)
        for _ in range(angle):
            pos += 1
            turtle.goto((startx + x_radius * math.cos(pos * (math.pi / 180))) + x_radius,
                   (starty + y_radius * math.sin(pos * (math.pi / 180))) + y_radius)
    else:
        for _ in range(angle):
            pos -= 1
            turtle.goto(((x_radius * 2) * math.cos(pos * (math.pi / 180.0))) + startx,
            y_radius * math.sin(pos * (math.pi / 180.0)) + starty - y_radius)

def brackets(width, height, num_of):
    """draws basic 90-degree structure"""
    startx, starty = turtle.xcor(), turtle.ycor()
    if num_of < 2:
        if turtle.xcor() > (startx - width):
            turtle.setheading(180)
            move(startx, starty + (height / 2.0))
            turtle.fd(width)
        turtle.setheading(0)
        turtle.fd(width)
    else:
        turtle.setheading(90)
        turtle.fd(height)
        bracket_dist = height / 2.0
        bracket_ext = 0
        for action in range(num_of):
            if action == 1:
                bracket_ext = width * 0.1
            turtle.setheading(0)
            turtle.fd(width - bracket_ext)
            move(startx, starty + bracket_dist)
            bracket_dist -= bracket_dist

# letters
def draw_a(width, height):
    """draws uppercase A"""
    startx, starty = turtle.xcor(), turtle.ycor()
    midpoint_ltx = midpointx(0, width / 2)
    midpoint_lty = midpointy(0, height)
    midpoint_rtx = midpointx(width / 2, width)
    midpoint_rty = midpointy(height, 0)
    midpoint_dist = distance(midpoint_rtx, midpoint_ltx,
                             midpoint_rty, midpoint_lty)
    arch(width, height)
    move(startx + midpoint_ltx, starty + midpoint_lty)
    turtle.setheading(0)
    turtle.fd(midpoint_dist)
    restart(startx, starty)

def draw_b(width, height):
    """draws uppercase B"""
    startx, starty = turtle.xcor(), turtle.ycor()
    top_radius = (height / 2) * 0.45
    bottom_radius = (height / 2) * 0.55
    ext = abs(width - bottom_radius)
    turtle.setheading(90)
    turtle.fd(height)
    for _ in range(2):
        turtle.setheading(0)
        arc(top_radius, 180, ext)
        top_radius = bottom_radius
    restart(startx, starty)

def draw_c(width, height):
    """draws uppercase C"""
    startx = turtle.xcor()
    starty = turtle.ycor()
    dist_adjust = width - ((((width / 2) * math.cos(30 * (math.pi / 180.0)) + (width / 2)) ** 2) ** 0.5)
    width_adj = 1 + (dist_adjust / width)
    ellipse((width / 2.0) * width_adj, height / 2.0, 300, 30)
    restart(startx, starty)

def draw_d(width, height):
    """draws uppercase D"""
    startx, starty = turtle.xcor(), turtle.ycor()
    turtle.setheading(90)
    turtle.fd(height)
    ellipse(width / 2, height / 2, 180, 90)
    restart(startx, starty)

def draw_e(width, height):
    """draws uppercase E"""
    startx, starty = turtle.xcor(), turtle.ycor()
    brackets(width, height, 3)
    restart(startx, starty)

def draw_f(width, height):
    """draws uppercase F"""
    startx, starty = turtle.xcor(), turtle.ycor()
    brackets(width, height, 2)
    restart(startx, starty)

def draw_g(width, height):
    """draws uppercase G"""
    startx, starty = turtle.xcor(), turtle.ycor()
    dist_adjust = width - ((((width / 2) * math.cos(30 * (math.pi / 180.0)) + (width / 2)) ** 2) ** 0.5)
    width_adj = 1 + (dist_adjust / width)
    ellipse((width / 2.0) * width_adj, height / 2.0, 300, 30)
    currenty = turtle.ycor()
    turtle.setheading(90)
    turtle.fd(starty + (height / 2.0) - currenty)
    turtle.setheading(180)
    turtle.fd(width * 0.3)
    restart(startx, starty)

def draw_h(width, height):
    """draws uppercase H"""
    startx, starty = turtle.xcor(), turtle.ycor()
    move(startx, starty + height)
    turtle.setheading(270)
    turtle.fd(height)
    move(startx + width, starty + height)
    turtle.fd(height)
    brackets(width, height, 1)
    restart(startx, starty)

def draw_i(width, height):
    """draws uppercase I"""
    startx, starty = turtle.xcor(), turtle.ycor()
    move(startx + (width / 2.0), starty)
    turtle.setheading(90)
    turtle.fd(height)
    restart(startx, starty)

def draw_j(width, height):
    """draws uppercase J"""
    startx, starty = turtle.xcor(), turtle.ycor()
    radius = width / 2.0
    move(startx + width, starty + height)
    turtle.setheading(270)
    turtle.fd(height - radius)
    arc(radius, 180, 0)
    restart(startx, starty)

def draw_k(width, height):
    """draws uppercase K"""
    startx, starty = turtle.xcor(), turtle.ycor()
    top_diag = distance(0, width, height * 0.4, height)
    top_angle = math.atan((height * 0.6) / width) * (180.0 / math.pi)
    tan_opp = (height / 2.0) - (height * 0.4)
    bottom_xcor = tan_opp / math.tan(top_angle * (math.pi / 180.0))
    bottom_angle = math.atan((height / 2) / (width - bottom_xcor)) \
                   * (180.0 / math.pi)
    bottom_diag = distance(startx + width, startx + bottom_xcor, starty, starty + (height / 2.0))
    turtle.setheading(90)
    turtle.fd(height)
    move(startx, starty + (height * 0.4))
    turtle.setheading(0)
    turtle.lt(top_angle)
    turtle.fd(top_diag)
    move(startx + bottom_xcor, starty + (height / 2.0))
    turtle.setheading(0 - bottom_angle)
    turtle.fd(bottom_diag)
    restart(startx, starty)

def draw_l(width, height):
    """draws uppercase L"""
    startx, starty = turtle.xcor(), turtle.ycor()
    move(startx, starty + height)
    turtle.setheading(270)
    turtle.fd(height)
    turtle.setheading(0)
    turtle.fd(width)
    restart(startx, starty)

def draw_m(width, height):
    """draws uppercase M"""
    startx, starty = turtle.xcor(), turtle.ycor()
    arch(width / 2.0, height)
    arch(width / 2.0, height)
    restart(startx, starty)

def draw_n(width, height):
    """draws uppercase N"""
    startx, starty = turtle.xcor(), turtle.ycor()
    diag_length = distance(startx, startx + width, starty, starty + height)
    top_angle = math.atan(width / height) * (180.0 / math.pi)
    turtle.setheading(90)
    turtle.fd(height)
    turtle.setheading(270 + top_angle)
    turtle.fd(diag_length)
    turtle.setheading(90)
    turtle.fd(height)
    restart(startx, starty)

def draw_o(width, height):
    """draws uppercase O"""
    startx, starty = turtle.xcor(), turtle.ycor()
    ellipse(width / 2.0, height / 2.0, 360, 90)
    restart(startx, starty)

def draw_p(width, height):
    """draws uppercase P"""
    startx, starty = turtle.xcor(), turtle.ycor()
    radius = (height / 2.0) * 0.5
    ext = width - radius
    turtle.setheading(90)
    turtle.fd(height)
    turtle.setheading(0)
    arc(radius, 180, ext)
    restart(startx, starty)

# def draw_q(width, height):
#     """draws uppercase Q"""
#     startx, starty = turtle.xcor(), turtle.ycor()
#     restart(startx, starty)

def draw_r(width, height):
    """draws uppercase R"""
    startx, starty = turtle.xcor(), turtle.ycor()
    radius = (height / 2.0) * 0.5
    ext = width - radius
    diag_angle = math.atan((height / 2.0) / (width - ext)) * (180.0 / math.pi)
    diag_length = distance(startx + ext, startx + width, starty + (height / 2.0), starty)
    turtle.setheading(90)
    turtle.fd(height)
    turtle.setheading(0)
    arc(radius, 180, ext)
    turtle.bk(ext)
    turtle.setheading(0 - diag_angle)
    turtle.fd(diag_length)
    restart(startx, starty)

# def draw_s(width, height):
#     """draws uppercase S"""
#     startx, starty = turtle.xcor(), turtle.ycor()
#     restart(startx, starty)

def draw_t(width, height):
    """draws uppercase T"""
    startx, starty = turtle.xcor(), turtle.ycor()
    move(startx + (width / 2.0), starty + height)
    turtle.setheading(270)
    turtle.fd(height)
    move(startx + width, starty + height)
    turtle.setheading(180)
    turtle.fd(width)
    restart(startx, starty)

def draw_u(width, height):
    """draws uppercase U"""
    startx, starty = turtle.xcor(), turtle.ycor()
    radius = width / 2.0
    ext = height - radius
    move(startx + width, starty + height)
    turtle.setheading(270)
    arc(radius, 180, ext)
    restart(startx, starty)

# def draw_v(width, height):
#     startx, starty = turtle.xcor(), turtle.ycor()
#     restart(startx, starty)

# def draw_w(width, height):
#     startx, starty = turtle.xcor(), turtle.ycor()
#     restart(startx, starty)

# def draw_x(width, height):
#     startx, starty = turtle.xcor(), turtle.ycor()
#     restart(startx, starty)

# def draw_y(width, height):
#     startx, starty = turtle.xcor(), turtle.ycor()
#     restart(startx, starty)

# def draw_z(width, height):
#     startx, starty = turtle.xcor(), turtle.ycor()
#     restart(startx, starty)

test(draw_u)

screen.exitonclick()
