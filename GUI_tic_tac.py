# PROJECT STEPS:
# Here are the steps we will follow to build the game.
# 1. Create a turtle and a function that draws the background.
# 2. Create a function that draws an x and a function that dras an o.
# 3. Create event listeners.
# 4. Create a representation of the bord in the code.
# 5. Create a turtle to give announcements to the play, and set it in the correct place to check if x won.
# 6. Create a function to check if someone has won, and use it in the correct place to check if x won.
# 7. Create a function to pick a place for the computer to put an o.
# 8. Check if o won.
# 9. Create a fuction to check for a tie.

import turtle
import math

# This function draws the grid the game will be played on
def drawBoard():
    # Draw both of the horizontal lines, starting from different heights
    for i in range(2):
        drawer.penup()
        drawer.goto(-300,100-200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    # Draw both of the vertical lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-100+200 *i, 300)
        drawer.pendown()
        drawer.forward(600)

    # Add numbers to the top corner of each square
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280-i * 200)
            drawer.pendown()

            drawer.write(num, font = ("Arial", 12))
            num += 1


    # Update the screen with new changes
    screen.update()

# This function draws an "x" centered at the inputted coordinates
def drawX(x,y):
    # Move to the correct spot
    drawer.penup()
    drawer.goto(x,y)
    drawer.pendown()

    drawer.setheading(60)

    # Draw the lines of the x
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)

    # Update the screen
    screen.update()

# This function draws an "o" centered at the inputted coordinates
def drawO(x,y):
    # Move to the correct spot
    drawer.penup()
    drawer.goto(x,y + 75)
    drawer.pendown()

    drawer.setheading(0)

    # Draw a circle with the correct size
    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)

    # Update the screen
    screen.update()

# Create turtle
drawer = turtle.Turtle()

drawer.pensize(10)
drawer.ht()

# Create screen
screen = turtle.Screen()
screen.tracer(0)

# Draw the board
drawBoard()

drawO(0,0)
