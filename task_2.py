import turtle
import math

def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return
    
    turtle.forward(branch_length)

    position = turtle.position()
    heading = turtle.heading()

    turtle.left(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)

    turtle.penup()
    turtle.setposition(position)
    turtle.setheading(heading)
    turtle.pendown()

    turtle.right(45)

    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)

    turtle.penup()
    turtle.setposition(position)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.backward(branch_length)

if __name__ == "__main__":
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.setposition(0, -250)
    turtle.pendown()

    n = int(input("Enter level recurtion(exsample: 6): "))

    draw_pythagoras_tree(100, n)

    turtle.done()