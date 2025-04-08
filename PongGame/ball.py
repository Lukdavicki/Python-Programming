# ball is projected from xcor = 0 and a random ycor with a random heading omitting 90 and 270(or 0 and 180 in logo mode)
# when ball collides with wall or paddle the heading is * -1 to reverse it
from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10

    def project_ball(self, i):
        new_x = self.xcor() + (self.x_move * i)
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # def project_ball_left(self):
    #     new_x = self.xcor() + self.x_move
    #     new_y = self.ycor() + self.y_move
    #     self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)