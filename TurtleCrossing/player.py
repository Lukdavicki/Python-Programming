from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# //turtle moves forward when pressed "Up" key. It can only move forward and not able to move left, right or backward

# //when the turtle hits the top edge it moves back the starting position and player levels up. on the next level the
# car sped increases.

# //when turtle collides with car its game over and everything stops.


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)

