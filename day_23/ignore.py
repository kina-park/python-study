from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("turtle_crossing_game")

# 애니메이션 끄기
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

car_list = []

game_is_on = True
while game_is_on:
    time.sleep(player.time)
    screen.update()  # 여기서 짜잔하고 모두 다켜짐
    new_car = CarManager()
    car_list.append(new_car)
    for car in car_list:
        car.move()
        print(player.distance(car))

screen.exitonclick()

