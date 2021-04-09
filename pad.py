from turtle import Turtle
class Pad(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(3,.5)
        self.speed("fastest")
    def up(self):
        self.goto(self.xcor(),self.ycor()+15)
        if self.ycor()>280 or self.ycor()<-280:
            self.undo()
    def down(self):
        self.goto(self.xcor(),self.ycor()-15)
        if self.ycor()>280 or self.ycor()<-280:
            self.undo()
