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

# define function to
# keep a check of index number
def Numbering(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def Coordinates(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# define function
# to make it interactive
# user click
def click(x, y):
    spot = Numbering(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
