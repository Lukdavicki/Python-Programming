from turtle import Turtle

LINE_COR = [300, 250, 200, 250, 150, 100, 50, 0, -50, -100, -150, -200, -250, -300]


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(0.75)


