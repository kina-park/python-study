import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]
tim.pensize()
tim.speed("fastest")


def spiral(n):
    for _ in range(int(360/n)):
        tim.pencolor(random_color())
        tim.circle(30)
        tim.right(n)
    # tim.setheading(random.choice(directions))

spiral(10)