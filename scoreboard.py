from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, block_num: int):
        super().__init__()
        self.block_num = block_num
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 350)
        self.write('Scores = ', align='center', font=('Courier', 30, 'normal'))
        self.goto(-50, 350)
        self.write(f"{self.score}/{self.block_num}", align="center", font=("Courier", 30, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()
