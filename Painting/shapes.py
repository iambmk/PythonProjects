import turtle as t
import random

tim = t.Turtle()

colors = ["red", "CornflowerBlue", "DarkOrchid", "green", "blue", "yellow", "cyan", "magenta"]


def draw_shape(num_sides):
    angel = (360 / sides)
    for side in range(sides):
        tim.forward(100)
        tim.right(angel)

for sides in range(3 , 11):
    tim.color(random.choice(colors))
    draw_shape(sides)

screen = t.Screen()
screen.exitonclick()
