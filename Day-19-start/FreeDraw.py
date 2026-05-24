from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def turn_counterclockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
