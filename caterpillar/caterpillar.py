import random
import turtle as t

t.bgcolor("yellow")
t.speed(0)
t.pensize(3)

caterpillar = t.Turtle()
caterpillar.shape("circle")
caterpillar.color("red")
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0), (13,2), (16,6), (18,18), (6,16), (2,13))
t.register_shape("leaf", leaf_shape)
leaf.shape('leaf')
leaf.color("green")
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
text_turtle = t.Turtle()
text_turtle.write("Нажми ПРОБЕЛ, чтобы начать игру", align="center", font=("Arial", 16, "bold"))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside

def game_over():
    caterpillar.color("yellow")
    leaf.color("yellow")
    t.penup()
    t.hideturtle()
    t.write("Игра окончена", align="center", font=("Arial", 30, "bold"))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score) + " очков", align="right", font=("Arial", 30, "bold"))

def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 1
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 0.5
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)


t.onkey(start_game, "space")
t.onkey(move_up, "Up")
t.onkey(move_down, "Down")
t.onkey(move_left, "Left")
t.onkey(move_right, "Right")
t.listen()
t.mainloop()