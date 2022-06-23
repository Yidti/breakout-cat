from turtle import Turtle
import turtle
import numpy as np

turtle.colormode(255)


class Block(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__(shape='square')
        self.color(tuple(np.random.choice(range(50, 256), size=3)))
        self.shapesize(0.5, 3)
        self.penup()
        self.goto(xpos, ypos)
