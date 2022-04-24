from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(230, 360)
        self.write(arg=f"Points: {self.score}", align="center", font=("Segoe UI", 20, "normal"))

    def point(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()

    def negative_point(self):
        self.score -= 10
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg=f"Game Over", align="center", font=("Segoe UI", 50, "bold"))

    def game_won(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg=f"You win!!", align="center", font=("Segoe UI", 50, "bold"))

