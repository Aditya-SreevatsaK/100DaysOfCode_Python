from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Score: {self.left_score}", align="center", font=("Courier", 20, "bold"))
        self.goto(100, 260)
        self.write(f"Score: {self.right_score}", align="center", font=("Courier", 20, "bold"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
