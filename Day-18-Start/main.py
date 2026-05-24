import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for i in range(400):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()


# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     tim.right(angle)
#     tim.fd(steps)
# # tim.screen.mainloop()
# tim.screen.title('Object-oriented turtle demo')
# tim.screen.bgcolor("orange")

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# with tim.fill():
#     for i in range(4):
#         tim.forward(100)
#         tim.right(90)
#
# tim.forward(200)






#
# screen = Screen()
# screen.exitonclick()