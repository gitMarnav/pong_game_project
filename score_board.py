from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Verdana', 40, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.up()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.l_score, False, align=ALIGNMENT,
                   font=FONT)
        self.goto(200, 200)
        self.write(self.r_score, False, align=ALIGNMENT,
                   font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over_l(self):

        self.goto(0, 0)
        self.write(
            f"\nGAME OVER\nL_Player Wins", align=ALIGNMENT, font=FONT)

    def game_over_r(self):

        self.goto(0, 0)
        self.write(
            f"\nGAME OVER\nR_Player Wins", align=ALIGNMENT, font=FONT)
