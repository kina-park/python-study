# from turtle import Turtle
#
#
# class Paddle(Turtle):
#
#     def __init__(self, paddle_position):
#         super().__init__()
#         self.paddle_position = paddle_position # self.create_paddle() 이전에 코드 작성하기!!!
#         self.paddle = self.create_paddle()
#
#     def create_paddle(self):
#         self.penup()
#         self.goto(self.paddle_position)
#         self.shape("square")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.color("white")
#         return self
#
#     def go_up(self):
#         new_y = self.paddle.ycor() + 20
#         self.paddle.goto(self.paddle.xcor(), new_y)
#
#     def go_down(self):
#         new_y = self.paddle.ycor() - 20
#         self.paddle.goto(self.paddle.xcor(), new_y)

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
