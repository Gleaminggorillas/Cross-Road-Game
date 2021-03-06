from turtle import Turtle
import random


COLORS = ["red", "blue", "green", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_DISTANCE_INCREMENT = 10


class Cars:

    def __init__(self):
        self.all_cars = []
        self.level_increment = 0

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(280, random.randint(-250, +250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + (MOVE_DISTANCE_INCREMENT * self.level_increment))

    def reset_cars(self):
        self.level_increment += 1
