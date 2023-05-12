import turtle

screen = turtle.Screen()
screen.title("Hexagon")
screen.bgcolor("red")

cursor = turtle.Turtle()

num_sides = 6
angle = 360 / num_sides
side_length = 150

for num in range(num_sides):
    cursor.right(angle)
    cursor.forward(side_length)

turtle.done()