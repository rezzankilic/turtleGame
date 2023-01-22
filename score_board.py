from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(0, 220)
        self.penup()



    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_score()


    def game_over(self):
        self.clear()
        self.write("Game Over", align=ALIGNMENT, font=FONT)