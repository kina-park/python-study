from turtle import Turtle


class Paddle:

    def __init__(self, paddle_position):
        self.paddle = Turtle()
        self.paddle_position = paddle_position
        self.create_paddle()

    def create_paddle(self):
        self.paddle.penup()
        self.paddle.goto(self.paddle_position)
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
