from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", encoding="utf8") as data:
            self.high_score = data.read()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        with open("data.txt", mode="w", encoding="utf8") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
