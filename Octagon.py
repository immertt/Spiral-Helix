import turtle

screen = turtle.Screen()

screen.bgcolor("orange")
screen.title("Octagon")

cursor = turtle.Turtle()

num_sides = 8
side_length = 100
angle = 360 / num_sides

for num in range(num_sides):
    cursor.right(angle)
    cursor.forward(side_length)

turtle.done()