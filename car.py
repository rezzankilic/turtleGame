import random
from turtle import Turtle

COLORS = ["blue", "yellow", "black", "aquamarine", "coral", "brown4", "DeepPink", "gold", "magenta"]
STARTING_MOVE_DISTANCE = 5
INCREASE_IN_MOVE = 10


class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_change = random.randint(1, 6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=0.7, stretch_len=2)
            new_car.color(random.choice(COLORS))

            random_y = random.randint(-190, 190)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREASE_IN_MOVE
