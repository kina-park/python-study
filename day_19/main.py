from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()

screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# 스페이스키가 눌리면, 함수 move_forwards()를 실행한다
## Function as Inputs / Higher Order Functions(고차함수): 다른 함수와 함께 작동하는 함수
# 함수를 인수로 사용할 때, 즉, 함수를 다른 함수에 전달할 때에는 끝에 괄호를 사용하지 않음.
# fun = move_forwards (o), fun = move_forwards (x)

# w키 - 앞으로 이동, s키 - 뒤로 이동,
# a키 - 시계반대방향 회전, d키 - 시계방향(오른쪽) 회전
# c키 - 그림 지우기, 터틀 중앙 위치로

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)

def clockwise():
    tim.right(10)
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
def reset():
    screen.reset()

screen.onkey(key= "w", fun= move_forwards)
screen.onkey(key= "s", fun= move_backwards)
screen.onkey(key= "a", fun= counter_clockwise)
screen.onkey(key= "d", fun= clockwise)
screen.onkey(key= "c", fun= reset)

screen.exitonclick()


