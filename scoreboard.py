from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",10,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.score1=0
        self.score2=0
        self.update()
    def update(self):
        self.clear()
        self.write(f"{self.score1}      {self.score2}",align=ALIGNMENT,font=FONT)
    def pad1_scores(self):
        self.score1+=1
        self.update()
    def pad2_scores(self):
        self.score2+=1
        self.update()
    def winner_check(self,end_point):
        if self.score1==end_point:
            self.home()
            self.write(f"Player 1 is Winner", align=ALIGNMENT, font=FONT)
            return True
        elif self.score2==end_point:
            self.home()
            self.write(f"Player 2 is Winner", align=ALIGNMENT, font=FONT)
            return True
        return False