from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
ball = Ball()
score = ScoreBoard()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.project_ball(1)
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.distance(r_paddle) > 50 and ball.xcor() > 400:
        score.l_point()
        ball.reset_ball()
        ball.project_ball(1)
    if ball.distance(l_paddle) > 50 and ball.xcor() < -400:
        score.r_point()
        ball.reset_ball()
        ball.project_ball(-1)


screen.exitonclick()

# //check why the PLayer Paddle is always returning to the -600,0 position

# figure out the proper start sequence for the paddle and ball functions, so they will work one after another and the
# ball will project after the CPu paddle will start moving and the user gets the  controls ON
