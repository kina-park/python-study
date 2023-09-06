from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.start()
        self.time = 0.5

    def start(self):
        self.shape("turtle")
        self.setheading(90)
        self.speed(8)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def finish(self):
        return self.ycor() > FINISH_LINE_Y

    def set_time(self):
        self.time += 0.3
