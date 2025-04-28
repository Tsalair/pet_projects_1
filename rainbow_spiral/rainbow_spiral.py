import turtle
from itertools import cycle

colors = cycle(["red", "orange", "yellow", "green", "blue", "dark blue", "purple"])

turtle.bgcolor("black")
turtle.speed("fast")
turtle.pensize(10)


def draw_circle(size, angle, shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    size += 10
    draw_circle(size, angle + 1, shift + 1)


draw_circle(30, 15, 10)
