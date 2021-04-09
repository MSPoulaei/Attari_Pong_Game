from pad import Pad
from turtle import Screen
screen=Screen()
screen.setup(600,600)
screen.title("Pong Game")
screen.bgcolor("black")


pad1=Pad()
pad1.goto(-280,0)
pad2=Pad()
pad2.goto(280,0)
screen.listen()
screen.onkey(pad1.up,"w")
screen.onkey(pad1.down,"s")
screen.onkey(pad2.up,"Up")
screen.onkey(pad2.down,"Down")




screen.exitonclick()