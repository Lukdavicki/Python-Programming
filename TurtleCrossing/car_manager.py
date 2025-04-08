from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# //cars are randomly generated on the Y-axis and will move from the right edge to the left edge


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_generator()

    def car_generator(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def car_movement(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def car_movement_increase(self):
        self.car_speed += MOVE_INCREMENT

