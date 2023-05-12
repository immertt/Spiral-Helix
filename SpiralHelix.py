import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Helix")

colorList = ["red", "blue", "purple", "green", "yellow"]
cursor = turtle.Turtle()
cursor.speed(10)

for i in range(10):
    cursor.color(colorList[i % 5])
    cursor.circle(10 * i)
    cursor.circle(-10 * i)
    cursor.left(i)


turtle.done()