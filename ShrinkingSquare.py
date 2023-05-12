import turtle

boarding_screen = turtle.Screen()
boarding_screen.title("Shrinking Squares")
boarding_screen.bgcolor("purple")

cursor = turtle.Turtle()
cursor.color("white")
cursor.speed(6)

def shrinkingsquare(size):
    for i in range(4):
        cursor.forward(size)
        cursor.left(90)
        size = size - 5

shrinkingsquare(150)
shrinkingsquare(130)
shrinkingsquare(100)
shrinkingsquare(70)
shrinkingsquare(40)
shrinkingsquare(20)
shrinkingsquare(5)
turtle.done()
