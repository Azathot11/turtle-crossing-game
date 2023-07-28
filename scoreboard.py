from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()
        self.get_highestScore()

    def get_highestScore(self):
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.goto(200, 250)
        self.write(f"High Score: {self.high_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))

    def game_over(self):
        self.high_score = self.score
        self.goto(0, 0)
        self.write(f"GAME OVER Your score is {self.score}", align="center", font=FONT)
        self.score = 0
