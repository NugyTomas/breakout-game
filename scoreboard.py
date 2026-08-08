from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, dimension):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.current_score = 0
        self.record = self.get_current_record()
        self.lives = 3
        self.level = 1

        self.scoreboard_y = dimension.scoreboard_y
        self.high_score_y = dimension.high_score_y
        self.scoreboard_left_x = dimension.scoreboard_left_x
        self.scoreboard_right_x = dimension.scoreboard_right_x
        self.font_size = dimension.scoreboard_font_size

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.goto(self.scoreboard_left_x, self.scoreboard_y)
        self.write(f"Level: {self.level}", align="left", font=("Courier", self.font_size, "normal"))

        self.goto(0, self.scoreboard_y)
        self.write(f"Score: {self.current_score}", align="center", font=("Courier", int(self.font_size*1.3), "bold"))

        self.goto(0, self.high_score_y)
        self.write(f"High score: {self.record}", align="center", font=("Courier", self.font_size, "normal"))

        self.goto(self.scoreboard_right_x, self.scoreboard_y)
        self.write(f"Lives: {'🤍' * self.lives}", align="right", font=("Courier", self.font_size, "normal"))

    def write_new_record(self):
        self.record = self.current_score

        with open("record.txt", "w") as file:
            file.write(str(self.current_score))

        self.update_scoreboard()

    @staticmethod
    def get_current_record():
        try:
            with open("record.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def reset(self):
        self.current_score = 0
        self.level = 1
        self.lives = 3
        self.record = self.get_current_record()
        self.update_scoreboard()