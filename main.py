from turtle import Screen
from playerturtle import PlayerTurtle
import time
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()

screen.title("Cross Road Game")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

car = Cars()

player = PlayerTurtle()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

#   move cars
    car.create_cars()
    car.move()

    scoreboard.update_scoreboard()

#   detect car collision
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

#   detect level up and reset
    if player.ycor() > 250:
        scoreboard.increase_level()
        player.reset()
        car.reset()

screen.exitonclick()
