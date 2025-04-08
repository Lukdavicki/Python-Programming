import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# screen.mode("logo")
screen.listen()
score = Scoreboard()
turtle = Player()
screen.onkey(turtle.move, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.show_score()
    car_manager.car_generator()
    car_manager.car_movement()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.reset_turtle()
        score.level_update()
        car_manager.car_movement_increase()


screen.exitonclick()
