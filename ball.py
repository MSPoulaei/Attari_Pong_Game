from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.restart()
    def move(self):
        self.forward(4)
    def restart(self):
        self.home()
        twodirections=[randint(-45, 45),randint(135, 225)]
        self.setheading(twodirections[randint(0,1)])