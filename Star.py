import turtle

screen = turtle.Screen()

screen.bgcolor("light blue")
screen.title("Star")

cursor = turtle.Turtle()

num_sides = 5
angle = 360 / num_sides * 2
side_length = 200

for num in range(num_sides):
    cursor.right(angle)
    cursor.forward(side_length)

turtle.done()
