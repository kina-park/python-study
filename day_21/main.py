from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# 화면 세팅
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head_snake.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head_snake.xcor() > 280 or snake.head_snake.xcor() < -280 or snake.head_snake.ycor() > 280 or snake.head_snake.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head_snake.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# 클릭하여 화면 종료
screen.exitonclick()



# 뱀 몸통 만들기
# pos = 0
# for i in range(3):
#     turtle = Turtle(shape="square")
#     turtle.color("white")
#     turtle.setpos(pos, 0)
#     pos += 20
