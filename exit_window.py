from turtle import Screen
from tkinter import *

# CURSOR_SIZE = 20
# FONT_SIZE = 12
# FONT = ('Arial', FONT_SIZE, 'bold')

screen = Screen()
screen.setup(width=600, height=400)


def do_something():
    print("Good bye")
    Screen().bye()

canvas = screen.getcanvas()
button = Button(canvas.master, text="Exit", command=do_something)

button.pack()
button.place(x=300, y=250)  # place the button anywhere on the screen


# button.sety(150 + CURSOR_SIZE + FONT_SIZE)


screen.exitonclick()
