from turtle import Screen, Turtle
from tkinter import *

screen = Screen()
screen.setup(width=600, height=400)


def do_something():
    print("Good bye")
    Screen().bye()

canvas = screen.getcanvas()
button = Button(canvas.master, text="Exit Window", command=do_something, bg='light blue', height=2, width=30, font= ('Helvetica 10 bold italic'))

button.pack()
button.place(x=175, y=200)  # place the button anywhere on the screen


screen.exitonclick()
