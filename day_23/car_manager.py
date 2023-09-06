from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        random_color = random.choice(COLORS)
        random_y = random.randint(-270, 270)
        self.shape("square")
        self.color(random_color)
        self.shapesize(stretch_len=2, stretch_wid=0.5)
        self.penup()
        self.goto(270, random_y)
        self.increment = 0

    def move(self):
        new_x = self.xcor() - (self.increment + STARTING_MOVE_DISTANCE)
        self.goto(new_x, self.ycor())

    def speedup(self):
        self.increment += MOVE_INCREMENT






