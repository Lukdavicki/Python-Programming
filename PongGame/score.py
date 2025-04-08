from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, move=True, align="left", font=('Arial', 50, 'normal'))
        self.goto(150, 200)
        self.write(self.r_score, move=True, align="left", font=('Arial', 50, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
