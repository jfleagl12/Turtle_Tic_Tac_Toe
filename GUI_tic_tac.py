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

# This function draws the grid the game will be played on
def drawBoard():
    # Draw both of the horizontal lines, starting from different heights
    for i in range(2):
        drawer.penup()
        drawer.goto(-300,100-200 * i)
        drawer.pendown()
        drawer.forward(600)

    # Update the screen with new changes
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
