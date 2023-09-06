from turtle import Turtle

# 상수
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head_snake = self.segments[0]
        self.tail_snake = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head_snake = self.segments[0]

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.tail_snake.position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head_snake.forward(MOVE_DISTANCE)

    def up(self):
        if self.head_snake.heading() != DOWN:
            self.head_snake.setheading(UP)

    def down(self):
        if self.head_snake.heading() != UP:
            self.head_snake.setheading(DOWN)

    def left(self):
        if self.head_snake.heading() != RIGHT:
            self.head_snake.setheading(LEFT)

    def right(self):
        if self.head_snake.heading() != LEFT:
            self.head_snake.setheading(RIGHT)
