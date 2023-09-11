from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.line_table()

    def line_table(self):
        line = "|\n|\n|\n|\n|\n|\n|"
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write(line, align="center", font=("courier", 40, "normal"))
        self.goto(-0, -400)
        self.write(line, align="center", font=("courier", 40, "normal"))

    def update_score(self):
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))
        self.line_table()

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()
