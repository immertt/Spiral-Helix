import turtle
import random

screen = turtle.Screen()
game_over = False
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
font_1 = ("Times New", 30, "normal")
score = 0


score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
grid_size = 10
turtle_list = []


x_coordinate = [-20, -10, 0, 10, 20]
y_coordinate = [-20, -10, 0, 10, 20]

def setup_score_turtle():
    score_turtle.color("blue")
    score_turtle.pensize(1)
    score_turtle.hideturtle()
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    score_turtle.goto(0, y)

    score_turtle.write(arg="Score: 0", move=False, align="center", font=font_1)

def make_turtle(x, y):

    t = turtle.Turtle()

    def show_score(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=font_1)

    t.onclick(show_score)
    t.shape("turtle")
    t.shapesize(1.8)
    t.penup()
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

def setup_make_turtles():
    for x in x_coordinate:
        for y in y_coordinate:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 350)
        #sonsuz döngü var bunun icin if kontrolu kullanmamız gerekiyor. Oyun bitince bu da bitmeli

def setup_countdown_turtle(time):
    global game_over
    countdown_turtle.color("red")
    countdown_turtle.pensize(1)
    countdown_turtle.hideturtle()
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.goto(0, y - 50)
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=font_1)
        screen.ontimer(lambda: setup_countdown_turtle(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=font_1)

turtle.tracer(0) #gecikme. animasyonları atlar

setup_score_turtle()
setup_make_turtles()
hide_turtles()
show_turtles_randomly()
setup_countdown_turtle(10)
turtle.tracer(1)   #gecikme. animasyonları atlar


turtle.mainloop()
