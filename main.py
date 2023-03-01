# import modules
from random import *
from turtle import *

# set the screen
screen = Screen()

# choose background color
screen.bgcolor("yellow")


# define the function
# for creating a square section
# for the game
def Square(x, y):
    up()
    goto(x, y)
    down()
    color('white', 'green')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

