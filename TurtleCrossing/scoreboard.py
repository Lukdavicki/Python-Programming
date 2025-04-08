from turtle import Turtle

FONT = ("Courier", 24, "normal")


# // write score, write game over on fail


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)

    def show_score(self):
        self.write(f"LEVEL: {self.score}", False, "center", FONT)
        self.color("black")

    def level_update(self):
        self.clear()
        self.score += 1
        print(self.score)

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"GAME OVER!💀", False, "center", FONT)