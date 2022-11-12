from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("triangle")

tim.speed("fastest")
def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_counter():
    tim.left(10)


def rotate_clock():
    tim.right(10)


def clear():
    tim.clear()


def penup():
    tim.penup()


def pendown():
    tim.pendown()


def set_red():
    tim.pencolor("red")


def set_blue():
    tim.pencolor("blue")


def move_up():
    tim.setheading(90)
    tim.forward(10)


def move_down():
    tim.setheading(270)
    tim.forward(10)


def move_right():
    tim.setheading(0)
    tim.forward(10)


def move_left():
    tim.setheading(180)
    tim.forward(10)


def setgreen():
    tim.pencolor("green")


def makedot():
    tim.dot()


screen.listen()

screen.onkey(move_forward, key="w")
screen.onkey(move_backward, key="s")
screen.onkey(rotate_counter, key="a")
screen.onkey(rotate_clock, key="d")
screen.onkey(clear, key="c")
screen.onkey(penup, key="u")
screen.onkey(pendown, key="v")
screen.onkey(set_red, key="r")
screen.onkey(setgreen, key="g")
screen.onkey(set_blue, key="b")
screen.onkey(move_right, key="l")
screen.onkey(move_left, key="j")
screen.onkey(move_down, key="m")
screen.onkey(move_up, key="i")
screen.onkey(makedot, key="k")
screen.exitonclick()
