from turtle import Turtle
FONT = ('Courier', 20, 'normal')


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.goto(position)
        self.color("white")
        self.hideturtle()
        self.load_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.load_score()

    def load_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)




