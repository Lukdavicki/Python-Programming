from turtle import Turtle, Screen

t = Turtle()
s = Screen()
# w forwards
# s backwards
# a cointer clockwise
# d clockwise
# c clear and reset position


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_clockwise():
    t.right(10)


def move_counterclockwise():
    t.left(10)


def reset_canvas():
    t.reset()


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=move_counterclockwise)
s.onkey(key="d", fun=move_clockwise)
s.onkey(key="c", fun=reset_canvas)

s.exitonclick()

