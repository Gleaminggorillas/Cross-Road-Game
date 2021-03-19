from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.goto(0, 255)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"level = {self.level}",
                   align=ALIGNMENT,
                   font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()
