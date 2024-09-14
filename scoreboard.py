from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 13, 'normal')

# Default HighScore initialization to the .txt file


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open('score.txt') as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.pu()
        self.color("white")
        self.goto(0, 230)       # 270 FOR SCREEN @600X600
        self.write(arg=f"Score : {self.score}       High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

        # Updating the highscore in the database
        with open('score.txt', mode='w') as file:
            file.write(str(self.high_score))

        self.score = 0
        self.update_score()

    def update(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}       High Score : {self.high_score}", align=ALIGNMENT, font=FONT)
