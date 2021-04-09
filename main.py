from turtle import Screen
from ball import Ball
from pad import Pad
from time import sleep
from random import randint
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
end_point=3
# pad init
pad1 = Pad()
pad1.goto(-280, 0)
pad2 = Pad()
pad2.goto(280, 0)
ball = Ball()
scoreboard = ScoreBoard()
# controls
screen.listen()
screen.onkey(pad1.up, "w")
screen.onkey(pad1.down, "s")
screen.onkey(pad2.up, "Up")
screen.onkey(pad2.down, "Down")

# main game while loop
game_is_over = False
while not game_is_over:
    sleep(.01)
    ball.move()
    if ball.xcor() > 295:
        scoreboard.pad1_scores()
        ball.restart()
    elif ball.xcor() < -295:
        scoreboard.pad2_scores()
        ball.restart()
    elif pad1.distance(ball) < 30:
        ball.setheading(randint(-45, 45))
    elif pad2.distance(ball) < 30:
        ball.setheading(randint(135, 225))
    elif ball.ycor() > 290 or ball.ycor() < -290:
        ball.setheading(360 - ball.heading())

    if scoreboard.winner_check(end_point):
        game_is_over=True
        ball.hideturtle()
    screen.update()
screen.exitonclick()
