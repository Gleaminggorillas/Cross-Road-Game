from turtle import Turtle
import random


COLORS = ["red", "blue", "green", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_DISTANCE_INCREMENT = 10


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(560, random.randint(-250, +250))
        self.x_move = -STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor()+self.x_move
        self.goto(new_x, self.ycor())

    def reset(self):
        new_x_move = self.x_move - MOVE_DISTANCE_INCREMENT
        self.x_move = new_x_move
