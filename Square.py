import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("Light blue")
drawing_board.title("Sqaure")

cursor_1 = turtle.Turtle()

for cursor in range(4):
    cursor_1.forward(200)
    cursor_1.left(90)

'''
cursor = turtle.Turtle()
cursor.forward(200)
cursor.right(90)
cursor.forward(200)
cursor.right(90)
cursor.forward(200)
cursor.right(90)
cursor.forward(200)
'''

turtle.done()

