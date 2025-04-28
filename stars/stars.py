import turtle as t
# from itertools import cycle
# from time import sleep
from random import randint, random

# colors = cycle(["red", "orange", "yellow", "green", "blue", "dark blue", "purple"])
# t.bgcolor("#0b0640")
t.speed("fast")

# size = 300
# points = 7
# angle = 720 / points * 2
# points_list = [5, 7, 9, 11, 13]


def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()

    for i in range(points):
        t.pencolor(col)
        t.forward(size)
        t.right(angle)

    t.end_fill()
    t.hideturtle()

    # sleep(5)


# while True:
#     points = next(cycle(points_list))
#     draw_star(points, 300, "yellow", 0, 0)



# основной код
t.Screen().bgcolor("#0b0640")

while True:
    rand_points = randint(2, 5) * 2 + 1
    rand_size = randint(10, 50)
    rand_color = (random(), random(), random())
    rand_x = randint(-350, 300)
    rand_y = randint(-250, 250)

    draw_star(rand_points, rand_size, rand_color, rand_x, rand_y)
