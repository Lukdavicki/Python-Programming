import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle_pos = t.position()
# t.penup()
# t.goto(-500, 0)
# t.pendown()
# print(t.position())
# for _ in range(50):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()
# /////
# def draw_shapes(number_sides):
#     angle = 360 / number_sides
#     for _ in range(number_sides):
#
#         t.forward(100)
#         t.right(angle)
#
# for shape_side_n in range(3,11):
#     draw_shapes(shape_side_n)

# ////
turtle.colormode(255)
#
#


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r,g,b)
    return color_tuple
#
# direction = [0, 90, 180, 270]
# t.pensize(10)
# for _ in range(200):
#     t.pencolor(random_color())
#     t.forward(20)
#     t.setheading(random.choice(direction))


t.speed("fastest")


for _ in range(72):
    t.pencolor(random_color())
    t.circle(100)
    t.right(5)
screen = Screen()
screen.exitonclick()
