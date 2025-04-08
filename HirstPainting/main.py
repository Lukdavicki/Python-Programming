from turtle import Turtle
from turtle import Screen
import random
# import colorgram
#
# colors = colorgram.extract("hirst_painting.jpg", 30)
#
# # create a list containing a tuple for every color that is extracted from the img
# color_list = []
#
# for color in colors:
#     color_list.append(tuple(color.rgb))
#
# print(color_list)
color_list = [(2, 13, 31), (52, 25, 17), (216, 129, 108), (13, 106, 159), (240, 212, 71), (149, 84, 41), (213, 88, 65), (164, 161, 33), (157, 7, 26), (155, 63, 101), (95, 6, 19), (12, 62, 32), (205, 74, 104), (12, 96, 57), (174, 135, 160), (2, 63, 144), (9, 172, 214), (159, 30, 21), (6, 211, 205), (12, 138, 85), (146, 226, 215), (122, 191, 149), (220, 178, 214), (122, 176, 194), (102, 218, 228), (251, 197, 1)]
line_list = [(-400, -400), (-400, -300), (-400, -200), (-400, -100), (-400, 0), (-400, 100), (-400, 200), (-400, 300), (-400, 400), (-400, 500)]
t = Turtle()
s = Screen()
s.colormode(255)
t.speed("fastest")
t.hideturtle()
t.penup()
s.screensize(400, 400)
t.shape("circle")
t.shapesize(1)
t.pensize(20)
t.goto(-400, -500)


def draw_color():
    t.showturtle()
    t.pendown()
    random_color = random.randint(0, len(color_list) - 1)
    t.color(color_list[random_color])
    t.dot()
    t.penup()
    t.hideturtle()
    t.forward(90)


for i in range(10):

    for j in range(10):
        draw_color()
    t.goto(line_list[i])
    print(t.pos())


s.exitonclick()
