from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-120, 250)
        self.load_score()
        self.hideturtle()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.load_score()

    def gameover(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
        self.hideturtle()

    def load_score(self):
        self.write(f"Level: {self.level}", align="right", font=FONT)
