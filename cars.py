from turtle import Turtle
import random


COLORS = ["red", "blue", "green", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_DISTANCE_INCREMENT = 10


class Cars:

    def __init__(self):
        self.all_cars = []
        #self.x_move = -STARTING_MOVE_DISTANCE

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
            car.backward(STARTING_MOVE_DISTANCE)
            #new_x = self.xcor()+self.x_move
            #self.goto(new_x, self.ycor())

    def reset(self):
        new_x_move = self.x_move - MOVE_DISTANCE_INCREMENT
        self.x_move = new_x_move
