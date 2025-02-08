from turtle import Turtle


FONT_ALIGN = 'center'
FONT = ("Courier", 15, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("highscore_data.txt", mode="r") as data:
            self.high_score = int(data.read())

        self.penup()
        self.hideturtle()
        self .goto(0, 270)
        self.color("white")
        self.write(f"Score = {self.score}   High Score = {self.high_score}", move= False, align=FONT_ALIGN, font=FONT)

    def update_highscore(self):
        with open("highscore_data.txt", mode="w") as data:
            data.write(f"{self.score}")
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}   High Score = {self.high_score} ", move= False, align=FONT_ALIGN, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.update_highscore()
            self.write(f"Game over\nNew Highscore {self.score}", move=False,
                       align='center', font=("Courier", 35, "bold"))
        else:
            self.write(f"Game over\nYour score is {self.score}", move=False,
                        align='center', font=("Courier", 35, "bold"))