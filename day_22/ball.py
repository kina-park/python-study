
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_up = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_up *= 0.7

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed_up = 0.1

    # def north_collision(self):
    #     random_x = [self.xcor() + 10, self.xcor() - 10]
    #     new_x = random.choice(random_x)
    #     new_y = self.ycor() - 10
    #     if -390 < new_x < 390 and -280 < new_y < 280:
    #         self.goto(new_x, new_y)
    #
    # def south_collision(self):
    #     random_x = [self.xcor() + 10, self.xcor() - 10]
    #     new_x = random.choice(random_x)
    #     new_y = self.ycor() + 10
    #     if -390 < new_x < 390 and -280 < new_y < 280:
    #         self.goto(new_x, new_y)
    #
    # def west_collision(self):
    #     random_y = [self.ycor() + 10, self.ycor() - 10]
    #     new_x = self.xcor() + 10
    #     new_y = random.choice(random_y)
    #     if -390 < new_x < 390 and -280 < new_y < 280:
    #         self.goto(new_x, new_y)
    #
    # def east_collision(self):
    #     random_y = [self.ycor() + 10, self.ycor() - 10]
    #     new_x = self.xcor() - 10
    #     new_y = random.choice(random_y)
    #     if -390 < new_x < 390 and -280 < new_y < 280:
    #         self.goto(new_x, new_y)





