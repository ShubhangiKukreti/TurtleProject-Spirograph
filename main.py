from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")


def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(200):
    colour = random_colours()
    tim.color(colour)
    tim.circle(100)
    tim.right(5)
    tim.tilt(200)


screen.exitonclick()
